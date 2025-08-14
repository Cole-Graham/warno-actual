"""Functions for modifying DepictionAlternatives.ndf"""

from typing import Any
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_gen_gp_gfx_depictionalternatives(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionAlternatives.ndf"""
    
    _handle_new_units(source_path)
    
    
def _handle_new_units(source_path: Any) -> None:
    """Handle new units for DepictionAlternatives.ndf"""
    
    logger.info("Creating alternatives depiction entries")
    
    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if not edits.get("is_ground_vehicle", False):
            continue

        unit_name = edits["NewName"]

        # Create alternatives entry using donor's models
        entry = (
            f"Alternatives_{unit_name} is ["
            f"    DepictionVisual_LOD_High( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor_name} ),"
            f"    DepictionVisual_LOD_Mid( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor_name}_MID ),"
            f"    DepictionVisual_LOD_Low( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor_name}_LOW ),"
            f"]"
        )
        source_path.add(entry)
        logger.info(f"Added alternatives depiction for {unit_name}")