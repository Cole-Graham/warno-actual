"""Functions for modifying unit cover behavior."""

from typing import Any, Dict

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_auto_cover(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Edit auto cover ranges in UniteDescriptor.ndf.
    
    Args:
        source_path: The NDF file to edit
        game_db: Game database containing unit data
    """
    logger.info("Modifying auto cover ranges")
    unit_db = game_db.get("units", {})
    
    for unit_descr in source_path:
        if not hasattr(unit_descr, 'namespace'):
            continue
            
        # Get unit name without prefix
        unit_name = unit_descr.namespace.replace("Descriptor_Unit_", "")
        
        # Skip if unit not in database
        if unit_name not in unit_db:
            continue
            
        unit_data = unit_db[unit_name]
        tags = unit_data.get("tags", [])
        
        # Check if unit is infantry or ground unit
        if 'Infanterie' in tags or 'GroundUnits' in tags:
            modules_list = unit_descr.v.by_m("ModulesDescriptors").v
            
            # Find and update auto cover module
            for module in modules_list:
                if not hasattr(module.v, 'type'):
                    continue
                    
                if module.v.type == "TAutoCoverModuleDescriptor":
                    module.v.by_m("AutoCoverRangeGRU").v = "70"
                    logger.info(f"Set auto cover range to 70m for {unit_name}")
                    break 