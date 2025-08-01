"""Gameplay modification modules.

Module Structure:
    depictions/     - Editors for unit depictions and showroom
    division_rules/ - Editors for division rules
    divisions/      - Editors for divisions
    effects/        - Editors for unit effects and capacities
    terrains/       - Editors for terrain properties
    ui/            - Editors for UI elements
    unit_descriptor/ - Editors for unit descriptors
    veterancy/      - Editors for veterancy and experience
    weapons/        - Editors for weapons and ammunition
"""

from typing import Any, Callable, Dict, List

from src.shared import get_shared_editors
from src.utils.logging_utils import setup_logger

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
from .divisions import (
    add_division_rules,
    deck_ap_points,
    add_to_divisions,
    create_deck_pack_descriptors,
    create_division_packs,
    edit_division_matrices,
    edit_division_units,
    update_deck_serializer,
    supply_divisions,
)
from .division_rules import (
    modify_deck_packs,
    update_deck_pack_references,
    mg_team_division_rules,
    unit_edits_divisionrules,
    supply_divisionrules,
    modify_decks,
    new_deck_packs,
)

from .effects import (
    edit_capacite_list,
    edit_critical_effects,
    edit_shock_effects,
    edit_shock_units,
    add_swift_capacity,
    edit_conditions,
    edit_damage_levels,
    edit_capacities,
)
from .game_constants import edit_gd_constants, edit_orders, edit_ravitaillement
from .terrains import edit_terrains
from .ui import (
    edit_division_emblems,
    edit_ingame_icons,
    edit_specialties,
    edit_specialty_icons,
    edit_unit_info_panel,
    ui_gameplay_textscripts,
    hide_divisions_divisions_ndf,
    hide_divisions_decks_ndf,
    hide_divisions_deckserializer_ndf,
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

logger = setup_logger(__name__)


def get_editors(game_db: Dict[str, Any]) -> Dict[str, List[Callable]]:
    # defunct (for now? I had to simplify config/build pipelines to get the patcher working)
    """Get all game file editors."""
    # Get base gameplay editors
    editors = {
        # Core gameplay mechanics
        "GameData/Gameplay/Constantes/GDConstants.ndf": [
            lambda source_path: edit_gd_constants(source_path),
        ],
        "GameData/Gameplay/Constantes/Ravitaillement.ndf": [
            lambda source_path: edit_ravitaillement(source_path),
        ],
        "GameData/Gameplay/Constantes/WeaponConstantes.ndf": [
            lambda source_path: edit_weapon_constantes(source_path),
        ],
        "GameData/Gameplay/Terrains/Terrains.ndf": [
            lambda source_path: edit_terrains(source_path),
        ],
        "GameData/Gameplay/Unit/Tactic/Team.ndf": [
            lambda source_path: edit_team_supply(source_path),
        ],
        # Division and deck files
        # "GameData/Generated/Gameplay/Decks/DeckPacks.ndf": [
        #     lambda source_path: create_deck_pack_descriptors(source_path)
        # ],
        "GameData/Generated/Gameplay/Decks/DeckSerializer.ndf": [
            lambda source_path: update_deck_serializer(source_path)
        ],
        "GameData/Generated/Gameplay/Decks/Divisions.ndf": [
            lambda source_path: add_to_divisions(source_path),
            lambda source_path: edit_division_units(source_path),
        ],
        "GameData/Generated/Gameplay/Decks/DivisionRules.ndf": [lambda source_path: add_division_rules(source_path)],
        "GameData/Generated/Gameplay/Decks/DivisionPacks.ndf": [lambda source_path: create_division_packs(source_path)],
        "GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf": [
            lambda source_path: edit_division_matrices(source_path)
        ],
        # Game constants
        # "GameData/Gameplay/Constantes/GDConstantes.ndf": [
        #     lambda source_path: edit_gd_constantes(source_path),
        # ],
        # "GameData/Gameplay/Constantes/Ravitaillement.ndf": [
        #     lambda source_path: edit_ravitaillement(source_path),
        # ],
        # Unit and weapon mechanics
        "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf": [
            lambda source_path: edit_units(source_path, game_db),
            lambda source_path: edit_antirad_optics(source_path),
            lambda source_path: edit_forward_deploy(source_path),
            lambda source_path: edit_infantry_armor_wa(source_path),
            lambda source_path: edit_auto_cover(source_path, game_db),
            lambda source_path: edit_shock_units(source_path, game_db),
            lambda source_path: create_new_units(source_path, game_db),
        ],
        "GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf": [
            lambda source_path: edit_fob_attributes(source_path),
        ],
        "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf": [
            lambda source_path: unit_edits_weapondescriptor(source_path, game_db),
            lambda source_path: add_radio_tag_to_mortars(source_path, game_db),
            lambda source_path: create_new_weapons(source_path, game_db),
        ],
        "GameData/Generated/Gameplay/Gfx/Ammunition.ndf": [
            lambda source_path: edit_ammunition(source_path, game_db),
            lambda source_path: apply_damage_families(source_path, game_db),
        ],
        "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf": [
            lambda source_path: edit_missiles(source_path, game_db),
        ],
        "GameData/Generated/Gameplay/Gfx/MissileDescriptors.ndf": [],
        "GameData/Generated/Gameplay/Gfx/OrderAvailability_Tactic.ndf": [
            lambda source_path: edit_orders(source_path, game_db),
        ],
        "GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf": [
            lambda source_path: edit_smoke_duration(source_path),
        ],
        "GameData/Generated/Gameplay/Gfx/DamageResistance.ndf": [
            lambda source_path: add_damage_resistance_values(source_path),
            lambda source_path: apply_damage_family_edits(source_path),
            lambda source_path: edit_infantry_armor(source_path),
        ],
        "GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyList.ndf": [
            lambda source_path: add_damage_families_to_list(source_path),
        ],
        "GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyListImpl.ndf": [
            lambda source_path: add_damage_families_to_impl(source_path),
        ],
        # Effects and veterancy files
        "GameData/Generated/Gameplay/Gfx/CapaciteList.ndf": [
            lambda source_path: edit_capacite_list(source_path),
        ],
        "GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf": [
            lambda source_path: edit_shock_effects(source_path),
            lambda source_path: edit_veterancy_effects(source_path),
        ],
        "GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf": [
            lambda source_path: edit_veterancy_hints(source_path),
        ],
        "GameData/Gameplay/Unit/CriticalModules/TemplateCriticalEffectModules.ndf": [
            lambda source_path: edit_critical_effects(source_path),
        ],
        # Depiction files
        # /Gfx
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialUnits.ndf": [
            lambda source_path: unit_edits_depictionaerial(source_path),
        ],
        "GameData/Generated/Gameplay/Gfx/MissileCarriage.ndf": [
            lambda source_path: unit_edits_missilecarriage(source_path),
        ],
        "GameData/Generated/Gameplay/Gfx/MissileCarriageDepiction.ndf": [
            lambda source_path: unit_edits_missilecarriagedepiction(source_path),
        ],
        "GameData/Generated/Gameplay/Gfx/ShowRoomUnits.ndf": [
            lambda source_path: edit_showroom_units(source_path),
            lambda source_path: create_showroom_depictions(source_path),
        ],
        # "GameData/Generated/Gameplay/Gfx/UniteCadavreDescriptor.ndf": [
        #     lambda source_path: create_cadavre_depictions(source_path)
        # ],
        # /Depictions
        "GameData/Generated/Gameplay/GFX/Depictions/DepictionAlternatives.ndf": [
            lambda source_path: create_alternatives_depictions(source_path)
        ],
        "GameData/Generated/Gameplay/GFX/Depictions/DepictionGhosts.ndf": [
            lambda source_path: create_ghost_depictions(source_path)
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialGhosts.ndf": [
            lambda source_path: create_aerial_ghost_depictions(source_path)
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionHumans.ndf": [
            lambda source_path: create_veh_human_depictions(source_path)
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionVehicles.ndf": [
            lambda source_path: create_veh_depictions(source_path),
            lambda source_path: unit_edits_depictionvehicles(source_path),
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionVehiclesShowRoom.ndf": [
            # lambda source_path: create_veh_showroom_depictions(source_path) # Maybe unnecessary
        ],
        # /Infanterie
        "GameData/Generated/Gameplay/Gfx/Infanterie/DepictionInfantry.ndf": [
            lambda source_path: edit_infantry_depictions(source_path, game_db["ammunition"], game_db["depiction_data"]),
            lambda source_path: create_infantry_depictions(source_path),
        ],
        # UI
        "GameData/Generated/UserInterface/Textures/ButtonTexturesUnites.ndf": [
            lambda source_path: create_button_textures(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitInfoPanelView.ndf": [
            lambda source_path: edit_unit_info_panel(source_path),
        ],
        "GameData/UserInterface/Use/InGame/UseInGameTextures.ndf": [
            lambda source_path: edit_ingame_icons(source_path),
        ],
        "GameData/Generated/UserInterface/Textures/DivisionTextures.ndf": [
            lambda source_path: edit_division_emblems(source_path),
        ],
        "GameData/Generated/UserInterface/Textures/SpecialityIconTextures.ndf": [
            lambda source_path: edit_specialty_icons(source_path),
        ],
        "GameData/Generated/UserInterface/UnitSpecialties.ndf": [
            lambda source_path: edit_specialties(source_path),
        ],
    }

    # Add shared editors
    shared_editors = get_shared_editors()
    for path, editor_list in shared_editors.items():
        if path in editors:
            editors[path].extend(editor_list)
        else:
            editors[path] = editor_list

    return editors
