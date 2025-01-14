"""Editor for Ammunition.ndf."""

from typing import Any, Dict

from src.constants.weapons.ammunition import weapons
from src.constants.weapons.vanilla_inst_modifications import (
    ammunition_removals,
    ammunition_renames,
)
from src.utils.logging_utils import setup_logger

from .damage_families import apply_damage_families
from .mg_teams import edit_mg_team_weapons
from .mortar_mods import add_corrected_shot_dispersion
from .vanilla_modifications import apply_vanilla_renames, remove_vanilla_instances

logger = setup_logger(__name__)

def edit_ammunition(source, game_db: Dict[str, Any]) -> None:
    """Edit Ammunition.ndf file."""
    ammo_db = game_db["ammunition"]
    
    # First handle vanilla modifications
    apply_vanilla_renames(source, ammunition_renames)
    remove_vanilla_instances(source, ammunition_removals)
    
    # Add mortar corrected shot
    add_corrected_shot_dispersion(source, ammo_db)
    
    # Modify MG team weapons
    edit_mg_team_weapons(source, ammo_db)
    
    # Apply damage family modifications
    apply_damage_families(source, ammo_db)
    
    # Then apply weapon edits...
    
    for (weapon_name, category, donor, is_new), data in weapons.items():
        if "Ammunition" not in data:
            continue
        
        try:
            descriptor = source.by_n(weapon_name)
            if not descriptor:
                logger.warning(f"Could not find weapon {weapon_name}")
                continue
                
            logger.info(f"Applying edits to {weapon_name}")
            # Apply edits will be implemented next...
            
        except Exception as e:
            logger.error(f"Failed to edit {weapon_name}: {str(e)}") 