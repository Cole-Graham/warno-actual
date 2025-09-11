"""Functions for modifying MimeticGhosts.ndf"""

from typing import Any
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_type

logger = setup_logger(__name__)

def edit_gen_gp_gfx_mimeticghosts(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/MimeticGhosts.ndf"""
    
    mimeticghostregistration_descr = find_obj_by_type(source_path, "TMimeticGhostRegistration")
    mimeticghost_map = mimeticghostregistration_descr.v.by_m("MimeticGhost")
    _handle_new_units(source_path, mimeticghost_map)
    

def _handle_new_units(source_path: Any, mimeticghost_map: Any) -> None:
    """Handle new units for MimeticGhosts.ndf"""
    
    logger.info("Creating mimetic ghost entries")
    
    for donor, edits in NEW_UNITS.items():
        if not edits.get("is_ground_vehicle", False) and not edits.get("is_aerial", False):
            continue
            
        unit_name = edits["NewName"]
        new_entry = f"('{unit_name}', GhostDepiction_{unit_name})"
        mimeticghost_map.v.add(new_entry)
        logger.info(f"Added mimetic ghost for {unit_name}")