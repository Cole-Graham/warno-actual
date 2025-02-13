"""Functions for modifying UI HUD unit label view name only."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecificunitlabelviewnameonly(source_path) -> None:
    """Edit UISpecificUnitLabelViewNameOnly.ndf.
    
    Args:
        source_path: NDF file containing HUD unit label view name only definitions
    """
    logger.info("Editing UISpecificUnitLabelViewNameOnly.ndf")
    
    # Update unit name and right list
    _update_unit_name_and_right_list(source_path)
    
    # Update upper label
    _update_upper_label(source_path)


def _update_unit_name_and_right_list(source_path) -> None:
    """Update unit name and right list properties."""
    unitnameandrightlistnameonly = source_path.by_namespace("UnitNameAndRightListNameOnly").v
    
    # Update frame and style
    componentframe = unitnameandrightlistnameonly.by_member("ComponentFrame").v
    componentframe.add('MagnifiableOffset = [0.0, ~/ReticleMagnifiableSize * -5.5]')
    unitnameandrightlistnameonly.by_member("FitStyle").v = "~/ContainerFitStyle/MaxBetweenUserDefinedAndContent"
    
    # Update render layers
    unitnameandrightlistnameonly.insert(3, 'BorderLocalRenderLayer = 4')
    unitnameandrightlistnameonly.insert(4, 'BackgroundLocalRenderLayer = 4')
    
    # Update components
    _update_list_components(unitnameandrightlistnameonly.by_member("Components").v)
    
    logger.debug("Updated unit name and right list properties")


def _update_list_components(components: Any) -> None:
    """Update list component properties."""
    for component in components:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if is_obj_type(component.v, "CurrentUnitLabelUpperList"):
            _update_current_unit_label(component.v)
        elif is_obj_type(component.v, "BUCKListDescriptor"):
            componentframe = component.v.by_member("ComponentFrame").v
            componentframe.add('MagnifiableOffset = [0.0, ~/ReticleMagnifiableSize * -5.5]')


def _update_current_unit_label(component: Any) -> None:
    """Update current unit label properties."""
    component_frame = '''\
ComponentFrame = TUIFramePropertyRTTI
(
    MagnifiableOffset = [0.0, ~/ReticleMagnifiableSize * -5.5]
    AlignementToFather = [0.5, 0.0]
    AlignementToAnchor = [0.5, 0.0]
)'''
    component.replace(0, component_frame)


def _update_upper_label(source_path) -> None:
    """Update upper label properties."""
    upperlabelnameonly = source_path.by_namespace("UpperLabelNameOnly").v
    
    # Update frame
    componentframe = upperlabelnameonly.by_member("ComponentFrame").v
    componentframe.by_member("MagnifiableOffset").v = "[0.0, ~/ReticleMagnifiableSize * -5.5]"
    componentframe.by_member("AlignementToAnchor").v = "[0.5, 0.0]"
    
    # Update elements
    _update_upper_label_elements(upperlabelnameonly.by_member("Elements").v)
    
    logger.debug("Updated upper label properties")


def _update_upper_label_elements(elements: Any) -> None:
    """Update upper label element properties."""
    for element in elements:
        if not isinstance(element.v, ndf.model.Object) or not is_obj_type(element.v, "BUCKListElementDescriptor"):
            continue
            
        component_descr = element.v.by_member("ComponentDescriptor").v
        if not isinstance(component_descr, ndf.model.Object):
            continue
            
        if component_descr.type == "TMoraleGaugeDescriptor":
            component_descr.by_member("AlignementToAnchor").v = "[0.5, 1.0]"
        elif component_descr.type == "CarriedUnitNameList":
            _add_carried_unit_frame(component_descr)
    
    # Add unit label icon
    new_entry = '''\
BUCKListElementDescriptor
(
    ComponentDescriptor = ~/UnitLabelUnitIconNameOnly
)'''
    elements.insert(2, new_entry)


def _add_carried_unit_frame(component: Any) -> None:
    """Add carried unit frame properties."""
    component_frame = '''\
ComponentFrame = TUIFramePropertyRTTI
(
    MagnifiableOffset = [0.0, ~/ReticleMagnifiableSize * -11.0]
    AlignementToFather = [0.5, 0.0]
    AlignementToAnchor = [0.5, 0.0]
)'''
    component.add(component_frame)
