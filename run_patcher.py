import sys
from datetime import datetime
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
    except Exception as e:
        logger.error(f"Patcher failed: {str(e)}")
        # Still show counts even if there was an exception
        counting_handler = get_counting_handler()
        if counting_handler:
            error_count, warning_count = counting_handler.get_counts()
            logger.info(f"Summary: {error_count} error(s), {warning_count} warning(s)")
        raise
