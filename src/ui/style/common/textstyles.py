"""Functions for modifying UI text styles."""
from src.utils.logging_utils import setup_logger
# from src import ndf
# from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_textstyles(source_path) -> None:
    """Edit TextStyles.ndf.
    
    Args:
        source_path: NDF file containing text style definitions
    """
    logger.info("Editing TextStyles.ndf")

    for row in source_path:
        if row.namespace == "TextStyleActivationPointTemp":
            new_entry = row.copy()
            new_entry.namespace = "TextStyleActivationPointTemp_M81"
            new_entry.v.by_m("ColorBottom").v = "M81_EbonyLight"
            new_entry.v.by_m("ColorUp").v = "M81_EbonyLight"
            source_path.insert(row.index, new_entry)
            logger.debug("Updated TextStyleActivationPointTemp text style")
            
            break
