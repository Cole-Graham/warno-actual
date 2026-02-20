from typing import Any, Dict, List, Optional, Tuple

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits
from src.constants.generated.gameplay.decks import load_new_divisions
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type, strip_quotes  # noqa

logger = setup_logger(__name__)


def edit_gen_gp_decks_divisionrules(source_path: Any, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Decks/DivisionRules.ndf"""
    _new_unit_division_rules(source_path)
    _unit_edits_divisionrules(source_path)
    _supply_divisionrules(source_path)
    _mg_team_division_rules(source_path, game_db)
    _create_national_division_rules(source_path, game_db)

def _unit_edits_divisionrules(source_path: Any) -> None:
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
            cards = (
                edits["Divisions"].get(division, {}).get("cards", edits["Divisions"].get("default", {}).get("cards"))
            )

            # Create new rule entry
            new_entry = _create_rule_entry(unit=unit, edits=edits, transport_str=transport_str, cards=cards)
            # Add to division
            logger.debug(f"Adding {unit} to {division}")
            deck_descr.v.by_m("UnitRuleList").v.add(new_entry)


def _build_transport_list(division_name: str, edits: Dict) -> str:
    """Build transport list string for a unit."""
    if not edits["Divisions"].get("is_transported", False):
        return ""

    # Get transports for specific division or use default
    transports = edits["Divisions"].get(division_name, {}).get("Transports") or edits["Divisions"].get(
        "default", {}
    ).get("Transports", None)
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
        div_name = deck_descr.n[len("Descriptor_Deck_Division_") : -len("_multi_Rule")]
        unit_rule_list = deck_descr.v.by_m("UnitRuleList").v

        for rule_obj in unit_rule_list:
            # Update FOB availability
            if rule_obj.v.by_m("UnitDescriptor").v.startswith("$/GFX/Unit/Descriptor_Unit_FOB"):
                rule_obj.v.by_m("NumberOfUnitInPack").v = "2"
                continue

            # Skip if not our target unit
            if rule_obj.v.by_m("UnitDescriptor").v != unit_descr:
                continue

            # add_transport_module = "EOrderType/UnloadFromTransport" in edits.get("orders", {}).get("add_orders", [])
            # if add_transport_module:
            #     unit_rule_list.remove(rule_obj.index)
            #     logger.debug(f"Removing {unit} from {div_name} because its now a transport unit")
            #     break

            logger.debug(f"Updating unit rules for {unit} in {div_name}")
            _apply_unit_updates(rule_obj.v, unit, div_name, edits)


def _apply_unit_updates(rule: Any, unit: str, div_name: str, edits: Dict) -> None:
    """Apply updates to a unit rule."""

    if "availability" in edits:
        base_avail = max(edits["availability"])
        # Format each value to the hundredth decimal place
        xp_multi = str([round(i / base_avail, 2) for i in edits["availability"]])
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
    transports = edits["Divisions"].get(div_name, {}).get("Transports") or edits["Divisions"].get("default", {}).get(
        "Transports"
    )

    if transports:
        transport_str = "[" + ", ".join(f"$/GFX/Unit/Descriptor_Unit_{t}" for t in transports) + "]"
        logger.debug(f"Setting {unit} transports to {transports}")
        rule.by_m("AvailableTransportList").v = transport_str


def _new_unit_division_rules(source_path: Any) -> None:
    """Add unit rules to DivisionRules.ndf."""
    logger.info("Adding unit rules to divisions")

    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits or "Divisions" not in edits:
            continue

        unit_name = edits["NewName"]

        for division, div_data in edits["Divisions"].items():
            if division == "default":
                continue

            division_obj_namespace = f"Descriptor_Deck_Division_{division}_Rule"
            transports = div_data.get("Transports", None)

            # Create transport list if available
            if transports is not None:
                transport_list = [f"$/GFX/Unit/Descriptor_Unit_{t}" for t in transports]
                transport_str = f"[{', '.join(transport_list)}]"

            base_avail = max(edits["availability"])
            xp_multi = str([round(i / base_avail, 2) for i in edits["availability"]])

            default_cards = edits["Divisions"]["default"]["cards"]
            cards = div_data.get("cards", default_cards)

            # Different entries for vehicles vs infantry/towed
            is_transportable = "EOrderType/Load" in edits.get("orders", [])
            is_vehicle_or_aerial = edits.get("is_ground_vehicle", False) or edits.get("is_aerial", False)
            is_towed = edits.get("is_ground_vehicle", False) and not edits.get("is_infantry", False)
            if not is_transportable:
                new_entry = (
                    f"TDeckUniteRule\n"
                    f"(\n"
                    f"    UnitDescriptor = $/GFX/Unit/Descriptor_Unit_{unit_name}\n"
                    f"    AvailableWithoutTransport = True\n"
                    f"    MaxPackNumber = {cards}\n"
                    f"    NumberOfUnitInPack = {base_avail}\n"
                    f"    NumberOfUnitInPackXPMultiplier = {xp_multi}\n"
                    f"),"
                )
            else:
                new_entry = (
                    f"TDeckUniteRule\n"
                    f"(\n"
                    f"    UnitDescriptor = $/GFX/Unit/Descriptor_Unit_{unit_name}\n"
                    f"    AvailableWithoutTransport = False\n"
                    f"    AvailableTransportList = {transport_str}\n"  # noqa
                    f"    MaxPackNumber = {cards}\n"
                    f"    NumberOfUnitInPack = {base_avail}\n"
                    f"    NumberOfUnitInPackXPMultiplier = {xp_multi}\n"
                    f"),"
                )

            # Add to division rules
            div_rules = source_path.by_n(division_obj_namespace).v.by_m("UnitRuleList")
            div_rules.v.add(new_entry)
            logger.info(f"Added rules for {unit_name} to {division}")

            # Handle unit replacements
            if edits.get("is_replacement", False):
                for i, unit_rule in enumerate(div_rules.v, start=0):
                    if unit_rule.v.by_m("UnitDescriptor").v == f"$/GFX/Unit/Descriptor_Unit_{donor}":
                        div_rules.v.remove(i)
                        logger.info(f"Removed old entry for {donor} from {division}")


def _supply_divisionrules(source_path: Any) -> None:
    """Apply supply unit edits to DivisionRules.ndf"""
    for unit, edits in supply_unit_edits.items():
        if "Divisions" in edits:
            _handle_division_changes(source_path, unit, edits)

        _update_existing_units(source_path, unit, edits)            
        

def _is_para_unit(unit_name: str, unit_db: Dict[str, Any]) -> bool:
    """Check if a unit has the para specialty."""
    unit_data = unit_db.get(unit_name)
    if not unit_data or 'specialties' not in unit_data:
        return False
    return any('para' in specialty.lower() for specialty in unit_data['specialties'])


def _mg_team_division_rules(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Edit machine gun team availability in DivisionRules.ndf"""
    logger.info("Editing MG team availability")
    
    unit_db = game_db["unit_data"]
    mgs: List[Tuple[str, str]] = [
        ("M2HB", "HMG"), ("NSV", "HMG"), 
        ("M60", "MMG"), ("MAG", "MMG"),
        ("AANF1", "MMG"), ("MG3", "MMG"), 
        ("PKM", "MMG"), ("L1A1", "HMG")
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
                is_para = _is_para_unit(unit_name, unit_db)
                
                # apply availability settings
                xp_multi = str([0.0, 1.0, 0.75, 0.0] if is_para else [1.0, 0.75, 0.0, 0.0])
                hmg_xp_multi = str([0.0, 1.0, 0.7, 0.0] if is_para else [1.0, 0.7, 0.0, 0.0])

                rule_obj.v.by_m("NumberOfUnitInPack").v = '10' if mg_type == "HMG" else '12'
                rule_obj.v.by_m("NumberOfUnitInPackXPMultiplier").v = hmg_xp_multi if mg_type == "HMG" else xp_multi
                
                logger.debug(f"Updated {unit_name} in {div_name} (Para: {is_para}, Type: {mg_type})")


def _serialize_unit_rule(rule_v: Any) -> str:
    """Serialize a TDeckUniteRule object to a string representation.
    
    Args:
        rule_v: The rule object (rule_obj.v from the list iteration)
    """
    # Extract values - they should already be strings when accessed via .v
    unit_descr = rule_v.by_m("UnitDescriptor").v
    available_without_transport = rule_v.by_m("AvailableWithoutTransport").v
    max_pack_number = rule_v.by_m("MaxPackNumber").v
    number_in_pack = rule_v.by_m("NumberOfUnitInPack").v
    xp_multiplier_raw = rule_v.by_m("NumberOfUnitInPackXPMultiplier").v
    
    # Handle XP multiplier - check if it's already a string or needs conversion
    if isinstance(xp_multiplier_raw, str):
        xp_multiplier = xp_multiplier_raw
    elif hasattr(xp_multiplier_raw, '__iter__') and not isinstance(xp_multiplier_raw, str):
        # Extract numeric values from list/ListRow objects
        xp_values = []
        for item in xp_multiplier_raw:
            # Try to get the actual value from ListRow objects
            if hasattr(item, 'value'):
                val = item.value
            elif hasattr(item, 'v'):
                val = item.v
            else:
                val = item
            # Strip quotes if it's a string, then convert
            if isinstance(val, str):
                val = strip_quotes(val)
            # Convert to string, handling floats properly
            if isinstance(val, float):
                xp_values.append(f"{val:.1f}" if val.is_integer() else str(val))
            elif isinstance(val, int):
                xp_values.append(str(val))
            else:
                # Try to convert to float first
                try:
                    float_val = float(val)
                    xp_values.append(f"{float_val:.1f}" if float_val.is_integer() else str(float_val))
                except (ValueError, TypeError):
                    xp_values.append(str(val))
        xp_multiplier = "[" + ", ".join(xp_values) + "]"
    else:
        xp_multiplier = str(xp_multiplier_raw)
    
    # Build the rule string
    rule_str = (
        f"TDeckUniteRule\n"
        f"(\n"
        f"    UnitDescriptor = {unit_descr}\n"
        f"    AvailableWithoutTransport = {available_without_transport}\n"
    )
    
    # Add transport list if present
    transport_list_member = rule_v.by_member("AvailableTransportList", False)
    if transport_list_member:
        transport_list_raw = transport_list_member.v
        
        # Handle transport list - check if it's already a string or needs conversion
        if isinstance(transport_list_raw, str):
            transport_list_str = transport_list_raw
        elif hasattr(transport_list_raw, '__iter__') and not isinstance(transport_list_raw, str):
            # Extract string values from list
            transport_values = []
            for item in transport_list_raw:
                # Try to get the actual value from ListRow objects
                if hasattr(item, 'value'):
                    val = item.value
                elif hasattr(item, 'v'):
                    val = item.v
                else:
                    val = item
                # Ensure it's a string and strip quotes if needed
                val_str = str(val)
                if val_str.startswith("'") or val_str.startswith('"'):
                    val_str = strip_quotes(val_str)
                transport_values.append(val_str)
            transport_list_str = "[" + ", ".join(transport_values) + "]"
        else:
            transport_list_str = str(transport_list_raw)
        
        rule_str += f"    AvailableTransportList = {transport_list_str}\n"
    
    rule_str += (
        f"    MaxPackNumber = {max_pack_number}\n"
        f"    NumberOfUnitInPack = {number_in_pack}\n"
        f"    NumberOfUnitInPackXPMultiplier = {xp_multiplier}\n"
        f"),"
    )
    
    return rule_str


def _extract_rule_metadata(rule_v: Any) -> Tuple[int, List[str]]:
    """Extract card count and transport list from a TDeckUniteRule object.
    
    Args:
        rule_v: The rule object (rule_obj.v from the list iteration)
    
    Returns:
        Tuple of (max_pack_number, transport_list)
        transport_list is a list of transport unit descriptors (or empty list if none)
    """
    max_pack_number = rule_v.by_m("MaxPackNumber").v
    # Convert to int if it's a string
    if isinstance(max_pack_number, str):
        try:
            max_pack_number = int(max_pack_number)
        except ValueError:
            max_pack_number = 0
    else:
        max_pack_number = int(max_pack_number)
    
    transport_list = []
    transport_list_member = rule_v.by_member("AvailableTransportList", False)
    if transport_list_member:
        transport_list_raw = transport_list_member.v
        
        # Handle transport list - extract string values
        if isinstance(transport_list_raw, str):
            # Parse string like "[$/GFX/Unit/Descriptor_Unit_X, $/GFX/Unit/Descriptor_Unit_Y]"
            if transport_list_raw.startswith("[") and transport_list_raw.endswith("]"):
                transport_str = transport_list_raw[1:-1].strip()
                if transport_str:
                    # Split by comma and clean up
                    transports = [t.strip() for t in transport_str.split(",")]
                    transport_list = transports
        elif hasattr(transport_list_raw, '__iter__') and not isinstance(transport_list_raw, str):
            # Extract string values from list
            for item in transport_list_raw:
                # Try to get the actual value from ListRow objects
                if hasattr(item, 'value'):
                    val = item.value
                elif hasattr(item, 'v'):
                    val = item.v
                else:
                    val = item
                # Ensure it's a string and strip quotes if needed
                val_str = str(val)
                if val_str.startswith("'") or val_str.startswith('"'):
                    val_str = strip_quotes(val_str)
                transport_list.append(val_str)
    
    return max_pack_number, transport_list


def _merge_transport_lists(transport_list1: List[str], transport_list2: List[str]) -> List[str]:
    """Merge two transport lists, removing duplicates while preserving order.
    
    Args:
        transport_list1: First transport list
        transport_list2: Second transport list
    
    Returns:
        Merged list with unique transports, preserving order (first list first, then second)
    """
    seen = set()
    merged = []
    
    # Add transports from first list
    for transport in transport_list1:
        if transport not in seen:
            seen.add(transport)
            merged.append(transport)
    
    # Add transports from second list that aren't already present
    for transport in transport_list2:
        if transport not in seen:
            seen.add(transport)
            merged.append(transport)
    
    return merged


def _update_rule_transports(rule_str: str, merged_transports: List[str]) -> str:
    """Update a serialized rule string with merged transport list.
    
    Args:
        rule_str: The serialized rule string
        merged_transports: List of merged transport unit descriptors
    
    Returns:
        Updated rule string with merged transports
    """
    import re
    
    # Build transport list string
    if merged_transports:
        transport_str = "[" + ", ".join(merged_transports) + "]"
    else:
        transport_str = ""
    
    # Check if rule already has AvailableTransportList
    if "AvailableTransportList" in rule_str:
        # Replace existing transport list - match the entire line
        # Pattern: whitespace + AvailableTransportList + = + [ + content + ]
        # We'll match everything from AvailableTransportList to the closing bracket on the same line
        pattern = r'(\s*)AvailableTransportList\s*=\s*\[.*?\]'
        
        if transport_str:
            # Find the indentation from the existing line
            match = re.search(pattern, rule_str, re.MULTILINE)
            if match:
                indent = match.group(1) if match.group(1) else "    "
                replacement = f"{indent}AvailableTransportList = {transport_str}"
            else:
                replacement = f"    AvailableTransportList = {transport_str}"
            rule_str = re.sub(pattern, replacement, rule_str, flags=re.MULTILINE)
        else:
            # Remove the entire line if no transports (including newline)
            pattern = r'\s*AvailableTransportList\s*=\s*\[.*?\]\s*\n'
            rule_str = re.sub(pattern, "", rule_str, flags=re.MULTILINE)
    else:
        # Insert transport list after AvailableWithoutTransport
        if transport_str:
            # Find the line with AvailableWithoutTransport and insert after it
            lines = rule_str.split('\n')
            new_lines = []
            for line in lines:
                new_lines.append(line)
                if 'AvailableWithoutTransport' in line and 'AvailableTransportList' not in line:
                    # Get indentation from the AvailableWithoutTransport line
                    indent_match = re.match(r'(\s*)', line)
                    indent = indent_match.group(1) if indent_match else "    "
                    new_lines.append(f"{indent}AvailableTransportList = {transport_str}")
            rule_str = '\n'.join(new_lines)
    
    return rule_str


def _extract_unit_name_from_descriptor(unit_descr: str) -> str:
    """Extract unit name from unit descriptor.
    
    Args:
        unit_descr: Unit descriptor in format "$/GFX/Unit/Descriptor_Unit_{unit_name}"
    
    Returns:
        Unit name without the descriptor prefix
    """
    prefix = "$/GFX/Unit/Descriptor_Unit_"
    if unit_descr.startswith(prefix):
        return unit_descr[len(prefix):]
    # Fallback: try to extract from any descriptor format
    if "Descriptor_Unit_" in unit_descr:
        return unit_descr.split("Descriptor_Unit_", 1)[1]
    return unit_descr


def _convert_custom_division_rule_to_string(unit_name: str, cards: int, availability: List[int], transports: Optional[List[Optional[str]]] = None) -> str:
    """Convert a custom division rule tuple to TDeckUniteRule string format.
    
    Args:
        unit_name: Name of the unit
        cards: Number of cards available
        availability: List of availability values for each XP level [reg, trained, hardened, veteran]
        transports: Optional list of transport unit names. Include None in the list to indicate
                   the unit can be deployed without transport but can optionally take transports.
    
    Returns:
        Formatted TDeckUniteRule string
    """
    unit_descr = f"$/GFX/Unit/Descriptor_Unit_{unit_name}"
    
    # Ensure availability list has exactly 4 elements
    if len(availability) != 4:
        logger.warning(f"Invalid availability format for {unit_name}: expected list of 4 elements, got {availability}")
        # Pad with zeros if too short, truncate if too long
        availability = (availability + [0] * 4)[:4]
    
    # Calculate base availability (max of the list)
    base_avail = max(availability) if availability else 0
    
    # Calculate XP multiplier (each value divided by base, rounded to 2 decimals)
    if base_avail > 0:
        xp_multi = [round(val / base_avail, 2) for val in availability]
    else:
        xp_multi = [0.0, 0.0, 0.0, 0.0]
    xp_multi_str = str(xp_multi)
    
    # Determine if unit needs transport
    # If None is in the transport list, the unit can be deployed without transport
    # but can optionally take transports
    has_transports = transports is not None and len(transports) > 0
    can_deploy_without_transport = False
    
    if has_transports:
        # Check if None is in the list (indicating optional transport)
        can_deploy_without_transport = None in transports
        # Filter out None values for the actual transport list
        valid_transports = [t for t in transports if t is not None]
    else:
        valid_transports = []
    
    # Set AvailableWithoutTransport based on whether None was in the list
    # If None is present, unit can deploy without transport (but can take one)
    # If None is not present but transports exist, unit requires transport
    available_without_transport = can_deploy_without_transport or not has_transports
    
    # Build transport list string if valid transports exist
    transport_str = ""
    if valid_transports:
        # Validate transport unit names (no spaces allowed)
        for transport in valid_transports:
            if " " in transport:
                logger.warning(f"Invalid transport unit name '{transport}' for {unit_name}: contains spaces. Unit names should use underscores instead.")
        transport_list = [f"$/GFX/Unit/Descriptor_Unit_{t}" for t in valid_transports]
        transport_str = "[" + ", ".join(transport_list) + "]"
    
    # Build the rule string
    rule_str = (
        f"TDeckUniteRule\n"
        f"(\n"
        f"    UnitDescriptor = {unit_descr}\n"
        f"    AvailableWithoutTransport = {available_without_transport}\n"
    )
    
    if transport_str:
        rule_str += f"    AvailableTransportList = {transport_str}\n"
    
    rule_str += (
        f"    MaxPackNumber = {cards}\n"
        f"    NumberOfUnitInPack = {base_avail}\n"
        f"    NumberOfUnitInPackXPMultiplier = {xp_multi_str}\n"
        f"),"
    )
    
    return rule_str


def _get_fob_unit_names() -> set:
    """Get set of valid FOB unit names from BuildingDescriptors.ndf or known list.
    
    Returns:
        Set of FOB unit names (e.g., {"FOB_US", "FOB_SOV", "FOB_UK", ...})
    """
    fob_names = {
        "FOB_BEL", "FOB_CAN", "FOB_CZ", "FOB_DDR", "FOB_ESP", 
        "FOB_FR", "FOB_NL", "FOB_POL", "FOB_RFA", "FOB_SOV", 
        "FOB_TCH", "FOB_UK", "FOB_US",
    }
    return fob_names


def _validate_unit_name(unit_name: str, game_db: Dict[str, Any]) -> bool:
    """Validate that a unit name exists in unit_data, NEW_UNITS, or FOB units.
    
    Args:
        unit_name: The unit name to validate (without Descriptor_Unit_ prefix)
        game_db: The game database containing unit_data
    
    Returns:
        True if unit exists, False otherwise
    """
    # Check in unit_data (existing units)
    unit_data = game_db.get("unit_data", {})
    if unit_name in unit_data:
        return True
    
    # Check in NEW_UNITS (new units use "NewName" key)
    for donor_unit, unit_info in NEW_UNITS.items():
        if unit_info.get("NewName") == unit_name:
            return True
    
    # Check if it's a FOB unit (special building units from BuildingDescriptors.ndf)
    fob_names = _get_fob_unit_names()
    if unit_name in fob_names:
        return True
    
    return False


def _create_national_division_rules(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Create division rules for national divisions by combining rules from source divisions or using custom rules."""
    new_divisions = load_new_divisions()
    
    if not new_divisions:
        logger.info("No new divisions to create rules for")
        return
    
    logger.info("Creating division rules for national divisions")
    
    # Create all divisions with custom division_rules
    logger.info("Creating divisions with custom division_rules")
    for div_key, div_data in new_divisions.items():
        cfg_name = div_data.get("cfg_name")
        if not cfg_name:
            logger.warning(f"No cfg_name specified for {div_key}, skipping")
            continue
        
        new_rule_namespace = f"Descriptor_Deck_Division_{cfg_name}_multi_Rule"
        
        # Check if rule already exists (shouldn't happen, but be safe)
        try:
            existing_rule = source_path.by_n(new_rule_namespace, False)
            if existing_rule:
                logger.warning(f"Division rule {new_rule_namespace} already exists, skipping creation")
                continue
        except (AttributeError, KeyError):
            pass  # Rule doesn't exist, which is expected
        
        # Check if this division has custom division_rules defined
        custom_rules = div_data.get("division_rules")
        if custom_rules:
            logger.info(f"Creating division rule {new_rule_namespace} from custom division_rules")
            collected_rules: Dict[str, str] = {}  # unit_descriptor -> serialized_rule
            collected_rule_metadata: Dict[str, Tuple[int, List[str]]] = {}  # unit_descriptor -> (card_count, transport_list)
            
            # Get rule exclusions if specified
            rule_exclusions = div_data.get("rule_exclusions", [])
            if rule_exclusions:
                logger.debug(f"Rule exclusions for {div_key}: {rule_exclusions}")
            
            # Handle division_rules as either a single dict or a list of dicts
            rules_dicts = []
            if isinstance(custom_rules, list):
                rules_dicts = custom_rules
                logger.debug(f"Processing {len(rules_dicts)} division rule dictionaries for {div_key}")
            elif isinstance(custom_rules, dict):
                rules_dicts = [custom_rules]
            else:
                logger.warning(f"Invalid division_rules format for {div_key}: expected dict or list of dicts, got {type(custom_rules)}")
                continue
            
            # Process each dictionary in the list
            for rules_dict in rules_dicts:
                if not isinstance(rules_dict, dict):
                    logger.warning(f"Invalid entry in division_rules list for {div_key}: expected dict, got {type(rules_dict)}. Skipping this entry.")
                    continue
                
                # Process each category in the custom rules dictionary
                for category, unit_rules in rules_dict.items():
                    if not isinstance(unit_rules, list):
                        continue
                    
                    for rule_tuple in unit_rules:
                        # Handle tuple format: (unit_name, cards, availability, [transports])
                        if len(rule_tuple) == 3:
                            unit_name, cards, availability = rule_tuple
                            transports = None
                        elif len(rule_tuple) == 4:
                            unit_name, cards, availability, transports = rule_tuple
                        else:
                            logger.warning(f"Invalid rule tuple format in {div_key} category {category}: {rule_tuple}")
                            continue
                        
                        # Check if this unit is excluded
                        if rule_exclusions and unit_name in rule_exclusions:
                            logger.debug(f"Skipping excluded unit {unit_name} in {div_key}")
                            continue
                        
                        # Validate availability list has 4 elements (for 4 XP levels)
                        if not isinstance(availability, list) or len(availability) != 4:
                            logger.warning(f"Invalid availability format for {unit_name} in {div_key}: expected list of 4 elements, got {availability}")
                            continue
                        
                        # Validate transports is a list if provided
                        if transports is not None and not isinstance(transports, list):
                            logger.warning(f"Invalid transports format for {unit_name} in {div_key}: expected list or None, got {type(transports)}")
                            transports = None
                        
                        # Validate transport unit names if provided
                        if transports:
                            valid_transports = []
                            for transport in transports:
                                if transport is None:
                                    valid_transports.append(None)
                                    continue
                                if " " in transport:
                                    logger.warning(f"Invalid transport unit name '{transport}' for {unit_name} in {div_key}: contains spaces. Unit names should use underscores instead.")
                                    continue
                                if not _validate_unit_name(transport, game_db):
                                    logger.warning(f"Invalid transport unit name '{transport}' for {unit_name} in {div_key}: transport not found in unit_data or NEW_UNITS")
                                    continue
                                valid_transports.append(transport)
                            transports = valid_transports if valid_transports else None
                        
                        # Validate unit name doesn't contain spaces
                        if " " in unit_name:
                            logger.warning(f"Invalid unit name '{unit_name}' in {div_key}: contains spaces. Unit names should use underscores instead.")
                            continue
                        
                        # Validate unit name exists in unit_data or NEW_UNITS
                        if not _validate_unit_name(unit_name, game_db):
                            logger.warning(f"Invalid unit name '{unit_name}' in {div_key} category {category}: unit not found in unit_data or NEW_UNITS")
                            continue
                        
                        unit_descr = f"$/GFX/Unit/Descriptor_Unit_{unit_name}"
                        
                        # Convert transports to descriptor format for merging
                        transport_descriptors = []
                        if transports:
                            # Filter out None values and convert to descriptors
                            for transport in transports:
                                if transport is not None:
                                    transport_descriptors.append(f"$/GFX/Unit/Descriptor_Unit_{transport}")
                        
                        # Check if we've already seen this unit
                        if unit_descr in collected_rules:
                            # Compare card counts - keep the one with higher card count, but merge transports
                            existing_card_count, existing_transports = collected_rule_metadata[unit_descr]
                            
                            if cards > existing_card_count:
                                # Replace with the rule that has more cards, but merge transports from both
                                logger.debug(f"Replacing duplicate unit {unit_descr} (cards: {existing_card_count} -> {cards})")
                                merged_transports = _merge_transport_lists(existing_transports, transport_descriptors)
                                # Convert merged transports back to unit names for rule string creation
                                merged_transport_names = [t.replace("$/GFX/Unit/Descriptor_Unit_", "") for t in merged_transports] if merged_transports else None
                                rule_str = _convert_custom_division_rule_to_string(
                                    unit_name=unit_name,
                                    cards=cards,
                                    availability=availability,
                                    transports=merged_transport_names
                                )
                                collected_rules[unit_descr] = rule_str
                                collected_rule_metadata[unit_descr] = (cards, merged_transports)
                                logger.debug(f"Merged transports when replacing {unit_descr}: {existing_transports} + {transport_descriptors} -> {merged_transports}")
                            elif cards == existing_card_count:
                                # Same card count - merge transports
                                logger.debug(f"Merging transports for duplicate unit {unit_descr} (cards: {cards})")
                                merged_transports = _merge_transport_lists(existing_transports, transport_descriptors)
                                if merged_transports != existing_transports:
                                    # Update the rule with merged transports
                                    rule_str = collected_rules[unit_descr]
                                    updated_rule_str = _update_rule_transports(rule_str, merged_transports)
                                    collected_rules[unit_descr] = updated_rule_str
                                    collected_rule_metadata[unit_descr] = (cards, merged_transports)
                                    logger.debug(f"Merged transports for {unit_descr}: {existing_transports} + {transport_descriptors} -> {merged_transports}")
                            else:
                                # Existing rule has more cards - merge transports into existing rule
                                logger.debug(f"Merging transports into existing rule for {unit_descr} (existing cards: {existing_card_count}, new cards: {cards})")
                                merged_transports = _merge_transport_lists(existing_transports, transport_descriptors)
                                if merged_transports != existing_transports:
                                    # Update the rule with merged transports
                                    rule_str = collected_rules[unit_descr]
                                    updated_rule_str = _update_rule_transports(rule_str, merged_transports)
                                    collected_rules[unit_descr] = updated_rule_str
                                    collected_rule_metadata[unit_descr] = (existing_card_count, merged_transports)
                                    logger.debug(f"Merged transports for {unit_descr}: {existing_transports} + {transport_descriptors} -> {merged_transports}")
                            continue
                        
                        # Convert to rule string
                        rule_str = _convert_custom_division_rule_to_string(
                            unit_name=unit_name,
                            cards=cards,
                            availability=availability,
                            transports=transports
                        )
                        
                        collected_rules[unit_descr] = rule_str
                        collected_rule_metadata[unit_descr] = (cards, transport_descriptors)
                        logger.debug(f"Added custom rule for {unit_name} in {div_key}")
            
            if not collected_rules:
                logger.warning(f"No unit rules collected from custom division_rules for {div_key}, skipping rule creation")
                continue
            
            # Find a donor division rule to insert before
            donor_rule = None
            for deck_descr in source_path:
                if deck_descr.n.endswith("_multi_Rule"):
                    donor_rule = deck_descr
                    break
            
            # Create new division rule from custom rules
            unit_rules_str = "\n".join([f"        {rule_str}" for rule_str in collected_rules.values()])
            
            division_rule_str = (
                f"{new_rule_namespace} is TDeckDivisionRule\n"
                f"(\n"
                f"    UnitRuleList =\n"
                f"    [\n"
                f"{unit_rules_str}\n"
                f"    ]\n"
                f")"
            )
            
            try:
                parsed_rule = ndf.convert(division_rule_str)
                if parsed_rule:
                    new_rule_obj = parsed_rule[0] if isinstance(parsed_rule, list) else parsed_rule
                    if donor_rule:
                        donor_index = donor_rule.index
                        source_path.insert(donor_index, new_rule_obj)
                    else:
                        source_path.add(new_rule_obj)
                    logger.info(f"Created division rule {new_rule_namespace} with {len(collected_rules)} unit rules from custom division_rules")
                else:
                    logger.error(f"Failed to parse division rule string for {new_rule_namespace}")
            except Exception as e:
                logger.error(f"Failed to add division rule {new_rule_namespace}: {str(e)}")
                import traceback
                logger.debug(traceback.format_exc())
    
    logger.info("Finished creating national division rules")