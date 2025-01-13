"""Build MG weapon categories from game data."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


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