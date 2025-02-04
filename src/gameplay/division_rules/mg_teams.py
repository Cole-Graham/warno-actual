import re
from typing import Any, Dict, List, Tuple

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import get_modules_list, is_obj_type

logger = setup_logger('division_mg_teams')

def is_para_unit(unit_name: str, unit_db: Dict[str, Any]) -> bool:
    """Check if a unit has the para specialty."""
    unit_data = unit_db.get(unit_name)
    if not unit_data or 'specialties' not in unit_data:
        return False
    return any('para' in specialty.lower() for specialty in unit_data['specialties'])

def get_mg_availability(mg_type: str, is_para: bool) -> Dict[str, Any]:
    """Get availability settings for a machine gun team."""
    is_heavy = mg_type == "HMG"
    availability = 9 if is_heavy else 12
    
    if is_para:
        xp_multi = [0.0, 1.0, 0.75, 0.0]
    else:
        xp_multi = [1.0, 0.75, 0.0, 0.0]
    
    return {
        'availability': str(availability),
        'xp_multiplier': str(xp_multi)
    }

def mg_team_division_rules(source: Any, game_db: Dict[str, Any]) -> None:
    """Edit machine gun team availability in divisions."""
    logger.info("Editing MG team availability")
    
    unit_db = game_db["unit_data"]
    mgs: List[Tuple[str, str]] = [
        ("M2HB", "HMG"), ("NSV", "HMG"), 
        ("M60", "MMG"), ("MAG", "MMG"),
        ("AANF1", "MMG"), ("MG3", "MMG"), 
        ("PKM", "MMG")
    ]
    
    division_rules = source.by_n("DivisionRules").v.by_member("DivisionRules").v
    
    for map_row in division_rules:
        div_key = map_row.k
        rules_list = map_row.v.by_m("UnitRuleList").v
        
        for rule_obj in rules_list:
            if not is_obj_type(rule_obj.v, "TDeckUniteRule"):
                continue
                
            # Skip solo units
            if rule_obj.v.by_m("NumberOfUnitInPackXPMultiplier").v == "[1.0, 1.0, 1.0, 1.0]":
                continue
                
            unit_descr = rule_obj.v.by_m("UnitDescriptor").v
            
            for name, mg_type in mgs:
                unit_descr_name = unit_descr.split("$/GFX/Unit/", 1)[1]
                if not unit_descr_name.startswith(f"Descriptor_Unit_HMGteam_{name}"):
                    continue
                    
                # Get unit name without prefix for database lookup
                unit_name = unit_descr_name.replace("Descriptor_Unit_", "")
                is_para = is_para_unit(unit_name, unit_db)
                
                # Get and apply availability settings
                settings = get_mg_availability(mg_type, is_para)
                rule_obj.v.by_m("NumberOfUnitInPack").v = settings['availability']
                rule_obj.v.by_m("NumberOfUnitInPackXPMultiplier").v = settings['xp_multiplier']
                
                logger.debug(f"Updated {unit_name} in {div_key} (Para: {is_para}, Type: {mg_type})") 