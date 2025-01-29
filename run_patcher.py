import sys

from config.config_loader import ConfigLoader
from src import ModConfig
from src.data import build_database
from src.utils.database_utils import verify_database
from src.utils.dictionary_utils import initialize_dictionary_files
from src.utils.logging_utils import setup_logger

logger = setup_logger('patcher')

def confirm_release_build() -> bool:
    """Prompt user to confirm release build."""
    while True:
        response = input("Are you sure you want to write the release build? (y/n): ").lower()
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
        
        # Build the database if needed
        if config.config_data['data_config']['build_database']:
            config.config_data['game_db'] = build_database(config.config_data)
        
        # Import and run main after database build
        from src.main import main
        main()
        
        logger.info("Patcher completed successfully")
    except Exception as e:
        logger.error(f"Patcher failed: {str(e)}")
        raise 