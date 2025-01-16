from typing import Any, Dict, List, Tuple

from src.constants.weapons import AMMUNITION_MISSILES_RENAMES, AMMUNITION_RENAMES

from .vanilla_modifications import vanilla_renames_weapondescriptor

# Combine the lists and remove duplicates
merged_renames = list(set(AMMUNITION_RENAMES) | set(AMMUNITION_MISSILES_RENAMES))

def edit_weapon_descriptor(source, game_db: Dict[str, Any]) -> None:
    """Edit WeaponDescriptor.ndf file."""
    renames = merged_renames
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]
    
    vanilla_renames_weapondescriptor(source, renames, ammo_db, weapon_db)
