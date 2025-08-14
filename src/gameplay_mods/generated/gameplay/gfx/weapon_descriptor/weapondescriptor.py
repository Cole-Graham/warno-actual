from typing import Any, Dict
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

from .handlers import (
    apply_default_salves,
    new_units_weapondescriptor,
    unit_edits_weapondescriptor,
    vanilla_renames_weapondescriptor,
    update_weapondescr_ammoname_quantity,
)

def edit_gen_gp_gfx_weapondescriptor(source_path: Any, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf"""
    
    unit_edits = load_unit_edits()
    
    vanilla_renames_weapondescriptor(source_path, logger, game_db)
    new_units_weapondescriptor(source_path, game_db)
    unit_edits_weapondescriptor(source_path, game_db)
    # Salves after unit edits to ensure we're working from the correct ammo names
    apply_default_salves(source_path, logger, game_db, unit_edits)
    update_weapondescr_ammoname_quantity(source_path, logger, game_db)
