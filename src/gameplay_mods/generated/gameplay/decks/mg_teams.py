# import re
from typing import Any, Dict, List, Tuple

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import get_modules_list, is_obj_type  # noqa

logger = setup_logger('division_mg_teams')


def is_para_unit(unit_name: str, unit_db: Dict[str, Any]) -> bool:
    """Check if a unit has the para specialty."""
    unit_data = unit_db.get(unit_name)
    if not unit_data or 'specialties' not in unit_data:
        return False
    return any('para' in specialty.lower() for specialty in unit_data['specialties'])


def mg_team_division_rules(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Edit machine gun team availability in DivisionRules.ndf"""
    logger.info("Editing MG team availability")
    
    unit_db = game_db["unit_data"]
    mgs: List[Tuple[str, str]] = [
        ("M2HB", "HMG"), ("NSV", "HMG"), 
        ("M60", "MMG"), ("MAG", "MMG"),
        ("AANF1", "MMG"), ("MG3", "MMG"), 
        ("PKM", "MMG")
    ]
    
    for deck_descr in source_path:
        rules_list = deck_descr.v.by_m("UnitRuleList").v
        div_name = deck_descr.n[len("Descriptor_Deck_Division_"):-len("_Rule")]
        
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
                
                # apply availability settings
                xp_multi = str([0.0, 1.0, 0.75, 0.0] if is_para else [1.0, 0.75, 0.0, 0.0])

                rule_obj.v.by_m("NumberOfUnitInPack").v = '9' if mg_type == "HMG" else '12'
                rule_obj.v.by_m("NumberOfUnitInPackXPMultiplier").v = xp_multi
                
                logger.debug(f"Updated {unit_name} in {div_name} (Para: {is_para}, Type: {mg_type})")
