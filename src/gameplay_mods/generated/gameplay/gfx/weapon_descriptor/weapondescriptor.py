from typing import Any, Dict
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

from src.data.mounted_weapon_identity import (
    apply_mounted_weapon_identity,
    warn_invalid_salves,
)
from .handlers import (
    apply_default_salves,
    apply_air_rocket_platform_standard,
    apply_he_dca_air_mounts,
    apply_helo_aa_turret_angles_pattern_standard,
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
    # After replaces: correct plane/helo dumbfire rocket platform ammo
    apply_air_rocket_platform_standard(logger, source_path, game_db)
    # After replaces + HAGRU attach so helo AA mounts are final
    apply_helo_aa_turret_angles_pattern_standard(logger, source_path, game_db)
    # Salves after unit edits to ensure we're working from the correct ammo names
    apply_default_salves(source_path, logger, game_db, unit_edits)
    # Magazine remount after salves/HAGRU so N is final; sets Salves to 1
    apply_infantry_magazine_salvo_remounts(source_path, logger, game_db)
    update_weapondescr_ammoname_quantity(source_path, logger, game_db)
    # Auto-wire SPAAG air mounts on every turret carrying a DamageFamily_he_dca
    # ammo (must run last so vanilla, new, and edited units are all in place).
    apply_he_dca_air_mounts(source_path, logger, game_db)
    apply_satchel_at_companion_mounts(source_path, logger, game_db)
    # Identity fields live on each mount. Apply after every remount so the
    # final Ammunition pointer picks up that ammo's name, caliber, traits, and icon.
    apply_mounted_weapon_identity(source_path, game_db.get("ammunition") or {}, logger)
    warn_invalid_salves(source_path, logger)
