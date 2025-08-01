"""Depiction modification modules."""

from .infantry import edit_infantry_depictions
from .new_depictions import (
    create_alternatives_depictions,
    create_button_textures,
    create_cadavre_depictions,
    create_ghost_depictions,
    create_infantry_depictions,
    create_showroom_depictions,
    create_veh_human_depictions,
    create_veh_depictions,
    create_veh_showroom_depictions,
    create_aerial_ghost_depictions,
)
from .showroom import edit_showroom_units
from .unit_edits import (
    unit_edits_cadavre_descriptor,
    unit_edits_depictionaerial,
    unit_edits_missilecarriage,
    unit_edits_missilecarriagedepiction,
    unit_edits_depictionvehicles,
    unit_edits_depictioninfantry,
)

__all__ = [
    'create_alternatives_depictions',
    'create_button_textures',
    'create_cadavre_depictions',
    'create_ghost_depictions',
    'create_infantry_depictions',
    'create_showroom_depictions',
    'edit_infantry_depictions',
    'edit_showroom_units',
    'create_veh_human_depictions',
    'create_veh_depictions',
    'create_veh_showroom_depictions',
    'create_aerial_ghost_depictions',
    'unit_edits_cadavre_descriptor',
    'unit_edits_depictionaerial',
    'unit_edits_missilecarriage',
    'unit_edits_missilecarriagedepiction',
    'unit_edits_depictionvehicles',
    'unit_edits_depictioninfantry',
]
