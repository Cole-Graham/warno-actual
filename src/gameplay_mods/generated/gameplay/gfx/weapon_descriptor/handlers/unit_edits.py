import re
from typing import Any, Dict, List, Tuple

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.constants.weapons import LIGHT_AT_AMMO
from src.constants.weapons import ammunitions as ammos
from src.constants.weapons.missiles.aa import missiles

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import (
    is_obj_type,
    is_valid_turret,
    strip_quotes,
)

from .new_units import _should_use_strength_variant

logger = setup_logger(__name__)

def unit_edits_weapondescriptor(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Unit Edits for WeaponDescriptor.ndf file.
    Args:
        source_path: The NDF file being edited
        game_db: Game database containing ammunition and weapon data
    """
    ammo_db = game_db["ammunition"]
    unit_db = game_db["unit_data"]
    weapon_db = game_db["weapons"]

    # Add HAGRU missiles to MANPAD turrets
    for weapon_descr in source_path:
        if not weapon_descr.namespace.startswith("WeaponDescriptor_"):
            continue

        if weapon_descr.namespace not in weapon_db:
            continue

        weapon_data = weapon_db[weapon_descr.namespace]

        # Process each turret
        for turret_idx, turret_data in weapon_data["turrets"].items():
            turret = weapon_descr.v.by_m("TurretDescriptorList").v[int(turret_idx)]
            if not is_valid_turret(turret.v):
                continue

            mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
            wpns_to_add = []

            # Check each weapon in the turret
            for ammo_name, weapon_info in turret_data["weapons"].items():
                # Strip _x{number} suffix for dictionary lookup
                base_ammo_name = re.sub(r"_x\d+$", "", ammo_name)

                # since Eugen used same formatting for quantity and salvo length,
                # we can use the same regex data to get the salvo length
                salvo_length = weapon_info.get("regex_quantity")

                # Check if this is a TBAGRU missile
                for (missile_name, _, _, _), missile_data in missiles.items():
                    if (
                        missile_name == base_ammo_name
                        and "Ammunition" in missile_data
                        and "arme" in missile_data["Ammunition"]
                        and missile_data["Ammunition"]["arme"].get("DamageFamily") == "DamageFamily_manpad_tbagru"
                    ):

                        # Find and copy the weapon
                        for weapon in mounted_wpns.v:
                            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                                continue

                            new_name = ammo_db["renames_old_new"].get(ammo_name, None)
                            if new_name:
                                ammo_path = f"$/GFX/Weapon/Ammo_{new_name}"
                            else:
                                ammo_path = f"$/GFX/Weapon/Ammo_{ammo_name}"
                            weapon_ammo = weapon.v.by_m("Ammunition").v
                            if weapon_ammo == ammo_path:
                                new_wpn = weapon.copy()
                                # Only add salvo length suffix if length > 1
                                if salvo_length == 1:
                                    new_ammo = f"$/GFX/Weapon/Ammo_{base_ammo_name}_HAGRU"
                                else:
                                    new_ammo = f"$/GFX/Weapon/Ammo_{base_ammo_name}_HAGRU" f"_salvolength{salvo_length}"
                                new_wpn.v.by_m("Ammunition").v = new_ammo
                                wpns_to_add.append(new_wpn)
                                logger.debug(
                                    f"Adding HAGRU missile {base_ammo_name}_HAGRU to " f"{weapon_descr.namespace}"
                                )
                                break

            # Add all new weapons after iteration
            for new_wpn in wpns_to_add:
                mounted_wpns.v.add(new_wpn)

    # vanilla_renames_weapondescriptor(source_path, ammo_db, weapon_db)

    # Get edits and weapon data
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
        turret_templates = _gather_turret_templates(source_path, unit, edits, ammo_db, weapon_db)

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
            

def _gather_turret_templates(
    source_path: Any, unit: str, edits: Dict, ammo_db: Dict[str, Any], weapon_db: Dict[str, Any]
) -> List[Tuple[str, Any]]:
    """Gather turret templates for equipment changes using database data.
    
    Handles "insert" key from equipmentchanges.
    """
    turret_objects = []
    weapons_to_add = []

    equipment_changes = edits["WeaponDescriptor"].get("equipmentchanges", {})
    # Check for "insert" key
    weapon_list = equipment_changes.get("insert")
    if not weapon_list:
        return []

    weapon_descr_name = f"WeaponDescriptor_{unit}"
    if not weapon_db or weapon_descr_name not in weapon_db:
        logger.warning(f"Weapon {weapon_descr_name} not found in database")
        return []

    # Find the matching weapon descriptor
    weapon_descr_data = weapon_db[weapon_descr_name]
    for weapon_descr in source_path:
        if weapon_descr.namespace != weapon_descr_name:
            continue

        try:
            turret_objects.extend(
                _find_turret_templates(
                    weapon_descr,
                    weapon_list,
                    weapons_to_add,
                    weapon_descr_data,
                    weapon_db,
                    ammo_db,
                    source_path,
                )
            )
            break  # Found and processed the descriptor
        except Exception as e:
            logger.error(f"Failed to find turret templates for {weapon_descr_name}: {str(e)}")

    logger.debug(f"Found templates for weapons: {weapons_to_add}")
    return turret_objects


def _find_turret_templates(
    weapon_descr: Any,
    add_list: List,
    weapons_to_add: List,
    weapon_descr_data: Dict,
    weapon_db: Dict,
    ammo_db: Dict,
    source_path: Any,
) -> List[Tuple[str, Any]]:
    """Find turret templates matching the add list using database data."""
    templates = []
    processed_weapons = set()  # Track which weapons we've already found templates for

    def find_donor_descriptor(weapon_name: str) -> Tuple[str, Dict] | Tuple[None, None]:
        """Find a weapon descriptor that has the weapon we want."""
        for descr_name, descr_data in weapon_db.items():
            if weapon_name in descr_data["weapon_locations"]:
                return descr_name, descr_data
        return None, None

    def add_turret_template(donor_descr_: Any, donor_locations: Dict, weapon_name: str) -> bool:
        for location in donor_locations[weapon_name]:
            # Get the turret from the donor descriptor
            for turret in donor_descr_.v.by_member("TurretDescriptorList").v:
                if turret.index == location["turret_index"]:
                    new_turret = _prepare_turret_template(turret, int(turret.index))
                    weapons_to_add.append(weapon_name)
                    templates.append((weapon_name, new_turret))
                    return True
        return False

    # Process each weapon to add
    for index_to_insert, ammo_name in add_list:
        if ammo_name in processed_weapons:  # Skip if we already found a template
            continue

        ammo_renames = ammo_db["renames_new_old"]
        old_name = ammo_renames.get(ammo_name, None)

        # Try both new and old names
        for name in [ammo_name, old_name]:
            if not name:
                continue

            # Find a descriptor that has this weapon
            donor_name, donor_data = find_donor_descriptor(name)
            if not donor_name:
                continue

            # Get the actual descriptor from source_path
            donor_descr = source_path.by_namespace(donor_name)
            if not donor_descr:
                continue

            template_added = add_turret_template(donor_descr, donor_data["weapon_locations"], name)
            if template_added:
                processed_weapons.add(ammo_name)
                break

    return templates


def _prepare_turret_template(turret: Any, index: int) -> Any:
    """Prepare a turret template with updated indices."""
    new_turret = turret.copy()

    # Update weapon indices
    mounted_wpns = new_turret.v.by_m("MountedWeaponDescriptorList")
    for weapon in mounted_wpns.v:
        weapon.v.by_m("SalvoStockIndex").v = str(index)

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
                # Update SalvoStockIndex to match the insert position
                mounted_weapons = turret_template.v.by_m("MountedWeaponDescriptorList")
                for mounted_weapon in mounted_weapons.v:
                    mounted_weapon.v.by_m("SalvoStockIndex").v = str(turret_index)
                
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

                # Update ammo name with quantity and strength if needed
                prefix = current_ammo.split("_", 1)[0]

                if _should_use_strength_variant(base_ammo, game_db):
                    if quantity > 1:
                        new_ammo = f"{prefix}_{base_ammo}_strength{unit_strength}_x{quantity}"
                    else:
                        new_ammo = f"{prefix}_{base_ammo}_strength{unit_strength}"
                else:
                    if quantity > 1:
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


def _apply_turret_changes(weapon_descr: Any, turrets_edits: Dict, weapon_descr_data: Dict, game_db: Dict, wd_edits: Dict = None) -> None:
    """Apply turret changes using database data."""
    # turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    turret_data = weapon_descr_data["turrets"]

    ammo_db = game_db["ammunition"]
    
    # Build a mapping of replacements: new_weapon -> old_weapon
    replacement_map = {}
    if wd_edits and "equipmentchanges" in wd_edits:
        equipment_changes = wd_edits["equipmentchanges"]
        if "replace" in equipment_changes:
            for replacement in equipment_changes["replace"]:
                if len(replacement) == 4:
                    old_weapon, new_weapon, old_fire_effect, new_fire_effect = replacement
                else:
                    old_weapon, new_weapon = replacement
                replacement_map[new_weapon] = old_weapon

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
            for turret_descr in turret_list.v:
                if not is_valid_turret(turret_descr.v):
                    logger.debug(f"Turret {turret_index} is not valid")
                    continue

                prefix = "$/GFX/Weapon/Ammo_"
                mounted_wpns = turret_descr.v.by_m("MountedWeaponDescriptorList")
                if "insert" in turret_edits["MountedWeapons"]:
                    for weapon in mounted_wpns.v:
                        wpn_index = weapon.index
                        if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                            logger.debug(f"Mounted weapon {wpn_index} is not valid")
                            continue

                        ammunition = weapon.v.by_m("Ammunition").v.split(prefix)[1]
                        for donor, donor_edits in turret_edits["MountedWeapons"]["insert"].items():
                            if ammunition != donor:
                                continue
                            new_wpn = weapon.copy()
                            for membr, value in donor_edits.items():
                                if isinstance(value, list):
                                    new_list = ndf.model.List()
                                    for item in value:
                                        new_list.add(f"'{item}'")
                                    new_wpn.v.by_m(membr).v = new_list
                                else:
                                    new_wpn.v.by_m(membr).v = str(value)

                            mounted_wpns.v.add(new_wpn)

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
    wd_name = weapon_descr.namespace
    salves_list = weapon_descr.v.by_m("Salves")
    salves_winchester = weapon_descr.v.by_m("SalvoIsMainSalvo", strict=False)
    weapon_indices = weapon_descr_data["weapon_indices"]
    renames_new_old = game_db["ammunition"]["renames_new_old"]
    salve_edits = wd_edits["Salves"]
    # Update salvos first to prevent index errors
    salvo_mapping = weapon_descr_data["salvo_mapping"]
    for weapon, val in salve_edits.items():

        # Skip special control keys
        if weapon in ("insert", "remove"):
            continue

        salvo = val
        winchester = None
        if type(val) in (list, dict, set, tuple) and len(val) == 2:
            salvo = val[0]
            winchester = str(val[1])

        old_weapon = renames_new_old.get(weapon, None)

        if weapon in salvo_mapping:
            indices = salvo_mapping[weapon]
            for index in indices:
                if salvo:
                    logger.debug(f"Updating salvo for {weapon} at index {index}")
                    salves_list.v.replace(index, str(salvo))
                if salves_winchester and winchester:
                    logger.debug(f"Updating index {index} of SalvoIsMainSalvo to {winchester}")
                    salves_winchester.v.replace(index, winchester)

        elif old_weapon and old_weapon in salvo_mapping:
            indices = salvo_mapping[old_weapon]
            for index in indices:
                if salvo:
                    logger.debug(f"Updating salvo for {weapon} at index {index}")
                    salves_list.v.replace(index, str(salvo))
                if salves_winchester and winchester:
                    logger.debug(f"Updating index {index} of SalvoIsMainSalvo to {winchester}")
                    salves_winchester.v.replace(index, winchester)

        elif "equipmentchanges" in wd_edits:
            if "replace" in wd_edits["equipmentchanges"]:
                for replacement in wd_edits["equipmentchanges"]["replace"]:
                    if len(replacement) == 4:
                        old_weapon, new_weapon, old_fire_effect, new_fire_effect = replacement
                    else:
                        old_weapon, new_weapon = replacement
                    # check if the new weapon is the same as the one in salve_edits
                    if new_weapon != weapon:
                        logger.debug(f"New weapon {new_weapon} is not the same as {weapon}")
                        continue
                    # check if the old weapon is a renamed version of the weapon in salvo_mapping
                    old_weapon_old_name = renames_new_old.get(old_weapon, None)
                    weapon_key = old_weapon_old_name if old_weapon_old_name else old_weapon
                    if weapon_key in salvo_mapping:
                        indices = salvo_mapping[weapon_key]
                        for index in indices:
                            if salvo:  # is not None:
                                logger.debug(f"Updating salvo for {weapon} at index {index}")
                                salves_list.v.replace(index, str(salvo))
                            if salves_winchester and winchester:
                                logger.debug(f"Updating index {index} of SalvoIsMainSalvo to {winchester}")
                                salves_winchester.v.replace(index, winchester)

        elif weapon == "remove":
            continue

        else:
            logger.error(f"No salvo edits found for {weapon}")

    # Insert new salvos at specific indices (in reverse order to maintain correct positions)
    if "insert" in salve_edits:
        insert_list = salve_edits["insert"]
        # Sort by index in descending order to insert highest indices first
        sorted_insert_list = sorted(insert_list, key=lambda x: x[0], reverse=True)
        for addition in sorted_insert_list:
            index, salvo = addition[0], addition[1]
            winchester = "False" if len(addition) < 3 else addition[2]
            logger.debug(f"Inserting salvo {salvo} at index {index}")
            salves_list.v.insert(index, str(salvo))
            if salves_winchester:
                logger.debug(f"Inserting salvo {salvo} at index {index}")
                salves_winchester.v.insert(index, winchester)

    # Remove salvos for specific weapons
    if "remove" in salve_edits:
        for weapon in salve_edits["remove"]:
            if weapon in weapon_indices:
                for index in sorted(weapon_indices[weapon], reverse=True):
                    logger.debug(f"Removing salvo at index {index}")
                    salves_list.v.remove(index)
                    if salves_winchester:
                        logger.debug(f"Removing index {index} of SalvoIsMainSalvo")
                        salves_winchester.v.remove(index)


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
    """Replace weapons with their replacements."""
    ammo_pattern = re.compile(r"\$/GFX/Weapon/Ammo_(.*?)(?:_x\d+)?$")
    turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]
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

    def __get_weapon_quantity(
        weapon_descr_: Any, turret_index_: str, ammo_name_: str, ammo_db_: Dict, weapon_db_: Dict
    ) -> int:
        """Get the quantity of a weapon from the weapons.json"""
        weapon_descr_name = weapon_descr_.namespace
        current_turret = weapon_db_[weapon_descr_name]["turrets"][turret_index_]

        if ammo_name_ in ammo_db_["renames_new_old"]:
            old_name = ammo_db_["renames_new_old"].get(ammo_name_, None)
            if old_name:
                current_weapon = current_turret["weapons"][old_name]
            else:
                current_weapon = current_turret["weapons"][ammo_name_]
        else:
            current_weapon = current_turret["weapons"][ammo_name_]

        return current_weapon["quantity"]

    for turret in turret_list:
        if not is_valid_turret(turret.v):
            continue

        turret_index = str(turret.index)
        mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
        for weapon in mounted_wpns.v:
            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                continue

            ammo_val = weapon.v.by_m("Ammunition").v

            # Handle fixed salvo replacements
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

            match = ammo_pattern.match(ammo_val)
            # Handle regular replacements
            if match:
                ammo_name = match.group(1)
                if "replace" in equipment_changes:
                    for replacement in equipment_changes["replace"]:
                        if len(replacement) == 4:
                            replace_fire_effect = True
                            current, replacement, old_fire_effect, new_fire_effect = replacement
                        else:
                            replace_fire_effect = False
                            current, replacement = replacement

                        if ammo_name == current:
                            quantity = __get_weapon_quantity(weapon_descr, turret_index, ammo_name, ammo_db, weapon_db)

                            # Check if replacement weapon should use strength variants
                            use_strength = False
                            for (weapon_name, category, _, _), data in ammos.items():
                                if weapon_name == replacement and category == "small_arms":
                                    damage_family = data.get("Ammunition", {}).get("Arme", {}).get("Family")
                                    use_strength = damage_family in [
                                        "DamageFamily_sa_full",
                                        "DamageFamily_sa_intermediate",
                                    ]
                                    break

                            if quantity > 1:
                                if use_strength:
                                    new_ammo = f"$/GFX/Weapon/Ammo_{replacement}_strength{unit_strength}_x{quantity}"
                                else:
                                    new_ammo = f"$/GFX/Weapon/Ammo_{replacement}_x{quantity}"
                            else:
                                if use_strength:
                                    new_ammo = f"$/GFX/Weapon/Ammo_{replacement}_strength{unit_strength}"
                                else:
                                    new_ammo = f"$/GFX/Weapon/Ammo_{replacement}"
                            weapon.v.by_m("Ammunition").v = new_ammo
                            logger.debug(f"Replaced {current} with {replacement}")

                        if replace_fire_effect:
                            fire_effect_val = strip_quotes(weapon.v.by_m("EffectTag").v).replace("FireEffect_", "")
                            if old_fire_effect == fire_effect_val:
                                weapon.v.by_m("EffectTag").v = "'" + f"FireEffect_{new_fire_effect}" + "'"
                                logger.debug(f"Replaced fire effect{old_fire_effect} with {new_fire_effect}")


def _adjust_light_at_salvos(
    weapon_descr: Any, unit_name: str, ammos_: Dict, ammo_db: Dict, unit_db: Dict, weapon_db: Dict
) -> None:
    """Adjust salvo counts for light AT weapons based on squad size."""
    # Get squad size from unit data
    squad_size = unit_db.get(unit_name, {}).get("strength")
    if not squad_size:
        logger.warning(f"No strength data found for {unit_name}")
        return
    if squad_size not in LIGHT_AT_AMMO:
        # this is not an error, some unit strengths are just not mapped (intentionally)
        logger.info(f"Invalid squad size {squad_size} for {unit_name}")
        return

    # Get this unit's weapon data
    weapon_descr_name = f"WeaponDescriptor_{unit_name}"
    unit_weapon_data = weapon_db.get(weapon_descr_name)
    if not unit_weapon_data:
        logger.debug(f"No weapon data found for {weapon_descr_name}")
        return

    # Get weapon renames mapping
    renames = ammo_db.get("renames_old_new", {})

    # Look through turrets for light AT weapons
    turrets = unit_weapon_data.get("turrets", {})
    for turret in turrets.values():
        for ammo_name, weapon_data in turret.get("weapons", {}).items():
            # Check original name for possible rename, and return the original name if none found
            ammo_to_check = renames.get(ammo_name, ammo_name)
            if any(key[0] == ammo_to_check and key[1] == "light_at" for key in ammos_.keys()):
                salvo_index = weapon_data["salvo_index"]
                new_ammo_count = LIGHT_AT_AMMO[squad_size]

                # Update the salvo count
                salves_list = weapon_descr.v.by_m("Salves").v
                logger.debug(
                    f"Updating {unit_name} {ammo_name} salvo count to {new_ammo_count} " f"for {squad_size}-man squad"
                )
                salves_list.replace(int(salvo_index), str(new_ammo_count))