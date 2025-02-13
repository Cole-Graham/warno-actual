"""Functions for gathering deck data from game files."""

from pathlib import Path
from typing import Any, Dict, List  # noqa

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import strip_quotes

logger = setup_logger('deck_data')


def gather_deck_data(mod_src_path: Path) -> Dict[str, Any]:
    """Gather deck data from Decks.ndf.
    
    Returns:
        Dict with categories of decks:
        {
            "multi": {
                "deck_name": {
                    "token": str,
                    "packs": List[str]
                }
            },
            # Other categories can be added later
        }
    """
    logger.info("Gathering deck data from Decks.ndf")
    
    # Initialize deck data structure with categories
    deck_data = {
        "multi": {}  # Only multi decks for now
    }
    ndf_path = r"GameData\Generated\Gameplay\Decks\Decks.ndf"
    
    try:
        # Just parsing input, no output needed
        mod = ndf.Mod(str(mod_src_path), "None")
        parse_source = mod.parse_src(ndf_path)
        
        multi_decks = 0  # Counter for multi decks
        
        for deck_row in parse_source:
            # Skip non-deck entries
            if not hasattr(deck_row, 'namespace'):
                continue
                
            namespace = deck_row.namespace
            
            # Process decks based on type
            if namespace.startswith("Descriptor_Deck_") and namespace.endswith("_multi"):
                # Extract deck name (remove prefix and suffix)
                deck_name = namespace.replace("Descriptor_Deck_", "").replace("_multi", "")
                
                try:
                    # Get deck token name
                    deck_token = strip_quotes(deck_row.v.by_m("DeckName").v)  # noqa
                    
                    # Get pack list
                    pack_list = []
                    for pack in deck_row.v.by_m("DeckPackList").v:  # noqa
                        # Remove ~/ prefix from pack names
                        pack_name = pack.v.replace("~/", "")
                        pack_list.append(pack_name)
                    
                    # Store under multi category
                    deck_data["multi"][deck_name] = {
                        "token": deck_token,
                        "packs": pack_list
                    }
                    
                    multi_decks += 1
                    logger.debug(f"Gathered data for multiplayer deck: {deck_name}")
                    
                except Exception as e:
                    logger.error(f"Failed to gather data for deck {deck_name}: {str(e)}")
                    continue
    
    except Exception as e:
        logger.error(f"Error gathering deck data: {str(e)}")
        raise
    
    logger.info(f"Gathered data for {multi_decks} multiplayer decks")
    return deck_data
