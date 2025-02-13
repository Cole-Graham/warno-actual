"""UI modification module."""

from typing import Any, Callable, Dict, List  # noqa

from .style import (
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
    edit_uispecificunitlabelviewnameonly,
    edit_uispecificunitlabelview,
    edit_uispecificunitselectionpanelview,
    edit_uispecificunitselectionweaponpanelview,
    edit_uiwarningpanel,
    edit_useoutgametextures,
)


def get_ui_editors() -> Dict[str, List[Callable]]:
    # defunct (for now? I had to simplify config/build pipelines to get the patcher working)
    """Get UI file editors."""
    return {
        # Style files
        "GameData/UserInterface/Style/Common/Colors.ndf": [
            lambda source_path: edit_colors(source_path)
        ],
        "GameData/UserInterface/Style/Common/TextStyles.ndf": [
            lambda source_path: edit_textstyles(source_path)
        ],
        "GameData/UserInterface/Style/DefaultStyle/DefaultStyleGuides.ndf": [
            lambda source_path: edit_defaultstyleguides(source_path)
        ],
        "GameData/UserInterface/Style/DefaultStyle/DefaultTextFormatScript.ndf": [
            lambda source_path: edit_defaulttextformatscript(source_path)
        ],
        
        # Common UI templates and components
        "GameData/UserInterface/Use/Common/UICommonFlareLabelResources.ndf": [
            lambda source_path: edit_uicommonflarelabelresources(source_path)
        ],
        "GameData/UserInterface/Use/Common/CommonTextures.ndf": [
            lambda source_path: edit_commontextures(source_path)
        ],
        "GameData/UserInterface/Use/Common/Templates/BuckSpecificBackgrounds.ndf": [
            lambda source_path: edit_buckspecificbackgrounds(source_path)
        ],
        "GameData/UserInterface/Use/Common/Templates/BuckSpecificButtons.ndf": [
            lambda source_path: edit_buckspecificbuttons(source_path)
        ],
        "GameData/UserInterface/Use/Common/Views/BUCKSpecificHint.ndf": [
            lambda source_path: edit_buckspecifichint(source_path)
        ],
        "GameData/UserInterface/Use/Common/UISpecificChatView.ndf": [
            lambda source_path: edit_uispecificchatview(source_path)
        ],
        "GameData/UserInterface/Use/Common/UISpecificUnitButtonView.ndf": [
            lambda source_path: edit_uispecificunitbuttonview(source_path)
        ],
        "GameData/UserInterface/Use/Common/UIWarningPanel.ndf": [
            lambda source_path: edit_uiwarningpanel(source_path)
        ],

        # In-game UI
        "GameData/UserInterface/Use/InGame/OrderDisplay.ndf": [
            lambda source_path: edit_orderdisplay(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UIInGameBUCKCubeAction.ndf": [
            lambda source_path: edit_uiingamebuckcubeaction(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UIIngameBUCKEngagementRules.ndf": [
            lambda source_path: edit_uiingamebuckengagementrules(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UIInGameDefaultContainer.ndf": [
            lambda source_path: edit_uiingamedefaultcontainer(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UIInGameHUDReplayResource.ndf": [
            lambda source_path: edit_uiingamehudreplayresource(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UIInGameLaunchBattleButtonResources.ndf": [
            lambda source_path: edit_uiingamelaunchbattlebuttonresources(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UIInGameMinimap.ndf": [
            lambda source_path: edit_uiingameminimap(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificHUDAlertPanelView.ndf": [
            lambda source_path: edit_uispecifichudalertpanelview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificHUDMultiSelectionPanelView.ndf": [
            lambda source_path: edit_uispecifichudmultiselectionpanelview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificHUDScoreView.ndf": [
            lambda source_path: edit_uispecifichudscoreview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificInGameHUDTimePanelView.ndf": [
            lambda source_path: edit_uispecificingamehudtimepanelview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificInGameIdleUnitView.ndf": [
            lambda source_path: edit_uispecificingameidleunitview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificInGamePlayerMissionLabelResources.ndf": [
            lambda source_path: edit_uispecificingameplayermissionlabelresources(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificMiniMapInfoView.ndf": [
            lambda source_path: edit_uispecificminimapinfoview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificOffMapView.ndf": [
            lambda source_path: edit_uispecificoffmapview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificOffMapAirplaneView.ndf": [
            lambda source_path: edit_uispecificoffmapairplaneview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificShortcutsForSelectionView.ndf": [
            lambda source_path: edit_uispecificshortcutsforselectionview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificSkirmishProductionMenuView.ndf": [
            lambda source_path: edit_uispecificskirmishproductionmenuview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelAggregationView.ndf": [
            lambda source_path: edit_uispecificunitlabelaggregationview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelCommon.ndf": [
            lambda source_path: edit_uispecificunitlabelcommon(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelMultiSelectionView.ndf": [
            lambda source_path: edit_uispecificunitlabelmultiselectionview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelView.ndf": [
            lambda source_path: edit_uispecificunitlabelview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitLabelViewNameOnly.ndf": [
            lambda source_path: edit_uispecificunitlabelviewnameonly(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitSelectionPanelView.ndf": [
            lambda source_path: edit_uispecificunitselectionpanelview(source_path)
        ],
        "GameData/UserInterface/Use/InGame/UISpecificUnitSelectionWeaponPanelView.ndf": [
            lambda source_path: edit_uispecificunitselectionweaponpanelview(source_path)
        ],

        # Out-game and ShowRoom UI
        "GameData/UserInterface/Use/OutGame/UseOutGameTextures.ndf": [
            lambda source_path: edit_useoutgametextures(source_path)
        ],
        "GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomArmoryComponent.ndf": [
            lambda source_path: edit_uispecificshowroomarmorycomponent(source_path)
        ],
        "GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomDeckCreatorScreenComponent.ndf": [
            lambda source_path: edit_uispecificshowroomdeckcreatorscreencomponent(source_path)
        ],
        "GameData/UserInterface/Use/ShowRoom/Views/UISpecificShowRoomGroupsDeckCreatorScreenView.ndf": [
            lambda source_path: edit_uispecificshowroomgroupsdeckcreatorscreenview(source_path)
        ],
    }
