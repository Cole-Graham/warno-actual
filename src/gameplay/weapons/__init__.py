"""Weapon modification modules."""

from .ammunition import edit_ammunition
from .damage_families import (
    add_damage_families_to_impl,
    add_damage_families_to_list,
    add_damage_resistance_values,
    apply_damage_families,
    apply_damage_family_edits,
    edit_infantry_armor,
    edit_weapon_constants,
)
from .mg_teams import edit_mg_team_weapons
from .missiles import edit_missiles
from .mortar_mods import (
    add_corrected_shot_dispersion,
    add_radio_tag_to_mortars,
    edit_smoke_duration,
)
from .unit_edits import edit_units
from .vanilla_modifications import apply_vanilla_renames, remove_vanilla_instances

__all__ = [
    'edit_ammunition',
    'add_damage_families_to_impl',
    'add_damage_families_to_list',
    'add_damage_resistance_values',
    'apply_damage_families',
    'apply_damage_family_edits',
    'edit_infantry_armor',
    'edit_mg_team_weapons',
    'edit_missiles',
    'edit_smoke_duration',
    'add_corrected_shot_dispersion',
    'add_radio_tag_to_mortars',
    'edit_units',
    'apply_vanilla_renames',
    'remove_vanilla_instances',
    'edit_weapon_constants',
] 