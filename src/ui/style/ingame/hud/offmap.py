"""Functions for modifying UI HUD offmap view."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecificoffmapview(source_path) -> None:
    """Edit UISpecificOffMapView.ndf.
    
    Args:
        source_path: NDF file containing HUD offmap view definitions
    """
    logger.info("Editing UISpecificOffMapView.ndf")
    
    # Update main component
    maincomponent = source_path.by_namespace("BUCKSpecificOffMapMainComponentDescriptor").v
    _add_background_properties(maincomponent)
    
    # Update components
    _update_components(maincomponent.by_member("Components").v)


def _add_background_properties(component: Any) -> None:
    """Add background properties to component."""
    component.insert(4, 'HasBackground = true')
    component.insert(5, 'BackgroundBlockColorToken = "DarkerGray30"')
    component.insert(6, 'HasBorder = true')
    component.insert(7, 'BorderThicknessToken = "2"')
    component.insert(8, 'BorderLineColorToken = "Gray"')
    logger.debug("Added background properties")


def _update_components(components: Any) -> None:
    """Update component properties."""
    for component in components:
        if not isinstance(component.v, ndf.model.Object):
            continue
        if is_obj_type(component.v, "PanelRoundedCorner"):
            components.remove(component)
            # _update_panel_properties(component.v)
        elif is_obj_type(component.v, "BUCKListDescriptor"):
            _update_list_elements(component.v.by_member("Elements").v)


def _update_panel_properties(panel: Any) -> None:
    """Update panel properties."""
    panel.add('HasBackground = true')
    panel.add('BackgroundBlockColorToken = "DarkerGray30"')
    panel.add('HasBorder = true')
    panel.add('BorderThicknessToken = "1"')
    panel.add('BorderLineColorToken = "Gray"')
    logger.debug("Updated panel properties")


def _update_list_elements(elements: Any) -> None:
    """Update list element properties."""
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if component_descr.type == "BUCKTextDescriptor":  # noqa
            component_descr.by_member("TextColor").v = '"M81_P3AmberOrange"'  # noqa
        elif component_descr.type == "BUCKContainerDescriptor":  # noqa
            _update_container(component_descr)


def _update_container(container: Any) -> None:
    """Update container properties."""
    componentframe = container.by_member("ComponentFrame").v
    componentframe.by_member("MagnifiableWidthHeight").v = "[0.0, 260.0]"
    
    for component in container.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKGridDescriptor"):
            continue
            
        component.v.by_member("FirstElementMargin").v = "TRTTILength2(Magnifiable = [10.0, 10.0])"
        component.v.by_member("InterElementMargin").v = "TRTTILength2(Magnifiable = [5.0, 14.0])"
    
    logger.debug("Updated container properties")
