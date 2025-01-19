"""Functions for modifying UI HUD unit label aggregation view."""
from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_uispecificunitlabelaggregationview(source_path) -> None:
    """Edit UISpecificUnitLabelAggregationView.ndf.
    
    Args:
        source: NDF file containing HUD unit label aggregation view definitions
    """
    logger.info("Editing UISpecificUnitLabelAggregationView.ndf")
    
    # Update player name component
    unitlabelunitplayernamebuckcomponent = source_path.by_namespace("UnitLabelUnitPlayerNameBUCKComponent").v
    unitlabelunitplayernamebuckcomponent.by_member("VerticalFitStyle").v = "~/FitStyle/FitToParent"
    logger.debug("Updated player name component fit style") 