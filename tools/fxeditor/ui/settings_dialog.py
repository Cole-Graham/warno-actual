"""Settings dialog: calibration, naming, floors, size-param allowlists, budget."""

from __future__ import annotations

import math
from typing import Dict, List, Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
)

from .state import AppState


class SettingsDialog(QDialog):
    def __init__(self, state: AppState, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setMinimumSize(520, 420)
        self.resize(580, 480)
        self._state = state
        self._accepted = False

        layout = QVBoxLayout(self)
        tabs = QTabWidget()
        layout.addWidget(tabs)

        # ── Calibration tab ──────────────────────────────────────
        cal_tab = QGroupBox()
        cal_layout = QVBoxLayout(cal_tab)

        row1 = QHBoxLayout()
        row1.addWidget(QLabel("Reference gameplay radius (m):"))
        self._ref_m_spin = QDoubleSpinBox()
        self._ref_m_spin.setRange(0.1, 10000.0)
        self._ref_m_spin.setDecimals(2)
        self._ref_m_spin.setValue(state.get("calibration_ref_m", 60.0))
        row1.addWidget(self._ref_m_spin)
        cal_layout.addLayout(row1)

        row2 = QHBoxLayout()
        row2.addWidget(QLabel("Anchor max NDF radius:"))
        self._anchor_spin = QDoubleSpinBox()
        self._anchor_spin.setRange(0.1, 100000.0)
        self._anchor_spin.setDecimals(6)
        self._anchor_spin.setValue(state.get("calibration_anchor_r", 4240.282686))
        row2.addWidget(self._anchor_spin)
        cal_layout.addLayout(row2)

        reload_btn = QPushButton("Reload from YAML")
        reload_btn.clicked.connect(self._reload_yaml)
        cal_layout.addWidget(reload_btn)
        cal_layout.addStretch()

        tabs.addTab(cal_tab, "Calibration")

        # ── Naming tab ───────────────────────────────────────────
        name_tab = QGroupBox()
        name_layout = QVBoxLayout(name_tab)

        name_layout.addWidget(QLabel("Filename template:"))
        self._template_edit = QLineEdit(state.naming_template)
        self._template_edit.textChanged.connect(self._update_name_preview)
        name_layout.addWidget(self._template_edit)

        self._name_preview = QLabel("")
        self._name_preview.setStyleSheet("color: #888; font-style: italic;")
        name_layout.addWidget(self._name_preview)
        self._update_name_preview()
        name_layout.addStretch()

        tabs.addTab(name_tab, "Naming")

        # ── Param Scaling tab ─────────────────────────────────────
        floor_tab = QGroupBox()
        floor_layout = QVBoxLayout(floor_tab)

        floor_layout.addWidget(QLabel(
            "These options scale per-call size and count parameters "
            "(e.g. parSize, parCount) alongside the spatial scaling. "
            "Both are OFF by default -- the scaler only changes the "
            "number and positions of VFX calls.",
        ))

        self._scale_sizes_cb = QCheckBox("Scale size parameters (parSize, parRadius, etc.)")
        self._scale_sizes_cb.setChecked(state.get("scale_sizes", False))
        floor_layout.addWidget(self._scale_sizes_cb)

        self._scale_counts_cb = QCheckBox("Scale count parameters (parCount, parCountDebrits, etc.)")
        self._scale_counts_cb.setChecked(state.get("scale_counts", False))
        floor_layout.addWidget(self._scale_counts_cb)

        r3 = QHBoxLayout()
        r3.addWidget(QLabel("Minimum burst count:"))
        self._min_burst_spin = QSpinBox()
        self._min_burst_spin.setRange(1, 100)
        self._min_burst_spin.setValue(state.get("min_burst_count", 3))
        r3.addWidget(self._min_burst_spin)
        floor_layout.addLayout(r3)

        r4 = QHBoxLayout()
        r4.addWidget(QLabel("Minimum size param ratio (scale-down floor):"))
        self._min_size_spin = QDoubleSpinBox()
        self._min_size_spin.setRange(0.0, 1.0)
        self._min_size_spin.setDecimals(2)
        self._min_size_spin.setSingleStep(0.05)
        self._min_size_spin.setValue(state.get("min_size_ratio", 0.3))
        r4.addWidget(self._min_size_spin)
        floor_layout.addLayout(r4)

        r5 = QHBoxLayout()
        r5.addWidget(QLabel("Minimum count param value:"))
        self._min_count_spin = QSpinBox()
        self._min_count_spin.setRange(0, 100)
        self._min_count_spin.setValue(state.get("min_count_value", 1))
        r5.addWidget(self._min_count_spin)
        floor_layout.addLayout(r5)

        floor_layout.addStretch()
        tabs.addTab(floor_tab, "Param Scaling")

        # ── Budget tab ───────────────────────────────────────────
        budget_tab = QGroupBox()
        budget_layout = QVBoxLayout(budget_tab)

        r6 = QHBoxLayout()
        r6.addWidget(QLabel("TActionCall cap:"))
        self._cap_spin = QSpinBox()
        self._cap_spin.setRange(200, 2000)
        self._cap_spin.setValue(state.taction_call_cap)
        self._cap_spin.setToolTip(
            "Maximum TActionCall rows per output file. Lower values prevent engine culling "
            "when multiple effects fire simultaneously (e.g. 12-missile MLRS salvo)."
        )
        r6.addWidget(self._cap_spin)
        budget_layout.addLayout(r6)

        budget_layout.addWidget(QLabel(
            "Once the cap is reached, larger radii spread the same number of "
            "composite events across a wider area.",
        ))
        budget_layout.addStretch()
        tabs.addTab(budget_tab, "Budget")

        # ── Buttons ──────────────────────────────────────────────
        btn_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel | QDialogButtonBox.Apply,
        )
        btn_box.accepted.connect(self._on_ok)
        btn_box.rejected.connect(self.reject)
        btn_box.button(QDialogButtonBox.Apply).clicked.connect(self._apply_to_state)
        layout.addWidget(btn_box)

    def _reload_yaml(self) -> None:
        from ..core.config import load_config
        cfg = load_config()
        self._ref_m_spin.setValue(cfg.reference_gameplay_radius_m)
        self._anchor_spin.setValue(cfg.anchor_max_ndf_radius)

    def _update_name_preview(self) -> None:
        tmpl = self._template_edit.text()
        rn = self._state.rootname or "fx_impact_mlrs_cluster_ap"
        preview = tmpl.replace("{rootname}", rn).replace("{radiusinmeters}", "250").replace("{n}", "1").replace("{suffix}", "_1")
        self._name_preview.setText(f"Preview: {preview}")

    def _apply_to_state(self) -> None:
        self._state.set("calibration_ref_m", self._ref_m_spin.value())
        self._state.set("calibration_anchor_r", self._anchor_spin.value())
        self._state.naming_template = self._template_edit.text()
        self._state.set("scale_sizes", self._scale_sizes_cb.isChecked())
        self._state.set("scale_counts", self._scale_counts_cb.isChecked())
        self._state.set("min_burst_count", self._min_burst_spin.value())
        self._state.set("min_size_ratio", self._min_size_spin.value())
        self._state.set("min_count_value", self._min_count_spin.value())
        self._state.taction_call_cap = self._cap_spin.value()

    def _on_ok(self) -> None:
        self._apply_to_state()
        self._accepted = True
        self.accept()

    @property
    def was_accepted(self) -> bool:
        return self._accepted
