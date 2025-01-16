"""Common FOB building modifications."""

from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_fob_minimap(source) -> None:
    """Add minimap texture module to FOB."""
    logger.info("Adding FOB minimap texture")
    
    for fob_descr in source:
        modules_list = fob_descr.v.by_m("ModulesDescriptors").v
        insert_index = -1
        
        # Find insertion point after production module
        for i, module in enumerate(modules_list):
            if not isinstance(module.v, ndf.model.Object):
                continue
            if module.v.type == "TProductionModuleDescriptor":
                insert_index = i
                break
                
        if insert_index >= 0:
            minimap_module = (
                'TMinimapDisplayModuleDescriptor'
                '('
                '    Texture = "Texture_Minimap_Unit_fob"'
                '    FollowUnitOrientation = False'
                ')'
            )
            modules_list.insert(insert_index, minimap_module)
            logger.info("Added FOB minimap texture module") 