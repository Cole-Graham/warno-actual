"""Modal editor: qty %% vs normalized distance from target center (r / target radius)."""

from __future__ import annotations

import math
import tkinter as tk
from tkinter import ttk
from typing import Any, Callable, Dict, List, Optional, Sequence

import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from .qty_curve_dialog import _NAMED_PRESET_MAX_NAME_LEN, _normalize_named_preset_library
from .radius_falloff import RADIUS_FALLOFF_SAMPLES
from .ui_components import create_vertical_scrollable, install_canvas_mousewheel


def _preset_flat(n: int, value: float) -> List[float]:
    v = float(value)
    return [v] * n


def _r_norm_blend_t(r: float, bottom_out: float) -> float:
    """0 at center (r=0), 1 from bottom_out onward; ramp reaches Ramp end at s=1."""
    r0 = 0.0
    rb = max(0.0, float(bottom_out))
    if rb <= r0 + 1e-12:
        return 1.0 if r > r0 else 0.0
    if r <= r0:
        return 0.0
    if r >= rb:
        return 1.0
    return (r - r0) / (rb - r0)


def _shape_smoothstep(t: float) -> float:
    return t * t * (3.0 - 2.0 * t)


def _preset_ramp_for_r_norm(
    xs: Sequence[float],
    start: float,
    end: float,
    bottom_out: float,
    shape: str,
) -> List[float]:
    """Ramp 100%→Ramp end from center (r_norm=0) to bottom_out; flat at Ramp end beyond."""
    if not xs:
        return []
    if len(xs) == 1:
        return [float(start)]
    a, b = float(start), float(end)
    rb = min(1.0, max(0.0, float(bottom_out)))
    out: List[float] = []
    for x in xs:
        rf = float(x)
        t = _r_norm_blend_t(rf, rb)
        if shape == 'linear':
            s = t
        elif shape == 'quadratic':
            s = t * t
        elif shape == 'sqrt':
            s = math.sqrt(t)
        elif shape == 'fourth_root':
            s = t ** 0.25
        elif shape == 'smoothstep':
            s = _shape_smoothstep(t)
        else:
            s = t
        out.append(a + (b - a) * s)
    return out


def open_radius_falloff_curve_dialog(
    parent: tk.Widget,
    *,
    title: str,
    values: Sequence[float],
    on_apply: Callable[[List[float]], None],
    n_samples: int = RADIUS_FALLOFF_SAMPLES,
    saved_geometry: Optional[str] = None,
    on_geometry_save: Optional[Callable[[str], None]] = None,
    preset_flat: Optional[float] = None,
    preset_end: Optional[float] = None,
    preset_bottom_out_r_norm: Optional[float] = None,
    on_presets_save: Optional[Callable[[Dict[str, float]], None]] = None,
    named_presets: Optional[Dict[str, Dict[str, Any]]] = None,
    on_named_library_save: Optional[Callable[[Dict[str, Dict[str, float]]], None]] = None,
) -> None:
    n = int(n_samples)
    if n <= 0:
        return

    dialog = tk.Toplevel(parent.winfo_toplevel())
    dialog.title(title)
    dialog.transient(parent.winfo_toplevel())
    dialog.grab_set()
    _W, _H = 800, 880
    dialog.minsize(640, 520)
    dialog.geometry(f'{_W}x{_H}')

    spin_vars: List[tk.DoubleVar] = []
    for i in range(n):
        v = float(values[i]) if i < len(values) else 100.0
        spin_vars.append(tk.DoubleVar(value=v))

    xs = [i / (n - 1) if n > 1 else 0.0 for i in range(n)]

    btn_row = ttk.Frame(dialog)
    btn_row.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=(4, 14))

    def _do_apply() -> None:
        out: List[float] = []
        for sv in spin_vars:
            try:
                x = float(sv.get())
            except tk.TclError:
                x = 100.0
            out.append(max(0.0, min(100.0, x)))
        on_apply(out)
        dialog.destroy()

    def _cancel() -> None:
        dialog.destroy()

    ttk.Button(btn_row, text='Apply', command=_do_apply).pack(side=tk.RIGHT, padx=4)
    ttk.Button(btn_row, text='Cancel', command=_cancel).pack(side=tk.RIGHT)

    top = ttk.Frame(dialog, padding=10)
    top.pack(fill=tk.BOTH, expand=True, side=tk.TOP)

    ttk.Label(
        top,
        text=(
            'Qty % vs distance from target center / target effect radius (0 = center, 1 = edge). '
            'Ramp presets go from 100% at the center to Ramp end at “Bottom out at r_norm”; '
            'larger distances stay at Ramp end. Trims more toward the edge in addition to the '
            'per-target-radius curves. Named presets save and reload Flat / Ramp end / Bottom out.'
        ),
        wraplength=700,
    ).pack(anchor=tk.W, pady=(0, 8))

    graph_fr = ttk.LabelFrame(top, text='Curve preview', padding=6)
    graph_fr.pack(fill=tk.X, pady=(0, 8))

    fig = Figure(figsize=(5.6, 2.6), dpi=100)
    ax = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=graph_fr)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def _draw_curve() -> None:
        ys: List[float] = []
        for sv in spin_vars:
            try:
                ys.append(max(0.0, min(100.0, float(sv.get()))))
            except tk.TclError:
                ys.append(100.0)
        ax.clear()
        ax.plot(
            xs,
            ys,
            'o-',
            color='#2563eb',
            linewidth=2.0,
            markersize=7,
            markerfacecolor='#3b82f6',
            markeredgecolor='#1d4ed8',
        )
        ax.set_xlabel('Distance / target radius')
        ax.set_ylabel('Qty %')
        ax.set_ylim(-2, 102)
        ax.set_xlim(-0.05, 1.05)
        ax.grid(True, alpha=0.35, linestyle='-', linewidth=0.8)
        ax.set_axisbelow(True)
        fig.tight_layout()
        canvas.draw_idle()

    for sv in spin_vars:
        sv.trace_add('write', lambda *_a: _draw_curve())

    _draw_curve()

    end_var = tk.DoubleVar(value=50.0)
    flat_var = tk.DoubleVar(value=100.0)
    if preset_flat is not None:
        try:
            flat_var.set(float(preset_flat))
        except (tk.TclError, ValueError, TypeError):
            pass
    if preset_end is not None:
        try:
            end_var.set(float(preset_end))
        except (tk.TclError, ValueError, TypeError):
            pass

    bottom_out_var = tk.DoubleVar(value=1.0)
    if preset_bottom_out_r_norm is not None:
        try:
            bottom_out_var.set(float(preset_bottom_out_r_norm))
        except (tk.TclError, ValueError, TypeError):
            pass

    def _preset_snapshot() -> Dict[str, float]:
        return {
            'flat': float(flat_var.get()),
            'end': float(end_var.get()),
            'bottom_out': float(bottom_out_var.get()),
        }

    def _on_dialog_destroy(event: tk.Event) -> None:
        if event.widget != dialog:
            return
        if on_geometry_save is not None:
            try:
                on_geometry_save(dialog.winfo_geometry())
            except tk.TclError:
                pass
        if on_presets_save is not None:
            try:
                on_presets_save(_preset_snapshot())
            except (tk.TclError, ValueError, TypeError):
                pass

    dialog.bind('<Destroy>', _on_dialog_destroy)

    preset_fr = ttk.LabelFrame(top, text='Presets', padding=6)
    preset_fr.pack(fill=tk.X, pady=(0, 8))

    library: Dict[str, Dict[str, float]] = _normalize_named_preset_library(named_presets)

    named_row = ttk.Frame(preset_fr)
    named_row.pack(fill=tk.X, pady=(0, 6))
    ttk.Label(named_row, text='Saved presets:').pack(side=tk.LEFT, padx=(0, 4))
    combo_var = tk.StringVar(value='')
    combo = ttk.Combobox(named_row, textvariable=combo_var, state='readonly', width=34)
    combo.pack(side=tk.LEFT, padx=(0, 6))

    named_row2 = ttk.Frame(preset_fr)
    named_row2.pack(fill=tk.X, pady=(0, 8))
    ttk.Label(named_row2, text='New name:').pack(side=tk.LEFT, padx=(0, 4))
    name_entry_var = tk.StringVar(value='')
    ttk.Entry(named_row2, textvariable=name_entry_var, width=26).pack(side=tk.LEFT, padx=(0, 6))

    def _refresh_combo() -> None:
        names = sorted(library.keys(), key=lambda s: s.lower())
        combo['values'] = names
        cur = combo_var.get()
        if cur and cur not in names:
            combo_var.set('')

    def _apply_named_to_spinboxes(snap: Dict[str, float]) -> None:
        if 'flat' in snap:
            try:
                flat_var.set(float(snap['flat']))
            except (tk.TclError, ValueError, TypeError):
                pass
        if 'end' in snap:
            try:
                end_var.set(float(snap['end']))
            except (tk.TclError, ValueError, TypeError):
                pass
        if 'bottom_out' in snap:
            try:
                bottom_out_var.set(float(snap['bottom_out']))
            except (tk.TclError, ValueError, TypeError):
                pass

    def _on_combo_selected(_evt: Any = None) -> None:
        name = combo_var.get().strip()
        if not name or name not in library:
            return
        _apply_named_to_spinboxes(library[name])

    def _save_named() -> None:
        name = name_entry_var.get().strip()
        if not name or len(name) > _NAMED_PRESET_MAX_NAME_LEN:
            return
        library[name] = _preset_snapshot()
        if on_named_library_save is not None:
            on_named_library_save(dict(library))
        _refresh_combo()
        combo_var.set(name)

    def _delete_named() -> None:
        name = combo_var.get().strip()
        if not name or name not in library:
            return
        del library[name]
        if on_named_library_save is not None:
            on_named_library_save(dict(library))
        _refresh_combo()

    ttk.Button(named_row2, text='Save as…', command=_save_named).pack(side=tk.LEFT, padx=2)
    ttk.Button(named_row2, text='Delete', command=_delete_named).pack(side=tk.LEFT, padx=2)

    combo.bind('<<ComboboxSelected>>', _on_combo_selected)
    _refresh_combo()

    preset_spin_row = ttk.Frame(preset_fr)
    preset_spin_row.pack(fill=tk.X)

    ttk.Label(preset_spin_row, text='Flat value:').pack(side=tk.LEFT, padx=(0, 4))
    ttk.Spinbox(
        preset_spin_row,
        from_=0.0,
        to=100.0,
        increment=1.0,
        width=6,
        textvariable=flat_var,
    ).pack(side=tk.LEFT, padx=(0, 8))
    ttk.Label(preset_spin_row, text='Ramp end:').pack(side=tk.LEFT, padx=(8, 4))
    ttk.Spinbox(
        preset_spin_row,
        from_=0.0,
        to=100.0,
        increment=1.0,
        width=6,
        textvariable=end_var,
    ).pack(side=tk.LEFT, padx=(0, 8))
    ttk.Label(preset_spin_row, text='Bottom out at r_norm:').pack(side=tk.LEFT, padx=(8, 4))
    ttk.Spinbox(
        preset_spin_row,
        from_=0.0,
        to=1.0,
        increment=0.05,
        width=6,
        textvariable=bottom_out_var,
    ).pack(side=tk.LEFT, padx=(0, 4))
    ttk.Label(preset_spin_row, text='(0=center → 1=edge)').pack(side=tk.LEFT, padx=(0, 8))

    def _apply_preset(vals: List[float]) -> None:
        for i, x in enumerate(vals):
            if i < len(spin_vars):
                spin_vars[i].set(x)

    btn_inner = ttk.Frame(preset_fr)
    btn_inner.pack(fill=tk.X, pady=(8, 0))
    ttk.Button(
        btn_inner,
        text='Flat',
        command=lambda: _apply_preset(_preset_flat(n, float(flat_var.get()))),
    ).pack(side=tk.LEFT, padx=2)

    def _ramp(shape: str) -> None:
        try:
            bo = float(bottom_out_var.get())
        except (tk.TclError, ValueError, TypeError):
            bo = 1.0
        _apply_preset(
            _preset_ramp_for_r_norm(xs, 100.0, float(end_var.get()), bo, shape),
        )

    ttk.Button(
        btn_inner,
        text='Linear 100→end',
        command=lambda: _ramp('linear'),
    ).pack(side=tk.LEFT, padx=2)
    ttk.Button(
        btn_inner,
        text='Quadratic',
        command=lambda: _ramp('quadratic'),
    ).pack(side=tk.LEFT, padx=2)
    ttk.Button(
        btn_inner,
        text='Sqrt',
        command=lambda: _ramp('sqrt'),
    ).pack(side=tk.LEFT, padx=2)
    ttk.Button(
        btn_inner,
        text='Fourth root',
        command=lambda: _ramp('fourth_root'),
    ).pack(side=tk.LEFT, padx=2)
    ttk.Button(
        btn_inner,
        text='Smoothstep',
        command=lambda: _ramp('smoothstep'),
    ).pack(side=tk.LEFT, padx=2)

    def _save_preset_defaults() -> None:
        if on_presets_save is None:
            return
        try:
            on_presets_save(_preset_snapshot())
        except (tk.TclError, ValueError, TypeError):
            pass

    ttk.Button(
        preset_fr,
        text='Save preset defaults',
        command=_save_preset_defaults,
    ).pack(anchor=tk.W, pady=(6, 0))

    scroll_container, scroll_canvas, inner = create_vertical_scrollable(top, padding=4)
    scroll_container.pack(fill=tk.BOTH, expand=True, pady=(0, 0))
    install_canvas_mousewheel(dialog, scroll_canvas, scroll_container)

    ttk.Label(inner, text='Per-distance values', font=('TkDefaultFont', 9, 'bold')).pack(
        anchor=tk.W,
        pady=(0, 4),
    )

    for i in range(n):
        row = ttk.Frame(inner)
        row.pack(fill=tk.X, pady=2)
        t_norm = xs[i]
        ttk.Label(row, text=f'{t_norm:.2f}', width=12).pack(side=tk.LEFT)
        ttk.Spinbox(
            row,
            from_=0.0,
            to=100.0,
            increment=1.0,
            width=8,
            textvariable=spin_vars[i],
        ).pack(side=tk.LEFT, padx=4)
        ttk.Label(row, text='%').pack(side=tk.LEFT)

    dialog.update_idletasks()
    if saved_geometry:
        try:
            dialog.geometry(saved_geometry)
        except tk.TclError:
            sw = dialog.winfo_screenwidth()
            sh = dialog.winfo_screenheight()
            dialog.geometry(f'{_W}x{_H}+{(sw - _W) // 2}+{(sh - _H) // 2}')
    else:
        sw = dialog.winfo_screenwidth()
        sh = dialog.winfo_screenheight()
        dialog.geometry(f'{_W}x{_H}+{(sw - _W) // 2}+{(sh - _H) // 2}')
