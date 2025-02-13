"""Functions for modifying UI background templates."""
from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_buckspecificbackgrounds(source_path) -> None:
    """Edit BuckSpecificBackgrounds.ndf.
    
    Args:
        source_path: NDF file containing background template definitions
    """
    logger.info("Editing BuckSpecificBackgrounds.ndf")
    
    # Update HUD background parallelogram
    hud_backgroundparallelogram = source_path.by_namespace("HUDBackgroundParallelogram").v
    hud_backgroundparallelogram.params.by_param("HidePointerEvents").v = "true"
    logger.debug("Updated HUDBackgroundParallelogram pointer events")
