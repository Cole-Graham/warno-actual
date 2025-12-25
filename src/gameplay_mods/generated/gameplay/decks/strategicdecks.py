"""Functions for modifying deck packs and their references."""

from typing import Any, Dict, Tuple, Optional
import re
from pathlib import Path
import json

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_namespace
from src import ModConfig

logger = setup_logger(__name__)

# Global variable to track if pack changes have been determined
_pack_changes_determined = False
deck_pack_changes = {
    "StrategicDecks": {},
    "StrategicPacks": {}
}

def edit_gen_gp_decks_strategicdecks(source_path: Any, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Decks/StrategicDecks.ndf"""
    global _pack_changes_determined, deck_pack_changes
    
    strategic_deck_data = game_db["decks"]["strategic"]
    
    if not _pack_changes_determined:
        deck_pack_changes = _determine_pack_changes(source_path, strategic_deck_data, deck_pack_changes)
        _pack_changes_determined = True
    
    _swap_leaders_strategicdecks(source_path, deck_pack_changes)


def edit_gen_gp_decks_strategicpacks(source_path: Any, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Decks/StrategicPacks.ndf"""
    global _pack_changes_determined, deck_pack_changes
    
    strategic_deck_data = game_db["decks"]["strategic"]
    
    if not _pack_changes_determined:
        deck_pack_changes = _determine_pack_changes(source_path, strategic_deck_data, deck_pack_changes)
        _pack_changes_determined = True
    
    _create_new_command_strategicpacks(source_path, deck_pack_changes)


def edit_gen_gp_decks_strategiccombatgroups(source_path: Any, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Decks/StrategicCombatGroups.ndf"""
    pass


def _swap_leaders_strategicdecks(source_path: Any, deck_pack_changes: Dict[str, Any]) -> None:
    """Swap new command units into existing deck pack references for strategic and challenge decks which used donor command
    units which were turned into Leader units (and thus can't capture zones)"""    
    for deck_descr_name, deck_descr_data in deck_pack_changes["StrategicDecks"].items():
        
        deck_pack_list = deck_descr_data["DeckPackList"]
        
        # Find the deck pack in the source path
        deck_descr_obj = find_obj_by_namespace(source_path, deck_descr_name)
        if not deck_descr_obj:
            logger.warning(f"No deck descriptor found for {deck_descr_name}")
            continue
        
        obj_deck_pack_list = deck_descr_obj.v.by_m("DeckPackList")
        for reference_index, reference_values in deck_pack_list.items():
            old_reference = reference_values["old_reference"]
            new_reference = f"~/{reference_values['new_reference']}"
            unit_number = reference_values["unit_number"]

            obj_deck_pack_list.v.replace(int(reference_index), new_reference)


def _create_new_command_strategicpacks(source_path: Any, deck_pack_changes: Dict[str, Any]) -> None:
    """Create new packs for strategic and challenge decks which used donor command
    units which were turned into Leader units (and thus can't capture zones)"""
    for pack_name, pack_data in deck_pack_changes["StrategicPacks"].items():
        main_unit_part = pack_data["main_unit_part"]
        transport_part = pack_data["transport_part"]
        xp = pack_data["xp"]
        
        new_entry_namespace = pack_name
        if transport_part:
            transport_line = f"    Transport = $/GFX/Unit/Descriptor_Unit_{transport_part}"
        else:
            transport_line = ""
            
        if int(xp) > 0:
            xp_line = f"    Xp = {xp}"
        else:
            xp_line = ""
        
        new_entry = (
            f'{new_entry_namespace} is DeckPackDescriptor\n'
            f'(\n'
            f'{xp_line}\n'
            f'{transport_line}\n'
            f'    Unit = $/GFX/Unit/Descriptor_Unit_{main_unit_part}\n'
            f')'
        )
        
        source_path.add(new_entry)


def _swap_leaders_strategiccombatgroups(source_path: Any) -> None:
    """Swap new command units into existing combat groups for strategic and challenge decks which used donor command
    units which were turned into Leader units (and thus can't capture zones)"""
    pass


def _determine_pack_changes(source_path: Any, strategic_deck_data: Dict[str, Any], deck_pack_changes: Dict[str, Any]) -> None:
    """Determine pack changes for strategic decks
    
    deck_pack_changes = {
        "StrategicDecks": {
            "Deck_namespace": {
                "DeckPackList": {
                    "index": {
                        "old_reference": str,
                        "new_reference": str,
                        "unit_number": int,
                    }
                }
            }
        },
        "StrategicPacks": {
            "new_pack_namespace": {
                "xp": int,
                "transport_part": str,
                "main_unit_part": str,
            }
        }
    }
    """
    
    donor_dict = {}
    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        new_unit_name = edits["NewName"]
        if "_CMD2_" in new_unit_name:
            
            # Get XP level from availability
            availability = edits.get("availability", None)
            xp = None
            if availability:
                for i, availability_ in enumerate(availability):
                    if availability_ != 0:
                        xp = str(i)
                        break
            
            donor_dict[donor_name] = {
                "new_unit_name": new_unit_name,
                "xp": xp
            }
        
    for strategic_deck_name, deck_data in strategic_deck_data.items():
        
        deck_descr_name = f"Descriptor_Deck_{strategic_deck_name}"
        deck_pack_changes["StrategicDecks"][deck_descr_name] = {
            "DeckPackList": {}
        }
        
        previous_deck_pack = "None"
        unit_number = 1
        for i, deck_pack in enumerate(deck_data["packs"]):
            # Parse the deck pack namespace
            parsed_parts = parse_deck_pack_namespace(deck_pack)
            
            logger.debug(f"Parsed deck pack '{deck_pack}': {parsed_parts}")
            
            # Now you can work with the parsed parts
            prefix = parsed_parts["prefix"]
            transport_part = parsed_parts["transport_part"]
            main_unit_part = parsed_parts["main_unit_part"]
            xp = parsed_parts["xp"]
            
            new_strat_pack_name = None
            new_unit_name = None
            
            if main_unit_part in donor_dict:
                donor_data = donor_dict[main_unit_part]
                new_unit_name = donor_data["new_unit_name"]
                xp = donor_data["xp"]
                
                # Replace donor unit name with new unit name in the namespace structure
                if transport_part:
                    new_strat_pack_name = f"{prefix}_{transport_part}_{new_unit_name}_{xp}"
                else:
                    new_strat_pack_name = f"{prefix}_{new_unit_name}_{xp}"
            
            # Track unit numbers for consecutive identical packs
            if previous_deck_pack != deck_pack:
                unit_number = 1
                previous_deck_pack = deck_pack
            else: 
                unit_number += 1
            
            if new_strat_pack_name:
                deck_pack_changes["StrategicDecks"][deck_descr_name]["DeckPackList"][str(i)] = {
                    "old_reference": deck_pack,
                    "new_reference": new_strat_pack_name,
                    "unit_number": unit_number
                }
                    
                deck_pack_changes["StrategicPacks"][new_strat_pack_name] = {
                    "xp": xp,
                    "transport_part": transport_part,
                    "main_unit_part": new_unit_name
                }
    deck_pack_changes_for_json = deck_pack_changes
    logs_dir = Path(__file__).parents[5] / "logs"
    logs_dir.mkdir(exist_ok=True)
    with open(logs_dir / "deck_pack_changes.json", "w") as f:
        json.dump(deck_pack_changes_for_json, f, indent=4)
    
    return deck_pack_changes

def parse_deck_pack_namespace(deck_pack: str) -> Dict[str, str]:
    """
    Parse a deck pack namespace into its distinct parts.
    
    Args:
        deck_pack: The deck pack namespace string
        
    Returns:
        Dictionary containing parsed parts:
        - prefix: The prefix part (e.g., "Descriptor_StrategicPack")
        - transport_part: The transport part if present, None otherwise
        - main_unit_part: The main unit part
        - xp: The experience level
        
    Examples:
        "Descriptor_StrategicPack_FV101_Scorpion_BEL_0" -> {
            "prefix": "Descriptor_StrategicPack",
            "transport_part": None,
            "main_unit_part": "FV101_Scorpion_BEL",
            "xp": "0"
        }
        
        "Descriptor_StrategicPack_M113A1B_BEL_Rifles_AT_BEL_0" -> {
            "prefix": "Descriptor_StrategicPack", 
            "transport_part": "M113A1B_BEL",
            "main_unit_part": "Rifles_AT_BEL",
            "xp": "0"
        }
    """
    # Split by underscore to get all parts
    parts = deck_pack.split('_')
    
    if len(parts) < 4:
        logger.warning(f"Invalid deck pack namespace format: {deck_pack}")
        return {
            "prefix": deck_pack,
            "transport_part": None,
            "main_unit_part": None,
            "xp": None
        }
    
    # The last part is always the XP level
    xp = parts[-1]
    
    # The prefix is always "Descriptor_StrategicPack" (2 parts)
    prefix = "_".join(parts[:2])
    
    # Check if this has a transport by looking for patterns
    # Transport pattern: prefix + transport_part + main_unit_part + xp
    # Non-transport pattern: prefix + main_unit_part + xp
    
    remaining_parts = parts[2:-1]  # Exclude prefix and XP
    
    # Try to detect transport pattern
    # Look for a pattern where we have a transport part followed by main unit part
    # Transport parts typically end with a country code (like _BEL, _US, etc.)
    transport_part = None
    main_unit_part = None
    
    # Check if we have enough parts for a transport
    if len(remaining_parts) >= 3:
        # Look for transport pattern: something ending with country code
        for i in range(1, len(remaining_parts) - 1):
            potential_transport = "_".join(remaining_parts[:i])
            potential_main_unit = "_".join(remaining_parts[i:])
            
            # Check if potential_transport ends with a country code
            if re.search(r'_[A-Z]{2,3}$', potential_transport):
                transport_part = potential_transport
                main_unit_part = potential_main_unit
                break
    
    # If no transport detected, treat all remaining parts as main unit
    if transport_part is None:
        main_unit_part = "_".join(remaining_parts)
    
    return {
        "prefix": prefix,
        "transport_part": transport_part,
        "main_unit_part": main_unit_part,
        "xp": xp
    }