"""Data building functionality."""

from typing import Dict

from src.utils.logging_utils import setup_logger

from .ammo_data import build_ammo_data

logger = setup_logger(__name__)


def build_database(source_files: Dict) -> Dict:
    """Build complete game data database.
    
    Args:
        source_files: Dictionary of NDF file paths to their parsed contents
        
    Returns:
        Dictionary containing all game data
    """
    logger.info("Building game database...")
    
    return {
        "ammunition": build_ammo_data(source_files),
        # Add other data categories here
    }
