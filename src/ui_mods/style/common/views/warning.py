"""Functions for modifying UI warning panel."""
# from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_uiwarningpanel(source_path) -> None:
    """Edit UIWarningPanel.ndf.
    
    Args:
        source_path: NDF file containing warning panel definitions
    """
    logger.info("Editing UIWarningPanel.ndf")
    
    # Update warning standard component colors
    warningstandard_template = source_path.by_namespace("WarningStandardComponent").v
    warningstandard_template.params.by_param("BackgroundBlockColorToken").v = '"M81_ArtichokeTransparent"'
    warningstandard_template.params.by_param("BorderLineColorToken").v = '"M81_DarkCharcoalTransparent"'
    logger.debug("Updated warning panel colors")
