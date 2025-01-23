"""Functions for creating new weapon descriptors."""

from typing import Any, Dict

from src import ndf
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_valid_turret

logger = setup_logger(__name__)

def create_new_weapons(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Create weapon descriptors for new units."""
    logger.info("Creating weapon descriptors for new units")
    
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits or edits.get("is_unarmed", False):
            continue
            
        # Clone donor weapon descriptor
        donor_weap = source_path.by_namespace(f"WeaponDescriptor_{donor}")
        if not donor_weap:
            logger.warning(f"Weapon descriptor not found for donor {donor}")
            continue
            
        new_weap_row = donor_weap.copy()
        new_weap_row.namespace = f"WeaponDescriptor_{edits['NewName']}"
        
        # Modify weapon properties
        for descr_row in new_weap_row.v.by_member("TurretDescriptorList").v:
            if not is_valid_turret(descr_row.v):
                continue
                
            for weapon_descr_row in descr_row.v.by_member("MountedWeaponDescriptorList").v:
                if not isinstance(weapon_descr_row.v, ndf.model.Object):
                    continue
                    
                _modify_weapon(weapon_descr_row, new_weap_row, edits, game_db)
        
        source_path.add(new_weap_row)
        logger.info(f"Added weapon descriptor for {edits['NewName']}")

def _modify_weapon(
    weapon_descr_row: Any,
    new_weap_row: Any,
    edits: Dict[str, Any],
    game_db: Dict[str, Any],
) -> None:
    """Modify weapon properties for new WeaponDescriptor."""
    
    ammo_db = game_db["ammunition"]
    # check to see if the ammo has been renamed
    def get_ammo_name(ammo_value: Any,
                      ammo_db: Dict[str, Any],
                      log_count: int
    ) -> str:
        """Compare ammo values and return the correct name with prefix.
        e.g. '$/GFX/Weapon/Ammo_PM_M4_Carbine'"""
        logger.debug(f"Checking weapon key {log_count}")
        stripped_ammo_value = ammo_value.split("_", 1)[1]
        if stripped_ammo_value in ammo_db["renames_new_old"]:
            logger.debug(f"Found old ammo name for {stripped_ammo_value}")
            return ammo_db["renames_new_old"][stripped_ammo_value]
        else:
            logger.debug(f"No old name found for {stripped_ammo_value}")
            return None
    
    # Handle salvos
    if "Salves" in edits:
        salvo_index = int(weapon_descr_row.v.by_member("SalvoStockIndex").v)
        salves_list = new_weap_row.v.by_member("Salves").v
        if isinstance(salves_list, ndf.model.List):
            salves_list.replace(salvo_index, str(edits["Salves"][salvo_index]))
            logger.debug(f"Changed salves index {salvo_index} to "
                         f"{edits['Salves'][salvo_index]}")
    
    # Handle weapon quantities
    ammo_keys = [
        ("weapon1", "weapon1_quantity"),
        ("weapon2", "weapon2_quantity"),
        ("weapon3", "weapon3_quantity"),
        ("weapon4", "weapon4_quantity")
    ]
    
    log_count = 1
    for ammo_key, quantity_key in ammo_keys:
        ammo_value = weapon_descr_row.v.by_member("Ammunition").v
        ammo_val = edits.get(ammo_key)
        quantity_val = edits.get(quantity_key)
        old_name = get_ammo_name(ammo_value, ammo_db, log_count)
        if old_name is not None:
            old_name_val = "$/GFX/Weapon/Ammo_" + old_name
        if ammo_val is not None and quantity_val is not None and ammo_value == ammo_val:
            nb_weapons = weapon_descr_row.v.by_member("NbWeapons")
            
            # update quantity
            if int(nb_weapons.v) != quantity_val:
                if quantity_val > 1: # hijacking this function to change ammo name quantity
                    new_ammo = ammo_val + "_x" + str(quantity_val)
                    weapon_descr_row.v.by_m("Ammunition").v = new_ammo

                weapon_descr_row.v.by_m("NbWeapons").v = quantity_val
                logger.debug(f"Set {ammo_key} ({ammo_val}) quantity to {quantity_val}\n")
                break 
           
            else:
                if quantity_val > 1: # hijacking this function to change ammo name quantity
                    new_ammo = ammo_val + "_x" + str(quantity_val)
                    weapon_descr_row.v.by_m("Ammunition").v = new_ammo
                
                logger.debug("Weapon already has the correct quantity for "
                             f"{ammo_key} ({ammo_val})")
                break
        
        elif old_name and ammo_val is not None and quantity_val is not None:
            if old_name_val == ammo_val and quantity_val > 1:
                new_ammo = old_name_val + "_x" + str(quantity_val)
                weapon_descr_row.v.by_m("Ammunition").v = new_ammo
                logger.debug(f"Updated ammo name for {ammo_key} to {new_ammo}")
                break
            # split_ammo_value = ammo_value.split("_", 1)
            # if old_name_val == split_ammo_value[1] and quantity_val > 1:
            #     new_ammo = split_ammo_value[0] + "_x" + str(quantity_val)
            #     weapon_descr_row.v.by_m("Ammunition").v = new_ammo
            #     logger.debug(f"Updated ammo name for {ammo_key} to {new_ammo}")
            #     break
        else:
            logger.debug(f"No ammo name found for {ammo_val}")
            log_count += 1
