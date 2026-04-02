"""Persist FX Editor UI state between sessions (JSON under user config dir).

v2: variation param/call qty + radius-falloff curves, per-group Size/Count toggles,
    dialog window geometry (qty curve, radius falloff, mult-edit).
v3: batch listbox selected_indices + explicit empty selection restore.
v4: dialog_substate (mult-edit pattern checks, qty/radius preset spin values).
v5: named preset libraries for qty and radius-falloff curve dialogs.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict

STATE_VERSION = 5


def state_file_path() -> Path:
    """Cross-platform config path: Local App Data / Application Support / .config."""
    if sys.platform == 'win32':
        base = Path(os.environ.get('LOCALAPPDATA', str(Path.home() / 'AppData' / 'Local')))
    elif sys.platform == 'darwin':
        base = Path.home() / 'Library' / 'Application Support'
    else:
        base = Path(os.environ.get('XDG_CONFIG_HOME', str(Path.home() / '.config')))
    d = base / 'warno_fx_editor'
    d.mkdir(parents=True, exist_ok=True)
    return d / 'state.json'


def load_state() -> Dict[str, Any]:
    path = state_file_path()
    if not path.exists():
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as handle:
            data = json.load(handle)
        return data if isinstance(data, dict) else {}
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return {}


def save_state(data: Dict[str, Any]) -> None:
    path = state_file_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = dict(data)
    payload['version'] = STATE_VERSION
    tmp = path.with_suffix('.json.tmp')
    with open(tmp, 'w', encoding='utf-8') as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False)
        handle.write('\n')
    tmp.replace(path)
