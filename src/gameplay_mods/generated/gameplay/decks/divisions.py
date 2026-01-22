"""Functions for modifying Divisions.ndf"""

from collections import defaultdict
from typing import Any, Dict

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes
from src.utils.dictionary_utils import write_dictionary_entries
from src import ModConfig
from src.constants.generated.gameplay.decks import load_new_divisions
from src.constants.generated.gameplay.decks.new_divisions import spec_tags

logger = setup_logger(__name__)

# Mapping of country codes to coalitions
NATION_TO_COALITION = {
    "US": "NATO",
    "USA": "NATO",
    "UK": "NATO",
    "FR": "NATO",
    "RFA": "NATO",
    "POL": "PACT",
    "SOV": "PACT",
    "RDA": "PACT",
    "DDR": "PACT",
}


def edit_gen_gp_decks_divisions(source_path) -> None:
    """GameData/Generated/Gameplay/Decks/Divisions.ndf"""

    config = ModConfig.get_instance()

    hide_divs = config.config_data.get("hide_divs", [])
    if config.config_data["build_config"]["write_dev"]:
        # In dev mode, remove divisions that should be shown for testing
        dev_show_divs = config.config_data.get("dev_show_divs", [])
        divs_to_hide = [div for div in hide_divs if div not in dev_show_divs]
    else:
        # In release mode, hide all divisions in hide_divs
        divs_to_hide = hide_divs

    indices_to_remove = []
    logger.info("Modifying hidden divisions in Divisions.ndf ")    
    for division in divs_to_hide:
        div_index = source_path.by_n(f"Descriptor_Deck_Division_{division}").index
        indices_to_remove.append(div_index)

    for index in sorted(indices_to_remove, reverse=True):
        source_path.remove(index)
    
    for deck_descr in source_path:
        MaxActivationPoints = deck_descr.v.by_member("MaxActivationPoints", False)
        if MaxActivationPoints and MaxActivationPoints.v == "50":
            MaxActivationPoints.v = "100"
    
    # Add new national divisions
    _add_national_divisions(source_path)


def _extract_nation_from_division_key(div_key: str) -> str:
    """Extract nation code from division key (e.g., 'US_general' -> 'US')."""
    # Handle various formats: US_general, USA_general, etc.
    if div_key.startswith("US"):
        # Could be US or USA - normalize to US for matching
        return "US"
    # Extract first part before underscore
    parts = div_key.split("_")
    return parts[0] if parts else div_key


def _normalize_nation_code(nation: str) -> str:
    """Normalize nation code for matching (e.g., 'USA' -> 'US', 'RDA' -> 'DDR')."""
    if nation == "USA":
        return "US"
    if nation == "RDA":
        return "DDR"
    return nation


def _get_coalition_for_nation(nation: str) -> str:
    """Get coalition (NATO/PACT) for a given nation code."""
    normalized_nation = _normalize_nation_code(nation)
    return NATION_TO_COALITION.get(normalized_nation, "NATO")  # Default to NATO if unknown


def _add_national_divisions(source_path: Any) -> None:
    """Add national divisions to Divisions.ndf."""
    new_divisions = load_new_divisions()
    
    if not new_divisions:
        logger.info("No new divisions to add")
        return
    
    # Map current interface order of multi divisions by nation
    # Structure: interface_order[nation][division_name] = order_value
    # Use normalized nation codes for consistent matching
    interface_order: Dict[str, Dict[str, float]] = defaultdict(dict)
    division_objects: Dict[str, Any] = {}  # Store division objects for later reference
    
    for deckdivision_descr in source_path:
        if not hasattr(deckdivision_descr, "namespace") or not deckdivision_descr.namespace.endswith("_multi"):
            continue
        
        division_name = deckdivision_descr.namespace.replace("Descriptor_Deck_Division_", "").replace("_multi", "")
        division_nation_raw = strip_quotes(deckdivision_descr.v.by_m("CountryId").v)
        division_nation = _normalize_nation_code(division_nation_raw)
        order_value = float(deckdivision_descr.v.by_m("InterfaceOrder").v)
        
        # Skip divisions with InterfaceOrder = -1.0 (hidden divisions)
        if order_value == -1.0:
            continue
        
        interface_order[division_nation][division_name] = order_value
        division_objects[division_name] = deckdivision_descr
    
    # Group new divisions by nation
    new_divisions_by_nation: Dict[str, Dict[str, Dict]] = defaultdict(dict)
    for div_key, div_data in new_divisions.items():
        nation_raw = _extract_nation_from_division_key(div_key)
        nation = _normalize_nation_code(nation_raw)
        new_divisions_by_nation[nation][div_key] = div_data
    
    # Calculate interface order adjustments
    # For each nation, find the first existing division (lowest InterfaceOrder)
    # New divisions will be inserted before it, so we need to bump existing divisions
    nation_first_orders: Dict[str, float] = {}
    for nation, divisions in interface_order.items():
        if divisions:
            nation_first_orders[nation] = min(divisions.values())
    
    # Calculate how many new divisions per nation
    new_div_counts: Dict[str, int] = {
        nation: len(divs) for nation, divs in new_divisions_by_nation.items()
    }
    
    # Update interface order for existing divisions (bump them by number of new divisions)
    for nation, divisions in interface_order.items():
        bump_amount = new_div_counts.get(nation, 0)
        if bump_amount > 0:
            for division_name in divisions:
                interface_order[nation][division_name] += bump_amount
                # Update the actual division object
                if division_name in division_objects:
                    division_objects[division_name].v.by_m("InterfaceOrder").v = str(
                        interface_order[nation][division_name]
                    )
    
    # Collect dictionary entries for all new divisions
    dictionary_entries = []
    
    # Create and add new division descriptors
    for nation, new_divs_dict in new_divisions_by_nation.items():
        if nation not in nation_first_orders:
            logger.warning(f"No existing divisions found for nation {nation}, skipping new divisions")
            continue
        
        # Find a donor division from the same nation to copy from
        donor_division = None
        for div_name, div_obj in division_objects.items():
            div_nation_raw = strip_quotes(div_obj.v.by_m("CountryId").v)
            div_nation = _normalize_nation_code(div_nation_raw)
            if div_nation == nation:
                donor_division = div_obj
                break
        
        if not donor_division:
            logger.warning(f"No donor division found for nation {nation}, skipping new divisions")
            continue
        
        # Calculate starting interface order for new divisions
        # They should be inserted before the first existing division
        # Note: InterfaceOrder values are reserved differently by coalition:
        #   - NATO: 1.0 and 2.0 are reserved
        #   - PACT: only 1.0 is reserved (first PACT division starts at 2.0)
        first_order = nation_first_orders[nation]
        num_new = len(new_divs_dict)
        start_order = first_order - num_new
        
        # Determine coalition and set reserved orders accordingly
        coalition = _get_coalition_for_nation(nation)
        if coalition == "NATO":
            RESERVED_ORDERS = {1.0, 2.0}
        else:  # PACT
            RESERVED_ORDERS = {1.0}
        
        # Track the current order value, incrementing and skipping reserved values
        current_order = start_order
        
        # Sort new divisions: "general" decks first, then alphabetical order for the rest
        def sort_key(item):
            div_key, _ = item
            # Return (is_general, div_key) tuple - False sorts before True, so we negate
            # to make general (True) come first
            is_general = div_key.endswith("_general")
            return (not is_general, div_key)
        
        # Create new division descriptors
        for idx, (div_key, div_data) in enumerate(sorted(new_divs_dict.items(), key=sort_key)):
            # Skip reserved InterfaceOrder values (coalition-specific)
            # If we hit a reserved value, shift to the next available value
            while current_order in RESERVED_ORDERS:
                current_order += 1.0
            
            new_order = current_order
            # Increment for next iteration
            current_order += 1.0
            
            # Create new division descriptor by copying donor
            new_div_descr = donor_division.copy()
            
            # Extract division type from key (e.g., "US_general" -> "general")
            div_type = div_key.split("_", 1)[1] if "_" in div_key else "general"
            cfg_name = div_data.get("cfg_name", f"{nation}_national_{div_type}")
            
            # Set namespace and name
            new_div_descr.namespace = f"Descriptor_Deck_Division_{cfg_name}_multi"
            new_div_descr.n = new_div_descr.namespace
            
            # Update fields
            new_div_descr.v.by_m("DescriptorId").v = f"GUID:{{{div_data['guid']}}}"
            new_div_descr.v.by_m("CfgName").v = f"'{cfg_name}'"
            
            # Set division name (token)
            div_name_tokens = div_data.get("div_name", ("", ""))
            if isinstance(div_name_tokens, tuple) and len(div_name_tokens) >= 2:
                new_div_descr.v.by_m("DivisionName").v = f"'{div_name_tokens[1]}'"
                # Collect dictionary entry: (token, text)
                dictionary_entries.append((div_name_tokens[1], div_name_tokens[0]))
            
            # Set interface order
            new_div_descr.v.by_m("InterfaceOrder").v = str(new_order)
            
            # Set division power classification
            div_power = div_data.get("div_power", "DC_PWR1")
            new_div_descr.v.by_m("DivisionPowerClassification").v = f"'{div_power}'"
            
            # Set coalition
            coalition = _get_coalition_for_nation(nation)
            new_div_descr.v.by_m("DivisionCoalition").v = f"ECoalition/{coalition}"
            
            # Set division tags
            tags = spec_tags.get(div_type, spec_tags["general"])
            tags_with_nation = tags + [nation, coalition]
            tags_str = "[" + ", ".join([f"'{tag}'" for tag in tags_with_nation]) + "]"
            new_div_descr.v.by_m("DivisionTags").v = tags_str
            
            # Set description hint title token
            desc_tokens = div_data.get("description_title", ("", ""))
            if isinstance(desc_tokens, tuple) and len(desc_tokens) >= 2:
                new_div_descr.v.by_m("DescriptionHintTitleToken").v = f"'{desc_tokens[1]}'"
                # Collect dictionary entry: (token, text)
                dictionary_entries.append((desc_tokens[1], desc_tokens[0]))
            
            # Set max activation points
            max_activation = div_data.get("activation_points", 85)
            new_div_descr.v.by_m("MaxActivationPoints").v = str(max_activation)
            
            # Set division rule reference
            new_div_descr.v.by_m("DivisionRule").v = f"Descriptor_Deck_Division_{cfg_name}_multi_Rule"
            
            # Set cost matrix reference
            new_div_descr.v.by_m("CostMatrix").v = f"MatrixCostName_{cfg_name}_multi"
            
            # Set country ID - use the original format from donor if available, otherwise use normalized nation
            # Check what format the donor uses
            donor_country_id = strip_quotes(donor_division.v.by_m("CountryId").v)
            # Use the same format as existing divisions for this nation
            country_id_to_use = donor_country_id if _normalize_nation_code(donor_country_id) == nation else nation
            new_div_descr.v.by_m("CountryId").v = f'"{country_id_to_use}"'
            
            # Set type texture
            type_texture = div_data.get("type_texture", "infantryReg")
            new_div_descr.v.by_m("TypeTexture").v = f'"Texture_Division_Type_{type_texture}"'
            
            # Set emblem texture - uses the division key (e.g., "US_general" -> "Texture_Division_Emblem_US_general")
            emblem_texture = f"Texture_Division_Emblem_{div_key}"
            new_div_descr.v.by_m("EmblemTexture").v = f'"{emblem_texture}"'
            
            # Add to source_path
            source_path.add(new_div_descr)
            logger.info(f"Added new division {cfg_name} with InterfaceOrder {new_order} for nation {nation}")
    
    # Write dictionary entries to outgame dictionary
    if dictionary_entries:
        write_dictionary_entries(dictionary_entries, dictionary_type="units")
    
    logger.info(f"Finished adding {sum(new_div_counts.values())} new divisions")