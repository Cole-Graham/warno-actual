from typing import Any, Dict, List, Tuple

from src.constants.weapons import AMMUNITION_MISSILES_RENAMES, AMMUNITION_RENAMES

from .vanilla_modifications import vanilla_renames_weapondescriptor

# Combine the lists and remove duplicates
merged_renames = list(set(AMMUNITION_RENAMES) | set(AMMUNITION_MISSILES_RENAMES))

def edit_weapon_descriptor(source_path, game_db: Dict[str, Any]) -> None:
    """Edit WeaponDescriptor.ndf file.
    
    Args:
        source_path: The NDF file being edited
        game_db: Game database containing ammunition and weapon data
    """
    renames = merged_renames
    ammo_db = game_db["ammunition"]
    weapon_db = game_db["weapons"]
    
    vanilla_renames_weapondescriptor(source_path, renames, ammo_db, weapon_db)
