"""Functions for modifying UI HUD idle unit view."""
from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_uispecificingameidleunitview(source_path) -> None:
    """Edit UISpecificInGameIdleUnitView.ndf.
    
    Args:
        source: NDF file containing HUD idle unit view definitions
    """
    logger.info("Editing UISpecificInGameIdleUnitView.ndf")
    
    # Update idle unit button
    idleunitbutton = source_path.by_namespace("IdleUnitButton").v
    idleunitbutton.insert(6, 'BorderLineColorToken = "DeploymentPhase/IdleUnitM81"')
    idleunitbutton.insert(7, 'ExternalBorderLineColorToken = "DeploymentPhase/IdleUnitM81"')
    idleunitbutton.insert(8, 'PanelRoundedCorner_BorderLineColorToken = "DeploymentPhase/IdleUnitM81"')
    logger.debug("Updated idle unit button borders")
    
    # Update idle unit number text
    idleunitnumbertext = source_path.by_namespace("IdleUnitNumberText").v
    idleunitnumbertext.by_member("TextColor").v = '"DeploymentPhase/IdleUnitM81"'
    logger.debug("Updated idle unit number text color") 