"""JSON state persistence for all UI fields."""

from __future__ import annotations

import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from ..core.falloff import FALLOFF_SAMPLES, default_curve

_log = logging.getLogger(__name__)


def _state_dir() -> Path:
    base = os.environ.get("LOCALAPPDATA", "")
    if not base:
        base = str(Path.home() / ".local" / "share")
    return Path(base) / "warno_fxeditor"


def _state_path() -> Path:
    return _state_dir() / "state.json"


_DEFAULTS: Dict[str, Any] = {
    "source_files": [],
    "source_radius_m": 60.0,
    "rootname": "",
    "target_radii_text": "35, 75, 100, 125, 150, 175, 200, 225, 250",
    "output_dir": "",
    "naming_template": "{rootname}_{radiusinmeters}m_{n}.ndf",
    "window_x": 100,
    "window_y": 100,
    "window_w": 1400,
    "window_h": 900,
    "window_maximized": False,
    "preview_target_radius": None,
    "view_radius": 300.0,
    "vfx_visibility": {},
    "effect_group_collapse": {},
    "last_source_dir": "",
    "last_output_dir": "",
    "falloff_curve": default_curve(),
    "falloff_flat_value": 100.0,
    "falloff_ramp_end": 15.0,
    "falloff_bottom_out": 1.0,
    "named_falloff_presets": {},
    "taction_call_cap": 600,
    "calibration_ref_m": 60.0,
    "calibration_anchor_r": 4240.282686,
    "min_burst_count": 3,
    "min_size_ratio": 0.3,
    "min_count_value": 1,
    "size_param_names": None,
    "count_param_names": None,
    "splitter_sizes": None,
}


class AppState:
    """Thin wrapper around a dict with typed accessors and auto-save."""

    def __init__(self) -> None:
        self._data: Dict[str, Any] = dict(_DEFAULTS)
        self._path = _state_path()

    def load(self) -> None:
        if not self._path.exists():
            _log.info("No state file at %s; using defaults", self._path)
            return
        try:
            raw = self._path.read_text(encoding="utf-8")
            loaded = json.loads(raw)
            if isinstance(loaded, dict):
                for k, v in loaded.items():
                    if k in _DEFAULTS:
                        self._data[k] = v
            _log.info("Loaded state from %s", self._path)
        except Exception:
            _log.warning("Could not read state file %s; using defaults", self._path, exc_info=True)

    def save(self) -> None:
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            self._path.write_text(
                json.dumps(self._data, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
        except Exception:
            _log.warning("Could not write state file %s", self._path, exc_info=True)

    def reset(self) -> None:
        self._data = dict(_DEFAULTS)

    # ── typed accessors ───────────────────────────────────────────

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default if default is not None else _DEFAULTS.get(key))

    def set(self, key: str, value: Any) -> None:
        self._data[key] = value

    @property
    def source_files(self) -> List[str]:
        return list(self._data.get("source_files", []))

    @source_files.setter
    def source_files(self, v: List[str]) -> None:
        self._data["source_files"] = list(v)

    @property
    def source_radius_m(self) -> float:
        return float(self._data.get("source_radius_m", 60.0))

    @source_radius_m.setter
    def source_radius_m(self, v: float) -> None:
        self._data["source_radius_m"] = float(v)

    @property
    def rootname(self) -> str:
        return str(self._data.get("rootname", ""))

    @rootname.setter
    def rootname(self, v: str) -> None:
        self._data["rootname"] = str(v)

    @property
    def target_radii_text(self) -> str:
        return str(self._data.get("target_radii_text", _DEFAULTS["target_radii_text"]))

    @target_radii_text.setter
    def target_radii_text(self, v: str) -> None:
        self._data["target_radii_text"] = str(v)

    @property
    def output_dir(self) -> str:
        return str(self._data.get("output_dir", ""))

    @output_dir.setter
    def output_dir(self, v: str) -> None:
        self._data["output_dir"] = str(v)

    @property
    def naming_template(self) -> str:
        return str(self._data.get("naming_template", _DEFAULTS["naming_template"]))

    @naming_template.setter
    def naming_template(self, v: str) -> None:
        self._data["naming_template"] = str(v)

    @property
    def falloff_curve(self) -> List[float]:
        c = self._data.get("falloff_curve", None)
        if not c or not isinstance(c, list):
            return default_curve()
        return [float(x) for x in c[:FALLOFF_SAMPLES]]

    @falloff_curve.setter
    def falloff_curve(self, v: List[float]) -> None:
        self._data["falloff_curve"] = [float(x) for x in v[:FALLOFF_SAMPLES]]

    @property
    def taction_call_cap(self) -> int:
        return int(self._data.get("taction_call_cap", 600))

    @taction_call_cap.setter
    def taction_call_cap(self, v: int) -> None:
        self._data["taction_call_cap"] = int(v)

    @property
    def vfx_visibility(self) -> Dict[str, bool]:
        return dict(self._data.get("vfx_visibility", {}))

    @vfx_visibility.setter
    def vfx_visibility(self, v: Dict[str, bool]) -> None:
        self._data["vfx_visibility"] = dict(v)
