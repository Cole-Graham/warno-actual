"""Functions for modifying UI HUD score view."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def edit_uispecifichudscoreview(source_path) -> None:
    """Edit UISpecificHUDScoreView.ndf."""
    logger.info("Editing UISpecificHUDScoreView.ndf")
    
    # Update score view properties
    scorepanelviewdescriptor = source_path.by_namespace("ScorePanelViewDescriptor").v
    
    # Update alliance score line
    _update_alliance_score_line(source_path)
    
    # Update player score components
    _update_player_score_components(source_path)
    
    # Update player score panel button
    _update_player_score_panel_button(source_path)

def _update_alliance_score_line(source_path: ndf.NdfBinary) -> None:
    """Update alliance score line properties."""
    alliancescoreline_template = source_path.by_namespace("AllianceScoreLine").v
    
    for component in alliancescoreline_template.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKListDescriptor"):
            continue
            
        _process_score_elements(component.v.by_member("Elements").v)
    
    logger.debug("Updated alliance score line properties")

def _process_score_elements(elements: Any) -> None:
    """Process score elements to update properties."""
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type != "BUCKContainerDescriptor":
            continue
            
        _update_score_container(component_descr)

def _update_score_container(container: Any) -> None:
    """Update score container properties."""
    if container.by_member("ElementName", False) is not None:
        elementname = container.by_member("ElementName").v
        if elementname == '<ElementName> + "PreGaugeContainer"':
            _update_gauge_container(container)
    else:
        _update_nested_components(container.by_member("Components").v)

def _update_gauge_container(container: Any) -> None:
    """Update gauge container properties."""
    container.by_member("BackgroundBlockColorToken").v = '"PanelScore/ScoreBackgroundM81"'
    container.add("HasBorder = true")
    container.add('BorderLineColorToken = "M81_ArtichokeVeryLight"')
    
    for component in container.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKTextureDescriptor"):
            continue
            
        component.v.by_member("TextureColorToken").v = '"M81_WhiteText95"'

def _update_nested_components(components: Any) -> None:
    """Update nested component properties."""
    for component in components:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if is_obj_type(component.v, "BUCKGaugeDescriptor"):
            _update_gauge_descriptor(component.v)
        elif is_obj_type(component.v, "BUCKListDescriptor"):
            _update_text_elements(component.v.by_member("Elements").v)

def _update_gauge_descriptor(gauge: Any) -> None:
    """Update gauge descriptor properties."""
    if gauge.by_member("ElementName").v == '<ElementName> + "Gauge"':
        gauge.by_member("BackgroundBlockColorToken").v = '"PanelScore/ScoreBackgroundM81"'
        gauge.add("HasBorder = true")
        gauge.add('BorderLineColorToken = "M81_ArtichokeVeryLight"')

def _update_text_elements(elements: Any) -> None:
    """Update text element properties."""
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type != "BUCKTextDescriptor":
            continue
            
        elementname = component_descr.by_member("ElementName").v
        if elementname in ['<ElementName> + "Text"', '<ElementName> + "IncomeText"', '<ElementName> + "VictoryTimer"']:
            component_descr.by_member("TextColor").v = '"M81_WhiteText95"'

def _update_player_score_components(source_path: ndf.NdfBinary) -> None:
    """Update player score component properties."""
    buckspecifichudscoreplayeroneline = source_path.by_namespace("BUCKSpecificHUDScorePlayerOneLine").v
    
    for element in buckspecifichudscoreplayeroneline.by_member("Elements").v:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        _update_player_score_component(element.v.by_member("ComponentDescriptor").v)

def _update_player_score_component(component: Any) -> None:
    """Update player score component properties."""
    if component.type == "BUCKSpecificTextWithHint":
        component.by_member("TextColor").v = '"BlancEquipe"'
        component.by_member("TypefaceToken").v = '"Bombardier"'
    elif component.type == "BUCKTextDescriptor" and component.by_member("ElementName", False) is not None:
        if component.by_member("ElementName").v == '"Points"':
            component.by_member("TextColor").v = '"M81_ArtichokeVeryLight"'
    elif component.type == "BUCKButtonDescriptor":
        for nested in component.by_member("Components").v:
            if not isinstance(nested.v, ndf.model.Object) or not is_obj_type(nested.v, "BUCKTextureDescriptor"):
                continue
                
            nested.v.by_member("TextureColorToken").v = '"CouleurTexture_boutonShortcutsTextM81"'

def _update_player_score_panel_button(source_path: ndf.NdfBinary) -> None:
    """Update player score panel button properties."""
    playerscorepanelbutton = source_path.by_namespace("PlayerScorePanelButton").v
    
    for component in playerscorepanelbutton.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKButtonDescriptor"):
            continue
            
        _update_button_properties(component.v)

def _update_button_properties(button: Any) -> None:
    """Update button properties."""
    button.by_member("DefaultToggleValue").v = "true"
    
    for component in button.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if is_obj_type(component.v, "BUCKContainerDescriptor"):
            _update_button_container(component.v)
        elif is_obj_type(component.v, "BUCKTextureDescriptor"):
            component.v.by_member("TextureColorToken").v = '"CouleurTexture_boutonShortcutsTextM81"'

def _update_button_container(container: Any) -> None:
    """Update button container properties."""
    for component in container.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        component.v.by_member("BackgroundBlockColorToken").v = '"BoutonTemps_BackgroundM81"'
        component.v.by_member("BorderLineColorToken").v = '"CouleurBordure_boutonShortcutsTextM81"' 