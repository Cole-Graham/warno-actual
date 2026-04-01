"""Mult-edit dialog: pick effect pattern groups and open shared curve editors."""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from typing import TYPE_CHECKING, Callable, Dict, List

from .scatter_analyze import effect_group_key
from .ui_components import create_vertical_scrollable, install_canvas_mousewheel

if TYPE_CHECKING:
    from .main import FXEditorApp


def _ordered_group_keys(app: 'FXEditorApp') -> List[str]:
    seen = set()
    out: List[str] = []
    for g in getattr(app, '_cached_effect_groups', None) or []:
        k = effect_group_key(g)
        if k not in seen:
            seen.add(k)
            out.append(k)
    for k in getattr(app, '_variation_group_toggle_vars', {}) or {}:
        if k not in seen:
            out.append(k)
    return out


def open_group_curves_multiedit_dialog(parent: tk.Widget, app: 'FXEditorApp') -> None:
    if not app._variation_group_toggle_vars:
        messagebox.showwarning(
            'Effect groups',
            'Refresh effect groups from selection first.',
        )
        return
    keys = _ordered_group_keys(app)
    if not keys:
        messagebox.showwarning('Effect groups', 'No effect groups to edit.')
        return

    dialog = tk.Toplevel(parent.winfo_toplevel())
    dialog.title('Mult-edit pattern curves')
    dialog.transient(parent.winfo_toplevel())
    dialog.grab_set()
    dialog.minsize(520, 420)
    dialog.geometry('640x520')

    top = ttk.Frame(dialog, padding=10)
    top.pack(fill=tk.BOTH, expand=True)

    ttk.Label(
        top,
        text=(
            'Check one or more effect patterns, then open a curve editor. '
            'When multiple patterns are checked, the edited curve is applied to all of them '
            '(initial values come from the first checked pattern in the list).'
        ),
        wraplength=600,
    ).pack(anchor=tk.W, pady=(0, 8))

    btn_row_checks = ttk.Frame(top)
    btn_row_checks.pack(fill=tk.X, pady=(0, 6))
    check_vars: Dict[str, tk.BooleanVar] = {k: tk.BooleanVar(value=False) for k in keys}
    saved_checks = getattr(app, '_saved_dialog_substate', {}).get('group_curves_multiedit_checks', {})
    if isinstance(saved_checks, dict):
        for k, v in check_vars.items():
            if k in saved_checks and isinstance(saved_checks[k], bool):
                v.set(saved_checks[k])

    def _set_all(value: bool) -> None:
        for v in check_vars.values():
            v.set(value)

    ttk.Button(btn_row_checks, text='Select all', command=lambda: _set_all(True)).pack(
        side=tk.LEFT,
        padx=(0, 6),
    )
    ttk.Button(btn_row_checks, text='Clear selection', command=lambda: _set_all(False)).pack(
        side=tk.LEFT,
        padx=(0, 6),
    )

    scroll_container, scroll_canvas, inner = create_vertical_scrollable(top, padding=4)
    scroll_container.pack(fill=tk.BOTH, expand=True, pady=(0, 8))
    install_canvas_mousewheel(dialog, scroll_canvas, scroll_container)

    for k in keys:
        row = ttk.Frame(inner)
        row.pack(fill=tk.X, pady=1)
        ttk.Checkbutton(row, variable=check_vars[k]).pack(side=tk.LEFT, padx=(0, 6))
        lab = k if len(k) <= 100 else k[:97] + '…'
        ttk.Label(row, text=lab, wraplength=520).pack(side=tk.LEFT, anchor=tk.W)

    curve_fr = ttk.LabelFrame(top, text='Curves (checked groups)', padding=6)
    curve_fr.pack(fill=tk.X, pady=(4, 0))

    def _selected_keys_in_order() -> List[str]:
        return [k for k in keys if check_vars[k].get()]

    def _run(action: Callable[[List[str]], None]) -> None:
        sel = _selected_keys_in_order()
        if not sel:
            messagebox.showwarning('Selection', 'Check at least one effect pattern.')
            return
        action(sel)

    r1 = ttk.Frame(curve_fr)
    r1.pack(fill=tk.X)
    ttk.Button(
        r1,
        text='Param Qty curve…',
        width=20,
        command=lambda: _run(app._open_param_qty_curve_for_keys),
    ).pack(side=tk.LEFT, padx=2, pady=2)
    ttk.Button(
        r1,
        text='Call Qty curve…',
        width=20,
        command=lambda: _run(app._open_call_qty_curve_for_keys),
    ).pack(side=tk.LEFT, padx=2, pady=2)
    r2 = ttk.Frame(curve_fr)
    r2.pack(fill=tk.X)
    ttk.Button(
        r2,
        text='Param radius falloff…',
        width=20,
        command=lambda: _run(app._open_param_radius_falloff_curve_for_keys),
    ).pack(side=tk.LEFT, padx=2, pady=2)
    ttk.Button(
        r2,
        text='Call radius falloff…',
        width=20,
        command=lambda: _run(app._open_call_radius_falloff_curve_for_keys),
    ).pack(side=tk.LEFT, padx=2, pady=2)

    bottom = ttk.Frame(dialog)
    bottom.pack(fill=tk.X, padx=10, pady=(0, 10))
    ttk.Button(bottom, text='Close', command=dialog.destroy).pack(side=tk.RIGHT)

    def _save_group_multiedit_state(event: tk.Event) -> None:
        if event.widget != dialog:
            return
        try:
            app._saved_dialog_geometry['group_curves_multiedit'] = dialog.winfo_geometry()
        except tk.TclError:
            pass
        app._saved_dialog_substate['group_curves_multiedit_checks'] = {
            k: bool(v.get()) for k, v in check_vars.items()
        }
        app._schedule_state_save()

    dialog.bind('<Destroy>', _save_group_multiedit_state)

    dialog.update_idletasks()
    geom = getattr(app, '_saved_dialog_geometry', {}).get('group_curves_multiedit')
    w, h = 640, 520
    if geom:
        try:
            dialog.geometry(geom)
        except tk.TclError:
            sw = dialog.winfo_screenwidth()
            sh = dialog.winfo_screenheight()
            dialog.geometry(f'{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}')
    else:
        sw = dialog.winfo_screenwidth()
        sh = dialog.winfo_screenheight()
        dialog.geometry(f'{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}')
