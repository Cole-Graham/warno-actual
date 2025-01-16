"""Database building and management."""

from typing import Any, Dict

from src.utils.config_utils import get_source_path
from src.utils.logging_utils import setup_logger

from .ammo_data import build_ammo_data
from .depiction_data import gather_depiction_data
from .persistence import load_database_from_disk, save_database_to_disk
from .source_loader import get_source_files
from .unit_data import gather_unit_data, gather_weapon_data

logger = setup_logger(__name__)

# Cache for database
_database_cache = None

def build_database(config: Dict[str, Any]) -> Dict[str, Any]:
    """Build or update the database with game data."""
    global _database_cache
    
    if _database_cache is not None:
        logger.debug("Using cached database")
        return _database_cache
        
    logger.info("Starting database build process")
    
    try:
        # Check if we should build/rebuild the database
        if not config.get("data_config", {}).get("build_database", True):
            logger.info("Using existing database")
            _database_cache = load_database_from_disk()
            return _database_cache
            
        # Load source files once and reuse
        source_files = get_source_files(config)
        if not source_files:
            logger.error("Failed to load source files")
            return {}
        
        # Get paths for data gathering
        source_path = get_source_path(config)
        
        # Build database components
        _database_cache = {
            "source_files": source_files,
            "ammunition": build_ammo_data(source_path),
            "unit_data": gather_unit_data(source_path),
            "weapons": gather_weapon_data(source_path),
            "depiction_data": gather_depiction_data(source_path)
        }
        
        logger.info(f"Built database with {len(_database_cache['unit_data'])} units")
        logger.info(f"Built database with {len(_database_cache['weapons'])} weapons")
        logger.info(f"Built database with {len(_database_cache['ammunition'])} ammunition entries")
        logger.info(f"Built database with {len(_database_cache['depiction_data'])} depiction entries")
        
        # Save to disk for future use
        save_database_to_disk(_database_cache)
        
        return _database_cache
        
    except Exception as e:
        logger.error(f"Database build failed: {str(e)}")
        raise
