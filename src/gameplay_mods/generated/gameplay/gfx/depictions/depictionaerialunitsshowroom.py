"""Functions for modifying DepictionAerialUnitsShowRoom.ndf"""

from typing import Any
from src.constants.unit_edits import load_depiction_edits
from src.constants.new_units import NEW_DEPICTIONS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ndf, find_obj_by_blackhole_key

logger = setup_logger(__name__)


def edit_gen_gp_gfx_depictionaerialunitsshowroom(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialUnitsShowRoom.ndf"""
    ndf_file = "DepictionAerialUnitsShowRoom.ndf"
    
    _edit_depictions(source_path, ndf_file)
    _create_new_depictions(source_path, ndf_file)
    

def _edit_depictions(source_path: Any, ndf_file: str) -> None:
    """Edit showroom depictions for existing units."""
    depiction_edits = load_depiction_edits()

    for unit_name, unit_data in depiction_edits.items():
        if ndf_file not in unit_data["valid_files"]:
            continue

        if "DepictionAerialUnitsShowRoom_ndf" not in unit_data:
            logger.error(f"{ndf_file} is valid for {unit_name} but no edits found")
            continue

        unit_edits = unit_data["DepictionAerialUnitsShowRoom_ndf"]

        for key, edits in unit_edits.items():
            if not isinstance(key, tuple):
                logger.error(f"Key is not a tuple: {key}")
                continue

            namespace, obj_type = key

            if obj_type == "ShowroomAerialDepictionRegistration":
                blackhole_key = f"showroom_{unit_name}"
                showroom_template = find_obj_by_blackhole_key(
                    source_path, blackhole_key, "ShowroomAerialDepictionRegistration",
                )

                if showroom_template is None:
                    logger.error(
                        f"Could not find ShowroomAerialDepictionRegistration "
                        f"with BlackHoleKey='{blackhole_key}' for {unit_name}"
                    )
                    continue

                for member_name, value in edits.items():
                    showroom_template.v.by_m(member_name).v = value
                    logger.info(f"Edited {member_name} for {unit_name}")


def _create_new_depictions(source_path: Any, ndf_file: str) -> None:
    """Create showroom depictions for new aerial units"""
    for unit_descr_name, unit_data in NEW_DEPICTIONS.items():
        unit_name = unit_data["unit_name"]
        if ndf_file not in unit_data["valid_files"]:
            continue
        unit_depictions = unit_data["DepictionAerialUnitsShowroom_ndf"]
        logger.debug(f"Processing aerial edits for {unit_descr_name}")
        
        for descr_type, descr_obj in unit_depictions.items():
            new_descr_obj = ndf.convert(descr_obj)
            source_path.add(new_descr_obj)
            logger.info(f"Added {descr_type} for {unit_name}")