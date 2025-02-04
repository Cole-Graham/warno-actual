"""Functions for creating new weapon descriptors."""

from typing import Any, Dict

from src import ndf
from src.constants.new_units import NEW_UNITS
from src.constants.weapons.ammunition.small_arms import weapons as small_arms_weapons
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_valid_turret

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
                
                # Handle replacements
                if "replace" in changes:
                    for old_ammo, new_ammo in changes["replace"]:
                        _replace_weapon(new_weap_row, old_ammo, new_ammo, game_db)
                        
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


def _replace_weapon(new_weap_row: Any, old_ammo: str, new_ammo: str, game_db: Dict[str, Any]) -> None:
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
    
    for descr_row in new_weap_row.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(descr_row.v):
            continue
            
        for weapon_descr_row in descr_row.v.by_member("MountedWeaponDescriptorList").v:
            if not isinstance(weapon_descr_row.v, ndf.model.Object):
                continue
                
            if weapon_descr_row.v.by_member("Ammunition").v.split("_", 1)[1] == ammo or (old_ammo and weapon_descr_row.v.by_member("Ammunition").v.split("_", 1)[1] == old_ammo):
                salves_list = new_weap_row.v.by_member("Salves").v
                if isinstance(salves_list, ndf.model.List):
                    salves_list.replace(int(weapon_descr_row.v.by_member("SalvoStockIndex").v), str(salvo))
                    logger.debug(f"Updated salvo for {ammo} to {salvo}")
                break
