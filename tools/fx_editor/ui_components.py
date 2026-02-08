"""Shared UI helpers for FX editor."""

import sys
from pathlib import Path
from typing import Any

# Add project root to path for imports (same as dpm_visualizer)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src import ndf


def format_value(value: Any) -> str:
    """Format an NDF value for display."""
    if isinstance(value, (ndf.model.List, ndf.model.Map, ndf.model.Object)):
        return ndf.printer.string(value).strip()
    return str(value)


def parse_value_input(value_text: str) -> Any:
    """Parse a user-provided value string into an NDF value if possible."""
    try:
        parsed = ndf.expression(value_text)
        if isinstance(parsed, dict) and 'value' in parsed:
            return parsed['value']
    except Exception:
        pass
    return value_text
