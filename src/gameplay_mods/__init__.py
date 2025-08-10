"""Gameplay modification modules."""


from typing import Any, Callable, Dict, List

# New import structure
from .gameplay import (
    # .constantes
    edit_gdconstants,
    edit_ravitaillement,
    # .unit
    edit_airplane_critical,
    edit_groundunit_critical,
    edit_helico_critical,
    edit_infanterie_critical,
    edit_template_critical,
    edit_testunits_critical,
)
from .generated import (
    # .gameplay.decks
    hide_divisions_deckserializer_ndf,
    update_deck_serializer,
    edit_deck_packs,
    edit_deck_pack_lists,
    hide_divisions_decks_ndf,
    update_deck_pack_references,
    new_deck_packs,
    new_unit_division_rules,
    supply_divisionrules,
    unit_edits_divisionrules,
    edit_divisioncostmatrix,
    edit_divisions,
    mg_team_division_rules,
    # .gameplay.gfx
    edit_orders,
    # .userinterface.textures
    edit_division_emblems,
)

__all__ = [
    # .gameplay.constantes
    'edit_gdconstants',
    'edit_ravitaillement',
    # .gameplay.unit
    'edit_airplane_critical',
    'edit_groundunit_critical',
    'edit_helico_critical',
    'edit_infanterie_critical',
    'edit_template_critical',
    'edit_testunits_critical',
    # .generated.gameplay.decks
    'hide_divisions_deckserializer_ndf',
    'update_deck_serializer',
    'edit_deck_packs',
    'edit_deck_pack_lists',
    'hide_divisions_decks_ndf',
    'update_deck_pack_references',
    'new_deck_packs',
    'new_unit_division_rules',
    'supply_divisionrules',
    'unit_edits_divisionrules',
    'edit_divisioncostmatrix',
    'edit_divisions',
    'mg_team_division_rules',
    # .generated.gameplay.gfx
    'edit_orders',
    # .generated.userinterface.textures
    'edit_division_emblems',
]

# Deprecated import structure (WIP migrating to new structure)
from .buildings import edit_fob_attributes
from .depictions import unit_edits_depictionaerial  # DepictionAerialUnits.ndf
from .depictions import unit_edits_missilecarriage  # MissileCarriage.ndf
from .depictions import (
    unit_edits_missilecarriagedepiction,  # MissileCarriageDepiction.ndf
)
from .depictions import (
    create_aerial_ghost_depictions,
    create_alternatives_depictions,
    create_button_textures,
    create_cadavre_depictions,
    create_ghost_depictions,
    create_infantry_depictions,
    create_showroom_depictions,
    create_veh_depictions,
    create_veh_human_depictions,
    create_veh_showroom_depictions,
    edit_infantry_depictions,
    edit_showroom_units,
    unit_edits_cadavre_descriptor,
    unit_edits_depictionvehicles,
    unit_edits_depictioninfantry,
)
from .terrains import edit_terrains
from .ui import (
    edit_ingame_icons,
    edit_specialties,
    edit_specialty_icons,
    edit_unit_info_panel,
    ui_gameplay_textscripts,
)
from .unit_descriptor import (
    create_new_units,
    edit_antirad_optics,
    edit_auto_cover,
    edit_forward_deploy,
    edit_infantry_armor_wa,
    edit_mg_teams,
    edit_team_supply,
    edit_units,
    global_bomber_edits,
    temp_fix_reco_radar,
    edit_identify_rules,
)
from .veterancy import edit_veterancy_effects, edit_veterancy_hints

from .weapons import (
    apply_default_salves,
    update_weapondescr_ammoname_quantity,
    edit_he_damage,
    edit_aim_times,
    edit_weapon_ranges,
    bomb_damage_standards,
    edit_fire_descriptors,
    change_fire_descriptors,
    add_corrected_shot_dispersion,
    add_radio_tag_to_mortars,
    edit_smoke_duration,
    vanilla_renames_weapondescriptor,
    edit_weapon_traits,
)
from .weapons.ammunition import edit_ammunition


from .weapons.damage_families import (
    add_damage_families_to_impl,
    add_damage_families_to_list,
    add_damage_resistance_values,
    apply_damage_families,
    apply_damage_family_edits,
    edit_infantry_armor,
    edit_weapon_constantes,
)
from .weapons.missiles import edit_missiles
from .weapons.new_weapons import create_new_weapons
from .weapons.unit_edits import unit_edits_weapondescriptor
