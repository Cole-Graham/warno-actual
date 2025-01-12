import json
from pathlib import Path
from typing import Any, Dict

from src.data.unit_data import gather_unit_data, gather_weapon_data
from src.utils.config_utils import get_destination_path, get_source_paths
from src.utils.logging_utils import setup_logger

logger = setup_logger('database')

def build_database(config: Dict[str, Any]) -> None:
    """Build or update the database with game data."""
    logger.info("Starting database build process")
    
    try:
        if not config.get("data_config", {}).get("build_database", True):
            logger.info("Database build skipped as per configuration")
            return
            
        # Create database directory relative to this file
        db_dir = Path(__file__).parent / "database"
        logger.info(f"Using database directory: {db_dir}")
        db_dir.mkdir(parents=True, exist_ok=True)
        
        # Get full source and destination paths from config
        source_paths = get_source_paths(config)
        dest_path = get_destination_path(config)
        
        # Use base game path for gathering data
        base_game_path = source_paths[-1]  # Base game is always last in the list
        unit_data = gather_unit_data(base_game_path, dest_path)
        logger.info("Gathering weapon data...")
        weapon_data = gather_weapon_data(base_game_path)
        
        # Save unit data
        unit_db_path = db_dir / "units.json"
        weapon_db_path = db_dir / "weapons.json"
        
        logger.info(f"Saving unit data ({len(unit_data)} entries)")
        with open(unit_db_path, 'w') as f:
            json.dump(unit_data, f, indent=2)
            
        logger.info(f"Saving weapon data ({len(weapon_data)} entries)")
        with open(weapon_db_path, 'w') as f:
            json.dump(weapon_data, f, indent=2)
            
        logger.debug(f"Unit data size: {unit_db_path.stat().st_size} bytes")
        logger.debug(f"Weapon data size: {weapon_db_path.stat().st_size} bytes")
        
        logger.info("Database build completed successfully")
        
    except Exception as e:
        logger.error(f"Database build failed: {str(e)}")
        raise

def load_data(config: Dict[str, Any], data_type: str) -> Dict[str, Any]:
    """Load specific data from the database."""
    try:
        # Use same path as build_database
        db_dir = Path(__file__).parent / "database"
        data_path = db_dir / f"{data_type}.json"
        
        if not data_path.exists():
            logger.warning(f"No {data_type} data found in database")
            return {}
            
        with open(data_path) as f:
            return json.load(f)
            
    except Exception as e:
        logger.error(f"Error loading {data_type} data: {str(e)}")
        return {}
    

