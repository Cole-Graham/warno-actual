"""Generate Actions list from a ScatterProject by cloning a TSimultaneousAction template."""

from __future__ import annotations

import copy
import sys
from pathlib import Path
from typing import Any, List, Optional, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .scatter_extract import (
    _mobile_position_from_simultaneous,
    _parse_float3_plus_par,
    _stringify_position_expr,
    gameplay_m_to_ndf_xy,
    ndf_xy_to_gameplay_m,
)
from .scatter_model import ScatterProject

# NamedParams that encode burst XY as float3[…] + parPosition (same emit replacement as parPositionRelative).
_SCATTER_NAMED_POSITION_KEYS = frozenset({'parPositionRelative', 'parStartPosition'})


def list_tsimultaneous_action_rows(actions: ndf.model.List) -> List[Any]:
    """Ordered list rows whose value is ``TSimultaneousAction``."""
    out: List[Any] = []
    for row in actions:
        try:
            sim = row.v
        except Exception:
            continue
        if isinstance(sim, ndf.model.Object) and sim.type == 'TSimultaneousAction':
            out.append(row)
    return out


def find_actions_list(parsed_root: ndf.model.List) -> Optional[ndf.model.List]:
    """First export object's ``Actions`` member list."""
    if len(parsed_root) == 0:
        return None
    first = parsed_root[0]
    if not isinstance(first, ndf.model.ListRow):
        return None
    obj = first.v
    if not isinstance(obj, ndf.model.Object):
        return None
    for member in obj:
        if member.member == 'Actions' and isinstance(member.v, ndf.model.List):
            return member.v
    return None


def _set_mobile_position_on_simultaneous(simultaneous: ndf.model.Object, dx_ndf: float, dy_ndf: float) -> bool:
    if simultaneous.type != 'TSimultaneousAction':
        return False
    expr = _stringify_position_expr(dx_ndf, dy_ndf)
    for m in simultaneous:
        if m.member != 'Mobile' or not isinstance(m.v, ndf.model.Object):
            continue
        mob = m.v
        if mob.type != 'TMobileWithLocalRepereMatrixFactory':
            continue
        for mm in mob:
            if mm.member == 'Position':
                mm.v = expr
                return True
    return False


def _replace_all_scatter_named_position_params(root: Any, dx_ndf: float, dy_ndf: float) -> int:
    """Set ``parPositionRelative`` / ``parStartPosition`` to ``float3[dx,dy,0] + parPosition`` (vanilla style)."""
    expr = _stringify_position_expr(dx_ndf, dy_ndf)
    n = 0

    def walk(node: Any) -> None:
        nonlocal n
        if isinstance(node, ndf.model.Object):
            if node.type == 'TActionCall':
                for member in node:
                    if member.member != 'NamedParams' or not isinstance(member.v, ndf.model.Map):
                        continue
                    for map_row in member.v:
                        key = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
                        if key in _SCATTER_NAMED_POSITION_KEYS:
                            map_row.v = expr
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


def _collect_ordered_distinct_relative_float3_ndf(sim: ndf.model.Object) -> List[Tuple[float, float]]:
    """Distinct ``float3[…] + parPosition`` anchors under one ``TSimultaneousAction`` (source order)."""
    seen: Set[Tuple[int, int]] = set()
    out: List[Tuple[float, float]] = []

    def from_taction(tac: ndf.model.Object) -> None:
        if tac.type != 'TActionCall':
            return
        for member in tac:
            if member.member != 'NamedParams' or not isinstance(member.v, ndf.model.Map):
                continue
            for map_row in member.v:
                key = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
                if key not in _SCATTER_NAMED_POSITION_KEYS:
                    continue
                s = ndf.printer.string(map_row.v).strip()
                p = _parse_float3_plus_par(s)
                if p:
                    k = (int(round(p[0])), int(round(p[1])))
                    if k not in seen:
                        seen.add(k)
                        out.append((float(p[0]), float(p[1])))

    def walk(node: Any) -> None:
        if isinstance(node, ndf.model.Object):
            if node.type == 'TActionCall':
                from_taction(node)
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

    if sim.type != 'TSimultaneousAction':
        return out
    for m in sim:
        if m.member != 'Actions' or not isinstance(m.v, ndf.model.List):
            continue
        for row in m.v:
            walk(row.v)
    return out


def _replace_scatter_named_position_params_multi_anchor(
    root: Any,
    bx_ndf: float,
    by_ndf: float,
    ref_ndf_x: float,
    ref_ndf_y: float,
    scale: float,
) -> int:
    """Map each ``float3[lx,ly,0]+parPosition`` to burst-centered layout preserving scaled deltas from ref."""
    n = 0
    sc = float(scale)

    def walk(node: Any) -> None:
        nonlocal n
        if isinstance(node, ndf.model.Object):
            if node.type == 'TActionCall':
                for member in node:
                    if member.member != 'NamedParams' or not isinstance(member.v, ndf.model.Map):
                        continue
                    for map_row in member.v:
                        key = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
                        if key not in _SCATTER_NAMED_POSITION_KEYS:
                            continue
                        s = ndf.printer.string(map_row.v).strip()
                        p = _parse_float3_plus_par(s)
                        if p:
                            lx, ly = float(p[0]), float(p[1])
                            nx = bx_ndf + (lx - ref_ndf_x) * sc
                            ny = by_ndf + (ly - ref_ndf_y) * sc
                            map_row.v = _stringify_position_expr(nx, ny)
                            n += 1
                            continue
                        s_compact = s.replace(' ', '').lower()
                        if s_compact == 'parposition':
                            map_row.v = _stringify_position_expr(bx_ndf, by_ndf)
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


def apply_scatter_burst_positions_to_simultaneous(
    sim: ndf.model.Object,
    burst_x_gameplay_m: float,
    burst_y_gameplay_m: float,
    ref_m: float,
    anchor_r: float,
    *,
    cluster_radius_scale: Optional[float] = None,
) -> Tuple[bool, int]:
    """Place one burst: Mobile and/or named scatter params.

    * **Mobile** templates: same anchor for every nested call (vanilla paired rows).
    * **Nil Mobile** with multiple distinct ``float3 + parPosition`` anchors: map each call to
      ``burst + scale * (original - ref)`` so sub-impacts stay grouped when the effect radius grows.
    """
    if sim.type != 'TSimultaneousAction':
        return False, 0
    bx_ndf, by_ndf = gameplay_m_to_ndf_xy(
        float(burst_x_gameplay_m),
        float(burst_y_gameplay_m),
        float(ref_m),
        float(anchor_r),
    )
    bx_ndf = float(int(round(bx_ndf)))
    by_ndf = float(int(round(by_ndf)))

    mob = _mobile_position_from_simultaneous(sim)
    if mob is not None:
        mobile_ok = _set_mobile_position_on_simultaneous(sim, bx_ndf, by_ndf)
        n_named = _replace_all_scatter_named_position_params(sim, bx_ndf, by_ndf)
        return mobile_ok, n_named

    distinct = _collect_ordered_distinct_relative_float3_ndf(sim)
    scale = float(cluster_radius_scale) if cluster_radius_scale is not None else 1.0

    if len(distinct) <= 1:
        n_named = _replace_all_scatter_named_position_params(sim, bx_ndf, by_ndf)
        return False, n_named

    ref_x, ref_y = float(distinct[0][0]), float(distinct[0][1])
    n_named = _replace_scatter_named_position_params_multi_anchor(
        sim,
        bx_ndf,
        by_ndf,
        ref_x,
        ref_y,
        scale,
    )
    if n_named == 0:
        n_named = _replace_all_scatter_named_position_params(sim, bx_ndf, by_ndf)
    return False, n_named


def set_simultaneous_burst_gameplay_position_m(
    sim: ndf.model.Object,
    x_gameplay_m: float,
    y_gameplay_m: float,
    ref_m: float,
    anchor_r: float,
) -> bool:
    """Write burst anchor in gameplay meters (rounded NDF ints), matching :func:`emit_scatter_into_actions`.

    Nil-Mobile templates with several ``float3 + parPosition`` anchors are **translated** so relative
    sub-impact layout is preserved (used by Call falloff repositioning).
    """
    if sim.type != 'TSimultaneousAction':
        return False
    rm = float(ref_m)
    ar = float(anchor_r)
    tgx = float(int(round(float(x_gameplay_m))))
    tgy = float(int(round(float(y_gameplay_m))))

    mob = _mobile_position_from_simultaneous(sim)
    if mob is not None:
        dx_ndf, dy_ndf = gameplay_m_to_ndf_xy(tgx, tgy, rm, ar)
        dx_ndf = float(int(round(dx_ndf)))
        dy_ndf = float(int(round(dy_ndf)))
        mobile_ok = _set_mobile_position_on_simultaneous(sim, dx_ndf, dy_ndf)
        n_named = _replace_all_scatter_named_position_params(sim, dx_ndf, dy_ndf)
        return mobile_ok or n_named > 0

    distinct = _collect_ordered_distinct_relative_float3_ndf(sim)
    if len(distinct) <= 1:
        dx_ndf, dy_ndf = gameplay_m_to_ndf_xy(tgx, tgy, rm, ar)
        dx_ndf = float(int(round(dx_ndf)))
        dy_ndf = float(int(round(dy_ndf)))
        n_named = _replace_all_scatter_named_position_params(sim, dx_ndf, dy_ndf)
        return n_named > 0

    ref_lx, ref_ly = float(distinct[0][0]), float(distinct[0][1])
    ogx, ogy = ndf_xy_to_gameplay_m(ref_lx, ref_ly, rm, ar)
    ogx = float(int(round(ogx)))
    ogy = float(int(round(ogy)))
    dgx, dgy = tgx - ogx, tgy - ogy
    if rm <= 0 or ar <= 0:
        dndx, dndy = dgx, dgy
    else:
        dndx = dgx * (ar / rm)
        dndy = dgy * (ar / rm)
    new_bx = float(int(round(ref_lx + dndx)))
    new_by = float(int(round(ref_ly + dndy)))
    n_named = _replace_scatter_named_position_params_multi_anchor(
        sim,
        new_bx,
        new_by,
        ref_lx,
        ref_ly,
        1.0,
    )
    return n_named > 0


def _has_any_scatter_named_position_param(root: Any) -> bool:
    """True if any ``TActionCall`` has ``parPositionRelative`` or ``parStartPosition`` in NamedParams."""

    def walk(node: Any) -> bool:
        if isinstance(node, ndf.model.Object):
            if node.type == 'TActionCall':
                for member in node:
                    if member.member != 'NamedParams' or not isinstance(member.v, ndf.model.Map):
                        continue
                    for map_row in member.v:
                        key = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
                        if key in _SCATTER_NAMED_POSITION_KEYS:
                            return True
            for member in node:
                if walk(member.v):
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

    return walk(root)


def _tsimultaneous_has_placeable_hook(sim: ndf.model.Object) -> bool:
    """True if emit can set burst XY (Mobile ``Position`` or scatter NamedParams below)."""
    if sim.type != 'TSimultaneousAction':
        return False
    for m in sim:
        if m.member != 'Mobile' or not isinstance(m.v, ndf.model.Object):
            continue
        mob = m.v
        if mob.type != 'TMobileWithLocalRepereMatrixFactory':
            continue
        for mm in mob:
            if mm.member == 'Position':
                return True
    return _has_any_scatter_named_position_param(sim)


def list_placeable_tsimultaneous_templates(actions: ndf.model.List) -> List[Any]:
    """``TSimultaneousAction`` list rows that emit can position (skip spark-only / no-anchor rows)."""
    out: List[Any] = []
    for row in list_tsimultaneous_action_rows(actions):
        sim = row.v
        if isinstance(sim, ndf.model.Object) and _tsimultaneous_has_placeable_hook(sim):
            out.append(row)
    return out


def distinct_placeable_template_first_indices(templates: List[Any]) -> List[int]:
    """One template index per distinct burst pattern (effect-group VFX signature), source order.

    Matches :func:`scatter_analyze.analyze_effect_groups` bucketing for placeable rows: same
    ``_signature_and_timing_from_sim`` tuple, with ``sig is None`` keyed uniquely per index.
    """
    # Lazy import: scatter_analyze imports this module at load time.
    from .scatter_analyze import _signature_and_timing_from_sim

    seen: Set[Any] = set()
    out: List[int] = []
    for i, row in enumerate(templates):
        sim = row.v
        if not isinstance(sim, ndf.model.Object) or sim.type != 'TSimultaneousAction':
            continue
        sig, _ = _signature_and_timing_from_sim(sim)
        key = sig if sig is not None else ('__nosig__', i)
        if key in seen:
            continue
        seen.add(key)
        out.append(i)
    return out


def build_cluster_emit_template_indices(n_target: int, templates: List[Any]) -> Tuple[int, List[int]]:
    """Ensure enough bursts that each distinct placeable pattern is emitted at least once.

    When ``n_target`` is small, plain ``i % len(templates)`` only uses the first ``n_target``
    templates, so patterns whose first occurrence is later never appear. This bumps
    ``n_target`` to at least the distinct-pattern count and schedules indices so the first
    ``n_patterns`` bursts cover one representative each, then round-robin as before.

    Returns ``(n_target_eff, per_burst_template_index)`` with ``len(...) == n_target_eff``.
    """
    nt = len(templates)
    if nt == 0:
        return 0, []
    first = distinct_placeable_template_first_indices(templates)
    n_patterns = len(first)
    n_target_eff = max(1, int(n_target)) if n_target > 0 else 0
    n_target_eff = max(n_target_eff, n_patterns)
    out = list(first)
    for j in range(n_target_eff - n_patterns):
        out.append((n_patterns + j) % nt)
    return n_target_eff, out


def _optional_set_first_wait_duration(simultaneous: ndf.model.Object, duration: Optional[float]) -> None:
    if duration is None:
        return
    duration = round(float(duration) + 1e-12, 2)

    def walk(node: Any) -> bool:
        if isinstance(node, ndf.model.Object):
            if node.type == 'TWaitInSec':
                for m in node:
                    if m.member == 'Duration':
                        m.v = duration
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

    walk(simultaneous)


def emit_scatter_into_actions(project: ScatterProject, parsed_root: ndf.model.List) -> int:
    """Replace ``Actions`` with one ``TSimultaneousAction`` row per burst, cycling source patterns.

    Each burst deep-copies a template row. If :attr:`ScatterBurst.template_index` is set, that
    placeable row is used; otherwise round-robin by burst index (``i % n_templates``). Cluster
    builds set ``template_index`` so every distinct placeable burst pattern appears at least once
    even when the area-scaled burst count is small.
    """
    actions = find_actions_list(parsed_root)
    if actions is None:
        raise ValueError('No Actions list found in export.')
    if not project.bursts:
        raise ValueError('ScatterProject has no bursts.')

    templates = list_placeable_tsimultaneous_templates(actions)
    if not templates:
        raise ValueError(
            'No placeable TSimultaneousAction rows in Actions (each row needs Mobile '
            'TMobileWithLocalRepereMatrixFactory Position, or parPositionRelative / parStartPosition on a TActionCall).',
        )

    while len(actions) > 0:
        del actions[-1]

    ref_m = project.reference_gameplay_radius_m
    anchor_r = project.anchor_max_ndf_radius

    count = 0
    nt = len(templates)
    for i, burst in enumerate(project.bursts):
        if burst.template_index is not None:
            ti = int(burst.template_index) % nt
        else:
            ti = i % nt
        template_row = templates[ti]
        row = copy.deepcopy(template_row)
        sim = row.v
        if not isinstance(sim, ndf.model.Object) or sim.type != 'TSimultaneousAction':
            continue
        crs = getattr(project, 'cluster_radius_scale', None)
        mobile_ok, n_named = apply_scatter_burst_positions_to_simultaneous(
            sim,
            burst.x_gameplay_m,
            burst.y_gameplay_m,
            ref_m,
            anchor_r,
            cluster_radius_scale=crs,
        )
        if not mobile_ok and n_named == 0:
            raise ValueError(
                'emit: template has no Mobile Position (TMobileWithLocalRepereMatrixFactory) '
                'and no parPositionRelative or parStartPosition on TActionCall; cannot place burst.',
            )
        _optional_set_first_wait_duration(sim, burst.delay_s)
        actions.add(row)
        count += 1
    return count


def round_all_twait_duration_hundredths(root: Any) -> int:
    """Round every TWaitInSec.Duration to two decimal places (gameplay-stable output)."""
    n = 0

    def walk(node: Any) -> None:
        nonlocal n
        if isinstance(node, ndf.model.Object):
            if node.type == 'TWaitInSec':
                for m in node:
                    if m.member == 'Duration':
                        m.v = round(float(m.v) + 1e-12, 2)
                        n += 1
                        return
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

    walk(root)
    return n


def format_ndf(parsed_root: ndf.model.List) -> str:
    return ndf.printer.string(parsed_root)
