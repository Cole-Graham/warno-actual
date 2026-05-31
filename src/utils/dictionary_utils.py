"""Utilities for handling dictionary/localization files."""

import csv
from pathlib import Path
from typing import List, Tuple  # noqa

from src import ModConfig
from src.utils.config_utils import get_mod_name
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Dictionary type to filename mapping
DICT_FILES = {
    "ingame": "INTERFACE_INGAME.csv",
    "outgame": "INTERFACE_OUTGAME.csv",
    "companies": "COMPANIES.csv",
    "platoons": "PLATOONS.csv",
    "units": "UNITS.csv"
}

# Track which files have been initialized this session
_initialized_files = set()


def initialize_dictionary_csv_files(force: bool = False) -> None:
    """Initialize empty CSV dictionary files under Localisation/{mod_name}/."""
    if force:
        _initialized_files.clear()

    logger.info("Initializing dictionary CSV files")
    for dict_type in DICT_FILES:
        dict_path = get_dictionary_path(DICT_FILES[dict_type])
        _initialize_dictionary_file(dict_path)
        _initialized_files.add(str(dict_path))


def get_dictionary_path(filename: str = "INTERFACE_INGAME.csv") -> Path:
    """Get the path to a dictionary file based on config.

    Args:
        filename: Name of the dictionary file

    Returns:
        Path to the dictionary file
    """
    config = ModConfig.get_instance().config_data
    warno_mods = Path(config['directories']['warno_mods'])
    mod_name = get_mod_name(config)
    base_game = config['directories']['base_game']

    if mod_name == base_game:
        raise ValueError(
            f"Mod name '{mod_name}' matches base_game '{base_game}'. "
            "This should not happen when constructing dictionary paths.",
        )

    dict_path = warno_mods / mod_name / "GameData/Localisation" / mod_name / filename
    logger.debug(f"Constructed dictionary path: {dict_path} (mod_name: {mod_name})")

    return dict_path


def _initialize_dictionary_file(dict_path: Path) -> None:
    """Initialize dictionary file with header."""
    if str(dict_path) in _initialized_files:
        return

    logger.info(f"Initializing dictionary file: {dict_path}")

    target_dir = Path(dict_path).parent
    target_dir.mkdir(parents=True, exist_ok=True)

    with open(dict_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        csvwriter.writerow(["TOKEN", "REFTEXT"])
        logger.debug(f"Created new dictionary file with header at {dict_path}")


def write_dictionary_entries(entries: List[Tuple[str, str]], dictionary_type: str = "units") -> None:
    """Write entries to dictionary file."""
    logger.info(f"Writing {len(entries)} entries to {dictionary_type} dictionary")

    if dictionary_type not in DICT_FILES:
        logger.error(f"Unknown dictionary type: {dictionary_type}")
        return

    unique_entries = {}
    for token, text in entries:
        if token in unique_entries:
            logger.debug(f"Duplicate token found: {token}")
        unique_entries[token] = text

    deduplicated = [(k, v) for k, v in unique_entries.items()]

    logger.info(
        f"Writing {len(deduplicated)} unique entries "
        f"(removed {len(entries) - len(deduplicated)} duplicates)",
    )

    dict_path = get_dictionary_path(DICT_FILES[dictionary_type])
    write_csv_entries(deduplicated, dict_path)


def write_csv_entries(entries: List[Tuple[str, str]], dict_path: Path) -> None:
    """Write entries to a CSV dictionary file."""
    logger.info(f"Attempting to write to: {dict_path}")

    dict_path.parent.mkdir(parents=True, exist_ok=True)

    existing_entries = set()
    if dict_path.exists():
        try:
            with open(dict_path, 'r', newline='', encoding='utf-8') as csvfile:
                logger.debug(f"Reading existing entries from {dict_path}")
                csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
                next(csvreader)  # Skip header row
                for row in csvreader:
                    if len(row) >= 2:
                        existing_entries.add((row[0], row[1]))
                logger.debug(f"Found {len(existing_entries)} existing entries")
        except Exception as e:
            logger.error(f"Error reading existing entries from {dict_path}: {e}")
    else:
        _initialize_dictionary_file(dict_path)
        _initialized_files.add(str(dict_path))

    added = 0
    skipped = 0

    try:
        with open(dict_path, 'a', newline='', encoding='utf-8') as csvfile:
            logger.debug(f"Opened {dict_path} for writing")
            csvwriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)

            for token, text in entries:
                if (token, text) not in existing_entries:
                    try:
                        csvwriter.writerow([token, text])
                        logger.debug(f"Successfully wrote entry: {token} = {text}")
                        added += 1
                    except Exception as e:
                        logger.error(f"Failed to write entry {token}: {e}")
                else:
                    logger.debug(f"Skipped duplicate entry: {token}")
                    skipped += 1

        logger.info(f"Added {added} entries, skipped {skipped} duplicates to {dict_path}")
    except Exception as e:
        logger.error(f"Failed to open/write to {dict_path}: {e}")
