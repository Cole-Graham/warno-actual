"""Scale how many ``TActionCall`` rows exist per VFX (separate from NamedParams ``parCount``)."""

from __future__ import annotations

import copy
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src import ndf

from .fx_logging import get_fx_logger
from .radius_falloff import (
    burst_indices_kept_by_spatial_independent_thinning,
    burst_indices_removed_by_spatial_trim,
    compute_call_spatial_burst_mults,
    ensure_spatial_trim_keeps_one_burst_per_vfx,
)
from .scatter_timeline import _list_row_child_v
from .size_batch import (
    _action_short_from_taction,
    compute_variant_t_and_collect_taction_rows,
)

_log = get_fx_logger("call_scale")

EffectCallScalePctMap = Dict[str, float]

# Sentinel ``EffectCallChange.vfx`` for spatial burst trimming (whole ``TSimultaneousAction`` rows).
SPATIAL_BURST_TRIM_VFX = '__spatial_burst_trim__'


@dataclass
class EffectCallChange:
    """One VFX whose ``TActionCall`` row count was adjusted."""

    vfx: str
    before: int
    after: int


def _collect_taction_call_rows(
    root: Any,
) -> List[Tuple[str, ndf.model.List, ndf.model.ListRow]]:
    """Preorder: ``(vfx, parent_list, list_row)`` for each ``ListRow`` whose ``.v`` is ``TActionCall``."""

    out: List[Tuple[str, ndf.model.List, ndf.model.ListRow]] = []

    def walk(node: Any) -> None:
        if isinstance(node, ndf.model.Object):
            for member in node:
                walk(member.v)
            return
        if isinstance(node, ndf.model.Map):
            for map_row in node:
                walk(map_row.v)
            return
        if isinstance(node, ndf.model.List):
            try:
                rows = list(node)
            except Exception:
                return
            for row in rows:
                rv = _list_row_child_v(row)
                if rv is None:
                    continue
                if isinstance(rv, ndf.model.Object) and rv.type == 'TActionCall':
                    vfx = _action_short_from_taction(rv)
                    if vfx:
                        out.append((vfx, node, row))
                walk(rv)
            return
        if isinstance(node, ndf.model.MemberRow):
            walk(node.v)
            return
        if isinstance(node, ndf.model.ListRow):
            lr = _list_row_child_v(node)
            if lr is not None:
                walk(lr)
            return

    walk(root)
    return out


def _index_in_list(parent: ndf.model.List, row: ndf.model.ListRow) -> int:
    for i, r in enumerate(parent):
        if r is row:
            return i
    raise ValueError('ListRow not found in parent List')


def _call_qty_weight_along_batch(scale_factor: float, smin: float, smax: float) -> float:
    """``w`` in ``[0, 1]``: position between smallest and largest batch scale factor (linear)."""
    span = smax - smin
    if span < 1e-12:
        return 1.0
    s = (scale_factor - smin) / span
    return max(0.0, min(1.0, float(s)))


def _trim_bursts_by_spatial_falloff(
    parsed_root: ndf.model.List,
    mults: List[float],
    *,
    dry_run: bool,
    removed_idx: Optional[Set[int]] = None,
) -> List[EffectCallChange]:
    """Remove whole ``TSimultaneousAction`` rows not kept by independent thinning (``p`` = curve weight).

    Pass ``removed_idx`` when it was already computed from ``mults`` to avoid a second thinning pass.
    """
    from .scatter_emit import find_actions_list, list_tsimultaneous_action_rows

    actions = find_actions_list(parsed_root)
    if actions is None:
        return []
    burst_rows = list_tsimultaneous_action_rows(actions)
    n = len(burst_rows)
    if n == 0:
        return []
    if len(mults) != n:
        _log.warning(
            'burst trim: mults length %d != TSimultaneousAction count %d; skipping trim',
            len(mults),
            n,
        )
        return []
    if removed_idx is None:
        removed_idx = burst_indices_removed_by_spatial_trim(mults)
    else:
        removed_idx = set(removed_idx)
    if not removed_idx:
        return []
    k = n - len(removed_idx)
    to_remove = [burst_rows[i] for i in removed_idx]
    if not dry_run:
        indexed: List[Tuple[ndf.model.List, int]] = []
        for row in to_remove:
            indexed.append((actions, _index_in_list(actions, row)))
        indexed.sort(key=lambda x: -x[1])
        for parent, idx in indexed:
            del parent[idx]
    return [EffectCallChange(vfx=SPATIAL_BURST_TRIM_VFX, before=n, after=k)]


def scale_effect_calls(
    parsed_root: ndf.model.List,
    effect_call_scale_pct: Optional[EffectCallScalePctMap],
    *,
    dry_run: bool = False,
    scale_factor: float = 1.0,
    effect_call_batch_scale_min: Optional[float] = None,
    effect_call_batch_scale_max: Optional[float] = None,
    call_radius_falloff_by_vfx: Optional[Dict[str, List[float]]] = None,
    target_radius_m: Optional[float] = None,
    ref_m: Optional[float] = None,
    anchor_r: Optional[float] = None,
    burst_gameplay_xy_m: Optional[List[Tuple[float, float]]] = None,
    spatial_burst_mults: Optional[Sequence[float]] = None,
) -> List[EffectCallChange]:
    """Set ``TActionCall`` row counts from source ``n``, radius scale, and Call Qty %%.

    Target count is ``max(1, round(n * scale_factor * effective_p))`` when ``n >= 1`` (each VFX
    keeps at least one row). ``effective_p`` applies the
    slider on the largest batch radius; smaller radii in the same batch ease toward keeping the
    natural ``n * scale_factor`` count.

    When ``call_radius_falloff_by_vfx`` and calibration args are set, **whole**
    ``TSimultaneousAction`` rows are removed from ``Actions``. Each burst gets a spatial weight
    (minimum of its VFX Call curves at ``r_norm`` = distance / target radius). Bursts are kept
    **independently** with that probability (deterministic per index) so radial density follows the
    curve in expectation; kept count is about ``sum(weights)`` but not forced to ``round(sum)``.
    After thinning, removed bursts are softened so **each VFX short name still appears in at least
    one kept burst** when possible. Remaining bursts are then scaled like the non-falloff path.
    Per-VFX ``TActionCall`` row targets are at least **1** whenever the source had rows (avoids
    dropping entire pattern groups when scaling down). Pass ``burst_gameplay_xy_m``
    (one point per emitted burst, same order) so ``r_norm`` does not depend on NDF string round-trip.

    Pass ``spatial_burst_mults`` when spatial weights were already computed for this tree (e.g.
    cluster pipeline) to avoid recomputing them.
    """
    smin = effect_call_batch_scale_min if effect_call_batch_scale_min is not None else scale_factor
    smax = effect_call_batch_scale_max if effect_call_batch_scale_max is not None else scale_factor

    use_call_radius_falloff = (
        call_radius_falloff_by_vfx is not None
        and len(call_radius_falloff_by_vfx) > 0
        and target_radius_m is not None
        and ref_m is not None
        and anchor_r is not None
    )

    if scale_factor == 1.0 and effect_call_scale_pct is None and not use_call_radius_falloff:
        return []

    changes: List[EffectCallChange] = []

    if use_call_radius_falloff:
        from .scatter_emit import find_actions_list, list_tsimultaneous_action_rows

        mults: List[float]
        if spatial_burst_mults is not None:
            actions = find_actions_list(parsed_root)
            nburst = len(list_tsimultaneous_action_rows(actions)) if actions else 0
            if len(spatial_burst_mults) == nburst:
                mults = list(spatial_burst_mults)
            else:
                _log.warning(
                    'scale_effect_calls: spatial_burst_mults length %d != TSimultaneousAction count %d; '
                    'recomputing spatial weights',
                    len(spatial_burst_mults),
                    nburst,
                )
                mults = compute_call_spatial_burst_mults(
                    parsed_root,
                    call_radius_falloff_by_vfx,
                    float(target_radius_m),
                    float(ref_m),
                    float(anchor_r),
                    burst_gameplay_xy_m,
                )
        else:
            mults = compute_call_spatial_burst_mults(
                parsed_root,
                call_radius_falloff_by_vfx,
                float(target_radius_m),
                float(ref_m),
                float(anchor_r),
                burst_gameplay_xy_m,
            )
        kept = burst_indices_kept_by_spatial_independent_thinning(mults)
        if mults:
            sw = sum(mults)
            _log.info(
                'scale_effect_calls (radius falloff path): burst spatial weight min=%.4f max=%.4f '
                '(n=%d bursts); independent thinning kept=%d (sum(weights)=%.2f)',
                min(mults),
                max(mults),
                len(mults),
                len(kept),
                sw,
            )
        removed_idx: Optional[Set[int]] = None
        if mults:
            removed_idx = {i for i in range(len(mults)) if i not in kept}
            before_rm = len(removed_idx)
            removed_idx = ensure_spatial_trim_keeps_one_burst_per_vfx(parsed_root, removed_idx)
            if len(removed_idx) < before_rm:
                _log.info(
                    'scale_effect_calls: spatial trim softened %d burst(s) so each VFX has ≥1 burst',
                    before_rm - len(removed_idx),
                )
        burst_changes = _trim_bursts_by_spatial_falloff(
            parsed_root,
            mults,
            dry_run=dry_run,
            removed_idx=removed_idx,
        )
        changes.extend(burst_changes)
        variant_t_by_id, rows_by_vfx = compute_variant_t_and_collect_taction_rows(parsed_root)
    else:
        variant_t_by_id, rows_by_vfx = compute_variant_t_and_collect_taction_rows(parsed_root)

    for vfx, rows in rows_by_vfx.items():
        pct = 100.0
        if effect_call_scale_pct is not None:
            pct = float(effect_call_scale_pct.get(vfx, 100.0))
        pct = max(0.0, min(100.0, pct))
        p = pct / 100.0
        w = _call_qty_weight_along_batch(scale_factor, smin, smax)
        effective_p = 1.0 + (p - 1.0) * w
        n = len(rows)
        if n == 0:
            continue
        k_target = max(0, int(round(n * scale_factor * effective_p + 1e-9)))
        k_target = max(k_target, 1)
        if k_target == n:
            continue

        entries: List[Tuple[ndf.model.List, ndf.model.ListRow, float, int]] = []
        for doc_i, (parent, row) in enumerate(rows):
            tact = _list_row_child_v(row)
            t = 1.0
            if tact is not None and isinstance(tact, ndf.model.Object) and tact.type == 'TActionCall':
                t = float(variant_t_by_id.get(id(tact), 1.0))
            entries.append((parent, row, t, doc_i))

        changes.append(EffectCallChange(vfx=vfx, before=n, after=k_target))
        if dry_run:
            continue

        if k_target < n:
            to_remove_n = n - k_target
            entries.sort(key=lambda x: (-x[2], -x[3]))
            to_remove = [(entries[i][0], entries[i][1]) for i in range(to_remove_n)]
            indexed: List[Tuple[ndf.model.List, int]] = []
            for parent, row in to_remove:
                indexed.append((parent, _index_in_list(parent, row)))
            indexed.sort(key=lambda x: (id(x[0]), -x[1]))
            for parent, idx in indexed:
                del parent[idx]
        else:
            extra = k_target - n
            for j in range(extra):
                parent, row, _, _ = entries[j % n]
                new_row = copy.deepcopy(row)
                idx = _index_in_list(parent, row)
                parent.insert(idx + 1, new_row)

    return changes


def format_call_qty_report_line(
    call_changes: List[EffectCallChange],
    *,
    effect_call_scale_pct: Optional[EffectCallScalePctMap] = None,
    scale_factor: float = 1.0,
    vfx_burst_denoms: Optional[Dict[str, int]] = None,
) -> str:
    """One-line summary of call-qty scaling (curve vs 100%); same math as FX Editor General preview.

    ``vfx_burst_denoms`` comes from :func:`~.scatter_analyze.vfx_effect_group_burst_counts` on the
    emitted tree **before** :func:`scale_effect_calls` (dry-run). Empty string if no changes.
    """
    if not call_changes:
        return ''
    pct_map = effect_call_scale_pct or {}
    bd = vfx_burst_denoms or {}
    sf = float(scale_factor)

    spatial = [c for c in call_changes if c.vfx == SPATIAL_BURST_TRIM_VFX]
    call_changes = [c for c in call_changes if c.vfx != SPATIAL_BURST_TRIM_VFX]
    parts: List[str] = []
    if spatial:
        c = spatial[0]
        parts.append(
            f'Call radius falloff (spatial): {int(c.before)}→{int(c.after)} TSimultaneousAction bursts',
        )

    def _call_pct(vfx: str) -> float:
        return float(pct_map.get(vfx, 100.0))

    def _baseline_rows_at_100_qty(n_src_rows: int) -> int:
        n = int(n_src_rows)
        return max(0, int(round(float(n) * sf + 1e-9)))

    def _all_have_burst_denoms(changes: List[EffectCallChange]) -> bool:
        if not bd or not changes:
            return False
        return all(c.vfx in bd and int(c.before) > 0 for c in changes)

    def _report_unit(changes: List[EffectCallChange]) -> str:
        return 'bursts' if _all_have_burst_denoms(changes) else 'TActionCall rows'

    def _sum_report_qty(changes: List[EffectCallChange], row_qty_fn: Any) -> int:
        if not changes:
            return 0
        if _all_have_burst_denoms(changes):
            t = 0
            for c in changes:
                rq = float(row_qty_fn(c))
                bf = float(c.before)
                N = float(bd[c.vfx])
                t += max(0, int(round(rq * N / bf)))
            return t
        t = 0
        for c in changes:
            t += int(row_qty_fn(c))
        return t

    curve_changes = [c for c in call_changes if _call_pct(c.vfx) < 100.0 - 1e-6]
    rest = [c for c in call_changes if _call_pct(c.vfx) >= 100.0 - 1e-6]

    if curve_changes:
        u = _report_unit(curve_changes)
        base_sum = _sum_report_qty(
            curve_changes,
            lambda c: _baseline_rows_at_100_qty(int(c.before)),
        )
        after_sum = _sum_report_qty(curve_changes, lambda c: int(c.after))
        parts.append(
            f'Call curve {len(curve_changes)} VFX: {base_sum}→{after_sum} {u} (100% qty→curve)',
        )
    if rest:
        trims = [c for c in rest if int(c.after) < int(c.before)]
        adds = [c for c in rest if int(c.after) > int(c.before)]
        if trims:
            u = _report_unit(trims)
            tr = _sum_report_qty(trims, lambda c: int(c.before) - int(c.after))
            parts.append(f'scale: {len(trims)} VFX, {tr} {u} removed')
        if adds:
            u = _report_unit(adds)
            ar = _sum_report_qty(adds, lambda c: int(c.after) - int(c.before))
            parts.append(f'scale: {len(adds)} VFX, {ar} {u} added')

    if not parts:
        return ''
    return ' | '.join(parts)
