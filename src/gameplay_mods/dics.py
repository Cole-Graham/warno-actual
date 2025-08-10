"""Functions for writing dictionary entries."""

from typing import List, Tuple

from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger

from .ui.traits import write_trait_texts
from .ui.unit_info_panel import write_info_panel_hints

logger = setup_logger(__name__)

def write_ammo_dictionary_entries(ingame_names: List[Tuple[str, str, str]], 
                                calibers: List[Tuple[str, str, str]]) -> None:
    """Write ammunition dictionary entries."""
    entries = []
    
    # Add weapon names
    for weapon, token, display in ingame_names:
        entries.append((token, display))
        
    # Add caliber entries
    for weapon, token, display in calibers:
        entries.append((token, display))
        
    if entries:
        write_dictionary_entries(entries, dictionary_type="units")

def write_missile_dictionary_entries(ingame_names: List[Tuple[str, str, str]], 
                                  calibers: List[Tuple[str, str, str]]) -> None:
    """Write missile dictionary entries."""
    entries = []
    
    # Add weapon names
    for weapon, token, display in ingame_names:
        entries.append((token, display))
        
    # Add caliber entries
    for weapon, token, display in calibers:
        entries.append((token, display))
        
    if entries:
        write_dictionary_entries(entries, dictionary_type="units")