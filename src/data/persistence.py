"""Database persistence utilities."""

import json
from pathlib import Path
from typing import Any, Dict

from src.utils.logging_utils import setup_logger

logger = setup_logger('database_utils')

# Map database keys to filenames
DB_FILENAMES = {
    "unit_data": "unit_data.json",
    "weapons": "weapons.json",
    "ammunition": "ammunition.json",
    "depiction_data": "depiction_data.json"
}

def save_database_to_disk(database: Dict[str, Any]) -> None:
    """Save database components to disk."""
    db_dir = Path(__file__).parent / "database"
    db_dir.mkdir(parents=True, exist_ok=True)
    
    # Save each component
    for name, data in database.items():
        if name == "source_files":  # Skip source files, they're just for immediate use
            continue
            
        if name not in DB_FILENAMES:
            logger.warning(f"Unknown database component: {name}")
            continue
            
        file_path = db_dir / DB_FILENAMES[name]
        logger.info(f"Saving {name} data ({len(data)} entries)")
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
            
        logger.debug(f"{name} data size: {file_path.stat().st_size} bytes")
    
    logger.info("Database saved successfully")

def load_database_from_disk() -> Dict[str, Any]:
    """Load database components from disk."""
    db_dir = Path(__file__).parent / "database"
    database = {}
    
    for db_key, filename in DB_FILENAMES.items():
        file_path = db_dir / filename
        try:
            with open(file_path) as f:
                database[db_key] = json.load(f)
            logger.debug(f"Loaded {db_key} from disk")
        except Exception as e:
            logger.error(f"Error loading {db_key}: {e}")
            
    return database
    

