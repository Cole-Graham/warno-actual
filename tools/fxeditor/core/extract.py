"""Extract positions, timing, and VFX short names from parsed NDF trees."""

from __future__ import annotations

import copy
import math
from dataclasses import dataclass, field
from typing import Any, List, Optional, Set, Tuple

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .ndf_io import (
    _SCATTER_NAMED_POSITION_KEYS,
    _list_row_child_v,
    action_short_from_taction,
    find_actions_list,
    first_taction_short_in_simultaneous,
    list_tsimultaneous_rows,
    mobile_position_from_simultaneous,
    parse_float3_plus_par,
    stringify_position_expr,
)


@dataclass
class ScatterPointVfx:
    """One scatter sample with VFX label, for scatter preview dots."""

    dx_ndf: float
    dy_ndf: float
    primary_vfx: str
    source: str  # 'mobile_position' | 'par_position_relative'


def extract_scatter_points_with_vfx(
    parsed_root: ndf.model.List,
) -> List[ScatterPointVfx]:
    """One dot per global burst (Mobile) or per parPositionRelative.

    For Mobile-positioned blocks: one dot at the Mobile position, labeled
    with the first TActionCall short name.
    For nil-Mobile blocks: one dot per parPositionRelative, labeled with
    that specific TActionCall's short name.
    """
    out: List[ScatterPointVfx] = []

    def collect_relative_from_taction(tac: ndf.model.Object) -> None:
        if tac.type != "TActionCall":
            return
        short = action_short_from_taction(tac)
        for member in tac:
            if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
                continue
            for map_row in member.v:
                key = strip_quotes(str(map_row.k)) if map_row.k is not None else ""
                if key not in _SCATTER_NAMED_POSITION_KEYS:
                    continue
                s = ndf.printer.string(map_row.v).strip()
                p = parse_float3_plus_par(s)
                if p:
                    label = short or "Unknown"
                    out.append(ScatterPointVfx(p[0], p[1], label, "par_position_relative"))

    def walk_taction_calls(node: Any) -> None:
        if isinstance(node, ndf.model.Object):
            if node.type == "TActionCall":
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
        if sim.type != "TSimultaneousAction":
            return
        primary = first_taction_short_in_simultaneous(sim) or "Unknown"
        mob_pos = mobile_position_from_simultaneous(sim)
        if mob_pos is not None:
            out.append(ScatterPointVfx(mob_pos[0], mob_pos[1], primary, "mobile_position"))
            return
        for m in sim:
            if m.member == "Actions":
                walk_taction_calls(m.v)

    def walk(root: Any) -> None:
        if isinstance(root, ndf.model.Object):
            if root.type == "TSimultaneousAction":
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


@dataclass
class BurstInfo:
    """Extracted info for one TSimultaneousAction (one burst site)."""

    index: int
    dx_ndf: float
    dy_ndf: float
    primary_vfx: str
    source_type: str  # 'mobile_position' | 'par_position_relative'
    wait_s: float = 0.0


def extract_ndf_xy_from_simultaneous(sim: ndf.model.Object) -> Optional[Tuple[float, float]]:
    """One NDF (dx, dy) for a TSimultaneousAction (Mobile or first parPositionRelative)."""
    if sim.type != "TSimultaneousAction":
        return None
    mob = mobile_position_from_simultaneous(sim)
    if mob is not None:
        return mob

    def collect_rel(tac: ndf.model.Object) -> Optional[Tuple[float, float]]:
        if tac.type != "TActionCall":
            return None
        for member in tac:
            if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
                continue
            for mr in member.v:
                key = strip_quotes(str(mr.k)) if mr.k is not None else ""
                if key != "parPositionRelative":
                    continue
                s = ndf.printer.string(mr.v).strip()
                p = parse_float3_plus_par(s)
                if p:
                    return p
        return None

    def walk_calls(node: Any) -> Optional[Tuple[float, float]]:
        if isinstance(node, ndf.model.Object):
            if node.type == "TActionCall":
                return collect_rel(node)
            for m in node:
                got = walk_calls(m.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.List):
            for row in node:
                got = walk_calls(row.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.MemberRow):
            return walk_calls(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                got = walk_calls(mr.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.ListRow):
            return walk_calls(node.v)
        return None

    for m in sim:
        if m.member != "Actions" or not isinstance(m.v, ndf.model.List):
            continue
        for row in m.v:
            seq = row.v
            if not isinstance(seq, ndf.model.Object) or seq.type != "TSequentialAction":
                continue
            got = walk_calls(seq)
            if got is not None:
                return got
    return None


def first_wait_in_simultaneous(sim: ndf.model.Object) -> Optional[float]:
    """First TWaitInSec.Duration in preorder under a TSimultaneousAction."""
    if sim.type != "TSimultaneousAction":
        return None

    def walk(node: Any) -> Optional[float]:
        if isinstance(node, ndf.model.Object):
            if node.type == "TWaitInSec":
                for m in node:
                    if m.member == "Duration":
                        return float(m.v)
                return None
            for m in node:
                got = walk(m.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.List):
            for row in node:
                got = walk(row.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.MemberRow):
            return walk(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                got = walk(mr.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.ListRow):
            return walk(node.v)
        return None

    return walk(sim)


def extract_burst_infos(parsed_root: ndf.model.List) -> List[BurstInfo]:
    """One BurstInfo per TSimultaneousAction in Actions list order."""
    actions = find_actions_list(parsed_root)
    if actions is None:
        return []
    out: List[BurstInfo] = []
    for i, row in enumerate(list_tsimultaneous_rows(actions)):
        sim = row.v
        if not isinstance(sim, ndf.model.Object):
            continue
        mob = mobile_position_from_simultaneous(sim)
        if mob is not None:
            dx, dy = mob
            src = "mobile_position"
        else:
            pt = extract_ndf_xy_from_simultaneous(sim)
            if pt is None:
                continue
            dx, dy = pt
            src = "par_position_relative"
        vfx = first_taction_short_in_simultaneous(sim) or "Unknown"
        w = first_wait_in_simultaneous(sim)
        out.append(BurstInfo(
            index=i,
            dx_ndf=dx,
            dy_ndf=dy,
            primary_vfx=vfx,
            source_type=src,
            wait_s=round(w, 2) if w is not None else 0.0,
        ))
    return out


# ── distinct relative float3 anchors in one TSimultaneousAction ──

def collect_ordered_distinct_relative_float3(sim: ndf.model.Object) -> List[Tuple[float, float]]:
    seen: Set[Tuple[int, int]] = set()
    out: List[Tuple[float, float]] = []

    def from_taction(tac: ndf.model.Object) -> None:
        if tac.type != "TActionCall":
            return
        for member in tac:
            if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
                continue
            for mr in member.v:
                key = strip_quotes(str(mr.k)) if mr.k is not None else ""
                if key not in _SCATTER_NAMED_POSITION_KEYS:
                    continue
                s = ndf.printer.string(mr.v).strip()
                p = parse_float3_plus_par(s)
                if p:
                    k = (int(round(p[0])), int(round(p[1])))
                    if k not in seen:
                        seen.add(k)
                        out.append((float(p[0]), float(p[1])))

    def walk(node: Any) -> None:
        if isinstance(node, ndf.model.Object):
            if node.type == "TActionCall":
                from_taction(node)
            for m in node:
                walk(m.v)
        elif isinstance(node, ndf.model.List):
            for row in node:
                walk(row.v)
        elif isinstance(node, ndf.model.MemberRow):
            walk(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                walk(mr.v)
        elif isinstance(node, ndf.model.ListRow):
            walk(node.v)

    if sim.type != "TSimultaneousAction":
        return out
    for m in sim:
        if m.member != "Actions" or not isinstance(m.v, ndf.model.List):
            continue
        for row in m.v:
            walk(row.v)
    return out


# ── position assignment on cloned templates ───────────────────────

def set_mobile_position(sim: ndf.model.Object, dx_ndf: float, dy_ndf: float) -> bool:
    if sim.type != "TSimultaneousAction":
        return False
    expr = stringify_position_expr(dx_ndf, dy_ndf)
    for m in sim:
        if m.member != "Mobile" or not isinstance(m.v, ndf.model.Object):
            continue
        mob = m.v
        if mob.type != "TMobileWithLocalRepereMatrixFactory":
            continue
        for mm in mob:
            if mm.member == "Position":
                mm.v = expr
                return True
    return False


def replace_all_scatter_position_params(root: Any, dx_ndf: float, dy_ndf: float) -> int:
    expr = stringify_position_expr(dx_ndf, dy_ndf)
    n = 0

    def walk(node: Any) -> None:
        nonlocal n
        if isinstance(node, ndf.model.Object):
            if node.type == "TActionCall":
                for member in node:
                    if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
                        continue
                    for mr in member.v:
                        key = strip_quotes(str(mr.k)) if mr.k is not None else ""
                        if key in _SCATTER_NAMED_POSITION_KEYS:
                            mr.v = expr
                            n += 1
            for member in node:
                walk(member.v)
        elif isinstance(node, ndf.model.List):
            for row in node:
                walk(row.v)
        elif isinstance(node, ndf.model.MemberRow):
            walk(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                walk(mr.v)
        elif isinstance(node, ndf.model.ListRow):
            walk(node.v)

    walk(root)
    return n


def replace_scatter_params_multi_anchor(
    root: Any,
    bx_ndf: float,
    by_ndf: float,
    ref_ndf_x: float,
    ref_ndf_y: float,
    scale: float,
) -> int:
    """Map each float3+parPosition to burst-centered layout preserving scaled deltas from ref."""
    n = 0
    sc = float(scale)

    def walk(node: Any) -> None:
        nonlocal n
        if isinstance(node, ndf.model.Object):
            if node.type == "TActionCall":
                for member in node:
                    if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
                        continue
                    for mr in member.v:
                        key = strip_quotes(str(mr.k)) if mr.k is not None else ""
                        if key not in _SCATTER_NAMED_POSITION_KEYS:
                            continue
                        s = ndf.printer.string(mr.v).strip()
                        p = parse_float3_plus_par(s)
                        if p:
                            lx, ly = float(p[0]), float(p[1])
                            nx = bx_ndf + (lx - ref_ndf_x) * sc
                            ny = by_ndf + (ly - ref_ndf_y) * sc
                            mr.v = stringify_position_expr(nx, ny)
                            n += 1
                            continue
                        s_compact = s.replace(" ", "").lower()
                        if s_compact == "parposition":
                            mr.v = stringify_position_expr(bx_ndf, by_ndf)
                            n += 1
            for member in node:
                walk(member.v)
        elif isinstance(node, ndf.model.List):
            for row in node:
                walk(row.v)
        elif isinstance(node, ndf.model.MemberRow):
            walk(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                walk(mr.v)
        elif isinstance(node, ndf.model.ListRow):
            walk(node.v)

    walk(root)
    return n


def apply_burst_position(
    sim: ndf.model.Object,
    burst_x_gameplay: float,
    burst_y_gameplay: float,
    ref_m: float,
    anchor_r: float,
    *,
    cluster_radius_scale: Optional[float] = None,
) -> Tuple[bool, int]:
    """Place one burst: Mobile and/or named scatter params."""
    if sim.type != "TSimultaneousAction":
        return False, 0
    if ref_m <= 0:
        return False, 0
    inv = anchor_r / ref_m
    bx_ndf = float(int(round(burst_x_gameplay * inv)))
    by_ndf = float(int(round(burst_y_gameplay * inv)))

    mob = mobile_position_from_simultaneous(sim)
    if mob is not None:
        mobile_ok = set_mobile_position(sim, bx_ndf, by_ndf)
        n_named = replace_all_scatter_position_params(sim, bx_ndf, by_ndf)
        return mobile_ok, n_named

    distinct = collect_ordered_distinct_relative_float3(sim)
    scale = float(cluster_radius_scale) if cluster_radius_scale is not None else 1.0

    if len(distinct) <= 1:
        n_named = replace_all_scatter_position_params(sim, bx_ndf, by_ndf)
        return False, n_named

    ref_x, ref_y = float(distinct[0][0]), float(distinct[0][1])
    n_named = replace_scatter_params_multi_anchor(sim, bx_ndf, by_ndf, ref_x, ref_y, scale)
    if n_named == 0:
        n_named = replace_all_scatter_position_params(sim, bx_ndf, by_ndf)
    return False, n_named


# ── position clamping ─────────────────────────────────────────────

def clamp_ndf_to_disk(
    dx_ndf: float,
    dy_ndf: float,
    *,
    radius_m: float,
    ref_m: float,
    anchor_r: float,
) -> Tuple[float, float]:
    if ref_m <= 0 or anchor_r <= 0:
        return dx_ndf, dy_ndf
    s = ref_m / anchor_r
    gx, gy = dx_ndf * s, dy_ndf * s
    h = math.hypot(gx, gy)
    r = max(1e-6, float(radius_m))
    if h <= r + 1e-6:
        return float(int(round(dx_ndf))), float(int(round(dy_ndf)))
    k = r / h
    return float(int(round(dx_ndf * k))), float(int(round(dy_ndf * k)))


def clamp_positions_to_disk(
    parsed_root: ndf.model.List,
    *,
    radius_m: float,
    ref_m: float,
    anchor_r: float,
) -> int:
    """Ensure every positioned anchor lies within radius_m gameplay disk."""
    if radius_m <= 0:
        return 0
    actions = find_actions_list(parsed_root)
    if actions is None:
        return 0
    total = 0
    for row in list_tsimultaneous_rows(actions):
        sim = row.v
        if not isinstance(sim, ndf.model.Object) or sim.type != "TSimultaneousAction":
            continue
        mob = mobile_position_from_simultaneous(sim)
        if mob is not None:
            dx, dy = float(mob[0]), float(mob[1])
            nx, ny = clamp_ndf_to_disk(dx, dy, radius_m=radius_m, ref_m=ref_m, anchor_r=anchor_r)
            if abs(nx - dx) > 1e-9 or abs(ny - dy) > 1e-9:
                set_mobile_position(sim, nx, ny)
                replace_all_scatter_position_params(sim, nx, ny)
                total += 1
        else:
            # Clamp nil-mobile scatter params independently
            def _clamp_nil(node: Any) -> int:
                cnt = 0
                if isinstance(node, ndf.model.Object):
                    if node.type == "TActionCall":
                        for member in node:
                            if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
                                continue
                            for mr in member.v:
                                key = strip_quotes(str(mr.k)) if mr.k is not None else ""
                                if key not in _SCATTER_NAMED_POSITION_KEYS:
                                    continue
                                s = ndf.printer.string(mr.v).strip()
                                p = parse_float3_plus_par(s)
                                if not p:
                                    continue
                                lx, ly = float(p[0]), float(p[1])
                                cx, cy = clamp_ndf_to_disk(lx, ly, radius_m=radius_m, ref_m=ref_m, anchor_r=anchor_r)
                                if abs(cx - lx) > 1e-9 or abs(cy - ly) > 1e-9:
                                    mr.v = stringify_position_expr(cx, cy)
                                    cnt += 1
                    for member in node:
                        cnt += _clamp_nil(member.v)
                elif isinstance(node, ndf.model.List):
                    for r in node:
                        cnt += _clamp_nil(r.v)
                elif isinstance(node, ndf.model.MemberRow):
                    cnt += _clamp_nil(node.v)
                elif isinstance(node, ndf.model.Map):
                    for mr in node:
                        cnt += _clamp_nil(mr.v)
                elif isinstance(node, ndf.model.ListRow):
                    cnt += _clamp_nil(node.v)
                return cnt
            total += _clamp_nil(sim)
    return total


# ── wait duration helpers ────────────────────────────────────────

def set_first_wait_duration(sim: ndf.model.Object, duration: Optional[float]) -> None:
    if duration is None:
        return
    d = round(float(duration) + 1e-12, 2)

    def walk(node: Any) -> bool:
        if isinstance(node, ndf.model.Object):
            if node.type == "TWaitInSec":
                for m in node:
                    if m.member == "Duration":
                        m.v = d
                        return True
                return False
            for m in node:
                if walk(m.v):
                    return True
        elif isinstance(node, ndf.model.List):
            for row in node:
                if walk(row.v):
                    return True
        elif isinstance(node, ndf.model.MemberRow):
            return walk(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                if walk(mr.v):
                    return True
        elif isinstance(node, ndf.model.ListRow):
            return walk(node.v)
        return False

    walk(sim)
