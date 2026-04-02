"""Shared UI helpers for FX editor."""

import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk
from typing import Any, Tuple, Union

# Add project root to path for imports (same as dpm_visualizer)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src import ndf


def _is_descendant(widget: tk.Widget, ancestor: tk.Widget) -> bool:
    w: Any = widget
    while w is not None:
        if w == ancestor:
            return True
        try:
            w = w.master
        except (tk.TclError, AttributeError):
            break
    return False


def create_vertical_scrollable(
    parent: tk.Widget,
    *,
    padding: Union[int, str] = 0,
) -> Tuple[ttk.Frame, tk.Canvas, ttk.Frame]:
    """Build a vertically scrollable area: ``container`` holds ``canvas`` + scrollbar; put children on ``inner``.

    The canvas grows horizontally with the parent; ``inner`` tracks canvas width. Pack ``container`` with
    ``fill=tk.BOTH, expand=True`` in ``parent``.
    """
    container = ttk.Frame(parent)
    canvas = tk.Canvas(container, highlightthickness=0)
    vsb = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)
    inner = ttk.Frame(canvas, padding=padding)
    win_id = canvas.create_window((0, 0), window=inner, anchor='nw')

    def _on_inner_configure(_event: tk.Event) -> None:
        canvas.configure(scrollregion=canvas.bbox('all'))

    def _on_canvas_configure(event: tk.Event) -> None:
        canvas.itemconfigure(win_id, width=event.width)

    inner.bind('<Configure>', _on_inner_configure)
    canvas.bind('<Configure>', _on_canvas_configure)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    vsb.pack(side=tk.RIGHT, fill=tk.Y)

    return container, canvas, inner


def _widget_uses_own_vertical_scroll(widget: tk.Widget) -> bool:
    """True for widgets that handle the mouse wheel themselves (avoid double-scrolling the outer canvas)."""
    try:
        cls = widget.winfo_class()
    except tk.TclError:
        return False
    return cls in ('Listbox', 'Text', 'TText')


def install_canvas_mousewheel(
    root: tk.Tk,
    canvas: tk.Canvas,
    container: tk.Widget,
) -> None:
    """Bind mouse wheel to ``canvas`` only when the pointer is over a descendant of ``container``."""

    def _on_mousewheel(event: tk.Event) -> None:
        if not _is_descendant(event.widget, container):
            return
        if _widget_uses_own_vertical_scroll(event.widget):
            return
        try:
            delta = getattr(event, 'delta', 0)
            if not delta:
                return
            if sys.platform == 'darwin':
                canvas.yview_scroll(-1 * int(delta), 'units')
            else:
                canvas.yview_scroll(int(-1 * (delta / 120)), 'units')
        except tk.TclError:
            pass

    def _on_linux_up(event: tk.Event) -> None:
        if not _is_descendant(event.widget, container):
            return
        if _widget_uses_own_vertical_scroll(event.widget):
            return
        canvas.yview_scroll(-1, 'units')

    def _on_linux_down(event: tk.Event) -> None:
        if not _is_descendant(event.widget, container):
            return
        if _widget_uses_own_vertical_scroll(event.widget):
            return
        canvas.yview_scroll(1, 'units')

    root.bind_all('<MouseWheel>', _on_mousewheel)
    root.bind_all('<Button-4>', _on_linux_up)
    root.bind_all('<Button-5>', _on_linux_down)

    def _on_destroy(_event: tk.Event) -> None:
        root.unbind_all('<MouseWheel>')
        root.unbind_all('<Button-4>')
        root.unbind_all('<Button-5>')

    container.bind('<Destroy>', _on_destroy, add='+')


def format_value(value: Any) -> str:
    """Format an NDF value for display."""
    if isinstance(value, (ndf.model.List, ndf.model.Map, ndf.model.Object)):
        return ndf.printer.string(value).strip()
    return str(value)


def parse_value_input(value_text: str) -> Any:
    """Parse a user-provided value string into an NDF value if possible."""
    try:
        parsed = ndf.expression(value_text)
        if isinstance(parsed, dict) and 'value' in parsed:
            return parsed['value']
    except Exception:
        pass
    return value_text
