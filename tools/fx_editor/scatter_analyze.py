"""Aggregate VFX call counts and burst stats from parsed FX NDF."""

from __future__ import annotations

import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .scatter_emit import find_actions_list
from .scatter_extract import _action_short_from_taction, _mobile_position_from_simultaneous, detect_emit_mode
from .scatter_timeline import _events_in_sequential_with_calls, _list_row_child_v


def _count_taction_calls_under(node: Any) -> Counter:
    c: Counter = Counter()

    def walk(n: Any) -> None:
        if isinstance(n, ndf.model.Object):
            if n.type == 'TActionCall':
                s = _action_short_from_taction(n)
                if s:
                    c[s] += 1
            for m in n:
                walk(m.v)
        elif isinstance(n, ndf.model.List):
            try:
                rows = list(n)
            except Exception:
                return
            for row in rows:
                rv = _list_row_child_v(row)
                if rv is not None:
                    walk(rv)
        elif isinstance(n, ndf.model.MemberRow):
            walk(n.v)
        elif isinstance(n, ndf.model.Map):
            for mr in n:
                walk(mr.v)
        elif isinstance(n, ndf.model.ListRow):
            lr = _list_row_child_v(n)
            if lr is not None:
                walk(lr)

    walk(node)
    return c


@dataclass
class ScatterEffectSummary:
    burst_count: int = 0
    vfx_call_counts: Dict[str, int] = field(default_factory=dict)
    emit_mode: str = ''
    total_taction_calls: int = 0


def summarize_scatter_ndf(parsed_root: ndf.model.List) -> ScatterEffectSummary:
    emit_mode = 'mobile_position'
    try:
        emit_mode = detect_emit_mode(parsed_root)
    except Exception:
        pass
    actions = find_actions_list(parsed_root)
    if actions is None:
        return ScatterEffectSummary(emit_mode=emit_mode)
    burst_count = 0
    total: Counter = Counter()
    try:
        action_rows = list(actions)
    except Exception:
        return ScatterEffectSummary(emit_mode=emit_mode)
    for row in action_rows:
        sim = _list_row_child_v(row)
        if sim is None or not isinstance(sim, ndf.model.Object) or sim.type != 'TSimultaneousAction':
            continue
        burst_count += 1
        total.update(_count_taction_calls_under(sim))
    return ScatterEffectSummary(
        burst_count=burst_count,
        vfx_call_counts=dict(sorted(total.items())),
        emit_mode=emit_mode,
        total_taction_calls=sum(total.values()),
    )


def _named_param_keys_on_taction(tac: ndf.model.Object) -> set:
    if tac.type != 'TActionCall':
        return set()
    out: set[str] = set()
    for member in tac:
        if member.member != 'NamedParams' or not isinstance(member.v, ndf.model.Map):
            continue
        for map_row in member.v:
            key = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
            if key:
                out.add(key)
    return out


def _position_flags_for_sim(sim: ndf.model.Object) -> Tuple[bool, bool, bool]:
    """Returns (has_global_mobile, has_parPositionRelative, has_parRandomPosition)."""
    has_mobile = _mobile_position_from_simultaneous(sim) is not None
    has_rel = False
    has_rand = False

    def walk(n: Any) -> None:
        nonlocal has_rel, has_rand
        if isinstance(n, ndf.model.Object):
            if n.type == 'TActionCall':
                keys = _named_param_keys_on_taction(n)
                if 'parPositionRelative' in keys:
                    has_rel = True
                if 'parRandomPosition' in keys:
                    has_rand = True
            for m in n:
                walk(m.v)
        elif isinstance(n, ndf.model.List):
            try:
                rows = list(n)
            except Exception:
                return
            for row in rows:
                rv = _list_row_child_v(row)
                if rv is not None:
                    walk(rv)
        elif isinstance(n, ndf.model.MemberRow):
            walk(n.v)
        elif isinstance(n, ndf.model.Map):
            for mr in n:
                walk(mr.v)
        elif isinstance(n, ndf.model.ListRow):
            lr = _list_row_child_v(n)
            if lr is not None:
                walk(lr)

    walk(sim)
    return has_mobile, has_rel, has_rand


def _format_position_summary(mobile: bool, rel: bool, rnd: bool) -> str:
    parts: List[str] = []
    if mobile:
        parts.append('Global Mobile anchor')
    if rel:
        parts.append('parPositionRelative per call')
    if rnd:
        parts.append('parRandomPosition per call')
    if not parts:
        return 'No Mobile; no positional NamedParams on calls'
    return '; '.join(parts)


def _signature_and_timing_from_sim(
    sim: ndf.model.Object,
) -> Tuple[Optional[Tuple[Tuple[str, ...], ...]], List[List[Tuple[float, str]]]]:
    """One tuple element per top-level TSequentialAction branch: ordered VFX names in that branch."""
    sig_parts: List[Tuple[str, ...]] = []
    timing_branches: List[List[Tuple[float, str]]] = []
    for m in sim:
        if m.member != 'Actions' or not isinstance(m.v, ndf.model.List):
            continue
        try:
            seq_rows = list(m.v)
        except Exception:
            continue
        for seq_row in seq_rows:
            seq = _list_row_child_v(seq_row)
            if not isinstance(seq, ndf.model.Object) or seq.type != 'TSequentialAction':
                continue
            entries = _events_in_sequential_with_calls(seq)
            branch_vfx = tuple(vfx for _, vfx, _ in entries)
            if branch_vfx:
                sig_parts.append(branch_vfx)
                timing_branches.append([(t, vfx) for t, vfx, _ in entries])
    if not sig_parts:
        return None, []
    return tuple(sig_parts), timing_branches


def _format_signature(sig: Tuple[Tuple[str, ...], ...]) -> str:
    branch_strs = []
    for branch in sig:
        branch_strs.append(' → '.join(branch))
    return ' || '.join(branch_strs)


def _first_branch_first_fire_time(sim: ndf.model.Object) -> Optional[float]:
    """Cumulative t of the first TActionCall in the first top-level TSequentialAction (per-burst timing key)."""
    for m in sim:
        if m.member != 'Actions' or not isinstance(m.v, ndf.model.List):
            continue
        try:
            seq_rows = list(m.v)
        except Exception:
            continue
        for seq_row in seq_rows:
            seq = _list_row_child_v(seq_row)
            if not isinstance(seq, ndf.model.Object) or seq.type != 'TSequentialAction':
                continue
            ev = _events_in_sequential_with_calls(seq)
            if ev:
                return ev[0][0]
    return None


def _format_burst_timing_histogram(sims: List[ndf.model.Object]) -> str:
    """Count how many bursts in the group use each first-branch first-fire time, e.g. 0.2s x 3, 0.35s x 2, 0.75s."""
    c: Counter = Counter()
    for sim in sims:
        t = _first_branch_first_fire_time(sim)
        if t is None:
            continue
        c[round(t, 6)] += 1
    if not c:
        return ''
    parts: List[str] = []
    for t in sorted(c.keys()):
        n = c[t]
        if n == 1:
            parts.append(f'{t:g}s')
        else:
            parts.append(f'{t:g}s x {n}')
    return ', '.join(parts)


@dataclass
class EffectGroupRow:
    pattern: Tuple[Tuple[str, ...], ...]
    count: int
    effects: str
    timing: str
    positioning: str
    branch_timings: List[List[Tuple[float, str]]] = field(default_factory=list)


def format_effect_group_block(row: EffectGroupRow, index: int) -> str:
    """Human-readable multi-line description of one effect group (for UI)."""
    lines: List[str] = []
    lines.append(f'── Group {index}  —  ×{row.count} burst(s) with this pattern')
    lines.append(f'Position: {row.positioning}')
    if row.timing:
        lines.append(f'Timing: {row.timing}  (first branch, first fire per burst)')
    lines.append('')
    if len(row.branch_timings) > 1:
        lines.append('  Parallel branches (one TSequentialAction each; all start together):')
    else:
        lines.append('  Single TSequentialAction branch:')
    for bi, branch in enumerate(row.branch_timings, start=1):
        lines.append(f'    Branch {bi}')
        if not branch:
            lines.append('      (no TActionCall)')
        else:
            for t, vfx in branch:
                lines.append(f'      t={t:g}s  →  {vfx}')
    lines.append('')
    return '\n'.join(lines)


def effect_group_key(row: EffectGroupRow) -> str:
    """Stable key for UI toggles (matches grouped pattern string)."""
    return row.effects


def _index_for_target_radius(target_radius_m: float, target_radii_m: List[float]) -> int:
    """Index into ``target_radii_m`` for ``target_radius_m`` (exact match if possible, else nearest)."""
    if not target_radii_m:
        return 0
    tr = float(target_radius_m)
    for i, t in enumerate(target_radii_m):
        if abs(float(t) - tr) < 1e-6:
            return i
    return min(
        range(len(target_radii_m)),
        key=lambda i: abs(float(target_radii_m[i]) - tr),
    )


def merge_effect_qty_pct_for_target_radius(
    groups: List[EffectGroupRow],
    key_to_curve: Dict[str, List[float]],
    target_radius_m: float,
    target_radii_m: List[float],
) -> Optional[Dict[str, float]]:
    """Map VFX short name → qty % at ``target_radius_m`` from per-pattern curves (one value per target radius).

    If a VFX appears in multiple merged groups, the **minimum** curve value at that radius applies.
    Returns ``None`` when all merged values are ~100% (no effective scaling).
    """
    if not groups or not key_to_curve or not target_radii_m:
        return None
    idx = _index_for_target_radius(target_radius_m, target_radii_m)
    out: Dict[str, float] = {}
    for g in groups:
        k = effect_group_key(g)
        if k not in key_to_curve:
            continue
        curve = key_to_curve[k]
        pct = float(curve[idx]) if idx < len(curve) else 100.0
        for branch in g.pattern:
            for vfx in branch:
                if vfx not in out:
                    out[vfx] = pct
                else:
                    out[vfx] = min(out[vfx], pct)
    if not out:
        return None
    if all(abs(v - 100.0) < 1e-6 for v in out.values()):
        return None
    return out


def merge_effect_radius_falloff_curves(
    groups: List[EffectGroupRow],
    key_to_curve: Dict[str, List[float]],
) -> Optional[Dict[str, List[float]]]:
    """Map VFX short name → falloff curve (qty %% vs distance/target radius). Same pattern as qty curves.

    If a VFX appears in multiple merged groups, the **minimum** value at each sample index applies.
    Returns ``None`` when there are no groups, no curves, or no group key matches ``key_to_curve``.
    """
    from .radius_falloff import RADIUS_FALLOFF_SAMPLES, align_radius_falloff_curve

    if not groups or not key_to_curve:
        return None
    samples = RADIUS_FALLOFF_SAMPLES
    out: Dict[str, List[float]] = {}
    for g in groups:
        k = effect_group_key(g)
        if k not in key_to_curve:
            continue
        curve = align_radius_falloff_curve(key_to_curve[k], samples)
        for branch in g.pattern:
            for vfx in branch:
                if vfx not in out:
                    out[vfx] = curve[:]
                else:
                    out[vfx] = [min(a, b) for a, b in zip(out[vfx], curve)]
    if not out:
        return None
    return out


def effect_count_scale_pct_from_group_sliders(
    groups: List[EffectGroupRow],
    key_to_pct: Dict[str, float],
) -> Dict[str, float]:
    """Map VFX short name → Param Qty %% (0–100) from per-pattern row keys.

    If the same VFX appears in multiple merged groups, the **minimum** slider value applies
    (stricter cap).
    """
    out: Dict[str, float] = {}
    for g in groups:
        k = effect_group_key(g)
        if k not in key_to_pct:
            continue
        pct = float(key_to_pct[k])
        for branch in g.pattern:
            for vfx in branch:
                if vfx not in out:
                    out[vfx] = pct
                else:
                    out[vfx] = min(out[vfx], pct)
    return out


def effect_named_flags_from_group_toggles(
    groups: List[EffectGroupRow],
    toggles: Dict[str, Tuple[bool, bool]],
) -> Dict[str, Dict[str, bool]]:
    """Map VFX short names to {size, count} OR-merge from per-group (keyed by ``effect_group_key``)."""
    out: Dict[str, Dict[str, bool]] = {}
    for g in groups:
        k = effect_group_key(g)
        if k not in toggles:
            continue
        sz, ct = toggles[k]
        for branch in g.pattern:
            for vfx in branch:
                if vfx not in out:
                    out[vfx] = {'size': False, 'count': False}
                out[vfx]['size'] = out[vfx]['size'] or sz
                out[vfx]['count'] = out[vfx]['count'] or ct
    return out


def format_effect_groups_document(groups: List[EffectGroupRow]) -> str:
    """Full scrollable document for the scatter “effect groups” panel."""
    if not groups:
        return '(No TSimultaneousAction groups with VFX were found.)\n'
    parts: List[str] = []
    parts.append(
        'Legend: each block is one distinct burst layout. Branches listed under the same group '
        'run in parallel inside one TSimultaneousAction; within a branch, t is cumulative '
        '(TWaitInSec delays before each TActionCall). '
        'The Timing line counts bursts by the first fire time on branch 1 (when delays differ across bursts).\n',
    )
    for i, g in enumerate(groups, start=1):
        parts.append(format_effect_group_block(g, i))
    return '\n'.join(parts).rstrip() + '\n'


def analyze_effect_groups(parsed_root: ndf.model.List) -> List[EffectGroupRow]:
    """Group TSimultaneousAction bursts that share the same per-branch VFX pattern (order preserved)."""
    actions = find_actions_list(parsed_root)
    if actions is None:
        return []
    buckets: Dict[Tuple[Tuple[str, ...], ...], List[ndf.model.Object]] = defaultdict(list)
    try:
        action_rows = list(actions)
    except Exception:
        return []
    for row in action_rows:
        sim = _list_row_child_v(row)
        if sim is None or not isinstance(sim, ndf.model.Object) or sim.type != 'TSimultaneousAction':
            continue
        sig, timing_branches = _signature_and_timing_from_sim(sim)
        if sig is None:
            continue
        buckets[sig].append(sim)

    rows: List[EffectGroupRow] = []
    for sig, sims in buckets.items():
        _, rep_branch_timings = _signature_and_timing_from_sim(sims[0])
        timing = _format_burst_timing_histogram(sims)

        pos_strs = [_format_position_summary(*_position_flags_for_sim(s)) for s in sims]
        if len(set(pos_strs)) == 1:
            positioning = pos_strs[0]
        else:
            positioning = 'Mixed: ' + '; '.join(sorted(set(pos_strs)))

        rows.append(
            EffectGroupRow(
                pattern=sig,
                count=len(sims),
                effects=_format_signature(sig),
                timing=timing,
                positioning=positioning,
                branch_timings=rep_branch_timings,
            ),
        )

    rows.sort(key=lambda r: (-r.count, r.effects))
    return rows


def vfx_effect_group_burst_counts(parsed_root: ndf.model.List) -> Dict[str, int]:
    """Per VFX: sum of ``×N`` burst counts from each effect group whose pattern contains that VFX.

    Effect groups (:func:`analyze_effect_groups`) bucket ``TSimultaneousAction`` rows by identical
    per-branch VFX signature; ``EffectGroupRow.count`` is ``len(sims)`` — the ``×544 burst(s)`` line.
    For a VFX that appears in multiple distinct patterns, this sums those ``N`` (e.g. 252 + 180).
    """
    groups = analyze_effect_groups(parsed_root)
    out: Dict[str, int] = defaultdict(int)
    for g in groups:
        vfx_in_g: Set[str] = set()
        for branch in g.pattern:
            for vfx in branch:
                vfx_in_g.add(vfx)
        for vfx in vfx_in_g:
            out[vfx] += g.count
    return dict(out)


def merge_effect_group_rows(row_lists: List[List[EffectGroupRow]]) -> List[EffectGroupRow]:
    """Union effect groups from multiple NDF parses. Same VFX pattern in different files merges into one row."""
    by_pattern: Dict[Tuple[Tuple[str, ...], ...], List[EffectGroupRow]] = defaultdict(list)
    for rows in row_lists:
        for r in rows:
            by_pattern[r.pattern].append(r)
    out: List[EffectGroupRow] = []
    for _sig, lst in by_pattern.items():
        first = lst[0]
        total_count = sum(r.count for r in lst)
        timings = [r.timing for r in lst if r.timing]
        unique_timings = sorted(set(timings))
        if len(unique_timings) <= 1:
            timing = unique_timings[0] if unique_timings else ''
        else:
            timing = ' · '.join(unique_timings[:4]) + ('…' if len(unique_timings) > 4 else '')

        positions = [r.positioning for r in lst]
        unique_pos = sorted(set(positions))
        if len(unique_pos) == 1:
            positioning = unique_pos[0]
        else:
            positioning = 'Mixed: ' + '; '.join(unique_pos[:5]) + ('…' if len(unique_pos) > 5 else '')

        out.append(
            EffectGroupRow(
                pattern=first.pattern,
                count=total_count,
                effects=first.effects,
                timing=timing,
                positioning=positioning,
                branch_timings=list(first.branch_timings),
            ),
        )
    out.sort(key=lambda r: (-r.count, r.effects))
    return out
