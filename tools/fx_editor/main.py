"""Main application entry point for FX Editor."""

import logging
import os
import platform
import queue
import re
import subprocess
import sys
import threading
import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# Add project root to path for imports (same as dpm_visualizer)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

_FX_EDITOR_DIR = Path(__file__).resolve().parent
_DEFAULT_BATCH_OUTPUT_DIR = _FX_EDITOR_DIR / 'out'

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .ndf_access import parse_ndf_file, write_ndf_file, get_export_row, update_namespace
from .model_index import build_tree, TreeNode
from .batch_variation_jobs import apply_variations_worker, preview_variations_worker
from .size_batch import (
    DEFAULT_VARIATION_FILENAME_TEMPLATE,
    effect_call_batch_scale_bounds,
    find_fx_files,
    parse_target_sizes,
    render_variation_filename,
)
from .scatter_analyze import (
    analyze_effect_groups,
    effect_group_key,
    effect_named_flags_from_group_toggles,
    merge_effect_group_rows,
    merge_effect_qty_pct_for_target_radius,
    merge_effect_radius_falloff_curves,
)
from .scatter_model import load_scatter_calibration_yaml
from .scatter_timing import infer_anchor_bounds_from_parsed
from .scatter_model import ScatterProject
from .call_scale import format_call_qty_report_line
from .preview_window import PreviewWindow
from .qty_curve_dialog import open_qty_curve_dialog
from .radius_falloff import RADIUS_FALLOFF_SAMPLES
from .radius_falloff_dialog import open_radius_falloff_curve_dialog
from .group_curves_multiedit_dialog import open_group_curves_multiedit_dialog
from .fx_logging import clear_debug_log_buffer, get_debug_log_buffer_text, setup_fx_logging
from .state_store import load_state, save_state
from .scatter_dialog import ScatterLayoutPanel
from .ui_components import (
    create_vertical_scrollable,
    format_value,
    install_canvas_mousewheel,
    parse_value_input,
)


class FXEditorApp:
    """Main application class for FX Editor."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self._saved_dialog_geometry: Dict[str, str] = {}
        #: Persisted dialog UI beyond geometry (mult-edit checks, curve preset spins, etc.).
        self._saved_dialog_substate: Dict[str, Any] = {}
        self._state_save_after_id: Optional[str] = None
        #: True while :meth:`_sync_scatter_tab_to_file_list` calls ``notebook.select`` (avoid wiping multi-select).
        self._suppress_notebook_listbox_sync: bool = False
        self.root.title('FX Editor')
        self.root.geometry('1200x800')

        self.current_file: Optional[Path] = None
        self.parsed_root: Optional[ndf.model.List] = None
        self.tree_nodes: Dict[str, TreeNode] = {}
        self.tree_item_refs: Dict[str, TreeNode] = {}
        self.property_refs: Dict[str, Any] = {}

        self.setup_ui()
        self._apply_saved_state(load_state())
        self.root.after(0, self._maximize_main_window)
        self.root.protocol('WM_DELETE_WINDOW', self._on_close)

    def setup_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding='10')
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.editor_tab = ttk.Frame(self.notebook)
        self.batch_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.editor_tab, text='Editor')
        self.notebook.add(self.batch_tab, text='Batch Size')

        self.setup_editor_tab()
        self.setup_batch_tab()

    def setup_editor_tab(self) -> None:
        top_frame = ttk.LabelFrame(self.editor_tab, text='FX File', padding='10')
        top_frame.pack(fill=tk.X, padx=10, pady=10)

        self.file_var = tk.StringVar()
        ttk.Entry(top_frame, textvariable=self.file_var, width=80).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(top_frame, text='Browse', command=self.browse_file).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(top_frame, text='Load', command=self.load_file).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(top_frame, text='Save', command=self.save_file).pack(side=tk.LEFT, padx=(5, 0))
        
        # Add namespace update button
        namespace_frame = ttk.Frame(top_frame)
        namespace_frame.pack(side=tk.LEFT, padx=(10, 0))
        ttk.Button(namespace_frame, text='Update Namespace', command=self.manual_namespace_update).pack()
        ttk.Button(
            namespace_frame,
            text='Debug log…',
            command=self.open_debug_log_window,
        ).pack(side=tk.LEFT, padx=(8, 0))

        paned = ttk.PanedWindow(self.editor_tab, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        left_frame = ttk.LabelFrame(paned, text='Structure', padding='5')
        right_frame = ttk.LabelFrame(paned, text='Properties', padding='5')
        paned.add(left_frame, weight=1)
        paned.add(right_frame, weight=2)

        tree_frame = ttk.Frame(left_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode=tk.BROWSE)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tree_scroll.config(command=self.tree.yview)
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

        props_frame = ttk.Frame(right_frame)
        props_frame.pack(fill=tk.BOTH, expand=True)
        props_scroll = ttk.Scrollbar(props_frame)
        props_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.properties_tree = ttk.Treeview(
            props_frame,
            columns=('value',),
            show='tree headings',
            yscrollcommand=props_scroll.set,
            selectmode=tk.BROWSE,
        )
        self.properties_tree.heading('#0', text='Name')
        self.properties_tree.heading('value', text='Value')
        self.properties_tree.column('value', width=400)
        self.properties_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        props_scroll.config(command=self.properties_tree.yview)
        self.properties_tree.bind('<<TreeviewSelect>>', self.on_property_select)

        edit_frame = ttk.Frame(right_frame)
        edit_frame.pack(fill=tk.X, pady=(5, 0))
        ttk.Label(edit_frame, text='New Value:').pack(side=tk.LEFT, padx=(0, 5))
        self.value_var = tk.StringVar()
        ttk.Entry(edit_frame, textvariable=self.value_var, width=60).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(edit_frame, text='Apply', command=self.apply_property_value).pack(side=tk.LEFT, padx=(5, 0))

        self.property_info = ttk.Label(right_frame, text='Select a node to view properties.')
        self.property_info.pack(fill=tk.X, pady=(5, 0))

    def setup_batch_tab(self) -> None:
        self.batch_inner_notebook = ttk.Notebook(self.batch_tab)
        self.batch_inner_notebook.pack(fill=tk.BOTH, expand=True)

        batch_general = ttk.Frame(self.batch_inner_notebook)
        self.batch_scatter_subtab = ttk.Frame(self.batch_inner_notebook)
        self.batch_inner_notebook.add(batch_general, text='General')
        self.batch_inner_notebook.add(self.batch_scatter_subtab, text='Scatter layout')

        scroll_container, batch_canvas, main_frame = create_vertical_scrollable(
            batch_general,
            padding='10',
        )
        scroll_container.pack(fill=tk.BOTH, expand=True)
        install_canvas_mousewheel(self.root, batch_canvas, scroll_container)

        dir_frame = ttk.LabelFrame(main_frame, text='Directory', padding='10')
        dir_frame.pack(fill=tk.X, pady=(0, 10))

        self.dir_var = tk.StringVar()
        ttk.Entry(dir_frame, textvariable=self.dir_var, width=60).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(dir_frame, text='Browse Dir', command=self.browse_directory).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(dir_frame, text='Browse Files', command=self.browse_files).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(dir_frame, text='Load Files', command=self.load_files).pack(side=tk.LEFT, padx=(5, 0))

        file_frame = ttk.LabelFrame(main_frame, text='Files', padding='10')
        file_frame.pack(fill=tk.X, expand=False, pady=(0, 10))

        listbox_frame = ttk.Frame(file_frame)
        listbox_frame.pack(fill=tk.X, expand=False)

        scrollbar = ttk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_listbox = tk.Listbox(
            listbox_frame,
            height=12,
            selectmode=tk.EXTENDED,
            exportselection=False,
            yscrollcommand=scrollbar.set,
        )
        self.file_listbox.pack(side=tk.LEFT, fill=tk.X, expand=True)
        scrollbar.config(command=self.file_listbox.yview)

        file_buttons_frame = ttk.Frame(file_frame)
        file_buttons_frame.pack(fill=tk.X, pady=(5, 0))
        ttk.Button(file_buttons_frame, text='Select All', command=self.select_all_files).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(file_buttons_frame, text='Clear Selection', command=self.clear_selection).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(
            file_buttons_frame,
            text='Open output folder',
            command=self.open_batch_output_folder,
        ).pack(side=tk.LEFT)

        out_dir_row = ttk.Frame(file_frame)
        out_dir_row.pack(fill=tk.X, pady=(6, 0))
        ttk.Label(out_dir_row, text='Variation output directory:').pack(side=tk.LEFT, padx=(0, 5))
        self.batch_output_dir_var = tk.StringVar(value=str(_DEFAULT_BATCH_OUTPUT_DIR))
        ttk.Entry(out_dir_row, textvariable=self.batch_output_dir_var, width=52).pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
        )
        ttk.Button(out_dir_row, text='Browse…', command=self.browse_batch_output_dir).pack(side=tk.LEFT, padx=(5, 0))

        param_pick_frame = ttk.Frame(main_frame)
        param_pick_frame.pack(fill=tk.X, pady=(0, 10))
        ttk.Button(
            param_pick_frame,
            text='Open Scatter layout…',
            command=self.open_scatter_layout_dialog,
        ).pack(side=tk.LEFT, padx=(0, 10))
        self.batch_param_status_label = ttk.Label(
            param_pick_frame,
            text='',
            font=('TkDefaultFont', 9),
        )
        self.batch_param_status_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.batch_include_declaration_var = tk.BooleanVar(value=True)
        self.variation_geom_var = tk.StringVar(value='param')
        self._batch_preview_scale_factor = 1.0
        self._cached_effect_groups: List[Any] = []
        self._variation_group_toggle_vars: Dict[str, Tuple[tk.BooleanVar, tk.BooleanVar]] = {}
        self._variation_group_count_scale_vars: Dict[str, tk.DoubleVar] = {}
        self._variation_group_call_scale_vars: Dict[str, tk.DoubleVar] = {}
        self._variation_group_param_qty_curve: Dict[str, List[float]] = {}
        self._variation_group_call_qty_curve: Dict[str, List[float]] = {}
        self._variation_group_param_radius_falloff_curve: Dict[str, List[float]] = {}
        self._variation_group_call_radius_falloff_curve: Dict[str, List[float]] = {}
        self._update_batch_param_status_label()

        results_frame = ttk.LabelFrame(main_frame, text='Results', padding='10')
        results_frame.pack(fill=tk.X, expand=False)
        results_btns = ttk.Frame(results_frame)
        results_btns.pack(fill=tk.X, pady=(0, 6))
        ttk.Button(
            results_btns,
            text='Copy results',
            command=self.copy_results_text_to_clipboard,
        ).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(
            results_btns,
            text='View debug log…',
            command=self.open_debug_log_window,
        ).pack(side=tk.LEFT)
        ttk.Label(
            results_btns,
            text='(stderr + buffer; set FX_EDITOR_LOG_LEVEL=DEBUG for per-burst detail)',
            font=('TkDefaultFont', 8),
        ).pack(side=tk.LEFT, padx=(10, 0))
        self._results_text_font = tkfont.nametofont('TkFixedFont').copy()
        self._results_text_font.configure(size=9)
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            height=10,
            wrap=tk.WORD,
            state=tk.DISABLED,
            font=self._results_text_font,
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)

        egf = ttk.LabelFrame(
            main_frame,
            text='NamedParams by effect pattern (parameter scaling)',
            padding=6,
        )
        egf.pack(fill=tk.X, pady=(0, 10))
        ttk.Checkbutton(
            egf,
            text='Scale declaration Params (default values in the effect declaration)',
            variable=self.batch_include_declaration_var,
            command=self._update_batch_param_status_label,
        ).pack(anchor=tk.W)
        ttk.Label(
            egf,
            text=(
                'Emit cycles every TSimultaneousAction pattern in the file. '
                'Refresh merges effect groups from all selected files (patterns only in one file still appear). '
                'Per-group Size/Count choose which NamedParams scale for VFX in that pattern. '
                'Param Qty % caps count-like NamedParams (parCount, etc.): 100% = full scale; lower values '
                'reduce more on larger size-variants. Use the curve button for per-target-radius qty %. '
                'Radius falloff trims more toward the edge of the target (distance from center / target '
                'radius), in addition to those curves. '
                'Call Qty % scales TActionCall row counts with target radius; declaration Params follow '
                'the checkbox above.'
            ),
            font=('TkDefaultFont', 8),
            wraplength=880,
            justify=tk.LEFT,
        ).pack(anchor=tk.W, pady=(4, 0))
        eg_btn_row = ttk.Frame(egf)
        eg_btn_row.pack(fill=tk.X, pady=(4, 0))
        ttk.Button(
            eg_btn_row,
            text='Refresh effect groups from selection',
            command=self._refresh_variation_effect_groups,
        ).pack(side=tk.LEFT)
        bulk_fr = ttk.Frame(eg_btn_row)
        bulk_fr.pack(side=tk.LEFT, padx=(16, 0))
        ttk.Label(bulk_fr, text='Per-group toggles:').pack(side=tk.LEFT, padx=(0, 6))
        ttk.Button(bulk_fr, text='Select all Size', width=14, command=self._variation_select_all_size).pack(
            side=tk.LEFT,
            padx=2,
        )
        ttk.Button(bulk_fr, text='Clear all Size', width=14, command=self._variation_clear_all_size).pack(
            side=tk.LEFT,
            padx=2,
        )
        ttk.Button(bulk_fr, text='Select all Count', width=14, command=self._variation_select_all_count).pack(
            side=tk.LEFT,
            padx=2,
        )
        ttk.Button(bulk_fr, text='Clear all Count', width=14, command=self._variation_clear_all_count).pack(
            side=tk.LEFT,
            padx=2,
        )
        ttk.Button(
            bulk_fr,
            text='Mult-edit…',
            width=12,
            command=self._open_group_curves_multiedit_dialog,
        ).pack(side=tk.LEFT, padx=(14, 2))
        self._variation_group_checks_frame = ttk.Frame(egf)
        self._variation_group_checks_frame.pack(fill=tk.X, pady=(4, 0))

        variation_frame = ttk.LabelFrame(main_frame, text='Batch size variations (scaled copies)', padding='10')
        variation_frame.pack(fill=tk.X, pady=(0, 10))

        self.variation_source_m_var = tk.StringVar(value='60')
        row_vs = ttk.Frame(variation_frame)
        row_vs.pack(fill=tk.X)
        ttk.Label(row_vs, text='Source effect radius (m):').pack(side=tk.LEFT, padx=(0, 5))
        ttk.Entry(row_vs, textvariable=self.variation_source_m_var, width=12).pack(side=tk.LEFT)

        ttk.Label(variation_frame, text='Target radii (m), comma or newline separated:').pack(anchor=tk.W, pady=(8, 0))
        self.variation_targets_text = scrolledtext.ScrolledText(
            variation_frame,
            height=4,
            wrap=tk.WORD,
            font=('TkDefaultFont', 9),
        )
        self.variation_targets_text.pack(fill=tk.X, pady=(2, 0))
        self.variation_targets_text.insert(
            tk.END,
            '35, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300',
        )

        row_rn = ttk.Frame(variation_frame)
        row_rn.pack(fill=tk.X, pady=(8, 0))
        ttk.Label(row_rn, text='Root name ({rootname}):').pack(side=tk.LEFT, padx=(0, 5))
        self.variation_rootname_var = tk.StringVar(
            value='fx_impact_sol_HE_M270_227mm',
        )
        ttk.Entry(row_rn, textvariable=self.variation_rootname_var, width=70).pack(side=tk.LEFT, fill=tk.X, expand=True)

        row_tpl = ttk.Frame(variation_frame)
        row_tpl.pack(fill=tk.X, pady=(6, 0))
        ttk.Label(row_tpl, text='Filename template:').pack(side=tk.LEFT, padx=(0, 5))
        self.variation_template_var = tk.StringVar(value=DEFAULT_VARIATION_FILENAME_TEMPLATE)
        ttk.Entry(row_tpl, textvariable=self.variation_template_var, width=70).pack(side=tk.LEFT, fill=tk.X, expand=True)

        ttk.Label(
            variation_frame,
            text=(
                'Placeholders: {rootname}, {radiusinmeters} (effect radius, m), {n} (trailing index '
                'from source stem), {suffix} (e.g. _1 from …_Cluster_1). Default uses …_r{radiusinmeters}m… '
                '(r = radius in meters). Namespace matches new stem.'
            ),
            font=('TkDefaultFont', 8),
            wraplength=900,
            justify=tk.LEFT,
        ).pack(anchor=tk.W, pady=(4, 0))

        self.variation_overwrite_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(
            variation_frame,
            text='Overwrite existing destination files',
            variable=self.variation_overwrite_var,
        ).pack(anchor=tk.W, pady=(4, 0))

        ttk.Label(
            variation_frame,
            text='Layout for each target radius (relative to source effect radius):',
            font=('TkDefaultFont', 9, 'bold'),
        ).pack(anchor=tk.W, pady=(10, 4))
        geom_fr = ttk.Frame(variation_frame)
        geom_fr.pack(fill=tk.X, anchor=tk.W)
        ttk.Radiobutton(
            geom_fr,
            text='Keep source Actions layout (scale numeric parameters only)',
            variable=self.variation_geom_var,
            value='param',
            command=self._sync_variation_geom_widgets,
        ).pack(anchor=tk.W)
        ttk.Radiobutton(
            geom_fr,
            text=(
                'Reshape scatter: scale TSimultaneousAction count ∝ target/source, hex layout + wait envelope'
            ),
            variable=self.variation_geom_var,
            value='cluster',
            command=self._sync_variation_geom_widgets,
        ).pack(anchor=tk.W)

        row_cl = ttk.Frame(variation_frame)
        row_cl.pack(fill=tk.X, pady=(4, 0))
        ttk.Label(row_cl, text='Max anchor wait (s):').pack(side=tk.LEFT, padx=(0, 5))
        self.variation_wait_max_var = tk.DoubleVar(value=0.75)
        self.variation_wait_spin = ttk.Spinbox(
            row_cl,
            from_=0.01,
            to=30.0,
            increment=0.05,
            width=8,
            textvariable=self.variation_wait_max_var,
        )
        self.variation_wait_spin.pack(side=tk.LEFT)
        ttk.Label(row_cl, text='Min (from file):').pack(side=tk.LEFT, padx=(12, 4))
        self.variation_anchor_min_label = ttk.Label(row_cl, text='—')
        self.variation_anchor_min_label.pack(side=tk.LEFT)

        ttk.Label(
            variation_frame,
            text=(
                'Reshape scatter: hex gameplay layout uses each target radius (m) as the disk radius for that file; '
                'burst count still scales with (target/source)².'
            ),
            font=('TkDefaultFont', 8),
            wraplength=880,
            justify=tk.LEFT,
        ).pack(anchor=tk.W, pady=(4, 0))

        self._cluster_mode_spinboxes = (self.variation_wait_spin,)

        var_btn = ttk.Frame(variation_frame)
        var_btn.pack(fill=tk.X, pady=(8, 0))
        self.variation_preview_btn = ttk.Button(
            var_btn,
            text='Preview variations',
            command=self.preview_variations,
        )
        self.variation_preview_btn.pack(side=tk.LEFT, padx=(0, 5))
        self.variation_apply_btn = ttk.Button(
            var_btn,
            text='Create variations',
            command=self.apply_variations,
        )
        self.variation_apply_btn.pack(side=tk.LEFT)
        self.variation_progress_fr = ttk.Frame(variation_frame)
        self.variation_progress_fr.pack(fill=tk.X, pady=(6, 0))
        self.variation_progress = ttk.Progressbar(
            self.variation_progress_fr,
            mode='determinate',
            length=400,
            maximum=100,
            value=0,
        )
        self.variation_progress.pack(fill=tk.X)
        self.variation_progress_label = ttk.Label(self.variation_progress_fr, text='', font=('TkDefaultFont', 8))
        self.variation_progress_label.pack(anchor=tk.W)
        self._batch_job_running = False
        self._batch_job_queue: Optional[queue.Queue] = None
        #: Serialized scatter tab reloads during batch apply so heavy ``load_from_project`` calls
        #: cannot starve ``_drain_batch_queue`` (progress would jump from e.g. 4/27 to 27/27).
        self._scatter_reload_queue: List[Dict[str, Any]] = []
        self._scatter_reload_pump_scheduled = False

        self.available_files: List[Path] = []
        #: Last file-list index synced to scatter notebook (avoids spurious <<ListboxSelect>> resetting preview tabs).
        self._last_scatter_listbox_idx: Optional[int] = None

        self._scatter_variation_vars: Dict[float, tk.BooleanVar] = {}
        self.scatter_variation_bar = ttk.Frame(self.batch_scatter_subtab)
        self.scatter_variation_bar.pack(fill=tk.X, padx=4, pady=(2, 0))
        self._scatter_variation_inner = ttk.Frame(self.scatter_variation_bar)
        self._scatter_variation_inner.pack(fill=tk.X)

        self.scatter_file_notebook = ttk.Notebook(self.batch_scatter_subtab)
        self.scatter_file_notebook.pack(fill=tk.BOTH, expand=True)
        self.scatter_panels: Dict[str, ScatterLayoutPanel] = {}
        self.scatter_file_notebook.bind('<<NotebookTabChanged>>', self._on_scatter_notebook_tab_changed)

        self.variation_geom_var.trace_add('write', lambda *_: self._sync_variation_geom_widgets())
        self.file_listbox.bind('<<ListboxSelect>>', self._on_batch_file_list_select)

        self._rebuild_scatter_file_tabs()
        self._sync_variation_geom_widgets()

    def _maximize_main_window(self) -> None:
        try:
            self.root.state('zoomed')
        except tk.TclError:
            pass

    def scatter_panel_for_path(self, path: Path) -> Optional[ScatterLayoutPanel]:
        return self.scatter_panels.get(str(Path(path).resolve()))

    @property
    def scatter_panel(self) -> Optional[ScatterLayoutPanel]:
        """Scatter UI for the selected batch file (or the first file if none selected)."""
        if not self.available_files:
            return None
        cur = self.file_listbox.curselection()
        idx = int(cur[0]) if cur else 0
        if idx >= len(self.available_files):
            idx = 0
        return self.scatter_panel_for_path(self.available_files[idx])

    def _rebuild_scatter_file_tabs(self) -> None:
        if not getattr(self, 'scatter_file_notebook', None):
            return
        for w in self.scatter_file_notebook.winfo_children():
            w.destroy()
        self.scatter_panels.clear()
        self._rebuild_scatter_variation_checkboxes()
        if not self.available_files:
            f = ttk.Frame(self.scatter_file_notebook)
            ttk.Label(
                f,
                text='Load NDF files in General (Browse Dir, then Load Files, or Browse Files).',
                wraplength=880,
            ).pack(expand=True, padx=16, pady=24)
            self.scatter_file_notebook.add(f, text='(no files)')
            return
        for fp in self.available_files:
            key = str(fp.resolve())
            fr = ttk.Frame(self.scatter_file_notebook)
            panel = ScatterLayoutPanel(fr, self)
            panel.pack(fill=tk.BOTH, expand=True)
            name = fp.name
            if len(name) > 44:
                name = name[:41] + '…'
            self.scatter_file_notebook.add(fr, text=name)
            self.scatter_panels[key] = panel
            panel.load_from_ndf_path(fp, silent=True)
        self._sync_scatter_tab_to_file_list(force=True)
        self.sync_scatter_tab_radii()

    def _on_batch_file_list_select(self, _event: Optional[tk.Event] = None) -> None:
        self._update_cluster_anchor_min_hint()
        try:
            cur = self.file_listbox.curselection()
            if not cur:
                return
            idx = int(cur[0])
            n_files = len(self.available_files)
            if n_files and idx >= n_files:
                idx = 0
            prev = self._last_scatter_listbox_idx
            if prev is not None and idx == prev:
                return
            self._sync_scatter_tab_to_file_list()
        finally:
            self._schedule_state_save()

    def _sync_scatter_tab_to_file_list(self, *, force: bool = False) -> None:
        if not getattr(self, 'scatter_file_notebook', None):
            return
        tabs = self.scatter_file_notebook.tabs()
        if not tabs or not self.available_files:
            return
        n_files = len(self.available_files)
        if len(tabs) < n_files:
            return
        cur = self.file_listbox.curselection()
        if not cur:
            if not force:
                return
            idx = 0
        else:
            idx = int(cur[0])
            if idx >= n_files:
                idx = 0
        self._suppress_notebook_listbox_sync = True
        try:
            self.scatter_file_notebook.select(idx)
        except tk.TclError:
            pass
        finally:
            self._suppress_notebook_listbox_sync = False
        self._last_scatter_listbox_idx = idx

    def _on_scatter_notebook_tab_changed(self, _event: Optional[tk.Event] = None) -> None:
        if not self.available_files:
            return
        try:
            idx = self.scatter_file_notebook.index(self.scatter_file_notebook.select())
        except tk.TclError:
            return
        n_files = len(self.available_files)
        if idx < 0 or idx >= n_files:
            return  # preview tabs after source files: do not sync listbox
        self._last_scatter_listbox_idx = idx
        if getattr(self, '_suppress_notebook_listbox_sync', False):
            return
        self.file_listbox.selection_clear(0, tk.END)
        self.file_listbox.selection_set(idx)
        self.file_listbox.see(idx)

    def _clear_scatter_preview_tabs(self) -> None:
        """Remove appended preview tabs (after source file tabs); keeps source tabs intact."""
        nb = getattr(self, 'scatter_file_notebook', None)
        if not nb:
            return
        n_src = len(self.available_files)
        try:
            while nb.index('end') > n_src:
                nb.forget(nb.tabs()[-1])
        except tk.TclError:
            pass
        self.scatter_panels = {
            k: v for k, v in self.scatter_panels.items() if not str(k).startswith('__preview_')
        }
        self._rebuild_scatter_variation_checkboxes()

    def _rebuild_scatter_variation_checkboxes(self) -> None:
        """One checkbox per unique preview target radius (m); toggles tab visibility."""
        for w in self._scatter_variation_inner.winfo_children():
            w.destroy()
        self._scatter_variation_vars.clear()
        targets: List[float] = []
        for panel in self.scatter_panels.values():
            tm = getattr(panel, 'preview_target_m', None)
            if tm is not None:
                targets.append(float(tm))
        if not targets:
            return
        uniq = sorted({round(t, 6) for t in targets})
        row = ttk.Frame(self._scatter_variation_inner)
        row.pack(fill=tk.X)
        ttk.Label(row, text='Show cluster preview tabs (m):').pack(side=tk.LEFT, padx=(0, 8))
        for tm in uniq:
            var = tk.BooleanVar(value=True)
            self._scatter_variation_vars[tm] = var
            ttk.Checkbutton(
                row,
                text=f'{tm:g}',
                variable=var,
                command=self._apply_scatter_variation_visibility,
            ).pack(side=tk.LEFT, padx=4)

    def _apply_scatter_variation_visibility(self) -> None:
        nb = getattr(self, 'scatter_file_notebook', None)
        if not nb:
            return
        for key, panel in self.scatter_panels.items():
            if not str(key).startswith('__preview_'):
                continue
            tm = getattr(panel, 'preview_target_m', None)
            if tm is None:
                continue
            rk = round(float(tm), 6)
            var = self._scatter_variation_vars.get(rk)
            if var is None:
                continue
            fr = panel.master
            try:
                nb.tab(fr, state='normal' if var.get() else 'hidden')
            except tk.TclError:
                pass

    def _append_scatter_preview_tab(
        self,
        tab_text: str,
        project: ScatterProject,
        source_ndf_path: str,
        target_m: float,
    ) -> None:
        """Append a Scatter layout tab for a preview project (cluster variation preview)."""
        nb = getattr(self, 'scatter_file_notebook', None)
        if not nb:
            return
        fr = ttk.Frame(nb)
        panel = ScatterLayoutPanel(fr, self)
        panel.pack(fill=tk.BOTH, expand=True)
        panel.load_from_project(project, source_ndf_path, preview_target_m=target_m)
        name = tab_text
        if len(name) > 44:
            name = name[:41] + '…'
        nb.add(fr, text=name)
        seq = getattr(self, '_scatter_preview_tab_seq', 0) + 1
        self._scatter_preview_tab_seq = seq
        self.scatter_panels[f'__preview_{seq}'] = panel

    def _max_variation_target_m_from_ui(self) -> Optional[float]:
        targets = parse_target_sizes(self.variation_targets_text.get('1.0', tk.END))
        if not targets:
            return None
        return float(max(targets))

    def sync_scatter_tab_radii(self) -> None:
        """Set every Scatter tab's view radius to max target radius (m); each tab keeps its own R (m) circle."""
        if not getattr(self, 'scatter_panels', None) or not self.scatter_panels:
            return
        mv = self._max_variation_target_m_from_ui()
        if mv is None:
            disks: List[float] = []
            for panel in self.scatter_panels.values():
                disks.append(panel.effective_disk_radius_m())
            mv = max(disks) if disks else 150.0
        mv = max(10.0, float(mv))
        for panel in self.scatter_panels.values():
            panel.apply_shared_view_radius(mv)

    def _on_dialog_geometry_saved(self, key: str, geom: str) -> None:
        self._saved_dialog_geometry[key] = geom

    def _save_curve_dialog_presets(self, name: str, presets: Dict[str, float]) -> None:
        self._saved_dialog_substate[name] = dict(presets)
        self._schedule_state_save()

    def _curve_named_library_from_state(self, key: str) -> Dict[str, Dict[str, float]]:
        from .qty_curve_dialog import _normalize_named_preset_library

        raw = self._saved_dialog_substate.get(key)
        if not isinstance(raw, dict):
            return {}
        return _normalize_named_preset_library(raw)

    def _save_curve_named_library(self, key: str, library: Dict[str, Dict[str, float]]) -> None:
        from .qty_curve_dialog import _normalize_named_preset_library

        self._saved_dialog_substate[key] = _normalize_named_preset_library(library)
        self._schedule_state_save()

    def _apply_batch_listbox_selection_from_state(self, batch: Dict[str, Any]) -> None:
        """Restore listbox selection from batch state (indices preferred, then paths, else all)."""
        paths = self.available_files
        n = len(paths)
        self.file_listbox.selection_clear(0, tk.END)
        if n == 0:
            return

        idxs = batch.get('selected_indices')
        if isinstance(idxs, list):
            if len(idxs) == 0:
                return
            valid: List[int] = []
            for raw in idxs:
                try:
                    ii = int(raw)
                except (TypeError, ValueError):
                    continue
                if 0 <= ii < n:
                    valid.append(ii)
            if valid:
                for i in valid:
                    self.file_listbox.selection_set(i)
                return

        sel_raw = batch.get('selected_files')
        if isinstance(sel_raw, list):
            if len(sel_raw) == 0:
                return
            want = {Path(s).resolve() for s in sel_raw if isinstance(s, str) and s.strip()}
            for i, p in enumerate(paths):
                if p in want:
                    self.file_listbox.selection_set(i)
            if self.file_listbox.curselection():
                return

        self.file_listbox.selection_set(0, tk.END)

    def _serialize_variation_curves(self) -> Dict[str, Any]:
        return {
            'param_qty': {k: list(v) for k, v in self._variation_group_param_qty_curve.items()},
            'call_qty': {k: list(v) for k, v in self._variation_group_call_qty_curve.items()},
            'param_radius_falloff': {
                k: list(v) for k, v in self._variation_group_param_radius_falloff_curve.items()
            },
            'call_radius_falloff': {
                k: list(v) for k, v in self._variation_group_call_radius_falloff_curve.items()
            },
        }

    def _serialize_variation_group_ui(self) -> Dict[str, Any]:
        return {
            k: {'size': bool(sz.get()), 'count': bool(ct.get())}
            for k, (sz, ct) in self._variation_group_toggle_vars.items()
        }

    def _apply_saved_variation_group_ui(self, blob: Any) -> None:
        if not isinstance(blob, dict):
            return
        for k, row in blob.items():
            if k not in self._variation_group_toggle_vars:
                continue
            if not isinstance(row, dict):
                continue
            sz, ct = self._variation_group_toggle_vars[k]
            if 'size' in row:
                sz.set(bool(row['size']))
            if 'count' in row:
                ct.set(bool(row['count']))

    def _apply_saved_variation_curves(self, blob: Any) -> None:
        if not isinstance(blob, dict):
            return
        targets = self._parsed_target_radii_m()
        n_tgt = max(len(targets), 1)
        pq = blob.get('param_qty')
        if isinstance(pq, dict):
            for k, vals in pq.items():
                if k not in self._variation_group_param_qty_curve:
                    continue
                if not isinstance(vals, list) or not vals:
                    continue
                self._variation_group_param_qty_curve[k] = self._curve_aligned_to_targets(
                    [float(x) for x in vals],
                    n_tgt,
                )[:]
        cq = blob.get('call_qty')
        if isinstance(cq, dict):
            for k, vals in cq.items():
                if k not in self._variation_group_call_qty_curve:
                    continue
                if not isinstance(vals, list) or not vals:
                    continue
                self._variation_group_call_qty_curve[k] = self._curve_aligned_to_targets(
                    [float(x) for x in vals],
                    n_tgt,
                )[:]
        prf = blob.get('param_radius_falloff')
        if isinstance(prf, dict):
            for k, vals in prf.items():
                if k not in self._variation_group_param_radius_falloff_curve:
                    continue
                if not isinstance(vals, list) or not vals:
                    continue
                self._variation_group_param_radius_falloff_curve[k] = self._curve_aligned_radius_falloff(
                    [float(x) for x in vals],
                )[:]
        crf = blob.get('call_radius_falloff')
        if isinstance(crf, dict):
            for k, vals in crf.items():
                if k not in self._variation_group_call_radius_falloff_curve:
                    continue
                if not isinstance(vals, list) or not vals:
                    continue
                self._variation_group_call_radius_falloff_curve[k] = self._curve_aligned_radius_falloff(
                    [float(x) for x in vals],
                )[:]

    def _sync_sliders_from_curves_after_restore(self) -> None:
        for k in self._variation_group_toggle_vars:
            pq = self._variation_group_param_qty_curve.get(k)
            if pq and k in self._variation_group_count_scale_vars:
                try:
                    self._variation_group_count_scale_vars[k].set(sum(pq) / len(pq))
                except tk.TclError:
                    pass
            cq = self._variation_group_call_qty_curve.get(k)
            if cq and k in self._variation_group_call_scale_vars:
                try:
                    self._variation_group_call_scale_vars[k].set(sum(cq) / len(cq))
                except tk.TclError:
                    pass

    def _apply_saved_state(self, data: Dict[str, Any]) -> None:
        if not data or data.get('version', 0) < 1:
            return
        dg = data.get('dialog_geometry')
        if isinstance(dg, dict):
            self._saved_dialog_geometry = {
                str(k): str(v).strip()
                for k, v in dg.items()
                if isinstance(k, str) and isinstance(v, str) and str(v).strip()
            }
        else:
            self._saved_dialog_geometry = {}
        ds = data.get('dialog_substate')
        self._saved_dialog_substate = {}
        if isinstance(ds, dict):
            gc = ds.get('group_curves_multiedit_checks')
            if isinstance(gc, dict):
                self._saved_dialog_substate['group_curves_multiedit_checks'] = {
                    str(k): bool(v) for k, v in gc.items() if isinstance(k, str)
                }
            for name in ('qty_curve_presets', 'radius_falloff_presets'):
                p = ds.get(name)
                if isinstance(p, dict):
                    out: Dict[str, float] = {}
                    flat = p.get('flat')
                    end = p.get('end')
                    bo = p.get('bottom_out')
                    if isinstance(flat, (int, float)):
                        out['flat'] = float(flat)
                    if isinstance(end, (int, float)):
                        out['end'] = float(end)
                    if isinstance(bo, (int, float)):
                        out['bottom_out'] = float(bo)
                    if out:
                        self._saved_dialog_substate[name] = out
            for lib_key in ('qty_curve_named_presets', 'radius_falloff_named_presets'):
                lib = ds.get(lib_key)
                if isinstance(lib, dict):
                    from .qty_curve_dialog import _normalize_named_preset_library

                    cleaned = _normalize_named_preset_library(lib)
                    if cleaned:
                        self._saved_dialog_substate[lib_key] = cleaned
        geom = data.get('geometry')
        if isinstance(geom, str) and geom.strip():
            try:
                self.root.geometry(geom.strip())
            except tk.TclError:
                pass
        tab = data.get('notebook_tab')
        if isinstance(tab, int) and 0 <= tab < self.notebook.index('end'):
            try:
                self.notebook.select(tab)
            except tk.TclError:
                pass

        ed = data.get('editor_file')
        if isinstance(ed, str) and ed.strip():
            self.file_var.set(ed.strip())

        batch = data.get('batch')
        if isinstance(batch, dict):
            d = batch.get('directory')
            if isinstance(d, str):
                self.dir_var.set(d)
            if 'include_declaration' in batch:
                self.batch_include_declaration_var.set(bool(batch['include_declaration']))
            bod = batch.get('batch_output_dir')
            if isinstance(bod, str) and bod.strip():
                self.batch_output_dir_var.set(bod.strip())

            files_raw = batch.get('files')
            if isinstance(files_raw, list) and files_raw:
                paths = []
                for p in files_raw:
                    if not isinstance(p, str) or not p.strip():
                        continue
                    pp = Path(p)
                    if pp.is_file():
                        paths.append(pp.resolve())
                if paths:
                    self.available_files = paths
                    self.file_listbox.delete(0, tk.END)
                    for p in paths:
                        self.file_listbox.insert(tk.END, p.name)
                    self._apply_batch_listbox_selection_from_state(batch)

        var = data.get('variation')
        if isinstance(var, dict):
            if isinstance(var.get('source_m'), str):
                self.variation_source_m_var.set(var['source_m'])
            if isinstance(var.get('rootname'), str):
                self.variation_rootname_var.set(var['rootname'])
            if isinstance(var.get('template'), str):
                self.variation_template_var.set(var['template'])
            if 'overwrite' in var:
                self.variation_overwrite_var.set(bool(var['overwrite']))
            txt = var.get('targets_text')
            if isinstance(txt, str):
                self.variation_targets_text.delete('1.0', tk.END)
                self.variation_targets_text.insert('1.0', txt)
            if isinstance(var.get('variation_geom'), str) and var['variation_geom'] in ('param', 'cluster'):
                self.variation_geom_var.set(var['variation_geom'])
            elif var.get('cluster_mode'):
                self.variation_geom_var.set('cluster')
            else:
                self.variation_geom_var.set('param')
            wm = var.get('wait_max_s')
            if isinstance(wm, (int, float)):
                self.variation_wait_max_var.set(float(wm))
        self._update_batch_param_status_label()
        self._sync_variation_geom_widgets()
        self._rebuild_scatter_file_tabs()
        if isinstance(batch, dict) and self.available_files:
            files_raw = batch.get('files')
            if isinstance(files_raw, list) and files_raw:
                self._apply_batch_listbox_selection_from_state(batch)
        if self.available_files:
            self._refresh_variation_effect_groups(silent=True)
            self._apply_saved_variation_group_ui(data.get('variation_group_ui'))
            self._apply_saved_variation_curves(data.get('variation_curves'))
            self._sync_sliders_from_curves_after_restore()
            self._update_batch_param_status_label()
        if isinstance(batch, dict) and self.available_files:
            fr = batch.get('files')
            if isinstance(fr, list) and fr:
                self.root.after_idle(
                    lambda b=batch: self._apply_batch_listbox_selection_from_state(b),
                )

    def _qty_curve_dialog_kwargs(self) -> Dict[str, Any]:
        p = self._saved_dialog_substate.get('qty_curve_presets') or {}
        out: Dict[str, Any] = {
            'saved_geometry': self._saved_dialog_geometry.get('qty_curve'),
            'on_geometry_save': lambda g: self._on_dialog_geometry_saved('qty_curve', g),
            'on_presets_save': lambda d: self._save_curve_dialog_presets('qty_curve_presets', d),
            'named_presets': self._curve_named_library_from_state('qty_curve_named_presets'),
            'on_named_library_save': lambda d: self._save_curve_named_library('qty_curve_named_presets', d),
        }
        if isinstance(p, dict):
            if isinstance(p.get('flat'), (int, float)):
                out['preset_flat'] = float(p['flat'])
            if isinstance(p.get('end'), (int, float)):
                out['preset_end'] = float(p['end'])
            if isinstance(p.get('bottom_out'), (int, float)):
                out['preset_bottom_out_m'] = float(p['bottom_out'])
        return out

    def _radius_falloff_dialog_kwargs(self) -> Dict[str, Any]:
        p = self._saved_dialog_substate.get('radius_falloff_presets') or {}
        out: Dict[str, Any] = {
            'saved_geometry': self._saved_dialog_geometry.get('radius_falloff'),
            'on_geometry_save': lambda g: self._on_dialog_geometry_saved('radius_falloff', g),
            'on_presets_save': lambda d: self._save_curve_dialog_presets('radius_falloff_presets', d),
            'named_presets': self._curve_named_library_from_state('radius_falloff_named_presets'),
            'on_named_library_save': lambda d: self._save_curve_named_library('radius_falloff_named_presets', d),
        }
        if isinstance(p, dict):
            if isinstance(p.get('flat'), (int, float)):
                out['preset_flat'] = float(p['flat'])
            if isinstance(p.get('end'), (int, float)):
                out['preset_end'] = float(p['end'])
            if isinstance(p.get('bottom_out'), (int, float)):
                out['preset_bottom_out_r_norm'] = float(p['bottom_out'])
        return out

    def _save_state(self) -> None:
        try:
            tab = self.notebook.index(self.notebook.select())
        except tk.TclError:
            tab = 0
        batch_files = [str(p) for p in self.available_files]
        selected = self.get_selected_files()
        selected_str = [str(p) for p in selected]
        payload: Dict[str, Any] = {
            'geometry': self.root.geometry(),
            'notebook_tab': int(tab),
            'editor_file': self.file_var.get().strip(),
            'batch': {
                'directory': self.dir_var.get().strip(),
                'include_declaration': self.batch_include_declaration_var.get(),
                'batch_output_dir': self.batch_output_dir_var.get().strip(),
                'files': batch_files,
                'selected_files': selected_str,
                'selected_indices': [int(i) for i in self.file_listbox.curselection()],
            },
            'variation': {
                'source_m': self.variation_source_m_var.get().strip(),
                'targets_text': self.variation_targets_text.get('1.0', tk.END).rstrip(),
                'rootname': self.variation_rootname_var.get().strip(),
                'template': self.variation_template_var.get().strip(),
                'overwrite': self.variation_overwrite_var.get(),
                'variation_geom': self.variation_geom_var.get(),
                'wait_max_s': self.variation_wait_max_var.get(),
            },
            'variation_curves': self._serialize_variation_curves(),
            'variation_group_ui': self._serialize_variation_group_ui(),
            'dialog_geometry': dict(self._saved_dialog_geometry),
            'dialog_substate': dict(self._saved_dialog_substate),
        }
        save_state(payload)

    def _schedule_state_save(self) -> None:
        aid = getattr(self, '_state_save_after_id', None)
        if aid is not None:
            try:
                self.root.after_cancel(aid)
            except tk.TclError:
                pass
        self._state_save_after_id = self.root.after(300, self._flush_state_save)

    def _flush_state_save(self) -> None:
        self._state_save_after_id = None
        try:
            self._save_state()
        except Exception:
            pass

    def _on_close(self) -> None:
        try:
            aid = getattr(self, '_state_save_after_id', None)
            if aid is not None:
                try:
                    self.root.after_cancel(aid)
                except tk.TclError:
                    pass
                self._state_save_after_id = None
            self._save_state()
        except Exception:
            pass
        self.root.destroy()

    def browse_file(self) -> None:
        file_path = filedialog.askopenfilename(
            title='Select FX NDF File',
            filetypes=[('NDF Files', '*.ndf')],
        )
        if file_path:
            self.file_var.set(file_path)

    def load_file(self) -> None:
        file_path = Path(self.file_var.get())
        if not file_path.exists():
            messagebox.showerror('Error', f'File does not exist:\n{file_path}')
            return
        try:
            self.parsed_root = parse_ndf_file(file_path)
            self.current_file = file_path
            # Always prompt for namespace update
            self.prompt_namespace_on_load()
            self.refresh_tree()
        except Exception as exc:
            messagebox.showerror('Parse Error', str(exc))

    def save_file(self) -> None:
        if not self.current_file or not self.parsed_root:
            messagebox.showwarning('No File', 'Load a file before saving.')
            return
        try:
            write_ndf_file(self.current_file, self.parsed_root)
            messagebox.showinfo('Saved', f'Saved changes to:\n{self.current_file}')
        except Exception as exc:
            messagebox.showerror('Save Error', str(exc))

    def refresh_tree(self, select_ref: Optional[Any] = None) -> None:
        self.tree.delete(*self.tree.get_children())
        self.tree_item_refs = {}
        self.tree_nodes = {}

        if not self.parsed_root:
            return

        root_node, node_map = build_tree(self.parsed_root)
        self.tree_nodes = node_map

        def add_tree_node(parent_item: str, node_id: str, depth: int) -> None:
            node = node_map[node_id]
            item = self.tree.insert(
                parent_item,
                'end',
                text=node.label,
                open=(depth < 2),
            )
            self.tree_item_refs[item] = node
            for child_id in node.children:
                add_tree_node(item, child_id, depth + 1)

        add_tree_node('', root_node.node_id, 0)

        if select_ref is not None:
            for item_id, node in self.tree_item_refs.items():
                if node.ref is select_ref:
                    self.tree.selection_set(item_id)
                    self.tree.see(item_id)
                    break

    def on_tree_select(self, event: Any) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        node = self.tree_item_refs.get(selection[0])
        if not node:
            return
        self.populate_properties(node)

    def populate_properties(self, node: TreeNode) -> None:
        self.properties_tree.delete(*self.properties_tree.get_children())
        self.property_refs = {}

        ref = node.ref
        title = f'Properties for {node.label}'

        if isinstance(ref, ndf.model.Object):
            for member_row in ref:
                value_text = format_value(member_row.v)
                item = self.properties_tree.insert('', 'end', text=member_row.member or '(unnamed)', values=(value_text,))
                self.property_refs[item] = member_row
        elif isinstance(ref, ndf.model.Map):
            for map_row in ref:
                key = strip_quotes(str(map_row.k)) if map_row.k is not None else '(nil)'
                value_text = format_value(map_row.v)
                item = self.properties_tree.insert('', 'end', text=key, values=(value_text,))
                self.property_refs[item] = map_row
        elif isinstance(ref, ndf.model.List):
            for idx, list_row in enumerate(ref):
                label = list_row.namespace or f'[{idx}]'
                value_text = format_value(list_row.v)
                item = self.properties_tree.insert('', 'end', text=label, values=(value_text,))
                self.property_refs[item] = list_row
        elif isinstance(ref, (ndf.model.MemberRow, ndf.model.MapRow, ndf.model.ListRow)):
            value_text = format_value(ref.v)
            label = '(value)'
            if isinstance(ref, ndf.model.MemberRow):
                label = ref.member or '(unnamed)'
            if isinstance(ref, ndf.model.MapRow):
                label = strip_quotes(str(ref.k)) if ref.k is not None else '(nil)'
            if isinstance(ref, ndf.model.ListRow):
                label = ref.namespace or '(unnamed)'
            item = self.properties_tree.insert('', 'end', text=label, values=(value_text,))
            self.property_refs[item] = ref
        else:
            title = 'No editable properties for this node.'

        self.property_info.config(text=title)
        self.value_var.set('')

    def on_property_select(self, event: Any) -> None:
        selection = self.properties_tree.selection()
        if not selection:
            return
        row = self.property_refs.get(selection[0])
        if not row:
            return
        self.value_var.set(format_value(row.v))

    def apply_property_value(self) -> None:
        selection = self.properties_tree.selection()
        if not selection:
            messagebox.showwarning('No Selection', 'Select a property to edit.')
            return
        row = self.property_refs.get(selection[0])
        if not row:
            return
        new_value_text = self.value_var.get().strip()
        if not new_value_text:
            messagebox.showwarning('No Value', 'Enter a value to apply.')
            return
        new_value = parse_value_input(new_value_text)
        row.v = new_value
        self.populate_properties(self.tree_item_refs[self.tree.selection()[0]])
        self.refresh_tree(select_ref=row)

    def browse_directory(self) -> None:
        directory = filedialog.askdirectory(
            initialdir=self.dir_var.get() or None,
            title='Select Directory with FX NDF Files',
        )
        if directory:
            self.dir_var.set(directory)

    def browse_files(self) -> None:
        file_paths = filedialog.askopenfilenames(
            title='Select FX NDF Files',
            filetypes=[('NDF Files', '*.ndf')],
        )
        if not file_paths:
            return
        files = [Path(file_path) for file_path in file_paths]
        self.file_listbox.delete(0, tk.END)
        for file_path in files:
            self.file_listbox.insert(tk.END, file_path.name)
        self.available_files = files
        self.file_listbox.selection_set(0, tk.END)
        self.log_message(f'Loaded {len(files)} file(s) from file picker')
        self._rebuild_scatter_file_tabs()
        self._refresh_variation_effect_groups(silent=True)

    def load_files(self) -> None:
        directory = Path(self.dir_var.get())
        if not directory.exists():
            messagebox.showerror('Error', f'Directory does not exist:\n{directory}')
            return
        files = find_fx_files(directory, '*.ndf')
        if not files:
            messagebox.showinfo('No Files', f'No NDF files found in:\n{directory}')
            return
        self.file_listbox.delete(0, tk.END)
        for file_path in files:
            self.file_listbox.insert(tk.END, file_path.name)
        self.available_files = files
        self.file_listbox.selection_set(0, tk.END)
        self.log_message(f'Loaded {len(files)} file(s) from {directory}')
        self._rebuild_scatter_file_tabs()
        self._refresh_variation_effect_groups(silent=True)

    def select_all_files(self) -> None:
        self.file_listbox.selection_set(0, tk.END)
        self._schedule_state_save()

    def clear_selection(self) -> None:
        self.file_listbox.selection_clear(0, tk.END)
        self._schedule_state_save()

    def resolved_batch_output_dir(self) -> Path:
        """Resolved output folder for size variations; created if missing."""
        raw = self.batch_output_dir_var.get().strip()
        p = Path(_DEFAULT_BATCH_OUTPUT_DIR) if not raw else Path(raw).expanduser()
        p = p.resolve()
        p.mkdir(parents=True, exist_ok=True)
        return p

    def browse_batch_output_dir(self) -> None:
        cur = self.batch_output_dir_var.get().strip()
        initial = cur if cur and Path(cur).expanduser().is_dir() else str(_DEFAULT_BATCH_OUTPUT_DIR)
        d = filedialog.askdirectory(
            initialdir=initial,
            title='Select variation output folder',
        )
        if d:
            self.batch_output_dir_var.set(d)

    def open_batch_output_folder(self) -> None:
        """Open the configured variation output directory (default: tools/fx_editor/out)."""
        try:
            folder = self.resolved_batch_output_dir()
        except OSError as exc:
            messagebox.showerror('Output folder', str(exc))
            return
        try:
            system = platform.system()
            if system == 'Windows':
                os.startfile(str(folder))  # type: ignore[attr-defined]
            elif system == 'Darwin':
                subprocess.Popen(['open', str(folder)])
            else:
                subprocess.Popen(['xdg-open', str(folder)])
        except Exception as exc:
            messagebox.showerror('Open folder', str(exc))

    def _batch_anchor_hint_source_path(self) -> Optional[Path]:
        """First NDF used for cluster anchor min hint; stable if listbox focus moves (see ``exportselection``)."""
        if not getattr(self, 'available_files', None):
            return None
        sel = self.get_selected_files()
        if sel:
            return sel[0]
        last = getattr(self, '_last_scatter_listbox_idx', None)
        if last is not None and 0 <= last < len(self.available_files):
            return self.available_files[last]
        return self.available_files[0]

    def get_selected_files(self) -> List[Path]:
        if not hasattr(self, 'available_files'):
            return []
        selected_indices = self.file_listbox.curselection()
        return [self.available_files[int(i)] for i in selected_indices]

    def clear_results(self) -> None:
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state=tk.DISABLED)

    def log_message(self, message: str) -> None:
        logging.getLogger('fx_editor.ui').info('%s', message)
        self.results_text.config(state=tk.NORMAL)
        self.results_text.insert(tk.END, message + '\n')
        self.results_text.see(tk.END)
        self.results_text.config(state=tk.DISABLED)
        self.root.update_idletasks()

    def copy_results_text_to_clipboard(self) -> None:
        """Copy the General tab Results text area to the system clipboard."""
        txt = self.results_text.get('1.0', tk.END)
        self.root.clipboard_clear()
        self.root.clipboard_append(txt)
        self.root.update_idletasks()

    def open_debug_log_window(self) -> None:
        """Show ring-buffer + stderr-mirrored debug lines (radius falloff, scatter preview, etc.)."""
        existing = getattr(self, '_debug_log_toplevel', None)
        if existing is not None:
            try:
                if existing.winfo_exists():
                    existing.deiconify()
                    existing.lift()
                    tw = getattr(self, '_debug_log_text', None)
                    if tw is not None:
                        tw.config(state=tk.NORMAL)
                        tw.delete('1.0', tk.END)
                        tw.insert('1.0', get_debug_log_buffer_text())
                        tw.config(state=tk.DISABLED)
                    return
            except tk.TclError:
                pass

        w = tk.Toplevel(self.root)
        self._debug_log_toplevel = w
        w.title('FX Editor — debug log')
        w.geometry('920x620')
        top = ttk.Frame(w, padding=8)
        top.pack(fill=tk.BOTH, expand=True)
        bar = ttk.Frame(top)
        bar.pack(fill=tk.X, pady=(0, 6))

        def _reload() -> None:
            self._debug_log_text.config(state=tk.NORMAL)
            self._debug_log_text.delete('1.0', tk.END)
            self._debug_log_text.insert('1.0', get_debug_log_buffer_text())
            self._debug_log_text.config(state=tk.DISABLED)

        def _copy() -> None:
            txt = get_debug_log_buffer_text()
            self.root.clipboard_clear()
            self.root.clipboard_append(txt)

        ttk.Button(bar, text='Refresh', command=_reload).pack(side=tk.LEFT, padx=(0, 6))
        ttk.Button(bar, text='Copy all', command=_copy).pack(side=tk.LEFT, padx=(0, 6))
        ttk.Button(bar, text='Clear buffer', command=lambda: (clear_debug_log_buffer(), _reload())).pack(
            side=tk.LEFT,
            padx=(0, 6),
        )
        ttk.Button(bar, text='Close', command=w.destroy).pack(side=tk.RIGHT)
        ttk.Label(
            bar,
            text='Mirror of stderr; per-burst lines need FX_EDITOR_LOG_LEVEL=DEBUG',
            font=('TkDefaultFont', 8),
        ).pack(side=tk.LEFT, padx=(12, 0))

        self._debug_log_text = scrolledtext.ScrolledText(top, wrap=tk.WORD, height=28, state=tk.DISABLED)
        self._debug_log_text.pack(fill=tk.BOTH, expand=True)
        _reload()

    def _batch_scale_kwargs(self) -> Dict[str, Any]:
        """Keyword arguments for process_file / write_scaled_copy / PreviewWindow batch scaling.

        ``scale_size`` / ``scale_count`` only gate :func:`scale_size_params` (NamedParams + declaration
        defaults). Cluster mode still runs :func:`emit_scatter_into_actions` with positions from
        ``target_m`` regardless of these flags.
        """
        named = self._named_flags_for_variations()
        if named is None:
            named = {}
        if self._variation_group_toggle_vars:
            scale_size = any(sz.get() for sz, _ in self._variation_group_toggle_vars.values())
            scale_count = any(ct.get() for _sz, ct in self._variation_group_toggle_vars.values())
        else:
            scale_size = False
            scale_count = False
        src_m = self._parse_positive_float(self.variation_source_m_var.get())
        targets_txt = self.variation_targets_text.get('1.0', tk.END)
        if src_m is not None:
            call_smin, call_smax = effect_call_batch_scale_bounds(src_m, targets_txt)
        else:
            call_smin, call_smax = 1.0, 1.0
        return {
            'allowed_names': None,
            'scale_size': scale_size,
            'scale_count': scale_count,
            'include_declaration_params': self.batch_include_declaration_var.get(),
            'effect_named_flags': named,
            'effect_call_batch_scale_min': call_smin,
            'effect_call_batch_scale_max': call_smax,
        }

    def _parsed_target_radii_m(self) -> List[float]:
        return parse_target_sizes(self.variation_targets_text.get('1.0', tk.END))

    def _any_qty_curve_non_full(self) -> bool:
        for lst in self._variation_group_param_qty_curve.values():
            if any(abs(x - 100.0) > 1e-6 for x in lst):
                return True
        for lst in self._variation_group_call_qty_curve.values():
            if any(abs(x - 100.0) > 1e-6 for x in lst):
                return True
        return False

    def _any_radius_falloff_curve_non_full(self) -> bool:
        for lst in self._variation_group_param_radius_falloff_curve.values():
            if any(abs(x - 100.0) > 1e-6 for x in lst):
                return True
        for lst in self._variation_group_call_radius_falloff_curve.values():
            if any(abs(x - 100.0) > 1e-6 for x in lst):
                return True
        return False

    def _effect_count_pct_for_target(
        self,
        target_m: float,
        targets: List[float],
    ) -> Optional[Dict[str, float]]:
        if not self._cached_effect_groups:
            return None
        return merge_effect_qty_pct_for_target_radius(
            self._cached_effect_groups,
            self._variation_group_param_qty_curve,
            target_m,
            targets,
        )

    def _effect_call_pct_for_target(
        self,
        target_m: float,
        targets: List[float],
    ) -> Optional[Dict[str, float]]:
        if not self._cached_effect_groups:
            return None
        return merge_effect_qty_pct_for_target_radius(
            self._cached_effect_groups,
            self._variation_group_call_qty_curve,
            target_m,
            targets,
        )

    def _param_radius_falloff_by_vfx(self) -> Optional[Dict[str, List[float]]]:
        if not self._cached_effect_groups:
            return None
        return merge_effect_radius_falloff_curves(
            self._cached_effect_groups,
            self._variation_group_param_radius_falloff_curve,
        )

    def _call_radius_falloff_by_vfx(self) -> Optional[Dict[str, List[float]]]:
        if not self._cached_effect_groups:
            return None
        return merge_effect_radius_falloff_curves(
            self._cached_effect_groups,
            self._variation_group_call_radius_falloff_curve,
        )

    def _variation_scaling_requested(self) -> bool:
        """True if batch scaling is active: Size/Count toggles, or any Param/Call qty curve not 100%."""
        if self._any_group_size_or_count():
            return True
        if self._any_qty_curve_non_full():
            return True
        return self._any_radius_falloff_curve_non_full()

    def _any_group_size_or_count(self) -> bool:
        if not self._variation_group_toggle_vars:
            return False
        return any(
            sz.get() or ct.get()
            for sz, ct in self._variation_group_toggle_vars.values()
        )

    def _update_batch_param_status_label(self) -> None:
        dec = 'on' if self.batch_include_declaration_var.get() else 'off'
        if self._variation_group_toggle_vars:
            sz = any(sz.get() for sz, _ in self._variation_group_toggle_vars.values())
            ct = any(ct.get() for _sz, ct in self._variation_group_toggle_vars.values())
            np = (
                f'NamedParams: size-like {"on" if sz else "off"}, '
                f'quantity-like {"on" if ct else "off"} (per pattern below).'
            )
        else:
            np = 'NamedParams: refresh effect groups below after loading files.'
        cluster_extra = ''
        if self.variation_geom_var.get() == 'cluster':
            cluster_extra = (
                ' Cluster scatter (positions + burst rows) always uses target radius (m); '
                'Size/Count only scale effect NamedParams, not Mobile layout.'
            )
        self.batch_param_status_label.config(
            text=(
                f'Batch: declaration Params {dec}. {np}{cluster_extra}'
            ),
        )

    def _sync_variation_geom_widgets(self) -> None:
        cluster = self.variation_geom_var.get() == 'cluster'
        st = tk.NORMAL if cluster else tk.DISABLED
        for w in getattr(self, '_cluster_mode_spinboxes', ()):
            try:
                w.configure(state=st)
            except tk.TclError:
                pass
        self._update_cluster_anchor_min_hint()
        self._update_batch_param_status_label()

    def _variation_select_all_size(self) -> None:
        for sz, _ct in self._variation_group_toggle_vars.values():
            sz.set(True)
        self._update_batch_param_status_label()

    def _variation_clear_all_size(self) -> None:
        for sz, _ct in self._variation_group_toggle_vars.values():
            sz.set(False)
        self._update_batch_param_status_label()

    def _variation_select_all_count(self) -> None:
        for _sz, ct in self._variation_group_toggle_vars.values():
            ct.set(True)
        self._update_batch_param_status_label()

    def _variation_clear_all_count(self) -> None:
        for _sz, ct in self._variation_group_toggle_vars.values():
            ct.set(False)
        self._update_batch_param_status_label()

    def _refresh_variation_effect_groups(self, *, silent: bool = False) -> None:
        for w in self._variation_group_checks_frame.winfo_children():
            w.destroy()
        self._variation_group_toggle_vars.clear()
        self._variation_group_count_scale_vars.clear()
        self._variation_group_call_scale_vars.clear()
        self._variation_group_param_qty_curve.clear()
        self._variation_group_call_qty_curve.clear()
        self._variation_group_param_radius_falloff_curve.clear()
        self._variation_group_call_radius_falloff_curve.clear()
        self._cached_effect_groups = []
        sel = self.get_selected_files()
        if not sel and self.available_files:
            sel = list(self.available_files)
        if not sel:
            if not silent:
                messagebox.showwarning('No file', 'Select at least one file in the list first.')
            return
        per_file: List[Any] = []
        errors: List[str] = []
        for path in sel:
            try:
                text = path.read_text(encoding='utf-8')
                root = ndf.convert(text)
                if not isinstance(root, ndf.model.List):
                    raise ValueError('Invalid NDF root')
                per_file.append(analyze_effect_groups(root))
            except Exception as exc:
                errors.append(f'{path.name}: {exc}')
        if not per_file:
            messagebox.showerror(
                'Effect groups',
                'Could not parse any selected file:\n\n' + '\n'.join(errors) if errors else '(none)',
            )
            return
        if errors:
            messagebox.showwarning(
                'Effect groups (partial)',
                'Merged groups from readable files. Skipped:\n\n' + '\n'.join(errors),
            )
        groups = merge_effect_group_rows(per_file)
        self._cached_effect_groups = groups
        if not groups:
            ttk.Label(self._variation_group_checks_frame, text='(No effect groups found.)').pack(anchor=tk.W)
            self._update_batch_param_status_label()
            return
        targets = self._parsed_target_radii_m()
        curve_len = max(len(targets), 1)
        for g in groups:
            k = effect_group_key(g)
            sz = tk.BooleanVar(value=False)
            ct = tk.BooleanVar(value=False)
            pct = tk.DoubleVar(value=100.0)
            call_pct = tk.DoubleVar(value=100.0)
            self._variation_group_toggle_vars[k] = (sz, ct)
            self._variation_group_count_scale_vars[k] = pct
            self._variation_group_call_scale_vars[k] = call_pct
            self._variation_group_param_qty_curve[k] = [100.0] * curve_len
            self._variation_group_call_qty_curve[k] = [100.0] * curve_len
            self._variation_group_param_radius_falloff_curve[k] = [100.0] * RADIUS_FALLOFF_SAMPLES
            self._variation_group_call_radius_falloff_curve[k] = [100.0] * RADIUS_FALLOFF_SAMPLES
            row = ttk.Frame(self._variation_group_checks_frame)
            row.pack(fill=tk.X, pady=1)
            lab = f'×{g.count}  {g.effects}'
            if len(lab) > 92:
                lab = lab[:89] + '…'
            ttk.Label(row, text=lab, wraplength=520).pack(side=tk.LEFT, padx=(0, 5))
            ttk.Checkbutton(
                row,
                text='Size',
                variable=sz,
                command=self._update_batch_param_status_label,
            ).pack(side=tk.LEFT, padx=3)
            ttk.Checkbutton(
                row,
                text='Count',
                variable=ct,
                command=self._update_batch_param_status_label,
            ).pack(side=tk.LEFT, padx=3)
            ttk.Label(row, text='Param Qty %').pack(side=tk.LEFT, padx=(8, 2))
            pct_lbl = ttk.Label(row, text='100%', width=5)

            def _sync_pct_lab(*_a: Any, lbl: ttk.Label = pct_lbl, var: tk.DoubleVar = pct) -> None:
                try:
                    lbl.config(text=f'{float(var.get()):.0f}%')
                except tk.TclError:
                    pass

            pct.trace_add('write', lambda *_a, fn=_sync_pct_lab: fn())

            def _on_param_scale(_v: str, *, kk: str = k) -> None:
                self._sync_param_curve_from_slider(kk)
                self._update_batch_param_status_label()

            ttk.Scale(
                row,
                from_=0.0,
                to=100.0,
                orient=tk.HORIZONTAL,
                length=120,
                variable=pct,
                command=_on_param_scale,
            ).pack(side=tk.LEFT, padx=2)
            pct_lbl.pack(side=tk.LEFT, padx=(0, 2))
            _sync_pct_lab()
            ttk.Button(
                row,
                text='Curve…',
                width=7,
                command=lambda kk=k: self._open_param_qty_curve(kk),
            ).pack(side=tk.LEFT, padx=(0, 2))
            ttk.Button(
                row,
                text='Radius falloff…',
                width=14,
                command=lambda kk=k: self._open_param_radius_falloff_curve(kk),
            ).pack(side=tk.LEFT, padx=(0, 4))
            ttk.Label(row, text='Call Qty %').pack(side=tk.LEFT, padx=(8, 2))
            call_lbl = ttk.Label(row, text='100%', width=5)

            def _sync_call_lab(*_a: Any, lbl: ttk.Label = call_lbl, var: tk.DoubleVar = call_pct) -> None:
                try:
                    lbl.config(text=f'{float(var.get()):.0f}%')
                except tk.TclError:
                    pass

            call_pct.trace_add('write', lambda *_a, fn=_sync_call_lab: fn())

            def _on_call_scale(_v: str, *, kk: str = k) -> None:
                self._sync_call_curve_from_slider(kk)
                self._update_batch_param_status_label()

            ttk.Scale(
                row,
                from_=0.0,
                to=100.0,
                orient=tk.HORIZONTAL,
                length=120,
                variable=call_pct,
                command=_on_call_scale,
            ).pack(side=tk.LEFT, padx=2)
            call_lbl.pack(side=tk.LEFT, padx=(0, 2))
            _sync_call_lab()
            ttk.Button(
                row,
                text='Curve…',
                width=7,
                command=lambda kk=k: self._open_call_qty_curve(kk),
            ).pack(side=tk.LEFT, padx=(0, 2))
            ttk.Button(
                row,
                text='Radius falloff…',
                width=14,
                command=lambda kk=k: self._open_call_radius_falloff_curve(kk),
            ).pack(side=tk.LEFT, padx=(0, 4))
        self._update_batch_param_status_label()

    def _named_flags_for_variations(self) -> Optional[Dict[str, Dict[str, bool]]]:
        if not self._cached_effect_groups or not self._variation_group_toggle_vars:
            return None
        toggles = {key: (a.get(), b.get()) for key, (a, b) in self._variation_group_toggle_vars.items()}
        return effect_named_flags_from_group_toggles(self._cached_effect_groups, toggles)

    @staticmethod
    def _curve_aligned_to_targets(curve: List[float], n: int) -> List[float]:
        if n <= 0:
            return []
        if len(curve) >= n:
            return curve[:n]
        return curve + [100.0] * (n - len(curve))

    def _sync_param_curve_from_slider(self, key: str) -> None:
        if key not in self._variation_group_count_scale_vars:
            return
        try:
            v = float(self._variation_group_count_scale_vars[key].get())
        except tk.TclError:
            return
        targets = self._parsed_target_radii_m()
        n = max(len(targets), 1)
        self._variation_group_param_qty_curve[key] = [v] * n

    def _sync_call_curve_from_slider(self, key: str) -> None:
        if key not in self._variation_group_call_scale_vars:
            return
        try:
            v = float(self._variation_group_call_scale_vars[key].get())
        except tk.TclError:
            return
        targets = self._parsed_target_radii_m()
        n = max(len(targets), 1)
        self._variation_group_call_qty_curve[key] = [v] * n

    def _open_param_qty_curve(self, group_key: str) -> None:
        targets = self._parsed_target_radii_m()
        if not targets:
            messagebox.showwarning(
                'Target radii',
                'Enter at least one target radius in the Batch section (Target radii field).',
            )
            return
        n = len(targets)
        curve = self._curve_aligned_to_targets(
            self._variation_group_param_qty_curve.get(group_key, [100.0] * n),
            n,
        )

        def on_apply(new_vals: List[float]) -> None:
            self._variation_group_param_qty_curve[group_key] = new_vals[:]
            pv = self._variation_group_count_scale_vars.get(group_key)
            if pv is not None and new_vals:
                pv.set(sum(new_vals) / len(new_vals))
            self._update_batch_param_status_label()

        short = group_key if len(group_key) <= 72 else group_key[:69] + '…'
        open_qty_curve_dialog(
            self.root,
            title=f'Param Qty % — {short}',
            target_radii_m=targets,
            values=curve,
            on_apply=on_apply,
            **self._qty_curve_dialog_kwargs(),
        )

    def _open_call_qty_curve(self, group_key: str) -> None:
        targets = self._parsed_target_radii_m()
        if not targets:
            messagebox.showwarning(
                'Target radii',
                'Enter at least one target radius in the Batch section (Target radii field).',
            )
            return
        n = len(targets)
        curve = self._curve_aligned_to_targets(
            self._variation_group_call_qty_curve.get(group_key, [100.0] * n),
            n,
        )

        def on_apply(new_vals: List[float]) -> None:
            self._variation_group_call_qty_curve[group_key] = new_vals[:]
            cv = self._variation_group_call_scale_vars.get(group_key)
            if cv is not None and new_vals:
                cv.set(sum(new_vals) / len(new_vals))
            self._update_batch_param_status_label()

        short = group_key if len(group_key) <= 72 else group_key[:69] + '…'
        open_qty_curve_dialog(
            self.root,
            title=f'Call Qty % — {short}',
            target_radii_m=targets,
            values=curve,
            on_apply=on_apply,
            **self._qty_curve_dialog_kwargs(),
        )

    @staticmethod
    def _curve_aligned_radius_falloff(curve: List[float]) -> List[float]:
        n = RADIUS_FALLOFF_SAMPLES
        if len(curve) >= n:
            return curve[:n]
        return curve + [100.0] * (n - len(curve))

    def _open_param_radius_falloff_curve(self, group_key: str) -> None:
        n = RADIUS_FALLOFF_SAMPLES
        curve = self._curve_aligned_radius_falloff(
            self._variation_group_param_radius_falloff_curve.get(group_key, [100.0] * n),
        )

        def on_apply(new_vals: List[float]) -> None:
            self._variation_group_param_radius_falloff_curve[group_key] = new_vals[:]
            self._update_batch_param_status_label()

        short = group_key if len(group_key) <= 72 else group_key[:69] + '…'
        open_radius_falloff_curve_dialog(
            self.root,
            title=f'Param Qty — radius falloff — {short}',
            values=curve,
            on_apply=on_apply,
            **self._radius_falloff_dialog_kwargs(),
        )

    def _open_call_radius_falloff_curve(self, group_key: str) -> None:
        n = RADIUS_FALLOFF_SAMPLES
        curve = self._curve_aligned_radius_falloff(
            self._variation_group_call_radius_falloff_curve.get(group_key, [100.0] * n),
        )

        def on_apply(new_vals: List[float]) -> None:
            self._variation_group_call_radius_falloff_curve[group_key] = new_vals[:]
            self._update_batch_param_status_label()

        short = group_key if len(group_key) <= 72 else group_key[:69] + '…'
        open_radius_falloff_curve_dialog(
            self.root,
            title=f'Call Qty — radius falloff — {short}',
            values=curve,
            on_apply=on_apply,
            **self._radius_falloff_dialog_kwargs(),
        )

    def _open_group_curves_multiedit_dialog(self) -> None:
        open_group_curves_multiedit_dialog(self.root, self)

    def _open_param_qty_curve_for_keys(self, keys: List[str]) -> None:
        if not keys:
            return
        if len(keys) == 1:
            self._open_param_qty_curve(keys[0])
            return
        targets = self._parsed_target_radii_m()
        if not targets:
            messagebox.showwarning(
                'Target radii',
                'Enter at least one target radius in the Batch section (Target radii field).',
            )
            return
        n = len(targets)
        first = keys[0]
        curve = self._curve_aligned_to_targets(
            self._variation_group_param_qty_curve.get(first, [100.0] * n),
            n,
        )

        def on_apply(new_vals: List[float]) -> None:
            for k in keys:
                self._variation_group_param_qty_curve[k] = new_vals[:]
                pv = self._variation_group_count_scale_vars.get(k)
                if pv is not None and new_vals:
                    pv.set(sum(new_vals) / len(new_vals))
            self._update_batch_param_status_label()

        open_qty_curve_dialog(
            self.root,
            title=f'Param Qty % — {len(keys)} groups',
            target_radii_m=targets,
            values=curve,
            on_apply=on_apply,
            **self._qty_curve_dialog_kwargs(),
        )

    def _open_call_qty_curve_for_keys(self, keys: List[str]) -> None:
        if not keys:
            return
        if len(keys) == 1:
            self._open_call_qty_curve(keys[0])
            return
        targets = self._parsed_target_radii_m()
        if not targets:
            messagebox.showwarning(
                'Target radii',
                'Enter at least one target radius in the Batch section (Target radii field).',
            )
            return
        n = len(targets)
        first = keys[0]
        curve = self._curve_aligned_to_targets(
            self._variation_group_call_qty_curve.get(first, [100.0] * n),
            n,
        )

        def on_apply(new_vals: List[float]) -> None:
            for k in keys:
                self._variation_group_call_qty_curve[k] = new_vals[:]
                cv = self._variation_group_call_scale_vars.get(k)
                if cv is not None and new_vals:
                    cv.set(sum(new_vals) / len(new_vals))
            self._update_batch_param_status_label()

        open_qty_curve_dialog(
            self.root,
            title=f'Call Qty % — {len(keys)} groups',
            target_radii_m=targets,
            values=curve,
            on_apply=on_apply,
            **self._qty_curve_dialog_kwargs(),
        )

    def _open_param_radius_falloff_curve_for_keys(self, keys: List[str]) -> None:
        if not keys:
            return
        if len(keys) == 1:
            self._open_param_radius_falloff_curve(keys[0])
            return
        n = RADIUS_FALLOFF_SAMPLES
        first = keys[0]
        curve = self._curve_aligned_radius_falloff(
            self._variation_group_param_radius_falloff_curve.get(first, [100.0] * n),
        )

        def on_apply(new_vals: List[float]) -> None:
            for k in keys:
                self._variation_group_param_radius_falloff_curve[k] = new_vals[:]
            self._update_batch_param_status_label()

        open_radius_falloff_curve_dialog(
            self.root,
            title=f'Param Qty — radius falloff — {len(keys)} groups',
            values=curve,
            on_apply=on_apply,
            **self._radius_falloff_dialog_kwargs(),
        )

    def _open_call_radius_falloff_curve_for_keys(self, keys: List[str]) -> None:
        if not keys:
            return
        if len(keys) == 1:
            self._open_call_radius_falloff_curve(keys[0])
            return
        n = RADIUS_FALLOFF_SAMPLES
        first = keys[0]
        curve = self._curve_aligned_radius_falloff(
            self._variation_group_call_radius_falloff_curve.get(first, [100.0] * n),
        )

        def on_apply(new_vals: List[float]) -> None:
            for k in keys:
                self._variation_group_call_radius_falloff_curve[k] = new_vals[:]
            self._update_batch_param_status_label()

        open_radius_falloff_curve_dialog(
            self.root,
            title=f'Call Qty — radius falloff — {len(keys)} groups',
            values=curve,
            on_apply=on_apply,
            **self._radius_falloff_dialog_kwargs(),
        )

    def _update_cluster_anchor_min_hint(self) -> None:
        if not getattr(self, 'variation_geom_var', None):
            return
        if self.variation_geom_var.get() != 'cluster':
            self.variation_anchor_min_label.config(text='—')
            return
        path = self._batch_anchor_hint_source_path()
        if path is None:
            self.variation_anchor_min_label.config(text='—')
            return
        try:
            text = path.read_text(encoding='utf-8')
            parsed = ndf.convert(text)
            if not isinstance(parsed, ndf.model.List):
                self.variation_anchor_min_label.config(text='—')
                return
            t_min, _t_def_max = infer_anchor_bounds_from_parsed(parsed)
            self.variation_anchor_min_label.config(text=f'{t_min:.3g}s')
        except Exception:
            self.variation_anchor_min_label.config(text='—')

    def open_scatter_layout_dialog(self) -> None:
        from .scatter_dialog import open_scatter_layout_dialog as _go_scatter

        _go_scatter(self)

    def prompt_namespace_on_load(self) -> None:
        """Always prompt user to set/update namespace when loading a file."""
        if not self.parsed_root:
            return
        
        export_row = get_export_row(self.parsed_root)
        if not export_row or not export_row.namespace:
            messagebox.showwarning('No Namespace', 'No export namespace found in file.')
            return
        
        current_namespace = export_row.namespace
        filename = self.current_file.name if self.current_file else "unknown"
        
        # Always prompt for namespace update
        self.prompt_for_new_namespace(current_namespace, None)
    
    def prompt_for_new_namespace(self, current_namespace: str, suggested_namespace: Optional[str] = None) -> None:
        """Prompt user for a new namespace and update both namespace and filename.
        
        Args:
            current_namespace: The current namespace value
            suggested_namespace: Optional suggested namespace (unused, kept for compatibility)
        """
        # Create a simple dialog for namespace input
        dialog = tk.Toplevel(self.root)
        dialog.title('Set Namespace')
        dialog.geometry('600x220')
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f'+{x}+{y}')
        
        # Show current values
        current_filename = self.current_file.name if self.current_file else "unknown"
        info_text = f'Current namespace: {current_namespace}\nCurrent filename: {current_filename}'
        ttk.Label(
            dialog,
            text=info_text,
            font=('TkDefaultFont', 9),
        ).pack(pady=(10, 5))
        
        ttk.Label(
            dialog,
            text='Enter new namespace (filename will be updated to match):',
            font=('TkDefaultFont', 9, 'bold'),
        ).pack(anchor=tk.W, padx=20, pady=(10, 5))
        
        namespace_var = tk.StringVar(value=current_namespace)
        namespace_entry = ttk.Entry(dialog, textvariable=namespace_var, width=70)
        namespace_entry.pack(padx=20, pady=5, fill=tk.X)
        namespace_entry.select_range(0, tk.END)
        namespace_entry.focus()
        
        # Show preview of new filename
        preview_label = ttk.Label(
            dialog,
            text='',
            font=('TkDefaultFont', 8),
            foreground='gray',
        )
        preview_label.pack(padx=20, pady=(0, 5))
        
        def update_preview(*args) -> None:
            new_ns = namespace_var.get().strip()
            if new_ns:
                preview_label.config(text=f'New filename will be: {new_ns}.ndf')
            else:
                preview_label.config(text='')
        
        namespace_var.trace('w', update_preview)
        update_preview()
        
        def apply_namespace() -> None:
            new_namespace = namespace_var.get().strip()
            if not new_namespace:
                messagebox.showwarning('Invalid Namespace', 'Namespace cannot be empty.')
                return
            if new_namespace == current_namespace:
                # Even if same, still update filename to ensure it matches
                new_filename = f'{new_namespace}.ndf'
                if self.current_file and self.current_file.name != new_filename:
                    self.rename_file_to_match_namespace(new_namespace)
                dialog.destroy()
                return
            
            # Validate namespace format (should be a valid identifier)
            if not new_namespace.replace('_', '').replace('-', '').isalnum():
                response = messagebox.askyesno(
                    'Invalid Characters',
                    f'Namespace contains special characters.\n\n'
                    f'Namespace: {new_namespace}\n\n'
                    f'Continue anyway?',
                )
                if not response:
                    return
            
            try:
                # Update namespace in parsed NDF
                update_namespace(self.parsed_root, new_namespace)
                
                # Rename file to match new namespace
                self.rename_file_to_match_namespace(new_namespace)
                
                messagebox.showinfo(
                    'Namespace and Filename Updated',
                    f'Namespace updated from:\n{current_namespace}\n\nto:\n{new_namespace}\n\n'
                    f'File renamed to: {new_namespace}.ndf',
                )
                dialog.destroy()
                # Refresh tree to show updated namespace
                self.refresh_tree()
            except Exception as exc:
                messagebox.showerror('Error', f'Failed to update namespace:\n{exc}')
        
        def cancel() -> None:
            dialog.destroy()
        
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text='Apply', command=apply_namespace).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text='Cancel', command=cancel).pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to apply
        namespace_entry.bind('<Return>', lambda e: apply_namespace())
        namespace_entry.bind('<Escape>', lambda e: cancel())
    
    def rename_file_to_match_namespace(self, new_namespace: str) -> None:
        """Rename the current file to match the new namespace.
        
        Args:
            new_namespace: The new namespace (will become the filename without .ndf)
        """
        if not self.current_file:
            return
        
        new_filename = f'{new_namespace}.ndf'
        new_file_path = self.current_file.parent / new_filename
        
        # If file already exists and it's not the same file, ask for confirmation
        if new_file_path.exists() and new_file_path != self.current_file:
            response = messagebox.askyesno(
                'File Exists',
                f'File already exists:\n{new_file_path}\n\n'
                f'Overwrite it?',
            )
            if not response:
                return
        
        try:
            # Rename the file
            self.current_file.rename(new_file_path)
            self.current_file = new_file_path
            # Update the file path in the UI
            self.file_var.set(str(new_file_path))
        except Exception as exc:
            raise Exception(f'Failed to rename file: {exc}')
    
    def manual_namespace_update(self) -> None:
        """Manually trigger namespace update prompt."""
        if not self.parsed_root:
            messagebox.showwarning('No File', 'Load a file before updating namespace.')
            return
        
        export_row = get_export_row(self.parsed_root)
        if not export_row or not export_row.namespace:
            messagebox.showwarning('No Namespace', 'No export namespace found in file.')
            return
        
        current_namespace = export_row.namespace
        self.prompt_for_new_namespace(current_namespace, None)

    def _parse_positive_float(self, text: str) -> Optional[float]:
        try:
            value = float(text.strip())
        except ValueError:
            return None
        if value <= 0:
            return None
        return value

    @staticmethod
    def _param_change_report(changes: List[Any]) -> str:
        """Short summary: total scaled NamedParams / declaration rows (one line)."""
        n = len(changes)
        return f'{n} param change(s)'

    @staticmethod
    def _call_change_report(
        call_changes: List[Any],
        *,
        effect_call_scale_pct: Optional[Dict[str, float]] = None,
        scale_factor: float = 1.0,
        vfx_burst_denoms: Optional[Dict[str, int]] = None,
    ) -> str:
        """Delegates to :func:`~.call_scale.format_call_qty_report_line` (Scatter tab uses the same)."""
        s = format_call_qty_report_line(
            call_changes,
            effect_call_scale_pct=effect_call_scale_pct,
            scale_factor=scale_factor,
            vfx_burst_denoms=vfx_burst_denoms,
        )
        return f'  |  {s}' if s else ''

    def _batch_curve_settings_lines(self) -> List[str]:
        """Human-readable Param/Call qty curves and Param/Call radius falloff (for Results pane)."""
        lines: List[str] = []
        lines.append('Curve settings (Param Qty / Call Qty / radius falloff):')
        targets = self._parsed_target_radii_m()
        if targets:
            lines.append(
                f'  Qty curves: target radii (m) = {", ".join(f"{t:g}" for t in targets)}',
            )
        else:
            lines.append(
                '  Qty curves: (no target radii in the Batch field — add radii to drive qty curves.)',
            )
        keys: Set[str] = set()
        keys.update(self._variation_group_param_qty_curve.keys())
        keys.update(self._variation_group_call_qty_curve.keys())
        keys.update(self._variation_group_param_radius_falloff_curve.keys())
        keys.update(self._variation_group_call_radius_falloff_curve.keys())
        lines.append(
            f'  Radius falloff: {RADIUS_FALLOFF_SAMPLES} samples vs r_norm = '
            'distance from scatter center / target batch radius (0 = center, 1 = edge).',
        )
        if not keys:
            lines.append(
                '  (No effect patterns — click "Refresh effect groups from selection" '
                'to edit per-pattern curves; until then, curves default to 100%.)',
            )
            return lines

        n_tgt = max(len(targets), 1)

        def _fmt_qty_vs_targets(vals: List[float]) -> str:
            av = self._curve_aligned_to_targets(vals, n_tgt)
            if targets and len(av) == len(targets):
                pairs = [f'{tm:g}m→{v:.0f}%' for tm, v in zip(targets, av)]
                return ', '.join(pairs)
            return ', '.join(f'{v:.0f}%' for v in av)

        def _fmt_rf(vals: List[float]) -> str:
            a = self._curve_aligned_radius_falloff(vals)
            parts = ', '.join(f'{v:.0f}%' for v in a)
            lo = min(a)
            hi = max(a)
            return f'[{parts}]  (min {lo:.0f}%, max {hi:.0f}%)'

        for k in sorted(keys):
            short = k if len(k) <= 96 else k[:93] + '…'
            lines.append(f'  Pattern: {short}')
            pq = self._variation_group_param_qty_curve.get(k, [100.0] * n_tgt)
            cq = self._variation_group_call_qty_curve.get(k, [100.0] * n_tgt)
            prf = self._variation_group_param_radius_falloff_curve.get(
                k,
                [100.0] * RADIUS_FALLOFF_SAMPLES,
            )
            crf = self._variation_group_call_radius_falloff_curve.get(
                k,
                [100.0] * RADIUS_FALLOFF_SAMPLES,
            )
            lines.append(f'    Param Qty % vs target radius: {_fmt_qty_vs_targets(pq)}')
            lines.append(f'    Call Qty % vs target radius: {_fmt_qty_vs_targets(cq)}')
            lines.append(f'    Param radius falloff (qty % vs r_norm): {_fmt_rf(prf)}')
            lines.append(f'    Call radius falloff (qty % vs r_norm): {_fmt_rf(crf)}')
        return lines

    def _log_batch_curve_settings(self) -> None:
        for line in self._batch_curve_settings_lines():
            self.log_message(line)

    def _variation_curve_snapshot(self) -> Dict[str, Any]:
        return {
            'param_qty_curve': {k: v[:] for k, v in self._variation_group_param_qty_curve.items()},
            'call_qty_curve': {k: v[:] for k, v in self._variation_group_call_qty_curve.items()},
            'param_radius_curve': {
                k: v[:] for k, v in self._variation_group_param_radius_falloff_curve.items()
            },
            'call_radius_curve': {
                k: v[:] for k, v in self._variation_group_call_radius_falloff_curve.items()
            },
            'cached_effect_groups': self._cached_effect_groups,
        }

    def _set_variation_job_ui_busy(self, busy: bool) -> None:
        st = tk.DISABLED if busy else tk.NORMAL
        self.variation_preview_btn.config(state=st)
        self.variation_apply_btn.config(state=st)
        self.root.config(cursor='watch' if busy else '')
        try:
            self.variation_progress.stop()
        except tk.TclError:
            pass
        if busy:
            self.variation_progress.configure(mode='determinate')
        else:
            self.variation_progress.configure(mode='determinate', value=0)
            self.variation_progress_label.config(text='')

    def _drain_batch_queue(self) -> None:
        """Drain up to N queue messages per timer tick; ``update_idletasks`` after each progress."""
        q = self._batch_job_queue
        if q is None:
            return
        max_per_tick = 80
        processed = 0
        try:
            while processed < max_per_tick:
                msg = q.get_nowait()
                processed += 1
                if msg[0] == 'done':
                    self._on_batch_job_done(msg[1])
                    self._batch_job_queue = None
                    return
                self._handle_batch_queue_item(msg)
                if msg[0] == 'progress':
                    self.root.update_idletasks()
        except queue.Empty:
            pass
        if self._batch_job_running:
            # If we hit the cap, continue draining immediately; else poll again shortly.
            delay = 0 if processed >= max_per_tick else 50
            self.root.after(delay, self._drain_batch_queue)

    def _scatter_reload_from_batch_payload(self, payload: Dict[str, Any]) -> None:
        """Apply cluster project to scatter tab (may be slow; run from the pump, one per event slice)."""
        project = payload['project']
        dest = payload['dest']
        file_path = payload['file_path']
        sp = self.scatter_panel_for_path(file_path.resolve())
        if sp is not None:
            sp.load_from_project(project, str(dest.resolve()))
        self.root.update_idletasks()

    def _pump_scatter_reload_queue(self) -> None:
        """Run one scatter reload, then yield so timers (batch queue drain / progress) can run."""
        if not self._scatter_reload_queue:
            self._scatter_reload_pump_scheduled = False
            return
        payload = self._scatter_reload_queue.pop(0)
        self._scatter_reload_from_batch_payload(payload)
        if self._scatter_reload_queue:
            # Yield so ``after(50, _drain_batch_queue)`` and WM_PAINT can run before the next heavy load.
            self.root.after(5, self._pump_scatter_reload_queue)
        else:
            self._scatter_reload_pump_scheduled = False

    def _enqueue_scatter_reload_from_batch(self, payload: Dict[str, Any]) -> None:
        self._scatter_reload_queue.append(payload)
        if not self._scatter_reload_pump_scheduled:
            self._scatter_reload_pump_scheduled = True
            self.root.after(0, self._pump_scatter_reload_queue)

    def _handle_batch_queue_item(self, msg: Tuple[Any, ...]) -> None:
        kind = msg[0]
        if kind == 'log':
            self.log_message(msg[1])
        elif kind == 'progress':
            self.variation_progress.configure(value=msg[1])
            self.variation_progress_label.config(text=f'{msg[1]} / {msg[2]}')
        elif kind == 'scatter_reload':
            self._enqueue_scatter_reload_from_batch(msg[1])

    def _finalize_preview_job_ui(self, payload: Dict[str, Any]) -> None:
        """Main-thread work after worker preview: PreviewWindow(s) + Scatter layout tabs (cluster pipeline per tab)."""
        meta = getattr(self, '_preview_finalize_progress', None) or {'cur': 0, 'max': 1}
        cur = int(meta['cur'])
        max_total = int(meta['max'])
        try:
            for spec in payload.get('preview_specs', []):
                try:
                    PreviewWindow(
                        self.root,
                        spec['file_path'],
                        spec['scale_factor'],
                        title_suffix=spec['title_suffix'],
                        allowed_size_param_names=None,
                        scale_size_params=spec['scale_size'],
                        scale_count_params=spec['scale_count'],
                        include_declaration_params=spec['include_declaration_params'],
                        effect_named_flags=spec['effect_named_flags'],
                        effect_count_scale_pct=spec['effect_count_scale_pct'],
                        param_radius_falloff_mult_by_taction_id=spec['param_radius_falloff_mult_by_taction_id'],
                    )
                except Exception as exc:
                    self.log_message(f'  Warning: Could not open preview: {exc}')
                cur += 1
                self.variation_progress.configure(value=cur)
                self.variation_progress_label.config(text=f'{cur} / {max_total} (preview window)')
                self.root.update_idletasks()
            n_scatter = len(payload.get('scatter_tabs', []))
            for i, (tab_lbl, proj, path, target_m) in enumerate(payload.get('scatter_tabs', []), start=1):
                try:
                    self._append_scatter_preview_tab(tab_lbl, proj, path, target_m)
                except Exception as exc:
                    self.log_message(f'  Scatter tab: {exc}')
                cur += 1
                self.variation_progress.configure(value=cur)
                self.variation_progress_label.config(
                    text=f'{cur} / {max_total} (scatter tab {i}/{n_scatter})',
                )
                self.root.update_idletasks()
            self._rebuild_scatter_variation_checkboxes()
            cur += 1
            self.variation_progress.configure(value=cur)
            self.variation_progress_label.config(text=f'{cur} / {max_total} (scatter UI)')
            self.root.update_idletasks()
            self._apply_scatter_variation_visibility()
            self.sync_scatter_tab_radii()
        finally:
            self._preview_finalize_progress = None
            self._batch_job_running = False
            self._set_variation_job_ui_busy(False)

    def _on_batch_job_done(self, payload: Dict[str, Any]) -> None:
        kind = payload.get('kind')
        if kind == 'preview' and not payload.get('error'):
            try:
                self.variation_progress.stop()
            except tk.TclError:
                pass
            ws = int(getattr(self, '_preview_job_worker_steps', 1))
            n_pw = len(payload.get('preview_specs', []))
            n_sc = len(payload.get('scatter_tabs', []))
            max_total = ws + n_pw + n_sc + 1
            self._preview_finalize_progress = {'cur': ws, 'max': max_total}
            self.variation_progress.configure(
                mode='determinate',
                maximum=max_total,
                value=ws,
            )
            self.variation_progress_label.config(
                text=(
                    f'{ws} / {max_total} (NDF batch done; '
                    f'{n_pw} preview window(s), {n_sc} scatter layout tab(s)…)'
                ),
            )
            self.root.update_idletasks()
            self.root.after(0, lambda p=payload: self._finalize_preview_job_ui(p))
            return
        if kind == 'preview' and payload.get('error'):
            self._batch_job_running = False
            self._set_variation_job_ui_busy(False)
            return
        self._batch_job_running = False
        self._set_variation_job_ui_busy(False)
        if kind == 'apply':
            if payload.get('error'):
                messagebox.showerror('Variations', 'Create failed — see Results.')
            else:
                messagebox.showinfo(
                    'Variations',
                    f'Created {payload["ok"]} file(s). Skipped {payload["skipped"]}. Errors: {payload["errors"]}.',
                )

    def preview_variations(self) -> None:
        if self._batch_job_running:
            messagebox.showwarning('Busy', 'A batch job is already running.')
            return
        selected_files = self.get_selected_files()
        if not selected_files:
            messagebox.showwarning('No Files', 'Please select at least one file.')
            return
        source_m = self._parse_positive_float(self.variation_source_m_var.get())
        if source_m is None:
            messagebox.showerror('Invalid size', 'Enter a positive source effect radius in meters.')
            return
        targets = parse_target_sizes(self.variation_targets_text.get('1.0', tk.END))
        if not targets:
            messagebox.showerror('No targets', 'Enter at least one target radius in meters.')
            return
        if self.variation_geom_var.get() == 'param' and not self._variation_scaling_requested():
            messagebox.showerror(
                'Parameter scaling',
                'For “keep layout” mode, enable Size and/or Count, or set Param Qty % or '
                'Call Qty % (slider or curve) below 100% for an effect pattern, or use a '
                'radius falloff curve.',
            )
            return
        rootname = self.variation_rootname_var.get().strip()
        if not rootname:
            messagebox.showerror('Root name', 'Enter a root name for {rootname}.')
            return
        template = self.variation_template_var.get().strip()
        if not template.endswith('.ndf'):
            messagebox.showerror('Template', 'Filename template must end with .ndf.')
            return
        for file_path in selected_files:
            stem = file_path.stem
            for target_m in targets:
                name = render_variation_filename(template, rootname, target_m, stem)
                if '/' in name or '\\' in name or name.strip() != name:
                    messagebox.showerror(
                        'Invalid name',
                        f'Resolved filename is not a plain name:\n{name}',
                    )
                    return

        self.clear_results()
        self._clear_scatter_preview_tabs()
        out_root = self.resolved_batch_output_dir()
        self.log_message('=== Variation preview ===')
        self.log_message(
            f'Mode: {"reshape scatter (burst count + emit + param scale)" if self.variation_geom_var.get() == "cluster" else "keep layout (param scale only)"}',
        )
        self.log_message(
            f'Source radius: {source_m:g} m  |  Target radii: {len(targets)}  |  Files: {len(selected_files)}',
        )
        self.log_message(f'Output directory: {out_root}')
        self._log_batch_curve_settings()
        ref_m, anchor_r = load_scatter_calibration_yaml()
        try:
            _ppw = int(os.environ.get('FX_EDITOR_PREVIEW_WORKERS', '1'))
        except (TypeError, ValueError):
            _ppw = 1
        snapshot: Dict[str, Any] = {
            'selected_files': list(selected_files),
            'source_m': source_m,
            'targets': targets,
            'template': template,
            'rootname': rootname,
            'geom': self.variation_geom_var.get(),
            'out_root': out_root,
            'bkw': self._batch_scale_kwargs(),
            'ref_m': ref_m,
            'anchor_r': anchor_r,
            'wait_max': float(self.variation_wait_max_var.get()),
            'preview_parallel_workers': max(1, min(_ppw, 16)),
            **self._variation_curve_snapshot(),
        }
        total_steps = max(len(selected_files) * len(targets), 1)
        self._preview_job_worker_steps = total_steps
        self._batch_job_running = True
        self._scatter_reload_queue.clear()
        self._scatter_reload_pump_scheduled = False
        self._batch_job_queue = queue.Queue()
        self._set_variation_job_ui_busy(True)
        self.variation_progress.configure(maximum=total_steps, value=0)
        self.variation_progress_label.config(text=f'0 / {total_steps}')
        threading.Thread(
            target=preview_variations_worker,
            args=(snapshot, self._batch_job_queue),
            daemon=True,
        ).start()
        self.root.after(0, self._drain_batch_queue)

    def apply_variations(self) -> None:
        if self._batch_job_running:
            messagebox.showwarning('Busy', 'A batch job is already running.')
            return
        selected_files = self.get_selected_files()
        if not selected_files:
            messagebox.showwarning('No Files', 'Please select at least one file.')
            return
        source_m = self._parse_positive_float(self.variation_source_m_var.get())
        if source_m is None:
            messagebox.showerror('Invalid size', 'Enter a positive source effect radius in meters.')
            return
        targets = parse_target_sizes(self.variation_targets_text.get('1.0', tk.END))
        if not targets:
            messagebox.showerror('No targets', 'Enter at least one target radius in meters.')
            return
        if self.variation_geom_var.get() == 'param' and not self._variation_scaling_requested():
            messagebox.showerror(
                'Parameter scaling',
                'For “keep layout” mode, enable Size and/or Count, or set Param Qty % or '
                'Call Qty % (slider or curve) below 100% for an effect pattern, or use a '
                'radius falloff curve.',
            )
            return
        rootname = self.variation_rootname_var.get().strip()
        if not rootname:
            messagebox.showerror('Root name', 'Enter a root name for {rootname}.')
            return
        template = self.variation_template_var.get().strip()
        if not template.endswith('.ndf'):
            messagebox.showerror('Template', 'Filename template must end with .ndf.')
            return
        overwrite = self.variation_overwrite_var.get()
        out_root = self.resolved_batch_output_dir()

        for file_path in selected_files:
            stem = file_path.stem
            for target_m in targets:
                name = render_variation_filename(template, rootname, target_m, stem)
                if '/' in name or '\\' in name or name.strip() != name:
                    messagebox.showerror(
                        'Invalid name',
                        f'Resolved filename is not a plain name:\n{name}',
                    )
                    return

        planned: List[Tuple[Path, Path, float]] = []
        seen_dest: set = set()
        for file_path in selected_files:
            stem = file_path.stem
            for target_m in targets:
                name = render_variation_filename(template, rootname, target_m, stem)
                dest = out_root / name
                key = str(dest.resolve())
                if key in seen_dest:
                    messagebox.showerror(
                        'Duplicate output',
                        f'The same destination would be written twice:\n{dest.name}\n'
                        f'Check target radii and template.',
                    )
                    return
                seen_dest.add(key)
                planned.append((file_path, dest, target_m))

        to_skip: List[Path] = []
        for _src, dest, _t in planned:
            if dest.exists():
                if not overwrite:
                    to_skip.append(dest)
        if to_skip and not overwrite:
            preview = '\n'.join(p.name for p in to_skip[:8])
            more = f'\n... and {len(to_skip) - 8} more' if len(to_skip) > 8 else ''
            if not messagebox.askyesno(
                'Existing files',
                f'{len(to_skip)} destination file(s) already exist and overwrite is off.\n'
                f'Those will be skipped.\n\n{preview}{more}\n\nContinue?',
            ):
                return

        count = len(planned)
        confirm_extra = ''
        if self.variation_geom_var.get() == 'cluster':
            confirm_extra = (
                '\n\nReshape scatter: burst count scales with (target/source)² (area); '
                'hex layout + wait envelope; emit cycles all TSimultaneousAction patterns in the file.'
            )
        if not messagebox.askyesno(
            'Confirm',
            f'Create {count} scaled copy/copies in:\n{out_root}\n\n'
            f'Source radius baseline: {source_m:g} m  |  Namespace will match each new filename.{confirm_extra}',
        ):
            return

        self.clear_results()
        self.log_message('=== Creating size variations ===')
        self.log_message(f'Output directory: {out_root}')
        self._log_batch_curve_settings()
        ref_m, anchor_r = load_scatter_calibration_yaml()
        snapshot: Dict[str, Any] = {
            'planned': planned,
            'overwrite': overwrite,
            'source_m': source_m,
            'targets': targets,
            'geom': self.variation_geom_var.get(),
            'bkw': self._batch_scale_kwargs(),
            'ref_m': ref_m,
            'anchor_r': anchor_r,
            'wait_max': float(self.variation_wait_max_var.get()),
            **self._variation_curve_snapshot(),
        }
        total_steps = max(len(planned), 1)
        self._batch_job_running = True
        self._scatter_reload_queue.clear()
        self._scatter_reload_pump_scheduled = False
        self._batch_job_queue = queue.Queue()
        self._set_variation_job_ui_busy(True)
        self.variation_progress.configure(maximum=total_steps, value=0)
        self.variation_progress_label.config(text=f'0 / {total_steps}')
        threading.Thread(
            target=apply_variations_worker,
            args=(snapshot, self._batch_job_queue),
            daemon=True,
        ).start()
        self.root.after(0, self._drain_batch_queue)


def main() -> None:
    setup_fx_logging()
    logging.getLogger('fx_editor').info('FX Editor starting (log: stderr + debug log window)')
    root = tk.Tk()
    app = FXEditorApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
