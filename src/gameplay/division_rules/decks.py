"""Functions for modifying decks."""

from typing import Any, Dict, List, Tuple

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits
from src.data import decks
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

# temp until we create constants for editing decks
eighth_inf_deck = {
    "add": ["8th_M1A1_Abrams_US_1_1"],
}

def modify_decks(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Modify decks in Decks.ndf"""
    
    for pack in eighth_inf_deck["add"]:
        deck = source_path.by_n("Descriptor_Deck_US_8th_Inf_multi")
        pack_ref = f"~/Descriptor_Deck_Pack_{pack}"
        deck.v.by_m("DeckPackList").v.add(pack_ref)

