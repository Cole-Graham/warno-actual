import re
import traceback
from typing import Any

from src.utils.logging_utils import setup_logger

from .POL_depiction_edits import mortier_2b9_vasilek_para_pol
from .SOV_depiction_edits import (
    mi_8tv_gunship_sov,
    mortier_2b9_vasilek_nonpara_sov,
    mortier_2b9_vasilek_sov,
    mtlb_vasilek_sov,
)

logger = setup_logger(__name__)

# fmt: off
dics_list = [
    mi_8tv_gunship_sov, 
    mtlb_vasilek_sov,
    mortier_2b9_vasilek_sov,
    mortier_2b9_vasilek_nonpara_sov,
    mortier_2b9_vasilek_para_pol
]
# fmt: on

def unit_edits_depictionaerial(source_path) -> None:
    """Edit unit depictions in DepictionAerialUnits.ndf"""
    
    ndf_file = "DepictionAerialUnits.ndf"
    dic_length = len(dics_list)
    
    unit_list_index = 0
    while unit_list_index < dic_length:
        
        valid_files = dics_list[unit_list_index]["valid_files"]
        if ndf_file not in valid_files:
            unit_list_index += 1
            continue
        
        unit_name = dics_list[unit_list_index]["unit_name"]
        unit_edits = dics_list[unit_list_index]["DepictionAerialUnits_ndf"]
        logger.debug(f"Unit edits: {unit_edits}")
        for key, edits in unit_edits.items():
            if isinstance(key, tuple):
                namespace, obj_type = key
            else:
                logger.error(f"Key is not a tuple: {key}")
                continue
            
            if namespace != None and namespace.startswith("Gfx_"):
                aerial_template = source_path.by_n(namespace)
                
                for row_name_or_type, value in edits.items():
                    # SubDepictions and SubDepictionGenerators are not modified, but
                    # ndf parse screws them up so I just fix them by replacing the values
                    possible_rows = ["Operators", "Actions", "SubDepictions",
                                    "SubDepictionGenerators"]
                    if row_name_or_type in possible_rows:
                        aerial_template.v.by_m(row_name_or_type).v = value
                        logger.info(f"Edited {row_name_or_type} for {unit_name}")
                        
            else:
                pass # expand if we need to look for row by type
            
        unit_list_index += 1

def unit_edits_missilecarriage(source_path) -> None:
    """Edit unit missile carriage in MissileCarriage.ndf"""
    
    ndf_file = "MissileCarriage.ndf"
    dic_length = len(dics_list)
    
    unit_list_index = 0
    while unit_list_index < dic_length:
        
        valid_files = dics_list[unit_list_index]["valid_files"]
        if ndf_file not in valid_files:
            unit_list_index += 1
            continue
        
        unit_name = dics_list[unit_list_index]["unit_name"]
        unit_edits = dics_list[unit_list_index]["MissileCarriage_ndf"]
        for key, edits in unit_edits.items():
            if isinstance(key, tuple):
                namespace, obj_type = key
            else:
                logger.error(f"Key is not a tuple: {key}")
                continue
            
            if namespace != None and namespace.endswith(unit_name):
                missile_carriage = source_path.by_n(namespace)
                
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
                            
                            elif "remove" in carriage_edits:
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
            
            elif namespace != None and namespace.endswith("_Showroom"):
                missile_carriage = source_path.by_n(namespace)
                
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
                            for row in rows_to_add:
                                carriage_list.v.add(row_index)
                        if rows_to_remove:
                            for row_index in rows_to_remove:
                                carriage_list.v.remove(row_index)
                                logger.info(f"Removed row {row_index} for {unit_name}")
            
            else:
                pass # expand if we need to look for row by type
            
        unit_list_index += 1

def unit_edits_missilecarriagedepiction(source_path) -> None:
    """Edit unit missile carriage depiction in MissileCarriageDepiction.ndf"""
    
    ndf_file = "MissileCarriageDepiction.ndf"
    dic_length = len(dics_list)
    
    unit_list_index = 0
    while unit_list_index < dic_length:
        
        valid_files = dics_list[unit_list_index]["valid_files"]
        if ndf_file not in valid_files:
            unit_list_index += 1
            continue
        
        unit_name = dics_list[unit_list_index]["unit_name"]
        unit_edits = dics_list[unit_list_index]["MissileCarriageDepiction_ndf"]
        for key, edits in unit_edits.items():
            if isinstance(key, tuple):
                namespace, obj_type = key
            else:
                logger.error(f"Key is not a tuple: {key}")
                continue

            if namespace != None and namespace.endswith(unit_name):
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
            
            elif namespace != None and namespace.startswith("SubGenerators_Showroom_"):
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
            
        unit_list_index += 1

def unit_edits_depictionvehicles(source_path) -> None:
    """Edit unit vehicle depictions in DepictionVehicles.ndf"""
    
    ndf_file = "DepictionVehicles.ndf"
    dic_length = len(dics_list)
    
    unit_list_index = 0
    while unit_list_index < dic_length:
        
        valid_files = dics_list[unit_list_index]["valid_files"]
        if ndf_file not in valid_files:
            unit_list_index += 1
            continue
        
        unit_name = dics_list[unit_list_index]["unit_name"]
        unit_edits = dics_list[unit_list_index]["DepictionVehicles_ndf"]
        
        for key, edits in unit_edits.items():
            if isinstance(key, tuple):
                namespace, obj_type = key
                if "copy" in edits:
                    
                    if namespace.startswith("DepictionOperator_"):
                        new_entry = source_path.by_n(namespace).copy()
                        new_entry.namespace = edits["copy"]
                        new_entry = _handle_weapon_operator(unit_name, new_entry, edits, True)
                        match = re.search(r'(\d+)$', edits["copy"])
                        if match:
                            index_addition = int(match.group(1))
                            row_index = source_path.by_n(namespace).index + (index_addition - 1)
                            source_path.insert(row_index, new_entry)
                            logger.info(f"Inserted new weapon operator for {unit_name} at index {row_index}")
                            unit_list_index += 1
                    
                    elif namespace.startswith("Gfx_"):
                        new_entry = source_path.by_n(namespace).copy()
                        new_entry.namespace = edits["copy"]
                        new_entry = _handle_vehicle_depiction(unit_name, new_entry, edits, True)
                        unit_list_index += 1
            else:
                logger.error(f"Key is not a tuple: {key}")
                continue
            
            if "copy" not in edits:
                if namespace != None and namespace.startswith("DepictionOperator_"):
                    logger.debug(f"Editing weapon operator for {unit_name}")
                    weapon_operator = source_path.by_n(namespace)
                    weapon_operator = _handle_weapon_operator(unit_name, weapon_operator, edits)
                    unit_list_index += 1
                    
                elif namespace != None and namespace.startswith("Gfx_"):
                    logger.debug(f"Editing vehicle depiction for {unit_name}")
                    vehicle_depiction = source_path.by_n(namespace)
                    _handle_vehicle_depiction(unit_name, vehicle_depiction, edits)
                    unit_list_index += 1
                
                else:
                    logger.warning(f"Skipping {unit_name} because {namespace} is not a valid namespace")
            
        # if "copy" in edits:
        #     source_path.insert(row_index, weapon_operator)
        #     logger.info(f"Inserted new vehicle depiction for {unit_name} at index {row_index}")
        #     unit_list_index += 1
        
        # else:
            # unit_list_index += 1

def _handle_weapon_operator(unit_name, weapon_operator, edits, is_new_entry=False):
    for row_name_or_type, value in edits.items():
        if row_name_or_type == "copy":
            continue
        
        member_access = weapon_operator.v.by_m(row_name_or_type)           
        if row_name_or_type == "FireEffectTag":
            member_access.v = value
        elif row_name_or_type == "WeaponShootDataPropertyName":
            member_access.v = "[" + ",".join(value) + "]"
        
    return weapon_operator
                
def _handle_vehicle_depiction(unit_name, vehicle_depiction, edits, is_new_entry=False):
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


