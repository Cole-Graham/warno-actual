"""Utilities for handling dictionary/localization files."""

import csv
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple  # noqa

from src import ModConfig
from src.utils.config_utils import get_mod_dst_path, get_mod_src_path
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
    
    config = ModConfig.get_instance().config_data
    is_dev = config['build_config']['write_dev']
    build_target_cfg = config['build_config']['target']
    base_game = config['directories']['base_game']
    
    # Determine mod folder name (same logic as get_dictionary_path)
    if is_dev and build_target_cfg == "gameplay":
        mod_name = config['directories']['gameplay_dev']
    elif is_dev and build_target_cfg == "ui_only":
        mod_name = config['directories']['ui_only_dev']
    elif not is_dev and build_target_cfg == "gameplay":
        mod_name = config['directories']['gameplay_release']
    elif not is_dev and build_target_cfg == "ui_only":
        mod_name = config['directories']['ui_only_release']
    else:
        mod_name = None
    
    # Check and fix LocalisationDicos.ndf once at startup
    if mod_name:
        warno_mods = Path(config['directories']['warno_mods'])
        localisation_dir = warno_mods / mod_name / "GameData" / "Localisation"
        base_game_subdir = localisation_dir / base_game
        _check_and_fix_localisation_dicos(localisation_dir, base_game_subdir, base_game, mod_name, config)
    
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
    build_target_cfg = config['build_config']['target']
    base_game = config['directories']['base_game']
    
    # Determine mod folder name
    if is_dev and build_target_cfg == "gameplay":
        mod_name = config['directories']['gameplay_dev']
    
    elif is_dev and build_target_cfg == "ui_only":
        mod_name = config['directories']['ui_only_dev']
    
    elif not is_dev and build_target_cfg == "gameplay":
        mod_name = config['directories']['gameplay_release']
    
    elif not is_dev and build_target_cfg == "ui_only":
        mod_name = config['directories']['ui_only_release']
    
    else:
        raise ValueError(f"Invalid build target: {build_target_cfg}")
    
    # Safety check: ensure we're not accidentally using base_game instead of mod_name
    if mod_name == base_game:
        raise ValueError(f"Mod name '{mod_name}' matches base_game '{base_game}'. This should not happen when constructing dictionary paths.")
    
    dict_path = warno_mods / mod_name / "GameData/Localisation" / mod_name / filename
    logger.debug(f"Constructed dictionary path: {dict_path} (mod_name: {mod_name})")
    
    return dict_path


def _initialize_dictionary_file(dict_path: Path) -> None:
    """Initialize dictionary file with header."""
    # Skip if already initialized this session
    if str(dict_path) in _initialized_files:
        return
        
    logger.info(f"Initializing dictionary file: {dict_path}")
    
    # Ensure directory exists
    target_dir = Path(dict_path).parent
    target_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if there's a conflicting base_game subdirectory in the Localisation folder
    # This can happen if the NDF mod system copies files from the base game mod
    config = ModConfig.get_instance().config_data
    base_game = config['directories']['base_game']
    is_dev = config['build_config']['write_dev']
    build_target_cfg = config['build_config']['target']
    
    # Determine mod folder name (same logic as get_dictionary_path)
    if is_dev and build_target_cfg == "gameplay":
        mod_name = config['directories']['gameplay_dev']
    elif is_dev and build_target_cfg == "ui_only":
        mod_name = config['directories']['ui_only_dev']
    elif not is_dev and build_target_cfg == "gameplay":
        mod_name = config['directories']['gameplay_release']
    elif not is_dev and build_target_cfg == "ui_only":
        mod_name = config['directories']['ui_only_release']
    else:
        mod_name = None
    
    localisation_dir = target_dir.parent
    # Ensure localisation directory exists
    localisation_dir.mkdir(parents=True, exist_ok=True)
    
    if mod_name:
        base_game_subdir = localisation_dir / base_game
        if base_game_subdir.exists() and base_game_subdir != target_dir:
            logger.warning(f"Found conflicting {base_game} subdirectory at {base_game_subdir}, but using correct path {target_dir}")
    
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


def _check_and_fix_localisation_dicos(localisation_dir: Path, base_game_subdir: Path, base_game: str, mod_name: str, config: Dict) -> None:
    """Check and fix LocalisationDicos.ndf location and FileName paths.
    
    Ensures the file is in the correct location and FileName paths use mod_name instead of base_game.
    If the file doesn't exist, copies it from the base_game mod.
    Also removes the incorrect base_game subdirectory after fixing.
    
    Args:
        localisation_dir: The Localisation directory path
        base_game_subdir: The base_game subdirectory path (if it exists)
        base_game: The base_game mod name
        mod_name: The target mod name
        config: Configuration dictionary
    """
    logger.info(f"Checking LocalisationDicos.ndf (mod_name: {mod_name}, base_game: {base_game})")
    
    wrong_ndf_path = base_game_subdir / "LocalisationDicos.ndf"
    # Correct path should be in the mod_name subdirectory, matching the CSV dictionary files
    correct_ndf_path = localisation_dir / mod_name / "LocalisationDicos.ndf"
    
    # Ensure correct directory exists
    correct_ndf_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Get base_game mod path to copy from if needed
    mod_src_path = get_mod_src_path(config)
    mod_dst_path = get_mod_dst_path(config)
    
    # Check for the file in base_game mod
    # The file is always at GameData/Localisation/{base_game}/LocalisationDicos.ndf
    base_game_localisation_dir = mod_src_path / "GameData" / "Localisation"
    base_game_ndf_path_subdir = base_game_localisation_dir / base_game / "LocalisationDicos.ndf"
    
    # Try to find the file in base_game mod
    source_ndf_path = None
    if base_game_ndf_path_subdir.exists():
        source_ndf_path = base_game_ndf_path_subdir
    else:
        # Fallback: search recursively for the file
        logger.debug(f"Searching recursively for LocalisationDicos.ndf in base_game mod")
        for found_file in mod_src_path.rglob("LocalisationDicos.ndf"):
            source_ndf_path = found_file
            logger.debug(f"  Found at: {source_ndf_path}")
            break
    
    logger.debug(f"  Correct path: {correct_ndf_path}")
    logger.debug(f"  Wrong path: {wrong_ndf_path}")
    logger.debug(f"  Base game path: {base_game_ndf_path_subdir}")
    logger.debug(f"  Source file found: {source_ndf_path}")
    
    # Handle file location: move from wrong location, or copy from base_game if it doesn't exist
    file_copied = False
    if not correct_ndf_path.exists():
        if wrong_ndf_path.exists():
            # Move file from wrong location to correct location
            try:
                logger.info(f"Moving LocalisationDicos.ndf from wrong location to correct location")
                logger.info(f"  From: {wrong_ndf_path}")
                logger.info(f"  To: {correct_ndf_path}")
                shutil.move(str(wrong_ndf_path), str(correct_ndf_path))
                logger.info(f"Successfully moved LocalisationDicos.ndf to correct location")
                file_copied = True
            except Exception as e:
                logger.error(f"Failed to move LocalisationDicos.ndf: {e}")
                return
        elif source_ndf_path and source_ndf_path.exists():
            # Copy file from base_game mod if it doesn't exist in target mod
            try:
                logger.info(f"Copying LocalisationDicos.ndf from base_game mod")
                logger.info(f"  From: {source_ndf_path}")
                logger.info(f"  To: {correct_ndf_path}")
                shutil.copy2(str(source_ndf_path), str(correct_ndf_path))
                logger.info(f"Successfully copied LocalisationDicos.ndf from base_game mod")
                file_copied = True
            except Exception as e:
                logger.error(f"Failed to copy LocalisationDicos.ndf from base_game mod: {e}")
                return
        else:
            # File doesn't exist anywhere - this should not happen if base_game mod is set up correctly
            logger.error(f"LocalisationDicos.ndf not found in base_game mod:")
            logger.error(f"  Expected at: {base_game_ndf_path_subdir}")
            logger.error(f"  Cannot copy file - base_game mod may be missing or incorrectly configured")
            return
    
    # Fix FileName paths in LocalisationDicos.ndf if it exists in the correct location
    # Always fix paths after copying/moving to ensure they use mod_name instead of base_game
    if correct_ndf_path.exists():
        try:
            logger.info(f"Fixing FileName paths in LocalisationDicos.ndf at {correct_ndf_path}")
            
            # Read the file content
            with open(correct_ndf_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace base_game with mod_name in FileName paths
            original_content = content
            updated_content = content.replace(f"Localisation/{base_game}/", f"Localisation/{mod_name}/")
            
            # Check if any changes were made
            if updated_content != original_content:
                # Write the updated content back
                with open(correct_ndf_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                # Count how many paths were updated
                updated_count = original_content.count(f"Localisation/{base_game}/")
                logger.info(f"Updated {updated_count} FileName paths in LocalisationDicos.ndf")
            else:
                # Check if paths already use mod_name
                if f"Localisation/{mod_name}/" in content:
                    logger.debug(f"FileName paths already use mod_name '{mod_name}'")
                else:
                    logger.warning(f"FileName paths in LocalisationDicos.ndf don't contain expected mod name")
                        
        except Exception as e:
            logger.error(f"Failed to fix LocalisationDicos.ndf: {e}")
            import traceback
            logger.debug(traceback.format_exc())
    
    # Remove the incorrect base_game subdirectory if it exists and is not the target directory
    if base_game_subdir.exists() and base_game_subdir != (localisation_dir / mod_name):
        try:
            # Only remove if it's empty or only contains files we've already moved
            if wrong_ndf_path.exists():
                logger.warning(f"Cannot remove {base_game} subdirectory: LocalisationDicos.ndf still exists there")
            else:
                logger.info(f"Removing incorrect {base_game} subdirectory: {base_game_subdir}")
                shutil.rmtree(base_game_subdir)
                logger.info(f"Successfully removed {base_game} subdirectory")
        except Exception as e:
            logger.error(f"Failed to remove {base_game} subdirectory at {base_game_subdir}: {e}")


def write_csv_entries(entries: List[Tuple[str, str]], dict_path: Path) -> None:
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
