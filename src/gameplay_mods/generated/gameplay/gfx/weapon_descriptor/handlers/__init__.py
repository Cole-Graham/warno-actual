from .default_salves import apply_default_salves
from .he_dca_air_mounts import apply_he_dca_air_mounts
from .hobs_no_hmd import (
    apply_hobs_no_hmd_pattern_for_weapon_descr,
    apply_hobs_no_hmd_pattern_standard,
)
from .namespace_ammo_quantity import update_weapondescr_ammoname_quantity
from .new_units import new_units_weapondescriptor
from .unit_edits import unit_edits_weapondescriptor
from .vanilla_renames import vanilla_renames_weapondescriptor

__all__ = [
    "apply_default_salves",
    "apply_he_dca_air_mounts",
    "apply_hobs_no_hmd_pattern_for_weapon_descr",
    "apply_hobs_no_hmd_pattern_standard",
    "update_weapondescr_ammoname_quantity",
    "new_units_weapondescriptor",
    "unit_edits_weapondescriptor",
    "vanilla_renames_weapondescriptor",
]