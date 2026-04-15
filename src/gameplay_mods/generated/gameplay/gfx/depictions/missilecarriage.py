"""Functions for modifying MissileCarriage.ndf"""

from typing import Any
from src.constants.unit_edits import load_depiction_edits
from src.constants.new_units import NEW_UNITS, NEW_DEPICTIONS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ndf

logger = setup_logger(__name__)

def edit_gen_gp_gfx_missilecarriage(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/MissileCarriage.ndf"""
    ndf_file = "MissileCarriage.ndf"

    _edit_carriages(source_path, ndf_file)
    _create_new_carriages(source_path, ndf_file)

def _edit_carriages(source_path: Any, ndf_file: str) -> None:
    """Edit missile carriages for existing units"""
    # Load all depiction edits
    depiction_edits = load_depiction_edits()

    # Process each unit's edits
    for unit_name, unit_data in depiction_edits.items():
        # Skip if this file isn't relevant for this unit
        if ndf_file not in unit_data["valid_files"]:
            continue

        # Get edits for this file
        if "MissileCarriage_ndf" not in unit_data:
            logger.error(f"{ndf_file} is valid for {unit_name} but no edits found")
            continue

        unit_edits = unit_data["MissileCarriage_ndf"]

        for key, edits in unit_edits.items():
            if not isinstance(key, tuple):
                logger.error(f"Key is not a tuple: {key}")
                continue

            namespace, obj_type = key
            if not namespace:
                continue

            missile_carriage = source_path.by_n(namespace)
            if not missile_carriage:
                logger.error(f"Could not find missile carriage {namespace} for {unit_name}")
                continue

            for row_name_or_type, value in edits.items():
                if row_name_or_type == "WeaponInfos":
                    carriage_list = missile_carriage.v.by_m(row_name_or_type)
                    rows_to_insert = []
                    rows_to_remove = []
                    for row_index, (edit_op, *edit_data) in value.items():
                        if edit_op == "edit":
                            for member, new_value in edit_data[0].items():
                                carriage_list.v[row_index].v.by_m(member).v = str(new_value)
                                logger.info(f"Edited {member} for {unit_name}")
                        elif edit_op == "replace":
                            carriage_list.v.replace(row_index, edit_data[0])
                            logger.info(f"Replaced row {row_index} for {unit_name}")
                        elif edit_op == "remove":
                            rows_to_remove.append(row_index)
                        elif edit_op == "insert":
                            rows_to_insert.append((row_index, edit_data[0]))

                    for row_index in sorted(rows_to_remove, reverse=True):
                        carriage_list.v.remove(row_index)
                        logger.info(f"Removed row {row_index} for {unit_name}")
                    for row_index, ndf_str in sorted(rows_to_insert, reverse=True):
                        carriage_list.v.insert(row_index, ndf_str)
                        logger.info(f"Inserted row at {row_index} for {unit_name}")
                else:
                    missile_carriage.v.by_m(row_name_or_type).v = value
                    logger.info(f"Edited {row_name_or_type} for {unit_name}")
            
            
def _create_new_carriages(source_path: Any, ndf_file: str) -> None:
    """Create missile carriages for new units"""
    for unit_name, unit_data in NEW_DEPICTIONS.items():
        if ndf_file not in unit_data["valid_files"]:
            continue
        unit_depictions = unit_data["MissileCarriage_ndf"]
        
        for descr_type, descr_obj in unit_depictions.items():
            new_descr_obj = ndf.convert(descr_obj)
            source_path.add(new_descr_obj)
            logger.info(f"Added {descr_type} for {unit_name}")