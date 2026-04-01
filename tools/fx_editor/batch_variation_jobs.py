"""Background workers for Batch Size preview / create — no Tk (runs on worker threads)."""

from __future__ import annotations

import os
import queue
import traceback
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from src import ndf

from .call_scale import format_call_qty_report_line
from .radius_falloff import taction_radius_falloff_multipliers
from .scatter_analyze import merge_effect_qty_pct_for_target_radius, merge_effect_radius_falloff_curves
from .scatter_variation import build_cluster_scatter_project, preview_cluster_variation, write_cluster_variation_file
from .size_batch import process_file, render_variation_filename, write_scaled_copy


def _param_change_line(changes: List[Any]) -> str:
    return f'{len(changes)} param change(s)'


def _call_change_line(
    call_changes: List[Any],
    *,
    effect_call_scale_pct: Optional[Dict[str, float]] = None,
    scale_factor: float = 1.0,
    vfx_burst_denoms: Optional[Dict[str, int]] = None,
) -> str:
    s = format_call_qty_report_line(
        call_changes,
        effect_call_scale_pct=effect_call_scale_pct,
        scale_factor=scale_factor,
        vfx_burst_denoms=vfx_burst_denoms,
    )
    return f'  |  {s}' if s else ''


def _qty_pct_for_target(
    snapshot: Dict[str, Any],
    target_m: float,
    targets: List[float],
    *,
    param: bool,
) -> Optional[Dict[str, float]]:
    groups = snapshot.get('cached_effect_groups') or []
    if not groups:
        return None
    curve = snapshot['param_qty_curve'] if param else snapshot['call_qty_curve']
    return merge_effect_qty_pct_for_target_radius(groups, curve, target_m, targets)


def _radius_falloff_for_vfx(snapshot: Dict[str, Any], *, param: bool) -> Optional[Dict[str, List[float]]]:
    groups = snapshot.get('cached_effect_groups') or []
    if not groups:
        return None
    curve = snapshot['param_radius_curve'] if param else snapshot['call_radius_curve']
    return merge_effect_radius_falloff_curves(groups, curve)


def _preview_parallel_workers_cap(snapshot: Dict[str, Any]) -> int:
    """``FX_EDITOR_PREVIEW_WORKERS`` env (default 1); snapshot key ``preview_parallel_workers`` overrides."""
    try:
        w = int(snapshot.get('preview_parallel_workers', os.environ.get('FX_EDITOR_PREVIEW_WORKERS', '1')))
    except (TypeError, ValueError):
        w = 1
    return max(1, min(w, 16))


def _cluster_preview_job(job: Dict[str, Any]) -> Dict[str, Any]:
    """Run :func:`preview_cluster_variation` in a worker process (picklable ``job`` dict)."""
    import sys
    import traceback
    from pathlib import Path

    root = Path(__file__).resolve().parents[2]
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    from tools.fx_editor.scatter_variation import preview_cluster_variation

    try:
        return preview_cluster_variation(
            Path(job['path']),
            float(job['source_m']),
            float(job['target_m']),
            float(job['ref_m']),
            float(job['anchor_r']),
            float(job['wait_max']),
            include_declaration_params=bool(job['include_declaration_params']),
            scale_size=bool(job['scale_size']),
            scale_count=bool(job['scale_count']),
            effect_named_flags=job.get('effect_named_flags'),
            effect_count_scale_pct=job.get('effect_count_scale_pct'),
            effect_call_scale_pct=job.get('effect_call_scale_pct'),
            effect_call_batch_scale_min=job.get('effect_call_batch_scale_min'),
            effect_call_batch_scale_max=job.get('effect_call_batch_scale_max'),
            param_radius_falloff_by_vfx=job.get('param_radius_falloff_by_vfx'),
            call_radius_falloff_by_vfx=job.get('call_radius_falloff_by_vfx'),
            pre_emit_roundtrip=bool(job.get('pre_emit_roundtrip', False)),
            post_emit_roundtrip=bool(job.get('post_emit_roundtrip', False)),
        )
    except Exception as exc:
        return {'error': str(exc), 'traceback': traceback.format_exc()}


def _cluster_preview_job_indexed(pair: Tuple[int, Dict[str, Any]]) -> Tuple[int, Dict[str, Any]]:
    """Process-pool wrapper so :func:`as_completed` can report progress after each job."""
    idx, job = pair
    return idx, _cluster_preview_job(job)


def preview_variations_worker(snapshot: Dict[str, Any], q: queue.Queue) -> None:
    """Compute preview; send ``('log', str)``, ``('progress', i, n)``, ``('preview', spec)``, ``('scatter_tab', ...)``, ``('done', payload)``."""
    preview_specs: List[Dict[str, Any]] = []
    scatter_tabs: List[Tuple[str, Any, str, float]] = []
    total_out = 0
    try:
        selected_files: List[Path] = snapshot['selected_files']
        targets: List[float] = snapshot['targets']
        source_m = snapshot['source_m']
        template = snapshot['template']
        rootname = snapshot['rootname']
        out_root: Path = snapshot['out_root']
        bkw = snapshot['bkw']
        ref_m = snapshot['ref_m']
        anchor_r = snapshot['anchor_r']
        wait_max = snapshot['wait_max']
        geom = snapshot['geom']
        total_steps = max(len(selected_files) * len(targets), 1)
        step = 0
        pw = _preview_parallel_workers_cap(snapshot)
        use_parallel_cluster = geom == 'cluster' and pw > 1 and len(selected_files) * len(targets) > 1

        if use_parallel_cluster:
            jobs: List[Dict[str, Any]] = []
            metas: List[Tuple[Any, ...]] = []
            for file_path in selected_files:
                stem = file_path.stem
                for target_m in targets:
                    pct = (target_m / source_m) * 100.0
                    ecp = _qty_pct_for_target(snapshot, target_m, targets, param=True)
                    ecall = _qty_pct_for_target(snapshot, target_m, targets, param=False)
                    param_rf = _radius_falloff_for_vfx(snapshot, param=True)
                    call_rf = _radius_falloff_for_vfx(snapshot, param=False)
                    name = render_variation_filename(template, rootname, target_m, stem)
                    dest = out_root / name
                    exists_note = ''
                    if dest.exists() and dest.resolve() != file_path.resolve():
                        exists_note = '  [destination exists]'
                    scale_factor = target_m / source_m
                    jobs.append(
                        {
                            'path': str(file_path.resolve()),
                            'source_m': source_m,
                            'target_m': target_m,
                            'ref_m': ref_m,
                            'anchor_r': anchor_r,
                            'wait_max': wait_max,
                            'include_declaration_params': bkw['include_declaration_params'],
                            'scale_size': bkw['scale_size'],
                            'scale_count': bkw['scale_count'],
                            'effect_named_flags': bkw['effect_named_flags'],
                            'effect_count_scale_pct': ecp,
                            'effect_call_scale_pct': ecall,
                            'effect_call_batch_scale_min': bkw.get('effect_call_batch_scale_min'),
                            'effect_call_batch_scale_max': bkw.get('effect_call_batch_scale_max'),
                            'param_radius_falloff_by_vfx': param_rf,
                            'call_radius_falloff_by_vfx': call_rf,
                            'pre_emit_roundtrip': False,
                            'post_emit_roundtrip': False,
                        },
                    )
                    metas.append(
                        (file_path, stem, target_m, pct, ecp, ecall, name, dest, exists_note, scale_factor),
                    )
            with ProcessPoolExecutor(max_workers=pw) as ex:
                results: List[Optional[Dict[str, Any]]] = [None] * len(jobs)
                futures = [
                    ex.submit(_cluster_preview_job_indexed, (i, j)) for i, j in enumerate(jobs)
                ]
                done_count = 0
                for fut in as_completed(futures):
                    idx, stats = fut.result()
                    results[idx] = stats
                    done_count += 1
                    q.put(('progress', done_count, total_steps))
            for meta, stats in zip(metas, results):
                file_path, stem, target_m, pct, ecp, ecall, name, dest, exists_note, scale_factor = meta
                assert stats is not None
                if stats.get('error'):
                    q.put(('log', f'✗ {file_path.name} @ {target_m:g} m: {stats["error"]}'))
                    total_out += 1
                else:
                    n0 = stats.get('n0', 0)
                    n_tgt = stats.get('n_target', 0)
                    changes = stats.get('changes', [])
                    call_changes = stats.get('call_changes', [])
                    q.put(
                        (
                            'log',
                            f'✓ cluster {file_path.name}  ->  {name}  |  {target_m:g} m  |  '
                            f'N0={n0} N_target={n_tgt}  |  {scale_factor:.4f}x  |  '
                            f'{_param_change_line(changes)}'
                            f'{_call_change_line(call_changes, effect_call_scale_pct=ecall, scale_factor=scale_factor, vfx_burst_denoms=stats.get("vfx_burst_denoms"))}'
                            f'{exists_note}',
                        ),
                    )
                    proj = stats.get('project')
                    if proj is not None:
                        tab_lbl = f'{Path(name).stem} @ {target_m:g}m'
                        scatter_tabs.append((tab_lbl, proj, str(file_path.resolve()), float(target_m)))
                    total_out += 1
            q.put(('log', f'Total output files: {total_out}'))
            if preview_specs:
                q.put(('log', f'Opening {len(preview_specs)} preview window(s)…'))
            q.put(
                (
                    'done',
                    {
                        'kind': 'preview',
                        'preview_specs': preview_specs,
                        'scatter_tabs': scatter_tabs,
                        'n_preview_windows': len(preview_specs),
                    },
                ),
            )
            return

        for file_path in selected_files:
            stem = file_path.stem
            for target_m in targets:
                step += 1
                try:
                    pct = (target_m / source_m) * 100.0
                    ecp = _qty_pct_for_target(snapshot, target_m, targets, param=True)
                    ecall = _qty_pct_for_target(snapshot, target_m, targets, param=False)
                    param_rf = _radius_falloff_for_vfx(snapshot, param=True)
                    call_rf = _radius_falloff_for_vfx(snapshot, param=False)
                    name = render_variation_filename(template, rootname, target_m, stem)
                    dest = out_root / name
                    exists_note = ''
                    if dest.exists() and dest.resolve() != file_path.resolve():
                        exists_note = '  [destination exists]'
                    scale_factor = target_m / source_m
                    if geom == 'cluster':
                        stats = preview_cluster_variation(
                            file_path,
                            source_m,
                            target_m,
                            ref_m,
                            anchor_r,
                            wait_max,
                            include_declaration_params=bkw['include_declaration_params'],
                            scale_size=bkw['scale_size'],
                            scale_count=bkw['scale_count'],
                            effect_named_flags=bkw['effect_named_flags'],
                            effect_count_scale_pct=ecp,
                            effect_call_scale_pct=ecall,
                            effect_call_batch_scale_min=bkw.get('effect_call_batch_scale_min'),
                            effect_call_batch_scale_max=bkw.get('effect_call_batch_scale_max'),
                            param_radius_falloff_by_vfx=param_rf,
                            call_radius_falloff_by_vfx=call_rf,
                        )
                        if stats.get('error'):
                            q.put(('log', f'✗ {file_path.name} @ {target_m:g} m: {stats["error"]}'))
                            total_out += 1
                            continue
                        n0 = stats.get('n0', 0)
                        n_tgt = stats.get('n_target', 0)
                        changes = stats.get('changes', [])
                        call_changes = stats.get('call_changes', [])
                        q.put(
                            (
                                'log',
                                f'✓ cluster {file_path.name}  ->  {name}  |  {target_m:g} m  |  '
                                f'N0={n0} N_target={n_tgt}  |  {scale_factor:.4f}x  |  '
                                f'{_param_change_line(changes)}'
                                f'{_call_change_line(call_changes, effect_call_scale_pct=ecall, scale_factor=scale_factor, vfx_burst_denoms=stats.get("vfx_burst_denoms"))}'
                                f'{exists_note}',
                            ),
                        )
                        proj = stats.get('project')
                        if proj is not None:
                            tab_lbl = f'{Path(name).stem} @ {target_m:g}m'
                            scatter_tabs.append((tab_lbl, proj, str(file_path.resolve()), float(target_m)))
                    else:
                        stats = process_file(
                            file_path,
                            scale_factor,
                            dry_run=True,
                            **{
                                **bkw,
                                'effect_count_scale_pct': ecp,
                                'effect_call_scale_pct': ecall,
                                'param_radius_falloff_by_vfx': param_rf,
                                'call_radius_falloff_by_vfx': call_rf,
                                'target_radius_m': target_m,
                                'ref_m': ref_m,
                                'anchor_r': anchor_r,
                            },
                        )
                        if stats.get('error'):
                            q.put(('log', f'✗ {file_path.name} @ {target_m:g} m: {stats["error"]}'))
                            total_out += 1
                            continue
                        changes = stats.get('changes', [])
                        call_changes = stats.get('call_changes', [])
                        if changes or call_changes:
                            q.put(
                                (
                                    'log',
                                    f'✓ {file_path.name}  ->  {name}  |  {target_m:g} m  |  '
                                    f'{pct:.2f}% of source ({scale_factor:.4f}x)  |  '
                                    f'{_param_change_line(changes)}'
                                    f'{_call_change_line(call_changes, effect_call_scale_pct=ecall, scale_factor=scale_factor, vfx_burst_denoms=stats.get("vfx_burst_denoms"))}'
                                    f'{exists_note}',
                                ),
                            )
                            title_suffix = f'{target_m:g} m → {name}'
                            param_mults_preview: Optional[Dict[int, float]] = None
                            if param_rf is not None:
                                try:
                                    ptxt = file_path.read_text(encoding='utf-8')
                                    proot = ndf.convert(ptxt)
                                    if isinstance(proot, ndf.model.List):
                                        param_mults_preview = taction_radius_falloff_multipliers(
                                            proot,
                                            float(target_m),
                                            param_rf,
                                            float(ref_m),
                                            float(anchor_r),
                                            log_label='param',
                                        )
                                except Exception:
                                    param_mults_preview = None
                            preview_specs.append(
                                {
                                    'file_path': file_path,
                                    'scale_factor': scale_factor,
                                    'title_suffix': title_suffix,
                                    'scale_size': bkw['scale_size'],
                                    'scale_count': bkw['scale_count'],
                                    'include_declaration_params': bkw['include_declaration_params'],
                                    'effect_named_flags': bkw['effect_named_flags'],
                                    'effect_count_scale_pct': ecp,
                                    'param_radius_falloff_mult_by_taction_id': param_mults_preview,
                                },
                            )
                        else:
                            q.put(
                                (
                                    'log',
                                    f'○ {file_path.name}  ->  {name}  |  {target_m:g} m  |  '
                                    f'{pct:.2f}% of source  |  no matching scaling{exists_note}',
                                ),
                            )
                    total_out += 1
                finally:
                    q.put(('progress', step, total_steps))
        q.put(('log', f'Total output files: {total_out}'))
        if preview_specs:
            q.put(('log', f'Opening {len(preview_specs)} preview window(s)…'))
        q.put(
            (
                'done',
                {
                    'kind': 'preview',
                    'preview_specs': preview_specs,
                    'scatter_tabs': scatter_tabs,
                    'n_preview_windows': len(preview_specs),
                },
            ),
        )
    except Exception as exc:
        q.put(('log', f'✗ Preview failed: {exc}'))
        q.put(('log', traceback.format_exc()))
        q.put(('done', {'kind': 'preview', 'error': True}))


def apply_variations_worker(snapshot: Dict[str, Any], q: queue.Queue) -> None:
    """Write files; send log/progress/done messages."""
    try:
        planned: List[Tuple[Path, Path, float]] = snapshot['planned']
        overwrite = snapshot['overwrite']
        source_m = snapshot['source_m']
        targets: List[float] = snapshot['targets']
        bkw = snapshot['bkw']
        ref_m = snapshot['ref_m']
        anchor_r = snapshot['anchor_r']
        wait_max = snapshot['wait_max']
        geom = snapshot['geom']
        total_steps = max(len(planned), 1)
        step = 0
        ok = 0
        skipped = 0
        errors = 0
        for file_path, dest, target_m in planned:
            step += 1
            pending_scatter: Optional[Dict[str, Any]] = None
            try:
                scale_factor = target_m / source_m
                ecp = _qty_pct_for_target(snapshot, target_m, targets, param=True)
                ecall = _qty_pct_for_target(snapshot, target_m, targets, param=False)
                param_rf = _radius_falloff_for_vfx(snapshot, param=True)
                call_rf = _radius_falloff_for_vfx(snapshot, param=False)
                if dest.exists() and not overwrite:
                    q.put(('log', f'○ Skip (exists): {dest.name}'))
                    skipped += 1
                    continue
                if geom == 'cluster':
                    try:
                        content = file_path.read_text(encoding='utf-8')
                        parsed = ndf.convert(content)
                        if not isinstance(parsed, ndf.model.List):
                            raise ValueError('Invalid NDF root')
                        project, n0, n_target = build_cluster_scatter_project(
                            parsed,
                            source_m,
                            target_m,
                            ref_m,
                            anchor_r,
                            wait_max,
                            str(file_path),
                        )
                        stats = write_cluster_variation_file(
                            file_path,
                            dest,
                            project,
                            scale_factor,
                            include_declaration_params=bkw['include_declaration_params'],
                            scale_size=bkw['scale_size'],
                            scale_count=bkw['scale_count'],
                            effect_named_flags=bkw['effect_named_flags'],
                            effect_count_scale_pct=ecp,
                            effect_call_scale_pct=ecall,
                            effect_call_batch_scale_min=bkw.get('effect_call_batch_scale_min'),
                            effect_call_batch_scale_max=bkw.get('effect_call_batch_scale_max'),
                            param_radius_falloff_by_vfx=param_rf,
                            call_radius_falloff_by_vfx=call_rf,
                            target_radius_m=target_m,
                            ref_m=ref_m,
                            anchor_r=anchor_r,
                            parsed_root=parsed,
                        )
                    except Exception as exc:
                        q.put(('log', f'✗ {file_path.name} -> {dest.name}: {exc}'))
                        errors += 1
                        continue
                    if stats.get('error'):
                        q.put(('log', f'✗ {file_path.name} -> {dest.name}: {stats["error"]}'))
                        errors += 1
                        continue
                    changes = stats.get('changes', [])
                    call_changes = stats.get('call_changes', [])
                    project.source_ndf_path = str(dest.resolve())
                    q.put(
                        (
                            'log',
                            f'✓ {dest.name}  cluster N0={n0} N_target={n_target}  '
                            f'({scale_factor:.4f}x, {_param_change_line(changes)}'
                            f'{_call_change_line(call_changes, effect_call_scale_pct=ecall, scale_factor=scale_factor, vfx_burst_denoms=stats.get("vfx_burst_denoms"))})',
                        ),
                    )
                    pending_scatter = {'file_path': file_path, 'dest': dest, 'project': project}
                    ok += 1
                else:
                    stats = write_scaled_copy(
                        file_path,
                        dest,
                        scale_factor,
                        **{
                            **bkw,
                            'effect_count_scale_pct': ecp,
                            'effect_call_scale_pct': ecall,
                            'param_radius_falloff_by_vfx': param_rf,
                            'call_radius_falloff_by_vfx': call_rf,
                            'target_radius_m': target_m,
                            'ref_m': ref_m,
                            'anchor_r': anchor_r,
                        },
                    )
                    if stats.get('error'):
                        q.put(('log', f'✗ {file_path.name} -> {dest.name}: {stats["error"]}'))
                        errors += 1
                        continue
                    changes = stats.get('changes', [])
                    call_changes = stats.get('call_changes', [])
                    q.put(
                        (
                            'log',
                            f'✓ {dest.name}  ({scale_factor:.4f}x, {_param_change_line(changes)}'
                            f'{_call_change_line(call_changes, effect_call_scale_pct=ecall, scale_factor=scale_factor, vfx_burst_denoms=stats.get("vfx_burst_denoms"))})',
                        ),
                    )
                    ok += 1
            finally:
                q.put(('progress', step, total_steps))
            if pending_scatter is not None:
                q.put(('scatter_reload', pending_scatter))
        q.put(('log', '---'))
        q.put(('log', f'Created: {ok}  Skipped: {skipped}  Errors: {errors}'))
        q.put(('done', {'kind': 'apply', 'ok': ok, 'skipped': skipped, 'errors': errors}))
    except Exception as exc:
        q.put(('log', f'✗ Create variations failed: {exc}'))
        q.put(('log', traceback.format_exc()))
        q.put(('done', {'kind': 'apply', 'error': True, 'ok': 0, 'skipped': 0, 'errors': 0}))
