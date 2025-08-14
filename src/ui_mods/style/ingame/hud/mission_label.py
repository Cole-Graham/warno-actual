"""Functions for modifying UI HUD player mission label."""
# from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_uispecificingameplayermissionlabelresources(source_path) -> None:
    """Edit UISpecificInGamePlayerMissionLabelResources.ndf."""
    logger.info("Editing UISpecificInGamePlayerMissionLabelResources.ndf")
    
    # Update mission label properties
    playermissionlabeldescriptor_template = source_path.by_namespace("PlayerMissionLabelDescriptor").v
    playermissionlabeldescriptor_template.params.add('Margin : float = 3.0')
    playermissionlabeldescriptor_template.params.add('Largeur : float = 70.0')
    logger.debug("Updated mission label dimensions")
