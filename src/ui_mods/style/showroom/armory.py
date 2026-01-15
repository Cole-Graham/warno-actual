"""Functions for modifying showroom armory component."""
# from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_uispecificshowroomarmorycomponent(source_path) -> None:
    """Edit UISpecificShowroomArmoryComponent.ndf.
    
    Args:
        source_path: NDF file containing showroom armory component definitions
    """
    logger.info("Editing UISpecificShowroomArmoryComponent.ndf")
    
    # Update max units
    source_path.by_namespace("MaxUnitsInDeckPerCategory").v = "11"
    logger.debug("Updated max units in deck per category")
    
    armory_component = source_path.by_namespace("ArmoryComponentDescriptor")
    unit_pack_descriptor = armory_component.v.by_member("UnitPackDescriptor")
    unit_pack_descriptor.v.by_member("FirstMargin").v = "TRTTILength(Magnifiable = 9.0)"
    unit_pack_descriptor.v.by_member("LastMargin").v = "TRTTILength(Magnifiable = 10.0)"
    logger.debug("Updated armory component margins")
