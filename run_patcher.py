import sys
from datetime import datetime
from pathlib import Path
# from config.config_loader import ConfigLoader
from src import ModConfig
from src.data import build_database, load_database_from_disk
from src.utils.database_utils import verify_database
from src.utils.dictionary_utils import initialize_dictionary_files
from src.utils.logging_utils import setup_logger, get_counting_handler

logger = setup_logger('patcher')


def confirm_release_build() -> bool:
    """Prompt user to confirm release build."""
    while True:
        version = ""
        build_target = ""
        try:
            build_target = ModConfig.get_instance().config_data["build_config"]["target"]
            if build_target == "gameplay":
                version = ModConfig.get_instance().config_data["build_config"].get("gameplay_version", "")
            elif build_target == "ui_only":
                version = ModConfig.get_instance().config_data["build_config"].get("ui_version", "")
        except Exception:
            pass
        version_str = f" (version: {version})" if version else ""
        response = input(f"Are you sure you want to write the release build {version_str}? (y/n): ").lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        print("Please enter 'y' or 'n'")


def confirm_database_rebuild() -> bool:
    """Prompt user to confirm database rebuild."""
    while True:
        response = input("Database is out of date. Rebuild database? (y/n): ").lower()
        if response == 'y':
            return True
        elif response == 'n':
            return False
        print("Please enter 'y' or 'n'")


def get_config_ini_path(config_data: dict) -> Path:
    """Get the path to the mod's Config.ini file.
    
    Args:
        config_data: The configuration data dictionary
        
    Returns:
        Path to the Config.ini file
    """
    build_config = config_data['build_config']
    dirs = config_data['directories']
    
    # Determine mod name based on build target and write_dev setting
    if build_config['target'] == 'gameplay':
        mod_name = dirs['gameplay_release'] if not build_config['write_dev'] else dirs['gameplay_dev']
    else:  # ui_only
        mod_name = dirs['ui_only_release'] if not build_config['write_dev'] else dirs['ui_only_dev']
    
    # Check if user has provided a custom base path override
    config_ini_base_path = dirs.get('config_ini_base_path', 'default')
    if config_ini_base_path and config_ini_base_path.strip() and config_ini_base_path.lower() != 'default':
        # User provided override, use it
        config_ini_path = Path(config_ini_base_path) / mod_name / "Config.ini"
    else:
        # Default path: {home}/Saved Games/EugenSystems/WARNO/mod/{mod_name}/Config.ini
        config_ini_path = Path.home() / "Saved Games" / "EugenSystems" / "WARNO" / "mod" / mod_name / "Config.ini"
    
    return config_ini_path


def parse_config_ini_version(config_ini_path: Path) -> str:
    """Parse the Version value from Config.ini file.
    
    Args:
        config_ini_path: Path to the Config.ini file
        
    Returns:
        Version string, or empty string if not found or file doesn't exist
    """
    if not config_ini_path.exists():
        return ""
    
    try:
        with open(config_ini_path, 'r', encoding='utf-8') as f:
            in_properties_section = False
            for line in f:
                line = line.strip()
                # Check for [Properties] section
                if line == '[Properties]':
                    in_properties_section = True
                    continue
                # Check if we've moved to another section
                if line.startswith('[') and line.endswith(']'):
                    in_properties_section = False
                    continue
                # Look for Version = value in Properties section
                if in_properties_section and line.startswith('Version'):
                    # Extract value after '='
                    parts = line.split('=', 1)
                    if len(parts) == 2:
                        version = parts[1].strip()
                        # Remove any trailing comments
                        if ';' in version:
                            version = version.split(';')[0].strip()
                        return version
    except Exception as e:
        logger.warning(f"Failed to parse Config.ini at {config_ini_path}: {e}")
        return ""
    
    return ""


if __name__ == "__main__":
    try:
        logger.info("Starting WARNO mod patcher")
        
        # Load configuration first
        config = ModConfig.get_instance()
        
        # Check if this is a release build
        if not config.config_data['build_config']['write_dev']:
            if not confirm_release_build():
                logger.info("Release build cancelled by user")
                sys.exit(0)
            logger.info("Release build confirmed by user")
        
        # Initialize dictionary files
        initialize_dictionary_files()
        
        # Verify database status
        if not verify_database(config.config_data):
            if config.config_data['data_config']['build_database']:
                logger.info("Rebuilding outdated database...")
            elif confirm_database_rebuild():
                config.config_data['data_config']['build_database'] = True
                logger.info("User confirmed database rebuild...")
            else:
                logger.warning("Continuing with outdated database...")
        
        # Always load or build the database
        if config.config_data['data_config']['build_database']:
            config.config_data['game_db'] = build_database(config.config_data)
        else:
            config.config_data['game_db'] = load_database_from_disk(config.config_data)
        
        # Always build constants precomputation data (regenerates on every run)
        from src.data.constants_precomputation import build_constants_precomputation_data
        constants_data = build_constants_precomputation_data(config.config_data, game_db=config.config_data['game_db'])
        config.config_data['game_db']['deck_pack_mappings'] = constants_data
        
        # Merge salvo_weapons (from base game database) with constants renames (from constants precomputation)
        # and add to ammo_db so handlers can access them the same way
        ammo_db = config.config_data['game_db'].get('ammunition', {})
        salvo_weapons = ammo_db.get('salvo_weapons', {})
        constants_renames = constants_data.get('ammunition_renames', {})
        constants_renames_old_new = constants_renames.get('renames_old_new', {})
        
        # Combine salvo weapons and constants renames
        renames_old_new = {**salvo_weapons, **constants_renames_old_new}
        
        # Create reversed mapping
        renames_new_old = {v: k for k, v in renames_old_new.items()}
        
        # Add merged renames to ammo_db
        ammo_db['renames_old_new'] = renames_old_new
        ammo_db['renames_new_old'] = renames_new_old
        
        # Import and run main after database is loaded
        from src.main import main
        main()
        
        # Get error and warning counts
        counting_handler = get_counting_handler()
        if counting_handler:
            error_count, warning_count = counting_handler.get_counts()
            logger.info(f"Patcher completed successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            logger.info(f"Summary: {error_count} error(s), {warning_count} warning(s)")
        else:
            logger.info(f"Patcher completed successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Log version information for release builds
        if not config.config_data['build_config']['write_dev']:
            build_config = config.config_data['build_config']
            # Get version from config.YAML
            if build_config['target'] == 'gameplay':
                config_version = build_config.get('gameplay_version', '')
            else:  # ui_only
                config_version = build_config.get('ui_version', '')
            
            logger.info(f"Version from config.YAML: {config_version}")
            
            # Get version from Config.ini
            config_ini_path = get_config_ini_path(config.config_data)
            config_ini_version = parse_config_ini_version(config_ini_path)
            if config_ini_version:
                logger.info(f"Version from Config.ini: {config_ini_version}")
            else:
                logger.warning(f"Could not read version from Config.ini at {config_ini_path}")
    except Exception as e:
        logger.error(f"Patcher failed: {str(e)}")
        # Still show counts even if there was an exception
        counting_handler = get_counting_handler()
        if counting_handler:
            error_count, warning_count = counting_handler.get_counts()
            logger.info(f"Summary: {error_count} error(s), {warning_count} warning(s)")
        
        # Log version information for release builds even on failure
        try:
            config = ModConfig.get_instance()
            if not config.config_data['build_config']['write_dev']:
                build_config = config.config_data['build_config']
                # Get version from config.YAML
                if build_config['target'] == 'gameplay':
                    config_version = build_config.get('gameplay_version', '')
                else:  # ui_only
                    config_version = build_config.get('ui_version', '')
                
                logger.info(f"Version from config.YAML: {config_version}")
                
                # Get version from Config.ini
                config_ini_path = get_config_ini_path(config.config_data)
                config_ini_version = parse_config_ini_version(config_ini_path)
                if config_ini_version:
                    logger.info(f"Version from Config.ini: {config_ini_version}")
                else:
                    logger.warning(f"Could not read version from Config.ini at {config_ini_path}")
        except Exception:
            pass  # Don't fail on version logging errors
        
        raise
