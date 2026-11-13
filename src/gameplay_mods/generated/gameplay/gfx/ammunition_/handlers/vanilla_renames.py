
from typing import Any, Dict, List, Tuple  # noqa

import logging

from src.data.mounted_weapon_identity import rekey_identity


def vanilla_renames_ammunition(source_path: Any, logger: logging.Logger, ammo_db: Dict[str, Any]) -> None:
    """Apply vanilla renames to Ammunition.ndf and AmmunitionMissiles.ndf"""
    # source: NDF file containing weapon descriptors
    # renames: List of (old_name, new_name) tuples
    # ammo_db: Ammunition database containing salvo weapon mappings
    for ammo_descr in source_path:
        if not hasattr(ammo_descr, 'namespace') or 'Ammo_' not in ammo_descr.namespace:
            continue
            
        old_namespace = ammo_descr.namespace
        old_name = old_namespace.split("Ammo_", 1)[1]
        # Check if this is a salvo weapon that needs renaming
        if old_name in ammo_db["renames_old_new"]:
            new_name = ammo_db["renames_old_new"][old_name]
            logger.info(f"Renaming salvo weapon {old_name} to {new_name}")
            ammo_descr.namespace = f"Ammo_{new_name}"
            rekey_identity(ammo_db, old_namespace, ammo_descr.namespace)
            continue


def remove_vanilla_instances(source_path: Any, logger: logging.Logger, removals: List[str]) -> None:
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