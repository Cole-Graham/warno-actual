"""Database utilities for versioning and validation."""
import hashlib
import json
import os
import subprocess
from pathlib import Path
from typing import Dict

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def ensure_db_directory(db_path: str) -> None:
    """Create database directory if it doesn't exist."""
    Path(db_path).mkdir(parents=True, exist_ok=True)

def calculate_db_checksum(db_data: Dict) -> str:
    """Calculate checksum of database content."""
    # Sort the data to ensure consistent checksums
    serialized = json.dumps(db_data, sort_keys=True)
    return hashlib.sha256(serialized.encode()).hexdigest()

def get_database_metadata_path(db_path: str) -> Path:
    """Get the path for database metadata files.
    Prepends 'src' to the database path."""
    return Path("src") / db_path

def save_db_metadata(db_path: str, checksum: str, config: Dict):
    """Save database metadata including version and checksum."""
    # Get src/data/database path for metadata
    metadata_path = get_database_metadata_path(db_path)
    ensure_db_directory(str(metadata_path))
    
    metadata = {
        "checksum": checksum,
        "last_updated": str(metadata_path.stat().st_mtime)
    }
    
    # Save local metadata to src/data/database
    meta_path = metadata_path / "db_metadata.json"
    with open(meta_path, 'w') as f:
        json.dump(metadata, f, indent=2)
        
    # If configured, update master metadata in same directory
    if config['data_config'].get('update_master_metadata', False):
        master_meta_path = metadata_path / "master_db_metadata.json"
        with open(master_meta_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        logger.info("Updated master database metadata")

def verify_database(config: Dict) -> bool:
    """Verify database exists and matches current version."""
    try:
        db_path = Path(config['data_config']['database_path'])
        metadata_path = get_database_metadata_path(str(db_path))
        
        # First check master metadata (source of truth)
        master_meta_path = metadata_path / "master_db_metadata.json"
        if not master_meta_path.exists():
            logger.error("Master database metadata not found")
            return False
            
        with open(master_meta_path) as f:
            master_metadata = json.load(f)
            
        # Check if database exists
        if not db_path.exists():
            logger.warning("Database directory not found - rebuild recommended")
            return False
            
        # Get all JSON files in database directory
        json_files = list(db_path.glob("*.json"))
        if not json_files:
            logger.warning("No database files found - rebuild recommended")
            return False
            
        # Load and verify checksum of current database
        combined_data = {}
        for file_path in json_files:
            with open(file_path) as f:
                combined_data[file_path.name] = json.load(f)
                
        # Compare checksum with master
        current_checksum = calculate_db_checksum(combined_data)
        if current_checksum != master_metadata.get("checksum"):
            logger.warning("Database checksum mismatch with master - rebuild recommended")
            return False
            
        return True
        
    except Exception as e:
        logger.error(f"Error verifying database: {e}")
        return False 