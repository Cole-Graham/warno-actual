"""Constants-dependent precomputation data generation.

This module handles generation of JSON data files that depend on constants (unit_edits, NEW_UNITS)
rather than game files. These JSON files are regenerated on every patcher run, even when
build_database is false. The "database" is just the collection of JSON files on disk.
"""

import json
from pathlib import Path
from typing import Any, Dict

from src.constants.weapons.vanilla_inst_modifications import (
    AMMUNITION_MISSILES_RENAMES,
    AMMUNITION_RENAMES,
)
from src.utils.config_utils import get_mod_src_path
from src.utils.database_utils import ensure_db_directory
from src.utils.logging_utils import setup_logger

from .deck_pack_mappings import build_deck_pack_mappings

logger = setup_logger(__name__)


def build_ammunition_renames(game_db: Dict[str, Any] = None) -> Dict[str, Dict[str, str]]:
    """Build ammunition renames from constants.
    
    Validates that old names exist in game_db before including them in renames.
    Logs warnings for old names that are not found in the game database.
    
    Args:
        game_db: Optional game database dict containing ammunition data
    
    Returns:
        Dict with renames_old_new and renames_new_old mappings based on constants
    """
    renames_old_new = {}
    
    # Build set of valid ammunition names from game_db if available
    valid_ammo_names = set()
    if game_db and "ammunition" in game_db:
        ammo_data = game_db["ammunition"]
        
        # Use the all_ammunition_and_missile list if available
        if "all_ammunition_and_missile" in ammo_data and isinstance(ammo_data["all_ammunition_and_missile"], list):
            valid_ammo_names = set(ammo_data["all_ammunition_and_missile"])
    
    # Add renames from constants, validating against game_db
    for old_name, new_name in AMMUNITION_RENAMES:
        if game_db and valid_ammo_names and old_name not in valid_ammo_names:
            logger.warning(f"Old ammunition name '{old_name}' not found in game_db, skipping rename")
        else:
            renames_old_new[old_name] = new_name
        
    for old_name, new_name in AMMUNITION_MISSILES_RENAMES:
        if game_db and valid_ammo_names and old_name not in valid_ammo_names:
            logger.warning(f"Old ammunition missile name '{old_name}' not found in game_db, skipping rename")
        else:
            renames_old_new[old_name] = new_name
    
    # Create reversed mapping
    renames_new_old = {v: k for k, v in renames_old_new.items()}
    
    return {
        "renames_old_new": renames_old_new,
        "renames_new_old": renames_new_old,
    }


def build_constants_precomputation_data(config: Dict[str, Any], game_db: Dict[str, Any] = None) -> Dict[str, Dict[str, str]]:
    """Build constants-dependent precomputation data and save as JSON files.
    
    This function always runs, regardless of build_database setting.
    It generates mappings based on current unit_edits and NEW_UNITS constants
    and saves them to constants_precomputation/deck_pack_mappings.json and
    constants_precomputation/ammunition_renames.json.
    
    Args:
        config: Configuration dict with database_path (path to JSON files) and mod_source_path
        game_db: Optional game_db dict used to validate ammunition renames
    
    Returns:
        Dict with deck_pack_mappings and ammunition_renames structure:
        {
            "deck_pack_modifications": {...},
            "reference_mappings": {...},
            "new_command_unit_deck_packs": {...},
            "ammunition_renames": {
                "renames_old_new": {...},
                "renames_new_old": {...}
            }
        }
    """
    logger.info("Building constants precomputation data")
    
    # Get mod_source_path to parse game files
    mod_source_path = get_mod_src_path(config)
    if not mod_source_path or not mod_source_path.exists():
        logger.error(f"Invalid mod_source_path: {mod_source_path}")
        return {
            "deck_pack_modifications": {},
            "reference_mappings": {},
            "new_command_unit_deck_packs": {},
            "ammunition_renames": {"renames_old_new": {}, "renames_new_old": {}},
        }
    
    try:
        # Build mappings by parsing game files
        # build_deck_pack_mappings filters at runtime using unit_edits and NEW_UNITS
        mappings = build_deck_pack_mappings(mod_source_path)
        
        # Build ammunition renames from constants
        ammunition_renames = build_ammunition_renames(game_db)
        
        # Save deck_pack_mappings to separate JSON file
        save_constants_precomputation_data(mappings, config)
        
        # Save ammunition_renames to separate JSON file
        save_ammunition_renames(ammunition_renames, config)
        
        # Add ammunition_renames to return dict for convenience
        mappings["ammunition_renames"] = ammunition_renames
        
        logger.info(
            f"Constants precomputation data built and saved: "
            f"{len(mappings.get('deck_pack_modifications', {}))} modifications, "
            f"{len(mappings.get('reference_mappings', {}))} references, "
            f"{len(mappings.get('new_command_unit_deck_packs', {}))} new command unit deck packs, "
            f"{len(ammunition_renames.get('renames_old_new', {}))} ammunition renames"
        )
        return mappings
    except Exception as e:
        logger.error(f"Failed to build constants precomputation data: {e}", exc_info=True)
        return {
            "deck_pack_modifications": {},
            "reference_mappings": {},
            "new_command_unit_deck_packs": {},
            "ammunition_renames": {"renames_old_new": {}, "renames_new_old": {}},
        }


def load_constants_precomputation_data(config: Dict[str, Any]) -> Dict[str, Dict[str, str]]:
    """Load constants precomputation data from JSON files on disk.
    
    Args:
        config: Configuration dict with database_path (path to JSON files directory)
    
    Returns:
        Dict with deck_pack_mappings and ammunition_renames structure, or empty dict if files don't exist
    """
    db_path = Path(config["data_config"]["database_path"])
    mappings_file = db_path / "constants_precomputation" / "deck_pack_mappings.json"
    renames_file = db_path / "constants_precomputation" / "ammunition_renames.json"
    
    mappings = {
        "deck_pack_modifications": {},
        "reference_mappings": {},
        "new_command_unit_deck_packs": {},
    }
    
    # Load deck_pack_mappings
    if mappings_file.exists():
        try:
            with open(mappings_file) as f:
                mappings.update(json.load(f))
            logger.debug("Loaded deck_pack_mappings from disk")
            # Ensure all expected keys exist
            if "new_command_unit_deck_packs" not in mappings:
                mappings["new_command_unit_deck_packs"] = {}
        except Exception as e:
            logger.error(f"Failed to load deck_pack_mappings: {e}")
    else:
        logger.debug("Deck pack mappings file not found")
    
    # Load ammunition_renames
    if renames_file.exists():
        try:
            with open(renames_file) as f:
                mappings["ammunition_renames"] = json.load(f)
            logger.debug("Loaded ammunition_renames from disk")
        except Exception as e:
            logger.error(f"Failed to load ammunition_renames: {e}")
            mappings["ammunition_renames"] = {"renames_old_new": {}, "renames_new_old": {}}
    else:
        logger.debug("Ammunition renames file not found")
        mappings["ammunition_renames"] = {"renames_old_new": {}, "renames_new_old": {}}
    
    return mappings


def save_constants_precomputation_data(data: Dict[str, Dict[str, str]], config: Dict[str, Any]) -> None:
    """Save deck_pack_mappings data as JSON file to disk.
    
    Args:
        data: Dict with deck_pack_mappings structure (without ammunition_renames)
        config: Configuration dict with database_path (path to JSON files directory)
    """
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    
    # Create directory if needed
    ensure_db_directory(str(constants_dir))
    
    # Remove ammunition_renames if present (it's saved separately)
    save_data = {k: v for k, v in data.items() if k != "ammunition_renames"}
    
    # Save as JSON file: constants_precomputation/deck_pack_mappings.json
    mappings_file = constants_dir / "deck_pack_mappings.json"
    try:
        with open(mappings_file, "w") as f:
            json.dump(save_data, f, indent=2, sort_keys=True)
        logger.debug(f"Saved deck_pack_mappings to {mappings_file}")
    except Exception as e:
        logger.error(f"Failed to save deck_pack_mappings: {e}")
        raise


def save_ammunition_renames(renames: Dict[str, Dict[str, str]], config: Dict[str, Any]) -> None:
    """Save ammunition renames data as JSON file to disk.
    
    Args:
        renames: Dict with renames_old_new and renames_new_old structure
        config: Configuration dict with database_path (path to JSON files directory)
    """
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    
    # Create directory if needed
    ensure_db_directory(str(constants_dir))
    
    # Save as JSON file: constants_precomputation/ammunition_renames.json
    renames_file = constants_dir / "ammunition_renames.json"
    try:
        with open(renames_file, "w") as f:
            json.dump(renames, f, indent=2, sort_keys=True)
        logger.debug(f"Saved ammunition_renames to {renames_file}")
    except Exception as e:
        logger.error(f"Failed to save ammunition_renames: {e}")
        raise

