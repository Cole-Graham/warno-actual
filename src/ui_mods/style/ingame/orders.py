"""Functions for modifying UI order display."""
from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_orderdisplay(source_path) -> None:
    """Edit OrderDisplay.ndf.
    
    Args:
        source_path: NDF file containing order display definitions
    """
    logger.info("Editing OrderDisplay.ndf")
    
    # Update order display line thickness
    for row in source_path:
        if not isinstance(row.v, ndf.model.Object):
            continue
            
        if not is_obj_type(row.v, "TOrderDisplayDrawInfo"):
            continue
            
        row.v.by_member("LineThickness").v = "1400.0"
        logger.debug("Updated order display line thickness")
