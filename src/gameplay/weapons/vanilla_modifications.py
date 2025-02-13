"""Functions for modifying vanilla ammunition instances."""
# import traceback
from typing import Any, Dict, List, Tuple  # noqa

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def vanilla_renames_ammunition(source_path: Any, ammo_db: Dict[str, Any]) -> None:
    """Apply vanilla renames to Ammunition.ndf and AmmunitionMissiles.ndf"""
    # source: NDF file containing weapon descriptors
    # renames: List of (old_name, new_name) tuples
    # ammo_db: Ammunition database containing salvo weapon mappings
    for ammo_descr in source_path:
        if not hasattr(ammo_descr, 'namespace') or 'Ammo_' not in ammo_descr.namespace:
            continue
            
        old_name = ammo_descr.namespace.split("Ammo_", 1)[1]
        # Check if this is a salvo weapon that needs renaming
        if old_name in ammo_db["renames_old_new"]:
            new_name = ammo_db["renames_old_new"][old_name]
            logger.info(f"Renaming salvo weapon {old_name} to {new_name}")
            ammo_descr.namespace = f"Ammo_{new_name}"
            continue


def vanilla_renames_weapondescriptor(source_path: Any, ammo_db: Dict[str, Any], weapon_db: Dict[str, Any]) -> None:
    """Apply vanilla renames to WeaponDescriptor.ndf
    
    Args:
        source_path: NDF file containing weapon descriptors
        ammo_db: Ammunition database containing salvo weapon mappings
        weapon_db: Weapon database containing weapon descriptor data
    """
    # renames: List of (old_name, new_name) tuples
    try:
        for descr_namespace, weapon_descr_data in weapon_db.items():
            for weapon_name, entries in weapon_descr_data["weapon_locations"].items():
                # try:
                for entry in entries:
                    if weapon_name in ammo_db["renames_old_new"]:
                        new_name = ammo_db["renames_old_new"][weapon_name]
                        turret_index = entry["turret_index"]
                
                        weapon_descr = source_path.by_namespace(descr_namespace)
                        if weapon_descr:
                            turret = weapon_descr.v.by_m("TurretDescriptorList").v[turret_index]
                            weapon = turret.v.by_m("MountedWeaponDescriptorList").v[entry["mounted_index"]]
                            weapon.v.by_m("Ammunition").v = f"$/GFX/Weapon/Ammo_{new_name}"
                            logger.info(f"Renaming salvo weapon {weapon_name} to {new_name} on turret {turret_index}")
                    else:
                        logger.debug(f"No renaming needed for {weapon_name}")
                # except Exception as e:
                #     logger.error(f"Error renaming weapon {weapon_name}: {e}")
                #     logger.error(traceback.format_exc())
    except Exception as e:
        logger.error(f"Error applying vanilla renames: {e}")
        raise


def remove_vanilla_instances(source_path: Any, removals: List[str]) -> None:
    """Remove specified vanilla ammunition instances.
    
    Args:
        source_path: NDF file containing weapon descriptors
        removals: List of instance names to remove
    """
    for ammo_descr in source_path:
        name = ammo_descr.namespace.split("Ammo_")[1]
        if name in removals:
            logger.info(f"Removing vanilla instance: {name}")
            source_path.remove(ammo_descr)
