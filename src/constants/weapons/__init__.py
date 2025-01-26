"""Weapon edit definitions."""

from .ammunition import ammunitions
from .damage_values import (
    DAMAGE_EDITS,
    DPICM_DAMAGES,
    FMBALLE_INFANTRY_EDITS,
    FMBALLE_ROWS,
    FULL_BALL_DAMAGE,
    INFANTRY_ARMOR_EDITS,
    SNIPER_DAMAGE,
    KPVT_DAMAGE,
)
from .missiles import missiles
from .salvo_standards import LIGHT_AT_AMMO
from .weapon_descriptions import WEAPON_DESCRIPTIONS
from .vanilla_inst_modifications import (
    AMMUNITION_MISSILES_REMOVALS,
    AMMUNITION_MISSILES_RENAMES,
    AMMUNITION_REMOVALS,
    AMMUNITION_RENAMES
)

__all__ = [
    'AMMUNITION_MISSILES_REMOVALS',
    'AMMUNITION_MISSILES_RENAMES', 
    'AMMUNITION_REMOVALS',
    'AMMUNITION_RENAMES',
    'DAMAGE_EDITS',
    'DPICM_DAMAGES',
    'FMBALLE_INFANTRY_EDITS',
    'FMBALLE_ROWS',
    'FULL_BALL_DAMAGE',
    'INFANTRY_ARMOR_EDITS',
    'KPVT_DAMAGE',
    'missiles',
    'SNIPER_DAMAGE',
    'LIGHT_AT_AMMO',
    'WEAPON_DESCRIPTIONS',
    'ammunitions'
] 
