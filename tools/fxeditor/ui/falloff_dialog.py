"""Radius falloff curve editor dialog with matplotlib preview."""

from __future__ import annotations

from typing import Dict, List, Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QComboBox,
    QDialog,
    QDoubleSpinBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from ..core.falloff import (
    FALLOFF_SAMPLES,
    default_curve,
    fourth_root_ramp,
    linear_ramp,
    quadratic_ramp,
    smoothstep_ramp,
    sqrt_ramp,
)

try:
    from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
    from matplotlib.figure import Figure
    _HAS_MPL = True
except ImportError:
    _HAS_MPL = False


class FalloffDialog(QDialog):
    """Qt curve editor dialog with matplotlib preview and 11 sample spinboxes."""

    def __init__(
        self,
        parent=None,
        *,
        initial_curve: Optional[List[float]] = None,
        named_presets: Optional[Dict[str, List[float]]] = None,
    ):
        super().__init__(parent)
        self.setWindowTitle("Radius Falloff Curve")
        self.setMinimumSize(700, 520)
        self.resize(780, 560)

        self._curve = list(initial_curve or default_curve())
        while len(self._curve) < FALLOFF_SAMPLES:
            self._curve.append(100.0)
        self._named_presets: Dict[str, List[float]] = dict(named_presets or {})
        self._result_curve: Optional[List[float]] = None

        layout = QVBoxLayout(self)

        # Matplotlib plot
        if _HAS_MPL:
            self._fig = Figure(figsize=(6, 2.8), dpi=100)
            self._fig.patch.set_facecolor("#1e1e23")
            self._ax = self._fig.add_subplot(111)
            self._canvas = FigureCanvasQTAgg(self._fig)
            layout.addWidget(self._canvas, 1)
        else:
            layout.addWidget(QLabel("(matplotlib not available — install it for curve preview)"))

        # Spinboxes row
        spin_group = QGroupBox("Curve samples (center → edge)")
        spin_layout = QGridLayout()
        self._spins: List[QDoubleSpinBox] = []
        for i in range(FALLOFF_SAMPLES):
            r_norm = i / (FALLOFF_SAMPLES - 1)
            lbl = QLabel(f"{r_norm:.1f}")
            lbl.setAlignment(Qt.AlignCenter)
            spin_layout.addWidget(lbl, 0, i)
            sp = QDoubleSpinBox()
            sp.setRange(0.0, 100.0)
            sp.setDecimals(1)
            sp.setSingleStep(5.0)
            sp.setValue(self._curve[i])
            sp.valueChanged.connect(self._on_spin_changed)
            spin_layout.addWidget(sp, 1, i)
            self._spins.append(sp)
        spin_group.setLayout(spin_layout)
        layout.addWidget(spin_group)

        # Ramp presets
        preset_row = QHBoxLayout()
        preset_row.addWidget(QLabel("Shape:"))
        for name, fn in [
            ("Flat", lambda: default_curve()),
            ("Linear", lambda: linear_ramp()),
            ("Quadratic", lambda: quadratic_ramp()),
            ("Sqrt", lambda: sqrt_ramp()),
            ("4th Root", lambda: fourth_root_ramp()),
            ("Smoothstep", lambda: smoothstep_ramp()),
        ]:
            btn = QPushButton(name)
            btn.clicked.connect(lambda checked=False, f=fn: self._apply_preset(f()))
            preset_row.addWidget(btn)

        # Ramp controls
        preset_row.addWidget(QLabel("  Start:"))
        self._start_spin = QDoubleSpinBox()
        self._start_spin.setRange(0.0, 100.0)
        self._start_spin.setValue(100.0)
        self._start_spin.setDecimals(1)
        preset_row.addWidget(self._start_spin)

        preset_row.addWidget(QLabel("End:"))
        self._end_spin = QDoubleSpinBox()
        self._end_spin.setRange(0.0, 100.0)
        self._end_spin.setValue(15.0)
        self._end_spin.setDecimals(1)
        preset_row.addWidget(self._end_spin)

        preset_row.addStretch()
        layout.addLayout(preset_row)

        # Named presets row
        named_row = QHBoxLayout()
        named_row.addWidget(QLabel("Preset:"))
        self._preset_combo = QComboBox()
        self._preset_combo.setMinimumWidth(160)
        self._refresh_preset_combo()
        named_row.addWidget(self._preset_combo)

        load_btn = QPushButton("Load")
        load_btn.clicked.connect(self._load_preset)
        named_row.addWidget(load_btn)

        save_btn = QPushButton("Save As...")
        save_btn.clicked.connect(self._save_preset)
        named_row.addWidget(save_btn)

        del_btn = QPushButton("Delete")
        del_btn.clicked.connect(self._delete_preset)
        named_row.addWidget(del_btn)

        named_row.addStretch()
        layout.addLayout(named_row)

        # Apply / Cancel
        btn_row = QHBoxLayout()
        btn_row.addStretch()
        apply_btn = QPushButton("Apply")
        apply_btn.clicked.connect(self._on_apply)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        btn_row.addWidget(apply_btn)
        btn_row.addWidget(cancel_btn)
        layout.addLayout(btn_row)

        self._update_plot()

    def _on_spin_changed(self) -> None:
        for i, sp in enumerate(self._spins):
            self._curve[i] = sp.value()
        self._update_plot()

    def _apply_preset(self, curve: List[float]) -> None:
        start = self._start_spin.value()
        end = self._end_spin.value()
        # Re-generate with current start/end if it's a ramp-style preset
        if len(curve) == FALLOFF_SAMPLES:
            # Check if it's the default flat
            if all(abs(v - 100.0) < 0.01 for v in curve):
                curve = [start] * FALLOFF_SAMPLES
            else:
                # Scale the curve to start/end range
                mn, mx = min(curve), max(curve)
                if abs(mx - mn) > 0.01:
                    curve = [start + (end - start) * (v - mn) / (mx - mn) for v in curve]
                else:
                    curve = [start] * FALLOFF_SAMPLES
        self._curve = list(curve)
        for i, sp in enumerate(self._spins):
            sp.blockSignals(True)
            sp.setValue(self._curve[i])
            sp.blockSignals(False)
        self._update_plot()

    def _update_plot(self) -> None:
        if not _HAS_MPL:
            return
        ax = self._ax
        ax.clear()
        ax.set_facecolor("#26262b")
        xs = [i / (FALLOFF_SAMPLES - 1) for i in range(FALLOFF_SAMPLES)]
        ax.plot(xs, self._curve, "o-", color="#5dade2", linewidth=2, markersize=5)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 105)
        ax.set_xlabel("Distance / Radius", color="#aaa", fontsize=9)
        ax.set_ylabel("Weight %", color="#aaa", fontsize=9)
        ax.tick_params(colors="#888", labelsize=8)
        ax.grid(True, alpha=0.2)
        self._fig.tight_layout()
        self._canvas.draw()

    def _refresh_preset_combo(self) -> None:
        self._preset_combo.clear()
        for name in sorted(self._named_presets.keys()):
            self._preset_combo.addItem(name)

    def _load_preset(self) -> None:
        name = self._preset_combo.currentText()
        if name in self._named_presets:
            self._apply_preset(list(self._named_presets[name]))

    def _save_preset(self) -> None:
        name, ok = QInputDialog.getText(self, "Save Preset", "Preset name:")
        if ok and name.strip():
            self._named_presets[name.strip()] = list(self._curve)
            self._refresh_preset_combo()
            idx = self._preset_combo.findText(name.strip())
            if idx >= 0:
                self._preset_combo.setCurrentIndex(idx)

    def _delete_preset(self) -> None:
        name = self._preset_combo.currentText()
        if name in self._named_presets:
            self._named_presets.pop(name)
            self._refresh_preset_combo()

    def _on_apply(self) -> None:
        self._result_curve = list(self._curve)
        self.accept()

    @property
    def result_curve(self) -> Optional[List[float]]:
        return self._result_curve

    @property
    def named_presets(self) -> Dict[str, List[float]]:
        return dict(self._named_presets)
