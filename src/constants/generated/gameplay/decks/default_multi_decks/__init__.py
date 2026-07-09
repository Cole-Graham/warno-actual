"""Default multiplayer deck loadouts keyed by division cfg_name."""

from typing import Dict

from src.utils.logging_utils import setup_logger

from .SOV_default_multi_decks import sov_default_multi_decks
from .US_default_multi_decks import us_default_multi_decks

logger = setup_logger(__name__)

__all__ = ["load_default_multi_decks"]


def load_default_multi_decks() -> Dict:
    """Load and merge all default multiplayer deck dictionaries."""
    merged_decks = {}
    merged_decks.update(us_default_multi_decks)
    merged_decks.update(sov_default_multi_decks)
    logger.info(f"Loaded default multiplayer decks for {len(merged_decks)} divisions")
    return merged_decks
