"""Functions for modifying DepictionAerialUnits.ndf"""

from typing import Any
from src.constants.unit_edits import load_depiction_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_gen_gp_gfx_depictionaerialunits(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialUnits.ndf"""
    ndf_file = "DepictionAerialUnits.ndf"

    # Load all depiction edits
    depiction_edits = load_depiction_edits()

    # Process each unit's edits
    for unit_name, unit_data in depiction_edits.items():
        # Skip if this file isn't relevant for this unit
        if ndf_file not in unit_data["valid_files"]:
            continue

        # Get edits for this file
        if "DepictionAerialUnits_ndf" not in unit_data:
            logger.error(f"{ndf_file} is valid for {unit_name} but no edits found")
            continue

        unit_edits = unit_data["DepictionAerialUnits_ndf"]
        logger.debug(f"Processing aerial edits for {unit_name}")

        for key, edits in unit_edits.items():
            if not isinstance(key, tuple):
                logger.error(f"Key is not a tuple: {key}")
                continue
            namespace, obj_type = key
            if namespace and namespace.startswith("Op_"):
                operator = source_path.by_n(namespace)
                if operator.v.type != obj_type:
                    operator.v.type = obj_type
                    logger.info(f"Changed type of {key} to {obj_type}")
                for row_name_or_type, value in edits.items():
                    if row_name_or_type == "add_members":
                        for member, val2 in value:
                            operator.v.add(f"{member} = {val2}")
                            logger.info(f"Added {member} for {unit_name}")
                    elif row_name_or_type == "replace_members":
                        for member, replacement, new_value in value:
                            if new_value is None:
                                new_value = operator.v.by_m(member).v
                            member_index = operator.v.by_m(member).index
                            operator.v.replace(member_index, f"{replacement} = {new_value}")
                            logger.info(f"Replaced {member} with {replacement} = {new_value} for {unit_name}")
                    elif row_name_or_type == "WeaponShootDataPropertyName":
                        if isinstance(value, list):
                            value = "[" + ",".join(value) + "]"
                            operator.v.by_m(row_name_or_type).v = value
                            logger.info(f"Edited {row_name_or_type} for {unit_name}")
                        else:
                            operator.v.by_m(row_name_or_type).v = value
                            logger.info(f"Edited {row_name_or_type} for {unit_name}")
                    else:
                        operator.v.by_m(row_name_or_type).v = value
                        logger.info(f"Edited {row_name_or_type} for {unit_name}")

            elif namespace and namespace.startswith("TacticDepiction_"):
                aerial_template = source_path.by_n(namespace)

                for row_name_or_type, value in edits.items():
                    # SubDepictions and SubDepictionGenerators are not modified, but
                    # ndf parse screws them up, so I just fix them by replacing the values
                    possible_rows = ["Operators", "Actions", "SubDepictions", "SubDepictionGenerators"]
                    if row_name_or_type in possible_rows:
                        aerial_template.v.by_m(row_name_or_type).v = value
                        logger.info(f"Edited {row_name_or_type} for {unit_name}")