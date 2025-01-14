"""Utilities for handling dictionary/localization files."""

import csv
from pathlib import Path
from typing import Dict, List, Set, Tuple

from src import ModConfig
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def get_dictionary_path(config: Dict, filename: str = "INTERFACE_INGAME.csv") -> Path:
    """Get the path to a dictionary file based on config.
    
    Args:
        config: Configuration dictionary
        filename: Name of the dictionary file
        
    Returns:
        Path to the dictionary file
    """
    warno_mods = Path(config['directories']['warno_mods'])
    is_dev = config['build_config']['write_dev']
    
    # Determine mod folder name
    if is_dev:
        mod_name = config['directories']['gameplay_dev']
    else:
        mod_name = config['directories']['gameplay_release']
        
    return warno_mods / mod_name / "GameData/Localisation" / mod_name / filename

def write_dictionary_entries(
    entries: List[Tuple[str, str]], 
    config: Dict,
    filename: str = "INTERFACE_INGAME.csv"
) -> None:
    """Write entries to a dictionary file if they don't already exist.
    
    Args:
        entries: List of (token, text) tuples to write
        config: Configuration dictionary
        filename: Name of the dictionary file
    """
    dict_path = get_dictionary_path(config, filename)
    
    # Ensure directory exists
    dict_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Read existing entries
    existing_entries: Set[Tuple[str, str]] = set()
    if dict_path.exists():
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
                logger.info(f"Added dictionary entry: {token}") 