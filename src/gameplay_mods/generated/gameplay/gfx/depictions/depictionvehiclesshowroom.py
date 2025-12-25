"""Functions for modifying DepictionVehiclesShowRoom.ndf"""

from typing import Any
from src.constants.new_units import NEW_UNITS, NEW_DEPICTIONS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_mimetic_name

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
            
            # Check for custom depiction first
            depiction_key = unit_name.lower()
            if depiction_key in NEW_DEPICTIONS and "DepictionVehiclesShowroom_ndf" in NEW_DEPICTIONS[depiction_key]:
                unit_depictions = NEW_DEPICTIONS[depiction_key]["DepictionVehiclesShowroom_ndf"]
                for descr_type, descr_obj in unit_depictions.items():
                    from src import ndf
                    new_descr_obj = ndf.convert(descr_obj)
                    source_path.add(new_descr_obj)
                    logger.info(f"Added custom showroom vehicle depiction for {unit_name}")
            else:
                # Find donor by MimeticName
                donor_mimetic = f"showroom_{donor_name}"
                donor_obj = find_obj_by_mimetic_name(source_path, donor_mimetic, "ShowroomVehicleDepictionRegistration")
                
                if not donor_obj:
                    logger.error(f"Could not find donor showroom depiction with MimeticName='{donor_mimetic}'")
                    continue
                
                new_depiction_obj = donor_obj.copy()
                new_depiction_obj.namespace = None
                mimetic_member = new_depiction_obj.v.by_m("MimeticName")
                mimetic_member.v = f'"showroom_{unit_name}"'
                alternatives_member = new_depiction_obj.v.by_m("Alternatives")
                alternatives_member.v = f"Alternatives_{unit_name}"

                if edits.get("is_infantry", False):
                    subdep_member = new_depiction_obj.v.by_m("SubDepictions", False)
                    if subdep_member:
                        subdep_member.v = f"HumanSubDepictionsShowroom_{unit_name}"

                source_path.add(new_depiction_obj)
                logger.info(f"Added vehicle showroom depiction for {unit_name}")