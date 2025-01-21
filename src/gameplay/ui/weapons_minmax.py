"""Functions for editing weapon min/max values."""
from typing import Any

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_weaponsminmax(source: Any) -> None:
    """Edit WeaponsMinMax.ndf to adjust UI scaling values."""
    logger.info("Editing weapons min/max values")
    
    root_obj = source.by_n("MinMaxValuesInterfaceHelper").v
    weapons_map = root_obj.by_m("WeaponsMinMaxValues").v
    minmax_atgm = weapons_map.by_key("~/MinMax_ATGM").v
    
    for min_max_param_obj in minmax_atgm:
        if min_max_param_obj.namespace == "Penetration":
            min_max_param_obj.v.by_m("Min").v = "10"
            logger.debug("Changed ATGM UI color scaling minimum to 10 AP")
            break 