"""UI modification modules."""

from .divisions import edit_division_emblems
from .ingame_icons import edit_ingame_icons
from .traits import edit_specialties, edit_specialty_icons, write_trait_texts
from .unit_info_panel import edit_unit_info_panel, write_info_panel_hints
from .weapon_textures import edit_weapontextures
from .weapons_minmax import edit_weaponsminmax

__all__ = [
    'edit_division_emblems',
    'edit_ingame_icons',
    'edit_specialties',
    'edit_specialty_icons',
    'edit_unit_info_panel',
    'write_info_panel_hints',
    'write_trait_texts',
    'edit_weapontextures',
    'edit_weaponsminmax',
]
