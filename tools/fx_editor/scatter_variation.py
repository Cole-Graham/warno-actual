"""Build cluster size variations by scaling TSimultaneousAction count + scatter emit + param scale."""

from __future__ import annotations

import copy
import os
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src import ndf

from .call_scale import EffectCallChange, scale_effect_calls
from .ndf_access import update_namespace
from .scatter_emit import (
    _collect_ordered_distinct_relative_float3_ndf,
    build_cluster_emit_template_indices,
    emit_scatter_into_actions,
    find_actions_list,
    format_ndf,
    list_tsimultaneous_action_rows,
    list_placeable_tsimultaneous_templates,
    round_all_twait_duration_hundredths,
)
from .scatter_extract import (
    extract_ndf_xy_from_simultaneous_for_scatter,
    ndf_xy_to_gameplay_m,
    primary_vfx_short_from_simultaneous,
)
from .radius_falloff import burst_gameplay_xy_m_from_parsed_root
from .scatter_layout_presets import gameplay_hex_with_source_residual
from .scatter_model import ScatterBurst, ScatterProject
from .scatter_timing import (
    count_tsimultaneous_in_actions,
    infer_anchor_bounds_from_parsed,
    redistribute_anchor_waits,
)
from .fx_logging import get_fx_logger
from .scatter_analyze import vfx_effect_group_burst_counts
from .size_batch import SizeChange, resolve_effect_call_geom_scale, scale_size_params

_log_pipe = get_fx_logger('scatter_pipeline')


def _align_source_xy_by_site_proximity(
    source_xy_gameplay: List[Tuple[float, float]],
    merge_radius_m: float,
) -> List[Tuple[float, float]]:
    """Merge template reference points that are within ``merge_radius_m`` (gameplay meters).

    Templates whose extracted anchors fall in the same cluster share one centroid for residual
    layout, so paired rows (e.g. Mobile + nil-Mobile composite) track the same disk offset.
    """
    if merge_radius_m <= 0 or len(source_xy_gameplay) < 2:
        return list(source_xy_gameplay)
    n = len(source_xy_gameplay)
    parent = list(range(n))

    def find(a: int) -> int:
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    r2 = float(merge_radius_m) ** 2
    for i in range(n):
        xi, yi = source_xy_gameplay[i]
        for j in range(i + 1, n):
            xj, yj = source_xy_gameplay[j]
            dx, dy = xi - xj, yi - yj
            if dx * dx + dy * dy <= r2:
                union(i, j)

    groups: Dict[int, List[int]] = {}
    for i in range(n):
        root = find(i)
        groups.setdefault(root, []).append(i)

    out = list(source_xy_gameplay)
    for _root, idxs in groups.items():
        sx = sum(source_xy_gameplay[k][0] for k in idxs) / len(idxs)
        sy = sum(source_xy_gameplay[k][1] for k in idxs) / len(idxs)
        for k in idxs:
            out[k] = (sx, sy)
    return out


def _simultaneous_has_mobile_position_factory(sim: ndf.model.Object) -> bool:
    """True if ``Mobile`` is a ``TMobileWithLocalRepereMatrixFactory`` with a ``Position`` member."""
    if sim.type != 'TSimultaneousAction':
        return False
    for m in sim:
        if m.member != 'Mobile' or not isinstance(m.v, ndf.model.Object):
            continue
        if m.v.type != 'TMobileWithLocalRepereMatrixFactory':
            continue
        for mm in m.v:
            if mm.member == 'Position':
                return True
    return False


def _chain_merge_mobile_then_singleton_nil_mobile(
    templates: List[Any],
    source_xy: List[Tuple[float, float]],
) -> Tuple[List[Tuple[float, float]], Set[Tuple[int, int]]]:
    """Align layout anchors for Mobile row + following single-site nil-Mobile composite.

    Game cluster FX (e.g. ``fx_impact_sol_HE_M270_227mm_Cluster_*.ndf``) often places
    ``Big_ground``/pairs on ``Mobile`` then a nil-``Mobile`` block whose every
    ``parPositionRelative`` is one constant. Gameplay distance between those two reference points
    can exceed ``site_merge_radius_m``, so disk layout splits them; copy the Mobile template's
    anchor onto the composite and record a merge pair for :func:`build_cluster_scatter_project`.
    """
    merged: Set[Tuple[int, int]] = set()
    if len(source_xy) != len(templates):
        return source_xy, merged
    out = list(source_xy)
    nt = len(templates)
    for j in range(nt - 1):
        sim_a = templates[j].v
        sim_b = templates[j + 1].v
        if not isinstance(sim_a, ndf.model.Object) or not isinstance(sim_b, ndf.model.Object):
            continue
        if sim_a.type != 'TSimultaneousAction' or sim_b.type != 'TSimultaneousAction':
            continue
        if not _simultaneous_has_mobile_position_factory(sim_a):
            continue
        if _simultaneous_has_mobile_position_factory(sim_b):
            continue
        if len(_collect_ordered_distinct_relative_float3_ndf(sim_b)) > 1:
            continue
        out[j + 1] = out[j]
        merged.add((j, j + 1))
    return out, merged

_CLUSTER_PROFILE = os.environ.get('FX_EDITOR_PROFILE', '').strip().lower() in ('1', 'true', 'yes')


def ndf_list_roundtrip(root: ndf.model.List) -> ndf.model.List:
    """Serialize and re-parse so the tree is safe to mutate (Row/deepcopy issues in ndf_parse).

    Used before/after scatter emit so Call/Param scaling matches preview and written files.
    """
    s = ndf.printer.string(root)
    out = ndf.convert(s)
    if not isinstance(out, ndf.model.List):
        raise TypeError('NDF round-trip did not yield a List root')
    return out


@dataclass
class ClusterEmitScaleResult:
    """After :func:`emit_scatter_into_actions` + Call scale + Param scale on the same ``work`` tree."""

    work: ndf.model.List
    call_changes: List[EffectCallChange]
    size_changes: List[SizeChange]
    vfx_burst_denoms: Dict[str, int]
    spatial_trim_removed_indices: Optional[Set[int]]


def run_cluster_emit_scale_pipeline(
    parsed: ndf.model.List,
    project: ScatterProject,
    *,
    scale_factor: float,
    target_radius_m: float,
    ref_m: float,
    anchor_r: float,
    effect_call_scale_pct: Optional[Dict[str, float]] = None,
    effect_call_batch_scale_min: Optional[float] = None,
    effect_call_batch_scale_max: Optional[float] = None,
    call_radius_falloff_by_vfx: Optional[Dict[str, List[float]]] = None,
    param_radius_falloff_by_vfx: Optional[Dict[str, List[float]]] = None,
    effect_count_scale_pct: Optional[Dict[str, float]] = None,
    consistent_call_density: bool = False,
    include_declaration_params: bool = True,
    scale_size: bool = True,
    scale_count: bool = True,
    effect_named_flags: Any = None,
    dry_run: bool = False,
    pre_emit_roundtrip: bool = True,
    post_emit_roundtrip: bool = True,
) -> ClusterEmitScaleResult:
    """Single path for cluster preview, scatter panel summary, and :func:`write_cluster_variation_file`.

    Order: optional pre-roundtrip → emit layout → optional post-roundtrip → burst_xy → (optional)
    spatial-trim preview when not ``consistent_call_density``) → ``vfx_effect_group_burst_counts`` →
    :func:`scale_effect_calls` → param falloff multipliers (from post-call NDF positions) →
    :func:`scale_size_params`.
    """
    from .radius_falloff import (
        burst_gameplay_xy_m_from_parsed_root,
        compute_call_spatial_burst_mults,
        compute_call_spatial_trim_removed_indices,
        taction_radius_falloff_multipliers,
    )

    if pre_emit_roundtrip:
        t0 = time.perf_counter()
        tree = ndf_list_roundtrip(parsed)
        if _CLUSTER_PROFILE:
            _log_pipe.debug('cluster pipeline: pre_emit ndf_list_roundtrip %s ms', (time.perf_counter() - t0) * 1000.0)
    else:
        tree = parsed
    t0 = time.perf_counter()
    emit_scatter_into_actions(project, tree)
    if _CLUSTER_PROFILE:
        _log_pipe.debug('cluster pipeline: emit_scatter_into_actions %s ms', (time.perf_counter() - t0) * 1000.0)
    if post_emit_roundtrip:
        t0 = time.perf_counter()
        work = ndf_list_roundtrip(tree)
        if _CLUSTER_PROFILE:
            _log_pipe.debug('cluster pipeline: post_emit ndf_list_roundtrip %s ms', (time.perf_counter() - t0) * 1000.0)
    else:
        work = tree

    burst_xy = [(float(b.x_gameplay_m), float(b.y_gameplay_m)) for b in project.bursts]
    spatial_trim_removed_indices: Optional[Set[int]] = None
    spatial_mults: Optional[List[float]] = None
    if (
        call_radius_falloff_by_vfx is not None
        and len(call_radius_falloff_by_vfx) > 0
        and not consistent_call_density
    ):
        spatial_mults = compute_call_spatial_burst_mults(
            work,
            call_radius_falloff_by_vfx,
            float(target_radius_m),
            float(ref_m),
            float(anchor_r),
            burst_xy,
        )
        spatial_trim_removed_indices = compute_call_spatial_trim_removed_indices(
            work,
            call_radius_falloff_by_vfx,
            float(target_radius_m),
            float(ref_m),
            float(anchor_r),
            burst_xy,
            layout_burst_count=len(project.bursts),
            mults=spatial_mults,
        )

    ec_geom = resolve_effect_call_geom_scale(
        float(scale_factor),
        consistent_call_density=consistent_call_density,
        cluster_layout=True,
    )

    t0 = time.perf_counter()
    vfx_burst_denoms = vfx_effect_group_burst_counts(work)
    if _CLUSTER_PROFILE:
        _log_pipe.debug('cluster pipeline: vfx_effect_group_burst_counts %s ms', (time.perf_counter() - t0) * 1000.0)
    t0 = time.perf_counter()
    call_changes = scale_effect_calls(
        work,
        effect_call_scale_pct,
        dry_run=dry_run,
        scale_factor=float(scale_factor),
        effect_call_geom_scale=ec_geom,
        consistent_call_density=consistent_call_density,
        effect_call_batch_scale_min=effect_call_batch_scale_min,
        effect_call_batch_scale_max=effect_call_batch_scale_max,
        call_radius_falloff_by_vfx=call_radius_falloff_by_vfx,
        target_radius_m=float(target_radius_m),
        ref_m=float(ref_m),
        anchor_r=float(anchor_r),
        burst_gameplay_xy_m=burst_xy,
        spatial_burst_mults=spatial_mults,
    )
    if _CLUSTER_PROFILE:
        _log_pipe.debug('cluster pipeline: scale_effect_calls %s ms', (time.perf_counter() - t0) * 1000.0)

    param_mults: Optional[Dict[int, float]] = None
    if param_radius_falloff_by_vfx is not None and len(param_radius_falloff_by_vfx) > 0:
        param_burst_xy = burst_gameplay_xy_m_from_parsed_root(work, float(ref_m), float(anchor_r))
        t0 = time.perf_counter()
        param_mults = taction_radius_falloff_multipliers(
            work,
            float(target_radius_m),
            param_radius_falloff_by_vfx,
            float(ref_m),
            float(anchor_r),
            burst_gameplay_xy_m=param_burst_xy,
            log_label='param',
        )
        if _CLUSTER_PROFILE:
            _log_pipe.debug('cluster pipeline: taction_radius_falloff_multipliers %s ms', (time.perf_counter() - t0) * 1000.0)

    t0 = time.perf_counter()
    size_changes = scale_size_params(
        work,
        float(scale_factor),
        dry_run=dry_run,
        allowed_names=None,
        scale_size=scale_size,
        scale_count=scale_count,
        include_declaration_params=include_declaration_params,
        effect_named_flags=effect_named_flags,
        effect_count_scale_pct=effect_count_scale_pct,
        param_radius_falloff_mult_by_taction_id=param_mults,
    )
    if _CLUSTER_PROFILE:
        _log_pipe.debug('cluster pipeline: scale_size_params %s ms', (time.perf_counter() - t0) * 1000.0)

    return ClusterEmitScaleResult(
        work=work,
        call_changes=call_changes,
        size_changes=size_changes,
        vfx_burst_denoms=vfx_burst_denoms,
        spatial_trim_removed_indices=spatial_trim_removed_indices,
    )


def build_cluster_scatter_project(
    parsed_root: ndf.model.List,
    source_m: float,
    target_m: float,
    ref_m: float,
    anchor_r: float,
    wait_max_s: float,
    source_ndf_path: str,
    *,
    site_merge_radius_m: float = 38.0,
) -> Tuple[ScatterProject, int, int]:
    """Return (project, N0, N_target).

    ``source_m`` and ``target_m`` are **effect radii** (m) from the Batch UI. Burst count scales
    with area: (target/source)². Hex gameplay disk radius is ``target_m`` for that variation.
    """
    actions = find_actions_list(parsed_root)
    if actions is None:
        raise ValueError('No Actions list in NDF.')
    n0 = count_tsimultaneous_in_actions(actions)
    if n0 == 0:
        raise ValueError('No TSimultaneousAction rows in Actions list.')
    ratio = target_m / source_m
    area_ratio = ratio * ratio
    n_target = max(1, round(n0 * area_ratio))
    t_min, _t_def_max = infer_anchor_bounds_from_parsed(parsed_root)
    t_max = max(t_min, float(wait_max_s))
    target_r = max(0.5, float(target_m))
    source_r = max(0.5, float(source_m))
    scatter_radius_m = max(1.0, target_r)
    templates = list_placeable_tsimultaneous_templates(actions)
    n_target, template_indices = build_cluster_emit_template_indices(n_target, templates)
    waits = redistribute_anchor_waits(t_min, t_max, n_target)
    source_xy: List[Tuple[float, float]] = []
    for row in templates:
        sim = row.v
        if not isinstance(sim, ndf.model.Object):
            source_xy.append((0.0, 0.0))
            continue
        ndf_pt = extract_ndf_xy_from_simultaneous_for_scatter(sim)
        if ndf_pt is None:
            source_xy.append((0.0, 0.0))
            continue
        gx, gy = ndf_xy_to_gameplay_m(ndf_pt[0], ndf_pt[1], ref_m, anchor_r)
        source_xy.append((float(int(round(gx))), float(int(round(gy)))))
    source_xy, chain_merged_pairs = _chain_merge_mobile_then_singleton_nil_mobile(
        templates,
        source_xy,
    )
    source_xy = _align_source_xy_by_site_proximity(source_xy, float(site_merge_radius_m))
    positions = list(
        gameplay_hex_with_source_residual(
            n_target,
            target_r,
            source_r,
            source_xy,
            jitter_salt=source_ndf_path,
            per_burst_template_index=template_indices,
        ),
    )
    for bi in range(1, n_target):
        ta = int(template_indices[bi - 1])
        tb = int(template_indices[bi])
        if (ta, tb) in chain_merged_pairs:
            positions[bi] = positions[bi - 1]
    bursts: List[ScatterBurst] = []
    for i in range(n_target):
        x, y = positions[i]
        ti = template_indices[i]
        sim = templates[ti].v
        pv = (
            primary_vfx_short_from_simultaneous(sim) or None
            if isinstance(sim, ndf.model.Object)
            else None
        )
        bursts.append(
            ScatterBurst(
                x,
                y,
                delay_s=waits[i],
                primary_vfx=pv,
                template_index=ti,
            ),
        )
    proj = ScatterProject(
        reference_gameplay_radius_m=ref_m,
        anchor_max_ndf_radius=anchor_r,
        bursts=bursts,
        source_ndf_path=source_ndf_path,
        wait_envelope_max_s=t_max,
        inferred_anchor_min_s=t_min,
        layout_disk_radius_m=scatter_radius_m,
        cluster_radius_scale=float(ratio),
    )
    return proj, n0, n_target


def preview_cluster_variation(
    src_path: Path,
    source_m: float,
    target_m: float,
    ref_m: float,
    anchor_r: float,
    wait_max_s: float,
    *,
    include_declaration_params: bool = True,
    scale_size: bool = True,
    scale_count: bool = True,
    effect_named_flags: Any = None,
    effect_count_scale_pct: Any = None,
    effect_call_scale_pct: Any = None,
    effect_call_batch_scale_min: Any = None,
    effect_call_batch_scale_max: Any = None,
    param_radius_falloff_by_vfx: Any = None,
    call_radius_falloff_by_vfx: Any = None,
    consistent_call_density: bool = False,
    pre_emit_roundtrip: bool = False,
    post_emit_roundtrip: bool = False,
) -> Dict[str, Any]:
    """Parse source, build cluster project, emit + dry-run param scale. No file write.

    Preview defaults to skipping :func:`ndf_list_roundtrip` (both pre- and post-emit) for speed;
    file writes use round-trips. Set ``pre_emit_roundtrip`` / ``post_emit_roundtrip`` to ``True``
    to match write-path normalization exactly.
    """
    stats: Dict[str, Any] = {
        'changes': [],
        'call_changes': [],
        'error': None,
        'n0': 0,
        'n_target': 0,
        'scale_factor': target_m / source_m,
    }
    try:
        content = src_path.read_text(encoding='utf-8')
        parsed = ndf.convert(content)
        if not isinstance(parsed, ndf.model.List):
            raise ValueError('Invalid NDF root')
        project, n0, n_target = build_cluster_scatter_project(
            parsed,
            source_m,
            target_m,
            ref_m,
            anchor_r,
            wait_max_s,
            str(src_path),
        )
        stats['n0'] = n0
        stats['n_target'] = n_target
        stats['project'] = project
        pipe = run_cluster_emit_scale_pipeline(
            parsed,
            project,
            scale_factor=float(stats['scale_factor']),
            target_radius_m=float(target_m),
            ref_m=float(ref_m),
            anchor_r=float(anchor_r),
            effect_call_scale_pct=effect_call_scale_pct,
            effect_call_batch_scale_min=effect_call_batch_scale_min,
            effect_call_batch_scale_max=effect_call_batch_scale_max,
            call_radius_falloff_by_vfx=call_radius_falloff_by_vfx,
            param_radius_falloff_by_vfx=param_radius_falloff_by_vfx,
            effect_count_scale_pct=effect_count_scale_pct,
            consistent_call_density=consistent_call_density,
            include_declaration_params=include_declaration_params,
            scale_size=scale_size,
            scale_count=scale_count,
            effect_named_flags=effect_named_flags,
            dry_run=True,
            pre_emit_roundtrip=pre_emit_roundtrip,
            post_emit_roundtrip=post_emit_roundtrip,
        )
        stats['vfx_burst_denoms'] = pipe.vfx_burst_denoms
        stats['call_changes'] = pipe.call_changes
        stats['changes'] = pipe.size_changes
        # Scatter UI / canvas use project.bursts XY; pipeline mutates pipe.work only.
        xy_sync = burst_gameplay_xy_m_from_parsed_root(
            pipe.work,
            float(ref_m),
            float(anchor_r),
        )
        if len(xy_sync) == len(project.bursts):
            for i, (gx, gy) in enumerate(xy_sync):
                project.bursts[i].x_gameplay_m = float(gx)
                project.bursts[i].y_gameplay_m = float(gy)
    except Exception as exc:
        stats['error'] = str(exc)
    return stats


def write_cluster_variation_file(
    src_path: Path,
    dest_path: Path,
    project: ScatterProject,
    scale_factor: float,
    *,
    include_declaration_params: bool = True,
    scale_size: bool = True,
    scale_count: bool = True,
    effect_named_flags: Any = None,
    effect_count_scale_pct: Any = None,
    effect_call_scale_pct: Any = None,
    effect_call_batch_scale_min: Any = None,
    effect_call_batch_scale_max: Any = None,
    param_radius_falloff_by_vfx: Any = None,
    call_radius_falloff_by_vfx: Any = None,
    consistent_call_density: bool = False,
    target_radius_m: Any = None,
    ref_m: Any = None,
    anchor_r: Any = None,
    parsed_root: Optional[ndf.model.List] = None,
) -> Dict[str, Any]:
    """Parse source, emit scatter, scale params, write dest. Returns stats dict."""
    stats: Dict[str, Any] = {
        'changes': [],
        'call_changes': [],
        'error': None,
        'project': project,
        'n_burst': len(project.bursts),
        'vfx_burst_denoms': {},
    }
    try:
        if parsed_root is None:
            content = src_path.read_text(encoding='utf-8')
            parsed = ndf.convert(content)
        else:
            parsed = copy.deepcopy(parsed_root)
        if not isinstance(parsed, ndf.model.List):
            raise ValueError('Invalid NDF root')
        tr_m = float(target_radius_m) if target_radius_m is not None else float(project.layout_disk_radius_m)
        rm = float(ref_m) if ref_m is not None else float(project.reference_gameplay_radius_m)
        ar = float(anchor_r) if anchor_r is not None else float(project.anchor_max_ndf_radius)
        pipe = run_cluster_emit_scale_pipeline(
            parsed,
            project,
            scale_factor=float(scale_factor),
            target_radius_m=tr_m,
            ref_m=rm,
            anchor_r=ar,
            effect_call_scale_pct=effect_call_scale_pct,
            effect_call_batch_scale_min=effect_call_batch_scale_min,
            effect_call_batch_scale_max=effect_call_batch_scale_max,
            call_radius_falloff_by_vfx=call_radius_falloff_by_vfx,
            param_radius_falloff_by_vfx=param_radius_falloff_by_vfx,
            effect_count_scale_pct=effect_count_scale_pct,
            consistent_call_density=consistent_call_density,
            include_declaration_params=include_declaration_params,
            scale_size=scale_size,
            scale_count=scale_count,
            effect_named_flags=effect_named_flags,
            dry_run=False,
        )
        stats['vfx_burst_denoms'] = pipe.vfx_burst_denoms
        stats['call_changes'] = pipe.call_changes
        stats['changes'] = pipe.size_changes
        round_all_twait_duration_hundredths(pipe.work)
        update_namespace(pipe.work, dest_path.stem)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.write_text(format_ndf(pipe.work), encoding='utf-8')
    except Exception as exc:
        stats['error'] = str(exc)
    return stats
