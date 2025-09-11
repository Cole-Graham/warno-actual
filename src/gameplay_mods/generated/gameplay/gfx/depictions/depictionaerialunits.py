"""Functions for modifying DepictionAerialUnits.ndf"""

from typing import Any
from src.constants.unit_edits import load_depiction_edits
from src.constants.new_units import NEW_UNITS, NEW_DEPICTIONS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ndf, find_obj_by_type, is_obj_type

logger = setup_logger(__name__)

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
                        

def _create_new_depictions(source_path: Any, ndf_file: str) -> None:
    """Create depictions for new units"""
    mimeticregistration_descr = find_obj_by_type(source_path, "TMimeticUnitRegistration")
    mimeticunit_map = mimeticregistration_descr.v.by_m("MimeticUnit")
    for unit_descr_name, unit_data in NEW_DEPICTIONS.items():
        if ndf_file not in unit_data["valid_files"]:
            continue
        unit_depictions = unit_data["DepictionAerialUnits_ndf"]
        logger.debug(f"Processing aerial edits for {unit_descr_name}")
        
        for descr_key, descr_obj in unit_depictions.items():
            new_descr_obj = ndf.convert(descr_obj)
            source_path.add(new_descr_obj)
            logger.info(f"Added {descr_key} for {unit_descr_name}")
        
        unit_name = unit_data["unit_name"]
        _add_unit_mimetic(unit_name, mimeticunit_map)
    
    # Fix order of descriptors
    descriptors_to_move = []
    # TMimeticUnitRegistration
    descriptors_to_move.append((mimeticregistration_descr.index, mimeticregistration_descr))
    # Pilot descriptors
    for descr_row in source_path:
        if is_obj_type(descr_row.v, "TemplateDepictionPilote"):
            descriptors_to_move.append((descr_row.index, descr_row))
    
    for index, descr_row in reversed(descriptors_to_move):
        source_path.remove(index)
    for index, descr_row in descriptors_to_move:
        source_path.add(descr_row)

def _add_unit_mimetic(unit_name: str, mimeticunit_map: Any) -> None:
    """Add unit mimetic to TMimeticUnitRegistration"""
    new_entry = f"('{unit_name}', TacticDepiction_{unit_name})"
    mimeticunit_map.v.add(new_entry)
    logger.info(f"Added unit mimetic for {unit_name}")