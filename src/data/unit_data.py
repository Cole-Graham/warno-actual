import re
from pathlib import Path
from typing import Any, Dict, List

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import (
    get_module_list,
    get_module_value,
    get_resource_value,
    is_obj_type,
    is_valid_turret,
    strip_quotes,
)

logger = setup_logger('unit_data')

def gather_unit_data(source_path: Path, dest_path: Path) -> Dict[str, Any]:
    """Gather unit data from UniteDescriptor.ndf."""
    logger.info("Gathering unit data from UniteDescriptor.ndf")
    logger.info(f"Source path: {source_path}")
    logger.info(f"Destination path: {dest_path}")
    
    unit_data = {}
    file_path = "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf"
    
    try:
        # Create mod instance with configured paths
        mod = ndf.Mod(source_path, dest_path)
        source = mod.parse_src(file_path)
        
        for unit_row in source:
            # Skip non-unit entries
            if not hasattr(unit_row, 'namespace'):
                continue
                
            # Get unit name without prefix
            unit_name = unit_row.namespace.replace("Descriptor_Unit_", "")
            
            # Extract unit data
            unit_info = extract_unit_info(unit_row)
            if unit_info:
                unit_data[unit_name] = unit_info
                logger.debug(f"Gathered data for unit: {unit_name}")
            else:
                logger.debug(f"No data gathered for unit: {unit_name}")
    
    except Exception as e:
        logger.error(f"Error gathering unit data: {str(e)}")
        raise
    
    logger.info(f"Gathered data for {len(unit_data)} units")
    if not unit_data:
        logger.warning("No unit data was gathered!")
    
    return unit_data

def extract_unit_info(unit_row: Any) -> Dict[str, Any]:
    """Extract relevant information from a unit row.
    
    Returns:
        Dict with:
            command_points (int): Cost in command points
            tags (List[str]): List of unit tags
            specialties (List[str]): List of unit specialties
    """
    unit_info = {}
    
    try:
        modules_list = unit_row.v.by_m("ModulesDescriptors").v
        
        for descr_row in modules_list:
            if not isinstance(descr_row.v, ndf.model.Object):
                continue
                
            module_type = descr_row.v.type
            
            # Extract data based on module type
            if module_type == "TProductionModuleDescriptor":
                unit_info.update(extract_production_data(descr_row))
            elif module_type == "TTagsModuleDescriptor":
                unit_info.update(extract_tags_data(descr_row))
            elif module_type == "TUnitUIModuleDescriptor":
                unit_info.update(extract_ui_data(descr_row))
    
    except Exception as e:
        logger.error(f"Error extracting data for {unit_row.namespace}: {str(e)}")
        return {}
    
    return unit_info

def extract_production_data(descr_row: Any) -> Dict[str, Any]:
    """Extract production-related data (command points, etc.)."""
    data = {}
    try:
        resources = get_module_value(descr_row, "ProductionRessourcesNeeded", None)
        if resources:
            cmd_points = get_resource_value(resources, "$/GFX/Resources/Resource_CommandPoints")
            if cmd_points:
                data["command_points"] = int(cmd_points)
    except Exception as e:
        logger.warning(f"Failed to extract production data: {str(e)}")
    return data

def extract_tags_data(descr_row: Any) -> Dict[str, Any]:
    """Extract unit tags data."""
    data = {}
    try:
        tagset = get_module_list(descr_row, "TagSet")
        data["tags"] = [strip_quotes(tag.v) for tag in tagset]
    except Exception as e:
        logger.warning(f"Failed to extract tags data: {str(e)}")
    return data

def extract_ui_data(descr_row: Any) -> Dict[str, Any]:
    """Extract UI-related data (specialties, etc.)."""
    data = {}
    try:
        specialties = get_module_list(descr_row, "SpecialtiesList")
        if specialties:
            data["specialties"] = [strip_quotes(spec.v) for spec in specialties]
    except Exception as e:
        logger.warning(f"Failed to extract UI data: {str(e)}")
    return data

def gather_weapon_data(base_path: Path) -> Dict[str, Any]:
    """Gather weapon data from WeaponDescriptor.ndf."""
    logger.info("Gathering weapon data")
    weapon_data = {}
    
    file_path = "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf"
    logger.debug(f"Reading weapon data from: {base_path / file_path}")
    
    try:
        # Create mod instance with configured paths
        mod = ndf.Mod(base_path, base_path)  # Use same path for source and dest
        source = mod.parse_src(file_path)
        
        weapon_count = 0
        for weapon_descr in source:
            weapon_count += 1
            if not hasattr(weapon_descr, 'namespace'):
                logger.debug("Found entry without namespace")
                continue
                
            weapon_name = weapon_descr.namespace
            if not weapon_name.startswith("WeaponDescriptor_"):
                logger.debug(f"Skipping non-weapon entry: {weapon_name}")
                continue
                
            logger.debug(f"Processing weapon: {weapon_name}")
            try:
                turret_data = _gather_turret_data(weapon_descr)
                salvo_data = _gather_salvo_data(weapon_descr)
                location_data = _gather_weapon_locations(weapon_descr)
                index_data = _gather_weapon_indices(weapon_descr)
                mapping_data = _gather_salvo_mapping(weapon_descr)
                
                if any([turret_data, salvo_data, location_data, index_data, mapping_data]):
                    weapon_data[weapon_name] = {
                        'turrets': turret_data,
                        'salvos': salvo_data,
                        'weapon_locations': location_data,
                        'weapon_indices': index_data,
                        'salvo_mapping': mapping_data
                    }
                    logger.debug(f"Added data for {weapon_name}")
                else:
                    logger.warning(f"No data gathered for {weapon_name}")
                    
            except Exception as e:
                logger.error(f"Failed to gather data for {weapon_name}: {str(e)}")
                continue
        
        logger.debug(f"Processed {weapon_count} entries in file")
        
    except Exception as e:
        logger.error(f"Failed to parse weapon file: {str(e)}")
        return weapon_data
    
    logger.info(f"Gathered data for {len(weapon_data)} weapons")
    return weapon_data

def _gather_turret_data(weapon_descr: Any) -> Dict[str, Any]:
    """Gather turret and weapon data from a weapon descriptor."""
    turret_data = {}
    
    try:
        turret_list = weapon_descr.v.by_member("TurretDescriptorList").v
    except Exception:
        logger.warning(f"No TurretDescriptorList found in {weapon_descr.namespace}")
        return turret_data
        
    for turret in turret_list:
        if not is_valid_turret(turret.v):
            continue
            
        try:
            yul_bone = int(turret.v.by_m("YulBoneOrdinal").v)
            turret_data[yul_bone] = {
                'weapons': _gather_mounted_weapons(turret)
            }
        except Exception as e:
            logger.warning(f"Failed to gather data for turret in {weapon_descr.namespace}: {str(e)}")
            continue
    
    return turret_data

def _gather_mounted_weapons(turret: Any) -> Dict[str, Any]:
    """Gather mounted weapon data from a turret."""
    weapon_data = {}
    
    try:
        mounted_wpns = turret.v.by_m("MountedWeaponDescriptorList").v
    except Exception:
        logger.warning("No MountedWeaponDescriptorList found")
        return weapon_data
        
    for weapon in mounted_wpns:
        if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
            continue
            
        try:
            ammo_val = weapon.v.by_m("Ammunition").v
            if not ammo_val.startswith("$/GFX/Weapon/Ammo_"):
                continue
                
            ammo_name = ammo_val.split("$/GFX/Weapon/Ammo_", 1)[1]
            weapon_data[ammo_name] = {
                'salvo_index': int(weapon.v.by_m("SalvoStockIndex").v),
                'quantity': _get_weapon_quantity(ammo_name)
            }
        except Exception as e:
            logger.warning(f"Failed to gather data for weapon: {str(e)}")
            continue
    
    return weapon_data

def _gather_salvo_data(weapon_descr: Any) -> List[str]:
    """Gather salvo data from a weapon descriptor."""
    try:
        salves_list = weapon_descr.v.by_m("Salves").v
        return [str(salvo.v) for salvo in salves_list]
    except Exception:
        logger.warning(f"Failed to gather salvo data for {weapon_descr.namespace}")
        return []

def _get_weapon_quantity(ammo_name: str) -> int:
    """Extract quantity from weapon name if present."""
    pattern = r".*?_x(\d+)$"
    match = re.match(pattern, ammo_name)
    return int(match.group(1)) if match else 1 

def _gather_weapon_indices(weapon_descr: Any) -> Dict[str, List[int]]:
    """Pre-compute weapon to salvo index mapping."""
    weapon_indices = {}
    
    for turret in weapon_descr.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(turret.v):
            continue
            
        for weapon in turret.v.by_m("MountedWeaponDescriptorList").v:
            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                continue
                
            ammo = weapon.v.by_m("Ammunition").v.split("$/GFX/Weapon/Ammo_", 1)[1]
            base_name = ammo.split('_x', 1)[0]
            
            if base_name not in weapon_indices:
                weapon_indices[base_name] = []
                
            weapon_indices[base_name].append(int(weapon.v.by_m("SalvoStockIndex").v))
    
    return weapon_indices

def _gather_salvo_mapping(weapon_descr: Any) -> Dict[str, str]:
    """Pre-compute weapon to salvo mapping."""
    salvo_mapping = {}
    
    for turret in weapon_descr.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(turret.v):
            continue
            
        for weapon in turret.v.by_m("MountedWeaponDescriptorList").v:
            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                continue
                
            ammo = weapon.v.by_m("Ammunition").v.split("$/GFX/Weapon/Ammo_", 1)[1]
            base_name = ammo.split('_x', 1)[0]
            index = weapon.v.by_m("SalvoStockIndex").v
            salvo_mapping[base_name] = index
    
    return salvo_mapping 

def _gather_weapon_locations(weapon_descr: Any) -> Dict[str, List[Dict[str, Any]]]:
    """Gather locations of all weapons in the descriptor."""
    weapon_locations = {}
    
    for turret in weapon_descr.v.by_member("TurretDescriptorList").v:
        if not is_valid_turret(turret.v):
            continue
            
        yul_bone = int(turret.v.by_m("YulBoneOrdinal").v)
        
        for weapon in turret.v.by_m("MountedWeaponDescriptorList").v:
            if not is_obj_type(weapon.v, "TMountedWeaponDescriptor"):
                continue
                
            ammo = weapon.v.by_m("Ammunition").v.split("$/GFX/Weapon/Ammo_", 1)[1]
            base_name = ammo.split('_x', 1)[0]
            
            if base_name not in weapon_locations:
                weapon_locations[base_name] = []
                
            weapon_locations[base_name].append({
                'turret_index': yul_bone,
                'salvo_index': int(weapon.v.by_m("SalvoStockIndex").v)
            })
    
    return weapon_locations 