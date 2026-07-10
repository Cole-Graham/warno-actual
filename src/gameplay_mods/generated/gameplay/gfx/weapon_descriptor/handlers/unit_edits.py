import re
from typing import Any, Dict, List, Tuple

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.replace_schema import normalize_replace
from src.constants.weapons import LIGHT_AT_AMMO
from src.constants.weapons import ammunitions as ammos
from src.constants.weapons import missiles

# Damage families that mark a missile as the "anti-helo" half of a HAGRU pair.
# Any ammo declaring one of these families gets a paired ``_HAGRU`` variant
# attached when the parent weapon is mounted on a unit.
TBAGRU_FAMILIES = frozenset({
    "DamageFamily_manpad_tbagru",
    "DamageFamily_sam_tbagru",
    "DamageFamily_a2a_tbagru",
})

_MOUNTED_AMMO_SUFFIX_RE = re.compile(r"(_x\d+|_salvolength\d+|_infmagazine\d+)$")


def _mounted_ammo_base_name(ammo_name: str) -> str:
    """Strip mount suffixes for name lookup; does not change suffix semantics."""
    return _MOUNTED_AMMO_SUFFIX_RE.sub("", ammo_name)


def _ammo_dict_category(weapon_name: str) -> str | None:
    base_name = _mounted_ammo_base_name(weapon_name)
    for (name, category, _, _), _ in ammos.items():
        if _mounted_ammo_base_name(name) == base_name:
            return category
    return None


def _replacement_mount_suffix(
    full_ammo_name: str,
    new_weapon: str,
    quantity: int,
) -> str:
    """Return a mount-path suffix for ``equipmentchanges.replace``.

    Only preserves suffixes already present on the donor mount (or ``_x`` derived
    from ``NbWeapons`` for ``small_arms`` when the path is bare). Never
    synthesizes ``_salvolength`` / ``_infmagazine`` — those suffixes belong on
    the donor path when the mounted ammo uses magazine/salvo-length descriptors.

    Magazine suffixes from the donor are preserved for non-``small_arms`` targets
    (vehicle SAM/ATGM, infantry AT/AA, etc.). They are never copied onto
    ``small_arms`` / MMG mounts (those use ``_x`` / strength instead).
    """
    if re.search(r"(_salvolength\d+|_infmagazine\d+)$", new_weapon):
        return ""

    magazine_match = re.search(r"(_salvolength|_infmagazine)(\d+)$", full_ammo_name)
    if magazine_match and _ammo_dict_category(new_weapon) != "small_arms":
        return f"{magazine_match.group(1)}{magazine_match.group(2)}"

    if _ammo_dict_category(new_weapon) != "small_arms":
        return ""

    x_match = re.search(r"_x(\d+)$", full_ammo_name)
    if x_match:
        return f"_x{x_match.group(1)}"

    if quantity > 1:
        return f"_x{quantity}"
    return ""


def _effective_helo_range(base_ammo_name: str, ammo_name: str, ammo_db: Dict[str, Any]) -> int | None:
    """Return effective MaximumRangeHelicopterGRU for ``base_ammo_name``.

    Prefers the ``missiles`` dict override (``Ammunition.parent_membr``), then
    falls back to the vanilla value in ``ammo_db['ammo_properties']``. Tries
    both the bare ammo namespace and the salvo-suffixed namespace because
    vanilla often only exposes the salvo variant (e.g. ``Ammo_SAM_Strela10_x4``).
    Returns ``None`` if no value can be resolved.
    """
    for (name, _, _, _), data in missiles.items():
        if name != base_ammo_name or not isinstance(data, dict):
            continue
        ammunition = data.get("Ammunition") if isinstance(data, dict) else None
        if not isinstance(ammunition, dict):
            break
        parent = ammunition.get("parent_membr") or {}
        if "MaximumRangeHelicopterGRU" in parent:
            try:
                return int(parent["MaximumRangeHelicopterGRU"])
            except (TypeError, ValueError):
                break
        break

    ammo_props = ammo_db.get("ammo_properties", {})
    for key in (f"Ammo_{base_ammo_name}", f"Ammo_{ammo_name}"):
        entry = ammo_props.get(key)
        if entry and entry.get("MaximumRangeHelicopterGRU") is not None:
            try:
                return int(entry["MaximumRangeHelicopterGRU"])
            except (TypeError, ValueError):
                continue
    return None

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import (
    is_obj_type,
    is_valid_turret,
    strip_quotes,
)

from .new_units import _should_use_strength_variant, _uses_sniper_damage_family, UNITS_SKIP_STRENGTH_VARIANTS

logger = setup_logger(__name__)

def unit_edits_weapondescriptor(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Unit Edits for WeaponDescriptor.ndf file."""
    ammo_db = game_db["ammunition"]
    unit_db = game_db["unit_data"]
    weapon_db = game_db["weapons"]

    unit_edits = load_unit_edits()

    for unit, edits in unit_edits.items():
        weapon_descr_name = f"WeaponDescriptor_{unit}"
        weapon_descr = source_path.by_namespace(weapon_descr_name, strict=False)

        if weapon_descr:
            _adjust_light_at_salvos(weapon_descr, unit, ammos, ammo_db, unit_db, weapon_db)
        if "WeaponDescriptor" not in edits:
            continue

        weapon_descr_name = f"WeaponDescriptor_{unit}"
        if weapon_descr_name not in weapon_db:
            logger.warning(f"No weapon data found for {unit}")
            continue
        weapon_descr_data = weapon_db[weapon_descr_name]

        # Gather templates for this specific unit's equipment changes
        insert_templates = game_db.get("insert_turret_templates", {})
        turret_templates = _gather_turret_templates(
            source_path, unit, edits, ammo_db, weapon_db, insert_templates,
        )

        if weapon_descr:
            _apply_weapon_edits(
                weapon_descr,
                edits,
                edits["WeaponDescriptor"],
                weapon_descr_data,
                turret_templates,
                game_db,
                source_path,
            )

            # _adjust_light_at_salvos(weapon_descr, unit, ammos,
            #                         ammo_db, unit_db, weapon_db)


    # Add HAGRU missiles to TBAGRU-family weapons (MANPAD / SAM / A2A).
    # Runs after all per-unit edits so live descriptors already reflect
    # turret removals, re-indexing, equipmentchanges.replace, and any
    # MountedWeapons overrides.  The clone therefore inherits the donor's
    # final AmmoBoxIndex / HandheldEquipmentKey / *PropertyName values.
    for weapon_descr in source_path:
        if not weapon_descr.namespace.startswith("WeaponDescriptor_"):
            continue

        turret_list = weapon_descr.v.by_m("TurretDescriptorList")
        for turret in turret_list.v:
            if not is_valid_turret(turret.v):
                continue

            mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
            wpns_to_add = []

            for weapon in mounted_wpns.v:
                if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                    continue

                ammo_path = weapon.v.by_m("Ammunition").v
                if not ammo_path.startswith("$/GFX/Weapon/Ammo_"):
                    continue
                ammo_name = ammo_path[len("$/GFX/Weapon/Ammo_"):]

                # Strip _x{N} / _salvolength{N} / _infmagazine{N} for missiles-dict lookup
                base_ammo_name = _mounted_ammo_base_name(ammo_name)

                # Salvo length: prefer explicit suffix, else current NbWeapons
                salvo_match = re.search(r"(_salvolength|_infmagazine)(\d+)$", ammo_name)
                if salvo_match:
                    salvo_length = int(salvo_match.group(2))
                    salvo_kind = salvo_match.group(1)
                else:
                    salvo_kind = "_salvolength"
                    try:
                        salvo_length = int(weapon.v.by_m("NbWeapons").v)
                    except Exception:
                        salvo_length = 1

                # Is the (post-edit) ammo a TBAGRU family member?
                for (missile_name, _, _, _), missile_data in missiles.items():
                    if (
                        missile_name == base_ammo_name
                        and "Ammunition" in missile_data
                        and missile_data["Ammunition"].get("Arme", {}).get("Family") in TBAGRU_FAMILIES
                    ):
                        # Skip when the base has no helo engagement range
                        helo_range = _effective_helo_range(base_ammo_name, ammo_name, ammo_db)
                        if helo_range == 0:
                            logger.debug(
                                f"Skipping HAGRU attachment for {base_ammo_name} on "
                                f"{weapon_descr.namespace}: helo range is 0",
                            )
                            break

                        # Determine whether to use a salvo/magazine variant of the HAGRU
                        hagru_name = f"{base_ammo_name}_HAGRU"
                        # Preserve infantry magazine / existing salvolength suffix from donor mount
                        if salvo_match:
                            use_salvo_variant = salvo_length > 1
                            suffix_kind = salvo_kind  # "_salvolength" or "_infmagazine"
                        else:
                            suffix_kind = "_salvolength"
                            hagru_salvo_lengths = None
                            for (hagru_missile_name, _, _, _), hagru_data in missiles.items():
                                if hagru_missile_name == hagru_name and "WeaponDescriptor" in hagru_data:
                                    hagru_salvo_lengths = hagru_data["WeaponDescriptor"].get("SalvoLengths")
                                    break

                            if hagru_salvo_lengths is None:
                                use_salvo_variant = False
                            elif salvo_length in hagru_salvo_lengths:
                                use_salvo_variant = salvo_length > 1
                            elif 1 in hagru_salvo_lengths:
                                use_salvo_variant = False
                            else:
                                salvo_length = hagru_salvo_lengths[0]
                                use_salvo_variant = True

                        # Clone the live mount (inherits final indices / keys)
                        new_wpn = weapon.copy()
                        if use_salvo_variant:
                            new_ammo = (
                                f"$/GFX/Weapon/Ammo_{base_ammo_name}_HAGRU"
                                f"{suffix_kind}{salvo_length}"
                            )
                        else:
                            new_ammo = f"$/GFX/Weapon/Ammo_{base_ammo_name}_HAGRU"
                        new_wpn.v.by_m("Ammunition").v = new_ammo
                        wpns_to_add.append(new_wpn)
                        logger.debug(
                            f"Adding HAGRU missile {base_ammo_name}_HAGRU to {weapon_descr.namespace}"
                        )
                        break  # only one HAGRU per donor

            for new_wpn in wpns_to_add:
                mounted_wpns.v.add(new_wpn)


def _gather_turret_templates(
    source_path: Any,
    unit: str,
    edits: Dict,
    ammo_db: Dict[str, Any],
    weapon_db: Dict[str, Any],
    insert_templates: Dict[str, str] | None = None,
) -> List[Tuple[str, Any]]:
    """Gather turret templates for equipment changes.

    Uses precomputed insert_turret_templates (from vanilla) only. No fallback to
    source_path, since patched donors are unreliable.
    """
    turret_objects = []
    weapons_to_add = []
    insert_templates = insert_templates or {}

    equipment_changes = edits["WeaponDescriptor"].get("equipmentchanges", {})
    weapon_list = equipment_changes.get("insert")
    if not weapon_list:
        return []

    weapon_descr_name = f"WeaponDescriptor_{unit}"
    if not weapon_db or weapon_descr_name not in weapon_db:
        logger.warning(f"Weapon {weapon_descr_name} not found in database")
        return []

    turret_objects.extend(
        _find_turret_templates(weapon_list, weapons_to_add, insert_templates),
    )

    logger.debug(f"Found templates for weapons: {weapons_to_add}")
    return turret_objects


def _find_turret_templates(
    add_list: List,
    weapons_to_add: List,
    insert_templates: Dict[str, str],
) -> List[Tuple[str, Any]]:
    """Find turret templates matching the add list.

    Uses insert_turret_templates (vanilla) only. No fallback to source_path.
    """
    templates = []
    processed_weapons = set()

    def add_turret_from_template(template_str: str, weapon_name: str, index: int) -> bool:
        try:
            parsed = ndf.convert(template_str)
            if parsed and len(parsed) > 0:
                turret_row = parsed[0]
                new_turret = _prepare_turret_template(turret_row, index)
                weapons_to_add.append(weapon_name)
                templates.append((weapon_name, new_turret))
                return True
        except Exception as e:
            logger.warning(f"Failed to parse insert template for {weapon_name}: {e}")
        return False

    for index_to_insert, ammo_name in add_list:
        if ammo_name in processed_weapons:
            continue

        if ammo_name not in insert_templates:
            logger.warning(f"No insert template in database for {ammo_name}, skipping")
            continue

        if add_turret_from_template(insert_templates[ammo_name], ammo_name, index_to_insert):
            processed_weapons.add(ammo_name)
            logger.debug(f"Using insert template for {ammo_name}")
        else:
            logger.warning(f"Could not add turret from template for {ammo_name}")

    return templates


def _prepare_turret_template(turret: Any, index: int) -> Any:
    """Prepare a turret template with updated indices."""
    new_turret = turret.copy()

    # Update weapon indices
    mounted_wpns = new_turret.v.by_m("MountedWeaponDescriptorList")
    for weapon in mounted_wpns.v:
        weapon.v.by_m("AmmoBoxIndex").v = str(index)

    # Update turret bone index
    new_yul_bone = index + 1
    new_turret.v.by_m("YulBoneOrdinal").v = str(new_yul_bone)
    return new_turret


def _insert_new_weapons(weapon_descr: Any, wd_edits: Dict, turret_templates: List[Tuple[str, Any]], game_db: Dict) -> None:
    """Insert new weapons at specific indices in the descriptor.
    
    Similar to _add_new_weapons but inserts turrets in reverse order (highest index first)
    to maintain correct positions when inserting multiple turrets.
    """
    equipment_changes = wd_edits["equipmentchanges"]
    ammo_db = game_db["ammunition"]
    unit_db = game_db["unit_data"]
    unit_edits = load_unit_edits()
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    insert_list = equipment_changes["insert"]

    # Get unit name and check if it's infantry
    unit_name = weapon_descr.namespace.replace("WeaponDescriptor_", "")
    is_infantry = False
    unit_strength = None

    # Check unit edits first
    if unit_name in unit_edits:
        unit_edit_data = unit_edits[unit_name]
        if unit_edit_data.get("UnitRole") == "infantry" or "Infanterie" in unit_edit_data.get("TagSet", {}).get("overwrite_all", []):
            is_infantry = True
        unit_strength = unit_edit_data.get("strength")
    
    # Check unit database if not found in edits or to verify infantry status
    if unit_name in unit_db:
        unit_data = unit_db[unit_name]
        if unit_data.get("unit_role") == "infantry" or "Infanterie" in unit_data.get("tags", []):
            is_infantry = True
        if not unit_strength:
            unit_strength = unit_data.get("strength")

    def _is_infantry_small_arm(weapon_name: str, game_db: Dict) -> bool:
        """Check if a weapon is an infantry small arm by checking if it has a valid caliber token."""
        # Check if weapon should use strength variant (indicates it's a small arm with caliber)
        if _should_use_strength_variant(weapon_name, game_db):
            return True
        return False

    def _apply_insert_edits(turret_template, turret_index, weapon_name):
        if "insert_edits" in equipment_changes:
            insert_edits = equipment_changes["insert_edits"].get(turret_index)
            if not insert_edits:
                return
            if "turret_edits" in insert_edits:
                for membr, value in insert_edits["turret_edits"].items():
                    turret_template.v.by_m(membr).v = str(value)
            mounted_weapons = turret_template.v.by_m("MountedWeaponDescriptorList")
            for mounted_weapon in mounted_weapons.v:
                for membr, value in insert_edits.items():
                    if membr == "turret_edits":
                        continue
                    if isinstance(value, (bool, int, float, str)):
                        mounted_weapon.v.by_m(membr).v = str(value)
                    elif isinstance(value, list):
                        ndf_list = ndf.model.List()
                        for item in value:
                            ndf_list.add(f"'{item}'")
                        mounted_weapon.v.by_m(membr).v = ndf_list
                
                # Apply strength and quantity variants for infantry small arms
                if is_infantry and unit_strength:
                    current_ammo = mounted_weapon.v.by_m("Ammunition").v
                    # Extract base ammo name (remove $/GFX/Weapon/Ammo_ prefix and any existing variants)
                    if current_ammo.startswith("$/GFX/Weapon/Ammo_"):
                        base_ammo = current_ammo.split("$/GFX/Weapon/Ammo_", 1)[1]
                        # Strip any existing strength or quantity suffixes
                        base_ammo = re.sub(r"(?:_strength\d+)?(?:_x\d{1,2})?$", "", base_ammo)
                        
                        # Check if this is an infantry small arm
                        if _is_infantry_small_arm(base_ammo, game_db):
                            quantity = int(mounted_weapon.v.by_m("NbWeapons").v)
                            prefix = "$/GFX/Weapon/Ammo_"
                            
                            if quantity > 1:
                                new_ammo = f"{prefix}{base_ammo}_strength{unit_strength}_x{quantity}"
                            else:
                                new_ammo = f"{prefix}{base_ammo}_strength{unit_strength}"
                            
                            mounted_weapon.v.by_m("Ammunition").v = new_ammo
                            logger.debug(f"Applied strength variant for infantry small arm {base_ammo}: {new_ammo}")

    # Sort insert_list by index in descending order to insert highest indices first
    # This ensures that when inserting multiple turrets, later insertions don't affect earlier ones
    sorted_insert_list = sorted(insert_list, key=lambda x: x[0], reverse=True)

    for ammo_name, turret_template in turret_templates:
        for turret_index, weapon_name in sorted_insert_list:
            old_name = ammo_db["renames_new_old"].get(weapon_name, None)
            if (old_name and old_name == ammo_name) or weapon_name == ammo_name:
                # Update AmmoBoxIndex to match the insert position
                mounted_weapons = turret_template.v.by_m("MountedWeaponDescriptorList")
                for mounted_weapon in mounted_weapons.v:
                    mounted_weapon.v.by_m("AmmoBoxIndex").v = str(turret_index)
                
                _apply_insert_edits(turret_template, turret_index, weapon_name)
                logger.debug(f"Inserting {ammo_name} at index {turret_index}")
                turret_list.insert(turret_index, turret_template)
                break  # Only insert once per template

    # Apply insert_edits to all turrets at the specified indices (both newly inserted and bumped)
    # The edit_index already accounts for any index bumping
    if "insert_edits" in equipment_changes:
        insert_edits = equipment_changes["insert_edits"]
        for edit_index, edits in insert_edits.items():
            if edit_index < len(turret_list):
                turret = turret_list[edit_index]
                if not is_valid_turret(turret.v):
                    continue
                
                # Apply turret edits
                if "turret_edits" in edits:
                    for membr, value in edits["turret_edits"].items():
                        turret.v.by_m(membr).v = str(value)
                
                # Apply mounted weapon edits
                mounted_weapons = turret.v.by_m("MountedWeaponDescriptorList")
                for mounted_weapon in mounted_weapons.v:
                    for membr, value in edits.items():
                        if membr == "turret_edits":
                            continue
                        if isinstance(value, (bool, int, float, str)):
                            mounted_weapon.v.by_m(membr).v = str(value)
                        elif isinstance(value, list):
                            ndf_list = ndf.model.List()
                            for item in value:
                                ndf_list.add(f"'{item}'")
                            mounted_weapon.v.by_m(membr).v = ndf_list
                
                logger.debug(f"Applied insert_edits to turret at index {edit_index}")


def _update_weapon_quantities(
    source_path: Any,
    unit_name: str,
    unit_edits: Dict[str, Any],
    equipment_changes: Dict[str, Any],
    game_db: Dict[str, Any],
) -> None:
    """Update weapon quantities for a unit."""
    weapon_db = game_db["weapons"]
    ammo_db = game_db["ammunition"]

    # Get unit strength
    unit_strength = None
    if "strength" in unit_edits:
        unit_strength = unit_edits["strength"]
    elif unit_name in game_db["unit_data"]:
        unit_strength = game_db["unit_data"][unit_name].get("strength")

    if not unit_strength:
        logger.warning(f"No strength found for unit {unit_name}")
        return

    weapon_descr = source_path.by_n(f"WeaponDescriptor_{unit_name}")
    if not weapon_descr:
        logger.warning(f"No weapon descriptor found for {unit_name}")
        return

    for turret in weapon_descr.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(turret.v):
            continue

        for weapon_descr_row in turret.v.by_member("MountedWeaponDescriptorList").v:
            if not isinstance(weapon_descr_row.v, ndf.model.Object):
                continue

            current_ammo = weapon_descr_row.v.by_member("Ammunition").v
            ammo_name = current_ammo.split("_", 1)[1]  # Remove $/GFX/Weapon/Ammo_ prefix

            # Strip any existing strength or quantity suffixes
            base_ammo = re.sub(r"(?:_strength\d+)?(?:_x\d{1,2})?$", "", ammo_name)

            # Check if this weapon has quantity changes
            animate_edits = equipment_changes.get("animate", {})
            quantity_edits = equipment_changes.get("quantity", {})            
            if base_ammo in animate_edits:
                animate_only_one_soldier = animate_edits[base_ammo]
                weapon_descr_row.v.by_m("AnimateOnlyOneSoldier").v = str(animate_only_one_soldier)

            if base_ammo in quantity_edits:
                quantity = quantity_edits[base_ammo]
                weapon_descr_row.v.by_m("NbWeapons").v = str(quantity)

                is_flamethrower = game_db["ammunition"]["ammo_properties"].get(
                    f"Ammo_{base_ammo}", {},
                ).get("MinMaxCategory") == "MinMax_FLAME"

                if not is_flamethrower:
                    # Update ammo name with quantity and strength if needed
                    prefix = current_ammo.split("_", 1)[0]

                    # Skip strength variant generation for specific units
                    use_strength_variant = _should_use_strength_variant(base_ammo, game_db) and (unit_name not in UNITS_SKIP_STRENGTH_VARIANTS)

                    if use_strength_variant:
                        if quantity > 1:
                            new_ammo = f"{prefix}_{base_ammo}_strength{unit_strength}_x{quantity}"
                        else:
                            new_ammo = f"{prefix}_{base_ammo}_strength{unit_strength}"
                    else:
                        if quantity > 1 and not _uses_sniper_damage_family(base_ammo, game_db):
                            new_ammo = f"{prefix}_{base_ammo}_x{quantity}"
                        else:
                            new_ammo = f"{prefix}_{base_ammo}"

                    weapon_descr_row.v.by_m("Ammunition").v = new_ammo

                logger.debug(f"Updated quantity for {base_ammo} to {quantity} in {unit_name}")


def _apply_weapon_edits(
    weapon_descr: Any,
    unit_edits: Dict,
    wd_edits: Dict,
    weapon_descr_data: Dict,
    turret_templates: List[Tuple[str, Any]],
    game_db: Dict,
    source_path: Any,
) -> None:
    """Apply weapon edits using database data."""

    # Handle salvo changes first to prevent index errors when editing salves
    if "Salves" in wd_edits:
        _apply_salvo_changes(weapon_descr, wd_edits, weapon_descr_data, game_db)

    # Handle turret changes
    if "turrets" in wd_edits:
        _apply_turret_changes(
            weapon_descr,
            wd_edits["turrets"],
            weapon_descr_data,
            game_db,
            wd_edits,
            source_path,
        )

    # Handle equipment changes
    if "equipmentchanges" in wd_edits:
        _apply_equipment_changes(
            weapon_descr,
            unit_edits,
            wd_edits,
            weapon_descr_data,
            turret_templates,
            game_db,
            source_path,
        )
    
    if "SalvoIsMainSalvo" in wd_edits:
        weapon_descr.v.by_m("SalvoIsMainSalvo").v = ndf.convert(str(wd_edits["SalvoIsMainSalvo"]))


def _find_donor_weapon(
    donor_ammo: str,
    weapon_db: Dict,
    source_path: Any,
    ammo_db: Dict,
    prefix: str,
) -> Any:
    """Find a weapon to use as donor from any weapon descriptor that has it (uses precomputed weapon_db)."""
    renames = ammo_db.get("renames_new_old", {})
    for lookup_name in [donor_ammo, renames.get(donor_ammo)]:
        if not lookup_name:
            continue
        for descr_name, descr_data in weapon_db.items():
            if lookup_name not in descr_data.get("weapon_locations", {}):
                continue
            donor_descr = source_path.by_namespace(descr_name, strict=False)
            if not donor_descr:
                continue
            for loc in descr_data["weapon_locations"][lookup_name]:
                turret = donor_descr.v.by_m("TurretDescriptorList").v[loc["turret_index"]]
                if not is_valid_turret(turret.v):
                    continue
                for w in turret.v.by_m("MountedWeaponDescriptorList").v:
                    if not is_obj_type(w.v, "TMountedWeaponDescriptor"):
                        continue
                    ammo = w.v.by_m("Ammunition").v.split(prefix)[1]
                    if ammo == lookup_name or ammo == donor_ammo or renames.get(ammo) == donor_ammo:
                        return w.copy()
    return None


def _apply_turret_changes(
    weapon_descr: Any,
    turrets_edits: Dict,
    weapon_descr_data: Dict,
    game_db: Dict,
    wd_edits: Dict = None,
    source_path: Any = None,
) -> None:
    """Apply turret changes using database data."""
    turret_data = weapon_descr_data["turrets"]
    ammo_db = game_db["ammunition"]
    weapon_db = game_db.get("weapons", {})
    
    # Build a mapping of replacements: new_weapon -> old_weapon
    replacement_map = {}
    if wd_edits and "equipmentchanges" in wd_edits:
        equipment_changes = wd_edits["equipmentchanges"]
        for spec in normalize_replace(equipment_changes.get("replace")):
            replacement_map[spec.new_weapon] = spec.old_weapon

    for turret_index, turret_edits in turrets_edits.items():
        if not isinstance(turret_index, int):
            continue
        # Turret indexing is now 0-based
        if str(turret_index) not in turret_data:  # json keys are always strings
            logger.warning(f"Turret {turret_index} not found in database for {weapon_descr.namespace}")
            continue
        turret_list = weapon_descr.v.by_m("TurretDescriptorList")
        # weapon_descr_namespace = weapon_descr.namespace
        # weapon/ammo edits
        if "MountedWeapons" in turret_edits:
            turret_descr = turret_list.v[turret_index]
            if not is_valid_turret(turret_descr.v):
                logger.debug(f"Turret {turret_index} is not valid")
            else:
                prefix = "$/GFX/Weapon/Ammo_"
                mounted_wpns = turret_descr.v.by_m("MountedWeaponDescriptorList")
                if "insert" in turret_edits["MountedWeapons"]:
                    for key, donor_edits in turret_edits["MountedWeapons"]["insert"].items():
                        # TODO: convert all mounted weapon edits to use the index:donor format
                        if isinstance(key, str) and ":" in key:
                            idx_str, donor = key.split(":", 1)
                            insert_at = int(idx_str)
                        else:
                            donor = key
                            insert_at = donor_edits.get("insert_at") if donor_edits else None

                        new_wpn = None
                        for weapon in mounted_wpns.v:
                            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                                continue
                            ammunition = weapon.v.by_m("Ammunition").v.split(prefix)[1]
                            if ammunition == donor:
                                new_wpn = weapon.copy()
                                break
                            if ammunition in ammo_db.get("renames_new_old", {}):
                                if ammo_db["renames_new_old"][ammunition] == donor:
                                    new_wpn = weapon.copy()
                                    break

                        if new_wpn is None and source_path and weapon_db:
                            new_wpn = _find_donor_weapon(
                                donor, weapon_db, source_path, ammo_db, prefix,
                            )

                        if new_wpn is not None:
                            if donor_edits:
                                for membr, value in donor_edits.items():
                                    if membr == "insert_at":
                                        continue
                                    if isinstance(value, list):
                                        new_list = ndf.model.List()
                                        for item in value:
                                            new_list.add(f"'{item}'")
                                        new_wpn.v.by_m(membr).v = new_list
                                    else:
                                        new_wpn.v.by_m(membr).v = str(value)

                            if insert_at is not None:
                                mounted_wpns.v.insert(insert_at, new_wpn)
                            else:
                                mounted_wpns.v.add(new_wpn)
                
                if "remove" in turret_edits["MountedWeapons"]:
                    for weapon_index in sorted(turret_edits["MountedWeapons"]["remove"], reverse=True):
                        mounted_wpns.v.remove(weapon_index)

                for weapon in mounted_wpns.v:
                    if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                        logger.debug(f"Mounted weapon {weapon.index} is not valid")
                        continue

                    ammunition = weapon.v.by_m("Ammunition").v.split(prefix)[1]
                    for ammo_name, ammo_edits in turret_edits["MountedWeapons"].items():
                        # Skip special keys like "insert"
                        if ammo_name == "insert":
                            continue
                        
                        # Check for match: direct, rename, or replacement
                        is_match = False
                        
                        # 1. Direct match
                        if ammunition == ammo_name:
                            is_match = True
                        # 2. Check if ammunition has been renamed and old name matches
                        elif ammunition in ammo_db["renames_new_old"]:
                            old_name = ammo_db["renames_new_old"].get(ammunition, None)
                            if old_name == ammo_name:
                                is_match = True
                        # 3. Check if ammo_name is a replacement for the current ammunition
                        # (i.e., ammo_name will replace ammunition, so we match on the old ammunition name)
                        if not is_match and ammo_name in replacement_map:
                            if replacement_map[ammo_name] == ammunition:
                                is_match = True
                        
                        if not is_match:
                            continue
                        for ammo_membr, ammo_value in ammo_edits.items():

                            if ammo_membr == "add_members":
                                for member, value in ammo_value:
                                    weapon.v.add(f"{member} = {value}")

                            elif ammo_membr == "Ammunition":
                                weapon.v.by_m(ammo_membr).v = f"$/GFX/Weapon/Ammo_{ammo_value}"

                            elif isinstance(ammo_value, list):
                                new_list = ndf.model.List()
                                for item in ammo_value:
                                    new_list.add(f"'{item}'")
                                weapon.v.by_m(ammo_membr).v = new_list

                            else:
                                weapon.v.by_m(ammo_membr).v = str(ammo_value)

        # turret property edits
        for membr, value in turret_edits.items():
            if membr == "MountedWeapons":
                continue
            else:
                turret_list.v[turret_index].v.by_m(membr).v = str(value)

    if "remove" in turrets_edits:
        turret_list = weapon_descr.v.by_member("TurretDescriptorList")
        # Sort in reverse order to remove highest indices first
        remove_indices = sorted([int(idx) for idx in turrets_edits["remove"]], reverse=True)
        for turret_index in remove_indices:
            turret_list.v.remove(turret_index)


def _apply_salvo_changes(weapon_descr: Any, wd_edits: Dict, weapon_descr_data: Dict, game_db: Dict) -> None:
    """Apply salvo changes using database data."""
    from src.data.infantry_magazine_salvo import strip_magazine_suffixes

    wd_name = weapon_descr.namespace
    salves_list = weapon_descr.v.by_m("Salves")
    salves_winchester = weapon_descr.v.by_m("SalvoIsMainSalvo", strict=False)
    weapon_indices = weapon_descr_data["weapon_indices"]
    renames_new_old = game_db["ammunition"]["renames_new_old"]
    salve_edits = wd_edits["Salves"]
    # Update salvos first to prevent index errors
    salvo_mapping = weapon_descr_data["salvo_mapping"]

    def _indices_for_salves_key(weapon: str) -> list | None:
        """Resolve Salves key to salvo_mapping indices (bare / rename / replace / magazine)."""
        candidates = [weapon]
        bare = strip_magazine_suffixes(weapon)
        if bare != weapon:
            candidates.append(bare)
        old_name = renames_new_old.get(weapon)
        if old_name:
            candidates.append(old_name)
        old_bare = renames_new_old.get(bare)
        if old_bare:
            candidates.append(old_bare)

        for cand in candidates:
            if cand in salvo_mapping:
                return salvo_mapping[cand]

        # Match salvo_mapping keys that strip to the same bare ammo
        for map_key, indices in salvo_mapping.items():
            if strip_magazine_suffixes(map_key) == bare:
                return indices

        # Via equipmentchanges.replace: Salves may name the magazine variant while
        # the mount still has the donor (or bare target) until remount runs later.
        equipment_changes = wd_edits.get("equipmentchanges") or {}
        for spec in normalize_replace(equipment_changes.get("replace")):
            new_bare = strip_magazine_suffixes(spec.new_weapon)
            if spec.new_weapon != weapon and new_bare != bare:
                continue
            old_weapon_old_name = renames_new_old.get(spec.old_weapon)
            weapon_key = old_weapon_old_name if old_weapon_old_name else spec.old_weapon
            if weapon_key in salvo_mapping:
                return salvo_mapping[weapon_key]
            weapon_key_bare = strip_magazine_suffixes(weapon_key)
            if weapon_key_bare in salvo_mapping:
                return salvo_mapping[weapon_key_bare]
            for map_key, indices in salvo_mapping.items():
                if strip_magazine_suffixes(map_key) == weapon_key_bare:
                    return indices
        return None

    for weapon, val in salve_edits.items():

        # Skip special control keys
        if weapon in ("insert", "remove"):
            continue

        salvo = val
        winchester = None
        if type(val) in (list, dict, set, tuple) and len(val) == 2:
            salvo = val[0]
            winchester = str(val[1])

        indices = _indices_for_salves_key(weapon)
        if indices is not None:
            for index in indices:
                if salvo:
                    logger.debug(f"Updating salvo for {weapon} at index {index}")
                    salves_list.v.replace(index, str(salvo))
                if salves_winchester and winchester:
                    logger.debug(f"Updating index {index} of SalvoIsMainSalvo to {winchester}")
                    salves_winchester.v.replace(index, winchester)
        else:
            logger.error(f"{weapon} ammo not found in {wd_name}")

    # Remove salvos BEFORE inserting so the weapon_indices lookup still resolves
    # against vanilla positions (inserts would otherwise shift the slot we're trying
    # to drop and the remove would target the wrong entry).
    if "remove" in salve_edits:
        for weapon in salve_edits["remove"]:
            if weapon in weapon_indices:
                for index in sorted(weapon_indices[weapon], reverse=True):
                    logger.debug(f"Removing salvo at index {index}")
                    salves_list.v.remove(index)
                    if salves_winchester:
                        logger.debug(f"Removing index {index} of SalvoIsMainSalvo")
                        salves_winchester.v.remove(index)

    # Insert new salvos at the user-specified final positions. We sort ASCENDING so
    # each insert lands at the exact index the user wrote: earlier inserts naturally
    # shift later ones into place. Descending order is broken when the vanilla Salves
    # list is shorter than the target indices (e.g. Feldgendarmerie_RFA: vanilla [80],
    # target [14, 11, 45, 4]) because ``list.insert`` clamps past-end indices to the
    # tail, which then scrambles the relative order of subsequent past-end inserts.
    if "insert" in salve_edits:
        insert_list = salve_edits["insert"]
        sorted_insert_list = sorted(insert_list, key=lambda x: x[0])
        for addition in sorted_insert_list:
            index, salvo = addition[0], addition[1]
            winchester = "False" if len(addition) < 3 else addition[2]
            logger.debug(f"Inserting salvo {salvo} at index {index}")
            salves_list.v.insert(index, str(salvo))
            if salves_winchester:
                logger.debug(f"Inserting salvo {salvo} at index {index}")
                salves_winchester.v.insert(index, winchester)


def _apply_equipment_changes(
    weapon_descr: Any,
    unit_edits: Dict,
    wd_edits: Dict,
    weapon_descr_data: Dict,
    turret_templates: List[Tuple[str, Any]],
    game_db: Dict,
    source_path: Any,
) -> None:
    """Apply equipment changes to weapon descriptor."""
    equipment_changes = wd_edits["equipmentchanges"]
    unit_name = weapon_descr.namespace.replace("WeaponDescriptor_", "")

    # Handle custom weapon swaps
    if any(key in equipment_changes for key in ["replace_custom", "add_custom"]):
        _apply_custom_weapon_swaps(weapon_descr, wd_edits, game_db)

    # Handle replacements
    if any(key in equipment_changes for key in ["replace", "replace_fixedsalvo"]):
        _apply_weapon_replacements(weapon_descr, equipment_changes, game_db)

    # Handle insertions (inserts at specific indices in reverse order for correct positioning)
    if "insert" in equipment_changes:
        _insert_new_weapons(weapon_descr, wd_edits, turret_templates, game_db)

    # Handle quantity changes
    if "quantity" in equipment_changes:
        _update_weapon_quantities(source_path, unit_name, unit_edits, equipment_changes, game_db)


def _apply_custom_weapon_swaps(weapon_descr: Any, wd_edits: Dict, game_db: Dict) -> None:
    """Apply custom weapon swaps."""
    from src.constants.weapons import mounted_weapons

    equipment_changes = wd_edits["equipmentchanges"]
    turret_list = weapon_descr.v.by_member("TurretDescriptorList")

    if "add_custom" in equipment_changes:
        for turret_index, mesh_alt_number, ammunition in equipment_changes["add_custom"]:
            turret = turret_list.v[turret_index]
            mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
            new_wpn = ndf.convert(mounted_weapons[ammunition])
            new_wpn[0].v.by_m("HandheldEquipmentKey").v = f"'WeaponAlternative_{mesh_alt_number}'"
            new_wpn[0].v.by_m("WeaponActiveAndCanShootPropertyName").v = f"'WeaponActiveAndCanShoot_{mesh_alt_number}'"
            new_wpn[0].v.by_m("WeaponIgnoredPropertyName").v = f"'WeaponIgnored_{mesh_alt_number}'"
            new_wpn[0].v.by_m("WeaponShootDataPropertyName").v = f"['WeaponShootData_0_{mesh_alt_number}']"
            mounted_wpns.v.add(new_wpn)

    if "replace_custom" in equipment_changes:
        for turret_index, weapon_index, mesh_alt_number, ammunition in equipment_changes["replace_custom"]:
            turret = turret_list.v[turret_index]
            mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
            new_wpn = ndf.convert(mounted_weapons[ammunition])
            new_wpn[0].v.by_m("HandheldEquipmentKey").v = f"'WeaponAlternative_{mesh_alt_number}'"
            new_wpn[0].v.by_m("WeaponActiveAndCanShootPropertyName").v = f"'WeaponActiveAndCanShoot_{mesh_alt_number}'"
            new_wpn[0].v.by_m("WeaponIgnoredPropertyName").v = f"'WeaponIgnored_{mesh_alt_number}'"
            new_wpn[0].v.by_m("WeaponShootDataPropertyName").v = f"['WeaponShootData_0_{mesh_alt_number}']"
            mounted_wpns.v.replace(weapon_index, new_wpn)


def _apply_weapon_replacements(weapon_descr: Any, equipment_changes: Dict, game_db: Dict) -> None:
    """Replace weapons with their replacements.

    ``replace`` tuples apply in order; each tuple replaces the *next* mount matching ``current``
    in turret order (then mount order), so duplicate donor ammo can map to different weapons.
    """
    ammo_pattern = re.compile(r"\$/GFX/Weapon/Ammo_(.+)$")
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    ammo_db = game_db["ammunition"]
    unit_db = game_db["unit_data"]
    unit_edits = load_unit_edits()

    # Get unit strength from unit name
    unit_name = weapon_descr.namespace.replace("WeaponDescriptor_", "")
    unit_strength = None

    # Check unit edits first
    if unit_name in unit_edits and "strength" in unit_edits[unit_name]:
        unit_strength = unit_edits[unit_name]["strength"]
    # Check unit database if not found in edits
    elif unit_name in unit_db:
        unit_strength = unit_db[unit_name].get("strength")

    if not unit_strength:
        logger.warning(f"No strength found for unit {unit_name}")
        return

    for turret in turret_list:
        if not is_valid_turret(turret.v):
            continue

        mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
        for weapon in mounted_wpns.v:
            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                continue

            ammo_val = weapon.v.by_m("Ammunition").v

            # Handle fixed salvo replacements (still scan all mounts)
            if "replace_fixedsalvo" in equipment_changes:
                for current, replacement in equipment_changes["replace_fixedsalvo"]:
                    new_name = None
                    if current in ammo_db["renames_old_new"]:
                        new_name = ammo_db["renames_old_new"].get(current, None)

                    if new_name and ammo_val == f"$/GFX/Weapon/Ammo_{new_name}":
                        weapon.v.by_m("Ammunition").v = f"$/GFX/Weapon/Ammo_{replacement}"
                        logger.debug(f"Replaced {current} with {replacement}")
                    elif ammo_val == f"$/GFX/Weapon/Ammo_{current}":
                        weapon.v.by_m("Ammunition").v = f"$/GFX/Weapon/Ammo_{replacement}"
                        logger.debug(f"Replaced {current} with {replacement}")

    if "replace" not in equipment_changes:
        return

    renames = ammo_db.get("renames_old_new", {})

    for spec in normalize_replace(equipment_changes["replace"]):
        replace_fire_effect = spec.swap_fire_effect
        current = spec.old_weapon
        new_weapon = spec.new_weapon
        old_fire_effect = spec.old_fire_effect
        new_fire_effect = spec.new_fire_effect

        renamed_current = renames.get(current)

        found = False
        for turret in turret_list:
            if not is_valid_turret(turret.v):
                continue
            mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
            for weapon in mounted_wpns.v:
                if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                    continue
                ammo_val = weapon.v.by_m("Ammunition").v
                match = ammo_pattern.match(ammo_val)
                if not match:
                    continue
                full_ammo_name = match.group(1)
                base_ammo_name = _mounted_ammo_base_name(full_ammo_name)
                current_base = _mounted_ammo_base_name(current)
                renamed_current_base = (
                    _mounted_ammo_base_name(renamed_current) if renamed_current else None
                )
                if (
                    base_ammo_name != current_base
                    and base_ammo_name != renamed_current_base
                ):
                    continue

                quantity = int(weapon.v.by_m("NbWeapons").v)

                use_strength = False
                for (weapon_name, category, _, _), data in ammos.items():
                    if weapon_name == new_weapon and category == "small_arms":
                        damage_family = data.get("Ammunition", {}).get("Arme", {}).get("Family")
                        use_strength = damage_family in [
                            "DamageFamily_sa_full",
                            "DamageFamily_sa_intermediate",
                        ]
                        break

                salvo_suffix = _replacement_mount_suffix(full_ammo_name, new_weapon, quantity)

                if re.search(r"_salvolength\d+$", new_weapon):
                    ammo_core = new_weapon
                elif use_strength:
                    ammo_core = f"{new_weapon}_strength{unit_strength}"
                else:
                    ammo_core = new_weapon

                if (
                    salvo_suffix
                    and not (
                        _uses_sniper_damage_family(new_weapon, game_db)
                        and salvo_suffix.startswith("_x")
                    )
                ):
                    ammo_core += salvo_suffix

                new_ammo = f"$/GFX/Weapon/Ammo_{ammo_core}"
                weapon.v.by_m("Ammunition").v = new_ammo
                logger.debug(f"Replaced {current} with {new_weapon}")

                if replace_fire_effect:
                    fire_effect_val = strip_quotes(weapon.v.by_m("EffectTag").v).replace("FireEffect_", "")
                    if old_fire_effect == fire_effect_val:
                        weapon.v.by_m("EffectTag").v = "'" + f"FireEffect_{new_fire_effect}" + "'"
                        logger.debug(f"Replaced fire effect{old_fire_effect} with {new_fire_effect}")
                found = True
                break
            else:
                continue
            break
        if not found:
            logger.warning(f"{unit_name}: weapon '{current}' not found in any turret for replacement")


def _adjust_light_at_salvos(
    weapon_descr: Any, unit_name: str, ammos_: Dict, ammo_db: Dict, unit_db: Dict, weapon_db: Dict
) -> None:
    """Remount light AT to magazine salvolength variants by squad size; Salves=1."""
    from src.data.infantry_magazine_salvo import magazine_ammo_name
    from src.utils.ndf_utils import is_obj_type, is_valid_turret

    squad_size = unit_db.get(unit_name, {}).get("strength")
    if not squad_size:
        logger.warning(f"No strength data found for {unit_name}")
        return
    if squad_size not in LIGHT_AT_AMMO:
        logger.info(f"Invalid squad size {squad_size} for {unit_name}")
        return

    weapon_descr_name = f"WeaponDescriptor_{unit_name}"
    unit_weapon_data = weapon_db.get(weapon_descr_name)
    if not unit_weapon_data:
        logger.debug(f"No weapon data found for {weapon_descr_name}")
        return

    renames = ammo_db.get("renames_old_new", {})
    new_ammo_count = LIGHT_AT_AMMO[squad_size]
    if new_ammo_count <= 1:
        return

    prefix = "$/GFX/Weapon/Ammo_"
    turrets = unit_weapon_data.get("turrets", {})
    for turret in turrets.values():
        for ammo_name, weapon_data in turret.get("weapons", {}).items():
            ammo_to_check = renames.get(ammo_name, ammo_name)
            base_for_cat = re.sub(r"(_salvolength\d+|_infmagazine\d+)$", "", ammo_to_check)
            if not any(key[0] == base_for_cat and key[1] == "light_at" for key in ammos_.keys()):
                continue

            salvo_index = weapon_data["salvo_index"]
            variant = magazine_ammo_name(base_for_cat, int(new_ammo_count))
            turret_list = weapon_descr.v.by_m("TurretDescriptorList")
            for turret_descr in turret_list.v:
                if not is_valid_turret(turret_descr.v):
                    continue
                for mounted in turret_descr.v.by_m("MountedWeaponDescriptorList").v:
                    if not is_obj_type(mounted.v, "TMountedWeaponDescriptor"):
                        continue
                    path = mounted.v.by_m("Ammunition").v
                    if not isinstance(path, str) or not path.startswith(prefix):
                        continue
                    current = path[len(prefix):]
                    current_base = re.sub(r"(_salvolength\d+|_infmagazine\d+)$", "", current)
                    if current_base != base_for_cat and current != ammo_name:
                        continue
                    mounted.v.by_m("Ammunition").v = f"{prefix}{variant}"
                    salves_list = weapon_descr.v.by_m("Salves").v
                    salves_list.replace(int(salvo_index), "1")
                    logger.debug(
                        f"Updating {unit_name} {ammo_name} -> {variant} "
                        f"(Salves=1) for {squad_size}-man squad"
                    )
                    break

