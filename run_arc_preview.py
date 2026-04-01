"""Launcher for Artillery Arc Preview (dev + PyInstaller entry point).

Run from repo root: python run_arc_preview.py
Or: python -m tools.artillery_arc_preview
"""

from __future__ import annotations

import sys
from pathlib import Path

if not getattr(sys, "frozen", False):
    _ROOT = Path(__file__).resolve().parent
    if str(_ROOT) not in sys.path:
        sys.path.insert(0, str(_ROOT))

from tools.artillery_arc_preview.main import main

if __name__ == "__main__":
    main()
