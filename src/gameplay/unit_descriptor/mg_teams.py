import re
from typing import Any, Dict, List, Tuple

import ndf_parse as ndf

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import get_modules_list, is_obj_type  # noqa

logger = setup_logger('mg_teams')


def edit_mg_teams(source: Any, game_db: Dict[str, Any]) -> None:
    """Edit machine gun team units in UniteDescriptor.ndf"""
    logger.info("Editing machine gun teams")
    
    unit_db = game_db.get("unit_data")
    
    mgs: List[Tuple[str, str]] = [
        ("M2HB", "HMG"), ("NSV", "HMG"), 
        ("M60", "MMG"), ("MAG", "MMG"),
        ("AANF1", "MMG"), ("MG3", "MMG"), 
        ("PKM", "MMG"), ("Mk19", "Mk19")
    ]
    
    for unit_row in source:
        if not hasattr(unit_row, 'namespace'):
            continue
            
        for name, mg_type in mgs:
            pattern = re.compile(rf'^Descriptor_Unit_HMGteam_{name}.*')
            if not pattern.match(unit_row.namespace):
                continue
                
            # Get unit name without prefix for database lookup
            unit_name = unit_row.namespace.replace("Descriptor_Unit_", "")
            is_para = _is_para_unit(unit_name, unit_db)
            
            # Get and apply stats
            stats = _get_mg_stats(mg_type, is_para)
            _update_mg_team(unit_row.v, stats)
            
            logger.debug(f"Updated {unit_name} (Para: {is_para}, Type: {mg_type})") 


def _is_para_unit(unit_name: str, unit_db: Dict[str, Any]) -> bool:
    """Check if a unit has the para specialty."""
    unit_data = unit_db.get(unit_name)
    if not unit_data or 'specialties' not in unit_data:
        return False
    return any('_para' in specialty.lower() for specialty in unit_data['specialties'])


def _get_mg_stats(mg_type: str, is_para: bool) -> Dict[str, Any]:
    """Get stats for a machine gun team based on type and para status."""
    is_heavy = mg_type in ("HMG", "Mk19")
    
    return {
        'cost': 30 if mg_type == "Mk19" else 25 if is_heavy else 15,
        'damage': "5" if is_heavy else "4",
        'soldiers': "5" if is_heavy else "4",
        'speed': "14" if is_heavy else "26",
        'specialty': "'infantry_equip_veryheavy'" if is_heavy else "'infantry_equip_light'"
    }


def _update_mg_team(unit_row: Any, stats: Dict[str, Any]) -> None:
    """Update a machine gun team's stats."""
    modules_list = get_modules_list(unit_row, "ModulesDescriptors")
    
    for module in modules_list.v:  # noqa
        if not isinstance(module.v, ndf.model.Object):
            continue
            
        module_type = module.v.type
        
        if module_type == "TBaseDamageModuleDescriptor":
            module.v.by_m("MaxPhysicalDamages").v = str(stats['damage'])
            
        elif module.namespace == "GroupeCombat":
            module.v.by_m("Default").v.by_m("NbSoldatInGroupeCombat").v = str(stats['soldiers'])  # noqa
            
        elif module.namespace == "GenericMovement":
            module.v.by_m("Default").v.by_m("MaxSpeedInKmph").v = str(stats['speed'])  # noqa
        
        elif module_type == "TProductionModuleDescriptor":
            resources = module.v.by_m("ProductionRessourcesNeeded").v
            resources.by_k("$/GFX/Resources/Resource_CommandPoints").v = str(stats['cost'])  # noqa
        
        # elif module_type == "TTacticalLabelModuleDescriptor":
        #     module.v.by_m("NbSoldiers").v = str(stats['soldiers'])
            
        elif module_type == "TUnitUIModuleDescriptor":
            specialties = module.v.by_m("SpecialtiesList")
            specialties.v.add(stats['specialty'])
