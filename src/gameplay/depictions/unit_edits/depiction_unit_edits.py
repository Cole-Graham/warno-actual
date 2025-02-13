import re
import traceback
from typing import Any, Dict  # noqa

from src import ndf
from src.constants.unit_edits import load_depiction_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes

logger = setup_logger(__name__)


def unit_edits_depictioninfantry(source_path: Any) -> None:
    """Edit unit depictions in GeneratedDepictionInfantry.ndf"""
    ndf_file = "GeneratedDepictionInfantry.ndf"
    
    # Load all depiction edits
    depiction_edits = load_depiction_edits()
    
    # Process each unit's edits
    for unit_name, unit_data in depiction_edits.items():
        # Skip if this file isn't relevant for this unit
        if ndf_file not in unit_data["valid_files"]:
            continue
        
        if "GeneratedDepictionInfantry_ndf" not in unit_data:
            logger.error(f"{ndf_file} is valid for {unit_name} but no edits found")
            continue
        
        unit_edits = unit_data["GeneratedDepictionInfantry_ndf"]
        logger.debug(f"Processing infantry edits for {unit_name}")
        
        for (namespace, obj_type), edits in unit_edits.items():
            if namespace and namespace.startswith("AllWeaponAlternatives_"):
                weapon_alternatives = source_path.by_n(namespace)
                if not weapon_alternatives:
                    logger.error(f"Could not find weapon alternatives {namespace} for {unit_name}")
                    continue
                
                for row_index, (edit_type, edit_list) in edits.items():
                    if edit_type == "edit":
                        for member, value in edit_list:
                            if member == "MeshDescriptor" or member == "ReferenceMeshForSkeleton":
                                new_mesh = f"$/GFX/DepictionResources/Modele_{value}"
                                weapon_alternatives.v[row_index].v.by_m(member).v = new_mesh
                                logger.info(f"Changed {member} for {unit_name} to {new_mesh}")

            elif namespace and namespace.startswith("AllWeaponSubDepiction_"):
                weapon_subdepictions = source_path.by_n(namespace)
                if not weapon_subdepictions:
                    logger.error(f"Could not find weapon subdepictions {namespace} for {unit_name}")
                    continue
                
                for member, member_edits in edits.items():
                    if member == "Operators":
                        operators_member = weapon_subdepictions.v.by_m(member)
                        for index, (edit_type, edit_list) in member_edits.items():
                            if edit_type == "edit":
                                for submember, value in edit_list:
                                    if submember == "FireEffectTag":
                                        # Remove quotes if present
                                        value = value.strip('"').strip("'")
                                        new_value = ndf.convert(f'["FireEffect_{value}"]')
                                        operators_member.v[index].v.by_m(submember).v = new_value
                                        logger.info(f"Changed FireEffectTag for {unit_name} to {value}")

            elif namespace and namespace.startswith("TacticDepiction_"):
                tacticdepiction_soldier = source_path.by_n(namespace)
                if not tacticdepiction_soldier:
                    logger.error(f"Could not find tactic depiction {namespace} for {unit_name}")
                    continue
                
                for member, member_edits in edits.items():
                    if member == "Operators":
                        operators_member = tacticdepiction_soldier.v.by_m(member)
                        for index, (edit_type, edit_list) in member_edits.items():
                            if edit_type == "replace":
                                # need to check if ConditionalTags object exists, else create it
                                conditional_tags = operators_member.v[index].v.by_m("ConditionalTags", False)
                                if conditional_tags is None:
                                    operators_member.v[index].v.add(ndf.convert("ConditionalTags = []"))
                                    conditional_tags = operators_member.v[index].v.by_m("ConditionalTags")
                                
                                for new_tag, mesh_alternative in edit_list:
                                    # Remove quotes if present
                                    # old_tag = old_tag.strip("'")
                                    # mesh_alternative = mesh_alternative.strip("'")
                                    
                                    for tag_tuple in conditional_tags.v:
                                        # weapon_type = strip_quotes(tag_tuple.v[0])
                                        mesh_alt = strip_quotes(tag_tuple.v[1])
                                        
                                        if mesh_alt == mesh_alternative:
                                            tag_tuple.v = f"('{new_tag}', '{mesh_alternative}')"
                                            logger.info(f"Replaced tag with {new_tag} for mesh "
                                                        f"{mesh_alternative} in {unit_name}")
                                        

def unit_edits_depictionaerial(source_path: Any) -> None:
    """Edit unit depictions in DepictionAerialUnits.ndf"""
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
                        for (member, val2) in value:
                            operator.v.add(f"{member} = {val2}")
                            logger.info(f"Added {member} for {unit_name}")
                    elif row_name_or_type == "replace_members":
                        for (member, replacement, new_value) in value:
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
                    
            elif namespace and namespace.startswith("Gfx_"):
                aerial_template = source_path.by_n(namespace)
                
                for row_name_or_type, value in edits.items():
                    # SubDepictions and SubDepictionGenerators are not modified, but
                    # ndf parse screws them up, so I just fix them by replacing the values
                    possible_rows = ["Operators", "Actions", "SubDepictions", "SubDepictionGenerators"]
                    if row_name_or_type in possible_rows:
                        aerial_template.v.by_m(row_name_or_type).v = value
                        logger.info(f"Edited {row_name_or_type} for {unit_name}")


def unit_edits_missilecarriage(source_path: Any) -> None:
    """Edit unit missile carriage in MissileCarriage.ndf"""
    ndf_file = "MissileCarriage.ndf"
    
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
            if namespace and namespace.endswith(unit_name):
                missile_carriage = source_path.by_n(namespace)
                if not missile_carriage:
                    logger.error(f"Could not find missile carriage {namespace} for {unit_name}")
                    continue
                
                for row_name_or_type, value in edits.items():
                    if row_name_or_type == "WeaponInfos":
                        carriage_list = missile_carriage.v.by_m(row_name_or_type)               
                        rows_to_add, rows_to_remove = [], []
                        for carriage_index, carriage_edits in value.items():
                            
                            if isinstance(carriage_edits, tuple):
                                if carriage_edits[0] == "add":
                                    rows_to_add.append(carriage_index)
                                    logger.info(f"Added row {carriage_index} {carriage_edits[1]} for {unit_name}")
                                elif carriage_edits[0] == "replace":
                                    carriage_list.v.replace(carriage_index, carriage_edits[1])
                                    logger.info(f"Replaced row {carriage_index} with {carriage_edits[1]} for {unit_name}")
                            
                            elif carriage_edits == "remove":
                                rows_to_remove.append(carriage_index)
                            else:
                                for member, new_value in carriage_edits.items():
                                    carriage_list.v[carriage_index].v.by_m(member).v = str(new_value)
                                    logger.info(f"Edited {member} for {unit_name}")
                        
                        if rows_to_add:
                            for row in rows_to_add:
                                carriage_list.v.add(row)
                        if rows_to_remove:
                            for row_index in rows_to_remove:
                                carriage_list.v.remove(row_index)
                                logger.info(f"Removed row {row_index} for {unit_name}")
            
            elif namespace and namespace.endswith("_Showroom"):
                missile_carriage = source_path.by_n(namespace)
                if not missile_carriage:
                    logger.error(f"Could not find showroom missile carriage {namespace} for {unit_name}")
                    continue
                    
                for row_name_or_type, value in edits.items():
                    if row_name_or_type == "WeaponInfos":
                        carriage_list = missile_carriage.v.by_m(row_name_or_type)
                        rows_to_add, rows_to_remove = [], []
                        for carriage_index, carriage_edits in value.items():
                            
                            if isinstance(carriage_edits, tuple):
                                if carriage_edits[0] == "add":
                                    rows_to_add.append(carriage_edits[1])
                                    logger.info(f"Added row {carriage_edits[1]} for {unit_name}")
                                elif carriage_edits[0] == "replace":
                                    carriage_list.v.replace(carriage_index, carriage_edits[1])
                                    logger.info(f"Replaced row {carriage_index} with {carriage_edits[1]} for {unit_name}")
                            
                            elif "remove" in carriage_edits:
                                rows_to_remove.append(carriage_index)
                            else:
                                for member, new_value in carriage_edits.items():
                                    carriage_list.v[carriage_index].v.by_m(member).v = str(new_value)
                                    logger.info(f"Edited {member} for {unit_name}")
                        
                        if rows_to_add:
                            for row_index in rows_to_add:
                                carriage_list.v.add(row_index)
                        if rows_to_remove:
                            for row_index in rows_to_remove:
                                carriage_list.v.remove(row_index)
                                logger.info(f"Removed row {row_index} for {unit_name}")
            
            else:
                pass # expand if we need to look for row by type


def unit_edits_missilecarriagedepiction(source_path: Any) -> None:
    """Edit unit missile carriage depiction in MissileCarriageDepiction.ndf"""
    ndf_file = "MissileCarriageDepiction.ndf"
    
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
                pass # expand if we need to look for row by type


def unit_edits_depictionvehicles(source_path: Any) -> None:
    """Edit unit vehicle depictions in DepictionVehicles.ndf"""
    ndf_file = "DepictionVehicles.ndf"
    
    # Load all depiction edits
    depiction_edits = load_depiction_edits()
    
    # Process each unit's edits
    for unit_name, unit_data in depiction_edits.items():
        # Skip if this file isn't relevant for this unit
        if ndf_file not in unit_data["valid_files"]:
            continue
            
        # Get edits for this file
        if "DepictionVehicles_ndf" not in unit_data:
            logger.error(f"{ndf_file} is valid for {unit_name} but no edits found")
            continue
            
        unit_edits = unit_data["DepictionVehicles_ndf"]
        
        for key, edits in unit_edits.items():
            if not isinstance(key, tuple):
                logger.error(f"Key is not a tuple: {key}")
                continue
                
            namespace, obj_type = key
            if "copy" in edits:
                if namespace.startswith("DepictionOperator_"):
                    # Handle weapon operator copy
                    donor = source_path.by_n(namespace)
                    if not donor:
                        logger.error(f"Could not find donor {namespace} for {unit_name}")
                        continue
                        
                    new_entry = donor.copy()
                    new_entry.namespace = edits["copy"]
                    new_entry = _handle_weapon_operator(unit_name, new_entry, edits)
                    
                    # Calculate insertion index
                    match = re.search(r'(\d+)$', edits["copy"])
                    if match:
                        index_addition = int(match.group(1))
                        row_index = donor.index + (index_addition - 1)
                        source_path.insert(row_index, new_entry)
                        logger.info(f"Inserted new weapon operator for {unit_name} at index {row_index}")
                
                elif namespace.startswith("Gfx_"):
                    # Handle vehicle depiction copy
                    donor = source_path.by_n(namespace)
                    if not donor:
                        logger.error(f"Could not find donor {namespace} for {unit_name}")
                        continue
                        
                    new_entry = donor.copy()
                    new_entry.namespace = edits["copy"]
                    new_entry = _handle_vehicle_depiction(unit_name, new_entry, edits)
                    source_path.insert(donor.index + 1, new_entry)
                    logger.info(f"Inserted new vehicle depiction for {unit_name}")
            
            else:
                # Handle direct edits
                if namespace.startswith("DepictionOperator_"):
                    weapon_operator = source_path.by_n(namespace)
                    if weapon_operator:
                        _handle_weapon_operator(unit_name, weapon_operator, edits)
                        logger.info(f"Updated weapon operator for {unit_name}")
                
                elif namespace.startswith("Gfx_"):
                    vehicle_depiction = source_path.by_n(namespace)
                    if vehicle_depiction:
                        _handle_vehicle_depiction(unit_name, vehicle_depiction, edits)
                        logger.info(f"Updated vehicle depiction for {unit_name}")


def _handle_weapon_operator(unit_name, weapon_operator, edits, is_new_entry=False):  # noqa
    for row_name_or_type, value in edits.items():
        if row_name_or_type == "copy":
            continue
        
        member_access = weapon_operator.v.by_m(row_name_or_type)           
        if row_name_or_type == "FireEffectTag":
            member_access.v = value
        elif row_name_or_type == "WeaponShootDataPropertyName":
            member_access.v = "[" + ",".join(value) + "]"
        
    return weapon_operator


def _handle_vehicle_depiction(unit_name, vehicle_depiction, edits, is_new_entry=False):  # noqa
    for row_name_or_type, value in edits.items():
        if row_name_or_type == "copy":
            continue
        
        member_access = vehicle_depiction.v.by_m(row_name_or_type)
        if row_name_or_type == "Operators":
            operators = member_access
            
            for op_index, op_edits in value.items():
                if isinstance(op_edits, tuple) and op_edits[0] == "add":
                    operators.v.insert(op_index, op_edits[1])
                else:
                    logger.error(f"Unknown operator edit: {op_edits}")
                    pass
            
        elif row_name_or_type == "Actions":
            try:    
                member_access.v = value
            except Exception as e:
                logger.error(f"Unknown action edit: {value}")
                logger.error(f"Exception: {str(e)}")
                logger.error(f"Traceback: {traceback.format_exc()}")

        elif row_name_or_type == "SubDepictions":
            sub_depictions = member_access
            
            try:
                for sub_depict_index, sub_depict_edits in value.items():
                    sub_depiction = sub_depictions.v[sub_depict_index]
                    for member_name_or_type, member_edits in sub_depict_edits.items():
                        
                        if member_name_or_type == "Depiction":
                            depiction_member = sub_depiction.v.by_m(member_name_or_type)
                            for dep_name_or_type, dep_edits in member_edits.items():
                                
                                if dep_name_or_type == "Operators":
                                    operator_member = depiction_member.v.by_m(dep_name_or_type)
                                    for op_index, op_edits in dep_edits.items():
                                        if isinstance(op_edits, tuple) and op_edits[0] == "add":
                                            operator_member.v.insert(op_index, op_edits[1])
                                        else:
                                            logger.error(f"Unknown operator edit: {op_edits}")
                                            pass
                                            
                                elif dep_name_or_type == "Actions":
                                    action_member = depiction_member.v.by_m(dep_name_or_type)
                                    for action_index, action_edits in dep_edits.items():
                                        if isinstance(action_edits, tuple) and action_edits[0] == "add":
                                            action_member.v.insert(action_index, action_edits[1])
                                        else:
                                            logger.error(f"Unknown action edit: {action_edits}")
                                            pass
            
            except Exception as e:
                logger.error(f"Unknown subdepiction edit: {row_name_or_type}")
                logger.error(f"Exception: {str(e)}")
                logger.error(f"Traceback: {traceback.format_exc()}")

        else:
            logger.error(f"Unknown row name or type: {row_name_or_type}")
            pass
    
    return vehicle_depiction
