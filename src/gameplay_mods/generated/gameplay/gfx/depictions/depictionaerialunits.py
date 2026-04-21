"""Functions for modifying DepictionAerialUnits.ndf"""

from typing import Any
from src.constants.unit_edits import load_depiction_edits
from src.constants.new_units import NEW_UNITS, NEW_DEPICTIONS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ndf, find_obj_by_type, is_obj_type

logger = setup_logger(__name__)

def _find_aerial_depiction_by_blackhole_key(source_path: Any, blackhole_key: str) -> Any:
    """Find a TacticAerialDepictionRegistration object by its BlackHoleKey member value.
    
    Args:
        source_path: The NDF List to search in
        blackhole_key: The BlackHoleKey value to search for (without quotes)
        
    Returns:
        The found object row, or None if not found
    """
    def match_blackhole_key(obj_row: Any) -> bool:
        """Check if object matches the blackhole key."""
        try:
            if not is_obj_type(obj_row.v, "TacticAerialDepictionRegistration"):
                return False
            blackhole_key_member = obj_row.v.by_m("BlackHoleKey")
            # BlackHoleKey is stored as a quoted string, so we need to strip quotes
            blackhole_key_value = str(blackhole_key_member.v).strip("'").strip('"')
            return blackhole_key_value == blackhole_key
        except Exception:
            return False
    
    return source_path.find_by_cond(match_blackhole_key, strict=False)

def edit_gen_gp_gfx_depictionaerialunits(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionAerialUnits.ndf"""
    ndf_file = "DepictionAerialUnits.ndf"

    _edit_depictions(source_path, ndf_file)
    _create_new_depictions(source_path, ndf_file)
                        

def _edit_depictions(source_path: Any, ndf_file: str) -> None:
    """Edit depictions for existing units"""
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
            if key == "new_objects":
                registration = _find_aerial_depiction_by_blackhole_key(source_path, unit_name)
                if registration is None:
                    logger.error(f"Could not find TacticAerialDepictionRegistration for {unit_name}, appending new objects to end")
                    for obj_key, ndf_str in edits.items():
                        source_path.add(ndf.convert(ndf_str))
                        logger.info(f"Added new operator {obj_key} for {unit_name}")
                else:
                    insert_index = registration.index
                    for obj_key, ndf_str in edits.items():
                        source_path.insert(insert_index, ndf.convert(ndf_str))
                        logger.info(f"Inserted new operator {obj_key} for {unit_name}")
                        insert_index += 1
                continue
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
                            ndf_list = ndf.model.List()
                            for item in value:
                                ndf_list.add(f"'{item}'")
                            operator.v.by_m(row_name_or_type).v = ndf_list
                            logger.info(f"Edited {row_name_or_type} for {unit_name}")
                        else:
                            operator.v.by_m(row_name_or_type).v = value
                            logger.info(f"Edited {row_name_or_type} for {unit_name}")
                    else:
                        operator.v.by_m(row_name_or_type).v = value
                        logger.info(f"Edited {row_name_or_type} for {unit_name}")

            elif obj_type == "TacticAerialDepictionRegistration":
                # Namespaces were removed, so we find objects by BlackHoleKey using unit_name
                aerial_template = _find_aerial_depiction_by_blackhole_key(source_path, unit_name)
                
                if aerial_template is None:
                    logger.error(f"Could not find TacticAerialDepictionRegistration with BlackHoleKey='{unit_name}' for {unit_name}")
                    continue

                possible_rows = ["Operators", "Actions", "SubDepictions", "SubDepictionGenerators"]
                for row_name_or_type, value in edits.items():
                    if row_name_or_type == "Operators" and isinstance(value, dict):
                        operators_list = aerial_template.v.by_m("Operators")
                        rows_to_insert = []
                        rows_to_remove = []
                        for row_index, (edit_op, *edit_data) in value.items():
                            if edit_op == "insert":
                                rows_to_insert.append((row_index, edit_data[0]))
                            elif edit_op == "remove":
                                rows_to_remove.append(row_index)
                            elif edit_op == "replace":
                                operators_list.v.replace(row_index, edit_data[0])
                                logger.info(f"Replaced Operators[{row_index}] for {unit_name}")

                        for row_index in sorted(rows_to_remove, reverse=True):
                            operators_list.v.remove(row_index)
                            logger.info(f"Removed Operators[{row_index}] for {unit_name}")
                        for row_index, ndf_str in sorted(rows_to_insert, reverse=True):
                            operators_list.v.insert(row_index, ndf_str)
                            logger.info(f"Inserted Operators[{row_index}] for {unit_name}")

                    elif row_name_or_type in possible_rows:
                        aerial_template.v.by_m(row_name_or_type).v = value
                        logger.info(f"Edited {row_name_or_type} for {unit_name}")
                        

def _create_new_depictions(source_path: Any, ndf_file: str) -> None:
    """Create depictions for new units"""
    # TMimeticUnitRegistration no longer exists in these files
    for unit_descr_name, unit_data in NEW_DEPICTIONS.items():
        if ndf_file not in unit_data["valid_files"]:
            continue
        unit_depictions = unit_data["DepictionAerialUnits_ndf"]
        logger.debug(f"Processing aerial edits for {unit_descr_name}")
        
        for descr_key, descr_obj in unit_depictions.items():
            new_descr_obj = ndf.convert(descr_obj)
            source_path.add(new_descr_obj)
            logger.info(f"Added {descr_key} for {unit_descr_name}")