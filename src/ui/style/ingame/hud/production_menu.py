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
    """Update command points display properties."""
    pointscommandement = source_path.by_namespace("PointsCommandement").v
    
    # Update frame and margins
    componentframe = pointscommandement.by_member("ComponentFrame").v
    componentframe.add('MagnifiableOffset = [0.0, 0.0]')
    pointscommandement.by_member("FirstMargin").v = "TRTTILength(Magnifiable = 72.0)"
    pointscommandement.by_member("BorderLineColorToken").v = '"M81_ArtichokeVeryLight"'
    
    # Update elements
    _update_command_points_elements(pointscommandement.by_member("Elements").v)
    
    # Add background
    pointscommandement.add(_get_command_points_background())
    
    logger.debug("Updated command points display properties")


def _update_command_points_elements(elements: Any) -> None:
    """Update command points element properties."""
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type == "BUCKTextureDescriptor":  # noqa
            _update_command_points_texture(component_descr)
        elif component_descr.type == "BUCKTextDescriptor":  # noqa
            _update_command_points_text(component_descr)


def _update_command_points_texture(component: Any) -> None:
    """Update command points texture properties."""
    if component.by_member("ElementName", False) is None:
        return
        
    if component.by_member("ElementName").v == '"CommandPoints"':
        componentframe = component.by_member("ComponentFrame").v
        componentframe.by_member("AlignementToAnchor").v = "[4.0, 0.5]"


def _update_command_points_text(component: Any) -> None:
    """Update command points text properties."""
    if component.by_member("UniqueName", False) is None:
        return
        
    uniquename = component.by_member("UniqueName").v
    if uniquename == '"CommmandPointsText"':
        component.by_member("HorizontalFitStyle").v = "~/FitStyle/UserDefined"
    elif uniquename == '"CommmandPointsIncomeText"':
        componentframe = component.by_member("ComponentFrame").v
        componentframe.by_member("AlignementToAnchor").v = "[-0.25, 0.5]"


def _get_command_points_background() -> str:
    """Get command points background template."""
    return '''\
BackgroundComponents = [
    PanelRoundedCorner
    (
        BackgroundBlockColorToken = "M81_Quincy"
        BorderLineColorToken = "M81_ArtichokeVeryLight"
    )
]'''


def _update_command_points_timer(source_path) -> None:
    """Update command points timer properties."""
    chronopointcommandement = source_path.by_namespace("ChronoPointCommandement").v
    chronopointcommandement.by_member("BorderLineColorToken").v = '"M81_ArtichokeVeryLight"'
    chronopointcommandement.add(_get_command_points_background())
    logger.debug("Updated command points timer properties")


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
