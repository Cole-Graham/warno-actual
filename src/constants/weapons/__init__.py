"""Weapon edit definitions."""

from .ammunition import weapons
from .damage_values import (
    DAMAGE_EDITS,
    DPICM_DAMAGES,
    FMBALLE_INFANTRY_EDITS,
    FMBALLE_ROWS,
    FULL_BALL_DAMAGE,
    INFANTRY_ARMOR_EDITS,
    SNIPER_DAMAGE,
)
from .missiles import missiles
from .squad_at_ammo import SQUAD_AT_AMMO
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
    'missiles',
    'SNIPER_DAMAGE',
    'SQUAD_AT_AMMO',
    'WEAPON_DESCRIPTIONS',
    'weapons'
] 
