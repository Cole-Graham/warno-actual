"""Functions for modifying showroom armory component."""
from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_uispecificshowroomarmorycomponent(source_path) -> None:
    """Edit UISpecificShowroomArmoryComponent.ndf.
    
    Args:
        source: NDF file containing showroom armory component definitions
    """
    logger.info("Editing UISpecificShowroomArmoryComponent.ndf")
    
    # Update max units
    source_path.by_namespace("MaxUnitsInDeckPerCategory").v = "11"
    logger.debug("Updated max units in deck per category") 