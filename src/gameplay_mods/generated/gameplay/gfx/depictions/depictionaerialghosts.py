"""Functions for modifying DepictionAerialGhosts.ndf"""

from typing import Any
from src.constants.new_units import NEW_UNITS, NEW_DEPICTIONS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_mimetic_name
from src import ndf

logger = setup_logger(__name__)

def edit_gen_gp_gfx_depictionaerialghosts(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialGhosts.ndf"""
    
    _handle_new_units(source_path)
    
    
def _handle_new_units(source_path: Any) -> None:
    """Handle new units for DepictionAerialGhosts.ndf"""
    
    for donor, edits in NEW_UNITS.items():
        if edits.get("is_aerial", False):
            unit_name = edits["NewName"]
            donor_name = donor[0]
            
            # Check for custom depiction first
            depiction_key = unit_name.lower()
            if depiction_key in NEW_DEPICTIONS and "DepictionAerialGhosts_ndf" in NEW_DEPICTIONS[depiction_key]:
                unit_depictions = NEW_DEPICTIONS[depiction_key]["DepictionAerialGhosts_ndf"]
                for descr_type, descr_obj in unit_depictions.items():
                    new_descr_obj = ndf.convert(descr_obj)
                    source_path.add(new_descr_obj)
                    logger.info(f"Added custom aerial ghost depiction for {unit_name}")
            else:
                # Find donor by MimeticName
                donor_obj = find_obj_by_mimetic_name(source_path, donor_name, "GhostAerialDepictionRegistration")
                
                if not donor_obj:
                    logger.error(f"Could not find donor ghost depiction with MimeticName='{donor_name}'")
                    continue
                
                new_depiction_obj = donor_obj.copy()
                new_depiction_obj.namespace = None
                mimetic_member = new_depiction_obj.v.by_m("MimeticName")
                mimetic_member.v = f'"{unit_name}"'
                alternatives_member = new_depiction_obj.v.by_m("Alternatives")
                alternatives_member.v = f"Alternatives_{unit_name}"
                
                source_path.add(new_depiction_obj)
                logger.info(f"Added aerial ghost depiction for {unit_name}")