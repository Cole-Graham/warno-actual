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
                    
                _modify_weapon(weapon_descr_row, new_weap_row, edits)
        
        source_path.add(new_weap_row)
        logger.info(f"Added weapon descriptor for {edits['NewName']}")

def _modify_weapon(weapon_descr_row: Any, new_weap_row: Any, edits: Dict[str, Any]) -> None:
    """Modify weapon properties."""
    # Handle salvos
    if "Salves" in edits:
        salvo_index = int(weapon_descr_row.v.by_member("SalvoStockIndex").v)
        salves_list = new_weap_row.v.by_member("Salves").v
        if isinstance(salves_list, ndf.model.List):
            salves_list.replace(salvo_index, str(edits["Salves"][salvo_index]))
            logger.debug(f"Changed salvos to {edits['Salves'][salvo_index]}")
    
    # Handle weapon quantities
    ammo_value = weapon_descr_row.v.by_member("Ammunition").v
    ammo_keys = [
        ("weapon1", "weapon1_quantity"),
        ("weapon2", "weapon2_quantity"),
        ("weapon3", "weapon3_quantity"),
        ("weapon4", "weapon4_quantity")
    ]
    
    for ammo_key, quantity_key in ammo_keys:
        ammo_val = edits.get(ammo_key)
        quantity_val = edits.get(quantity_key)
        if ammo_val is not None and quantity_val is not None and ammo_value == ammo_val:
            weapon_descr_row.v.by_member("NbWeapons").v = quantity_val
            logger.debug(f"Set {ammo_key} quantity to {quantity_val}")
            break 