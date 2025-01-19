"""Functions for modifying UI replay resources."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def edit_uiingamehudreplayresource(source_path) -> None:
    """Edit UIInGameHUDReplayResource.ndf.
    
    Args:
        source: NDF file containing replay resource definitions
    """
    logger.info("Editing UIInGameHUDReplayResource.ndf")
    
    replaypanel = source_path.by_namespace("ReplayPanel").v
    
    # Update background components
    _update_background_components(replaypanel.by_member("BackgroundComponents").v)
    
    # Update panel elements
    _update_panel_elements(replaypanel.by_member("Elements").v)

def _update_background_components(background_components: Any) -> None:
    """Update background component properties."""
    for component in background_components:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        component.v.by_member("BackgroundBlockColorToken").v = '"M81_DarkCharcoalTransparent"'
        component.v.by_member("BorderLineColorToken").v = '"M81_DarkCharcoalSelection"'
    
    logger.debug("Updated background component colors")

def _update_panel_elements(elements: Any) -> None:
    """Update panel element properties."""
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type != "BUCKListDescriptor":
            continue
            
        elementname = component_descr.by_member("ElementName").v
        if elementname == '"ReplayPanelSliderHorizontalList"':
            _update_slider_components(component_descr.by_member("Elements").v)
        elif elementname == '"ReplayPanelMainButtonsContainerList"':
            _update_button_components(component_descr.by_member("Elements").v)

def _update_slider_components(elements: Any) -> None:
    """Update slider component properties."""
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type != "BUCKContainerDescriptor":
            continue
            
        for component in component_descr.by_member("Components").v:
            if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKGaugeDescriptor"):
                continue
                
            component.v.by_member("BorderLineColorToken").v = '"M81_DarkCharcoalSelection"'
    
    logger.debug("Updated slider component colors")

def _update_button_components(elements: Any) -> None:
    """Update button component properties."""
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if not isinstance(component_descr, ndf.model.Object) or component_descr.type != "BUCKContainerDescriptor":
            continue
            
        for component in component_descr.by_member("Components").v:
            if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKTextDescriptor"):
                continue
                
            component.v.by_member("TextColor").v = '"M81_ArtichokeVeryLight"'
    
    logger.debug("Updated button text colors") 