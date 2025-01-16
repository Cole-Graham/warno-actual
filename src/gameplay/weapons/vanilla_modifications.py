"""Functions for modifying vanilla ammunition instances."""

from typing import Any, Dict, List, Tuple

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def apply_vanilla_renames(source: Any, renames: List[Tuple[str, str]], ammo_db: Dict[str, Any]) -> None:
    """Apply vanilla ammunition renames.
    
    Args:
        source: NDF file containing weapon descriptors
        renames: List of (old_name, new_name) tuples
        ammo_db: Ammunition database containing salvo weapon mappings
    """
    for ammo_descr in source:
        if not hasattr(ammo_descr, 'namespace') or 'Ammo_' not in ammo_descr.namespace:
            continue
            
        old_name = ammo_descr.namespace.split("Ammo_", 1)[1]
        
        # Check if this is a salvo weapon that needs renaming
        if old_name in ammo_db["salvo_weapons"]:
            new_name = ammo_db["salvo_weapons"][old_name]
            logger.info(f"Renaming salvo weapon {old_name} to {new_name}")
            ammo_descr.namespace = f"Ammo_{new_name}"
            continue
        
        # Then check regular renames
        for old, new in renames:
            if old_name == old:
                logger.info(f"Renaming {old_name} to {new}")
                ammo_descr.namespace = f"Ammo_{new}"
                break


def vanilla_renames_weapondescriptor(source: Any, renames: List[Tuple[str, str]], ammo_db: Dict[str, Any], weapon_db: Dict[str, Any]) -> None:
    """Apply vanilla weapon descriptor renames.
    
    Args:
        source: NDF file containing weapon descriptors
        renames: List of (old_name, new_name) tuples
        ammo_db: Ammunition database containing salvo weapon mappings
        weapon_db: Weapon database containing weapon descriptor data
    """
    for descr_namespace, weapon_descr_data in weapon_db.items():
        for location_data in weapon_descr_data["weapon_locations"].items():
            if location_data[0] in ammo_db["salvo_weapons"]:
                new_name = ammo_db["salvo_weapons"][location_data[0]]
                turret_index = location_data["turret_index"]
        
                weapon_descr = source.by_namespace(descr_namespace)
                if weapon_descr:
                    turret = weapon_descr.v.by_m("TurretDescriptorList").v[turret_index]
                    weapon = turret.v.by_m("MountedWeaponDescriptorList").v[location_data["mounted_index"]]
                    weapon.v.by_m("Ammunition").v = f"$/GFX/Weapon/Ammo_{new_name}"
                    logger.info(f"Renaming salvo weapon {location_data[0]} to {new_name}")
            
            if location_data[0] in renames:
                new_name = renames[location_data[0]]
                weapon_descr = source.by_namespace(descr_namespace)
                if weapon_descr:
                    turret = weapon_descr.v.by_m("TurretDescriptorList").v[turret_index]
                    weapon = turret.v.by_m("MountedWeaponDescriptorList").v[location_data["mounted_index"]]
                    weapon.v.by_m("Ammunition").v = f"$/GFX/Weapon/Ammo_{new_name}"
                    logger.info(f"Renaming weapon {location_data[0]} to {new_name}")
        
                
def remove_vanilla_instances(source, removals: List[str]) -> None:
    """Remove specified vanilla weapon instances.
    
    Args:
        source: NDF file containing weapon descriptors
        removals: List of instance names to remove
    """
    for ammo_descr in source:
        name = ammo_descr.namespace.split("Ammo_")[1]
        if name in removals:
            logger.info(f"Removing vanilla instance: {name}")
            source.remove(ammo_descr) 