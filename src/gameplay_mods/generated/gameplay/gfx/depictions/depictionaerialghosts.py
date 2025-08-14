"""Functions for modifying DepictionAerialGhosts.ndf"""

from typing import Any
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_gen_gp_gfx_depictionaerialghosts(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialGhosts.ndf"""
    
    _handle_new_units(source_path)
    
    
def _handle_new_units(source_path: Any) -> None:
    """Handle new units for DepictionAerialGhosts.ndf"""
    
    for donor, edits in NEW_UNITS.items():
        if edits.get("is_aerial", False):
            unit_name = edits["NewName"]
            new_object_entry = (
                f"GhostDepiction_{unit_name} is GhostAerialDepictionDesc\n"
                f"(\n"
                f"    Alternatives = Alternatives_{unit_name}\n"
                f"    Selector = SpecificAirplaneDepictionSelector\n"
                f")"
            )
            source_path.add(new_object_entry)
            logger.info(f"Added aerial ghost depiction for {unit_name}")