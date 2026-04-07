"""Scatter layout panel: preview game-extracted vs mod-generated cluster layouts (Batch Size tab)."""

from __future__ import annotations

import hashlib
import math
import sys
from collections import defaultdict
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk
from typing import TYPE_CHECKING, Dict, List, Optional, Set, Tuple

if TYPE_CHECKING:
    from .main import FXEditorApp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src import ndf

from .call_scale import format_call_qty_report_line
from .fx_logging import get_fx_logger
from .ndf_tree_debug import describe_ndf_tree_issues
from .size_batch import parse_target_sizes, resolve_effect_call_geom_scale
from .scatter_analyze import (
    analyze_effect_groups,
    format_effect_groups_document,
    summarize_scatter_ndf,
)
from .scatter_extract import extract_scatter_points_with_vfx, ndf_xy_to_gameplay_m
from .radius_falloff import burst_gameplay_xy_m_from_parsed_root
from .scatter_model import ScatterBurst, ScatterProject, load_scatter_calibration_yaml
from .scatter_timeline import TimelineEvent, build_timeline_events, timeline_end_time_s
from .scatter_variation import run_cluster_emit_scale_pipeline
from .ui_components import create_vertical_scrollable, install_canvas_mousewheel

_log = get_fx_logger("scatter_preview")


_VFX_PALETTE = (
    '#e6194b',
    '#3cb44b',
    '#4363d8',
    '#f58231',
    '#911eb4',
    '#46f0f0',
    '#f032e6',
    '#bcf60c',
    '#fabebe',
    '#008080',
    '#e6beff',
    '#9a6324',
    '#fffac8',
    '#800000',
    '#aaffc3',
    '#808000',
    '#ffd8b1',
    '#000075',
    '#808080',
)


def _color_for_vfx(name: Optional[str]) -> str:
    if not name:
        return '#4ec9b0'
    h = int(hashlib.md5(name.lower().encode('utf-8')).hexdigest(), 16)
    return _VFX_PALETTE[h % len(_VFX_PALETTE)]


class ScatterLayoutPanel(ttk.Frame):
    """Read-only scatter preview: VFX-colored points, timing scrubber, effect-group summary."""

    PAD = 24

    @staticmethod
    def _safe_double(var: tk.DoubleVar, default: float) -> float:
        """Spinboxes can briefly hold '' while editing; var.get() then raises TclError."""
        try:
            return float(var.get())
        except (tk.TclError, ValueError, TypeError):
            return default

    def __init__(self, parent: tk.Widget, app: 'FXEditorApp') -> None:
        super().__init__(parent)
        self.app = app
        self.ref_m, self.anchor_r = load_scatter_calibration_yaml()
        self.project = ScatterProject(
            reference_gameplay_radius_m=self.ref_m,
            anchor_max_ndf_radius=self.anchor_r,
        )
        self.preview_target_m: Optional[float] = None
        #: From :func:`run_cluster_emit_scale_pipeline` (same tree as Call spatial trim; not recomputed on canvas).
        self._spatial_trim_removed_indices: Optional[Set[int]] = None
        self._spatial_trim_removed_n: int = 0
        self._vfx_visible: Dict[str, tk.BooleanVar] = {}
        self._timeline_events: List[TimelineEvent] = []
        self._anim_t_max = 0.0
        self._anim_playing = False
        self._anim_after_id: Optional[str] = None

        self._build_ui()
        self._redraw_canvas()

    def _build_ui(self) -> None:
        top = ttk.Frame(self, padding=8)
        top.pack(fill=tk.X)
        ttk.Label(
            top,
            text=(
                f'Output preview only (read-only): load NDFs in General. Gameplay ↔ NDF: {self.ref_m:g} m ↔ '
                f'max NDF radius {self.anchor_r:.3f} (scatter_calibration.yaml). '
                f'View radius controls zoom. Cluster preview: dashed circle = target radius (r_norm=1 for falloff). '
                f'Otherwise: dashed circle = layout max extent from bursts.'
            ),
            wraplength=900,
        ).pack(anchor=tk.W)

        row1 = ttk.Frame(self, padding=4)
        row1.pack(fill=tk.X)
        ttk.Label(row1, text='View radius (m):').pack(side=tk.LEFT, padx=(0, 2))
        self.view_radius_var = tk.DoubleVar(value=150.0)
        ttk.Spinbox(
            row1,
            from_=10.0,
            to=5000.0,
            width=8,
            textvariable=self.view_radius_var,
            command=self._redraw_canvas,
        ).pack(side=tk.LEFT)
        self.preset_r_var = tk.DoubleVar(value=80.0)
        self._preset_r_label = ttk.Label(row1, text='')
        self._preset_r_label.pack(side=tk.LEFT, padx=(16, 0))
        self.preset_r_var.trace_add('write', self._on_preset_r_write)

        anim_row = ttk.LabelFrame(
            self,
            text='VFX timing preview (from loaded NDF; parallel bursts)',
            padding=4,
        )
        anim_row.pack(fill=tk.X, padx=8, pady=4)
        self.anim_time_var = tk.DoubleVar(value=0.0)
        # Fraction 0..1 of timeline; actual time = anim_time_var * _anim_t_max (see _redraw_canvas).
        self.anim_scale = ttk.Scale(
            anim_row,
            from_=0.0,
            to=1.0,
            variable=self.anim_time_var,
        )
        self.anim_scale.pack(fill=tk.X, padx=4, pady=2)
        anim_btns = ttk.Frame(anim_row)
        anim_btns.pack(fill=tk.X)
        self.anim_play_btn = ttk.Button(anim_btns, text='Play', command=self._toggle_anim_play)
        self.anim_play_btn.pack(side=tk.LEFT, padx=2)
        ttk.Label(anim_btns, text='Speed:').pack(side=tk.LEFT, padx=(12, 2))
        self.anim_speed_var = tk.DoubleVar(value=0.5)
        ttk.Spinbox(
            anim_btns,
            from_=0.25,
            to=8.0,
            increment=0.25,
            width=6,
            textvariable=self.anim_speed_var,
        ).pack(side=tk.LEFT)
        self.anim_time_var.trace_add('write', lambda *_: self._redraw_canvas())

        mid = ttk.Frame(self)
        mid.pack(fill=tk.BOTH, expand=True, padx=8, pady=4)

        legend_wrap = ttk.LabelFrame(mid, text='VFX / pattern visibility', padding=4)
        legend_wrap.pack(side=tk.LEFT, fill=tk.Y)
        legend_wrap.configure(width=220)
        legend_wrap.pack_propagate(False)
        scroll_container, leg_canvas, self.vfx_filter_inner = create_vertical_scrollable(
            legend_wrap,
            padding=4,
        )
        scroll_container.pack(fill=tk.BOTH, expand=True)
        install_canvas_mousewheel(self.winfo_toplevel(), leg_canvas, scroll_container)

        self.canvas = tk.Canvas(
            mid,
            background='#1e1e1e',
            highlightthickness=1,
        )
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(8, 0))
        self.canvas.bind('<Configure>', lambda e: self._redraw_canvas())

        self._effect_groups_labelframe = ttk.LabelFrame(mid, text='Effect groups (from loaded NDF)', padding=4)
        self._effect_groups_labelframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=8)
        right = self._effect_groups_labelframe
        self.summary_meta = ttk.Label(
            right,
            text='Open an NDF from General (Load Files) to summarize effect groups.',
            wraplength=920,
            justify=tk.LEFT,
        )
        self.summary_meta.pack(anchor=tk.W)
        sum_wrap = ttk.Frame(right)
        sum_wrap.pack(fill=tk.BOTH, expand=True)
        vsb = ttk.Scrollbar(sum_wrap, orient=tk.VERTICAL)
        self.summary_text = tk.Text(
            sum_wrap,
            height=14,
            width=52,
            wrap=tk.WORD,
            font=('Consolas', 9),
            background='#252526',
            foreground='#cccccc',
            insertbackground='#cccccc',
            relief=tk.FLAT,
            padx=10,
            pady=8,
            state=tk.DISABLED,
        )
        vsb.config(command=self.summary_text.yview)
        self.summary_text.config(yscrollcommand=vsb.set)
        self.summary_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        def _summary_wheel(ev: tk.Event) -> str:
            self.summary_text.yview_scroll(int(-1 * (ev.delta / 120)), 'units')
            return 'break'

        def _summary_wheel_linux(ev: tk.Event) -> str:
            if ev.num == 4:
                self.summary_text.yview_scroll(-1, 'units')
            elif ev.num == 5:
                self.summary_text.yview_scroll(1, 'units')
            return 'break'

        self.summary_text.bind('<MouseWheel>', _summary_wheel)
        self.summary_text.bind('<Button-4>', _summary_wheel_linux)
        self.summary_text.bind('<Button-5>', _summary_wheel_linux)

        self._rebuild_vfx_filter_ui()
        self._on_preset_r_write()

    def _on_preset_r_write(self, *_args: object) -> None:
        self._update_preset_r_label()
        self._redraw_canvas()

    def _update_preset_r_label(self) -> None:
        r_layout = self._safe_double(self.preset_r_var, 80.0)
        if self.preview_target_m is not None:
            t = float(self.preview_target_m)
            self._preset_r_label.config(
                text=(
                    f'Target radius (Call falloff r_norm=1): {t:.1f} m  |  '
                    f'Layout max extent: {r_layout:.1f} m'
                ),
            )
        else:
            self._preset_r_label.config(text=f'Gameplay disk R (m): {r_layout:.1f}')

    def effective_disk_radius_m(self) -> float:
        """Largest gameplay radius (m) for fitting the canvas view (cluster: includes target radius)."""
        pre = max(1.0, self._safe_double(self.preset_r_var, 80.0))
        if self.preview_target_m is not None:
            return max(pre, float(self.preview_target_m))
        return pre

    def _canvas_reference_radius_m(self) -> float:
        """Dashed circle in gameplay meters: target batch radius when cluster preview, else layout disk R."""
        if self.preview_target_m is not None:
            return max(1e-6, float(self.preview_target_m))
        return max(1e-6, self._safe_double(self.preset_r_var, 80.0))

    def apply_shared_view_radius(self, view_radius_m: float) -> None:
        """Set canvas view radius (m) for consistent zoom across all Scatter tabs."""
        self.view_radius_var.set(max(10.0, float(view_radius_m)))
        self._redraw_canvas()

    def _sync_preset_r_from_bursts(self) -> None:
        """Set dashed-circle R and layout_disk_radius_m from burst extent (source NDF tabs)."""
        if not self.project.bursts:
            r = max(1.0, float(self.ref_m))
        else:
            max_r = max(
                math.hypot(b.x_gameplay_m, b.y_gameplay_m) for b in self.project.bursts
            )
            r = max(1.0, max_r)
        self.project.layout_disk_radius_m = r
        self.preset_r_var.set(r)

    def load_from_project(
        self,
        project: ScatterProject,
        ndf_path: Optional[str] = None,
        *,
        preview_target_m: Optional[float] = None,
    ) -> None:
        """Apply a ScatterProject from batch variations and refresh summary/timeline."""
        self.preview_target_m = preview_target_m
        self.project = project
        self.ref_m = project.reference_gameplay_radius_m
        self.anchor_r = project.anchor_max_ndf_radius
        if ndf_path:
            self.project.source_ndf_path = ndf_path
        if project.layout_disk_radius_m is not None:
            self.preset_r_var.set(float(project.layout_disk_radius_m))
        else:
            self._sync_preset_r_from_bursts()
        self._update_preset_r_label()
        self._rebuild_vfx_filter_ui()
        self._refresh_effect_summary_and_timeline()

    def _set_summary_document(self, body: str) -> None:
        self.summary_text.configure(state=tk.NORMAL)
        self.summary_text.delete('1.0', tk.END)
        self.summary_text.insert('1.0', body)
        self.summary_text.configure(state=tk.DISABLED)

    def _refresh_effect_summary_and_timeline(self) -> None:
        self._set_summary_document('')
        self.summary_meta.config(text='')
        self._timeline_events = []
        self._anim_t_max = 0.0
        self.anim_scale.configure(to=1.0)
        path = self.project.source_ndf_path
        if not path or not Path(path).is_file():
            self.summary_meta.config(text='No NDF path or file missing; load files in General.')
            return
        last_good_root: Optional[ndf.model.List] = None
        try:
            text = Path(path).read_text(encoding='utf-8')
            root = ndf.convert(text)
            if not isinstance(root, ndf.model.List):
                self.summary_meta.config(text='Invalid NDF root.')
                return
            last_good_root = root
            cluster_preview = self.preview_target_m is not None
            if not cluster_preview:
                self._spatial_trim_removed_indices = None
                self._spatial_trim_removed_n = 0
            call_line = ''
            if cluster_preview:
                self._effect_groups_labelframe.config(
                    text=(
                        'Effect groups (cluster preview — emitted + batch scaling: Call/Param Qty, '
                        'radius falloff)'
                    ),
                )
                bkw = self.app._batch_scale_kwargs()
                ccd = bool(bkw.get('consistent_call_density', False))
                targets = parse_target_sizes(self.app.variation_targets_text.get('1.0', tk.END))
                tgt_m = float(self.preview_target_m)
                ecp = (
                    self.app._effect_count_pct_for_target(tgt_m, targets)
                    if targets
                    else None
                )
                ecall = (
                    self.app._effect_call_pct_for_target(tgt_m, targets)
                    if targets
                    else None
                )
                param_rf = self.app._param_radius_falloff_by_vfx()
                call_rf = self.app._call_radius_falloff_by_vfx()
                src_m = self.app._parse_positive_float(self.app.variation_source_m_var.get())
                sf = (tgt_m / src_m) if src_m and src_m > 0 else 1.0
                n_curve_rows = len(self.app._variation_group_call_radius_falloff_curve)
                n_cached_groups = len(self.app._cached_effect_groups)
                _log.info(
                    'scatter cluster preview: ndf=%s tgt_m=%.6g bursts=%d scale_factor=%.6g '
                    'cached_effect_groups=%d call_rf=%s param_rf=%s raw_call_falloff_rows=%d',
                    Path(path).name,
                    tgt_m,
                    len(self.project.bursts),
                    sf,
                    n_cached_groups,
                    'None' if call_rf is None else f'{len(call_rf)} vfx',
                    'None' if param_rf is None else f'{len(param_rf)} vfx',
                    n_curve_rows,
                )
                if call_rf is None and n_curve_rows > 0:
                    _log.warning(
                        'scatter cluster preview: Call radius falloff curves are edited (%d row(s)) but '
                        'merged map is None — refresh effect groups (General) or fix group key mismatch.',
                        n_curve_rows,
                    )
                pipe = run_cluster_emit_scale_pipeline(
                    root,
                    self.project,
                    scale_factor=float(sf),
                    target_radius_m=float(tgt_m),
                    ref_m=float(self.ref_m),
                    anchor_r=float(self.anchor_r),
                    effect_call_scale_pct=ecall,
                    effect_call_batch_scale_min=bkw.get('effect_call_batch_scale_min'),
                    effect_call_batch_scale_max=bkw.get('effect_call_batch_scale_max'),
                    call_radius_falloff_by_vfx=call_rf,
                    param_radius_falloff_by_vfx=param_rf,
                    effect_count_scale_pct=ecp,
                    consistent_call_density=ccd,
                    include_declaration_params=bkw['include_declaration_params'],
                    scale_size=bkw['scale_size'],
                    scale_count=bkw['scale_count'],
                    effect_named_flags=bkw['effect_named_flags'],
                    dry_run=False,
                )
                self._spatial_trim_removed_indices = pipe.spatial_trim_removed_indices
                if self._spatial_trim_removed_indices is not None:
                    self._spatial_trim_removed_n = len(self.project.bursts)
                else:
                    self._spatial_trim_removed_n = 0
                _log.info(
                    'scatter cluster preview: after Call scale, call_changes=%d row(s)',
                    len(pipe.call_changes),
                )
                root = pipe.work
                last_good_root = pipe.work
                xy_sync = burst_gameplay_xy_m_from_parsed_root(
                    pipe.work,
                    float(self.ref_m),
                    float(self.anchor_r),
                )
                if len(xy_sync) == len(self.project.bursts):
                    for bi, (gx, gy) in enumerate(xy_sync):
                        self.project.bursts[bi].x_gameplay_m = float(gx)
                        self.project.bursts[bi].y_gameplay_m = float(gy)
                elif xy_sync:
                    _log.warning(
                        'scatter cluster preview: NDF burst count %d != layout %d; canvas XY not synced',
                        len(xy_sync),
                        len(self.project.bursts),
                    )
                g_call = resolve_effect_call_geom_scale(
                    float(sf),
                    consistent_call_density=ccd,
                    cluster_layout=True,
                )
                call_line = format_call_qty_report_line(
                    pipe.call_changes,
                    effect_call_scale_pct=ecall,
                    scale_factor=sf,
                    effect_call_geom_scale=g_call,
                    ignore_call_qty_curves=ccd,
                    vfx_burst_denoms=pipe.vfx_burst_denoms,
                )
            else:
                self._effect_groups_labelframe.config(text='Effect groups (from loaded NDF)')
            last_good_root = root
            summ = summarize_scatter_ndf(root)
            groups_error_note = ''
            try:
                groups = analyze_effect_groups(root)
            except Exception as exc:
                groups = []
                groups_error_note = f'  |  Effect groups detail skipped: {exc}'
            n_b = len(self.project.bursts)
            _TIMELINE_BURST_CAP = 1500
            timeline_note = ''
            if cluster_preview and n_b > _TIMELINE_BURST_CAP:
                self._timeline_events = []
                self._anim_t_max = 0.0
                timeline_note = f'  |  Timeline off ({n_b} bursts > {_TIMELINE_BURST_CAP})'
            else:
                try:
                    self._timeline_events = build_timeline_events(
                        root,
                        ref_m=self.ref_m,
                        anchor_r=self.anchor_r,
                    )
                    self._anim_t_max = timeline_end_time_s(self._timeline_events)
                except Exception as exc:
                    self._timeline_events = []
                    self._anim_t_max = 0.0
                    timeline_note = f'  |  Timeline unavailable: {exc}'
            max_r = 0.0
            if self.project.bursts:
                max_r = max((
                    math.hypot(b.x_gameplay_m, b.y_gameplay_m) for b in self.project.bursts
                ))
            extra = ''
            if self.project.bursts:
                extra = f'  |  Layout bursts: {len(self.project.bursts)}  |  Approx max radius: {max_r:.0f} m'
            prefix = 'Cluster preview: ' if cluster_preview else 'File: '
            call_block = ''
            if cluster_preview:
                call_block = (
                    '\n\nEffect summary and timeline use the emitted NDF after Call scale + Param scale '
                    '(including radius falloff), matching General / batch preview. '
                    'This preview does not write NDF files; use Create variations with Overwrite to refresh outputs.'
                )
                if call_line:
                    call_block += (
                        f'\n\nCall qty (same as General preview log): {call_line}\n'
                        'Note: each group line is bursts per layout (xN); the curve summary adds '
                        'burst-scaled counts across all Call-curve VFX, so it is not a single xN.\n'
                    )
                    if ccd:
                        call_block += (
                            'Consistent areal call density: Call Qty %% is ignored; TActionCall counts follow area. '
                            'Call radius falloff **repositions** burst anchors (same burst count) using the curves '
                            'as a radial weight (deterministic sampling); nothing is removed for falloff.\n'
                        )
                    else:
                        call_block += (
                            'Call spatial falloff: each burst gets keep-probability = min of its TActionCall VFX curves '
                            '(%% as 0–1) at r_norm = distance/target radius (0=center, 1=edge of the dashed circle). '
                            'Each burst is kept independently with that probability (deterministic from burst index); '
                            'expected kept count is sum(weights). Radial density follows the curve in expectation. '
                            'The scatter canvas omits dots for bursts that trim removes (same emitted NDF '
                            'tree and burst XY as batch Call scale; not recomputed on the canvas). '
                            'Call Qty %% and scale still adjust TActionCall row counts inside bursts that remain.'
                        )
            self.summary_meta.config(
                text=(
                    f'{prefix}TSimultaneousAction bursts: {summ.burst_count}  |  '
                    f'Emit mode: {summ.emit_mode}  |  Total TActionCall: {summ.total_taction_calls}'
                    f'{extra}{groups_error_note}{timeline_note}{call_block}'
                ),
            )
            self._set_summary_document(format_effect_groups_document(groups))
            # Slider stores fraction 0..1; t_now = frac * _anim_t_max (ttk.Scale is unreliable with large `to` in seconds).
            self.anim_scale.configure(from_=0.0, to=1.0)
            self.anim_time_var.set(0.0)
            self._redraw_canvas()
        except Exception as exc:
            _log.exception('scatter summary pipeline failed')
            diag = ''
            if last_good_root is not None:
                try:
                    diag = describe_ndf_tree_issues(last_good_root)
                except Exception:
                    diag = ''
            msg = f'Summary unavailable: {exc}'
            if diag:
                msg += '\n\n' + diag
            self.summary_meta.config(text=msg)
            self._set_summary_document('')
            self._spatial_trim_removed_indices = None
            self._spatial_trim_removed_n = 0

    def _toggle_anim_play(self) -> None:
        if self._anim_playing:
            self._anim_playing = False
            if self._anim_after_id is not None:
                self.after_cancel(self._anim_after_id)
                self._anim_after_id = None
            self.anim_play_btn.config(text='Play')
            return
        if self._anim_t_max <= 1e-9:
            return
        self._anim_playing = True
        self.anim_play_btn.config(text='Pause')
        self._anim_tick()

    def _anim_tick(self) -> None:
        if not self._anim_playing:
            return
        if self._anim_t_max <= 1e-9:
            self._anim_playing = False
            self.anim_play_btn.config(text='Play')
            return
        t_max = max(self._anim_t_max, 1e-9)
        frac = self._safe_double(self.anim_time_var, 0.0)
        dt_s = 0.05 * self._safe_double(self.anim_speed_var, 0.5)
        t_s = frac * t_max + dt_s
        if t_s > t_max:
            t_s = 0.0
        self.anim_time_var.set(t_s / t_max)
        self._anim_after_id = self.after(50, self._anim_tick)

    def _rebuild_vfx_filter_ui(self) -> None:
        for w in self.vfx_filter_inner.winfo_children():
            w.destroy()
        labels = sorted({self._group_key(b.primary_vfx) for b in self.project.bursts})
        dead = [k for k in self._vfx_visible if k not in labels]
        for k in dead:
            del self._vfx_visible[k]
        for key in labels:
            var = self._vfx_visible.setdefault(key, tk.BooleanVar(value=True))
            disp = '(no VFX label)' if key == '' else key
            row = ttk.Frame(self.vfx_filter_inner)
            row.pack(anchor=tk.W, fill=tk.X)
            cb = ttk.Checkbutton(
                row,
                text=disp,
                variable=var,
                command=self._redraw_canvas,
            )
            cb.pack(side=tk.LEFT)
            tk.Label(
                row,
                text='   ',
                background=_color_for_vfx(key or None),
                relief=tk.SOLID,
                borderwidth=1,
            ).pack(side=tk.LEFT, padx=(6, 0))

    @staticmethod
    def _group_key(primary: Optional[str]) -> str:
        return primary if primary else ''

    def _burst_visible(self, b: ScatterBurst) -> bool:
        key = self._group_key(b.primary_vfx)
        var = self._vfx_visible.get(key)
        return var is None or var.get()

    def load_from_ndf_path(self, path: Path, *, silent: bool = False) -> bool:
        """Load scatter points from an NDF file (same logic as Import). Returns True if points were loaded."""
        self.preview_target_m = None
        self._spatial_trim_removed_indices = None
        self._spatial_trim_removed_n = 0
        p = Path(path)
        try:
            text = p.read_text(encoding='utf-8')
            root = ndf.convert(text)
            if not isinstance(root, ndf.model.List):
                raise ValueError('Invalid NDF root')
            pts = extract_scatter_points_with_vfx(root)
            if not pts:
                if silent:
                    self.app.log_message(
                        f'Scatter tab {p.name}: no Mobile Position or parPositionRelative points.',
                    )
                else:
                    messagebox.showwarning(
                        'Import',
                        'No Mobile Position or parPositionRelative points found.',
                    )
                return False
            self.project.bursts = []
            for pt in pts:
                gx, gy = ndf_xy_to_gameplay_m(pt.dx_ndf, pt.dy_ndf, self.ref_m, self.anchor_r)
                igx = int(round(gx))
                igy = int(round(gy))
                self.project.bursts.append(
                    ScatterBurst(float(igx), float(igy), primary_vfx=pt.primary_vfx),
                )
            self.project.source_ndf_path = str(p.resolve())
            self._sync_preset_r_from_bursts()
            self._rebuild_vfx_filter_ui()
            self._refresh_effect_summary_and_timeline()
            if not silent:
                messagebox.showinfo('Import', f'Loaded {len(self.project.bursts)} point(s).')
            return True
        except Exception as exc:
            if silent:
                self.app.log_message(f'Scatter tab {p.name}: {exc}')
            else:
                messagebox.showerror('Import', str(exc))
            return False

    def _canvas_metrics(self) -> Tuple[float, float, float, float, float]:
        """cx, cy, half_px, scale (m per px in x), view_radius_m."""
        cw = max(1, self.canvas.winfo_width())
        ch = max(1, self.canvas.winfo_height())
        cx = cw / 2.0
        cy = ch / 2.0
        vr = max(10.0, self._safe_double(self.view_radius_var, 150.0))
        half = min(cw, ch) / 2.0 - self.PAD
        half = max(1.0, half)
        scale = half / vr
        return cx, cy, scale, vr, half

    def _gameplay_to_canvas(self, gx: float, gy: float) -> Tuple[float, float]:
        cx, cy, scale, _, _ = self._canvas_metrics()
        return cx + gx * scale, cy - gy * scale

    def _redraw_canvas(self, event: Optional[tk.Event] = None) -> None:
        self.canvas.delete('all')
        cx, cy, scale, _, _ = self._canvas_metrics()
        ref_r_m = self._canvas_reference_radius_m()
        ref_r_px = ref_r_m * scale
        self.canvas.create_oval(
            cx - ref_r_px,
            cy - ref_r_px,
            cx + ref_r_px,
            cy + ref_r_px,
            outline='#888888',
            dash=(4, 4),
        )
        if self.preview_target_m is not None:
            r_layout = max(1e-6, self._safe_double(self.preset_r_var, 80.0))
            if abs(r_layout - ref_r_m) > 0.5:
                lr_px = r_layout * scale
                self.canvas.create_oval(
                    cx - lr_px,
                    cy - lr_px,
                    cx + lr_px,
                    cy + lr_px,
                    outline='#444444',
                    dash=(2, 6),
                )
        cw = max(1, self.canvas.winfo_width())
        ch = max(1, self.canvas.winfo_height())
        self.canvas.create_line(0, cy, cw, cy, fill='#333333')
        self.canvas.create_line(cx, 0, cx, ch, fill='#333333')
        t_max = max(self._anim_t_max, 1e-9)
        t_now = self._safe_double(self.anim_time_var, 0.0) * t_max
        fired_burst_indices: set[int] = set()
        for e in self._timeline_events:
            if e.t_s <= t_now + 1e-9:
                fired_burst_indices.add(e.burst_index)

        spatial_trim_removed: Set[int] = set()
        if self.preview_target_m is not None:
            call_rf = self.app._call_radius_falloff_by_vfx()
            if call_rf is not None and len(call_rf) > 0:
                if (
                    self._spatial_trim_removed_indices is not None
                    and self._spatial_trim_removed_n == len(self.project.bursts)
                ):
                    spatial_trim_removed = self._spatial_trim_removed_indices

        by_pos: dict[tuple[int, int], list[int]] = defaultdict(list)
        for bi in fired_burst_indices:
            if bi >= len(self.project.bursts):
                continue
            if bi in spatial_trim_removed:
                continue
            bb = self.project.bursts[bi]
            key = (int(round(bb.x_gameplay_m)), int(round(bb.y_gameplay_m)))
            by_pos[key].append(bi)
        for _k, lst in by_pos.items():
            lst.sort()

        for i, b in enumerate(self.project.bursts):
            if i in spatial_trim_removed:
                continue
            if not self._burst_visible(b):
                continue
            px, py = self._gameplay_to_canvas(b.x_gameplay_m, b.y_gameplay_m)
            fill = _color_for_vfx(b.primary_vfx)
            hi = i in fired_burst_indices
            pos_key = (int(round(b.x_gameplay_m)), int(round(b.y_gameplay_m)))
            base_r = 4
            self.canvas.create_oval(
                px - base_r,
                py - base_r,
                px + base_r,
                py + base_r,
                fill=fill,
                outline='white',
                width=1,
                tags=('pt', str(i)),
            )
            if hi:
                lst = by_pos[pos_key]
                rank = lst.index(i)
                ring_r = 6 + rank * 5
                self.canvas.create_oval(
                    px - ring_r,
                    py - ring_r,
                    px + ring_r,
                    py + ring_r,
                    outline='#ffd700',
                    width=2,
                    tags=('pt_ring', str(i)),
                )


def open_scatter_layout_dialog(app: 'FXEditorApp') -> None:
    """Switch to Batch Size → Scatter layout sub-tab."""
    app.notebook.select(app.batch_tab)
    app.batch_inner_notebook.select(app.batch_scatter_subtab)
