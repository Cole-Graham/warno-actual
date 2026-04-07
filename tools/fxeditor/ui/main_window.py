"""Main PySide6 window assembling all controls."""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Dict, List, Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDoubleSpinBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QSlider,
    QSplitter,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from ..core.budget import count_source_taction_calls
from ..core.config import CalibrationConfig, load_config
from ..core.extract import ScatterPointVfx, extract_scatter_points_with_vfx
from ..core.falloff import default_curve
from ..core.grouping import (
    analyze_effect_groups,
    build_composite_site_model,
)
from ..core.naming import extract_trailing_index
from ..core.ndf_io import (
    count_taction_calls,
    find_actions_list,
    list_tsimultaneous_rows,
    parse_ndf,
)
from ..core.scaler import ScaleResult, ScalerConfig, scale_single_file_in_memory
from ..core.spatial_classifier import classify_source, format_classification_summary
from .effect_group_panel import EffectGroupPanel
from .falloff_dialog import FalloffDialog
from .scatter_canvas import ScatterCanvas, ScatterDot
from .settings_dialog import SettingsDialog
from .state import AppState
from .worker import GenerateWorker

_log = logging.getLogger(__name__)


def _parse_radii(text: str) -> List[float]:
    out: List[float] = []
    for raw in re.split(r"[\s,;]+", text.strip()):
        if not raw:
            continue
        try:
            out.append(float(raw))
        except ValueError:
            continue
    return sorted(set(out))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VFX Scaler Tool")

        self._state = AppState()
        self._state.load()
        self._worker: Optional[GenerateWorker] = None
        self._parsed_roots: Dict[str, object] = {}
        self._source_texts: Dict[str, str] = {}
        self._source_n0 = 0
        self._source_total_calls = 0
        self._preview_dirty = False

        self._build_menu()
        self._build_ui()
        self._restore_state()

    # ── Menu ─────────────────────────────────────────────────────

    def _build_menu(self) -> None:
        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction("Open Source Files...", self._open_source_files, "Ctrl+O")
        file_menu.addAction("Save State", self._save_state, "Ctrl+S")
        file_menu.addSeparator()
        file_menu.addAction("Reset to Defaults", self._reset_defaults)
        file_menu.addSeparator()
        file_menu.addAction("Exit", self.close)

        settings_menu = menu.addMenu("&Settings")
        settings_menu.addAction("Preferences...", self._open_settings, "Ctrl+,")

        help_menu = menu.addMenu("&Help")
        help_menu.addAction("About", self._show_about)

    # ── UI Build ─────────────────────────────────────────────────

    def _build_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QHBoxLayout(central)

        self._splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(self._splitter)

        # ── Left Panel ───────────────────────────────────────────
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(8, 8, 4, 8)

        # Source files
        src_row = QHBoxLayout()
        src_row.addWidget(QLabel("Source files:"))
        self._src_label = QLabel("(none)")
        self._src_label.setStyleSheet("color: #aaa;")
        src_row.addWidget(self._src_label, 1)
        src_btn = QPushButton("Browse...")
        src_btn.clicked.connect(self._open_source_files)
        src_row.addWidget(src_btn)
        left_layout.addLayout(src_row)

        # Source radius
        r_row = QHBoxLayout()
        r_row.addWidget(QLabel("Source radius (m):"))
        self._src_radius_spin = QDoubleSpinBox()
        self._src_radius_spin.setRange(1.0, 1000.0)
        self._src_radius_spin.setDecimals(1)
        self._src_radius_spin.setValue(60.0)
        self._src_radius_spin.valueChanged.connect(self._mark_dirty)
        r_row.addWidget(self._src_radius_spin)
        left_layout.addLayout(r_row)

        # Root name
        rn_row = QHBoxLayout()
        rn_row.addWidget(QLabel("Root name:"))
        self._rootname_edit = QLineEdit()
        rn_row.addWidget(self._rootname_edit)
        left_layout.addLayout(rn_row)

        # Target radii
        tr_row = QHBoxLayout()
        tr_row.addWidget(QLabel("Target radii:"))
        self._radii_edit = QLineEdit()
        self._radii_edit.setPlaceholderText("35, 75, 100, 125, 150, 175, 200, 225, 250")
        self._radii_edit.textChanged.connect(self._mark_dirty)
        tr_row.addWidget(self._radii_edit)
        left_layout.addLayout(tr_row)

        # Output dir
        out_row = QHBoxLayout()
        out_row.addWidget(QLabel("Output dir:"))
        self._outdir_edit = QLineEdit()
        out_row.addWidget(self._outdir_edit, 1)
        out_browse = QPushButton("Browse...")
        out_browse.clicked.connect(self._browse_output_dir)
        out_row.addWidget(out_browse)
        left_layout.addLayout(out_row)

        # Falloff + Cap row
        fc_row = QHBoxLayout()
        falloff_btn = QPushButton("Edit Falloff Curve...")
        falloff_btn.clicked.connect(self._open_falloff_dialog)
        fc_row.addWidget(falloff_btn)

        fc_row.addWidget(QLabel("TActionCall cap:"))
        self._cap_spin = QDoubleSpinBox()
        self._cap_spin.setRange(200, 2000)
        self._cap_spin.setDecimals(0)
        self._cap_spin.setValue(600)
        self._cap_spin.valueChanged.connect(self._mark_dirty)
        fc_row.addWidget(self._cap_spin)

        left_layout.addLayout(fc_row)

        # Effect group panel
        self._effect_panel = EffectGroupPanel()
        self._effect_panel.visibility_changed.connect(self._on_vfx_visibility_changed)
        left_layout.addWidget(self._effect_panel, 1)

        self._splitter.addWidget(left_widget)

        # ── Right Panel ──────────────────────────────────────────
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(4, 8, 8, 8)

        # Preview controls
        pv_row = QHBoxLayout()
        self._refresh_btn = QPushButton("Refresh Preview")
        self._refresh_btn.setMinimumHeight(28)
        self._refresh_btn.setStyleSheet("font-weight: bold;")
        self._refresh_btn.clicked.connect(self._refresh_preview)
        pv_row.addWidget(self._refresh_btn)

        pv_row.addWidget(QLabel("View radius:"))
        self._view_radius_spin = QDoubleSpinBox()
        self._view_radius_spin.setRange(10.0, 2000.0)
        self._view_radius_spin.setDecimals(0)
        self._view_radius_spin.setValue(300.0)
        self._view_radius_spin.valueChanged.connect(self._on_view_radius_changed)
        pv_row.addWidget(self._view_radius_spin)
        pv_row.addStretch()
        right_layout.addLayout(pv_row)

        # Tabbed scatter preview
        self._scatter_tabs = QTabWidget()
        self._scatter_tabs.setTabsClosable(False)
        right_layout.addWidget(self._scatter_tabs, 1)

        # Timeline scrubber
        tl_row = QHBoxLayout()
        tl_row.addWidget(QLabel("Timeline:"))
        self._timeline_slider = QSlider(Qt.Horizontal)
        self._timeline_slider.setRange(0, 200)
        self._timeline_slider.setValue(200)
        self._timeline_slider.valueChanged.connect(self._on_timeline_changed)
        tl_row.addWidget(self._timeline_slider, 1)
        self._timeline_label = QLabel("all")
        tl_row.addWidget(self._timeline_label)
        right_layout.addLayout(tl_row)

        # Generate section
        gen_row = QHBoxLayout()
        self._gen_btn = QPushButton("Generate All")
        self._gen_btn.setMinimumHeight(36)
        self._gen_btn.clicked.connect(self._start_generate)
        gen_row.addWidget(self._gen_btn)
        self._progress = QProgressBar()
        self._progress.setVisible(False)
        gen_row.addWidget(self._progress, 1)
        right_layout.addLayout(gen_row)

        # Log
        self._log_area = QTextEdit()
        self._log_area.setReadOnly(True)
        self._log_area.setMaximumHeight(160)
        self._log_area.setStyleSheet("font-family: 'Consolas', monospace; font-size: 11px;")
        right_layout.addWidget(self._log_area)

        self._splitter.addWidget(right_widget)
        self._splitter.setStretchFactor(0, 1)
        self._splitter.setStretchFactor(1, 2)

    # ── State ────────────────────────────────────────────────────

    def _restore_state(self) -> None:
        s = self._state
        x, y = s.get("window_x", 100), s.get("window_y", 100)
        w, h = s.get("window_w", 1400), s.get("window_h", 900)
        self.setGeometry(x, y, w, h)
        if s.get("window_maximized", False):
            self.showMaximized()

        self._src_radius_spin.setValue(s.source_radius_m)
        self._rootname_edit.setText(s.rootname)
        self._radii_edit.setText(s.target_radii_text)
        self._outdir_edit.setText(s.output_dir)
        self._cap_spin.setValue(s.taction_call_cap)
        self._view_radius_spin.setValue(s.get("view_radius", 300.0))

        splitter_sizes = s.get("splitter_sizes")
        if splitter_sizes and isinstance(splitter_sizes, list):
            self._splitter.setSizes([int(x) for x in splitter_sizes])

        if s.source_files:
            self._load_sources(s.source_files)

    def _save_state(self) -> None:
        s = self._state
        g = self.geometry()
        s.set("window_x", g.x())
        s.set("window_y", g.y())
        s.set("window_w", g.width())
        s.set("window_h", g.height())
        s.set("window_maximized", self.isMaximized())
        s.source_radius_m = self._src_radius_spin.value()
        s.rootname = self._rootname_edit.text()
        s.target_radii_text = self._radii_edit.text()
        s.output_dir = self._outdir_edit.text()
        s.taction_call_cap = int(self._cap_spin.value())
        s.set("view_radius", self._view_radius_spin.value())
        s.set("splitter_sizes", self._splitter.sizes())
        s.vfx_visibility = self._effect_panel.get_visibility()
        s.save()

    def closeEvent(self, event) -> None:
        self._save_state()
        super().closeEvent(event)

    def _reset_defaults(self) -> None:
        self._state.reset()
        self._restore_state()

    # ── File operations ──────────────────────────────────────────

    def _open_source_files(self) -> None:
        last_dir = self._state.get("last_source_dir", "")
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select Source NDF Files", last_dir, "NDF Files (*.ndf);;All Files (*)",
        )
        if not files:
            return
        self._state.set("last_source_dir", str(Path(files[0]).parent))
        self._state.source_files = files
        self._load_sources(files)

    def _load_sources(self, paths: List[str]) -> None:
        self._parsed_roots.clear()
        self._source_texts.clear()
        names = []
        for p in paths:
            pp = Path(p)
            if not pp.exists():
                continue
            try:
                text = pp.read_text(encoding="utf-8")
                parsed = parse_ndf(text)
                self._parsed_roots[str(pp)] = parsed
                self._source_texts[str(pp)] = text
                names.append(pp.name)
            except Exception as exc:
                _log.warning("Failed to parse %s: %s", pp, exc)

        if not names:
            self._src_label.setText("(failed to load)")
            return
        self._src_label.setText(", ".join(names))

        first_path = Path(paths[0])
        base, suffix, n = extract_trailing_index(first_path.stem)
        if not self._rootname_edit.text():
            self._rootname_edit.setText(base)

        if not self._outdir_edit.text():
            default_out = str(Path(__file__).resolve().parent.parent / "out")
            self._outdir_edit.setText(default_out)

        self._analyze_sources()
        self._build_source_tabs()
        self._refresh_preview()

    def _analyze_sources(self) -> None:
        if not self._parsed_roots:
            return

        cal = self._get_calibration()
        first_parsed = next(iter(self._parsed_roots.values()))

        site_model = build_composite_site_model(
            first_parsed,
            ref_m=cal.reference_gameplay_radius_m,
            anchor_r=cal.anchor_max_ndf_radius,
        )
        self._source_n0 = site_model.n_sites if site_model else 10
        self._source_total_calls = count_source_taction_calls(first_parsed)

        groups = analyze_effect_groups(first_parsed)

        # Also run spatial classification for the info panel
        cls = classify_source(
            first_parsed,
            cal.reference_gameplay_radius_m,
            cal.anchor_max_ndf_radius,
        )
        cls_summary = format_classification_summary(cls)

        self._effect_panel.set_groups(
            groups, self._source_n0,
            initial_visibility=self._state.vfx_visibility or None,
            classification_summary=cls_summary,
        )

    # ── Config changes ───────────────────────────────────────────

    def _mark_dirty(self) -> None:
        self._preview_dirty = True
        self._refresh_btn.setText("Refresh Preview *")
        self._refresh_btn.setStyleSheet("font-weight: bold; color: #e8a040;")

    def _on_view_radius_changed(self) -> None:
        vr = self._view_radius_spin.value()
        for i in range(self._scatter_tabs.count()):
            canvas = self._scatter_tabs.widget(i)
            if isinstance(canvas, ScatterCanvas):
                canvas.set_view_radius(vr)

    def _on_vfx_visibility_changed(self, vis: Dict[str, bool]) -> None:
        for i in range(self._scatter_tabs.count()):
            canvas = self._scatter_tabs.widget(i)
            if isinstance(canvas, ScatterCanvas):
                canvas.set_vfx_visibility(vis)

    def _on_timeline_changed(self, val: int) -> None:
        if val >= 200:
            t = None
            self._timeline_label.setText("all")
        else:
            t = val / 100.0 * 2.0
            self._timeline_label.setText(f"{t:.2f}s")
        for i in range(self._scatter_tabs.count()):
            canvas = self._scatter_tabs.widget(i)
            if isinstance(canvas, ScatterCanvas):
                canvas.set_timeline_t(t)

    # ── Tabbed Scatter Preview ───────────────────────────────────

    def _build_source_tabs(self) -> None:
        """Create one tab per source file showing its raw scatter dots."""
        self._scatter_tabs.clear()
        cal = self._get_calibration()
        s = cal.reference_gameplay_radius_m / cal.anchor_max_ndf_radius if cal.anchor_max_ndf_radius > 0 else 1.0

        for path_str, parsed in self._parsed_roots.items():
            pp = Path(path_str)
            canvas = ScatterCanvas()
            canvas.set_view_radius(self._view_radius_spin.value())

            pts = extract_scatter_points_with_vfx(parsed)
            dots = self._pts_to_dots(pts, s)

            # Count TSimultaneousAction blocks and TActionCalls
            actions = find_actions_list(parsed)
            n_tsim = len(list_tsimultaneous_rows(actions)) if actions else 0
            n_calls = count_taction_calls(parsed)

            canvas.set_dots(dots)
            canvas.set_target_radius(self._src_radius_spin.value())
            canvas.set_taction_info(n_calls, int(self._cap_spin.value()))
            canvas.set_tsim_count(n_tsim)

            vis = self._effect_panel.get_visibility()
            if vis:
                canvas.set_vfx_visibility(vis)

            tab_name = pp.stem
            if len(tab_name) > 30:
                tab_name = tab_name[:27] + "..."
            self._scatter_tabs.addTab(canvas, tab_name)

    def _refresh_preview(self) -> None:
        """Run the classified emit pipeline for each (source, target_radius)
        and create preview variation tabs."""
        self._preview_dirty = False
        self._refresh_btn.setText("Refresh Preview")
        self._refresh_btn.setStyleSheet("font-weight: bold;")

        # Remove any existing preview tabs (keep source tabs)
        n_sources = len(self._parsed_roots)
        while self._scatter_tabs.count() > n_sources:
            self._scatter_tabs.removeTab(self._scatter_tabs.count() - 1)

        radii = _parse_radii(self._radii_edit.text())
        if not radii or not self._source_texts:
            return

        cal = self._get_calibration()
        s = cal.reference_gameplay_radius_m / cal.anchor_max_ndf_radius if cal.anchor_max_ndf_radius > 0 else 1.0
        config = self._build_scaler_config()

        QApplication.setOverrideCursor(Qt.WaitCursor)
        try:
            for path_str, source_text in self._source_texts.items():
                pp = Path(path_str)
                stem = pp.stem
                if len(stem) > 20:
                    stem = stem[:17] + "..."

                for target_m in radii:
                    config_copy = ScalerConfig(
                        source_radius_m=config.source_radius_m,
                        target_radii_m=[target_m],
                        rootname=config.rootname,
                        output_dir=config.output_dir,
                        naming_template=config.naming_template,
                        taction_call_cap=config.taction_call_cap,
                        min_burst_count=config.min_burst_count,
                        min_size_ratio=config.min_size_ratio,
                        min_count_value=config.min_count_value,
                        falloff_curve=config.falloff_curve,
                        calibration=config.calibration,
                    )
                    emitted, result = scale_single_file_in_memory(
                        source_text, target_m, config_copy,
                    )
                    if emitted is None:
                        _log.warning(
                            "Preview emit failed for %s @ %gm: %s",
                            pp.name, target_m, result.error,
                        )
                        continue

                    pts = extract_scatter_points_with_vfx(emitted)
                    dots = self._pts_to_dots(pts, s)

                    actions = find_actions_list(emitted)
                    n_tsim = len(list_tsimultaneous_rows(actions)) if actions else 0
                    n_calls = result.taction_calls

                    canvas = ScatterCanvas()
                    canvas.set_view_radius(self._view_radius_spin.value())
                    canvas.set_dots(dots)
                    canvas.set_target_radius(target_m)
                    canvas.set_taction_info(n_calls, config.taction_call_cap)
                    canvas.set_tsim_count(n_tsim)

                    constrained_tag = " [B]" if result.constrained else ""
                    tab_name = f"{stem} @ {target_m:g}m{constrained_tag}"
                    self._scatter_tabs.addTab(canvas, tab_name)

                    vis = self._effect_panel.get_visibility()
                    if vis:
                        canvas.set_vfx_visibility(vis)

            # Select the first preview tab if any were created
            if self._scatter_tabs.count() > n_sources:
                self._scatter_tabs.setCurrentIndex(n_sources)
        finally:
            QApplication.restoreOverrideCursor()

    def _pts_to_dots(
        self,
        pts: List[ScatterPointVfx],
        cal_scale: float,
    ) -> List[ScatterDot]:
        """Convert ScatterPointVfx (NDF coords) to ScatterDot (gameplay coords)."""
        dots: List[ScatterDot] = []
        for i, pt in enumerate(pts):
            gx = pt.dx_ndf * cal_scale
            gy = pt.dy_ndf * cal_scale
            dots.append(ScatterDot(
                x=gx,
                y=gy,
                vfx=pt.primary_vfx,
                index=i,
                delay_s=0.0,
                template_index=0,
            ))
        return dots

    # ── Dialogs ──────────────────────────────────────────────────

    def _open_falloff_dialog(self) -> None:
        dlg = FalloffDialog(
            self,
            initial_curve=self._state.falloff_curve,
            named_presets=self._state.get("named_falloff_presets", {}),
        )
        if dlg.exec() == FalloffDialog.Accepted and dlg.result_curve:
            self._state.falloff_curve = dlg.result_curve
            self._state.set("named_falloff_presets", dlg.named_presets)
            self._mark_dirty()

    def _open_settings(self) -> None:
        dlg = SettingsDialog(self._state, self)
        dlg.exec()
        if dlg.was_accepted:
            self._mark_dirty()

    def _show_about(self) -> None:
        QMessageBox.about(
            self,
            "About VFX Scaler Tool",
            "VFX Scaler Tool for WARNO\n\n"
            "Scales cluster VFX NDF files to arbitrary target radii "
            "while preserving the original artistic feel.\n\n"
            "Built with PySide6.",
        )

    # ── Generate ─────────────────────────────────────────────────

    def _get_calibration(self) -> CalibrationConfig:
        return CalibrationConfig(
            reference_gameplay_radius_m=self._state.get("calibration_ref_m", 60.0),
            anchor_max_ndf_radius=self._state.get("calibration_anchor_r", 4240.282686),
        )

    def _build_scaler_config(self) -> ScalerConfig:
        cal = self._get_calibration()
        return ScalerConfig(
            source_radius_m=self._src_radius_spin.value(),
            target_radii_m=_parse_radii(self._radii_edit.text()),
            rootname=self._rootname_edit.text(),
            output_dir=self._outdir_edit.text(),
            naming_template=self._state.naming_template,
            taction_call_cap=int(self._cap_spin.value()),
            min_burst_count=self._state.get("min_burst_count", 3),
            min_size_ratio=self._state.get("min_size_ratio", 0.3),
            min_count_value=self._state.get("min_count_value", 1),
            falloff_curve=self._state.falloff_curve,
            scale_sizes=self._state.get("scale_sizes", False),
            scale_counts=self._state.get("scale_counts", False),
            calibration=cal,
        )

    def _start_generate(self) -> None:
        if self._worker and self._worker.isRunning():
            QMessageBox.warning(self, "Busy", "Generation is already running.")
            return
        if not self._state.source_files:
            QMessageBox.warning(self, "No Sources", "Please load source NDF files first.")
            return
        radii = _parse_radii(self._radii_edit.text())
        if not radii:
            QMessageBox.warning(self, "No Radii", "Please enter target radii.")
            return
        if not self._outdir_edit.text():
            QMessageBox.warning(self, "No Output Dir", "Please set an output directory.")
            return

        config = self._build_scaler_config()
        source_paths = [Path(p) for p in self._state.source_files if Path(p).exists()]

        self._log_area.clear()
        self._log_area.append(f"Generating {len(source_paths)} file(s) x {len(radii)} radii...\n")
        self._progress.setVisible(True)
        self._progress.setRange(0, len(source_paths) * len(radii))
        self._progress.setValue(0)
        self._gen_btn.setEnabled(False)

        self._worker = GenerateWorker(source_paths, config, self)
        self._worker.progress.connect(self._on_gen_progress)
        self._worker.finished_all.connect(self._on_gen_finished)
        self._worker.error.connect(self._on_gen_error)
        self._worker.start()

    def _on_gen_progress(self, done: int, total: int, result: ScaleResult) -> None:
        self._progress.setValue(done)
        status = "OK" if not result.error else f"ERROR: {result.error}"
        constrained = " [BUDGET]" if result.constrained else ""
        self._log_area.append(
            f"  {Path(result.source_path).name} @ {result.target_radius_m:g}m -> "
            f"sites={result.n_sites_effective}/{result.n_sites_target} "
            f"calls={result.taction_calls}{constrained}  {status}",
        )

    def _on_gen_finished(self, results: List[ScaleResult]) -> None:
        self._progress.setVisible(False)
        self._gen_btn.setEnabled(True)
        errors = [r for r in results if r.error]
        self._log_area.append(f"\nDone: {len(results)} files generated, {len(errors)} errors.")
        if errors:
            for e in errors:
                self._log_area.append(f"  ERROR: {e.source_path} @ {e.target_radius_m}m: {e.error}")

    def _on_gen_error(self, msg: str) -> None:
        self._progress.setVisible(False)
        self._gen_btn.setEnabled(True)
        self._log_area.append(f"\nFATAL ERROR: {msg}")

    def _browse_output_dir(self) -> None:
        last = self._state.get("last_output_dir", self._outdir_edit.text())
        d = QFileDialog.getExistingDirectory(self, "Select Output Directory", last)
        if d:
            self._outdir_edit.setText(d)
            self._state.set("last_output_dir", d)
