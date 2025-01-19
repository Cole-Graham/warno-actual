"""Functions for modifying UI minimap."""
from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_uiingameminimap(source_path) -> None:
    """Edit UIInGameMinimap.ndf.
    
    Args:
        source: NDF file containing minimap definitions
    """
    logger.info("Editing UIInGameMinimap.ndf")
    
    # Update minimap properties
    ingameminimap = source_path.by_namespace("InGameMinimap").v
    ingameminimap.by_member("CameraTrapezoidOriginColor").v = "RGBA[255, 255, 255, 45]"
    logger.debug("Updated minimap camera trapezoid color") 