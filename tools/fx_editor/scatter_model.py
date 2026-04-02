"""Serializable scatter project (gameplay-space layout) for FX codegen."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class ScatterBurst:
    x_gameplay_m: float
    y_gameplay_m: float
    delay_s: Optional[float] = None
    primary_vfx: Optional[str] = None
    #: Index into placeable ``TSimultaneousAction`` templates; ``None`` = legacy ``burst_i % n``.
    template_index: Optional[int] = None


@dataclass
class ScatterProject:
    """Layout in gameplay meters; conversion to NDF uses calibration."""

    version: int = 1
    reference_gameplay_radius_m: float = 120.0
    anchor_max_ndf_radius: float = 4272.522908071997
    emit_mode: str = 'mobile_position'
    template_list_row_index: int = 0
    bursts: List[ScatterBurst] = field(default_factory=list)
    source_ndf_path: Optional[str] = None
    wait_envelope_max_s: Optional[float] = None
    inferred_anchor_min_s: Optional[float] = None
    #: Gameplay disk radius (m) for hex / reference circle; cluster uses target radius.
    layout_disk_radius_m: Optional[float] = None

    def to_json_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d['bursts'] = [asdict(b) for b in self.bursts]
        return d

    @classmethod
    def from_json_dict(cls, d: Dict[str, Any]) -> 'ScatterProject':
        bursts_raw = d.get('bursts') or []
        bursts = [
            ScatterBurst(
                x_gameplay_m=float(b['x_gameplay_m']),
                y_gameplay_m=float(b['y_gameplay_m']),
                delay_s=None if b.get('delay_s') is None else float(b['delay_s']),
                primary_vfx=b.get('primary_vfx'),
                template_index=(
                    None if b.get('template_index') is None else int(b['template_index'])
                ),
            )
            for b in bursts_raw
        ]
        return cls(
            version=int(d.get('version', 1)),
            reference_gameplay_radius_m=float(d.get('reference_gameplay_radius_m', 120.0)),
            anchor_max_ndf_radius=float(d.get('anchor_max_ndf_radius', 4272.522908071997)),
            emit_mode=str(d.get('emit_mode', 'mobile_position')),
            template_list_row_index=int(d.get('template_list_row_index', 0)),
            bursts=bursts,
            source_ndf_path=d.get('source_ndf_path'),
            wait_envelope_max_s=(
                None if d.get('wait_envelope_max_s') is None else float(d['wait_envelope_max_s'])
            ),
            inferred_anchor_min_s=(
                None if d.get('inferred_anchor_min_s') is None else float(d['inferred_anchor_min_s'])
            ),
            layout_disk_radius_m=(
                None if d.get('layout_disk_radius_m') is None else float(d['layout_disk_radius_m'])
            ),
        )

    def save_json(self, path: Path) -> None:
        path.write_text(json.dumps(self.to_json_dict(), indent=2), encoding='utf-8')

    @classmethod
    def load_json(cls, path: Path) -> 'ScatterProject':
        data = json.loads(path.read_text(encoding='utf-8'))
        return cls.from_json_dict(data)


def load_scatter_calibration_yaml(path: Optional[Path] = None) -> Tuple[float, float]:
    """Return (reference_gameplay_radius_m, anchor_max_ndf_radius)."""
    if path is None:
        path = Path(__file__).resolve().parent / 'scatter_calibration.yaml'
    try:
        import ruamel.yaml  # type: ignore

        y = ruamel.yaml.YAML(typ='safe')
        with open(path, 'r', encoding='utf-8') as handle:
            d = y.load(handle)
    except Exception:
        return 120.0, 4272.522908071997
    if not isinstance(d, dict):
        return 120.0, 4272.522908071997
    return float(d.get('reference_gameplay_radius_m', 120.0)), float(
        d.get('anchor_max_ndf_radius', 4272.522908071997),
    )
