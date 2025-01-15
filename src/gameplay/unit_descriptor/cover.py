"""Functions for modifying unit cover behavior."""

from typing import Any, List

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ndf

logger = setup_logger(__name__)


def _get_unit_tags(tags_input: Any) -> List[str]:
    """Convert tags input into list of tag strings.
    
    Args:
        tags_input: Either a string to parse or an ndf List object
    """
    # If input is already a List, use it directly
    if isinstance(tags_input, ndf.model.List):
        tags = tags_input
    else:
        # Otherwise parse the string input
        tags = ndf.convert(str(tags_input).encode('utf-8'))[0].v
    
    return [tag.v.strip("'") for tag in tags]


def edit_auto_cover(source) -> None:
    """Edit auto cover ranges in UniteDescriptor.ndf."""
    logger.info("Modifying auto cover ranges")
    
    for unit_descr in source:
        modules_list = unit_descr.v.by_m("ModulesDescriptors").v
        is_infantry = False
        is_ground_unit = False
        
        for module in modules_list:
            if not hasattr(module.v, 'type'):
                continue
                
            module_type = module.v.type
            
            # Check unit tags
            if module_type == "TTagsModuleDescriptor":
                tags = _get_unit_tags(module.v.by_m("TagSet").v)
                is_infantry = 'Infanterie' in tags
                is_ground_unit = 'GroundUnits' in tags
                
            # Update auto cover range
            if module_type == "TAutoCoverModuleDescriptor":
                if is_infantry or is_ground_unit:
                    module.v.by_m("AutoCoverRangeGRU").v = "70"
                    logger.info(f"Set auto cover range to 70m for {unit_descr.namespace}")
                    break 