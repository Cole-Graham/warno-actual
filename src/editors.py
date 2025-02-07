"""Central registry of all file editors."""

from typing import Callable, Dict, List

# Import all gameplay editors
from src.gameplay import (
    unit_edits_divisionrules, 
    supply_divisionrules,
    supply_divisions,
    edit_mg_teams,
    apply_default_salves,
    ui_gameplay_textscripts,
    update_weapondescr_ammoname_quantity,
    edit_he_damage,
    edit_aim_times,
    edit_weapon_ranges,
    global_bomber_edits,
    bomb_damage_standards,
    edit_fire_descriptors,
    change_fire_descriptors,
    mg_team_division_rules,
    add_radio_tag_to_mortars,
    edit_smoke_duration,
    temp_fix_reco_radar,
    create_veh_showroom_depictions,
    deck_ap_points,
)
from src.gameplay.buildings import edit_fob_attributes

from src.gameplay.depictions import (
    create_aerial_ghost_depictions,
    create_alternatives_depictions,
    create_button_textures,
    create_cadavre_depictions,
    create_ghost_depictions,
    create_infantry_depictions,
    create_showroom_depictions,
    create_veh_depiction_selectors,
    create_veh_depictions,
    create_veh_human_depictions,
    edit_infantry_depictions,
    edit_showroom_units,
    unit_edits_depictionaerial,
    unit_edits_depictionvehicles,
    unit_edits_missilecarriage,
    unit_edits_missilecarriagedepiction,
    unit_edits_depictioninfantry,
)
from src.gameplay.divisions import (
    add_division_rules,
    add_to_divisions,
    create_division_packs,
    edit_division_matrices,
    edit_division_units,
    update_deck_serializer,
)
from src.gameplay.effects import (
    edit_capacite_list,
    edit_critical_effects,
    edit_shock_effects,
    edit_shock_effects_packs_list,
    edit_shock_units,
)
from src.gameplay.game_constants import (
    edit_gd_constantes,
    edit_orders,
    edit_ravitaillement,
)
from src.gameplay.terrains import edit_terrains

# Add new import
from src.gameplay.ui import (
    edit_division_emblems,
    edit_ingame_icons,
    edit_specialties,
    edit_specialty_icons,
    edit_unit_info_panel,
    edit_weaponsminmax,
    edit_weapontextures,
)
from src.gameplay.unit_descriptor import (
    create_new_units,
    edit_antirad_optics,
    edit_auto_cover,
    edit_forward_deploy,
    edit_infantry_armor_wa,
    edit_team_supply,
    edit_units,
)
from src.gameplay.veterancy.vet_bonuses import (
    edit_veterancy_effects,
    edit_veterancy_hints,
    write_veterancy_tokens,
)
from src.gameplay.weapons.ammunition import edit_ammunition
from src.gameplay.weapons.damage_families import (
    add_damage_families_to_impl,
    add_damage_families_to_list,
    add_damage_resistance_values,
    apply_damage_families,
    apply_damage_family_edits,
    edit_infantry_armor,
    edit_weapon_constantes,
)
from src.gameplay.weapons.missiles import edit_missiles, edit_missile_speed
from src.gameplay.weapons.new_weapons import create_new_weapons
from src.gameplay.weapons.unit_edits import unit_edits_weapondescriptor
from src.shared import get_shared_editors
from src.shared.buildings.fob import add_fob_minimap_texture

# Import all UI editors
from src.ui.style import (
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
    edit_uiwarningpanel,
    edit_useoutgametextures,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def get_all_editors(config: Dict) -> Dict[str, List[Callable]]:
    """Get all file editors."""
    game_db = config.get('game_db', {})
    
    editors = {
        # Core gameplay mechanics
        "GameData/Gameplay/Constantes/GDConstantes.ndf": [
            edit_gd_constantes,
        ],
        "GameData/Gameplay/Constantes/Ravitaillement.ndf": [
            edit_ravitaillement,
        ],
        "GameData/Gameplay/Constantes/WeaponConstantes.ndf": [
            edit_weapon_constantes,
        ],
        "GameData/Gameplay/Terrains/Terrains.ndf": [
            edit_terrains,
        ],
        "GameData/Gameplay/Unit/Tactic/Team.ndf": [
            edit_team_supply,
        ],
        "GameData/Gameplay/Unit/CriticalModules/TemplateCriticalEffectModules.ndf": [
            edit_critical_effects,
        ],

        # Division and deck files
        "GameData/Generated/Gameplay/Decks/DeckSerializer.ndf": [
            update_deck_serializer,
        ],
        "GameData/Generated/Gameplay/Decks/Divisions.ndf": [
            # add_to_divisions, 
            # edit_division_units,
            # supply_divisions,
            deck_ap_points,
        ],
        "GameData/Generated/Gameplay/Decks/DivisionRules.ndf": [
            add_division_rules,
            unit_edits_divisionrules,
            supply_divisionrules,
            lambda source_path: mg_team_division_rules(source_path, game_db),
        ],
        # "GameData/Generated/Gameplay/Decks/DivisionPacks.ndf": [
        #     create_division_packs,
        # ],

        "GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf": [
            edit_division_matrices,
        ],

        # Damage system
        "GameData/Generated/Gameplay/Gfx/DamageResistance.ndf": [
            add_damage_resistance_values,
            apply_damage_family_edits,
            edit_infantry_armor,
        ],
        "GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyList.ndf": [
            add_damage_families_to_list,
        ],
        "GameData/Generated/Gameplay/Gfx/DamageResistanceFamilyListImpl.ndf": [
            add_damage_families_to_impl,
        ],

        # Unit and weapon files
        "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf": [
            # Create new units first, before editing donors used to create them.
            lambda source_path: temp_fix_reco_radar(source_path, game_db),
            lambda source_path: create_new_units(source_path, game_db),
            lambda source_path: edit_units(source_path, game_db),
            lambda source_path: edit_auto_cover(source_path, game_db),
            edit_antirad_optics,
            edit_forward_deploy,
            edit_infantry_armor_wa,
            lambda source_path: edit_shock_units(source_path, game_db),
            lambda source_path: edit_mg_teams(source_path, game_db),
            lambda source_path: global_bomber_edits(source_path, game_db),
            lambda source_path: add_radio_tag_to_mortars(source_path, game_db),
        ],
        "GameData/Generated/Gameplay/Gfx/Ammunition.ndf": [
            lambda source_path: edit_ammunition(source_path, game_db),
            lambda source_path: apply_damage_families(source_path, game_db),
            lambda source_path: edit_he_damage(source_path, game_db),
            edit_aim_times,
            edit_weapon_ranges,
            bomb_damage_standards,
            change_fire_descriptors,
        ],
        "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf": [
            lambda source_path: edit_missiles(source_path, game_db),
            bomb_damage_standards,
        ],
        "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf": [
            lambda source_path: unit_edits_weapondescriptor(source_path, game_db),
            lambda source_path: apply_default_salves(source_path, game_db),
            lambda source_path: create_new_weapons(source_path, game_db),
            lambda source_path: update_weapondescr_ammoname_quantity(source_path, game_db),
        ],
        "GameData/Generated/Gameplay/Gfx/MissileDescriptors.ndf": [
            lambda source_path: edit_missile_speed(source_path, game_db),
        ],
        "GameData/Generated/Gameplay/Gfx/FireDescriptor.ndf": [
            edit_fire_descriptors,
        ],
        "GameData/Generated/Gameplay/Gfx/OrderAvailability_Tactic.ndf": [
            lambda source_path: edit_orders(source_path, game_db),
        ],
        "GameData/Generated/Gameplay/Gfx/SmokeDescriptor.ndf": [
            edit_smoke_duration,
        ],
        "GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf": [
            edit_fob_attributes,
        ],

        # Effects and veterancy
        "GameData/Generated/Gameplay/Gfx/CapaciteList.ndf": [
            edit_capacite_list,
        ],
        # "GameData/Generated/Gameplay/Gfx/EffectsPacksList.ndf": [
        #     edit_shock_effects_packs_list,
        # ],
        "GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf": [
            edit_shock_effects,
            edit_veterancy_effects,
        ],
        "GameData/Generated/Gameplay/Gfx/ExperienceLevels.ndf": [
            edit_veterancy_hints,
        ],

        # Depiction files
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialUnits.ndf": [
            unit_edits_depictionaerial,
        ],
        "GameData/Generated/Gameplay/Gfx/MissileCarriage.ndf": [
            unit_edits_missilecarriage,
        ],
        "GameData/Generated/Gameplay/Gfx/MissileCarriageDepiction.ndf": [
            unit_edits_missilecarriagedepiction,
        ],
        "GameData/Generated/Gameplay/Gfx/ShowRoomUnits.ndf": [
            edit_showroom_units,
            create_showroom_depictions,
        ],
        "GameData/Generated/Gameplay/Gfx/UniteCadavreDescriptor.ndf": [
            create_cadavre_depictions,
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionAlternatives.ndf": [
            create_alternatives_depictions,
        ],
        # "GameData/Generated/Gameplay/Gfx/Depictions/GeneratedDepictionSelectors.ndf": [
        #     create_veh_depiction_selectors,
        # ],
        "GameData/Generated/Gameplay/Gfx/Depictions/GeneratedDepictionGhosts.ndf": [
            create_ghost_depictions,
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/GeneratedDepictionAerialGhosts.ndf": [
            create_aerial_ghost_depictions,
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/GeneratedDepictionHumans.ndf": [
            create_veh_human_depictions,
        ],
        "GameData/Generated/Gameplay/Gfx/Depictions/DepictionVehicles.ndf": [
            create_veh_depictions,
            unit_edits_depictionvehicles,
        ],
        "GameData/Generated/Gameplay/Gfx/Infanterie/GeneratedDepictionInfantry.ndf": [
            lambda source_path: edit_infantry_depictions(source_path, game_db['ammunition'], game_db['depiction_data']),
            create_infantry_depictions,
            unit_edits_depictioninfantry,
        ],
        # UI files
        # Style files
        "GameData/UserInterface/Style/Common/Colors.ndf": [
            edit_colors,
        ],
        "GameData/UserInterface/Style/Common/TextStyles.ndf": [
            edit_textstyles,
        ],
        "GameData/UserInterface/Style/DefaultStyle/DefaultStyleGuides.ndf": [
            edit_defaultstyleguides,
        ],
        "GameData/UserInterface/Style/DefaultStyle/DefaultTextFormatScript.ndf": [
            edit_defaulttextformatscript,
            ui_gameplay_textscripts,
        ],
        
        # Texture files
        "GameData/Generated/UserInterface/Textures/ButtonTexturesUnites.ndf": [
            create_button_textures,
        ],
        "GameData/Generated/UserInterface/Textures/SpecialityIconTextures.ndf": [
            edit_specialty_icons,
        ],
        "GameData/Generated/UserInterface/Textures/DivisionTextures.ndf": [
            edit_division_emblems,
        ],
        "GameData/UserInterface/Use/InGame/UseInGameTextures.ndf": [
            edit_ingame_icons,
        ],
        "GameData/Generated/UserInterface/Textures/MinimapIcons.ndf": [
            add_fob_minimap_texture,  # Direct function reference instead of lambda
        ],
        
        # Common UI templates and components
        "GameData/UserInterface/Use/Common/Templates/BuckSpecificBackgrounds.ndf": [
            edit_buckspecificbackgrounds,
        ],
        "GameData/UserInterface/Use/Common/Templates/BuckSpecificButtons.ndf": [
            edit_buckspecificbuttons,
        ],
        "GameData/UserInterface/Use/Common/Views/BUCKSpecificHint.ndf": [
            edit_buckspecifichint,
        ],
        "GameData/UserInterface/Use/Common/CommonTextures.ndf": [
            edit_commontextures,
        ],
        "GameData/UserInterface/Use/Common/UISpecificChatView.ndf": [
            edit_uispecificchatview,
        ],
        "GameData/UserInterface/Use/Common/UISpecificUnitButtonView.ndf": [
            edit_uispecificunitbuttonview,
        ],
        "GameData/UserInterface/Use/Common/UIWarningPanel.ndf": [
            edit_uiwarningpanel,
        ],

        # In-game UI
        "GameData/UserInterface/Use/InGame/OrderDisplay.ndf": [
            edit_orderdisplay,
        ],
        "GameData/UserInterface/Use/InGame/UIInGameBUCKCubeAction.ndf": [
            edit_uiingamebuckcubeaction,
        ],
        "GameData/UserInterface/Use/InGame/UIIngameBUCKEngagementRules.ndf": [
            edit_uiingamebuckengagementrules,
        ],
        "GameData/UserInterface/Use/InGame/UIInGameDefaultContainer.ndf": [
            edit_uiingamedefaultcontainer,
        ],
        "GameData/UserInterface/Use/InGame/UIInGameHUDReplayResource.ndf": [
            edit_uiingamehudreplayresource,
        ],
        "GameData/UserInterface/Use/InGame/UIInGameLaunchBattleButtonResources.ndf": [
            edit_uiingamelaunchbattlebuttonresources,
        ],
        "GameData/UserInterface/Use/InGame/UIInGameMinimap.ndf": [
            edit_uiingameminimap,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificHUDAlertPanelView.ndf": [
            edit_uispecifichudalertpanelview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificHUDMultiSelectionPanelView.ndf": [
            edit_uispecifichudmultiselectionpanelview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificHUDScoreView.ndf": [
            edit_uispecifichudscoreview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificInGameHUDTimePanelView.ndf": [
            edit_uispecificingamehudtimepanelview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificInGameIdleUnitView.ndf": [
            edit_uispecificingameidleunitview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificInGamePlayerMissionLabelResources.ndf": [
            edit_uispecificingameplayermissionlabelresources,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificMiniMapInfoView.ndf": [
            edit_uispecificminimapinfoview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificOffMapView.ndf": [
            edit_uispecificoffmapview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificOffMapAirplaneView.ndf": [
            edit_uispecificoffmapairplaneview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificShortcutsForSelectionView.ndf": [
            edit_uispecificshortcutsforselectionview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificSkirmishProductionMenuView.ndf": [
            edit_uispecificskirmishproductionmenuview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitInfoPanelView.ndf": [
            edit_unit_info_panel,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelAggregationView.ndf": [
            edit_uispecificunitlabelaggregationview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelCommon.ndf": [
            edit_uispecificunitlabelcommon,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelMultiSelectionView.ndf": [
            edit_uispecificunitlabelmultiselectionview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelView.ndf": [
            edit_uispecificunitlabelview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelViewNameOnly.ndf": [
            edit_uispecificunitlabelviewnameonly,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitSelectionPanelView.ndf": [
            edit_uispecificunitselectionpanelview,
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitSelectionWeaponPanelView.ndf": [
            edit_uispecificunitselectionweaponpanelview,
        ],

        # Out-game and ShowRoom UI
        "GameData/UserInterface/Use/OutGame/UseOutGameTextures.ndf": [
            edit_useoutgametextures,
        ],
        "GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomArmoryComponent.ndf": [
            edit_uispecificshowroomarmorycomponent,
        ],
        "GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomDeckCreatorScreenComponent.ndf": [
            edit_uispecificshowroomdeckcreatorscreencomponent,
        ],
        "GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomGroupsDeckCreatorScreenView.ndf": [
            edit_uispecificshowroomgroupsdeckcreatorscreenview,
        ],

        # Common UI templates and components
        "GameData/UserInterface/Use/Common/UICommonFlareLabelResources.ndf": [
            edit_uicommonflarelabelresources,
        ],

        # Generated UI files
        "GameData/Generated/UserInterface/Textures/WeaponTextures.ndf": [
            edit_weapontextures,
        ],
        "GameData/Generated/UserInterface/WeaponsMinMax.ndf": [
            edit_weaponsminmax,
        ],
        "GameData/Generated/UserInterface/UnitSpecialties.ndf": [
            edit_specialties,
        ],


        # Depiction files
        "GameData/Generated/Gameplay/Gfx/Depictions/GeneratedDepictionVehiclesShowRoom.ndf": [
            lambda source_path: create_veh_showroom_depictions(source_path) # Maybe unnecessary
        ],
        
        # UI files
        "GameData/UserInterface/Use/InGame/UIInGameResources.ndf": [
            edit_uiingameresources,
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
    write_veterancy_tokens()

    return editors 