"""Functions for modifying DepictionAerialUnits.ndf"""

from typing import Any
from src.constants.unit_edits import load_depiction_edits
from src.constants.new_units import NEW_UNITS, NEW_DEPICTIONS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ndf, find_obj_by_type

logger = setup_logger(__name__)


def edit_gen_gp_gfx_depictionaerialunitsshowroom(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialUnitsShowRoom.ndf"""
    ndf_file = "DepictionAerialUnitsShowRoom.ndf"
    
    _create_new_depictions(source_path, ndf_file)
    

def _create_new_depictions(source_path: Any, ndf_file: str) -> None:
    """Create showroom depictions for new aerial units"""
    mimeticregistration_descr = find_obj_by_type(source_path, "TMimeticUnitRegistration")
    insert_index = mimeticregistration_descr.index
    mimeticunit_map = mimeticregistration_descr.v.by_m("MimeticUnit")
    for unit_descr_name, unit_data in NEW_DEPICTIONS.items():
        unit_name = unit_data["unit_name"]
        if ndf_file not in unit_data["valid_files"]:
            continue
        unit_depictions = unit_data["DepictionAerialUnitsShowroom_ndf"]
        logger.debug(f"Processing aerial edits for {unit_descr_name}")
        
        for descr_type, descr_obj in unit_depictions.items():
            new_descr_obj = ndf.convert(descr_obj)
            source_path.insert(insert_index, new_descr_obj)
            logger.info(f"Added {descr_type} for {unit_name}")
    
        _add_unit_mimetic(unit_name, mimeticunit_map)
            

def _add_unit_mimetic(unit_name: str, mimeticunit_map: Any) -> None:
    """Add unit mimetic to TMimeticUnitRegistration"""
    new_entry = f"('showroom_{unit_name}', Gfx_{unit_name}_Showroom)"
    mimeticunit_map.v.add(new_entry)
    logger.info(f"Added showroomunit mimetic for {unit_name}")