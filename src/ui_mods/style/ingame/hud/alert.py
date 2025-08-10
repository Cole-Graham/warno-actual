"""Functions for modifying UI HUD alert panel."""
from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_uispecifichudalertpanelview(source_path) -> None:
    """Edit UISpecificHUDAlertPanelView.ndf.
    
    Args:
        source_path: NDF file containing HUD alert panel definitions
    """
    logger.info("Editing UISpecificHUDAlertPanelView.ndf")
    
    # Update alert line gradient
    alertline = source_path.by_namespace("AlertLine").v
    for component in alertline.by_member("Components").v:
        if not isinstance(component.v, ndf.model.Object):
            continue
            
        if is_obj_type(component.v, "BUCKGradientDescriptor"):
            component.v.by_member("TransitionColor1").v = '"AlertPanel/Gradient1_M81"'
            logger.debug("Updated alert line gradient color")
