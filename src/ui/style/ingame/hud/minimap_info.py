"""Functions for modifying UI HUD minimap info view."""
from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_uispecificminimapinfoview(source_path) -> None:
    """Edit UISpecificMiniMapInfoView.ndf."""
    logger.info("Editing UISpecificMiniMapInfoView.ndf")
    
    # Update minimap size
    source_path.by_namespace("MinimapMagnifiableSize").v = "380.0"
    logger.debug("Updated minimap size") 