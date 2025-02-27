"""Weapon edit definitions."""

from .ammunition import ammunitions
from .damage_values import (
    VANILLA_LAST_ROW,
    VANILLA_LAST_COLUMN,
    DAMAGE_EDITS,
    DPICM_DAMAGES,
    FMBALLE_INFANTRY_EDITS,
    FMBALLE_ROWS,
    SA_FULL_DAMAGE_RATIOS,
    SA_INTERMEDIATE_DAMAGE_RATIOS,
    SA_INF_ARMOR_DAMAGE_RATIOS,
    INFANTRY_ARMOR_EDITS,
    SNIPER_DAMAGE,
    KPVT_DAMAGE,
    NPLM_BOMB_DAMAGE,
    PGB_BOMB_DAMAGE,
    MANPAD_HAGRU_DAMAGE,
    MANPAD_TBAGRU_DAMAGE,
)
from .missiles import missiles
from .mounted_weapons import mounted_weapons
from .salvo_standards import LIGHT_AT_AMMO
from .weapon_descriptions import WEAPON_DESCRIPTIONS, WEAPON_TRAITS
from .vanilla_inst_modifications import (
    AMMUNITION_MISSILES_REMOVALS,
    AMMUNITION_MISSILES_RENAMES,
    AMMUNITION_REMOVALS,
    AMMUNITION_RENAMES
)

__all__ = [
    'VANILLA_LAST_ROW',
    'VANILLA_LAST_COLUMN',
    'AMMUNITION_MISSILES_REMOVALS',
    'AMMUNITION_MISSILES_RENAMES', 
    'AMMUNITION_REMOVALS',
    'AMMUNITION_RENAMES',
    'DAMAGE_EDITS',
    'DPICM_DAMAGES',
    'FMBALLE_INFANTRY_EDITS',
    'FMBALLE_ROWS',
    'SA_FULL_DAMAGE_RATIOS',
    'SA_INTERMEDIATE_DAMAGE_RATIOS',
    'SA_INF_ARMOR_DAMAGE_RATIOS',
    'INFANTRY_ARMOR_EDITS',
    'KPVT_DAMAGE',
    'NPLM_BOMB_DAMAGE',
    'missiles',
    'mounted_weapons',
    'SNIPER_DAMAGE',
    'LIGHT_AT_AMMO',
    'WEAPON_DESCRIPTIONS',
    'WEAPON_TRAITS',
    'ammunitions',
    'PGB_BOMB_DAMAGE',
    'MANPAD_HAGRU_DAMAGE',
    'MANPAD_TBAGRU_DAMAGE',
] 
