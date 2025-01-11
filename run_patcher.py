from src.utils.logging_utils import setup_logger

logger = setup_logger('patcher')

if __name__ == "__main__":
    try:
        logger.info("Starting WARNO mod patcher")
        from src.main import main
        main()
        logger.info("Patcher completed successfully")
    except Exception as e:
        logger.error(f"Patcher failed: {str(e)}")
        raise 