"""Data management module."""

from typing import Any, Dict

from src.utils.config_utils import get_source_path
from src.utils.logging_utils import setup_logger

from .ammo_data import build_ammo_data
from .depiction_data import gather_depiction_data
from .persistence import load_database_from_disk, save_database_to_disk
from .source_loader import get_source_files
from .unit_data import gather_unit_data, gather_weapon_data

logger = setup_logger(__name__)


def build_database(config: Dict[str, Any]) -> Dict[str, Any]:
    """Build or update the database with game data.
    
    This is the main entry point for database operations.
    Orchestrates the build process and handles persistence.
    """
    logger.info("Starting database build process")
    
    try:
        # Check if we should build/rebuild the database
        if not config.get("data_config", {}).get("build_database", True):
            logger.info("Using existing database")
            return load_database_from_disk()
            
        # Load source files once and reuse
        source_files = get_source_files(config)
        if not source_files:
            logger.error("Failed to load source files")
            return {}
        
        # Get paths for data gathering
        source_path = get_source_path(config)
        
        # Build database components
        database = {
            "source_files": source_files,
            "ammunition": build_ammo_data(source_path),
            "unit_data": gather_unit_data(source_path),
            "weapon_data": gather_weapon_data(source_path),
            "depiction_data": gather_depiction_data(source_path)
        }
        
        # Save to disk for future use
        save_database_to_disk(database)
        
        return database
        
    except Exception as e:
        logger.error(f"Database build failed: {str(e)}")
        raise
