"""Standards applied by scanning Ammunition.ndf for traits, names, calibers, ranges, etc."""

from .aim_time import AIM_TIME_STANDARDS, AimTimeRule
from .canon_he_damage import CANON_HE_DAMAGE_BY_CALIBER
from .he_bomb_damage import (
    HE_BOMB_DAMAGE_BY_WEIGHT,
    HE_BOMB_NAME_MATCH,
    HE_BOMB_TRAIT_TOKENS,
)
from .clu_sol_traits import (
    CLU_SOL_DAMAGE_FAMILY_TO_TRAIT,
    CLU_SOL_TRAIT_TOKEN_CLUSTER,
    CLU_SOL_TRAIT_TOKEN_HEAT,
)
from .weapon_range import WEAPON_RANGE_MEMBERS_TO_CHECK

__all__ = [
    "AIM_TIME_STANDARDS",
    "AimTimeRule",
    "CANON_HE_DAMAGE_BY_CALIBER",
    "HE_BOMB_DAMAGE_BY_WEIGHT",
    "HE_BOMB_NAME_MATCH",
    "HE_BOMB_TRAIT_TOKENS",
    "CLU_SOL_DAMAGE_FAMILY_TO_TRAIT",
    "CLU_SOL_TRAIT_TOKEN_CLUSTER",
    "CLU_SOL_TRAIT_TOKEN_HEAT",
    "WEAPON_RANGE_MEMBERS_TO_CHECK",
]
