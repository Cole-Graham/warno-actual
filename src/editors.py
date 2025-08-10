"""Central registry of all file editors."""

from typing import Callable, Dict, List

# New import structure
from .gameplay_mods import (
    # .gameplay.constantes
    edit_gdconstants,
    edit_ravitaillement,
    # .gameplay.unit
    edit_airplane_critical,
    edit_groundunit_critical,
    edit_helico_critical,
    edit_infanterie_critical,
    edit_template_critical,
    edit_testunits_critical,
    # .generated.gameplay
    hide_divisions_deckserializer_ndf,
    update_deck_serializer,
    edit_deck_packs,
    edit_deck_pack_lists, # Possibly deprecated
    hide_divisions_decks_ndf,
    update_deck_pack_references,
    new_deck_packs,
    new_unit_division_rules,
    supply_divisionrules,
    unit_edits_divisionrules,
    edit_divisioncostmatrix,
    edit_divisions,
    mg_team_division_rules,
    edit_capacitelist,
    edit_conditionsdescriptor,
    edit_damagelevels,
    edit_effetssurunite,
    edit_orderavailabilitytactic,
    edit_unitedescriptor,
    # .generated.userinterface
    edit_division_emblems,
)

__all__ = [
    # .gameplay_mods.gameplay.constantes
    'edit_gdconstants',
    'edit_ravitaillement',
    # .gameplay_mods.gameplay.unit
    'edit_airplane_critical',
    'edit_groundunit_critical',
    'edit_helico_critical',
    'edit_infanterie_critical',
    'edit_template_critical',
    'edit_testunits_critical',
    # .gameplay_mods.generated.gameplay
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
    'edit_unitedescriptor',
    'edit_orderavailabilitytactic',
    'edit_conditionsdescriptor',
    'edit_damagelevels',
    'edit_effetssurunite',
    'edit_capacitelist',
    # .gameplay_mods.generated.userinterface
    'edit_division_emblems',
]

# Deprecated import structure (WIP migrating to new structure)
from src.gameplay_mods import (
    add_radio_tag_to_mortars,
    add_swift_capacity,
    apply_default_salves,
    bomb_damage_standards,
    change_fire_descriptors,
    create_veh_showroom_depictions,
    edit_aim_times,
    edit_capacities,
    edit_conditions,
    edit_damage_levels,
    edit_fire_descriptors,
    edit_he_damage,
    edit_identify_rules,
    edit_mg_teams,
    edit_smoke_duration,
    edit_weapon_ranges,
    edit_weapon_traits,
    global_bomber_edits,
    modify_decks,
    temp_fix_reco_radar,
    ui_gameplay_textscripts,
    unit_edits_cadavre_descriptor,
    update_weapondescr_ammoname_quantity,
    vanilla_renames_weapondescriptor,
)
from src.gameplay_mods.buildings import edit_fob_attributes
from src.gameplay_mods.depictions import (
    create_aerial_ghost_depictions,
    create_alternatives_depictions,
    create_button_textures,
    create_cadavre_depictions,
    create_ghost_depictions,
    create_infantry_depictions,
    create_showroom_depictions,
    create_veh_depictions,
    create_veh_human_depictions,
    edit_infantry_depictions,
    edit_showroom_units,
    unit_edits_depictionaerial,
    unit_edits_depictioninfantry,
    unit_edits_depictionvehicles,
    unit_edits_missilecarriage,
    unit_edits_missilecarriagedepiction,
)
from src.gameplay_mods.terrains import edit_terrains

# Add new import
from src.gameplay_mods.ui import (
    edit_ingame_icons,
    edit_specialties,
    edit_specialty_icons,
    edit_unit_info_panel,
    edit_weaponsminmax,
    edit_weapontextures,
)
from src.gameplay_mods.unit_descriptor import (
    create_new_units,
    edit_antirad_optics,
    edit_auto_cover,
    edit_forward_deploy,
    edit_infantry_armor_wa,
    edit_team_supply,
    edit_units,
)
from src.gameplay_mods.veterancy.vet_bonuses import (
    edit_veterancy_effects,
    edit_veterancy_hints,
    write_veterancy_tokens,
)
from src.gameplay_mods.weapons.ammunition import edit_ammunition
from src.gameplay_mods.weapons.damage_families import (
    add_damage_families_to_impl,
    add_damage_families_to_list,
    add_damage_resistance_values,
    apply_damage_families,
    apply_damage_family_edits,
    edit_infantry_armor,
    edit_weapon_constantes,
)
from src.gameplay_mods.weapons.missiles import edit_missile_speed, edit_missiles
from src.gameplay_mods.weapons.new_weapons import create_new_weapons
from src.gameplay_mods.weapons.unit_edits import unit_edits_weapondescriptor
from src.shared_mods import get_shared_editors
from src.shared_mods.buildings.fob import add_fob_minimap_module, add_fob_minimap_texture

# Import all UI editors
from src.ui_mods.style import (
    edit_buckspecificbackgrounds,
    edit_buckspecificbuttons,
    edit_buckspecifichint,
    edit_colors,
    edit_commontextures,
    edit_defaultstyleguides,
    edit_defaulttextformatscript,
    edit_orderdisplay,
    edit_textstyles,
    edit_uicommonflarelabelresources,
    edit_uiingamebuckcubeaction,
    edit_uiingamebuckengagementrules,
    edit_uiingamedefaultcontainer,
    edit_uiingamehudreplayresource,
    edit_uiingamelaunchbattlebuttonresources,
    edit_uiingameminimap,
    edit_uiingameresources,
    edit_uispecificchatview,
    edit_uispecifichudalertpanelview,
    edit_uispecifichudmultiselectionpanelview,
    edit_uispecifichudscoreview,
    edit_uispecificingamehudtimepanelview,
    edit_uispecificingameidleunitview,
    edit_uispecificingameplayermissionlabelresources,
    edit_uispecificminimapinfoview,
    edit_uispecificoffmapairplaneview,
    edit_uispecificoffmapview,
    edit_uispecificshortcutsforselectionview,
    edit_uispecificshowroomarmorycomponent,
    edit_uispecificshowroomdeckcreatorscreencomponent,
    edit_uispecificshowroomgroupsdeckcreatorscreenview,
    edit_uispecificskirmishproductionmenuview,
    edit_uispecificunitbuttonview,
    edit_uispecificunitlabelaggregationview,
    edit_uispecificunitlabelcommon,
    edit_uispecificunitlabelmultiselectionview,
    edit_uispecificunitlabelview,
    edit_uispecificunitlabelviewnameonly,
    edit_uispecificunitselectionpanelview,
    edit_uispecificunitselectionweaponpanelview,
    edit_uispecificsmartgroupselectionpanelview,
    edit_uiwarningpanel,
    edit_useoutgametextures,
    edit_uispecificloginview,
    edit_uispecificoutgamerecoverloginview,
    edit_uispecificoutgamerecoverpasswordview,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def get_all_editors(config: Dict) -> Dict[str, List[Callable]]:
    """Get all file editors."""
    game_db = config.get("game_db", {})
    build_target = config["build_config"]["target"]

    editors = {
        # Core gameplay mechanics
        "GameData/Gameplay/Constantes/GDConstants.ndf": [
            (edit_gdconstants, "gameplay"),
        ],
        "GameData/Gameplay/Constantes/Ravitaillement.ndf": [
            (edit_ravitaillement, "gameplay"),
        ],
        "GameData/Gameplay/Constantes/WeaponConstantes.ndf": [
            (edit_weapon_constantes, "gameplay"),
        ],
        "GameData/Gameplay/Terrains/Terrains.ndf": [
            (edit_terrains, "gameplay"),
        ],
        "GameData/Gameplay/Unit/Tactic/Team.ndf": [
            (edit_team_supply, "gameplay"),
        ],
        # Critical effect modules
        "GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Airplane.ndf": [
            (edit_airplane_critical, "gameplay"),
        ],
        "GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_GroundUnit.ndf": [
            (edit_groundunit_critical, "gameplay"),
        ],
        "GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Helico.ndf": [
            (edit_helico_critical, "gameplay"),
        ],
        "GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Infanterie.ndf": [
            (edit_infanterie_critical, "gameplay"),
        ],
        "GameData/Gameplay/Unit/CriticalModules/TemplateCriticalEffectModules.ndf": [
            (edit_template_critical, "gameplay"),
        ],
        "GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_TestUnits.ndf": [
            (edit_testunits_critical, "gameplay"),
        ],
        # Division and deck files
        "GameData/Generated/Gameplay/Decks/DeckSerializer.ndf": [
            (update_deck_serializer, "gameplay"),
            (hide_divisions_deckserializer_ndf, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/Divisions.ndf": [
            (edit_divisions, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/DivisionRules.ndf": [
            (new_unit_division_rules, "gameplay"),
            (unit_edits_divisionrules, "gameplay"),
            (supply_divisionrules, "gameplay"),
            (lambda source_path: mg_team_division_rules(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/DeckPacks.ndf": [
            (lambda source_path: edit_deck_packs(source_path, game_db), "gameplay"),
            (new_deck_packs, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/Decks.ndf": [
            # TODO: Confirm if this is deprecated
            # (edit_deck_pack_lists, "gameplay"),
            (lambda source_path: update_deck_pack_references(source_path, game_db), "gameplay"),
            (lambda source_path: modify_decks(source_path, game_db), "gameplay"),
            (hide_divisions_decks_ndf, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf": [
            (edit_divisioncostmatrix, "gameplay"),
        ],
        # Damage system
        "GameData/Generated/Gameplay/Gfx/DamageResistance.ndf": [
            (
                apply_damage_family_edits,
                "gameplay",
            ),  # todo: this needs to be applied first, but it should be written better not to (or at least give a warning in logs)
            (add_damage_resistance_values, "gameplay"),
            (edit_infantry_armor, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyList.ndf": [
            (add_damage_families_to_list, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyListImpl.ndf": [
            (add_damage_families_to_impl, "gameplay"),
        ],
        # Unit and weapon files
        "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf": [
            # Create new units first, before editing donors used to create them.
            # TODO: Confirm Eugen properly fixed this
            # lambda source_path: temp_fix_reco_radar(source_path, game_db),
            # TODO: Add back TypeUnitFormation to constants for new units and/or unit edits. Eugen removed it from
            # the TTypeUnitModuleDescriptor module and I thought it was just completely removed. But its now in its own
            # TFormationModuleDescriptor module, so we have to find out what the constants were that I removed.
            (lambda source_path: edit_unitedescriptor(source_path, game_db), "gameplay"),
            (lambda source_path: create_new_units(source_path, game_db), "gameplay"),
            (lambda source_path: edit_units(source_path, game_db), "gameplay"),
            (lambda source_path: edit_auto_cover(source_path, game_db), "gameplay"),
            (edit_antirad_optics, "gameplay"),
            (edit_forward_deploy, "gameplay"),
            (edit_infantry_armor_wa, "gameplay"),
            (lambda source_path: edit_mg_teams(source_path, game_db), "gameplay"),
            (lambda source_path: global_bomber_edits(source_path, game_db), "gameplay"),
            (lambda source_path: add_radio_tag_to_mortars(source_path, game_db), "gameplay"),
            (add_swift_capacity, "gameplay"),
            (edit_capacities, "gameplay"),
            (edit_identify_rules, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Ammunition.ndf": [
            (lambda source_path: edit_ammunition(source_path, game_db), "gameplay"),
            (lambda source_path: apply_damage_families(source_path, game_db), "gameplay"),
            (lambda source_path: edit_he_damage(source_path, game_db), "gameplay"),
            (edit_aim_times, "gameplay"),
            (edit_weapon_ranges, "gameplay"),
            (bomb_damage_standards, "gameplay"),
            (change_fire_descriptors, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf": [
            (lambda source_path: edit_missiles(source_path, game_db), "gameplay"),
            (bomb_damage_standards, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf": [
            (lambda source_path: vanilla_renames_weapondescriptor(source_path, game_db), "gameplay"),
            (lambda source_path: create_new_weapons(source_path, game_db), "gameplay"),
            (lambda source_path: unit_edits_weapondescriptor(source_path, game_db), "gameplay"),
            (lambda source_path: apply_default_salves(source_path, game_db), "gameplay"),
            (lambda source_path: update_weapondescr_ammoname_quantity(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/MissileDescriptors.ndf": [
            (lambda source_path: edit_missile_speed(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/FireDescriptor.ndf": [
            (edit_fire_descriptors, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/OrderAvailability_Tactic.ndf": [
            (lambda source_path: edit_orderavailabilitytactic(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf": [
            (edit_smoke_duration, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf": [
            (edit_fob_attributes, "gameplay"),
            # TODO: Ask Eugen to add this to vanilla or allow for some texture editing exceptions for UI mods
            (add_fob_minimap_module, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/DamageLevels.ndf": [
            (edit_damage_levels, "gameplay"),
        ],
        # Effects and veterancy
        "GameData/Generated/Gameplay/Gfx/CapaciteList.ndf": [
            (edit_capacitelist, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf": [
            (edit_effetssurunite, "gameplay"),  # todo: this should be renamed to more generic effects editing function
            (edit_veterancy_effects, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/ConditionsDescriptor.ndf": [
            (edit_conditions, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf": [
            (edit_veterancy_hints, "gameplay"),
        ],
        # Depiction files
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialUnits.ndf": [
            (unit_edits_depictionaerial, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/MissileCarriage.ndf": [
            (unit_edits_missilecarriage, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/MissileCarriageDepiction.ndf": [
            (unit_edits_missilecarriagedepiction, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/ShowRoomUnits.ndf": [
            (edit_showroom_units, "gameplay"),
            (create_showroom_depictions, "gameplay"),
        ],
        # "GameData/Generated/Gameplay/Gfx/UniteCadavreDescriptor.ndf": [
        #     unit_edits_cadavre_descriptor,
        #     create_cadavre_depictions,
        # ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionAlternatives.ndf": [
            (create_alternatives_depictions, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionGhosts.ndf": [
            (create_ghost_depictions, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialGhosts.ndf": [
            (create_aerial_ghost_depictions, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionHumans.ndf": [
            (create_veh_human_depictions, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionVehicles.ndf": [
            (create_veh_depictions, "gameplay"),
            (unit_edits_depictionvehicles, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Infanterie/DepictionInfantry.ndf": [
            (lambda source_path: edit_infantry_depictions(source_path, game_db), "gameplay"),
            (lambda source_path: create_infantry_depictions(source_path, game_db), "gameplay"),
            (unit_edits_depictioninfantry, "gameplay"),
        ],
        # UI files
        # Style files
        "GameData/UserInterface/Style/Common/Colors.ndf": [
            (edit_colors, "ui"),
        ],
        "GameData/UserInterface/Style/Common/TextStyles.ndf": [
            (edit_textstyles, "ui"),
        ],
        "GameData/UserInterface/Style/DefaultStyle/DefaultStyleGuides.ndf": [
            (edit_defaultstyleguides, "ui"),
        ],
        "GameData/UserInterface/Style/DefaultStyle/DefaultTextFormatScript.ndf": [
            (edit_defaulttextformatscript, "ui"),
            (ui_gameplay_textscripts, "gameplay"),
        ],
        # Texture files
        "GameData/Generated/UserInterface/Textures/ButtonTexturesUnites.ndf": [
            (create_button_textures, "gameplay"),
        ],
        "GameData/Generated/UserInterface/Textures/SpecialityIconTextures.ndf": [
            (edit_specialty_icons, "gameplay"),
        ],
        "GameData/Generated/UserInterface/Textures/DivisionTextures.ndf": [
            (edit_division_emblems, "gameplay"),
        ],
        "GameData/UserInterface/Use/InGame/UseInGameTextures.ndf": [
            (edit_ingame_icons, "gameplay"),
        ],
        "GameData/Generated/UserInterface/Textures/MinimapIcons.ndf": [
            (add_fob_minimap_texture, "gameplay"),
        ],
        # Common UI templates and components
        # Not sure if this is needed or was ever needed, temporarily disabled.
        # "GameData/UserInterface/Use/Common/Templates/BuckSpecificBackgrounds.ndf": [
        #     edit_buckspecificbackgrounds,
        # ],
        "GameData/UserInterface/Use/Common/Templates/BuckSpecificButtons.ndf": [
            (edit_buckspecificbuttons, "ui"),
        ],
        "GameData/UserInterface/Use/Common/Views/BUCKSpecificHint.ndf": [
            (edit_buckspecifichint, "ui"),
        ],
        "GameData/UserInterface/Use/Common/CommonTextures.ndf": [
            (edit_commontextures, "ui"),
        ],
        "GameData/UserInterface/Use/Common/UISpecificChatView.ndf": [
            (edit_uispecificchatview, "ui"),
        ],
        "GameData/UserInterface/Use/Common/UISpecificUnitButtonView.ndf": [
            (edit_uispecificunitbuttonview, "ui"),
        ],
        "GameData/UserInterface/Use/Common/UIWarningPanel.ndf": [
            (edit_uiwarningpanel, "ui"),
        ],
        # In-game UI
        "GameData/UserInterface/Use/InGame/OrderDisplay.ndf": [
            (edit_orderdisplay, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UIInGameBUCKCubeAction.ndf": [
            (edit_uiingamebuckcubeaction, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UIIngameBUCKEngagementRules.ndf": [
            (edit_uiingamebuckengagementrules, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UIInGameDefaultContainer.ndf": [
            (edit_uiingamedefaultcontainer, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UIInGameHUDReplayResource.ndf": [
            (edit_uiingamehudreplayresource, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UIInGameLaunchBattleButtonResources.ndf": [
            (edit_uiingamelaunchbattlebuttonresources, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UIInGameMinimap.ndf": [
            (edit_uiingameminimap, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificHUDAlertPanelView.ndf": [
            (edit_uispecifichudalertpanelview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificHUDMultiSelectionPanelView.ndf": [
            (edit_uispecifichudmultiselectionpanelview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificHUDScoreView.ndf": [
            (edit_uispecifichudscoreview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificInGameHUDTimePanelView.ndf": [
            (edit_uispecificingamehudtimepanelview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificInGameIdleUnitView.ndf": [
            (edit_uispecificingameidleunitview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificInGamePlayerMissionLabelResources.ndf": [
            (edit_uispecificingameplayermissionlabelresources, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificMiniMapInfoView.ndf": [
            (edit_uispecificminimapinfoview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificOffMapView.ndf": [
            (edit_uispecificoffmapview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificOffMapAirplaneView.ndf": [
            (edit_uispecificoffmapairplaneview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificShortcutsForSelectionView.ndf": [
            (edit_uispecificshortcutsforselectionview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificSkirmishProductionMenuView.ndf": [
            (edit_uispecificskirmishproductionmenuview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitInfoPanelView.ndf": [
            (edit_unit_info_panel, "gameplay"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelAggregationView.ndf": [
            (edit_uispecificunitlabelaggregationview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelCommon.ndf": [
            (edit_uispecificunitlabelcommon, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelMultiSelectionView.ndf": [
            (edit_uispecificunitlabelmultiselectionview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelView.ndf": [
            (edit_uispecificunitlabelview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelViewNameOnly.ndf": [
            (edit_uispecificunitlabelviewnameonly, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitSelectionPanelView.ndf": [
            (edit_uispecificunitselectionpanelview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitSelectionWeaponPanelView.ndf": [
            (edit_uispecificunitselectionweaponpanelview, "ui"),
        ],
        "GameData/UserInterface/Use/InGame/UISpecificSmartGroupSelectionPanelView.ndf": [
            (edit_uispecificsmartgroupselectionpanelview, "ui"),
        ],
        # Out-game and ShowRoom UI
        "GameData/UserInterface/Use/OutGame/UISpecificLoginView.ndf": [
            (edit_uispecificloginview, "ui"),
        ],
        "GameData/UserInterface/Use/OutGame/UISpecificOutGameRecoverLoginView.ndf": [
            (edit_uispecificoutgamerecoverloginview, "ui"),
        ],
        "GameData/UserInterface/Use/OutGame/UISpecificOutGameRecoverPasswordView.ndf": [
            (edit_uispecificoutgamerecoverpasswordview, "ui"),
        ],
        "GameData/UserInterface/Use/OutGame/UseOutGameTextures.ndf": [
            (edit_useoutgametextures, "ui"),
        ],
        "GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomArmoryComponent.ndf": [
            (edit_uispecificshowroomarmorycomponent, "ui"),
        ],
        "GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomDeckCreatorScreenComponent.ndf": [
            (edit_uispecificshowroomdeckcreatorscreencomponent, "ui"),
        ],
        "GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomGroupsDeckCreatorScreenView.ndf": [
            (edit_uispecificshowroomgroupsdeckcreatorscreenview, "ui"),
        ],
        # Common UI templates and components
        "GameData/UserInterface/Use/Common/UICommonFlareLabelResources.ndf": [
            (edit_uicommonflarelabelresources, "ui"),
        ],
        # Generated UI files
        "GameData/Generated/UserInterface/Textures/WeaponTextures.ndf": [
            (edit_weapontextures, "gameplay"),
        ],
        "GameData/Generated/UserInterface/WeaponsMinMax.ndf": [
            (edit_weaponsminmax, "gameplay"),
        ],
        "GameData/Generated/UserInterface/UnitSpecialties.ndf": [
            (edit_specialties, "gameplay"),
        ],
        "GameData/Generated/UserInterface/WeaponTraits.ndf": [
            (edit_weapon_traits, "gameplay"),
        ],
        # Depiction files
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionVehiclesShowRoom.ndf": [
            (lambda source_path: create_veh_showroom_depictions(source_path), "gameplay"),  # Maybe unnecessary
        ],
        # UI files
        "GameData/UserInterface/Use/InGame/UIInGameResources.ndf": [
            (edit_uiingameresources, "ui"),
        ],
    }

    # We can leave the shared editors commented out for now if they're causing duplicates
    # shared_editors = get_shared_editors()
    # for path, editor_list in shared_editors.items():
    #     if path in editors:
    #         editors[path].extend(editor_list)
    #     else:
    #         editors[path] = editor_list

    # Write dictionary entries for veterancy bonuses
    if build_target == "gameplay":
        write_veterancy_tokens()

    return editors
