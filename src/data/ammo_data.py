"""Functions for building ammunition data from game files."""

import re
from pathlib import Path
from typing import Any, Dict

from src import ndf
from src.constants.weapons.vanilla_inst_modifications import (
    AMMUNITION_RENAMES,
    AMMUNITION_MISSILES_RENAMES,
)
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_valid_turret

logger = setup_logger('ammo_data')


def get_vanilla_renames(mod: Any, ndf_path: Any) -> Dict[str, str]:
    """Get mapping of original weapon names to their new names.
    
    Args:
        parse_source: The parsed NDF data to process
        
    Returns:
        Dictionary mapping original names to renamed versions
    """
    renames = {}
    
    try:
        # Process renames from parsed source
        _process_renames(mod, ndf_path, renames)
            
        # Add static renames from ammunition and missiles modules
        for old_name, new_name in AMMUNITION_RENAMES:
            renames[old_name] = new_name
            
        for old_name, new_name in AMMUNITION_MISSILES_RENAMES:
            renames[old_name] = new_name
            
        return renames
        
    except Exception as e:
        logger.error(f"Error getting vanilla renames: {str(e)}")
        return {}


def _process_renames(mod: Any, ndf_path: Any, renames: Dict[str, str]) -> None:
    """Process renames from parsed NDF data."""
    # Build data for salvo weapon renames using same logic as build_salvo_weapons
    EXCLUDED_PREFIXES = ('Gatling', 'MMG', 'Pod')
    
    parse_source = mod.parse_src(ndf_path)

    for ammo_descr in parse_source:
        if not hasattr(ammo_descr, 'namespace'):
            continue
                
        name = ammo_descr.namespace.removeprefix('Ammo_')
        
        # Skip if name starts with any excluded prefix
        if any(name.startswith(prefix) for prefix in EXCLUDED_PREFIXES):
            continue
                
        match = re.match(r'^(.+)_x(\d+)$', name)
        if match:
            base_name = match.group(1)
            salvo_num = match.group(2)
            new_name = f"{base_name}_salvolength{salvo_num}"
            renames[name] = new_name


def build_ammo_data(mod_src_path: Path) -> Dict[str, Any]:
    """Build ammunition database from source files."""
    logger.info("Building ammunition database")
    
    ammo_data = {}
    ammo_path = "GameData/Generated/Gameplay/Gfx/Ammunition.ndf"
    ammo_missile_path = "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf"
    unit_path = "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf"
    weapon_descriptor_path = "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf"

    try:
        mod = ndf.Mod(mod_src_path, "None")
        ammo_file = mod.parse_src(ammo_path)
        ammo_missile_file = mod.parse_src(ammo_missile_path)
        unit_file = mod.parse_src(unit_path)
        weapon_descriptor_file = mod.parse_src(weapon_descriptor_path)

        # Merge salvo weapons and renames separately
        salvo_weapons = build_salvo_weapons(ammo_file)
        salvo_weapons.update(build_salvo_weapons(ammo_missile_file))
        
        renames = build_renames(ammo_file)
        renames.update(build_renames(ammo_missile_file))
        
        # Combine salvo weapons and renames
        renames_old_new = {**salvo_weapons, **renames}
        
        # Create reversed mapping
        renames_new_old = {v: k for k, v in renames_old_new.items()}
        
        return {
            "mg_categories": build_mg_categories(ammo_file),
            "mortar_categories": build_mortar_categories(ammo_file),
            "unit_categories": build_unit_categories(unit_file),
            "full_ball_weapons": build_full_ball_weapons(ammo_file),
            "sniper_weapons": build_sniper_weapons(ammo_file),
            "renames_old_new": renames_old_new,
            "renames_new_old": renames_new_old,
            "salves_map": build_ammo_salves_map(weapon_descriptor_file)
        }
        
    except Exception as e:
        logger.error(f"Error building ammunition database: {e}", exc_info=True)
        return {
            "mg_categories": {},
            "mortar_categories": {},
            "unit_categories": {},
            "full_ball_weapons": [],
            "sniper_weapons": [],
            "renames_old_new": {},
            "renames_new_old": {},
            "salves_map": {},
        }

def build_ammo_salves_map(parse_source) -> dict:
    """Build mapping of ammunition salves in WeaponDescriptor.ndf
    for ammunition.json (used for applying default salves during ammunition edits)"""
    salves_map = {}
    salves_list = []
    
    for weapon_descr in parse_source:
        salves_map[weapon_descr.n] = {}
        salves = weapon_descr.v.by_m("Salves")
        
        salves_list = []
        salves_list.extend(int(value.v) for value in salves.v)
        salves_map[weapon_descr.n]['salves_list'] = salves_list
        salves_map[weapon_descr.n]['salves'] = {}
            
        turret_list = weapon_descr.v.by_m("TurretDescriptorList")
        for turret in turret_list.v:
            if not is_valid_turret(turret.v):
                logger.warning(f"Invalid turret: {turret.v}")
                continue
            
            mounted_weapons = turret.v.by_m("MountedWeaponDescriptorList")
            for weapon in mounted_weapons.v:
                ammunition = weapon.v.by_m("Ammunition").v.split('_', 1)[1]
                salvo_stock_index = weapon.v.by_m("SalvoStockIndex").v
                salvos = salves.v[int(salvo_stock_index)].v
                
                data = [int(salvo_stock_index), int(salvos)]
                salves_map[weapon_descr.n]['salves'][ammunition] = data
    
    return salves_map

def build_mg_categories(parse_source) -> dict:
    """Build MG weapon categories from ammunition data.
    
    Args:
        source: Ammunition.ndf file
    
    Returns:
        Dictionary of MG weapon categories
    """
    hmg_teams = []
    mmg_teams = []
    hmg_turrets = []
    mmg_turrets = []
    
    for weapon_descr in parse_source:
        membr = weapon_descr.v.by_m
        
        # Get weapon characteristics
        is_rotary_cannon = membr("TypeCategoryName").v == "'ZJQCIJREVP'"
        is_rifle = membr("TypeCategoryName").v == "'MPRVLPMVZK'"
        is_inf_mmg = membr("TypeCategoryName").v == "'YSLEYULPVD'"
        is_battle_rifle = membr("TypeCategoryName").v == "'THRUBJLEUJ'"
        
        caliber = membr("Caliber").v
        traits_list = membr("TraitsToken").v
        
        # Check traits
        is_tripod = "'tripod'" in [t.v for t in traits_list]
        is_coax = "'coax'" in [t.v for t in traits_list]
        is_stabilized = membr("CanShootWhileMoving").v == "True"
        
        # Categorize weapon
        if is_tripod and not is_stabilized:
            if caliber == "'12_7mm'":
                hmg_teams.append(weapon_descr.n)
            elif caliber in ["'UZKJUPNFLB'", "'ARZDNMYCBF'"] and not (is_rifle or is_inf_mmg):
                mmg_teams.append(weapon_descr.n)
        else:
            if caliber == "'12_7mm'" and not is_rotary_cannon:
                if is_coax or is_stabilized:
                    hmg_turrets.append(weapon_descr.n)
            elif caliber in ["'UZKJUPNFLB'", "'ARZDNMYCBF'"] and not any([
                is_coax, is_rifle, is_inf_mmg, is_battle_rifle
            ]) and is_stabilized:
                mmg_turrets.append(weapon_descr.n)
    
    return {
        "hmg_teams": hmg_teams,
        "mmg_teams": mmg_teams,
        "hmg_turrets": hmg_turrets,
        "mmg_turrets": mmg_turrets,
        "hmg_exceptions": ["Ammo_HMG_team_12_7_mm_NSV_6U6"]
    } 


def build_mortar_categories(parse_source) -> dict:
    """Build mortar categories from ammunition data."""
    mortars = []
    smoke_mortars = []
    
    for weapon_descr in parse_source:
        name = weapon_descr.n
        if name.startswith("Mortier_"):
            if "_SMOKE" in name:
                smoke_mortars.append(name)
            else:
                mortars.append(name)
    
    return {
        "mortars": mortars,
        "smoke_mortars": smoke_mortars
    } 


def build_unit_categories(parse_source) -> dict:
    """Build unit categories from unit descriptors."""
    mortar_units = []
    
    for unit in parse_source:
        modules = unit.v.by_m("ModulesDescriptors").v
        for module in modules:
            if not hasattr(module.v, 'type'):
                continue
                
            if module.v.type == "TUnitUIModuleDescriptor":
                if module.v.by_m("MenuIconTexture").v == "'Texture_RTS_H_mortar'":
                    mortar_units.append(unit.n)
                    break
    
    return {
        "mortar_units": mortar_units
    } 


def build_full_ball_weapons(parse_source) -> list:
    """Build list of weapons that should use full ball damage."""
    full_ball = []
    
    for weapon in parse_source:
        if weapon.v.by_m("TypeCategoryName").v != "'GGSLNBFHEX'":
            if weapon.v.by_m("Caliber").v in ["'ARZDNMYCBF'", "'UZKJUPNFLB'"]:
                full_ball.append(weapon.n)
    
    return full_ball


def build_sniper_weapons(parse_source) -> list:
    """Build list of sniper weapons."""
    snipers = []
    
    for weapon in parse_source:
        if weapon.v.by_m("TypeCategoryName").v == "'GGSLNBFHEX'":
            snipers.append(weapon.n)
    
    return snipers 

def build_renames(parse_source) -> Dict[str, str]:
    """Build mapping of constants renames to their new names.
    
    Returns:
        Dict mapping original names to renamed versions
    """
    renames = {}
    
    for ammo_descr in parse_source:
        
        name = ammo_descr.namespace.removeprefix('Ammo_')
        
        for old_name, new_name in AMMUNITION_RENAMES:
            if old_name == name:
                renames[old_name] = new_name
    
        for old_name, new_name in AMMUNITION_MISSILES_RENAMES:
            if old_name == name:
                renames[old_name] = new_name
    
    return renames

def build_salvo_weapons(parse_source) -> Dict[str, str]:
    """Build mapping of vanilla salvo weapons to their new names.
    
    Returns:
        Dict mapping original names to salvolength names
    """
    salvo_weapons = {}
    
    # Prefixes to exclude from salvo renaming
    EXCLUDED_PREFIXES = ('Gatling', 'MMG', 'Pod')
    
    for weapon_descr in parse_source:
        if not hasattr(weapon_descr, 'namespace'):
            continue
            
        name = weapon_descr.namespace.removeprefix('Ammo_')
        
        # Skip if name starts with any excluded prefix
        if any(name.startswith(prefix) for prefix in EXCLUDED_PREFIXES):
            continue
            
        match = re.match(r'^(.+)_x(\d+)$', name)
        if match:
            base_name = match.group(1)
            salvo_num = match.group(2)
            new_name = f"{base_name}_salvolength{salvo_num}"
            salvo_weapons[name] = new_name
            
    logger.info(f"Found {len(salvo_weapons)} vanilla salvo weapons to rename")
    return salvo_weapons 