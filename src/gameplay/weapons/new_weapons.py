"""Functions for creating new weapon descriptors."""

import re
from typing import Any, Dict

from src import ndf
from src.constants.new_units import NEW_UNITS
from src.constants.weapons.ammunition.small_arms import weapons as small_arms_weapons
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_valid_turret, strip_quotes

logger = setup_logger(__name__)


def create_new_weapons(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Create weapon descriptors for new units."""
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
                
                # Handle additions
                if "add" in changes:
                    for ammo in changes["add"]:
                        _add_weapon(source_path, changes, new_weap_row, ammo, game_db)
                
                # Handle replacements
                if "replace" in changes:
                    for old_ammo, new_ammo in changes["replace"]:
                        _replace_weapon(changes, new_weap_row, old_ammo, new_ammo, game_db)
                        
                # Handle quantities
                if "quantity" in changes:
                    for ammo, quantity in changes["quantity"].items():
                        _update_weapon_quantity(new_weap_row, ammo, quantity, game_db)
            
            # Handle salvos
            if "Salves" in weapon_edits:
                for ammo, salvo in weapon_edits["Salves"].items():
                    _update_weapon_salvo(new_weap_row, ammo, salvo, game_db)
        
        source_path.add(new_weap_row)
        logger.info(f"Added weapon descriptor for {edits['NewName']}")

def _add_weapon(
    source_path: Any,
    changes: Dict[str, Any],
    new_weap_row: Any, 
    ammo: str,
    game_db: Dict[str, Any]
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
    turret_index = changes["add"][0][0]  # First element's turret index
    weapon_name = changes["add"][0][1]   # First element's weapon name
    
    # check if weapon is renamed
    old_name = ammo_db["renames_new_old"].get(weapon_name, None)
    
    # Find matching weapon in database to use as template
    template_found = False
    for descr_name, descr_data in weapon_db.items():
        if old_name and old_name not in descr_data['weapon_locations']:
            continue
        elif not old_name and weapon_name not in descr_data['weapon_locations']:
            continue
            
        # Get weapon location data
        weapon_locations = descr_data['weapon_locations'][old_name or weapon_name]
        if not weapon_locations:
            continue
            
        # Get first location where this weapon appears
        location = weapon_locations[0]  # Contains mounted_index, salvo_index, turret_index
        
        # Find the weapon descriptor in source_path to copy from
        donor_descr = source_path.by_namespace(descr_name)
        if not donor_descr:
            continue
            
        # Get and copy the entire turret containing our template weapon
        donor_turret = donor_descr.v.by_m("TurretDescriptorList").v[location['turret_index']]
        if not is_valid_turret(donor_turret.v):
            continue
            
        # Create new turret by copying template
        new_turret = donor_turret.copy()
        
        # Update weapon indices
        mounted_wpns = new_turret.v.by_m("MountedWeaponDescriptorList")
        for weapon in mounted_wpns.v:
            weapon.v.by_m("SalvoStockIndex").v = str(turret_index)
            weapon.v.by_m("HandheldEquipmentKey").v = f"'MeshAlternative_{turret_index + 1}'"
            weapon.v.by_m("WeaponActiveAndCanShootPropertyName").v = f"'WeaponActiveAndCanShoot_{turret_index + 1}'"
            weapon.v.by_m("WeaponIgnoredPropertyName").v = f"'WeaponIgnored_{turret_index + 1}'"
            weapon.v.by_m("WeaponShootDataPropertyName").v = f"['WeaponShootData_0_{turret_index + 1}']"
        
        # Update turret bone index
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

def _replace_weapon(
    changes: Dict[str, Any],   
    new_weap_row: Any,
    old_ammo: str,
    new_ammo: str,
    game_db: Dict[str, Any]
) -> None:
    """Replace a weapon in the weapon descriptor."""
    ammo_db = game_db["ammunition"]
    old_ammo_db = ammo_db["renames_new_old"].get(old_ammo, None)
    
    for descr_row in new_weap_row.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(descr_row.v):
            continue
            
        for weapon_descr_row in descr_row.v.by_member("MountedWeaponDescriptorList").v:
            if not isinstance(weapon_descr_row.v, ndf.model.Object):
                continue
            
            current_ammo = weapon_descr_row.v.by_member("Ammunition").v
            if current_ammo.split("_", 1)[1] == old_ammo or (old_ammo_db and current_ammo.split("_", 1)[1] == old_ammo_db):
                prefix = current_ammo.split("_", 1)[0]
                weapon_descr_row.v.by_m("Ammunition").v = f"{prefix}_{new_ammo}"
                logger.debug(f"Replaced weapon {old_ammo} with {new_ammo}")
                if "fire_effect" in changes:
                    fire_effect_val = strip_quotes(weapon_descr_row.v.by_m("EffectTag").v)
                    for old_fire_effect, new_fire_effect in changes["fire_effect"]:
                        if old_fire_effect == fire_effect_val.replace("FireEffect_", ""):
                            weapon_descr_row.v.by_m("EffectTag").v = "'" + f"FireEffect_{new_fire_effect}" + "'"
                            logger.debug(f"Replaced fire effect{old_fire_effect} with {new_fire_effect}")
                break


def _update_weapon_quantity(new_weap_row: Any, ammo: str, quantity: int, game_db: Dict[str, Any]) -> None:
    """Update the quantity of a weapon in the weapon descriptor."""
    ammo_db = game_db["ammunition"]
    old_ammo = ammo_db["renames_new_old"].get(ammo, None)
    
    for descr_row in new_weap_row.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(descr_row.v):
            continue
            
        for weapon_descr_row in descr_row.v.by_member("MountedWeaponDescriptorList").v:
            if not isinstance(weapon_descr_row.v, ndf.model.Object):
                continue
                
            current_ammo = weapon_descr_row.v.by_member("Ammunition").v
            current_ammo_base = current_ammo.split("_x")[0].split("_", 1)[1]  # Remove prefix and any _x{number} suffix
            
            # Check both current name and old name
            if current_ammo_base == ammo or (old_ammo and current_ammo_base == old_ammo):
                # Update NbWeapons
                weapon_descr_row.v.by_m("NbWeapons").v = quantity
                
                # Update ammo name with quantity only for small arms
                is_small_arm = any(ammo == weapon_name 
                                 for (weapon_name, category, _, _) in small_arms_weapons.keys() 
                                 if category == "small_arms")
                
                if quantity > 1 and is_small_arm:
                    prefix = current_ammo.split("_", 1)[0]  # Get the $/GFX/Weapon/Ammo part
                    new_ammo = f"{prefix}_{ammo}_x{quantity}"  # Always use new name
                    weapon_descr_row.v.by_m("Ammunition").v = new_ammo
                    logger.debug(f"Updated quantity and name for small arm {ammo} to {new_ammo} (x{quantity})")
                else:
                    logger.debug(f"Updated quantity for {ammo} to {quantity}")
                break


def _update_weapon_salvo(new_weap_row: Any, ammo: str, salvo: int, game_db: Dict[str, Any]) -> None:
    """Update the salvo of a weapon in the weapon descriptor."""
    ammo_db = game_db["ammunition"]
    old_ammo = ammo_db["renames_new_old"].get(ammo, None)
    quantity_pattern = re.compile(r'\$/GFX/Weapon/Ammo_(.+?)(?:_x\d{1,2})?$')
    
    if ammo == "add":
        salves_list = new_weap_row.v.by_member("Salves").v
        for addition in salvo:
            index, salvo = addition[0], addition[1]
            salves_list.insert(index, str(salvo))
    else:
        for descr_row in new_weap_row.v.by_member("TurretDescriptorList").v:
            if not is_valid_turret(descr_row.v):
                continue
                
            for weapon_descr_row in descr_row.v.by_member("MountedWeaponDescriptorList").v:
                if not isinstance(weapon_descr_row.v, ndf.model.Object):
                    continue
                
                current_ammo = weapon_descr_row.v.by_member("Ammunition").v
                # Extract base ammo name without quantity suffix
                base_ammo_match = quantity_pattern.match(current_ammo)
                if not base_ammo_match:
                    continue
                    
                base_ammo = base_ammo_match.group(1)
                if base_ammo == ammo or (old_ammo and base_ammo == old_ammo):
                    salves_list = new_weap_row.v.by_member("Salves").v
                    if isinstance(salves_list, ndf.model.List):
                        salves_list.replace(int(weapon_descr_row.v.by_member("SalvoStockIndex").v), str(salvo))
                        logger.debug(f"Updated salvo for {ammo} to {salvo}")
                    break
