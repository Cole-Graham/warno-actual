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
from .scatter_layout_presets import gameplay_hex_with_source_residual
from .scatter_model import ScatterBurst, ScatterProject
from .scatter_timing import (
    count_tsimultaneous_in_actions,
    infer_anchor_bounds_from_parsed,
    redistribute_anchor_waits,
)
from .fx_logging import get_fx_logger
from .scatter_analyze import vfx_effect_group_burst_counts
from .size_batch import SizeChange, scale_size_params

_log_pipe = get_fx_logger('scatter_pipeline')

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
    include_declaration_params: bool = True,
    scale_size: bool = True,
    scale_count: bool = True,
    effect_named_flags: Any = None,
    dry_run: bool = False,
    pre_emit_roundtrip: bool = True,
    post_emit_roundtrip: bool = True,
) -> ClusterEmitScaleResult:
    """Single path for cluster preview, scatter panel summary, and :func:`write_cluster_variation_file`.

    Order: optional pre-roundtrip → emit layout → optional post-roundtrip → burst_xy → spatial-trim
    preview indices (for UI) → ``vfx_effect_group_burst_counts`` → :func:`scale_effect_calls` →
    param falloff multipliers → :func:`scale_size_params`.
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
    if call_radius_falloff_by_vfx is not None and len(call_radius_falloff_by_vfx) > 0:
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
        actions = find_actions_list(work)
        n_sim = len(list_tsimultaneous_action_rows(actions)) if actions is not None else 0
        if len(burst_xy) == n_sim:
            param_burst_xy = burst_xy
        else:
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
            continue
        ndf_pt = extract_ndf_xy_from_simultaneous_for_scatter(sim)
        if ndf_pt is None:
            continue
        gx, gy = ndf_xy_to_gameplay_m(ndf_pt[0], ndf_pt[1], ref_m, anchor_r)
        source_xy.append((float(int(round(gx))), float(int(round(gy)))))
    positions = gameplay_hex_with_source_residual(
        n_target,
        target_r,
        source_r,
        source_xy,
        jitter_salt=source_ndf_path,
    )
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
