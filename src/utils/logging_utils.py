import logging
import os
import re
import stat
import time
from contextlib import contextmanager
# from datetime import datetime
from pathlib import Path
from typing import Callable, Optional

# Rules to normalize messages so similar warnings (e.g. same unit in different divisions) count as one.
# Each tuple: (compiled regex, replacement callable that receives the match and returns normalized string)
_MESSAGE_NORMALIZATION_RULES: list[tuple[re.Pattern, Callable[[re.Match], str]]] = [
    (
        re.compile(
            r"^Invalid unit name '([^']+)' in .+ category .+: unit not found in unit_data or NEW_UNITS$",
        ),
        lambda m: f"Invalid unit name '{m.group(1)}': unit not found in unit_data or NEW_UNITS",
    ),
]


def _normalize_message_for_uniqueness(message: str) -> str:
    """Normalize message so similar warnings count as one for unique-message tracking."""
    for pattern, replacement in _MESSAGE_NORMALIZATION_RULES:
        match = pattern.match(message)
        if match:
            return replacement(match)
    return message


class CountingHandler(logging.Handler):
    """A logging handler that counts errors and warnings, including unique message counts."""

    def __init__(self):
        super().__init__()
        self.error_count = 0
        self.warning_count = 0
        self._unique_error_messages: set[str] = set()
        self._unique_warning_messages: set[str] = set()

    def emit(self, record):
        """Count errors and warnings, tracking unique messages."""
        message = record.getMessage()
        unique_key = _normalize_message_for_uniqueness(message)
        if record.levelno >= logging.ERROR:
            self.error_count += 1
            self._unique_error_messages.add(unique_key)
        elif record.levelno >= logging.WARNING:
            self.warning_count += 1
            self._unique_warning_messages.add(unique_key)

    def get_counts(self):
        """Get total and unique error/warning counts.

        Returns:
            Tuple of (error_count, warning_count, unique_error_count, unique_warning_count)
        """
        return (
            self.error_count,
            self.warning_count,
            len(self._unique_error_messages),
            len(self._unique_warning_messages),
        )

    def reset(self):
        """Reset the counts."""
        self.error_count = 0
        self.warning_count = 0
        self._unique_error_messages.clear()
        self._unique_warning_messages.clear()


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
            with open(path, 'a'):
                pass
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
            except Exception:  # noqa
                continue
        
        # For each group, sort by modification time and delete old ones
        for logs in log_groups.values():
            logs.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            for old_log in logs[keep_count:]:
                try:
                    ensure_file_permissions(old_log)
                    # old_log.unlink()
                except (OSError, PermissionError):
                    continue
    except Exception as e:
        print(f"Warning: Error during log cleanup: {e}")


# Global counting handler instance for tracking errors/warnings across all loggers
_counting_handler: Optional[CountingHandler] = None


def get_counting_handler() -> Optional[CountingHandler]:
    """Get the global counting handler instance."""
    return _counting_handler


def setup_logger(name: str) -> logging.Logger:
    """Set up and return a logger with fallback options for file handling.
    
    Args:
        name: Name for the logger
        
    Returns:
        Configured logger object
    """
    global _counting_handler
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Add counting handler if it doesn't exist (shared across all loggers)
    if _counting_handler is None:
        _counting_handler = CountingHandler()
        _counting_handler.setLevel(logging.WARNING)  # Only count warnings and above
    logger.addHandler(_counting_handler)
    
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
