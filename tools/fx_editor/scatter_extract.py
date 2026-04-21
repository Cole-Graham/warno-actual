"""Extract scatter XY from FX NDF (Mobile Position and parPositionRelative) and compute bounds."""

from __future__ import annotations

import math
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src import ndf
from src.utils.ndf_utils import strip_quotes

FLOAT3_PLUS_PAR = re.compile(
    r'float3\s*\[\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^\]]+)\s*\]\s*\+\s*parPosition',
    re.IGNORECASE,
)
# Mobile ``Position = float3[x,y,z]`` without ``+ parPosition`` (absolute anchor in file space).
FLOAT3_LITERAL_XY = re.compile(
    r'^float3\s*\[\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^\]]+)\s*\]\s*$',
    re.IGNORECASE,
)


@dataclass
class ScatterExtractionResult:
    """Points in raw NDF XY units (engine space, not 1:1 gameplay meters)."""

    points_ndf: List[Tuple[float, float]] = field(default_factory=list)
    sources: List[str] = field(default_factory=list)  # 'mobile_position' | 'par_position_relative'

    @property
    def count(self) -> int:
        return len(self.points_ndf)

    def max_radius_from_origin(self) -> float:
        if not self.points_ndf:
            return 0.0
        return max(math.hypot(dx, dy) for dx, dy in self.points_ndf)

    def axis_bounds(self) -> Tuple[float, float, float, float]:
        """min_x, max_x, min_y, max_y."""
        if not self.points_ndf:
            return 0.0, 0.0, 0.0, 0.0
        xs = [p[0] for p in self.points_ndf]
        ys = [p[1] for p in self.points_ndf]
        return min(xs), max(xs), min(ys), max(ys)


def _parse_float3_plus_par(text: str) -> Optional[Tuple[float, float]]:
    text = text.strip()
    m = FLOAT3_PLUS_PAR.search(text)
    if not m:
        return None
    try:
        return float(m.group(1)), float(m.group(2))
    except ValueError:
        return None


def _parse_mobile_position_xy(text: str) -> Optional[Tuple[float, float]]:
    """``float3[…]+parPosition``, bare ``float3[…]``, or ``parPosition`` for Mobile.Position."""
    text = text.strip()
    p = _parse_float3_plus_par(text)
    if p is not None:
        return p
    m = FLOAT3_LITERAL_XY.match(text)
    if m:
        try:
            return float(m.group(1)), float(m.group(2))
        except ValueError:
            return None
    if text.replace(' ', '').lower() == 'parposition':
        return (0.0, 0.0)
    return None


def _stringify_position_expr(dx: float, dy: float) -> str:
    """Vanilla-style integer components in float3 (e.g. float3[-2247,833,0])."""
    ix = int(round(dx))
    iy = int(round(dy))
    return f'float3[{ix},{iy},0] + parPosition'


@dataclass
class ScatterPointVfx:
    """One scatter sample with primary VFX label (first TActionCall in a simultaneous group)."""

    dx_ndf: float
    dy_ndf: float
    primary_vfx: str
    source: str  # 'mobile_position' | 'par_position_relative'


def _action_short_from_taction(obj: ndf.model.Object) -> str:
    if obj.type != 'TActionCall':
        return ''
    for member in obj:
        if member.member == 'Action':
            av = strip_quotes(str(member.v))
            return av.split('/')[-1] if av else ''
    return ''


def _first_taction_short_in_simultaneous(sim: ndf.model.Object) -> str:
    """First TActionCall Action short name in preorder (main VFX for a global Mobile position)."""

    def walk(node: Any) -> str:
        if isinstance(node, ndf.model.Object):
            if node.type == 'TActionCall':
                s = _action_short_from_taction(node)
                if s:
                    return s
            for m in node:
                got = walk(m.v)
                if got:
                    return got
        elif isinstance(node, ndf.model.List):
            for row in node:
                got = walk(row.v)
                if got:
                    return got
        elif isinstance(node, ndf.model.MemberRow):
            return walk(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                got = walk(mr.v)
                if got:
                    return got
        elif isinstance(node, ndf.model.ListRow):
            return walk(node.v)
        return ''

    if sim.type != 'TSimultaneousAction':
        return ''
    for m in sim:
        if m.member == 'Actions' and isinstance(m.v, ndf.model.List):
            for row in m.v:
                got = walk(row.v)
                if got:
                    return got
    return ''


def _mobile_position_from_simultaneous(sim: ndf.model.Object) -> Optional[Tuple[float, float]]:
    if sim.type != 'TSimultaneousAction':
        return None
    for m in sim:
        if m.member != 'Mobile' or not isinstance(m.v, ndf.model.Object):
            continue
        mob = m.v
        if mob.type != 'TMobileWithLocalRepereMatrixFactory':
            continue
        for mm in mob:
            if mm.member == 'Position':
                s = ndf.printer.string(mm.v).strip()
                p = _parse_mobile_position_xy(s)
                if p is not None:
                    return p
    return None


def extract_scatter_points_with_vfx(parsed_root: ndf.model.List) -> List[ScatterPointVfx]:
    """One point per global burst (Mobile) or per parPositionRelative; primary VFX labels the group."""
    out: List[ScatterPointVfx] = []

    def collect_relative_from_taction(tac: ndf.model.Object) -> None:
        if tac.type != 'TActionCall':
            return
        short = _action_short_from_taction(tac)
        for member in tac:
            if member.member != 'NamedParams' or not isinstance(member.v, ndf.model.Map):
                continue
            for map_row in member.v:
                key = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
                if key != 'parPositionRelative':
                    continue
                s = ndf.printer.string(map_row.v).strip()
                p = _parse_float3_plus_par(s)
                if p:
                    label = short or 'Unknown'
                    out.append(ScatterPointVfx(p[0], p[1], label, 'par_position_relative'))

    def walk_taction_calls(node: Any) -> None:
        if isinstance(node, ndf.model.Object):
            if node.type == 'TActionCall':
                collect_relative_from_taction(node)
            for m in node:
                walk_taction_calls(m.v)
        elif isinstance(node, ndf.model.List):
            for row in node:
                walk_taction_calls(row.v)
        elif isinstance(node, ndf.model.MemberRow):
            walk_taction_calls(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                walk_taction_calls(mr.v)
        elif isinstance(node, ndf.model.ListRow):
            walk_taction_calls(node.v)

    def walk_simultaneous(sim: ndf.model.Object) -> None:
        if sim.type != 'TSimultaneousAction':
            return
        primary = _first_taction_short_in_simultaneous(sim) or 'Unknown'
        mob_pos = _mobile_position_from_simultaneous(sim)
        if mob_pos is not None:
            out.append(ScatterPointVfx(mob_pos[0], mob_pos[1], primary, 'mobile_position'))
            return
        for m in sim:
            if m.member == 'Actions':
                walk_taction_calls(m.v)

    def walk(root: Any) -> None:
        if isinstance(root, ndf.model.Object):
            if root.type == 'TSimultaneousAction':
                walk_simultaneous(root)
            for member in root:
                walk(member.v)
        elif isinstance(root, ndf.model.List):
            for row in root:
                walk(row.v)
        elif isinstance(root, ndf.model.MemberRow):
            walk(root.v)
        elif isinstance(root, ndf.model.Map):
            for mr in root:
                walk(mr.v)
        elif isinstance(root, ndf.model.ListRow):
            walk(root.v)

    walk(parsed_root)
    return out


def extract_ndf_xy_from_simultaneous_for_scatter(sim: ndf.model.Object) -> Optional[Tuple[float, float]]:
    """One NDF (dx, dy) for a single TSimultaneousAction (Mobile or first parPositionRelative)."""
    if sim.type != 'TSimultaneousAction':
        return None
    mob_pos = _mobile_position_from_simultaneous(sim)
    if mob_pos is not None:
        return mob_pos

    def collect_relative_from_taction(tac: ndf.model.Object) -> Optional[Tuple[float, float]]:
        if tac.type != 'TActionCall':
            return None
        for member in tac:
            if member.member != 'NamedParams' or not isinstance(member.v, ndf.model.Map):
                continue
            for map_row in member.v:
                key = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
                if key != 'parPositionRelative':
                    continue
                s = ndf.printer.string(map_row.v).strip()
                p = _parse_float3_plus_par(s)
                if p:
                    return p[0], p[1]
        return None

    def walk_taction_calls(node: Any) -> Optional[Tuple[float, float]]:
        if isinstance(node, ndf.model.Object):
            if node.type == 'TActionCall':
                got = collect_relative_from_taction(node)
                if got is not None:
                    return got
            for m in node:
                got = walk_taction_calls(m.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.List):
            for row in node:
                got = walk_taction_calls(row.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.MemberRow):
            return walk_taction_calls(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                got = walk_taction_calls(mr.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.ListRow):
            return walk_taction_calls(node.v)
        return None

    for m in sim:
        if m.member != 'Actions' or not isinstance(m.v, ndf.model.List):
            continue
        for row in m.v:
            seq = row.v
            if not isinstance(seq, ndf.model.Object) or seq.type != 'TSequentialAction':
                continue
            got = walk_taction_calls(seq)
            if got is not None:
                return got
    return None


def primary_vfx_short_from_simultaneous(sim: ndf.model.Object) -> str:
    """First TActionCall short name under this simultaneous group (for legend / filters)."""
    return _first_taction_short_in_simultaneous(sim) or ''


def extract_scatter_from_parsed(parsed_root: ndf.model.List) -> ScatterExtractionResult:
    """Collect (dx, dy) from Mobile Position and parPositionRelative patterns."""
    pts = extract_scatter_points_with_vfx(parsed_root)
    result = ScatterExtractionResult()
    for p in pts:
        result.points_ndf.append((p.dx_ndf, p.dy_ndf))
        result.sources.append(p.source)
    return result


def extract_scatter_from_file(path: Path) -> ScatterExtractionResult:
    text = path.read_text(encoding='utf-8')
    parsed = ndf.convert(text)
    if not isinstance(parsed, ndf.model.List):
        raise ValueError(f'Expected root List, got {type(parsed).__name__}')
    return extract_scatter_from_parsed(parsed)


def ndf_xy_to_gameplay_m(
    dx_ndf: float,
    dy_ndf: float,
    reference_gameplay_radius_m: float,
    anchor_max_ndf_radius: float,
) -> Tuple[float, float]:
    """Linear map: vanilla max radius -> reference_gameplay_radius_m."""
    if anchor_max_ndf_radius <= 0:
        return dx_ndf, dy_ndf
    s = reference_gameplay_radius_m / anchor_max_ndf_radius
    return dx_ndf * s, dy_ndf * s


def gameplay_m_to_ndf_xy(
    gx: float,
    gy: float,
    reference_gameplay_radius_m: float,
    anchor_max_ndf_radius: float,
) -> Tuple[float, float]:
    if reference_gameplay_radius_m <= 0:
        return gx, gy
    inv = anchor_max_ndf_radius / reference_gameplay_radius_m
    return gx * inv, gy * inv


def detect_emit_mode(parsed_root: ndf.model.List) -> str:
    """Return 'mobile_position' if any Mobile Position found, else 'position_relative_in_namedparams'."""
    ex = extract_scatter_from_parsed(parsed_root)
    if any(s == 'mobile_position' for s in ex.sources):
        return 'mobile_position'
    if any(s == 'par_position_relative' for s in ex.sources):
        return 'position_relative_in_namedparams'
    return 'mobile_position'
