"""Functions for building ammunition data from game files."""

import re
from pathlib import Path
from typing import Any, Dict

from src import ndf
from src.gameplay.weapons.ammunition import AMMUNITION_RENAMES
from src.gameplay.weapons.missiles import AMMUNITION_MISSILES_RENAMES
from src.utils.logging_utils import setup_logger

logger = setup_logger('ammo_data')


def get_vanilla_renames(source_path: Path) -> Dict[str, str]:
    """Get mapping of original weapon names to their new names."""
    renames = {}
    
    try:
        mod = ndf.Mod(source_path, source_path)
        
        # Get renames from both ammunition files
        ammo_path = "GameData/Generated/Gameplay/Gfx/Ammunition.ndf"
        missiles_path = "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf"
        
        ammo_source = mod.parse_src(ammo_path)
        missiles_source = mod.parse_src(missiles_path)
        
        # Process regular ammo renames
        _process_renames(ammo_source, renames)
        # Process missile renames
        _process_renames(missiles_source, renames)
        
        # Add static renames from ammunition and missiles modules
        for old_name, new_name in AMMUNITION_RENAMES:
            renames[old_name] = new_name
            
        for old_name, new_name in AMMUNITION_MISSILES_RENAMES:
            renames[old_name] = new_name
            
        return renames
        
    except Exception as e:
        logger.error(f"Error getting vanilla renames: {str(e)}")
        return {}
        
def _process_renames(source: Any, renames: Dict[str, str]) -> None:
    """Process renames from a source file."""
    # Build salvo weapon renames using same logic as build_salvo_weapons
    EXCLUDED_PREFIXES = ('Gatling', 'MMG', 'Pod')
    
    for weapon_descr in source:
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
            renames[name] = new_name


def build_ammo_data(source_path: Path) -> Dict[str, Any]:
    """Build ammunition database from source files."""
    logger.info("Building ammunition database")
    
    ammo_data = {}
    ammo_path = "GameData/Generated/Gameplay/Gfx/Ammunition.ndf"
    ammo_missile_path = "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf"
    unit_path = "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf"
    
    try:
        mod = ndf.Mod(source_path, source_path)
        ammo_file = mod.parse_src(ammo_path)
        ammo_missile_file = mod.parse_src(ammo_missile_path)
        unit_file = mod.parse_src(unit_path)
        
        return {
            "mg_categories": build_mg_categories(ammo_file),
            "mortar_categories": build_mortar_categories(ammo_file),
            "unit_categories": build_unit_categories(unit_file),
            "full_ball_weapons": build_full_ball_weapons(ammo_file),
            "sniper_weapons": build_sniper_weapons(ammo_file),
            "salvo_weapons": {
                **build_salvo_weapons(ammo_file),  # Regular ammunition salvo weapons
                **build_salvo_weapons(ammo_missile_file)  # Missile salvo weapons
            },
        }
        
    except Exception as e:
        logger.error(f"Error building ammunition database: {e}", exc_info=True)
        return {
            "mg_categories": {},
            "mortar_categories": {},
            "unit_categories": {},
            "full_ball_weapons": [],
            "sniper_weapons": [],
            "salvo_weapons": {},
        }


def build_mg_categories(source) -> dict:
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
    
    for weapon_descr in source:
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


def build_mortar_categories(source) -> dict:
    """Build mortar categories from ammunition data."""
    mortars = []
    smoke_mortars = []
    
    for weapon_descr in source:
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


def build_unit_categories(source) -> dict:
    """Build unit categories from unit descriptors."""
    mortar_units = []
    
    for unit in source:
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


def build_full_ball_weapons(source) -> list:
    """Build list of weapons that should use full ball damage."""
    full_ball = []
    
    for weapon in source:
        if weapon.v.by_m("TypeCategoryName").v != "'GGSLNBFHEX'":
            if weapon.v.by_m("Caliber").v in ["'ARZDNMYCBF'", "'UZKJUPNFLB'"]:
                full_ball.append(weapon.n)
    
    return full_ball


def build_sniper_weapons(source) -> list:
    """Build list of sniper weapons."""
    snipers = []
    
    for weapon in source:
        if weapon.v.by_m("TypeCategoryName").v == "'GGSLNBFHEX'":
            snipers.append(weapon.n)
    
    return snipers 


def build_salvo_weapons(source: Any) -> Dict[str, str]:
    """Build mapping of vanilla salvo weapons to their new names.
    
    Returns:
        Dict mapping original names to salvolength names
    """
    salvo_weapons = {}
    
    # Prefixes to exclude from salvo renaming
    EXCLUDED_PREFIXES = ('Gatling', 'MMG', 'Pod')
    
    for weapon_descr in source:
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