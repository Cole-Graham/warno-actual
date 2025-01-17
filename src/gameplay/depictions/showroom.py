"""Showroom unit editing."""
from typing import Any, Dict

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_showroom_units(source_path: Any) -> None:
    """Edit showroom units."""
    unit_edits = load_unit_edits()
    
    logger.info("Editing ShowRoomUnits.ndf")
    
    for unit_descr in source_path:
        if not hasattr(unit_descr, 'namespace'):
            continue
            
        # Get unit name without prefix
        unit_name = unit_descr.namespace.removeprefix("Descriptor_ShowRoomUnit_")
        if unit_name not in unit_edits:
            continue
            
        edits = unit_edits[unit_name]
        try:
            _apply_unit_edits(unit_descr, edits)
        except Exception as e:
            logger.error(f"Failed to edit showroom unit {unit_name}: {str(e)}")

def _apply_unit_edits(unit_descr: Any, edits: Dict) -> None:
    """Apply edits to a showroom unit descriptor."""
    modules_list = unit_descr.v.by_m("ModulesDescriptors").v
    unit_name = unit_descr.namespace.removeprefix("Descriptor_ShowRoomUnit_")
    
    for module in modules_list:
        if not isinstance(module.v, ndf.model.Object):
            continue
            
        try:
            if module.v.type == "TInfantrySquadModuleDescriptor":
                _update_squad_strength(module, edits, unit_name)
                    
            elif module.v.type == "TInfantrySquadWeaponAssignmentModuleDescriptor":
                _update_weapon_assignment(module, edits, unit_name)
                
        except Exception as e:
            logger.error(f"Failed to update module {module.v.type} for {unit_name}: {str(e)}")

def _update_squad_strength(module: Any, edits: Dict, unit_name: str) -> None:
    """Update infantry squad strength."""
    if "WeaponAssignment" in edits and "Strength" in edits:
        try:
            module.v.by_m("NbSoldatInGroupeCombat").v = edits["Strength"]
            logger.info(f"Updated strength for {unit_name} to {edits['Strength']}")
        except Exception as e:
            logger.error(f"Failed to update strength for {unit_name}: {str(e)}")

def _update_weapon_assignment(module: Any, edits: Dict, unit_name: str) -> None:
    """Update infantry weapon assignments."""
    if "WeaponAssignment" not in edits:
        return
        
    try:
        module.v.by_m("InitialSoldiersToTurretIndexMap").v = f"MAP{edits['WeaponAssignment']}"
        logger.info(f"Updated weapon assignment for {unit_name}")
    except Exception as e:
        logger.error(f"Failed to update weapon assignment for {unit_name}: {str(e)}") 