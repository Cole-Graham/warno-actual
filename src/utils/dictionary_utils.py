"""Utilities for handling dictionary/localization files."""

import csv
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

from src import ModConfig
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

def initialize_dictionary_files() -> None:
    """Initialize all dictionary files at start of patcher run."""
    logger.info("Initializing all dictionary files")
    
    # Get paths for all dictionary types
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
    is_dev = config['build_config']['write_dev']
    
    # Determine mod folder name
    if is_dev:
        mod_name = config['directories']['gameplay_dev']
    else:
        mod_name = config['directories']['gameplay_release']
        
    return warno_mods / mod_name / "GameData/Localisation" / mod_name / filename

def _initialize_dictionary_file(dict_path: str) -> None:
    """Initialize dictionary file with header."""
    # Skip if already initialized this session
    if str(dict_path) in _initialized_files:
        return
        
    logger.info(f"Initializing dictionary file: {dict_path}")
    
    # Ensure directory exists
    Path(dict_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Create new file with header
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
        
    # Convert to dict to remove duplicates, keeping last occurrence of each token
    unique_entries = {}
    for token, text in entries:
        if token in unique_entries:
            logger.debug(f"Duplicate token found: {token}")
        unique_entries[token] = text
    
    # Convert back to list of tuples
    deduplicated = [(k, v) for k, v in unique_entries.items()]
    
    logger.info(f"Writing {len(deduplicated)} unique entries (removed {len(entries) - len(deduplicated)} duplicates)")
    
    # Get dictionary path and write entries
    dict_path = get_dictionary_path(DICT_FILES[dictionary_type])
    write_csv_entries(deduplicated, dict_path)

def write_csv_entries(entries: List[Tuple[str, str]], dict_path: str) -> None:
    """Write entries to a CSV dictionary file."""
    logger.info(f"Attempting to write to: {dict_path}")
    
    # Read existing entries into a set for faster lookup
    existing_entries = set()
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
    
    # Track what we're adding
    added = 0
    skipped = 0
    
    # Write entries
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