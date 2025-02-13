"""Functions for modifying UI chat view."""
# from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_uispecificchatview(source_path) -> None:
    """Edit UISpecificChatView.ndf.
    
    Args:
        source_path: NDF file containing chat view definitions
    """
    logger.info("Editing UISpecificChatView.ndf")
    
    # Update chat component position
    maincomponent_descr_template = source_path.by_namespace("BUCKSpecificGameChatMainComponentDescriptor").v
    component_frame = maincomponent_descr_template.by_member("ComponentFrame").v
    component_frame.by_member("MagnifiableOffset").v = "[10.0, -310.0]"
    logger.debug("Updated chat component position")
