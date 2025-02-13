"""Functions for modifying UI HUD multiselection panel."""
from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecifichudmultiselectionpanelview(source_path) -> None:
    """Edit UISpecificHUDMultiSelectionPanelView.ndf.
    
    Args:
        source_path: NDF file containing HUD multiselection panel definitions
    """
    logger.info("Editing UISpecificHUDMultiSelectionPanelView.ndf")
    
    # Update horizontal list properties
    _update_horizontal_list(source_path)
    
    # Update main component properties
    _update_main_component(source_path)


def _update_horizontal_list(source_path) -> None:
    """Update horizontal list properties."""
    hudmultiselectionhorizontallistdescriptor = source_path.by_namespace("HUDMultiSelectionHorizontalListDescriptor").v
    hudmultiselectionhorizontallistdescriptor.by_member("BackgroundBlockColorToken").v = '"M81_Ebony"'
    logger.debug("Updated horizontal list background color")


def _update_main_component(source_path) -> None:
    """Update main component properties."""
    maincomponent = source_path.by_namespace("BUCKSpecificHUDMultiSelectionPanelMainComponentDescriptor").v
    
    for component in maincomponent.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if is_obj_type(component.v, "BUCKSpecificScrollingContainerDescriptor"):
            component.v.by_member("ScrollBarBackgroundToken").v = '"M81_Artichoke64"'
            component.v.by_member("ScrollBarElevatorBackgroundToken").v = '"M81_Quincy"'
            logger.debug("Updated scrollbar colors")
