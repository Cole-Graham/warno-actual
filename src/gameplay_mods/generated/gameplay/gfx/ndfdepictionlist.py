"""Functions for modifying NdfDepictionList.ndf"""

from typing import Any
from src.constants.new_units import NEW_DEPICTIONS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_namespace

logger = setup_logger(__name__)

def edit_gen_gp_gfx_ndfdepictionlist(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/NdfDepictionList.ndf"""
    
    generateddepictionndffiles = find_obj_by_namespace(source_path, "GeneratedDepictionNdfFiles")
    _handle_new_units(generateddepictionndffiles)
    
    
def _handle_new_units(generateddepictionndffiles: Any) -> None:
    """Handle new units for NdfDepictionList.ndf"""
    
    logger.info("Creating NdfDepictionList entries")
    
    for unit_descr_name, unit_data in NEW_DEPICTIONS.items():
        unit_name = unit_data["unit_name"]
        target_dir_name = unit_data.get(f"{unit_name}_ndf", {}).get("directory", None)
        if target_dir_name is None:
            continue
        directory = f'"GameData:/Gameplay/Gfx/DepictionResources/{target_dir_name}/{unit_name}.ndf"'
        generateddepictionndffiles.v.add(directory)