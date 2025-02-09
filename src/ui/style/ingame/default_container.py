"""Functions for modifying UI default container."""
from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_uiingamedefaultcontainer(source_path) -> None:
    """Edit UIInGameDefaultContainer.ndf."""
    logger.info("Editing UIInGameDefaultContainer.ndf")
    
    # Update panel properties
    panelroundedcorner_template = source_path.by_namespace("PanelRoundedCorner").v
    panelroundedcorner_template.params.by_param("BackgroundBlockColorToken").v = '"M81_DarkCharcoalTransparent"'
    panelroundedcorner_template.params.by_param("BorderLineColorToken").v = '"M81_DarkCharcoalSelection"'
    panelroundedcorner_template.params.by_param("Radius").v = "4"
    panelroundedcorner_template.params.by_param("RoundedVertexes").v = "[true, true, true, true]"
    
    logger.debug("Updated panel properties") 