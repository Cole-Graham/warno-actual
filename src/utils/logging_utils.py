import logging
import time
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path


@contextmanager
def log_time(logger: logging.Logger, operation: str):
    """Log the time taken for an operation."""
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        logger.info(f"{operation} completed in {elapsed:.2f} seconds")

def cleanup_old_logs(log_dir: Path, keep_count: int = 5):
    """Delete old log files, keeping only the most recent ones.
    
    Args:
        log_dir: Directory containing log files
        keep_count: Number of most recent logs to keep for each type
    """
    # Group logs by their category (main, database, gameplay)
    log_groups = {}
    for log_file in log_dir.glob("*.log"):
        category = log_file.stem.split('_')[0]  # Get base category name
        if category not in log_groups:
            log_groups[category] = []
        log_groups[category].append(log_file)
    
    # For each group, sort by modification time and delete old ones
    for logs in log_groups.values():
        logs.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        for old_log in logs[keep_count:]:
            old_log.unlink()

def setup_logger(name: str) -> logging.Logger:
    """Set up and return a logger."""
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Clean up old logs before creating new one
    cleanup_old_logs(log_dir)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # More specific categorization
    category = name
    
    file_handler = logging.FileHandler(
        log_dir / f"{category}.log",
        encoding='utf-8',
        mode='w'  # Overwrite each run
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter('%(levelname)s - %(message)s')
    )
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger 