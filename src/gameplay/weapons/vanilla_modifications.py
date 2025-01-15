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