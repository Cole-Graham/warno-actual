from typing import Any, Dict, Optional

from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger('divisions_unit_edits')

def strip_division_name(division_name: str) -> Optional[str]:
    """Extract core division name from full descriptor name."""
    prefix = 'Descriptor_Deck_Division_'
    suffix = '_multi'
    
    if division_name.startswith(prefix) and division_name.endswith(suffix):
        return division_name[len(prefix):-len(suffix)]
    return None

def _handle_division_changes(div_descr: Any, unit: str, div_name: str, edits: Dict) -> None:
    """Handle adding/removing units from a division."""
    pack_list_map = div_descr.v.by_member("PackList").v
    
    # Handle removal
    if "remove" in edits["Divisions"] and div_name in edits["Divisions"]["remove"]:
        logger.debug(f"Removing {unit} from {div_name}")
        pack_list_map.remove_by_key(f"~/Descriptor_Deck_Pack_{unit}")
        return
        
    # Handle addition
    if "add" in edits["Divisions"] and div_name in edits["Divisions"]["add"]:
        cards = (edits["Divisions"].get(div_name, {}).get("cards") or 
                edits["Divisions"]["default"]["cards"])
        pack_list_map.add(f"(~/Descriptor_Deck_Pack_{unit}, {cards})")
        logger.debug(f"Adding {cards} cards of {unit} to {div_name}")
        return

def _update_card_count(pack_list_map: Any, unit: str, div_name: str, edits: Dict) -> None:
    """Update card count for a unit in a division."""
    for map_row in pack_list_map:
        unit_key = map_row.k
        if unit_key != f"~/Descriptor_Deck_Pack_{unit}":
            continue
            
        if not "Divisions" in edits:
            break
            
        # Get card count from division-specific or default settings
        cards = (edits["Divisions"].get(div_name, {}).get("cards") or 
                edits["Divisions"].get("default", {}).get("cards"))
                
        if cards:
            logger.debug(f"Setting {unit} cards to {cards} in {div_name}")
            map_row.v = str(cards)
            break

def edit_division_units(source: Any) -> None:
    """Edit unit availability in divisions."""
    logger.info("Editing unit availability in divisions")
    
    unit_edits = load_unit_edits()
    
    for unit, edits in unit_edits.items():
        for div_descr in source:
            div_name = strip_division_name(div_descr.namespace)
            if div_name is None:
                continue
                
            if "Divisions" in edits:
                _handle_division_changes(div_descr, unit, div_name, edits)
                _update_card_count(div_descr.v.by_member("PackList").v, unit, div_name, edits) 