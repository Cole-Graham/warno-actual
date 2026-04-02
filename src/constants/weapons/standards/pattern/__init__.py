"""Standards applied by scanning Ammunition.ndf for traits, names, calibers, ranges, etc."""

from .aim_time import AIM_TIME_STANDARDS, AimTimeRule
from .canon_he_damage import CANON_HE_DAMAGE_BY_CALIBER, CANON_HE_DAMAGE_EXCEPTIONS
from .he_bomb_damage import (
    HE_BOMB_DAMAGE_BY_WEIGHT,
    HE_BOMB_NAME_MATCH,
    HE_BOMB_TRAIT_TOKENS,
)
from .weapon_range import WEAPON_RANGE_MEMBERS_TO_CHECK

__all__ = [
    "AIM_TIME_STANDARDS",
    "AimTimeRule",
    "CANON_HE_DAMAGE_BY_CALIBER",
    "CANON_HE_DAMAGE_EXCEPTIONS",
    "HE_BOMB_DAMAGE_BY_WEIGHT",
    "HE_BOMB_NAME_MATCH",
    "HE_BOMB_TRAIT_TOKENS",
    "WEAPON_RANGE_MEMBERS_TO_CHECK",
]
