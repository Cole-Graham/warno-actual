"""Constants-dependent precomputation data generation.

This module handles generation of JSON data files that depend on constants (unit_edits, NEW_UNITS)
rather than game files. These JSON files are regenerated on every patcher run, even when
build_database is false. The "database" is just the collection of JSON files on disk.
"""

import json
from pathlib import Path
from typing import Any, Dict

from src.utils.config_utils import get_mod_src_path
from src.utils.database_utils import ensure_db_directory
from src.utils.logging_utils import setup_logger

from .deck_pack_mappings import build_deck_pack_mappings

logger = setup_logger(__name__)


def build_constants_precomputation_data(config: Dict[str, Any], game_db: Dict[str, Any] = None) -> Dict[str, Dict[str, str]]:
    """Build constants-dependent precomputation data and save as JSON file.
    
    This function always runs, regardless of build_database setting.
    It generates mappings based on current unit_edits and NEW_UNITS constants
    and saves them to constants_precomputation/deck_pack_mappings.json.
    
    Args:
        config: Configuration dict with database_path (path to JSON files) and mod_source_path
        game_db: Optional game_db dict (not used, kept for compatibility)
    
    Returns:
        Dict with deck_pack_mappings structure:
        {
            "deck_pack_modifications": {...},
            "reference_mappings": {...},
            "new_command_unit_deck_packs": {...}
        }
    """
    logger.info("Building constants precomputation data")
    
    # Get mod_source_path to parse game files
    mod_source_path = get_mod_src_path(config)
    if not mod_source_path or not mod_source_path.exists():
        logger.error(f"Invalid mod_source_path: {mod_source_path}")
        return {"deck_pack_modifications": {}, "reference_mappings": {}}
    
    try:
        # Build mappings by parsing game files
        # build_deck_pack_mappings filters at runtime using unit_edits and NEW_UNITS
        mappings = build_deck_pack_mappings(mod_source_path)
        
        # Save JSON file to constants_precomputation subfolder
        save_constants_precomputation_data(mappings, config)
        
        logger.info(
            f"Constants precomputation data built and saved: "
            f"{len(mappings.get('deck_pack_modifications', {}))} modifications, "
            f"{len(mappings.get('reference_mappings', {}))} references, "
            f"{len(mappings.get('new_command_unit_deck_packs', {}))} new command unit deck packs"
        )
        return mappings
    except Exception as e:
        logger.error(f"Failed to build constants precomputation data: {e}", exc_info=True)
        return {
            "deck_pack_modifications": {},
            "reference_mappings": {},
            "new_command_unit_deck_packs": {},
        }


def load_constants_precomputation_data(config: Dict[str, Any]) -> Dict[str, Dict[str, str]]:
    """Load constants precomputation data from JSON file on disk.
    
    Args:
        config: Configuration dict with database_path (path to JSON files directory)
    
    Returns:
        Dict with deck_pack_mappings structure, or empty dict if file doesn't exist
    """
    db_path = Path(config["data_config"]["database_path"])
    mappings_file = db_path / "constants_precomputation" / "deck_pack_mappings.json"
    
    if not mappings_file.exists():
        logger.debug("Constants precomputation data not found, returning empty dict")
        return {
            "deck_pack_modifications": {},
            "reference_mappings": {},
            "new_command_unit_deck_packs": {},
        }
    
    try:
        with open(mappings_file) as f:
            mappings = json.load(f)
        logger.debug("Loaded constants precomputation data from disk")
        # Ensure all expected keys exist (for backward compatibility)
        if "new_command_unit_deck_packs" not in mappings:
            mappings["new_command_unit_deck_packs"] = {}
        return mappings
    except Exception as e:
        logger.error(f"Failed to load constants precomputation data: {e}")
        return {
            "deck_pack_modifications": {},
            "reference_mappings": {},
            "new_command_unit_deck_packs": {},
        }


def save_constants_precomputation_data(data: Dict[str, Dict[str, str]], config: Dict[str, Any]) -> None:
    """Save constants precomputation data as JSON file to disk.
    
    Args:
        data: Dict with deck_pack_mappings structure
        config: Configuration dict with database_path (path to JSON files directory)
    """
    db_path = Path(config["data_config"]["database_path"])
    constants_dir = db_path / "constants_precomputation"
    
    # Create directory if needed
    ensure_db_directory(str(constants_dir))
    
    # Save as JSON file: constants_precomputation/deck_pack_mappings.json
    mappings_file = constants_dir / "deck_pack_mappings.json"
    try:
        with open(mappings_file, "w") as f:
            json.dump(data, f, indent=2, sort_keys=True)
        logger.debug(f"Saved constants precomputation data to {mappings_file}")
    except Exception as e:
        logger.error(f"Failed to save constants precomputation data: {e}")
        raise

