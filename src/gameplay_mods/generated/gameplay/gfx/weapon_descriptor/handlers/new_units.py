"""Functions for creating new weapon descriptors."""

import re
from typing import Any, Dict

from src import ndf
from src.constants.new_units import NEW_UNITS
# from src.constants.weapons.ammunition.small_arms import weapons as small_arms_weapons
from src.constants.weapons import ammunitions
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_valid_turret, strip_quotes, is_obj_type

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

        # Log donor turret count before copying
        donor_turret_list = donor_weap.v.by_member("TurretDescriptorList")
        donor_turret_count = len(donor_turret_list.v) if donor_turret_list.v else 0
        unit_name = edits.get("NewName", donor_name)
        logger.debug(f"Donor {donor_name} turret count: {donor_turret_count}")

        new_weap_row = donor_weap.copy()
        new_weap_row.namespace = f"WeaponDescriptor_{edits['NewName']}"

        # Handle weapon modifications if present
        if "WeaponDescriptor" in edits:
            weapon_edits = edits["WeaponDescriptor"]

            # Handle equipment changes
            if "equipmentchanges" in weapon_edits:
                changes = weapon_edits["equipmentchanges"]
                
                # Log initial turret count after copy
                initial_turret_list = new_weap_row.v.by_member("TurretDescriptorList")
                initial_turret_count = len(initial_turret_list.v) if initial_turret_list.v else 0
                logger.debug(f"Initial turret count for {unit_name} after copy: {initial_turret_count}")

                # Handle insertions
                if "insert" in changes:
                    for weapon_tuple in changes["insert"]:
                        _insert_weapon(source_path, weapon_tuple, new_weap_row, changes, edits, game_db)
                    
                    # Log turret count after insertions
                    after_insert_turret_list = new_weap_row.v.by_member("TurretDescriptorList")
                    after_insert_turret_count = len(after_insert_turret_list.v) if after_insert_turret_list.v else 0
                    logger.debug(f"Turret count for {unit_name} after insertions: {after_insert_turret_count}")

                # Apply insert_edits to all turrets at the specified indices (both newly inserted and bumped)
                if "insert_edits" in changes:
                    _apply_insert_edits_to_turrets(new_weap_row, changes["insert_edits"])

                # Handle index adjustments for bumped weapons in turret and mounted weapon lists
                if "update" in changes:
                    _update_weapon(changes, new_weap_row)
                    
                # Handle replacements
                if "replace_with_turret" in changes:
                    for replacement in changes["replace_with_turret"]:
                        if len(replacement) == 4:
                            old_weapon_name, new_weapon_name, old_fire_effect, new_fire_effect = replacement
                            _replace_weapon_with_turret(source_path, new_weap_row, changes, edits, game_db, old_weapon_name, new_weapon_name, new_fire_effect)
                        else:
                            old_weapon_name, new_weapon_name = replacement
                            _replace_weapon_with_turret(source_path, new_weap_row, changes, edits, game_db, old_weapon_name, new_weapon_name, new_weapon_name)
                        
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

                # Handle HAGRU MANPADS
                if "HAGRU_MANPADS" in changes:
                    for turret_index, donor_weapon_index, hagru_ammo in changes["HAGRU_MANPADS"]:
                        _add_hagru_manpads(new_weap_row, turret_index, donor_weapon_index, hagru_ammo)

                # Handle quantities
                if "quantity" in changes:
                    for ammo, quantity in changes["quantity"].items():
                        _update_weapon_quantity(new_weap_row, ammo, quantity, game_db)

            # Handle turrets
            if "turrets" in weapon_edits:
                for turret_index, turret_edits in weapon_edits["turrets"].items():
                    _update_turret(new_weap_row, turret_index, turret_edits, game_db)

            # Handle salvos
            if "Salves" in weapon_edits:
                salve_edits = weapon_edits["Salves"]
                # Handle insertions first to prevent index errors
                if "insert" in salve_edits:
                    salves_list = new_weap_row.v.by_member("Salves").v
                    if isinstance(salves_list, ndf.model.List):
                        insert_list = salve_edits["insert"]
                        # Sort by index in descending order to insert highest indices first
                        sorted_insert_list = sorted(insert_list, key=lambda x: x[0], reverse=True)
                        for addition in sorted_insert_list:
                            index, salvo_val = addition[0], addition[1]
                            logger.debug(f"Inserting salvo {salvo_val} at index {index}")
                            salves_list.insert(index, str(salvo_val))
                
                # Handle other salvo updates
                for ammo, salvo in salve_edits.items():
                    if ammo == "insert":
                        continue
                    _update_weapon_salvo(new_weap_row, ammo, salvo, game_db)
            
            if "SalvoIsMainSalvo" in weapon_edits:
                new_weap_row.v.by_m("SalvoIsMainSalvo").v = ndf.convert(str(weapon_edits["SalvoIsMainSalvo"]))

        # Update any unmodified weapons that should use strength variants
        _update_unmodified_weapons(new_weap_row, game_db)

        source_path.add(new_weap_row)
        logger.info(f"Added weapon descriptor for {edits['NewName']}")


def _extract_base_ammo_name(weapon_name: str) -> str:
    """Extract the base ammo name by removing salvo length, quantity, and strength variants.
    
    Args:
        weapon_name: Weapon name that may contain variants like _salvolength{N}, _x{N}, _strength{N}
        
    Returns:
        Base weapon name without variant suffixes
    """
    # Remove salvo length variants: _salvolength{N} or _x{N}
    base_name = re.sub(r'_salvolength\d+$', '', weapon_name)
    base_name = re.sub(r'_x\d+$', '', base_name)
    # Remove strength variants: _strength{N}
    base_name = re.sub(r'_strength\d+$', '', base_name)
    return base_name


def _find_turret_template_by_base_ammo(
    source_path: Any,
    weapon_db: Dict[str, Any],
    base_ammo_name: str,
    weapon_name: str,
) -> tuple[Any, int] | None:
    """Find a turret template by searching for weapons with the same base ammo name.
    
    Args:
        source_path: The NDF file being edited
        weapon_db: Game database containing weapon locations
        base_ammo_name: Base ammo name to search for (without variants)
        weapon_name: Original weapon name (for logging)
        
    Returns:
        Tuple of (donor_turret, turret_index) if found, None otherwise
    """
    # Search through all weapon descriptors for weapons with matching base name
    for descr_name, descr_data in weapon_db.items():
        # Check all weapons in this descriptor
        for weapon_in_db, weapon_locations in descr_data["weapon_locations"].items():
            # Extract base name from weapon in database
            weapon_base = _extract_base_ammo_name(weapon_in_db)
            
            # If base names match, use this weapon's turret
            if weapon_base == base_ammo_name and weapon_locations:
                location = weapon_locations[0]  # Get first location
                
                # Find the weapon descriptor in source_path
                donor_descr = source_path.by_namespace(descr_name)
                if not donor_descr:
                    continue
                
                # Get the turret containing this weapon
                donor_turret = donor_descr.v.by_m("TurretDescriptorList").v[location["turret_index"]]
                if is_valid_turret(donor_turret.v):
                    logger.debug(f"Found turret template for {weapon_name} using base ammo {base_ammo_name} from {weapon_in_db}")
                    return (donor_turret, location["turret_index"])
    
    return None


def _insert_weapon(
    source_path: Any, weapon_tuple: tuple, new_weap_row: Any, changes: Dict[str, Any], edits: Dict[str, Any], game_db: Dict[str, Any]
) -> None:
    """Insert a weapon turret at a specific index in the weapon descriptor.

    Args:
        source_path: The NDF file being edited
        weapon_tuple: Tuple containing (turret_index, weapon_name, fire_effect) where turret_index is the insertion position
        new_weap_row: The weapon descriptor to modify
        changes: Dictionary containing equipment changes (for quantity information)
        edits: Dictionary containing unit configuration (for strength and unit type)
        game_db: Game database containing weapon and ammunition data
    """
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]

    # Get turret index and weapon name from weapon tuple
    turret_index = weapon_tuple[0]  # Turret index
    weapon_name = weapon_tuple[1]  # Weapon name
    fire_effect = weapon_tuple[2]  # Fire effect
    
    if len(weapon_tuple) == 4:
        new_yul_bone = weapon_tuple[3]
    else:
        new_yul_bone = turret_index + 1

    # Get unit properties from edits (passed from parent function)
    unit_strength = edits.get("strength")
    is_infantry = edits.get("is_infantry", False)
    is_ground_vehicle = edits.get("is_ground_vehicle", False)
    
    # Check if strength is required but missing
    if not unit_strength and is_infantry and not is_ground_vehicle:
        unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
        logger.warning(f"No strength found for new unit {unit_name}")
        return

    # check if weapon is renamed
    old_name = ammo_db["renames_new_old"].get(weapon_name, None)
    
    # If not found in renames, check if it's a salvo weapon that needs conversion
    # Convert _salvolength{N} format to _x{N} format for database lookup
    if not old_name:
        salvo_match = re.match(r'^(.+)_salvolength(\d+)$', weapon_name)
        if salvo_match:
            base_name = salvo_match.group(1)
            salvo_num = salvo_match.group(2)
            old_name = f"{base_name}_x{salvo_num}"

    # Find matching weapon in database to use as template
    template_found = False
    donor_turret = None
    location = None
    
    # First, try exact match
    for descr_name, descr_data in weapon_db.items():
        # Try old_name first (from renames or salvo conversion), then weapon_name
        lookup_name = old_name or weapon_name
        if lookup_name not in descr_data["weapon_locations"]:
            continue

        # Get weapon location data
        weapon_locations = descr_data["weapon_locations"][lookup_name]
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
            unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
            logger.warning(f"Invalid turret {donor_turret.v} for {unit_name}")
            donor_turret = None
            continue
        
        template_found = True
        break
    
    # If exact match not found, try finding by base ammo name (for salvo variants)
    if not template_found:
        base_ammo_name = _extract_base_ammo_name(weapon_name)
        result = _find_turret_template_by_base_ammo(source_path, weapon_db, base_ammo_name, weapon_name)
        if result:
            donor_turret, location_data = result
            # Create a minimal location dict for compatibility
            location = {"turret_index": location_data, "mounted_index": 0, "salvo_index": 0}
            template_found = True
    
    if template_found and donor_turret:
        # Create new turret by copying template
        new_turret = donor_turret.copy()

        # Update weapon indices and add strength to ammo path
        mounted_wpns = new_turret.v.by_m("MountedWeaponDescriptorList")
        for weapon in mounted_wpns.v:
            weapon.v.by_m("EffectTag").v = f"'FireEffect_{fire_effect}'"
            weapon.v.by_m("SalvoStockIndex").v = str(turret_index)
            weapon.v.by_m("HandheldEquipmentKey").v = f"'WeaponAlternative_{new_yul_bone}'"
            weapon.v.by_m("WeaponActiveAndCanShootPropertyName").v = f"'WeaponActiveAndCanShoot_{new_yul_bone}'"
            weapon.v.by_m("WeaponIgnoredPropertyName").v = f"'WeaponIgnored_{new_yul_bone}'"
            weapon.v.by_m("WeaponShootDataPropertyName").v = f"['WeaponShootData_0_{new_yul_bone}']"

            # Update ammo path to include strength
            current_ammo = weapon.v.by_m("Ammunition").v
            prefix = current_ammo.split("_", 1)[0]  # Get $/GFX/Weapon/Ammo part
            quantity = changes.get("quantity", {}).get(weapon_name, int(weapon.v.by_m("NbWeapons").v))

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
        if new_turret.v.by_m("Tag", False) is not None:
            new_turret.v.by_m("Tag").v = f'"tourelle{new_yul_bone}"'
        new_turret.v.by_m("YulBoneOrdinal").v = str(new_yul_bone)

        # Apply insert_edits to the turret template before insertion
        if "insert_edits" in changes:
            insert_edits = changes["insert_edits"].get(turret_index)
            if insert_edits:
                _apply_insert_edits_to_turret_template(new_turret, insert_edits, weapon_name, is_infantry, unit_strength, game_db)

        # Insert into target turret list at the specified index - use same pattern as unit_edits.py
        turret_list = new_weap_row.v.by_member("TurretDescriptorList").v
        
        # TODO: Ulibos gave me updated ndf_parse-0.2.1-py3-none-any.whl in root of repo
        # TODO: This workaround should no longer be needed, will clean up later
        # Workaround for NDF parse bug: insert(0, item) replaces all elements instead of inserting
        # The bug is in ndf_parse model/abc.py line 1175: when key.stop is 0, 
        # "key.stop or len(self.__inner)" evaluates to len(self.__inner) because 0 is falsy
        # So insert(0, item) becomes slice(0, len) which replaces all elements instead of inserting
        # Solution: when inserting at 0 with existing items, rebuild the list with new turret first
        if turret_index == 0 and len(turret_list) > 0:
            # Collect all existing turrets
            existing_turrets = list(turret_list)
            # Clear the list by removing all elements
            turret_list.remove(slice(0, len(turret_list)))
            # Insert the new turret first
            turret_list.add(new_turret)
            # Insert all existing turrets back
            for existing_turret in existing_turrets:
                turret_list.add(existing_turret)
        else:
            turret_list.insert(turret_index, new_turret)

        logger.debug(f"Inserted turret with {weapon_name} at index {turret_index}")
    else:
        if not template_found:
            logger.warning(f"Could not find template for weapon {weapon_name}")


def _replace_weapon_with_turret(
    source_path: Any, new_weap_row: Any, changes: Dict[str, Any], edits: Dict[str, Any], game_db: Dict[str, Any], 
    old_weapon_name: str, new_weapon_name: str, fire_effect: str
) -> None:
    """Replace a weapon and its turret by finding a donor turret.
    
    Args:
        source_path: The NDF file being edited
        new_weap_row: The weapon descriptor to modify
        changes: Dictionary containing equipment changes (for quantity information)
        edits: Dictionary containing unit configuration (for strength and unit type)
        game_db: Game database containing weapon and ammunition data
        old_weapon_name: Name of the weapon to find and replace
        new_weapon_name: Name of the new weapon to use from donor turret
        fire_effect: Fire effect to use for the new weapon
    """
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]
    
    # Get unit properties from edits
    unit_strength = edits.get("strength")
    is_infantry = edits.get("is_infantry", False)
    is_ground_vehicle = edits.get("is_ground_vehicle", False)
    
    # Check if strength is required but missing
    if not unit_strength and is_infantry and not is_ground_vehicle:
        unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
        logger.warning(f"No strength found for new unit {unit_name}")
        return
    
    # Find the turret index containing the old weapon
    turret_index = None
    turret_list = new_weap_row.v.by_member("TurretDescriptorList")
    ammo_db_renames_old_new = ammo_db.get("renames_old_new", {})
    
    for idx, turret in enumerate(turret_list.v):
        if not is_valid_turret(turret.v):
            continue
        
        mounted_weapons = turret.v.by_member("MountedWeaponDescriptorList")
        for weapon_descr_row in mounted_weapons.v:
            if not isinstance(weapon_descr_row.v, ndf.model.Object):
                continue
            
            current_ammo = weapon_descr_row.v.by_member("Ammunition").v
            current_base_ammo = current_ammo.split("_", 1)[1]  # Just get the base name after $/GFX/Weapon/Ammo_
            current_base_ammo = re.sub(r"_strength\d+", "", current_base_ammo)  # Remove strength identifier
            current_base_ammo = re.sub(r"_x\d+$", "", current_base_ammo)  # Remove quantity identifier if present
            new_name = ammo_db_renames_old_new.get(current_base_ammo, None)
            
            # Check if this is the weapon to replace
            if current_base_ammo == old_weapon_name or new_name == old_weapon_name:
                turret_index = idx
                break
        
        if turret_index is not None:
            break
    
    if turret_index is None:
        unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
        logger.warning(f"Could not find turret containing weapon {old_weapon_name} for {unit_name}")
        return
    
    # Get the yul_bone from the existing turret
    existing_turret = turret_list.v[turret_index]
    new_yul_bone = int(existing_turret.v.by_m("YulBoneOrdinal").v)
    
    # Check if new weapon is renamed
    old_name = ammo_db["renames_new_old"].get(new_weapon_name, None)
    
    # If not found in renames, check if it's a salvo weapon that needs conversion
    # Convert _salvolength{N} format to _x{N} format for database lookup
    if not old_name:
        salvo_match = re.match(r'^(.+)_salvolength(\d+)$', new_weapon_name)
        if salvo_match:
            base_name = salvo_match.group(1)
            salvo_num = salvo_match.group(2)
            old_name = f"{base_name}_x{salvo_num}"
    
    # Find matching weapon in database to use as template
    template_found = False
    donor_turret = None
    location = None
    
    # First, try exact match
    for descr_name, descr_data in weapon_db.items():
        lookup_name = old_name or new_weapon_name
        if lookup_name not in descr_data["weapon_locations"]:
            continue
        
        # Get weapon location data
        weapon_locations = descr_data["weapon_locations"][lookup_name]
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
            unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
            logger.warning(f"Invalid turret {donor_turret.v} for {unit_name}")
            donor_turret = None
            continue
        
        template_found = True
        break
    
    # If exact match not found, try finding by base ammo name (for salvo variants)
    if not template_found:
        base_ammo_name = _extract_base_ammo_name(new_weapon_name)
        result = _find_turret_template_by_base_ammo(source_path, weapon_db, base_ammo_name, new_weapon_name)
        if result:
            donor_turret, location_data = result
            # Create a minimal location dict for compatibility
            location = {"turret_index": location_data, "mounted_index": 0, "salvo_index": 0}
            template_found = True
    
    if template_found and donor_turret:
        # Create new turret by copying template
        new_turret = donor_turret.copy()
        
        # Update weapon indices and add strength to ammo path
        mounted_wpns = new_turret.v.by_m("MountedWeaponDescriptorList")
        for weapon in mounted_wpns.v:
            weapon.v.by_m("EffectTag").v = f"'FireEffect_{fire_effect}'"
            weapon.v.by_m("SalvoStockIndex").v = str(turret_index)
            weapon.v.by_m("HandheldEquipmentKey").v = f"'WeaponAlternative_{new_yul_bone}'"
            weapon.v.by_m("WeaponActiveAndCanShootPropertyName").v = f"'WeaponActiveAndCanShoot_{new_yul_bone}'"
            weapon.v.by_m("WeaponIgnoredPropertyName").v = f"'WeaponIgnored_{new_yul_bone}'"
            weapon.v.by_m("WeaponShootDataPropertyName").v = f"['WeaponShootData_0_{new_yul_bone}']"
            
            # Update ammo path to include strength
            current_ammo = weapon.v.by_m("Ammunition").v
            prefix = current_ammo.split("_", 1)[0]  # Get $/GFX/Weapon/Ammo part
            quantity = changes.get("quantity", {}).get(new_weapon_name, int(weapon.v.by_m("NbWeapons").v))
            
            if _should_use_strength_variant(new_weapon_name, game_db):
                if quantity > 1:
                    new_ammo = f"{prefix}_{new_weapon_name}_strength{unit_strength}_x{quantity}"
                else:
                    new_ammo = f"{prefix}_{new_weapon_name}_strength{unit_strength}"
            else:
                if quantity > 1:
                    new_ammo = f"{prefix}_{new_weapon_name}_x{quantity}"
                else:
                    new_ammo = f"{prefix}_{new_weapon_name}"
            weapon.v.by_m("Ammunition").v = new_ammo
            weapon.v.by_m("NbWeapons").v = str(quantity)
        
        # Update turret bone index
        # TODO: turret bone might not always be the same as turret index
        if new_turret.v.by_m("Tag", False) is not None:
            new_turret.v.by_m("Tag").v = f'"tourelle{new_yul_bone}"'
        new_turret.v.by_m("YulBoneOrdinal").v = str(new_yul_bone)
        
        # Replace the turret at the found index
        turret_list.v[turret_index] = new_turret
        
        logger.debug(f"Replaced turret at index {turret_index} containing {old_weapon_name} with turret containing {new_weapon_name}")
    elif not template_found:
        logger.warning(f"Could not find template for weapon {new_weapon_name}")


def _update_weapon(
    changes: Dict[str, Any],
    new_weap_row: Any,
) -> None:
    """Update index values for bumped weapons in turret and mounted weapon lists."""
    updates = changes["update"]
    turret_list = new_weap_row.v.by_member("TurretDescriptorList")
    for turret_index in updates:
        # Check if turret index exists before accessing
        if turret_index >= len(turret_list.v):
            unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
            logger.error(f"Turret index {turret_index} out of range for {unit_name} (only {len(turret_list.v)} turrets exist)")
            continue
        
        turret = turret_list.v[turret_index]
        turret.v.by_m("YulBoneOrdinal").v = str(turret_index + 1)
        mounted_weapons = turret.v.by_member("MountedWeaponDescriptorList")
        for weapon in mounted_weapons.v:
            weapon.v.by_m("SalvoStockIndex").v = str(turret_index)
            weapon.v.by_m("HandheldEquipmentKey").v = f"'WeaponAlternative_{turret_index + 1}'"
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
        is_ground_vehicle = edits.get("is_ground_vehicle", False)
        if edits.get("NewName") == unit_name:
            unit_strength = edits.get("strength")
            break

    # I classify towed equipment as both ground vehicle and infantry, but they never have small arms.
    if not unit_strength and is_infantry and not is_ground_vehicle:
        logger.warning(f"No strength found for new unit {unit_name}")
        return

    # # Check if this weapon should use strength variants
    # use_strength = False
    # for (weapon_name, category, _, _), data in small_arms_weapons.items():
    #     if weapon_name == new_ammo and category == "small_arms":
    #         damage_family = data.get("Ammunition", {}).get("Arme", {}).get("Family")
    #         use_strength = damage_family in ["DamageFamily_sa_full", "DamageFamily_sa_intermediate"]
    #         break

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
                    if _should_use_strength_variant(new_ammo, game_db):
                        new_ammo_path = f"{prefix}_{new_ammo}_strength{unit_strength}_x{quantity}"
                    else:
                        new_ammo_path = f"{prefix}_{new_ammo}_x{quantity}"
                else:
                    if _should_use_strength_variant(new_ammo, game_db):
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
        is_ground_vehicle = edits.get("is_ground_vehicle", False)
        if edits.get("NewName") == unit_name:
            unit_strength = edits.get("strength")
            break

    if not unit_strength and is_infantry and not is_ground_vehicle:
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
        is_ground_vehicle = edits.get("is_ground_vehicle", False)
        if edits.get("NewName") == unit_name:
            unit_strength = edits.get("strength")
            break

    if not unit_strength and is_infantry and not is_ground_vehicle:
        logger.warning(f"No strength found for new unit {unit_name}")
        return

    # Skip special control keys (insert is handled separately before this function is called)
    if ammo in ("insert", "remove"):
        return

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
                    # Check if index is valid before replacing
                    if salvo_to_replace < len(salves_list):
                        logger.debug(f"Updating salvo for {ammo} to {salvo} at index {salvo_to_replace}")
                        salves_list.replace(salvo_to_replace, str(salvo))
                    else:
                        logger.warning(f"Salvo index {salvo_to_replace} out of range for {ammo} (list has {len(salves_list)} elements)")
                break


def _should_use_strength_variant(weapon_name: str, game_db: Dict[str, Any]) -> bool:
    """Check if a weapon should use strength variants based on its damage family.

    Args:
        weapon_name: Name of the weapon to check
        game_db: Game database containing ammunition data

    Returns:
        bool: True if weapon should use strength variants
    """
    ammo_properties = game_db["ammunition"]["ammo_properties"].get(f"Ammo_{weapon_name}", {})
    is_crew_or_vehicle_weapon = ammo_properties.get("MinMaxCategory", None) == "MinMax_MMG_HMG"
    if is_crew_or_vehicle_weapon:
        return False
    
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
        is_ground_vehicle = edits.get("is_ground_vehicle", False)
        if edits.get("NewName") == unit_name:
            unit_strength = edits.get("strength")
            break

    if not unit_strength and is_infantry and not is_ground_vehicle:
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
                ammo_properties = game_db["ammunition"]["ammo_properties"].get(f"Ammo_{weapon_name}", {})
                is_crew_or_vehicle_weapon = ammo_properties.get("MinMaxCategory", None) == "MinMax_MMG_HMG"
                
                if weapon_name == current_base_ammo and category == "small_arms" and not is_crew_or_vehicle_weapon:
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


def _apply_insert_edits_to_turret_template(
    turret_template: Any,
    insert_edits: Dict[str, Any],
    weapon_name: str,
    is_infantry: bool,
    unit_strength: int,
    game_db: Dict[str, Any],
) -> None:
    """Apply insert_edits to a turret template before insertion.
    
    Args:
        turret_template: The turret template to modify
        insert_edits: Dictionary containing edits to apply
        weapon_name: Name of the weapon being inserted
        is_infantry: Whether the unit is infantry
        unit_strength: Unit strength value
        game_db: Game database containing weapon and ammunition data
    """
    # Apply turret edits
    if "turret_edits" in insert_edits:
        for membr, value in insert_edits["turret_edits"].items():
            turret_template.v.by_m(membr).v = str(value)
    
    # Apply mounted weapon edits
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
                if _should_use_strength_variant(base_ammo, game_db):
                    quantity = int(mounted_weapon.v.by_m("NbWeapons").v)
                    prefix = "$/GFX/Weapon/Ammo_"
                    
                    if quantity > 1:
                        new_ammo = f"{prefix}{base_ammo}_strength{unit_strength}_x{quantity}"
                    else:
                        new_ammo = f"{prefix}{base_ammo}_strength{unit_strength}"
                    
                    mounted_weapon.v.by_m("Ammunition").v = new_ammo
                    logger.debug(f"Applied strength variant for infantry small arm {base_ammo}: {new_ammo}")


def _apply_insert_edits_to_turrets(new_weap_row: Any, insert_edits: Dict[int, Dict[str, Any]]) -> None:
    """Apply insert_edits to all turrets at the specified indices (both newly inserted and bumped).
    
    Args:
        new_weap_row: The weapon descriptor to modify
        insert_edits: Dictionary keyed by turret index containing edits to apply
    """
    turret_list = new_weap_row.v.by_member("TurretDescriptorList").v
    
    for edit_index, edits in insert_edits.items():
        if edit_index >= len(turret_list):
            unit_name = new_weap_row.namespace.replace("WeaponDescriptor_", "")
            logger.warning(f"Turret index {edit_index} out of range for {unit_name} (only {len(turret_list)} turrets exist)")
            continue
        
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


def _update_turret(new_weap_row: Any, turret_index: int, turret_edits: Dict[str, Any], game_db: Dict[str, Any]) -> None:
    """Update turret properties for new units."""
    turret_list = new_weap_row.v.by_member("TurretDescriptorList")
    turret = turret_list.v[turret_index]
    
    # Handle MountedWeapons insertions
    if "MountedWeapons" in turret_edits and "insert" in turret_edits["MountedWeapons"]:
        if not is_valid_turret(turret.v):
            logger.warning(f"Turret {turret_index} is not valid for inserting mounted weapons")
        else:
            prefix = "$/GFX/Weapon/Ammo_"
            mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList")
            
            for weapon in mounted_wpns.v:
                if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                    continue
                
                ammunition = weapon.v.by_m("Ammunition").v.split(prefix)[1]
                
                for donor, donor_edits in turret_edits["MountedWeapons"]["insert"].items():
                    if ammunition != donor:
                        continue
                    
                    # Copy the weapon and apply edits
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
                    logger.debug(f"Inserted mounted weapon {donor} to turret {turret_index}")

    # turret property edits
    for membr, value in turret_edits.items():
        if membr == "MountedWeapons":
            continue
        else:
            turret_list.v[turret_index].v.by_m(membr).v = str(value)