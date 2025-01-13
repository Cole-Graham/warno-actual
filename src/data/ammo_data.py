"""Functions for building ammunition data from game files."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def build_ammo_data(source_files: dict) -> dict:
    """Build ammunition database from source files.
    
    Args:
        source_files: Dictionary of NDF file paths to their parsed contents
        
    Returns:
        Dictionary containing all ammunition-related data
    """
    ammo_file = source_files["GameData/Generated/Gameplay/Gfx/Ammunition.ndf"]
    unit_file = source_files["GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf"]
    
    return {
        "mg_categories": build_mg_categories(ammo_file),
        "mortar_categories": build_mortar_categories(ammo_file),
        "unit_categories": build_unit_categories(unit_file),
        "full_ball_weapons": build_full_ball_weapons(ammo_file),
        "sniper_weapons": build_sniper_weapons(ammo_file),
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