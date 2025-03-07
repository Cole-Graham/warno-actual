"""Database utilities for versioning and validation."""
import hashlib
import json
# import os
# import subprocess
from pathlib import Path
from typing import Any, Dict

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def ensure_db_directory(db_path: str) -> None:
    """Create database directory if it doesn't exist."""
    Path(db_path).mkdir(parents=True, exist_ok=True)


def _sort_dict_recursively(d: Any) -> Any:
    """Sort dictionary recursively to ensure consistent ordering."""
    if isinstance(d, dict):
        return {k: _sort_dict_recursively(v) for k, v in sorted(d.items())}
    elif isinstance(d, list):
        return [_sort_dict_recursively(x) for x in d]
    return d


def calculate_db_checksum(db_data: Dict) -> str:
    """Calculate checksum of database content."""
    # Sort data recursively to ensure consistent ordering
    sorted_data = _sort_dict_recursively(db_data)
    
    # Log each component's data for debugging
    for key in sorted(sorted_data.keys()):
        component_json = json.dumps(sorted_data[key], sort_keys=True, ensure_ascii=True, separators=(',', ':'))
        component_hash = hashlib.sha256(component_json.encode('utf-8')).hexdigest()
        logger.debug(f"Component {key} hash: {component_hash}")
    
    # Use dumps with sort_keys and ensure_ascii for consistent serialization
    serialized = json.dumps(
        sorted_data,
        sort_keys=True,
        ensure_ascii=True,
        separators=(',', ':')
    )
    
    # Log first 100 chars of serialized data for debugging
    logger.debug(f"First 100 chars of serialized data: {serialized[:100]}")
    
    return hashlib.sha256(serialized.encode('utf-8')).hexdigest()


def get_database_path(db_path: str) -> Path:
    """Get the path to the database directory."""
    return Path(db_path)


def save_db_metadata(db_path: str, checksum: str, config: Dict):
    """Save database metadata including version and checksum."""
    db_path = get_database_path(db_path)
    ensure_db_directory(str(db_path))
    
    metadata = {
        "checksum": checksum,
        "last_updated": str(db_path.stat().st_mtime)
    }
    
    # Save local metadata
    meta_path = db_path / "db_metadata.json"
    with open(meta_path, 'w') as f:
        json.dump(metadata, f, indent=2)
        
    # If configured, update master metadata
    if config['data_config'].get('update_master_metadata', False):
        master_meta_path = db_path / "master_db_metadata.json"
        with open(master_meta_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        logger.info("Updated master database metadata")


def verify_database(config: Dict) -> bool:
    """Verify database exists and matches current version."""
    try:
        db_path = get_database_path(config['data_config']['database_path'])
        
        # First check master metadata (source of truth)
        master_meta_path = db_path / "master_db_metadata.json"
        if not master_meta_path.exists():
            logger.error("Master database metadata not found")
            return False
            
        with open(master_meta_path) as f:
            master_metadata = json.load(f)
            
        # Check local metadata
        local_meta_path = db_path / "db_metadata.json"
        if not local_meta_path.exists():
            logger.warning("Local database metadata not found - rebuild recommended")
            return False
            
        with open(local_meta_path) as f:
            local_metadata = json.load(f)
            
        # Just compare the checksums from the metadata files
        if local_metadata.get("checksum") != master_metadata.get("checksum"):
            logger.warning("Database checksum mismatch with master - rebuild recommended")
            return False
            
        return True
        
    except Exception as e:
        logger.error(f"Error verifying database: {e}")
        return False
