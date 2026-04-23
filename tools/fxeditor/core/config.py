"""Load calibration values from tools/fxeditor/fxeditor.yaml."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import re

_DEFAULT_YAML = Path(__file__).resolve().parent.parent / "fxeditor.yaml"


@dataclass
class CalibrationConfig:
    reference_gameplay_radius_m: float = 60.0
    anchor_max_ndf_radius: float = 4240.282686

    def ndf_to_gameplay(self, dx: float, dy: float) -> tuple[float, float]:
        if self.anchor_max_ndf_radius <= 0:
            return dx, dy
        s = self.reference_gameplay_radius_m / self.anchor_max_ndf_radius
        return dx * s, dy * s

    def gameplay_to_ndf(self, gx: float, gy: float) -> tuple[float, float]:
        if self.reference_gameplay_radius_m <= 0:
            return gx, gy
        inv = self.anchor_max_ndf_radius / self.reference_gameplay_radius_m
        return gx * inv, gy * inv


def _parse_simple_yaml(text: str) -> dict:
    """Minimal parser for flat key: value YAML (no nested structures)."""
    out: dict = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.+)$", line)
        if m:
            key = m.group(1)
            val = m.group(2).strip()
            try:
                out[key] = float(val)
            except ValueError:
                out[key] = val
    return out


def load_config(path: Optional[Path] = None) -> CalibrationConfig:
    p = path or _DEFAULT_YAML
    if not p.exists():
        return CalibrationConfig()
    text = p.read_text(encoding="utf-8")
    data = _parse_simple_yaml(text)
    return CalibrationConfig(
        reference_gameplay_radius_m=float(data.get("reference_gameplay_radius_m", 60.0)),
        anchor_max_ndf_radius=float(data.get("anchor_max_ndf_radius", 4240.282686)),
    )
