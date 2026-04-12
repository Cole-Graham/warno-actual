import logging
import re
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Optional

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


_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

_counting_handler: Optional[CountingHandler] = None
_logging_configured = False


def get_counting_handler() -> Optional[CountingHandler]:
    """Get the global counting handler instance."""
    return _counting_handler


def configure_logging() -> None:
    """Configure logging once at startup.

    Attaches handlers to the root logger so all module loggers propagate
    their records to a single consolidated log file, the console, and the
    warning/error counter.  Safe to call more than once (subsequent calls
    are no-ops).
    """
    global _counting_handler, _logging_configured
    if _logging_configured:
        return
    _logging_configured = True

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    log_dir = _PROJECT_ROOT / "logs"
    try:
        log_dir.mkdir(exist_ok=True)
        log_path = log_dir / "patcher.log"
        file_handler = logging.FileHandler(log_path, encoding="utf-8", mode="w")
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"),
        )
        root.addHandler(file_handler)
    except Exception as e:
        print(f"Warning: Could not set up log file: {e}")

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    root.addHandler(console_handler)

    _counting_handler = CountingHandler()
    _counting_handler.setLevel(logging.WARNING)
    root.addHandler(_counting_handler)


def setup_logger(name: str) -> logging.Logger:
    """Return a named logger.

    All handler configuration is done once by ``configure_logging()``.
    If ``configure_logging()`` has not been called yet (e.g. in tests or
    standalone scripts), a basic fallback is set up automatically.
    """
    if not _logging_configured:
        configure_logging()
    return logging.getLogger(name)
