"""Central registry of all file editors."""

from typing import Callable, Dict, List

# New import structure
from .gameplay_mods import (
    # .gameplay
    edit_gameplay_constantes_gdconstants,
    edit_gameplay_constantes_ravitaillement,
    edit_gameplay_constantes_weaponconstantes,
    edit_gameplay_terrains,
    edit_gameplay_unit_airplanecritical,
    edit_gameplay_unit_groundunitcritical,
    edit_gameplay_unit_helicocritical,
    edit_gameplay_unit_infanteriecritical,
    edit_gameplay_unit_team,
    edit_gameplay_unit_templatecritical,
    edit_gameplay_unit_testunitscritical,
    # .generated
    edit_gen_gp_decks,
    edit_gen_gp_decks_deckpacks,
    edit_gen_gp_decks_deckserializer,
    edit_gen_gp_decks_divisioncostmatrix,
    edit_gen_gp_decks_divisionrules,
    edit_gen_gp_decks_divisions,
    edit_gen_gp_decks_strategicdecks,
    edit_gen_gp_decks_strategicpacks,
    edit_gen_gp_gfx_ammunition,
    edit_gen_gp_gfx_ammunitionmissiles,
    edit_gen_gp_gfx_missiledescriptors,
    edit_gen_gp_gfx_buildingdescriptors,
    edit_gen_gp_gfx_capacitelist,
    edit_gen_gp_gfx_conditionsdescriptor,
    edit_gen_gp_gfx_damagelevels,
    edit_gen_gp_gfx_damageresistance,
    edit_gen_gp_gfx_damageresistancefamilylist,
    edit_gen_gp_gfx_damageresistancefamilylistimpl,
    edit_gen_gp_gfx_depictionaerialghosts,
    edit_gen_gp_gfx_depictionaerialunits,
    edit_gen_gp_gfx_depictionaerialunitsshowroom,
    edit_gen_gp_gfx_depictionalternatives,
    edit_gen_gp_gfx_depictionghosts,
    edit_gen_gp_gfx_depictionhumans,
    edit_gen_gp_gfx_depictioninfantry,
    edit_gen_gp_gfx_depictionvehicles,
    edit_gen_gp_gfx_depictionvehiclesshowroom,
    edit_gen_gp_gfx_effetssurunite,
    edit_gen_gp_gfx_experiencelevels,
    edit_gen_gp_gfx_firedescriptor,
    edit_gen_gp_gfx_ndfdepictionlist,
    edit_gen_gp_gfx_mimeticghosts,
    edit_gen_gp_gfx_missilecarriage,
    edit_gen_gp_gfx_missilecarriagedepiction,
    edit_gen_gp_gfx_orderavailabilitytactic,
    edit_gen_gp_gfx_smokedescriptor,
    edit_gen_gp_gfx_unitedescriptor,
    edit_gen_gp_gfx_weapondescriptor,
    edit_gen_ui_buttontexturesunites,
    edit_gen_ui_divisiontextures,
    edit_gen_ui_minimapicons,
    edit_gen_ui_specialityicontextures,
    edit_gen_ui_unitspecialties,
    edit_gen_ui_weapontextures,
    edit_gen_ui_weapontraits,
    edit_gen_ui_weaponsminmax,
    # .userinterface
    edit_ui_ingame_useingametextures,
    edit_ui_ingame_uispecificunitinfopanelview,
    edit_ui_style_defaulttextformatscript,
)

# Import all UI editors
from src.ui_mods.style import (
    edit_buckspecificbuttons,
    edit_buckspecifichint,
    edit_colors,
    edit_commontextures,
    edit_defaultstyleguides,
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
__all__ = [
    # gameplay_mods.gameplay
    'edit_gameplay_constantes_gdconstants',
    'edit_gameplay_constantes_ravitaillement',
    'edit_gameplay_constantes_weaponconstantes',
    'edit_gameplay_terrains',
    'edit_gameplay_unit_airplanecritical',
    'edit_gameplay_unit_groundunitcritical',
    'edit_gameplay_unit_helicocritical',
    'edit_gameplay_unit_infanteriecritical',
    'edit_gameplay_unit_team',
    'edit_gameplay_unit_templatecritical',
    'edit_gameplay_unit_testunitscritical',
    # gameplay_mods.generated
    'edit_gen_gp_decks',
    'edit_gen_gp_decks_deckpacks',
    'edit_gen_gp_decks_deckserializer',
    'edit_gen_gp_decks_divisioncostmatrix',
    'edit_gen_gp_decks_divisionrules',
    'edit_gen_gp_decks_divisions',
    'edit_gen_gp_decks_strategicdecks',
    'edit_gen_gp_decks_strategicpacks',
    'edit_gen_gp_gfx_ammunition',
    'edit_gen_gp_gfx_ammunitionmissiles',
    'edit_gen_gp_gfx_missiledescriptors',
    'edit_gen_gp_gfx_buildingdescriptors',
    'edit_gen_gp_gfx_capacitelist',
    'edit_gen_gp_gfx_conditionsdescriptor',
    'edit_gen_gp_gfx_damagelevels',
    'edit_gen_gp_gfx_damageresistance',
    'edit_gen_gp_gfx_damageresistancefamilylist',
    'edit_gen_gp_gfx_damageresistancefamilylistimpl',
    'edit_gen_gp_gfx_depictionaerialghosts',
    'edit_gen_gp_gfx_depictionaerialunits',
    'edit_gen_gp_gfx_depictionaerialunitsshowroom',
    'edit_gen_gp_gfx_depictionalternatives',
    'edit_gen_gp_gfx_depictionghosts',
    'edit_gen_gp_gfx_depictionhumans',
    'edit_gen_gp_gfx_depictioninfantry',
    'edit_gen_gp_gfx_depictionvehicles',
    'edit_gen_gp_gfx_depictionvehiclesshowroom',
    'edit_gen_gp_gfx_effetssurunite',
    'edit_gen_gp_gfx_experiencelevels',
    'edit_gen_gp_gfx_firedescriptor',
    'edit_gen_gp_gfx_mimeticghosts',
    'edit_gen_gp_gfx_missilecarriage',
    'edit_gen_gp_gfx_missilecarriagedepiction',
    'edit_gen_gp_gfx_ndfdepictionlist',
    'edit_gen_gp_gfx_orderavailabilitytactic',
    'edit_gen_gp_gfx_smokedescriptor',
    'edit_gen_gp_gfx_unitedescriptor',
    'edit_gen_gp_gfx_weapondescriptor',
    'edit_gen_ui_buttontexturesunites',
    'edit_gen_ui_divisiontextures',
    'edit_gen_ui_minimapicons',
    'edit_gen_ui_specialityicontextures',
    'edit_gen_ui_unitspecialties',
    'edit_gen_ui_weapontextures',
    'edit_gen_ui_weapontraits',
    'edit_gen_ui_weaponsminmax',
    # gameplay_mods.userinterface
    'edit_ui_ingame_useingametextures',
    'edit_ui_ingame_uispecificunitinfopanelview',
    'edit_ui_style_defaulttextformatscript',
    # .ui_mods
    'edit_buckspecificbuttons',
    'edit_buckspecifichint',
    'edit_colors',
    'edit_commontextures',
    'edit_defaultstyleguides',
    'edit_orderdisplay',
    'edit_textstyles',
    'edit_uicommonflarelabelresources',
    'edit_uiingamebuckcubeaction',
    'edit_uiingamebuckengagementrules',
    'edit_uiingamedefaultcontainer',
    'edit_uiingamehudreplayresource',
    'edit_uiingamelaunchbattlebuttonresources',
    'edit_uiingameminimap',
    'edit_uiingameresources',
    'edit_uispecificchatview',
    'edit_uispecifichudalertpanelview',
    'edit_uispecifichudmultiselectionpanelview',
    'edit_uispecifichudscoreview',
    'edit_uispecificingamehudtimepanelview',
    'edit_uispecificingameidleunitview',
    'edit_uispecificingameplayermissionlabelresources',
    'edit_uispecificminimapinfoview',
    'edit_uispecificoffmapairplaneview',
    'edit_uispecificoffmapview',
    'edit_uispecificshortcutsforselectionview',
    'edit_uispecificshowroomarmorycomponent',
    'edit_uispecificshowroomdeckcreatorscreencomponent',
    'edit_uispecificshowroomgroupsdeckcreatorscreenview',
    'edit_uispecificskirmishproductionmenuview',
    'edit_uispecificunitbuttonview',
    'edit_uispecificunitlabelaggregationview',
    'edit_uispecificunitlabelcommon',
    'edit_uispecificunitlabelmultiselectionview',
    'edit_uispecificunitlabelview',
    'edit_uispecificunitlabelviewnameonly',
    'edit_uispecificunitselectionpanelview',
    'edit_uispecificunitselectionweaponpanelview',
    'edit_uispecificsmartgroupselectionpanelview',
    'edit_uiwarningpanel',
    'edit_useoutgametextures',
    'edit_uispecificloginview',
    'edit_uispecificoutgamerecoverloginview',
    'edit_uispecificoutgamerecoverpasswordview',
]

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def get_all_editors(config: Dict) -> Dict[str, List[Callable]]:
    """Get all file editors."""
    game_db = config.get("game_db", {})
    build_target = config["build_config"]["target"]

    editors = {
        # Core gameplay mechanics
        "GameData/Gameplay/Constantes/GDConstants.ndf": [
            (edit_gameplay_constantes_gdconstants, "gameplay"),
        ],
        "GameData/Gameplay/Constantes/Ravitaillement.ndf": [
            (edit_gameplay_constantes_ravitaillement, "gameplay"),
        ],
        "GameData/Gameplay/Constantes/WeaponConstantes.ndf": [
            (edit_gameplay_constantes_weaponconstantes, "gameplay"),
        ],
        "GameData/Gameplay/Terrains/Terrains.ndf": [
            (edit_gameplay_terrains, "gameplay"),
        ],
        "GameData/Gameplay/Unit/Tactic/Team.ndf": [
            (edit_gameplay_unit_team, "gameplay"),
        ],
        # Critical effect modules
        "GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Airplane.ndf": [
            (edit_gameplay_unit_airplanecritical, "gameplay"),
        ],
        "GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_GroundUnit.ndf": [
            (edit_gameplay_unit_groundunitcritical, "gameplay"),
        ],
        "GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Helico.ndf": [
            (edit_gameplay_unit_helicocritical, "gameplay"),
        ],
        "GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Infanterie.ndf": [
            (edit_gameplay_unit_infanteriecritical, "gameplay"),
        ],
        "GameData/Gameplay/Unit/CriticalModules/TemplateCriticalEffectModules.ndf": [
            (edit_gameplay_unit_templatecritical, "gameplay"),
        ],
        "GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_TestUnits.ndf": [
            (edit_gameplay_unit_testunitscritical, "gameplay"),
        ],
        # Division and deck files
        "GameData/Generated/Gameplay/Decks/DeckSerializer.ndf": [
            (edit_gen_gp_decks_deckserializer, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/Divisions.ndf": [
            (edit_gen_gp_decks_divisions, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/DivisionRules.ndf": [
            (lambda source_path: edit_gen_gp_decks_divisionrules(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/DeckPacks.ndf": [
            (lambda source_path: edit_gen_gp_decks_deckpacks(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/Decks.ndf": [
            (lambda source_path: edit_gen_gp_decks(source_path, game_db), "gameplay"),
            # TODO: Confirm if this is deprecated, not from main refactor but from a previous refactor of this specific task
            # (edit_deck_pack_lists, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/StrategicDecks.ndf": [
            (lambda source_path: edit_gen_gp_decks_strategicdecks(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/StrategicPacks.ndf": [
            (lambda source_path: edit_gen_gp_decks_strategicpacks(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf": [
            (lambda source_path: edit_gen_gp_decks_divisioncostmatrix(source_path), "gameplay"),
        ],
        # Damage system
        "GameData/Generated/Gameplay/Gfx/DamageResistance.ndf": [
            # TODO: Make sure damage family edits are applied first, but it should be written better not to (or at least give a warning in logs)
            (edit_gen_gp_gfx_damageresistance, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyList.ndf": [
            (edit_gen_gp_gfx_damageresistancefamilylist, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyListImpl.ndf": [
            (edit_gen_gp_gfx_damageresistancefamilylistimpl, "gameplay"),
        ],
        # Unit and weapon files
        "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf": [
            # Create new units first, before editing donors used to create them.
            # TODO: Confirm Eugen properly fixed this
            # lambda source_path: temp_fix_reco_radar(source_path, game_db),
            # TODO: Add back TypeUnitFormation to constants for new units and/or unit edits. Eugen removed it from
            # the TTypeUnitModuleDescriptor module and I thought it was just completely removed. But its now in its own
            # TFormationModuleDescriptor module, so we have to find out what the constants were that I removed.
            (lambda source_path: edit_gen_gp_gfx_unitedescriptor(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Ammunition.ndf": [
            (lambda source_path: edit_gen_gp_gfx_ammunition(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf": [
            (lambda source_path: edit_gen_gp_gfx_ammunitionmissiles(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf": [
            (lambda source_path: edit_gen_gp_gfx_weapondescriptor(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/MissileDescriptors.ndf": [
            (lambda source_path: edit_gen_gp_gfx_missiledescriptors(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/NdfDepictionList.ndf": [
            (edit_gen_gp_gfx_ndfdepictionlist, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/FireDescriptor.ndf": [
            (edit_gen_gp_gfx_firedescriptor, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/OrderAvailability_Tactic.ndf": [
            (lambda source_path: edit_gen_gp_gfx_orderavailabilitytactic(source_path, game_db), "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf": [
            (edit_gen_gp_gfx_smokedescriptor, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf": [
            (edit_gen_gp_gfx_buildingdescriptors, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/DamageLevels.ndf": [
            (edit_gen_gp_gfx_damagelevels, "gameplay"),
        ],
        # Effects and veterancy
        "GameData/Generated/Gameplay/Gfx/CapaciteList.ndf": [
            (edit_gen_gp_gfx_capacitelist, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf": [
            (edit_gen_gp_gfx_effetssurunite, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/ConditionsDescriptor.ndf": [
            (edit_gen_gp_gfx_conditionsdescriptor, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf": [
            (edit_gen_gp_gfx_experiencelevels, "gameplay"),
        ],
        # Depiction files
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialUnits.ndf": [
            (edit_gen_gp_gfx_depictionaerialunits, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialUnitsShowRoom.ndf": [
            (edit_gen_gp_gfx_depictionaerialunitsshowroom, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/MimeticGhosts.ndf": [
            (edit_gen_gp_gfx_mimeticghosts, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/MissileCarriage.ndf": [
            (edit_gen_gp_gfx_missilecarriage, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/MissileCarriageDepiction.ndf": [
            (edit_gen_gp_gfx_missilecarriagedepiction, "gameplay"),
        ],
        # "GameData/Generated/Gameplay/Gfx/UniteCadavreDescriptor.ndf": [
        #     unit_edits_cadavre_descriptor,
        #     create_cadavre_depictions,
        # ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionAlternatives.ndf": [
            (edit_gen_gp_gfx_depictionalternatives, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionGhosts.ndf": [
            (edit_gen_gp_gfx_depictionghosts, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialGhosts.ndf": [
            (edit_gen_gp_gfx_depictionaerialghosts, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionHumans.ndf": [
            (edit_gen_gp_gfx_depictionhumans, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionVehicles.ndf": [
            (edit_gen_gp_gfx_depictionvehicles, "gameplay"),
        ],
        "GameData/Generated/Gameplay/Gfx/Infanterie/DepictionInfantry.ndf": [
            (lambda source_path: edit_gen_gp_gfx_depictioninfantry(source_path, game_db), "gameplay"),
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
            (edit_ui_style_defaulttextformatscript, "gameplay"),
        ],
        # Texture files
        "GameData/Generated/UserInterface/Textures/ButtonTexturesUnites.ndf": [
            (edit_gen_ui_buttontexturesunites, "gameplay"),
        ],
        "GameData/Generated/UserInterface/Textures/SpecialityIconTextures.ndf": [
            (edit_gen_ui_specialityicontextures, "gameplay"),
        ],
        "GameData/Generated/UserInterface/Textures/DivisionTextures.ndf": [
            (edit_gen_ui_divisiontextures, "gameplay"),
        ],
        "GameData/UserInterface/Use/InGame/UseInGameTextures.ndf": [
            (edit_ui_ingame_useingametextures, "gameplay"),
        ],
        "GameData/Generated/UserInterface/Textures/MinimapIcons.ndf": [
            (edit_gen_ui_minimapicons, "gameplay"),
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
            (edit_ui_ingame_uispecificunitinfopanelview, "gameplay"),
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
            (edit_gen_ui_weapontextures, "gameplay"),
        ],
        "GameData/Generated/UserInterface/WeaponsMinMax.ndf": [
            (edit_gen_ui_weaponsminmax, "gameplay"),
        ],
        "GameData/Generated/UserInterface/UnitSpecialties.ndf": [
            (edit_gen_ui_unitspecialties, "gameplay"),
        ],
        "GameData/Generated/UserInterface/WeaponTraits.ndf": [
            (edit_gen_ui_weapontraits, "gameplay"),
        ],
        # Depiction files
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionVehiclesShowRoom.ndf": [
            (edit_gen_gp_gfx_depictionvehiclesshowroom, "gameplay"),
        ],
        # UI files
        "GameData/UserInterface/Use/InGame/UIInGameResources.ndf": [
            (edit_uiingameresources, "ui"),
        ],
    }

    return editors
