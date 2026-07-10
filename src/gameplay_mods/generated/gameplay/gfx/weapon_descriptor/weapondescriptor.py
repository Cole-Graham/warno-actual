from typing import Any, Dict
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

from .handlers import (
    apply_default_salves,
    apply_he_dca_air_mounts,
    apply_satchel_at_companion_mounts,
    apply_hobs_no_hmd_pattern_standard,
    apply_infantry_magazine_salvo_remounts,
    new_units_weapondescriptor,
    unit_edits_weapondescriptor,
    vanilla_renames_weapondescriptor,
    update_weapondescr_ammoname_quantity,
)

def edit_gen_gp_gfx_weapondescriptor(source_path: Any, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf"""
    
    unit_edits = load_unit_edits()
    
    vanilla_renames_weapondescriptor(source_path, logger, game_db)
    apply_hobs_no_hmd_pattern_standard(logger, source_path, game_db)
    new_units_weapondescriptor(source_path, game_db)
    unit_edits_weapondescriptor(source_path, game_db)
    # Salves after unit edits to ensure we're working from the correct ammo names
    apply_default_salves(source_path, logger, game_db, unit_edits)
    # Magazine remount after salves/HAGRU so N is final; sets Salves to 1
    apply_infantry_magazine_salvo_remounts(source_path, logger, game_db)
    update_weapondescr_ammoname_quantity(source_path, logger, game_db)
    # Auto-wire SPAAG air mounts on every turret carrying a DamageFamily_he_dca
    # ammo (must run last so vanilla, new, and edited units are all in place).
    apply_he_dca_air_mounts(source_path, logger, game_db)
    apply_satchel_at_companion_mounts(source_path, logger, game_db)
