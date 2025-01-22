import logging
import os
import stat
import time
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path
from typing import Optional


@contextmanager
def log_time(logger: logging.Logger, operation: str):
    """Log the time taken for an operation."""
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        logger.info(f"{operation} completed in {elapsed:.2f} seconds")

def ensure_file_permissions(file_path: Path) -> None:
    """Ensure the file has the correct permissions for writing.
    
    Args:
        file_path: Path to the log file
    """
    try:
        # Make file writable by user if it exists
        if file_path.exists():
            current = stat.S_IMODE(os.lstat(file_path).st_mode)
            os.chmod(file_path, current | stat.S_IWRITE)
    except (OSError, PermissionError) as e:
        print(f"Warning: Could not set permissions for {file_path}: {e}")

def get_writable_path(base_path: Path, name: str, max_attempts: int = 3) -> Optional[Path]:
    """Get a writable log file path, with fallback options.
    
    Args:
        base_path: Base directory for logs
        name: Base name for the log file
        max_attempts: Maximum number of alternate paths to try
        
    Returns:
        Path object if a writable path is found, None otherwise
    """
    paths_to_try = [
        base_path / f"{name}.log",  # First try standard path
        base_path / f"{name}_{int(time.time())}.log",  # Try with timestamp
        Path.home() / f"warno_mod_{name}.log",  # Try home directory
    ]

    for path in paths_to_try[:max_attempts]:
        try:
            # Test if we can write to this path
            if not path.parent.exists():
                path.parent.mkdir(parents=True, exist_ok=True)
            if path.exists():
                ensure_file_permissions(path)
            with open(path, 'a'): pass
            return path
        except (OSError, PermissionError):
            continue
            
    return None

def cleanup_old_logs(log_dir: Path, keep_count: int = 5):
    """Delete old log files, keeping only the most recent ones.
    
    Args:
        log_dir: Directory containing log files
        keep_count: Number of most recent logs to keep for each type
    """
    try:
        # Group logs by their category (main, database, gameplay)
        log_groups = {}
        for log_file in log_dir.glob("*.log"):
            try:
                category = log_file.stem.split('_')[0]  # Get base category name
                if category not in log_groups:
                    log_groups[category] = []
                log_groups[category].append(log_file)
            except Exception:
                continue
        
        # For each group, sort by modification time and delete old ones
        for logs in log_groups.values():
            logs.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            for old_log in logs[keep_count:]:
                try:
                    ensure_file_permissions(old_log)
                    old_log.unlink()
                except (OSError, PermissionError):
                    continue
    except Exception as e:
        print(f"Warning: Error during log cleanup: {e}")

def setup_logger(name: str) -> logging.Logger:
    """Set up and return a logger with fallback options for file handling.
    
    Args:
        name: Name for the logger
        
    Returns:
        Configured logger object
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Try to set up file handler
    log_dir = Path("logs")
    try:
        log_dir.mkdir(exist_ok=True)
        cleanup_old_logs(log_dir)
        
        # Get writable log path
        log_path = get_writable_path(log_dir, name)
        if log_path:
            try:
                file_handler = logging.FileHandler(
                    log_path,
                    encoding='utf-8',
                    mode='w'  # Overwrite each run
                )
                file_handler.setLevel(logging.DEBUG)
                file_handler.setFormatter(
                    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                )
                logger.addHandler(file_handler)
            except Exception as e:
                print(f"Warning: Could not create file handler: {e}")
    except Exception as e:
        print(f"Warning: Could not set up log directory: {e}")

    # Always add console handler as fallback
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(
        logging.Formatter('%(levelname)s - %(message)s')
    )
    logger.addHandler(console_handler)
    
    return logger 