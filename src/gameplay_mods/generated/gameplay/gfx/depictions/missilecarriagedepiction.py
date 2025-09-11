"""Functions for modifying MissileCarriageDepiction.ndf"""

from typing import Any
from src.constants.unit_edits import load_depiction_edits
from src.constants.new_units import NEW_UNITS, NEW_DEPICTIONS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ndf

logger = setup_logger(__name__)

def edit_gen_gp_gfx_missilecarriagedepiction(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/MissileCarriageDepiction.ndf"""
    ndf_file = "MissileCarriageDepiction.ndf"

    _edit_depictions(source_path, ndf_file)
    _create_new_depictions(source_path, ndf_file)
    

def _edit_depictions(source_path: Any, ndf_file: str) -> None:
    """Edit missile carriage depictions for existing units"""
    # Load all depiction edits
    depiction_edits = load_depiction_edits()

    # Process each unit's edits
    for unit_name, unit_data in depiction_edits.items():
        # Skip if this file isn't relevant for this unit
        if ndf_file not in unit_data["valid_files"]:
            continue

        # Get edits for this file
        if "MissileCarriageDepiction_ndf" not in unit_data:
            logger.error(f"{ndf_file} is valid for {unit_name} but no edits found")
            continue

        unit_edits = unit_data["MissileCarriageDepiction_ndf"]

        for key, edits in unit_edits.items():
            if not isinstance(key, tuple):
                logger.error(f"Key is not a tuple: {key}")
                continue

            namespace, obj_type = key
            if namespace is not None and namespace.endswith(unit_name):
                missile_carriage = source_path.by_n(namespace)

                for row_name_or_type, value in edits.items():
                    if row_name_or_type == "Missiles":
                        missile_list = missile_carriage.v.by_m(row_name_or_type)
                        rows_to_add, rows_to_remove = [], []
                        for missile_index, missile_edits in value.items():
                            if isinstance(missile_edits, tuple):
                                if missile_edits[0] == "add":
                                    rows_to_add.append(missile_index)
                                    logger.info(f"Added missile {missile_index} {missile_edits[1]} for {unit_name}")
                                elif missile_edits[0] == "replace":
                                    missile_list.v.replace(missile_index, missile_edits[1])
                                    logger.info(f"Replaced row {missile_index} for {unit_name}")

                            elif "remove" in missile_edits:
                                rows_to_remove.append(missile_index)
                            else:
                                for member, new_value in missile_edits.items():
                                    missile_list.v[missile_index].v.by_m(member).v = str(new_value)
                                    logger.info(f"Edited {member} for {unit_name}")

                        if rows_to_add:
                            for row in rows_to_add:
                                missile_list.v.add(row)
                        if rows_to_remove:
                            for row_index in rows_to_remove:
                                missile_list.v.remove(row_index)
                                logger.info(f"Removed missile {row_index} for {unit_name}")

            elif namespace is not None and namespace.startswith("SubGenerators_Showroom_"):
                missile_carriage = source_path.by_n(namespace)

                for row_name_or_type, value in edits.items():
                    if row_name_or_type == "Missiles":
                        missile_list = missile_carriage.v.by_m(row_name_or_type)
                        rows_to_add, rows_to_remove = [], []
                        for missile_index, missile_edits in value.items():

                            if isinstance(missile_edits, tuple):
                                if missile_edits[0] == "add":
                                    rows_to_add.append(missile_edits[1])
                                    logger.info(f"Added missile {missile_index} {missile_edits[1]} for {unit_name}")
                                elif missile_edits[0] == "replace":
                                    missile_list.v.replace(missile_index, missile_edits[1])
                                    logger.info(f"Replaced row {missile_index} for {unit_name}")

                            elif "remove" in missile_edits:
                                rows_to_remove.append(missile_index)
                                logger.info(f"Removed missile {missile_index} {missile_edits[1]} for {unit_name}")
                            else:
                                for member, new_value in missile_edits.items():
                                    missile_list.v[missile_index].v.by_m(member).v = str(new_value)
                                    logger.info(f"Edited {member} to {new_value} for {unit_name}")

                        if rows_to_add:
                            for row in rows_to_add:
                                missile_list.v.add(row)
                        if rows_to_remove:
                            for row_index in rows_to_remove:
                                missile_list.v.remove(row_index)

            else:
                pass  # expand if we need to look for row by type
            

def _create_new_depictions(source_path: Any, ndf_file: str) -> None:
    """Create missile carriage depictions for new units"""
    for unit_name, unit_data in NEW_DEPICTIONS.items():
        if ndf_file not in unit_data["valid_files"]:
            continue
        unit_depictions = unit_data["MissileCarriageDepiction_ndf"]
        logger.debug(f"Processing missile carriage depictions for {unit_name}")
        
        for descr_type, descr_obj in unit_depictions.items():
            new_descr_obj = ndf.convert(descr_obj)
            source_path.add(new_descr_obj)
            logger.info(f"Added {descr_type} for {unit_name}")