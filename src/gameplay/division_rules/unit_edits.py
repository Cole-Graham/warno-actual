from typing import Any, Dict, List

from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type  # noqa

logger = setup_logger(__name__)


def unit_edits_divisionrules(source_path: Any) -> None:
    """Apply unit edits to DivisionRules.ndf"""
    logger.info("Applying unit edits to divisions")
    
    unit_edits = load_unit_edits()
    
    for unit, edits in unit_edits.items():
        if "Divisions" in edits:
            _handle_division_changes(source_path, unit, edits)
            
        _update_existing_units(source_path, unit, edits)


def _handle_division_changes(source_path: Any, unit: str, edits: Dict) -> None:
    """Handle adding/removing units from divisions."""
    if "remove" in edits["Divisions"]:
        _remove_from_divisions(source_path, unit, edits["Divisions"]["remove"])
        
    if "add" in edits["Divisions"]:
        _add_to_divisions(source_path, unit, edits)


def _remove_from_divisions(source_path: Any, unit: str, divisions: List[str]) -> None:
    """Remove a unit from specified divisions."""
    for deck_descr in source_path:
        for division in divisions:
            if deck_descr.n != f"Descriptor_Deck_Division_{division}_multi_Rule":
                continue
            unit_rule_list = deck_descr.v.by_m("UnitRuleList")
            unit_descr = f"$/GFX/Unit/Descriptor_Unit_{unit}"
            
            for rule_obj in unit_rule_list.v:  
                if rule_obj.v.by_m("UnitDescriptor").v == unit_descr:
                    logger.debug(f"Removing {unit} from {division}")
                    unit_rule_list.v.remove(rule_obj.index)
                    break


def _add_to_divisions(source_path: Any, unit: str, edits: Dict) -> None:
    """Add a unit to specified divisions."""
    for deck_descr in source_path:
        for division in edits["Divisions"]["add"]:
            if deck_descr.n != f"Descriptor_Deck_Division_{division}_multi_Rule":
                continue
                
            # Build transport list if needed
            transport_str = _build_transport_list(division, edits)
            
            # get cards for division or default card count
            cards = edits["Divisions"].get(division, {}).get("cards", edits["Divisions"].get("default", {}).get("cards"))

            # Create new rule entry
            new_entry = _create_rule_entry(
                unit=unit,
                edits=edits,
                transport_str=transport_str,
                cards=cards
            )
            # Add to division
            logger.debug(f"Adding {unit} to {division}")
            deck_descr.v.by_m("UnitRuleList").v.add(new_entry)


def _build_transport_list(division_name: str, edits: Dict) -> str:
    """Build transport list string for a unit."""
    if not edits["Divisions"].get("is_transported", False):
        return ""
        
    # Get transports for specific division or use default
    transports = (edits["Divisions"].get(division_name, {}).get("Transports") or 
                 edits["Divisions"].get("default", {}).get("Transports", None))
    if transports is None:
        raise ValueError("Failed to retrieve transport list")
    
    # Add prefix to each transport
    prefixed = [f"$/GFX/Unit/Descriptor_Unit_{t}" for t in transports]
    return "[" + ", ".join(prefixed) + "]"


def _create_rule_entry(unit: str, edits: Dict, transport_str: str = "", cards: int = 0) -> str:
    """Create a division rule entry string."""

    base_entry = (
        f"TDeckUniteRule("
        f"    UnitDescriptor = $/GFX/Unit/Descriptor_Unit_{unit}"
        f"    AvailableWithoutTransport = {not edits['Divisions'].get('needs_transport', False)}"
    )
    
    if transport_str:
        base_entry += f"\n    AvailableTransportList = {transport_str}"

    base_avail = max(edits["availability"])
    xp_multi_str = str([i / base_avail for i in edits["availability"]])

    base_entry += (
        f"\n    MaxPackNumber = {cards}"
        f"\n    NumberOfUnitInPack = {base_avail}"
        f"\n    NumberOfUnitInPackXPMultiplier = {xp_multi_str}"
        f"\n),"
    )
    
    return base_entry


def _update_existing_units(source_path: Any, unit: str, edits: Dict) -> None:
    """Update existing unit entries in divisions."""
    unit_descr = f"$/GFX/Unit/Descriptor_Unit_{unit}"
    
    for deck_descr in source_path:
        if not deck_descr.n.endswith("multi_Rule"):
            continue
        div_name = deck_descr.n[len("Descriptor_Deck_Division_"):-len("_multi_Rule")]
        unit_rule_list = deck_descr.v.by_m("UnitRuleList").v
    
        for rule_obj in unit_rule_list:                    
            # Update FOB availability
            if rule_obj.v.by_m("UnitDescriptor").v.startswith("$/GFX/Unit/Descriptor_Unit_FOB"):
                rule_obj.v.by_m("NumberOfUnitInPack").v = "2"
                continue
                
            # Skip if not our target unit
            if rule_obj.v.by_m("UnitDescriptor").v != unit_descr:
                continue
            
            # add_transport_module = "UnloadFromTransport" in edits.get("orders", {}).get("add_orders", [])
            # if add_transport_module:
            #     unit_rule_list.remove(rule_obj.index)
            #     logger.debug(f"Removing {unit} from {div_name} because its now a transport unit")
            #     break
                
            logger.debug(f"Updating {unit} in {div_name}")
            _apply_unit_updates(rule_obj.v, unit, div_name, edits)


def _apply_unit_updates(rule: Any, unit: str, div_name: str, edits: Dict) -> None:
    """Apply updates to a unit rule."""

    if "availability" in edits:
        base_avail = max(edits["availability"])
        xp_multi = str([i / base_avail for i in edits["availability"]])
        logger.debug(f"Setting {unit} availability to {base_avail}")
        rule.by_m("NumberOfUnitInPack").v = base_avail
        logger.debug(f"Setting {unit} XP multiplier to {xp_multi}")
        rule.by_m("NumberOfUnitInPackXPMultiplier").v = xp_multi
        
    if "Divisions" in edits:
        _update_cards(rule, unit, div_name, edits)
        _update_transports(rule, unit, div_name, edits)


def _update_cards(rule: Any, unit: str, div_name: str, edits: Dict) -> None:
    """Update card count for a unit."""
    # First check for division-specific cards
    div_cards = edits["Divisions"].get(div_name, {}).get("cards")
    if div_cards is not None:
        logger.debug(f"Setting {unit} cards to {div_cards} (division-specific)")
        rule.by_m("MaxPackNumber").v = str(div_cards)
        return
        
    # Fall back to default cards if they exist
    if "default" in edits["Divisions"] and "cards" in edits["Divisions"]["default"]:
        default_cards = edits["Divisions"]["default"]["cards"]
        logger.debug(f"Setting {unit} cards to {default_cards} (default)")
        rule.by_m("MaxPackNumber").v = str(default_cards)


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
    for unit, edits in supply_unit_edits.items():
        if "Divisions" in edits:
            _handle_division_changes(source_path, unit, edits)
            
        _update_existing_units(source_path, unit, edits)
