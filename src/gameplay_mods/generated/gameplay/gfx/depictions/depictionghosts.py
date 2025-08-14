"""Functions for modifying DepictionGhosts.ndf"""

from typing import Any
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_gp_gfx_depictionghosts(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionGhosts.ndf"""
    
    _handle_new_units(source_path)
    
    
def _handle_new_units(source_path: Any) -> None:
    """Handle new units for DepictionGhosts.ndf"""
    
    logger.info("Creating ghost depiction entries")

    for donor, edits in NEW_UNITS.items():
        if not edits.get("is_ground_vehicle", False):
            continue

        unit_name = edits["NewName"]

        # Create ghost depiction entry
        entry = (
            f"GhostDepiction_{unit_name} is GhostVehicleDepictionDesc"
            f"("
            f"    Alternatives = Alternatives_{unit_name}"
            f"    Selector = SpecificVehicleDepictionSelector"
            f")"
        )
        source_path.add(entry)
        logger.info(f"Added ghost depiction for {unit_name}")