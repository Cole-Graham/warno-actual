"""Database persistence utilities."""

import json
from pathlib import Path
from typing import Any, Dict

from src.utils.logging_utils import setup_logger

logger = setup_logger('database_utils')

def save_database_to_disk(database: Dict[str, Any]) -> None:
    """Save database components to disk."""
    db_dir = Path(__file__).parent / "database"
    db_dir.mkdir(parents=True, exist_ok=True)
    
    # Save each component
    for name, data in database.items():
        if name == "source_files":  # Skip source files, they're just for immediate use
            continue
            
        file_path = db_dir / f"{name}.json"
        logger.info(f"Saving {name} data ({len(data)} entries)")
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
            
        logger.debug(f"{name} data size: {file_path.stat().st_size} bytes")
    
    logger.info("Database saved successfully")

def load_database_from_disk() -> Dict[str, Any]:
    """Load database components from disk."""
    db_dir = Path(__file__).parent / "database"
    database = {}
    
    for file_path in db_dir.glob("*.json"):
        name = file_path.stem
        try:
            with open(file_path) as f:
                database[name] = json.load(f)
            logger.debug(f"Loaded {name} from disk")
        except Exception as e:
            logger.error(f"Error loading {name}: {e}")
            
    return database
    

