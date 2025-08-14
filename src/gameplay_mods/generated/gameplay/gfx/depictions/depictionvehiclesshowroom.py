"""Functions for modifying DepictionVehiclesShowRoom.ndf"""

from typing import Any
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_gp_gfx_depictionvehiclesshowroom(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionVehiclesShowRoom.ndf"""
    
    _handle_new_units(source_path)

    
def _handle_new_units(source_path: Any) -> None:
    """Handle new units for DepictionVehiclesShowRoom.ndf"""
    
    logger.info("Creating vehicle showroom depiction entries")

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if edits.get("is_ground_vehicle", False):
            unit_name = edits["NewName"]
            new_depiction_obj = source_path.by_namespace(f"Gfx_{donor_name}_Showroom").copy()
            new_depiction_obj.namespace = f"Gfx_{unit_name}_Showroom"
            new_depiction_obj.v.by_member("Alternatives").v = f"Alternatives_{unit_name}"
            # new_depiction_obj.v.by_member("Selector").v = f"Selector_{unit_name}"

            if edits.get("is_infantry", False):
                new_depiction_obj.v.by_member("SubDepictions").v = f"HumanSubDepictionsShowroom_{unit_name}"

            source_path.add(new_depiction_obj)
            logger.info(f"Added vehicle showroom depiction for {unit_name}")