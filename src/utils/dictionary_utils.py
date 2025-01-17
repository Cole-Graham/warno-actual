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

def write_dictionary_entries(entries: List[Tuple[str, str]], dictionary_type: str = "units") -> None:
    """Write entries to dictionary file.
    
    Args:
        entries: List of (token, text) tuples
        dictionary_type: Type of dictionary ("units" or "ingame")
    """
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
    
    # Get dictionary path
    dict_path = get_dictionary_path(DICT_FILES[dictionary_type])
    
    write_csv_entries(deduplicated, dict_path)

def write_csv_entries(entries: List[Tuple[str, str]], dict_path: str) -> None:
    """Write entries to a CSV dictionary file.
    
    Args:
        entries: List of (token, text) tuples to write
        dict_path: Path to the dictionary file
    """
    # Ensure directory exists
    Path(dict_path).parent.mkdir(parents=True, exist_ok=True)
    
    # Read existing entries
    existing_entries: Set[Tuple[str, str]] = set()
    if Path(dict_path).exists():
        with open(dict_path, 'r', newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';', quotechar='"')
            existing_entries = {tuple(row) for row in csvreader}
    
    # Write new entries
    with open(dict_path, 'a', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(
            csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        
        for token, text in entries:
            if (token, text) not in existing_entries:
                csvwriter.writerow([token, text])
                logger.debug(f"Added dictionary entry: {token}")