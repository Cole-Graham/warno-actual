"""Functions for modifying UI HUD unit label multiselection view."""
from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecificunitlabelmultiselectionview(source_path) -> None:
    """Edit UISpecificUnitLabelMultiSelectionView.ndf.
    
    Args:
        source_path: NDF file containing HUD unit label multiselection view definitions
    """
    logger.info("Editing UISpecificUnitLabelMultiSelectionView.ndf")
    
    # Update unit label component
    _update_unit_label_component(source_path)


def _update_unit_label_component(source_path) -> None:
    """Update unit label component properties."""
    unitlabelunitbuckcomponentdescriptorformultiselection = source_path.by_namespace("UnitLabelUnitBUCKComponentDescriptorForMultiSelection").v
    
    for component in unitlabelunitbuckcomponentdescriptorformultiselection.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKContainerDescriptor"):
            continue
            
        _update_container_components(component.v.by_member("Components").v)
    
    logger.debug("Updated unit label component properties")


def _update_container_components(components: Any) -> None:
    """Update container component properties."""
    for component in components:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "BUCKSensibleAreaDescriptor"):
            continue
            
        _update_sensible_area_components(component.v.by_member("Components").v)


def _update_sensible_area_components(components: Any) -> None:
    """Update sensible area component properties."""
    for component in components:
        if not isinstance(component.v, ndf.model.Object) or not is_obj_type(component.v, "PanelRoundedCorner"):
            continue
            
        component.v.by_member("Radius").v = "4"
        component.v.by_member("BackgroundBlockColorToken").v = '"BoutonTemps_ROE_M81"'
        component.v.by_member("BorderLineColorToken").v = '"BoutonTemps_ROE_Border_M81"'
    
    logger.debug("Updated panel properties")
