from .default_salves import apply_default_salves
from .air_rocket_platform import apply_air_rocket_platform_standard
from .he_dca_air_mounts import apply_he_dca_air_mounts
from .helo_aa_turret_angles import apply_helo_aa_turret_angles_pattern_standard
from .satchel_at_companion_mounts import apply_satchel_at_companion_mounts
from .hobs_no_hmd import (
    apply_hobs_no_hmd_pattern_for_weapon_descr,
    apply_hobs_no_hmd_pattern_standard,
)
from .infantry_magazine_salvo_remounts import apply_infantry_magazine_salvo_remounts
from .namespace_ammo_quantity import update_weapondescr_ammoname_quantity
from .new_units import new_units_weapondescriptor
from .unit_edits import unit_edits_weapondescriptor
from .vanilla_renames import vanilla_renames_weapondescriptor

__all__ = [
    "apply_default_salves",
    "apply_air_rocket_platform_standard",
    "apply_he_dca_air_mounts",
    "apply_helo_aa_turret_angles_pattern_standard",
    "apply_satchel_at_companion_mounts",
    "apply_hobs_no_hmd_pattern_for_weapon_descr",
    "apply_hobs_no_hmd_pattern_standard",
    "apply_infantry_magazine_salvo_remounts",
    "update_weapondescr_ammoname_quantity",
    "new_units_weapondescriptor",
    "unit_edits_weapondescriptor",
    "vanilla_renames_weapondescriptor",
]