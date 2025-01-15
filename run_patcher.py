from config.config_loader import ConfigLoader
from src.data import build_database
from src.utils.logging_utils import setup_logger

logger = setup_logger('patcher')

if __name__ == "__main__":
    try:
        logger.info("Starting WARNO mod patcher")
        
        # Load configuration first
        config = ConfigLoader("config/config.YAML").load()
        
        # Build the database if configured to do so
        build_database(config)
        
        # Import and run main after database build
        from src.main import main
        main()
        
        logger.info("Patcher completed successfully")
    except Exception as e:
        logger.error(f"Patcher failed: {str(e)}")
        raise 