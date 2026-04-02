"""Central logging for FX Editor: terminal (stderr), ring buffer for UI viewer."""

from __future__ import annotations

import logging
import os
import sys
from collections import deque
from typing import Deque, Optional

LOGGER_NAME = "fx_editor"
_MAX_BUFFER_LINES = 8000

_buffer: Deque[str] = deque(maxlen=_MAX_BUFFER_LINES)


class _RingBufferHandler(logging.Handler):
    """Append formatted log lines to an in-memory deque for the debug log window."""

    def emit(self, record: logging.LogRecord) -> None:
        try:
            msg = self.format(record)
            _buffer.append(msg)
        except Exception:
            self.handleError(record)


def setup_fx_logging(stream_level: Optional[int] = None) -> logging.Logger:
    """Configure the ``fx_editor`` logger: stderr + ring buffer. Call once from ``main()``.

    Set ``FX_EDITOR_LOG_LEVEL`` to ``DEBUG``, ``INFO``, or ``WARNING`` to control stderr verbosity
    (default ``INFO``). The ring buffer always records ``DEBUG`` and above for the log viewer.
    """
    if stream_level is None:
        env = os.environ.get('FX_EDITOR_LOG_LEVEL', '').strip().upper()
        if env == 'DEBUG':
            stream_level = logging.DEBUG
        elif env == 'INFO':
            stream_level = logging.INFO
        elif env in ('WARNING', 'WARN'):
            stream_level = logging.WARNING
        else:
            stream_level = logging.INFO
    log = logging.getLogger(LOGGER_NAME)
    log.handlers.clear()
    log.setLevel(logging.DEBUG)
    log.propagate = False

    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    sh = logging.StreamHandler(sys.stderr)
    sh.setLevel(stream_level)
    sh.setFormatter(fmt)
    log.addHandler(sh)

    bh = _RingBufferHandler()
    bh.setLevel(logging.DEBUG)
    bh.setFormatter(fmt)
    log.addHandler(bh)

    return log


def get_fx_logger(name_suffix: str = "") -> logging.Logger:
    """Child logger under ``fx_editor`` (e.g. ``fx_editor.scatter_preview``)."""
    if not name_suffix:
        return logging.getLogger(LOGGER_NAME)
    return logging.getLogger(f"{LOGGER_NAME}.{name_suffix}")


def get_debug_log_buffer_text() -> str:
    """Return all buffered lines for the detailed log viewer."""
    return "\n".join(_buffer)


def clear_debug_log_buffer() -> None:
    """Clear the in-memory log buffer (optional UI action)."""
    _buffer.clear()
