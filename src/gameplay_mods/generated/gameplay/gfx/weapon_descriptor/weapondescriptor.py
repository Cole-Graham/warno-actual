from typing import Any, Dict
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

from .handlers import (
    apply_default_salves,
    apply_he_dca_air_mounts,
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
    # Auto-wire SPAAG air mounts on every turret carrying a DamageFamily_he_dca
    # ammo (must run last so vanilla, new, and edited units are all in place).
    apply_he_dca_air_mounts(source_path, logger, game_db)
