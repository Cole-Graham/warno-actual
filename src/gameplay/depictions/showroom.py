"""Showroom unit editing."""

from typing import Any, Dict

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger('showroom_edits')

def edit_showroom_units(source: Any, unit_db: Dict[str, Any]) -> None:
    """Edit showroom unit descriptors."""
    logger.info("Editing showroom units")
    
    unit_edits = load_unit_edits()
    for unit_descr in source:
        if not hasattr(unit_descr, 'namespace'):
            continue
            
        unit_name = unit_descr.namespace.replace("Descriptor_ShowRoomUnit_", "")
        if unit_name not in unit_edits:
            continue
            
        edits = unit_edits[unit_name]
        _apply_showroom_edits(unit_descr, edits)

def _apply_showroom_edits(unit_descr: Any, edits: Dict) -> None:
    """Apply edits to a showroom unit."""
    modules_list = unit_descr.v.by_m("ModulesDescriptors").v
    
    for module in modules_list:
        if not isinstance(module.v, ndf.model.Object):
            continue
            
        if module.v.type == "TInfantrySquadModuleDescriptor":
            if "WeaponAssignment" in edits and "Strength" in edits:
                module.v.by_m("NbSoldatInGroupeCombat").v = edits["Strength"]
                logger.debug(f"Updated strength for {unit_descr.namespace}")
                
        elif module.v.type == "TInfantrySquadWeaponAssignmentModuleDescriptor":
            if "WeaponAssignment" in edits:
                module.v.by_m("InitialSoldiersToTurretIndexMap").v = f"MAP{edits['WeaponAssignment']}"
                logger.info(f"Updated weapon assignment for {unit_descr.namespace}") 