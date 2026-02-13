"""Database building and management."""

import json
from pathlib import Path
from typing import Any, Dict

from src.utils.config_utils import get_mod_src_path
from src.utils.database_utils import calculate_db_checksum, save_db_metadata
from src.utils.logging_utils import setup_logger

from .ammo_data import build_ammo_data
from .deck_pack_mappings import build_deck_pack_data
from .decks import gather_deck_data
from .depiction_data import gather_depiction_data
from .order_types_data import (
    compare_order_types_with_previous,
    gather_order_types,
)
from .persistence import load_database_from_disk, save_database_to_disk
from .source_loader import get_source_files
from .unit_data import (
    build_all_tags,
    build_upgrade_from_mapping,
    compare_tags_with_previous,
    gather_unit_data,
    gather_weapon_data,
)

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
            _database_cache = load_database_from_disk(config=config)
            return _database_cache

        # Load source files once and reuse
        source_files = get_source_files(config)
        if not source_files:
            logger.error("Failed to load source files")
            return {}

        # Get paths for data gathering
        mod_source_path = get_mod_src_path(config)

        # Build database components
        # Note: deck_pack_mappings moved to constants_precomputation (generated separately)
        unit_data = gather_unit_data(mod_source_path)
        order_types_data = gather_order_types(mod_source_path)
        all_tags_list = build_all_tags(unit_data)["all_tags"]
        unit_data["all_tags"] = all_tags_list
        _database_cache = {
            "source_files": source_files,
            "ammunition": build_ammo_data(mod_source_path),
            "unit_data": unit_data,
            "weapons": gather_weapon_data(mod_source_path),
            "depiction_data": gather_depiction_data(mod_source_path),
            "decks": gather_deck_data(mod_source_path),
            "deck_pack_data": build_deck_pack_data(mod_source_path),
            "order_types": order_types_data,
            "upgrade_from_mapping": build_upgrade_from_mapping(unit_data),
        }

        db_path = Path(config["data_config"]["database_path"])

        # Compare tags with previous build (vanilla game data) and log warnings if changed
        previous_unit_data_path = db_path / "unit_data.json"
        if previous_unit_data_path.exists():
            try:
                with open(previous_unit_data_path) as f:
                    previous_unit_data = json.load(f)
                previous_tags_list = previous_unit_data.get("all_tags", [])
                compare_tags_with_previous(all_tags_list, previous_tags_list)
            except Exception as e:
                logger.debug("Could not compare with previous tags: %s", e)

        # Compare order types with previous build and log warnings if changed
        previous_order_types_path = db_path / "order_types.json"
        if previous_order_types_path.exists():
            try:
                with open(previous_order_types_path) as f:
                    previous = json.load(f)
                previous_list = previous.get("all_order_types", [])
                compare_order_types_with_previous(
                    order_types_data.get("all_order_types", []),
                    previous_list,
                )
            except Exception as e:
                logger.debug("Could not compare with previous order types: %s", e)

        logger.info(f"Built database with {len(_database_cache['unit_data'])} units")
        logger.info(f"Built database with {len(_database_cache['weapons'])} weapons")
        logger.info(f"Built database with {len(_database_cache['ammunition'])} ammunition entries")
        logger.info(f"Built database with {len(_database_cache['depiction_data'])} depiction entries")
        logger.info(f"Built database with {len(_database_cache['decks'])} deck entries")
        logger.info(
            f"Built database with {len(_database_cache['deck_pack_data']['base_units'])} base units in deck pack data"
        )
        logger.info(
            f"Built database with {len(_database_cache['upgrade_from_mapping'])} UpgradeFrom relationships"
        )
        logger.info(
            f"Built database with {len(_database_cache['order_types']['all_order_types'])} order types"
        )
        logger.info(
            f"Built database with {len(_database_cache['unit_data']['all_tags'])} tags (excluding UNITE_*)"
        )

        # Save to disk for future use
        save_database_to_disk(_database_cache, config)

        # After building database, save metadata
        # Get all JSON files in database directory except metadata files and constants_precomputation
        db_path = Path(config["data_config"]["database_path"])
        excluded_files = {"db_metadata.json", "master_db_metadata.json"}
        # Exclude constants_precomputation subfolder from checksum (it's regenerated on every run)
        db_files = [
            f for f in db_path.glob("*.json")
            if f.name not in excluded_files and f.parent.name != "constants_precomputation"
        ]

        # Combine all database files into single dict for checksum
        db_data = {}
        for file in db_files:
            with open(file) as f:
                db_data[file.stem] = json.load(f)

        checksum = calculate_db_checksum(db_data)
        save_db_metadata(config["data_config"]["database_path"], checksum, config)

        return _database_cache

    except Exception as e:
        logger.error(f"Database build failed: {str(e)}")
        raise
