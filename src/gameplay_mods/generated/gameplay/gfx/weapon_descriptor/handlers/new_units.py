"""Functions for creating new weapon descriptors."""

import re
from typing import Any, Dict

from src import ndf
from src.constants.new_units import NEW_UNITS
# from src.constants.weapons.ammunition.small_arms import weapons as small_arms_weapons
from src.constants.weapons import ammunitions
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_valid_turret, strip_quotes

small_arms_weapons = ammunitions

logger = setup_logger(__name__)


def new_units_weapondescriptor(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Create weapon descriptors for new units in WeaponDescriptor.ndf"""
    logger.info("Creating weapon descriptors for new units")

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if edits.get("is_unarmed", False):
            continue

        # Get the new unit name that will be used for the namespace
        if "NewName" not in edits:
            logger.error(f"Missing NewName for donor unit {donor_name}")
            continue

        # Clone donor weapon descriptor
        donor_weap = source_path.by_namespace(f"WeaponDescriptor_{donor_name}")
        if not donor_weap:
            logger.warning(f"Weapon descriptor not found for donor {donor_name}")
            continue

        new_weap_row = donor_weap.copy()
        new_weap_row.namespace = f"WeaponDescriptor_{edits['NewName']}"

        # Handle weapon modifications if present
        if "WeaponDescriptor" in edits:
            weapon_edits = edits["WeaponDescriptor"]

            # Handle equipment changes
            if "equipmentchanges" in weapon_edits:
                changes = weapon_edits["equipmentchanges"]

                # Handle replacements
                if "replace" in changes:
                    for replacement in changes["replace"]:
                        if len(replacement) == 4:
                            old_ammo, new_ammo, old_fire_effect, new_fire_effect = replacement
                            _replace_weapon(
                                source_path,
                                changes,
                                new_weap_row,
                                old_ammo,
                                new_ammo,
                                old_fire_effect,
                                new_fire_effect,
                                game_db,
                            )
                        else:
                            old_ammo, new_ammo = replacement
                            _replace_weapon(source_path, changes, new_weap_row, old_ammo, new_ammo, None, None, game_db)

                # Handle additions
                if "add" in changes:
                    for ammo in changes["add"]:
                        _add_weapon(source_path, changes, new_weap_row, ammo, game_db)

                # Handle index adjustments for bumped weapons in turret and mounted weapon lists
                if "update" in changes:
                    _update_weapon(changes, new_weap_row)

                # Handle HAGRU MANPADS
                if "HAGRU_MANPADS" in changes:
                    for turret_index, donor_weapon_index, hagru_ammo in changes["HAGRU_MANPADS"]:
                        _add_hagru_manpads(new_weap_row, turret_index, donor_weapon_index, hagru_ammo)

                # Handle quantities
                if "quantity" in changes:
                    for ammo, quantity in changes["quantity"].items():
                        _update_weapon_quantity(new_weap_row, ammo, quantity, game_db)

            # Handle salvos
            if "Salves" in weapon_edits:
                for ammo, salvo in weapon_edits["Salves"].items():
                    _update_weapon_salvo(new_weap_row, ammo, salvo, game_db)

        # Update any unmodified weapons that should use strength variants
        _update_unmodified_weapons(new_weap_row, game_db)

        source_path.add(new_weap_row)
        logger.info(f"Added weapon descriptor for {edits['NewName']}")


def _add_weapon(
    source_path: Any, changes: Dict[str, Any], new_weap_row: Any, ammo: str, game_db: Dict[str, Any]
) -> None:
    """Add a weapon to the weapon descriptor.

    Args:
        source_path: The NDF file being edited
        changes: Dictionary containing equipment changes
        new_weap_row: The weapon descriptor to modify
        ammo: The ammunition to add
        game_db: Game database containing weapon and ammunition data
    """
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]

    # Get turret index and weapon name from changes
    # TODO: handle multiple weapon additions, currently hardcoded to access the first tuple '[0]'
    turret_index = changes["add"][0][0]  # First element's turret index
    weapon_name = changes["add"][0][1]  # First element's weapon name
    fire_effect = changes["add"][0][2]  # First element's fire effect

    # Get unit strength from NEW_UNITS
    unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
    unit_strength = None
    for donor, edits in NEW_UNITS.items():
        is_infantry = edits.get("is_infantry", False)
        if edits.get("NewName") == unit_name:
            unit_strength = edits.get("strength")
            break

    if not unit_strength and is_infantry:
        logger.warning(f"No strength found for new unit {unit_name}")
        return

    # check if weapon is renamed
    old_name = ammo_db["renames_new_old"].get(weapon_name, None)

    # Find matching weapon in database to use as template
    template_found = False
    for descr_name, descr_data in weapon_db.items():
        if old_name and old_name not in descr_data["weapon_locations"]:
            continue
        elif not old_name and weapon_name not in descr_data["weapon_locations"]:
            continue

        # Get weapon location data
        weapon_locations = descr_data["weapon_locations"][old_name or weapon_name]
        if not weapon_locations:
            continue

        # Get first location where this weapon appears
        location = weapon_locations[0]  # Contains mounted_index, salvo_index, turret_index

        # Find the weapon descriptor in source_path to copy from
        donor_descr = source_path.by_namespace(descr_name)
        if not donor_descr:
            continue

        # Get and copy the entire turret containing our template weapon
        donor_turret = donor_descr.v.by_m("TurretDescriptorList").v[location["turret_index"]]
        if not is_valid_turret(donor_turret.v):
            continue

        # Create new turret by copying template
        new_turret = donor_turret.copy()

        # Update weapon indices and add strength to ammo path
        mounted_wpns = new_turret.v.by_m("MountedWeaponDescriptorList")
        for weapon in mounted_wpns.v:
            weapon.v.by_m("EffectTag").v = f"'FireEffect_{fire_effect}'"
            weapon.v.by_m("SalvoStockIndex").v = str(turret_index)
            weapon.v.by_m("HandheldEquipmentKey").v = f"'MeshAlternative_{turret_index + 1}'"
            weapon.v.by_m("WeaponActiveAndCanShootPropertyName").v = f"'WeaponActiveAndCanShoot_{turret_index + 1}'"
            weapon.v.by_m("WeaponIgnoredPropertyName").v = f"'WeaponIgnored_{turret_index + 1}'"
            weapon.v.by_m("WeaponShootDataPropertyName").v = f"['WeaponShootData_0_{turret_index + 1}']"

            # Update ammo path to include strength
            current_ammo = weapon.v.by_m("Ammunition").v
            prefix = current_ammo.split("_", 1)[0]  # Get $/GFX/Weapon/Ammo part
            quantity = changes["quantity"].get(weapon_name, int(weapon.v.by_m("NbWeapons").v))

            if _should_use_strength_variant(weapon_name, game_db):
                if quantity > 1:
                    new_ammo = f"{prefix}_{weapon_name}_strength{unit_strength}_x{quantity}"
                else:
                    new_ammo = f"{prefix}_{weapon_name}_strength{unit_strength}"
            else:
                if quantity > 1:
                    new_ammo = f"{prefix}_{weapon_name}_x{quantity}"
                else:
                    new_ammo = f"{prefix}_{weapon_name}"
            weapon.v.by_m("Ammunition").v = new_ammo
            weapon.v.by_m("NbWeapons").v = str(quantity)

        # Update turret bone index
        # TODO: turret bone might not always be the same as turret index
        new_yul_bone = turret_index + 1
        new_turret.v.by_m("YulBoneOrdinal").v = str(new_yul_bone)

        # Add to target turret list
        turret_list = new_weap_row.v.by_member("TurretDescriptorList")
        turret_list.v.insert(turret_index, new_turret)

        logger.debug(f"Added turret with {weapon_name} at index {turret_index}")
        template_found = True
        break

    if not template_found:
        logger.warning(f"Could not find template for weapon {weapon_name}")


def _update_weapon(
    changes: Dict[str, Any],
    new_weap_row: Any,
) -> None:
    """Update index values for bumped weapons in turret and mounted weapon lists."""
    updates = changes["update"]
    turret_list = new_weap_row.v.by_member("TurretDescriptorList")
    for turret_index in updates:
        turret = turret_list.v[turret_index]
        turret.v.by_m("YulBoneOrdinal").v = str(turret_index + 1)
        mounted_weapons = turret.v.by_member("MountedWeaponDescriptorList")
        for weapon in mounted_weapons.v:
            weapon.v.by_m("SalvoStockIndex").v = str(turret_index)
            weapon.v.by_m("HandheldEquipmentKey").v = f"'MeshAlternative_{turret_index + 1}'"
            weapon.v.by_m("WeaponActiveAndCanShootPropertyName").v = f"'WeaponActiveAndCanShoot_{turret_index + 1}'"
            weapon.v.by_m("WeaponIgnoredPropertyName").v = f"'WeaponIgnored_{turret_index + 1}'"
            weapon.v.by_m("WeaponShootDataPropertyName").v = f"['WeaponShootData_0_{turret_index + 1}']"


def _add_hagru_manpads(
    new_weap_row: Any,
    turret_index: int,
    donor_weapon_index: int,
    hagru_ammo: str,
) -> None:
    """Add a HAGRU MANPADS to the weapon descriptor."""
    turret_list = new_weap_row.v.by_member("TurretDescriptorList")
    turret = turret_list.v[turret_index]
    mounted_weapons = turret.v.by_member("MountedWeaponDescriptorList")
    donor_weapon = mounted_weapons.v[donor_weapon_index]
    new_weapon = donor_weapon.copy()
    new_weapon.v.by_m("Ammunition").v = f"$/GFX/Weapon/Ammo_{hagru_ammo}"
    mounted_weapons.v.add(new_weapon)


def _replace_weapon(
    source_path: Any,
    changes: Dict[str, Any],
    new_weap_row: Any,
    old_ammo: str,
    new_ammo: str,
    old_fire_effect: str,
    new_fire_effect: str,
    game_db: Dict[str, Any],
) -> None:
    """Replace a weapon with a new one."""
    ammo_db = game_db["ammunition"]

    # Get unit strength from NEW_UNITS
    unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
    unit_strength = None
    for donor, edits in NEW_UNITS.items():
        is_infantry = edits.get("is_infantry", False)
        if edits.get("NewName") == unit_name:
            unit_strength = edits.get("strength")
            break

    if not unit_strength and is_infantry:
        logger.warning(f"No strength found for new unit {unit_name}")
        return

    # Check if this weapon should use strength variants
    use_strength = False
    for (weapon_name, category, _, _), data in small_arms_weapons.items():
        if weapon_name == new_ammo and category == "small_arms":
            damage_family = data.get("Ammunition", {}).get("Arme", {}).get("Family")
            use_strength = damage_family in ["DamageFamily_sa_full", "DamageFamily_sa_intermediate"]
            break

    # Iterate through turrets and weapons to find the one to replace
    for descr_row in new_weap_row.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(descr_row.v):
            continue

        for weapon_descr_row in descr_row.v.by_member("MountedWeaponDescriptorList").v:
            if not isinstance(weapon_descr_row.v, ndf.model.Object):
                continue

            current_ammo = weapon_descr_row.v.by_member("Ammunition").v
            current_base_ammo = current_ammo.split("_", 1)[1]  # Just get the base name after $/GFX/Weapon/Ammo_
            current_base_ammo = re.sub(r"_strength\d+", "", current_base_ammo)  # Remove strength identifier
            current_base_ammo = re.sub(r"_x\d+$", "", current_base_ammo)  # Remove quantity identifier if present
            new_name = ammo_db["renames_old_new"].get(current_base_ammo, None)

            # Check if this is the weapon to replace
            if current_base_ammo == old_ammo or new_name == old_ammo:
                # Update ammo path with quantity and strength if needed
                prefix = current_ammo.split("_", 1)[0]  # Get $/GFX/Weapon/Ammo part
                quantity = int(weapon_descr_row.v.by_m("NbWeapons").v)

                if quantity > 1:
                    if use_strength:
                        new_ammo_path = f"{prefix}_{new_ammo}_strength{unit_strength}_x{quantity}"
                    else:
                        new_ammo_path = f"{prefix}_{new_ammo}_x{quantity}"
                else:
                    if use_strength:
                        new_ammo_path = f"{prefix}_{new_ammo}_strength{unit_strength}"
                    else:
                        new_ammo_path = f"{prefix}_{new_ammo}"

                weapon_descr_row.v.by_m("Ammunition").v = new_ammo_path
                logger.debug(f"Replaced weapon with {new_ammo} using ammo path {new_ammo_path}")

                if old_fire_effect and new_fire_effect:
                    fire_effect_val = strip_quotes(weapon_descr_row.v.by_m("EffectTag").v)
                    current_fire_effect = fire_effect_val.replace("FireEffect_", "")
                    weapon_descr_row.v.by_m("EffectTag").v = f"'FireEffect_{new_fire_effect}'"
                    logger.debug(f"Replaced fire effect {current_fire_effect} with {new_fire_effect}")
                break


def _update_weapon_quantity(new_weap_row: Any, ammo: str, quantity: int, game_db: Dict[str, Any]) -> None:
    """Update the quantity of a weapon in the weapon descriptor."""
    ammo_db = game_db["ammunition"]
    old_ammo = ammo_db["renames_new_old"].get(ammo, None)

    # Get unit strength from NEW_UNITS
    unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
    unit_strength = None
    for donor, edits in NEW_UNITS.items():
        is_infantry = edits.get("is_infantry", False)
        if edits.get("NewName") == unit_name:
            unit_strength = edits.get("strength")
            break

    if not unit_strength and is_infantry:
        logger.warning(f"No strength found for new unit {unit_name}")
        return

    for descr_row in new_weap_row.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(descr_row.v):
            continue

        for weapon_descr_row in descr_row.v.by_member("MountedWeaponDescriptorList").v:
            if not isinstance(weapon_descr_row.v, ndf.model.Object):
                continue

            current_ammo = weapon_descr_row.v.by_member("Ammunition").v
            current_base_ammo = current_ammo.split("_", 1)[1]  # Just get the base name after $/GFX/Weapon/Ammo_

            # Check both current name and old name
            if current_base_ammo == ammo or (old_ammo and current_base_ammo == old_ammo):
                # Update NbWeapons
                weapon_descr_row.v.by_m("NbWeapons").v = str(quantity)

                # Update ammo name with quantity only for small arms
                is_small_arm = _should_use_strength_variant(ammo, game_db)

                if is_small_arm:
                    prefix = current_ammo.split("_", 1)[0]
                    if _should_use_strength_variant(ammo, game_db):
                        if quantity > 1:
                            new_ammo = f"{prefix}_{ammo}_strength{unit_strength}_x{quantity}"
                        else:
                            new_ammo = f"{prefix}_{ammo}_strength{unit_strength}"
                    else:
                        if quantity > 1:
                            new_ammo = f"{prefix}_{ammo}_x{quantity}"
                        else:
                            new_ammo = f"{prefix}_{ammo}"
                    weapon_descr_row.v.by_m("Ammunition").v = new_ammo
                    logger.debug(f"Updated quantity and name for small arm {ammo} to {new_ammo} (x{quantity})")
                else:
                    logger.debug(f"Updated quantity for {ammo} to {quantity}")
                break


def _update_weapon_salvo(new_weap_row: Any, ammo: str, salvo: int, game_db: Dict[str, Any]) -> None:
    """Update the salvo of a weapon in the weapon descriptor."""
    ammo_db = game_db["ammunition"]
    old_ammo = ammo_db["renames_new_old"].get(ammo, None)

    # Get unit strength from NEW_UNITS
    unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
    unit_strength = None
    for donor, edits in NEW_UNITS.items():
        is_infantry = edits.get("is_infantry", False)
        if edits.get("NewName") == unit_name:
            unit_strength = edits.get("strength")
            break

    if not unit_strength and is_infantry:
        logger.warning(f"No strength found for new unit {unit_name}")
        return

    if ammo != "add":
        for descr_row in new_weap_row.v.by_member("TurretDescriptorList").v:
            if not is_valid_turret(descr_row.v):
                continue

            for weapon_descr_row in descr_row.v.by_member("MountedWeaponDescriptorList").v:
                if not isinstance(weapon_descr_row.v, ndf.model.Object):
                    continue

                current_ammo = weapon_descr_row.v.by_member("Ammunition").v
                current_base_ammo = current_ammo.split("_", 1)[1]  # Just get the base name after $/GFX/Weapon/Ammo_
                current_base_ammo = re.sub(r"_strength\d+", "", current_base_ammo)  # Remove strength identifier
                current_base_ammo = re.sub(r"_x\d+$", "", current_base_ammo)  # Remove quantity identifier if present

                if current_base_ammo == ammo or (old_ammo and current_base_ammo == old_ammo):
                    salves_list = new_weap_row.v.by_member("Salves").v
                    if isinstance(salves_list, ndf.model.List):
                        salvo_to_replace = int(weapon_descr_row.v.by_member("SalvoStockIndex").v)
                        logger.debug(f"Updating salvo for {ammo} to {salvo} at index {salvo_to_replace}")
                        salves_list.replace(salvo_to_replace, str(salvo))
                    break
    else:
        # handle additions first to prevent errors trying to update a salvo index out of range.
        salves_list = new_weap_row.v.by_member("Salves").v
        for addition in salvo:
            index, salvo = addition[0], addition[1]
            salves_list.insert(index, str(salvo))


def _should_use_strength_variant(weapon_name: str, game_db: Dict[str, Any]) -> bool:
    """Check if a weapon should use strength variants based on its damage family.

    Args:
        weapon_name: Name of the weapon to check
        game_db: Game database containing ammunition data

    Returns:
        bool: True if weapon should use strength variants
    """
    for (ammo_name, category, _, _), data in small_arms_weapons.items():
        if ammo_name == weapon_name and category == "small_arms":
            damage_family = data.get("Ammunition", {}).get("Arme", {}).get("Family")
            return damage_family in ["DamageFamily_sa_full", "DamageFamily_sa_intermediate"]
    return False


def _update_unmodified_weapons(new_weap_row: Any, game_db: Dict[str, Any]) -> None:
    """Update unmodified weapons to ensure correct strength variants."""
    # Get unit strength from NEW_UNITS
    unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
    unit_strength = None
    for donor, edits in NEW_UNITS.items():
        is_infantry = edits.get("is_infantry", False)
        if edits.get("NewName") == unit_name:
            unit_strength = edits.get("strength")
            break

    if not unit_strength and is_infantry:
        logger.warning(f"No strength found for new unit {unit_name}")
        return

    for descr_row in new_weap_row.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(descr_row.v):
            continue

        for weapon_descr_row in descr_row.v.by_member("MountedWeaponDescriptorList").v:
            if not isinstance(weapon_descr_row.v, ndf.model.Object):
                continue

            current_ammo = weapon_descr_row.v.by_member("Ammunition").v
            current_base_ammo = current_ammo.split("_", 1)[1]  # Just get base name after $/GFX/Weapon/Ammo_

            # Check if this weapon should use strength variants
            use_strength = False
            for (weapon_name, category, _, _), data in small_arms_weapons.items():
                if weapon_name == current_base_ammo and category == "small_arms":
                    damage_family = data.get("Ammunition", {}).get("Arme", {}).get("Family")
                    use_strength = damage_family in ["DamageFamily_sa_full", "DamageFamily_sa_intermediate"]
                    break

            if use_strength:
                prefix = current_ammo.split("_", 1)[0]
                quantity = int(weapon_descr_row.v.by_m("NbWeapons").v)

                if quantity > 1:
                    new_ammo = f"{prefix}_{current_base_ammo}_strength{unit_strength}_x{quantity}"
                else:
                    new_ammo = f"{prefix}_{current_base_ammo}_strength{unit_strength}"

                weapon_descr_row.v.by_m("Ammunition").v = new_ammo
                logger.debug(f"Updated unmodified weapon {current_base_ammo} to use strength variant: {new_ammo}")
