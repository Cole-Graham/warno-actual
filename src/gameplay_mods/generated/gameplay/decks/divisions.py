"""Functions for modifying Divisions.ndf"""

from collections import defaultdict
from typing import Any, Dict

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes
from src.utils.dictionary_utils import write_dictionary_entries
from src import ModConfig
from src.constants.generated.gameplay.decks import load_new_divisions
from src.constants.generated.gameplay.decks.new_divisions import DIV_TYPE_TO_TOKEN

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
    write_dev = config.config_data["build_config"]["write_dev"]
    dev_show_divs = config.config_data.get("dev_show_divs") or []
    if write_dev and len(dev_show_divs) > 0:
        # In dev mode, remove divisions that should be shown for testing
        divs_to_hide = [div for div in hide_divs if div not in dev_show_divs]
    else:
        # In release mode, hide all divisions in hide_divs
        divs_to_hide = hide_divs

    # Collect donor divisions BEFORE removing - we need them to copy structure for new divisions
    donor_divisions = _collect_donor_divisions(source_path)

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

    # Add new national divisions (pass pre-collected donors since we removed them)
    _add_national_divisions(source_path, donor_divisions)


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


def _set_or_add_member(obj, member_name: str, value: str) -> None:
    """Set member value if it exists, otherwise add it (for donor compatibility)."""
    member = obj.by_member(member_name, False)
    if member:
        member.v = value
    else:
        obj.add(f"{member_name} = {value}")


def _collect_donor_divisions(source_path: Any) -> Dict[str, Any]:
    """Collect donor divisions (any with _multi suffix) for copying structure.
    Must be called BEFORE removing hidden divisions."""
    donor_divisions: Dict[str, Any] = {}
    for deckdivision_descr in source_path:
        if not hasattr(deckdivision_descr, "namespace") or not deckdivision_descr.namespace.endswith("_multi"):
            continue

        division_nation_raw = strip_quotes(deckdivision_descr.v.by_m("CountryId").v)
        division_nation = _normalize_nation_code(division_nation_raw)

        if division_nation not in donor_divisions:
            donor_divisions[division_nation] = deckdivision_descr
    return donor_divisions


def _add_national_divisions(source_path: Any, donor_divisions: Dict[str, Any]) -> None:
    """Add national divisions to Divisions.ndf."""
    new_divisions = load_new_divisions()

    if not new_divisions:
        logger.info("No new divisions to add")
        return
    
    # Group new divisions by nation
    new_divisions_by_nation: Dict[str, Dict[str, Dict]] = defaultdict(dict)
    for div_key, div_data in new_divisions.items():
        nation_raw = _extract_nation_from_division_key(div_key)
        nation = _normalize_nation_code(nation_raw)
        new_divisions_by_nation[nation][div_key] = div_data
    
    # Sort nations: US first, SOV second, then alphabetical
    def nation_sort_key(nation: str) -> tuple:
        if nation == "US":
            return (0, nation)  # US first
        elif nation == "SOV":
            return (1, nation)  # SOV second
        else:
            return (2, nation)  # Others alphabetically
    
    sorted_nations = sorted(new_divisions_by_nation.keys(), key=nation_sort_key)
    
    # Sort divisions within each nation: general first, then alphabetical
    def division_sort_key(item):
        div_key, _ = item
        is_general = div_key.endswith("_general")
        return (not is_general, div_key)  # False sorts before True, so general comes first
    
    # Collect dictionary entries for all new divisions
    dictionary_entries = []

    # Create and add new division descriptors
    for nation in sorted_nations:
        new_divs_dict = new_divisions_by_nation[nation]
        
        # Find donor division for this nation
        donor_division = None
        
        # Try to find donor from same nation first
        if nation in donor_divisions:
            donor_division = donor_divisions[nation]
        else:
            # Fallback: find any donor division (prefer same coalition)
            coalition = _get_coalition_for_nation(nation)
            for donor_nation, donor_div in donor_divisions.items():
                donor_coalition = _get_coalition_for_nation(donor_nation)
                if donor_coalition == coalition:
                    donor_division = donor_div
                    break
            
            # If still no donor, use any available
            if not donor_division and donor_divisions:
                donor_division = next(iter(donor_divisions.values()))
        
        if not donor_division:
            logger.warning(f"No donor division found for nation {nation}, skipping {len(new_divs_dict)} new division(s)")
            continue
        
        # Determine coalition
        coalition = _get_coalition_for_nation(nation)
        
        # Sort divisions: general first, then alphabetical
        sorted_divisions = sorted(new_divs_dict.items(), key=division_sort_key)
        
        # Create new division descriptors
        for div_key, div_data in sorted_divisions:
            interface_order = div_data.get("interface_order")
            if interface_order is None:
                logger.error(f"Missing interface_order for {div_key}, skipping division")
                continue

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
            
            # Set interface order (hardcoded, starting at 500 to avoid vanilla division range)
            new_div_descr.v.by_m("InterfaceOrder").v = str(float(interface_order))
            
            # Remove deprecated members (DivisionPowerClassification, TypeTexture replaced by TypeToken)
            if new_div_descr.v.by_member("DivisionPowerClassification", False):
                new_div_descr.v.remove_by_member("DivisionPowerClassification")
            if new_div_descr.v.by_member("TypeTexture", False):
                new_div_descr.v.remove_by_member("TypeTexture")
            
            # Set coalition
            new_div_descr.v.by_m("DivisionCoalition").v = f"ECoalition/{coalition}"
            
            # Set division tags: ['DEFAULT', nation, coalition, TypeToken]
            type_token = DIV_TYPE_TO_TOKEN.get(div_type, DIV_TYPE_TO_TOKEN["general"])
            tags = ["DEFAULT", nation, coalition, type_token]
            tags_str = "[" + ", ".join([f"'{tag}'" for tag in tags]) + "]"
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
            donor_country_id = strip_quotes(donor_division.v.by_m("CountryId").v)
            # Use the same format as donor if it matches nation, otherwise use normalized nation
            country_id_to_use = donor_country_id if _normalize_nation_code(donor_country_id) == nation else nation
            new_div_descr.v.by_m("CountryId").v = f'"{country_id_to_use}"'
            
            # Set TypeToken (replaces TypeTexture) - add if donor lacks it
            _set_or_add_member(new_div_descr.v, "TypeToken", f'"{type_token}"')
            
            # Set SummaryTextToken and HistoryTextToken (required in new format)
            summary_tokens = div_data.get("summary_text", ("", ""))
            if isinstance(summary_tokens, tuple) and len(summary_tokens) >= 2 and summary_tokens[1]:
                _set_or_add_member(new_div_descr.v, "SummaryTextToken", f"'{summary_tokens[1]}'")
                dictionary_entries.append((summary_tokens[1], summary_tokens[0]))
            history_tokens = div_data.get("history_text", ("", ""))
            if isinstance(history_tokens, tuple) and len(history_tokens) >= 2 and history_tokens[1]:
                _set_or_add_member(new_div_descr.v, "HistoryTextToken", f"'{history_tokens[1]}'")
                dictionary_entries.append((history_tokens[1], history_tokens[0]))
            
            # Set StandoutUnits (max 3 units/transports from division rules)
            standout_units = div_data.get("standout_units", [])
            if standout_units:
                standout_str = "[\n        " + ",\n        ".join(
                    f"$/GFX/Unit/Descriptor_Unit_{u}" for u in standout_units
                ) + ",\n    ]"
                _set_or_add_member(new_div_descr.v, "StandoutUnits", standout_str)
            
            # Set emblem texture - uses the division key (e.g., "US_general" -> "Texture_Division_Emblem_US_general")
            emblem_texture = f"Texture_Division_Emblem_{div_key}"
            new_div_descr.v.by_m("EmblemTexture").v = f'"{emblem_texture}"'
            
            # Add to source_path
            source_path.add(new_div_descr)
            logger.info(f"Added new division {cfg_name} with InterfaceOrder {interface_order} for nation {nation}")
    
    # Write dictionary entries to outgame dictionary
    if dictionary_entries:
        write_dictionary_entries(dictionary_entries, dictionary_type="units")
    
    total_divs = sum(len(divs) for divs in new_divisions_by_nation.values())
    logger.info(f"Finished adding {total_divs} new divisions")