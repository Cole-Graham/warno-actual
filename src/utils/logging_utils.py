import glob
import logging
import os
from datetime import datetime
from pathlib import Path


def cleanup_old_logs(log_dir: Path, keep_count: int = 5):
    """Delete old log files, keeping only the most recent ones.
    
    Args:
        log_dir: Directory containing log files
        keep_count: Number of most recent logs to keep for each type
    """
    # Group logs by their prefix (e.g., 'main', 'unit_edits', etc)
    log_groups = {}
    for log_file in log_dir.glob("*.log"):
        prefix = log_file.name.split('_')[0]
        if prefix not in log_groups:
            log_groups[prefix] = []
        log_groups[prefix].append(log_file)
    
    # For each group, sort by modification time and delete old ones
    for logs in log_groups.values():
        logs.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        for old_log in logs[keep_count:]:
            old_log.unlink()

def setup_logger(name: str) -> logging.Logger:
    """Set up and return a logger with file and console handlers.
    
    Args:
        name: Name of the logger/module
        
    Returns:
        Configured logger instance
    """
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
    
    # Create formatters
    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console_formatter = logging.Formatter(
        '%(levelname)s - %(message)s'
    )
    
    # File handler - include timestamp in filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_handler = logging.FileHandler(
        log_dir / f"{name}_{timestamp}.log",
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(console_formatter)
    
    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger 