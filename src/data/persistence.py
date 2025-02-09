"""Database persistence utilities."""

import json
from pathlib import Path
from typing import Any, Dict

from src.utils.database_utils import ensure_db_directory
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Map database keys to filenames
DB_FILENAMES = {
    "unit_data": "unit_data.json",
    "weapons": "weapons.json",
    "ammunition": "ammunition.json",
    "depiction_data": "depiction_data.json",
    "decks": "decks.json"
}

def save_database_to_disk(database: Dict[str, Any], config: Dict) -> None:
    """Save database to disk."""
    try:
        db_path = Path(config['data_config']['database_path'])
        ensure_db_directory(str(db_path))
        
        # Save each component
        for key, data in database.items():
            if key == "source_files":  # Skip source files
                continue
                
            if key not in DB_FILENAMES:
                logger.warning(f"Unknown database component: {key}")
                continue
                
            file_path = db_path / DB_FILENAMES[key]
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
                
        logger.info("Database saved to disk")
    except Exception as e:
        logger.error(f"Failed to save database: {e}")
        raise

def load_database_from_disk(config: Dict) -> Dict[str, Any]:
    """Load database components from disk."""
    db_path = Path(config['data_config']['database_path'])
    database = {}
    
    for db_key, filename in DB_FILENAMES.items():
        file_path = db_path / filename
        try:
            with open(file_path) as f:
                database[db_key] = json.load(f)
            logger.debug(f"Loaded {db_key} from disk")
        except Exception as e:
            logger.error(f"Error loading {db_key}: {e}")
            
    return database
    

