"""Functions for modifying UI HUD skirmish production menu view."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecificskirmishproductionmenuview(source_path) -> None:
    """Edit UISpecificSkirmishProductionMenuView.ndf.
    
    Args:
        source_path: NDF file containing HUD production menu view definitions
    """
    logger.info("Editing UISpecificSkirmishProductionMenuView.ndf")
    
    # Update main component
    _update_main_component(source_path)
    
    # Update game info panel
    _update_game_info_panel(source_path)
    
    # Update command points display
    _update_command_points(source_path)
    
    # Update command points timer
    _update_command_points_timer(source_path)
    
    # Update sector display
    _update_sector_display(source_path)
    
    # Update production buttons
    _update_production_buttons(source_path)
    
    # Update skirmish production menu pawn button
    _update_skirmish_production_menu_pawn_button(source_path)


def _update_skirmish_production_menu_pawn_button(source_path) -> None:
    """SkirmishProductionMenuPawnButton.
    UISpecificSkirmishProductionMenuView.ndf
    """
    skirmishproductionmenupawnbutton = source_path.by_namespace("SkirmishProductionMenuPawnButton").v
    for component in skirmishproductionmenupawnbutton.by_member("Components").v:
        if isinstance(component.v, ndf.model.Object):
            if is_obj_type(component.v, "PanelRoundedCorner"):
                component.v.by_member("BackgroundBlockColorToken").v = '"BoutonTemps_Background_M81"'
                component.v.by_member("BorderLineColorToken").v = '"BoutonTemps_Line_M81"'
            # handle other object components here with elif statements
        # handle other components here with elif statements
    
    skirmishproductionmenucategorybutton = source_path.by_namespace("SkirmishProductionMenuCategoryButton").v
    skirmishproductionmenucategorybutton.by_member("TextColorToken").v = '"ButtonHUD/Text2_M81"'

    logger.debug("Updated SkirmishProductionMenuPawnButton properties")

def _update_main_component(source_path) -> None:
    """Update main component properties."""
    maincomponent = source_path.by_namespace("BUCKSpecificSkirmishProductionMenuMainComponentDescriptor").v
    
    for component in maincomponent.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKListDescriptor"):
            continue
            
        if component.v.by_member("ElementName", False) is None:
            continue
            
        if component.v.by_member("ElementName").v == '"UnitProductionList"':
            component.v.by_member("InterItemMargin").v = "TRTTILength(Magnifiable = 15.0)"
    
    logger.debug("Updated main component properties")


def _update_game_info_panel(source_path) -> None:
    """Update game info panel properties."""
    panelinfopartie = source_path.by_namespace("PanelInfoPartie").v
    
    # Update frame
    componentframe = panelinfopartie.by_member("ComponentFrame").v
    componentframe.by_member("AlignementToFather").v = "[0.0, 0.0]"
    componentframe.by_member("AlignementToAnchor").v = "[0.0, 0.0]"
    componentframe.by_member("MagnifiableOffset").v = "[600.0, 4.0]"
    
    # Update background
    for component in panelinfopartie.by_member("BackgroundComponents").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        component.v.by_member("BackgroundBlockColorToken").v = '"M81_Artichoke"'
        component.v.by_member("BorderLineColorToken").v = '"M81_ArtichokeVeryLight"'
    
    logger.debug("Updated game info panel properties")


def _update_command_points(source_path) -> None:
    """Replace command points row with VIP-compliant nested list elements."""
    index = source_path.by_namespace("PointsCommandement").index
    source_path.replace(index, _get_points_commandement())
    logger.debug("Updated command points display (VIP nested horizontal list slots)")


def _get_points_commandement() -> str:
    """Horizontal list: X alignment on inner widgets only (not list slots)."""
    return '''\
private PointsCommandement is BUCKListDescriptor
(
    ComponentFrame = TUIFramePropertyRTTI
    (
        RelativeWidthHeight = [0.0, 1.0]
        MagnifiableOffset = [0.0, 0.0]
    )

    Axis = ~/ListAxis/Horizontal
    FirstMargin = TRTTILength(Magnifiable = 72.0)
    InterItemMargin = TRTTILength(Magnifiable = 4.0)
    LastMargin = TRTTILength(Magnifiable = 16.0)

    HasBorder = true
    BorderThicknessToken = "1"
    BorderLineColorToken = "M81_ArtichokeVeryLight"
    BordersToDraw = ~/TBorderSide/Right

    BackgroundComponents =
    [
        PanelRoundedCorner
        (
            BackgroundBlockColorToken = "M81_Quincy"
            BorderLineColorToken = "M81_ArtichokeVeryLight"
        ),
    ]

    Elements =
    [
        BUCKListElementDescriptor
        (
            ComponentDescriptor = BUCKContainerDescriptor
            (
                ComponentFrame = TUIFramePropertyRTTI
                (
                    MagnifiableWidthHeight = [16.0, 16.0]
                    AlignementToFather = [0.0, 0.5]
                    AlignementToAnchor = [0.0, 0.5]
                )
                FitStyle = ~/ContainerFitStyle/FitToContent
                Components =
                [
                    BUCKTextureDescriptor
                    (
                        ElementName = "CommandPoints"
                        ComponentFrame = TUIFramePropertyRTTI
                        (
                            MagnifiableWidthHeight = [16.0, 16.0]
                            AlignementToFather = [0.0, 0.5]
                            AlignementToAnchor = [4.0, 0.5]
                        )
                        TextureToken = "UseInGame_CommandPoints"
                        Components =
                        [
                            BUCKSpecificHintableArea
                            (
                                HintBodyToken = "LR_cmd"
                                DicoToken = ~/LocalisationConstantes/dico_interface_ingame
                            ),
                        ]
                    ),
                ]
            )
        ),
        BUCKListElementDescriptor
        (
            ComponentDescriptor = BUCKTextDescriptor
            (
                UniqueName = "CommmandPointsText"
                ComponentFrame = TUIFramePropertyRTTI
                (
                    RelativeWidthHeight = [0.0, 1.0]
                    AlignementToFather = [0.0, 0.5]
                    AlignementToAnchor = [0.0, 0.5]
                )
                ParagraphStyle = TParagraphStyle
                (
                    Alignment = UIText_Right
                    VerticalAlignment = UIText_VerticalCenter
                    InterLine = 0
                )
                TextStyle = "Default"
                HorizontalFitStyle = ~/FitStyle/UserDefined
                TypefaceToken = "Liberator"
                BigLineAction = ~/BigLineAction/CutByDots
                TextDico = ~/LocalisationConstantes/dico_interface_ingame
                TextToken = "HPROD_CMDP"
                TextColor = "Gold"
                TextSize = "26"
                Hint = BUCKSpecificHintableArea
                (
                    DicoToken = ~/LocalisationConstantes/dico_interface_ingame
                    HintBodyToken = "LR_cmd"
                )
            )
        ),
        BUCKListElementDescriptor
        (
            ComponentDescriptor = BUCKContainerDescriptor
            (
                ComponentFrame = TUIFramePropertyRTTI
                (
                    RelativeWidthHeight = [0.0, 1.0]
                    AlignementToFather = [0.0, 0.5]
                    AlignementToAnchor = [0.0, 0.5]
                )
                FitStyle = ~/ContainerFitStyle/FitToContent
                Components =
                [
                    BUCKTextDescriptor
                    (
                        UniqueName = "CommmandPointsIncomeText"
                        ComponentFrame = TUIFramePropertyRTTI
                        (
                            RelativeWidthHeight = [0.0, 1.0]
                            AlignementToFather = [0.0, 0.5]
                            AlignementToAnchor = [-0.25, 0.625]
                        )
                        ParagraphStyle = TParagraphStyle
                        (
                            Alignment = UIText_Right
                            VerticalAlignment = UIText_VerticalCenter
                            InterLine = 0
                        )
                        TextStyle = "Default"
                        HorizontalFitStyle = ~/FitStyle/FitToContent
                        TypefaceToken = "Liberator"
                        BigLineAction = ~/BigLineAction/CutByDots
                        TextDico = ~/LocalisationConstantes/dico_interface_ingame
                        TextToken = "HPROD_CMDI"
                        TextColor = "Gold"
                        TextSize = "16"
                        Hint = BUCKSpecificHintableArea
                        (
                            UniqueName = "CommmandPointsIncomeHintText"
                            ForbiddenTags = ["StrategicScenario"]
                            DicoToken = ~/LocalisationConstantes/dico_interface_ingame
                            HintTitleToken = "HPD_INCT"
                            HintBodyToken = "LR_incob"
                        )
                    ),
                ]
            )
        ),
    ]
)'''


def _update_command_points_timer(source_path) -> None:
    """Update command points timer properties."""
    chronopointcommandement = source_path.by_namespace("ChronoPointCommandement").v
    chronopointcommandement.by_member("BorderLineColorToken").v = '"M81_ArtichokeVeryLight"'
    chronopointcommandement.add(_get_chrono_command_points_background())
    logger.debug("Updated command points timer properties")


def _get_chrono_command_points_background() -> str:
    """Background panel for ChronoPointCommandement (same tokens as PointsCommandement)."""
    return '''\
BackgroundComponents = [
    PanelRoundedCorner
    (
        BackgroundBlockColorToken = "M81_Quincy"
        BorderLineColorToken = "M81_ArtichokeVeryLight"
    )
]'''


def _update_sector_display(source_path) -> None:
    """Update sector display properties."""
    nombresecteur = source_path.by_namespace("NombreSecteur").v
    nombresecteur.by_member("BorderLineColorToken").v = '"M81_ArtichokeVeryLight"'
    
    for element in nombresecteur.by_member("Elements").v:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.by_member("UniqueName", False) is None:  # noqa
            continue
            
        if component_descr.by_member("UniqueName").v == '"SectorPointsGauge"':  # noqa
            component_descr.by_member("BorderLineColorToken").v = '"M81_ArtichokeVeryLight"'  # noqa
    
    logger.debug("Updated sector display properties")


def _update_production_buttons(source_path) -> None:
    """Update production button properties."""
    # Smart group button
    smartgrouptypeproductionbutton = source_path.by_namespace("SmartGroupTypeProductionButton").v
    smartgrouptypeproductionbutton.by_member("BackgroundBlockColorToken").v = '"BoutonTemps_Background_M81"'
    smartgrouptypeproductionbutton.by_member("TextColorToken").v = '"ButtonHUD/Text2_M81"'
    
    # Deck type button
    decktypeproductionbutton = source_path.by_namespace("DeckTypeProductionButton").v
    decktypeproductionbutton.by_member("BackgroundBlockColorToken").v = '"BoutonTemps_Background_M81"'
    decktypeproductionbutton.by_member("TextColorToken").v = '"ButtonHUD/Text2_M81"'
    
    # Combat group button
    combatgroupproductionbutton = source_path.by_namespace("SkirmishProductionMenuCombatGroupButton").v
    combatgroupproductionbutton.by_member("PanelRoundedCorner_BackgroundBlockColorToken").v = '"BoutonTemps_Background_M81"'
    combatgroupproductionbutton.by_member("TextColorToken").v = '"ButtonHUD/Text2_M81"'
    combatgroupproductionbutton.by_member("ButtonMagnifiableWidthHeight").v = "[105, 30.0]"
    
    # Pawn button
    skirmishproductionmenupawnbutton = source_path.by_namespace("SkirmishProductionMenuPawnButton").v
    for component in skirmishproductionmenupawnbutton.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        component.v.by_member("RoundedVertexes").v = "[false, false, false, true]"
    
    logger.debug("Updated production button properties")
