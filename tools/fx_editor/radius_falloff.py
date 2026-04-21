"""Spatial falloff vs normalized distance from scatter center (distance / target radius)."""

from __future__ import annotations

import hashlib
import math
import sys
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src import ndf

from .fx_logging import get_fx_logger
from .scatter_emit import (
    find_actions_list,
    list_tsimultaneous_action_rows,
    set_simultaneous_burst_gameplay_position_m,
)
from .scatter_extract import extract_ndf_xy_from_simultaneous_for_scatter, ndf_xy_to_gameplay_m
from .size_batch import _action_short_from_taction, _iter_taction_call_objects

_log = get_fx_logger("radius_falloff")

RADIUS_FALLOFF_SAMPLES = 11

# Stable salt so batch, preview, and file output agree on which bursts pass independent thinning.
_SPATIAL_INDEP_THIN_SALT = b'fx_editor_call_spatial_independent_thin_v1'

# One-time 64-bit seed from salt (SHA-256 once at import, not per burst).
_THIN_MIX_SEED64 = int.from_bytes(
    hashlib.sha256(_SPATIAL_INDEP_THIN_SALT).digest()[:8],
    'big',
)


def _mix64_to_u01(z: int) -> float:
    """Map 64-bit mixed value to ``[0, 1)``."""
    return (z & 0xFFFFFFFFFFFFFFFF) / float(2**64)


def _splitmix64_mix(x: int) -> int:
    """64-bit mixing function (SplitMix64-style finalizer); deterministic across platforms."""
    x = (x + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
    z = x
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9 & 0xFFFFFFFFFFFFFFFF
    z = (z ^ (z >> 27)) * 0x94D049BB133111EB & 0xFFFFFFFFFFFFFFFF
    return (z ^ (z >> 31)) & 0xFFFFFFFFFFFFFFFF


def _det_uniform01_for_burst_index(i: int) -> float:
    """Reproducible [0, 1) from burst index (same across runs and machines).

    Uses fast 64-bit mixing (no per-burst SHA-256). Changing :data:`_SPATIAL_INDEP_THIN_SALT`
    or this function intentionally changes which bursts pass thinning.
    """
    x = (_THIN_MIX_SEED64 ^ (i * 0xD6E8FEB866772FD1)) & 0xFFFFFFFFFFFFFFFF
    return _mix64_to_u01(_splitmix64_mix(x))


def burst_indices_kept_by_spatial_independent_thinning(mults: Sequence[float]) -> Set[int]:
    """Keep each burst *independently* with probability ``mults[i]`` (curve value in ``[0, 1]``).

    Uses deterministic ``u_i`` in ``[0,1)`` per burst index so layout order matches batch output.
    Expected kept count is ``sum(mults)`` (not necessarily an integer match). Surviving burst density
    in radius follows the falloff curve in expectation instead of a hard ``keep K largest weights`` disk.
    """
    kept: Set[int] = set()
    for i, p in enumerate(mults):
        p = max(0.0, min(1.0, float(p)))
        if p <= 0.0:
            continue
        if p >= 1.0 - 1e-15:
            kept.add(i)
            continue
        u = _det_uniform01_for_burst_index(i)
        if u < p:
            kept.add(i)
    return kept


def burst_indices_removed_by_spatial_trim(mults: Sequence[float]) -> Set[int]:
    """Indices removed by Call spatial thinning (complement of :func:`burst_indices_kept_by_spatial_independent_thinning`)."""
    n = len(mults)
    if n == 0:
        return set()
    kept = burst_indices_kept_by_spatial_independent_thinning(mults)
    return {i for i in range(n) if i not in kept}


def align_radius_falloff_curve(curve: Sequence[float], n: int = RADIUS_FALLOFF_SAMPLES) -> List[float]:
    """Pad or truncate to ``n`` samples (missing points default to 100%%)."""
    if n <= 0:
        return []
    if len(curve) >= n:
        return [float(x) for x in curve[:n]]
    out = [float(x) for x in curve]
    out.extend([100.0] * (n - len(out)))
    return out


def _min_spatial_falloff_mult_from_aligned(
    aligned_by_vfx: Dict[str, List[float]],
    r_norm: float,
    restrict_to_vfx: Optional[Sequence[str]],
) -> float:
    """Same semantics as :func:`min_spatial_falloff_mult_at_r_norm` but uses pre-aligned curves."""
    if not aligned_by_vfx:
        return 1.0
    if restrict_to_vfx is not None:
        keys = [k for k in restrict_to_vfx if k in aligned_by_vfx]
        if not keys:
            return 1.0
    else:
        keys = list(aligned_by_vfx.keys())
    m = 1.0
    for k in keys:
        ac = aligned_by_vfx[k]
        pct = interp_radius_falloff_pct(ac, r_norm)
        m = min(m, max(0.0, min(1.0, pct / 100.0)))
    return m


def min_spatial_falloff_mult_at_r_norm(
    falloff_by_vfx: Dict[str, List[float]],
    r_norm: float,
    *,
    restrict_to_vfx: Optional[Sequence[str]] = None,
) -> float:
    """Minimum of interpolated %% across VFX curves at ``r_norm``.

    **Call spatial** thinning uses one keep-probability per burst: the minimum of each curve’s
    interpolated ``%% / 100`` at ``r_norm`` for ``TActionCall`` VFX names that apply to **that**
    burst (``restrict_to_vfx``). If none of those names appear in ``falloff_by_vfx``, returns
    ``1.0`` (no curve-driven penalty for that burst).

    ``r_norm`` is distance from scatter center / target batch radius (m), clamped to ``[0, 1]``;
    curve samples are 11 points along ``0 … 1`` (center → edge of target radius).

    If ``restrict_to_vfx`` is ``None``, the minimum is taken across **all** keys in
    ``falloff_by_vfx`` (legacy behavior for callers without per-burst VFX lists).
    """
    if not falloff_by_vfx:
        return 1.0
    aligned_by_vfx = {k: align_radius_falloff_curve(v) for k, v in falloff_by_vfx.items()}
    return _min_spatial_falloff_mult_from_aligned(aligned_by_vfx, r_norm, restrict_to_vfx)


def burst_r_norms_for_spatial_falloff(
    parsed_root: ndf.model.List,
    target_radius_m: float,
    ref_m: float,
    anchor_r: float,
    burst_gameplay_xy_m: Optional[Sequence[Tuple[float, float]]] = None,
) -> List[float]:
    """One ``r_norm`` per ``TSimultaneousAction`` row (same order as :func:`list_tsimultaneous_action_rows`)."""
    from .scatter_timeline import _list_row_child_v

    actions = find_actions_list(parsed_root)
    if actions is None:
        return []
    burst_rows = list_tsimultaneous_action_rows(actions)
    tr = max(float(target_radius_m), 1e-9)
    use_burst_xy = (
        burst_gameplay_xy_m is not None
        and len(burst_gameplay_xy_m) == len(burst_rows)
    )
    if burst_gameplay_xy_m is not None and len(burst_gameplay_xy_m) != len(burst_rows):
        _log.warning(
            'burst_r_norms: burst_gameplay_xy_m length %d != TSimultaneousAction count %d; '
            'using NDF positions for r_norm',
            len(burst_gameplay_xy_m),
            len(burst_rows),
        )
    out: List[float] = []
    for burst_i, burst_row in enumerate(burst_rows):
        sim = _list_row_child_v(burst_row)
        if sim is None or not isinstance(sim, ndf.model.Object) or sim.type != 'TSimultaneousAction':
            out.append(0.0)
            continue
        if use_burst_xy:
            gx, gy = burst_gameplay_xy_m[burst_i]
            r = math.hypot(float(gx), float(gy))
            out.append(max(0.0, min(1.0, r / tr)))
        else:
            out.append(_r_norm_from_simultaneous(sim, target_radius_m, ref_m, anchor_r))
    return out


def burst_row_vfx_short_names_for_spatial_falloff(parsed_root: ndf.model.List) -> List[List[str]]:
    """One list of unique VFX short names per ``TSimultaneousAction`` row (same order as ``r_norm``).

    Used for Call spatial trim so each burst’s weight is the minimum of curves only for VFX
    that appear in that burst, not every VFX in the effect.
    """
    from .scatter_timeline import _list_row_child_v
    from .size_batch import _action_short_from_taction, _iter_taction_call_objects

    actions = find_actions_list(parsed_root)
    if actions is None:
        return []
    burst_rows = list_tsimultaneous_action_rows(actions)
    out: List[List[str]] = []
    for br in burst_rows:
        sim = _list_row_child_v(br)
        if sim is None or not isinstance(sim, ndf.model.Object) or sim.type != 'TSimultaneousAction':
            out.append([])
            continue
        seen: Set[str] = set()
        names: List[str] = []
        for tact in _iter_taction_call_objects(sim):
            v = _action_short_from_taction(tact)
            if v and v not in seen:
                seen.add(v)
                names.append(v)
        out.append(names)
    return out


def ensure_spatial_trim_keeps_one_burst_per_vfx(
    parsed_root: ndf.model.List,
    removed_indices: Set[int],
) -> Set[int]:
    """Shrink ``removed_indices`` so every VFX short name still appears in at least one kept burst.

    Call spatial thinning can drop every burst that contained a given VFX; this un-removes the
    smallest-index removed burst that carries each uncovered VFX until all are covered.
    """
    burst_vfx = burst_row_vfx_short_names_for_spatial_falloff(parsed_root)
    n = len(burst_vfx)
    if n == 0:
        return set(removed_indices)
    removed = set(removed_indices)
    kept = {i for i in range(n) if i not in removed}
    all_vfx: Set[str] = set()
    for names in burst_vfx:
        all_vfx.update(names)

    def vfx_covered(vfx: str) -> bool:
        for i in kept:
            if vfx in burst_vfx[i]:
                return True
        return False

    for vfx in sorted(all_vfx):
        if vfx_covered(vfx):
            continue
        for i in sorted(removed):
            if vfx in burst_vfx[i]:
                removed.discard(i)
                kept.add(i)
                break
    return removed


def compute_call_spatial_burst_mults(
    parsed_root: ndf.model.List,
    falloff_by_vfx: Dict[str, List[float]],
    target_radius_m: float,
    ref_m: float,
    anchor_r: float,
    burst_gameplay_xy_m: Optional[Sequence[Tuple[float, float]]] = None,
) -> List[float]:
    """One spatial weight per ``TSimultaneousAction`` row; **single source of truth** for Call spatial trim.

    Same inputs and ordering as the spatial branch of :func:`scale_effect_calls` (including
    ``burst_gameplay_xy_m`` vs NDF-derived ``r_norm``). Use with
    :func:`burst_indices_removed_by_spatial_trim` / :func:`burst_indices_kept_by_spatial_independent_thinning`.
    """
    from .scatter_timeline import _list_row_child_v

    actions = find_actions_list(parsed_root)
    if actions is None:
        return []
    burst_rows = list_tsimultaneous_action_rows(actions)
    tr = max(float(target_radius_m), 1e-9)
    use_burst_xy = (
        burst_gameplay_xy_m is not None
        and len(burst_gameplay_xy_m) == len(burst_rows)
    )
    if burst_gameplay_xy_m is not None and len(burst_gameplay_xy_m) != len(burst_rows):
        _log.warning(
            'compute_call_spatial_burst_mults: burst_gameplay_xy_m length %d != TSimultaneousAction count %d; '
            'using NDF positions for r_norm',
            len(burst_gameplay_xy_m),
            len(burst_rows),
        )
    aligned_by_vfx = {k: align_radius_falloff_curve(v) for k, v in falloff_by_vfx.items()}
    out: List[float] = []
    for burst_i, burst_row in enumerate(burst_rows):
        sim = _list_row_child_v(burst_row)
        if sim is None or not isinstance(sim, ndf.model.Object) or sim.type != 'TSimultaneousAction':
            out.append(
                _min_spatial_falloff_mult_from_aligned(aligned_by_vfx, 0.0, []),
            )
            continue
        if use_burst_xy:
            gx, gy = burst_gameplay_xy_m[burst_i]
            r = math.hypot(float(gx), float(gy))
            r_norm = max(0.0, min(1.0, r / tr))
        else:
            r_norm = _r_norm_from_simultaneous(sim, target_radius_m, ref_m, anchor_r)
        seen: Set[str] = set()
        vfx_names: List[str] = []
        for tact in _iter_taction_call_objects(sim):
            v = _action_short_from_taction(tact)
            if v and v not in seen:
                seen.add(v)
                vfx_names.append(v)
        out.append(
            _min_spatial_falloff_mult_from_aligned(aligned_by_vfx, r_norm, vfx_names),
        )
    return out


def compute_call_spatial_trim_removed_indices(
    parsed_root: ndf.model.List,
    falloff_by_vfx: Dict[str, List[float]],
    target_radius_m: float,
    ref_m: float,
    anchor_r: float,
    burst_gameplay_xy_m: Optional[Sequence[Tuple[float, float]]] = None,
    *,
    layout_burst_count: Optional[int] = None,
    mults: Optional[Sequence[float]] = None,
) -> Optional[Set[int]]:
    """Burst indices removed by Call spatial trim; ``None`` if ``layout_burst_count`` does not match parsed tree.

    Pass ``mults`` when :func:`compute_call_spatial_burst_mults` was already run for this tree to avoid duplicate work.
    """
    if mults is None:
        mults = compute_call_spatial_burst_mults(
            parsed_root,
            falloff_by_vfx,
            target_radius_m,
            ref_m,
            anchor_r,
            burst_gameplay_xy_m,
        )
    else:
        mults = list(mults)
    if layout_burst_count is not None and len(mults) != layout_burst_count:
        _log.warning(
            'compute_call_spatial_trim_removed_indices: mults length %d != layout_burst_count %d; '
            'skip trim preview',
            len(mults),
            layout_burst_count,
        )
        return None
    raw = burst_indices_removed_by_spatial_trim(mults)
    return ensure_spatial_trim_keeps_one_burst_per_vfx(parsed_root, raw)


def interp_radius_falloff_pct(curve: Sequence[float], r_norm: float) -> float:
    """Linear interpolation: ``r_norm`` in ``[0, 1]`` (center → edge of target radius)."""
    n = len(curve)
    if n == 0:
        return 100.0
    if n == 1:
        return float(curve[0])
    r = max(0.0, min(1.0, float(r_norm)))
    x = r * (n - 1)
    i = int(math.floor(x))
    i = min(i, n - 2)
    t = x - i
    a = float(curve[i])
    b = float(curve[min(i + 1, n - 1)])
    return a + t * (b - a)


def _r_norm_from_simultaneous(
    sim: ndf.model.Object,
    target_radius_m: float,
    ref_m: float,
    anchor_r: float,
) -> float:
    """``hypot(x,y) / target_radius_m`` clamped to ``[0, 1]``; center if position cannot be read."""
    tr = max(float(target_radius_m), 1e-9)
    ndf_pt = extract_ndf_xy_from_simultaneous_for_scatter(sim)
    if ndf_pt is None:
        return 0.0
    gx, gy = ndf_xy_to_gameplay_m(ndf_pt[0], ndf_pt[1], ref_m, anchor_r)
    r = math.hypot(float(gx), float(gy))
    return max(0.0, min(1.0, r / tr))


def burst_gameplay_xy_m_from_parsed_root(
    parsed_root: ndf.model.List,
    ref_m: float,
    anchor_r: float,
) -> List[Tuple[float, float]]:
    """One gameplay (x, y) per ``TSimultaneousAction`` row, in ``Actions`` order.

    Call :func:`scale_effect_calls` with spatial burst trimming first when needed; then pass this
    result into :func:`taction_radius_falloff_multipliers` for the **param** pass so
    ``burst_gameplay_xy_m`` length matches ``list_tsimultaneous_action_rows`` (layout lists stay
    long after trim).
    """
    from .scatter_timeline import _list_row_child_v

    actions = find_actions_list(parsed_root)
    if actions is None:
        return []
    out: List[Tuple[float, float]] = []
    for br in list_tsimultaneous_action_rows(actions):
        sim = _list_row_child_v(br)
        if sim is None or not isinstance(sim, ndf.model.Object) or sim.type != 'TSimultaneousAction':
            out.append((0.0, 0.0))
            continue
        ndf_pt = extract_ndf_xy_from_simultaneous_for_scatter(sim)
        if ndf_pt is None:
            out.append((0.0, 0.0))
            continue
        gx, gy = ndf_xy_to_gameplay_m(ndf_pt[0], ndf_pt[1], ref_m, anchor_r)
        out.append((float(gx), float(gy)))
    return out


def taction_radius_falloff_multipliers(
    parsed_root: ndf.model.List,
    target_radius_m: float,
    falloff_by_vfx: Dict[str, List[float]],
    ref_m: float,
    anchor_r: float,
    *,
    burst_gameplay_xy_m: Optional[Sequence[Tuple[float, float]]] = None,
    log_label: str = 'spatial',
) -> Dict[int, float]:
    """Map ``id(TActionCall)`` → multiplier in ``[0, 1]`` (100%% curve = 1.0).

    Each ``TSimultaneousAction`` row is one burst; ``falloff_by_vfx`` maps VFX short name → curve
    samples over normalized radius ``0 … 1``. VFX names missing from the map get multiplier ``1.0``
    (no spatial falloff for that call).

    When ``burst_gameplay_xy_m`` is provided with the same length as the number of
    ``TSimultaneousAction`` rows (cluster emit order), normalized radius uses those gameplay
    coordinates instead of re-parsing Mobile / parPosition from the NDF tree (avoids printer /
    regex mismatch that would treat every burst as r=0).

    ``log_label`` prefixes log lines (e.g. ``param`` vs ``call``) so two passes in the same run are
    not confused.
    """
    tag = f'[{log_label}]'
    if not falloff_by_vfx:
        _log.debug('%s taction_radius_falloff: empty falloff_by_vfx, returning no multipliers', tag)
        return {}
    actions = find_actions_list(parsed_root)
    if actions is None:
        _log.debug('%s taction_radius_falloff: no Actions list, returning no multipliers', tag)
        return {}
    out: Dict[int, float] = {}
    burst_rows = list_tsimultaneous_action_rows(actions)
    tr = max(float(target_radius_m), 1e-9)
    use_burst_xy = (
        burst_gameplay_xy_m is not None
        and len(burst_gameplay_xy_m) == len(burst_rows)
    )
    if burst_gameplay_xy_m is not None and len(burst_gameplay_xy_m) != len(burst_rows):
        _log.warning(
            '%s taction_radius_falloff: burst_gameplay_xy_m length %d != TSimultaneousAction count %d; '
            'using NDF positions for r_norm',
            tag,
            len(burst_gameplay_xy_m),
            len(burst_rows),
        )
    _log.debug(
        '%s taction_radius_falloff: vfx_curves=%d target_r_m=%.6g bursts=%d use_burst_xy=%s',
        tag,
        len(falloff_by_vfx),
        tr,
        len(burst_rows),
        use_burst_xy,
    )
    from .scatter_timeline import _list_row_child_v

    aligned_by_vfx = {k: align_radius_falloff_curve(v) for k, v in falloff_by_vfx.items()}
    _burst_debug_cap = 8
    for burst_i, burst_row in enumerate(burst_rows):
        sim = _list_row_child_v(burst_row)
        if sim is None or not isinstance(sim, ndf.model.Object) or sim.type != 'TSimultaneousAction':
            continue
        if use_burst_xy:
            gx, gy = burst_gameplay_xy_m[burst_i]
            r = math.hypot(float(gx), float(gy))
            r_norm = max(0.0, min(1.0, r / tr))
        else:
            r_norm = _r_norm_from_simultaneous(sim, target_radius_m, ref_m, anchor_r)
        burst_pairs: List[Tuple[str, float]] = []
        for tact in _iter_taction_call_objects(sim):
            vfx = _action_short_from_taction(tact)
            if not vfx:
                continue
            curve = falloff_by_vfx.get(vfx)
            if curve is None:
                out[id(tact)] = 1.0
                burst_pairs.append((vfx, 1.0))
            else:
                ac = aligned_by_vfx[vfx]
                pct = interp_radius_falloff_pct(ac, r_norm)
                mult = max(0.0, min(1.0, pct / 100.0))
                out[id(tact)] = mult
                burst_pairs.append((vfx, mult))
        if burst_i < _burst_debug_cap and burst_pairs:
            _log.debug(
                '%s taction_radius_falloff burst %d r_norm=%.4f tactions=%s',
                tag,
                burst_i,
                r_norm,
                burst_pairs,
            )
    if out:
        vals = list(out.values())
        _log.info(
            '%s taction_radius_falloff: n_tactions=%d mult min=%.4f max=%.4f '
            '(target_r_m=%.6g use_burst_xy=%s)',
            tag,
            len(out),
            min(vals),
            max(vals),
            tr,
            use_burst_xy,
        )
    return out


_BIAS_MIX_SEED64 = int.from_bytes(
    hashlib.sha256(b'fx_editor_call_falloff_position_bias_v1').digest()[:8],
    'big',
)


def _det_uniform01_for_bias_slot(slot: int) -> float:
    x = (_BIAS_MIX_SEED64 ^ (int(slot) * 0xC6BC279692B5C323)) & 0xFFFFFFFFFFFFFFFF
    return _mix64_to_u01(_splitmix64_mix(x))


def _sample_r_norm_from_falloff_marginal(
    aligned_by_vfx: Dict[str, List[float]],
    restrict_to_vfx: Optional[Sequence[str]],
    u: float,
    *,
    n_steps: int = 129,
) -> float:
    """Inverse-CDF sample of ``r_norm`` in ``[0, 1]`` with marginal density ``∝ w(r) * r`` on the disk."""
    n = max(8, int(n_steps))
    r_grid = [j / (n - 1) for j in range(n)]
    seg_mass: List[float] = []
    for j in range(n - 1):
        r0, r1 = r_grid[j], r_grid[j + 1]
        dr = r1 - r0
        w0 = _min_spatial_falloff_mult_from_aligned(aligned_by_vfx, r0, restrict_to_vfx)
        w1 = _min_spatial_falloff_mult_from_aligned(aligned_by_vfx, r1, restrict_to_vfx)
        w0 = max(1e-15, float(w0))
        w1 = max(1e-15, float(w1))
        seg_mass.append(0.5 * (r0 * w0 + r1 * w1) * dr)
    z = sum(seg_mass)
    if z < 1e-30:
        return max(0.0, min(1.0, float(u)))
    uu = max(0.0, min(1.0, float(u))) * z
    acc = 0.0
    for j, m in enumerate(seg_mass):
        if acc + m >= uu - 1e-15:
            if m < 1e-30:
                return r_grid[j]
            t = (uu - acc) / m
            return r_grid[j] + t * (r_grid[j + 1] - r_grid[j])
        acc += m
    return 1.0


def apply_call_falloff_burst_position_bias(
    parsed_root: ndf.model.List,
    falloff_by_vfx: Dict[str, List[float]],
    target_radius_m: float,
    ref_m: float,
    anchor_r: float,
    *,
    dry_run: bool = False,
) -> int:
    """Reposition every ``TSimultaneousAction`` burst so radial distribution follows Call falloff curves.

    Does **not** remove bursts or ``TActionCall`` rows. For each burst, samples a new radius using the
    same per-burst VFX restriction as Call spatial trim (minimum curve at ``r_norm``), with marginal
    density ``∝ w(r) * r`` on the effect disk, and uniform angle. Deterministic per burst index.

    Returns the number of bursts whose anchor was successfully updated (0 if ``dry_run``).
    """
    if not falloff_by_vfx:
        return 0
    actions = find_actions_list(parsed_root)
    if actions is None:
        return 0
    burst_rows = list_tsimultaneous_action_rows(actions)
    if not burst_rows:
        return 0
    aligned_by_vfx = {k: align_radius_falloff_curve(v) for k, v in falloff_by_vfx.items()}
    burst_vfx = burst_row_vfx_short_names_for_spatial_falloff(parsed_root)
    tr = max(float(target_radius_m), 1e-9)
    n_ok = 0
    for i, burst_row in enumerate(burst_rows):
        sim = burst_row.v
        if not isinstance(sim, ndf.model.Object) or sim.type != 'TSimultaneousAction':
            continue
        names = burst_vfx[i] if i < len(burst_vfx) else []
        restrict: Optional[List[str]] = names if names else None
        u_r = _det_uniform01_for_bias_slot(i * 2 + 11)
        u_th = _det_uniform01_for_bias_slot(i * 2 + 104729)
        r_norm = _sample_r_norm_from_falloff_marginal(aligned_by_vfx, restrict, u_r)
        r_game = r_norm * tr
        theta = 2.0 * math.pi * u_th
        gx = float(r_game * math.cos(theta))
        gy = float(r_game * math.sin(theta))
        gx = float(int(round(gx)))
        gy = float(int(round(gy)))
        h = math.hypot(gx, gy)
        if h > tr and h > 1e-9:
            gx = float(int(round(gx * tr / h)))
            gy = float(int(round(gy * tr / h)))
        if dry_run:
            continue
        if set_simultaneous_burst_gameplay_position_m(sim, gx, gy, ref_m, anchor_r):
            n_ok += 1
    return n_ok
