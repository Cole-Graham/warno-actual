from typing import Any, Dict, List

from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def unit_edits_divisionrules(source_path: Any) -> None:
    """Apply unit edits to DivisionRules.ndf"""
    logger.info("Applying unit edits to divisions")
    
    unit_edits = load_unit_edits()
    division_rules = source_path.by_n("DivisionRules").v.by_member("DivisionRules").v
    
    for unit, edits in unit_edits.items():
        if "Divisions" in edits:
            _handle_division_changes(division_rules, unit, edits)
            
        _update_existing_units(division_rules, unit, edits)

def _handle_division_changes(division_rules: Any, unit: str, edits: Dict) -> None:
    """Handle adding/removing units from divisions."""
    if "remove" in edits["Divisions"]:
        _remove_from_divisions(division_rules, unit, edits["Divisions"]["remove"])
        
    if "add" in edits["Divisions"]:
        _add_to_divisions(division_rules, unit, edits)

def _remove_from_divisions(division_rules: Any, unit: str, divisions: List[str]) -> None:
    """Remove a unit from specified divisions."""
    for division_name in divisions:
        div_key = f"~/Descriptor_Deck_Division_{division_name}_multi"
        
        for map_row in division_rules:
            if map_row.k != div_key:
                continue
                
            unit_rule_list = map_row.v.by_m("UnitRuleList")
            unit_descr = f"$/GFX/Unit/Descriptor_Unit_{unit}"
            
            for rule_obj in unit_rule_list.v:
                if not is_obj_type(rule_obj.v, None):
                    continue
                    
                if rule_obj.v.by_m("UnitDescriptor").v == unit_descr:
                    logger.debug(f"Removing {unit} from {division_name}")
                    unit_rule_list.v.remove(rule_obj.index)
                    break

def _add_to_divisions(division_rules: Any, unit: str, edits: Dict) -> None:
    """Add a unit to specified divisions."""
    for division_name in edits["Divisions"]["add"]:
        div_key = f"~/Descriptor_Deck_Division_{division_name}_multi"
        
        for map_row in division_rules:
            if map_row.k != div_key:
                continue
                
            # Build transport list if needed
            transport_str = _build_transport_list(division_name, edits)
            
            # Create new rule entry
            new_entry = _create_rule_entry(
                unit=unit,
                edits=edits,
                transport_str=transport_str
            )
            
            # Add to division
            logger.debug(f"Adding {unit} to {division_name}")
            map_row.v.by_m("UnitRuleList").v.add(new_entry)

def _build_transport_list(division_name: str, edits: Dict) -> str:
    """Build transport list string for a unit."""
    if not edits["Divisions"]["is_transported"]:
        return ""
        
    # Get transports for specific division or use default
    transports = (edits["Divisions"].get(division_name, {}).get("Transports") or 
                 edits["Divisions"]["default"]["Transports"])
    
    # Add prefix to each transport
    prefixed = [f"$/GFX/Unit/Descriptor_Unit_{t}" for t in transports]
    return "[" + ", ".join(prefixed) + "]"

def _create_rule_entry(unit: str, edits: Dict, transport_str: str = "") -> str:
    """Create a division rule entry string."""
    base_entry = (
        f"TDeckUniteRule("
        f"    UnitDescriptor = $/GFX/Unit/Descriptor_Unit_{unit}"
        f"    AvailableWithoutTransport = {not edits['Divisions']['needs_transport']}"
    )
    
    if transport_str:
        base_entry += f"\n    AvailableTransportList = {transport_str}"
        
    base_entry += (
        f"\n    NumberOfUnitInPack = {edits['availability']}"
        f"\n    NumberOfUnitInPackXPMultiplier = {edits['XPMultiplier']}"
        f"\n),"
    )
    
    return base_entry

def _update_existing_units(division_rules: Any, unit: str, edits: Dict) -> None:
    """Update existing unit entries in divisions."""
    unit_descr = f"$/GFX/Unit/Descriptor_Unit_{unit}"
    
    for map_row in division_rules:
        if not map_row.k.endswith("_multi"):
            continue
            
        div_name = map_row.k[len("~/Descriptor_Deck_Division_"):-len("_multi")]
        rules_list = map_row.v.by_m("UnitRuleList").v
        
        for rule_obj in rules_list:
            if not is_obj_type(rule_obj.v, "TDeckUniteRule"):
                continue
                
            # Update FOB availability
            if rule_obj.v.by_m("UnitDescriptor").v.startswith("$/GFX/Unit/Descriptor_Unit_FOB"):
                rule_obj.v.by_m("NumberOfUnitInPack").v = "2"
                continue
                
            # Skip if not our target unit
            if rule_obj.v.by_m("UnitDescriptor").v != unit_descr:
                continue
                
            logger.debug(f"Updating {unit} in {div_name}")
            _apply_unit_updates(rule_obj.v, unit, div_name, edits)

def _apply_unit_updates(rule: Any, unit: str, div_name: str, edits: Dict) -> None:
    """Apply updates to a unit rule."""
    if "availability" in edits:
        logger.debug(f"Setting {unit} availability to {edits['availability']}")
        rule.by_m("NumberOfUnitInPack").v = edits["availability"]
        
    if "XPMultiplier" in edits:
        logger.debug(f"Setting {unit} XP multiplier to {edits['XPMultiplier']}")
        rule.by_m("NumberOfUnitInPackXPMultiplier").v = str(edits["XPMultiplier"])
        
    if "Divisions" in edits:
        _update_transports(rule, unit, div_name, edits)

def _update_transports(rule: Any, unit: str, div_name: str, edits: Dict) -> None:
    """Update transport list for a unit."""
    # Check division-specific transports first, then fall back to default
    transports = (edits["Divisions"].get(div_name, {}).get("Transports") or 
                 edits["Divisions"].get("default", {}).get("Transports"))
    
    if transports:
        transport_str = "[" + ", ".join(f"$/GFX/Unit/Descriptor_Unit_{t}" for t in transports) + "]"
        logger.debug(f"Setting {unit} transports to {transports}")
        rule.by_m("AvailableTransportList").v = transport_str

def supply_divisionrules(source_path: Any) -> None:
    """Apply supply unit edits to DivisionRules.ndf"""

    logger.info("Applying supply unit edits to divisions")
    
    division_rules = source_path.by_n("DivisionRules").v.by_member("DivisionRules").v
    
    for unit, edits in supply_unit_edits.items():
        if "Divisions" in edits:
            _handle_division_changes(division_rules, unit, edits)
            
        _update_existing_units(division_rules, unit, edits)