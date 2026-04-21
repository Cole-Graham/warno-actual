"""Scrollable panel showing analyzed effect groups with VFX visibility checkboxes."""

from __future__ import annotations

from typing import Dict, List, Optional, Set

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from ..core.grouping import EffectGroupRow, format_effect_group_block


class EffectGroupPanel(QWidget):
    """Displays effect groups and VFX visibility toggles."""

    visibility_changed = Signal(dict)  # {vfx_name: bool}

    def __init__(self, parent=None):
        super().__init__(parent)
        self._groups: List[EffectGroupRow] = []
        self._vfx_checks: Dict[str, QCheckBox] = {}
        self._n0_label: Optional[QLabel] = None

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self._n0_label = QLabel("Composite sites: —")
        self._n0_label.setStyleSheet("font-weight: bold; padding: 4px;")
        layout.addWidget(self._n0_label)

        # VFX visibility section
        self._vis_box = QGroupBox("VFX Visibility")
        self._vis_layout = QVBoxLayout()
        self._vis_box.setLayout(self._vis_layout)
        layout.addWidget(self._vis_box)

        # Effect groups scroll area
        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)
        self._scroll_content = QWidget()
        self._scroll_layout = QVBoxLayout(self._scroll_content)
        self._scroll_layout.setContentsMargins(4, 4, 4, 4)
        self._scroll.setWidget(self._scroll_content)
        layout.addWidget(self._scroll, 1)

    def set_groups(
        self,
        groups: List[EffectGroupRow],
        n0: int,
        initial_visibility: Optional[Dict[str, bool]] = None,
        classification_summary: str = "",
    ) -> None:
        self._groups = groups

        # Update N0 label with classification summary
        if classification_summary:
            self._n0_label.setText(f"Composite sites: {n0}\n{classification_summary}")
            self._n0_label.setWordWrap(True)
        else:
            self._n0_label.setText(f"Composite sites: {n0}")

        # Rebuild VFX checkboxes
        for cb in self._vfx_checks.values():
            self._vis_layout.removeWidget(cb)
            cb.deleteLater()
        self._vfx_checks.clear()

        all_vfx: Set[str] = set()
        for g in groups:
            for branch in g.pattern:
                for vfx in branch:
                    all_vfx.add(vfx)

        for vfx in sorted(all_vfx):
            cb = QCheckBox(vfx)
            checked = True
            if initial_visibility and vfx in initial_visibility:
                checked = initial_visibility[vfx]
            cb.setChecked(checked)
            cb.stateChanged.connect(self._on_toggle)
            self._vis_layout.addWidget(cb)
            self._vfx_checks[vfx] = cb

        # Rebuild effect group blocks
        while self._scroll_layout.count():
            item = self._scroll_layout.takeAt(0)
            w = item.widget()
            if w:
                w.deleteLater()

        for i, g in enumerate(groups, start=1):
            block_text = format_effect_group_block(g, i)
            lbl = QLabel(block_text)
            lbl.setWordWrap(True)
            lbl.setStyleSheet("font-family: 'Consolas', 'Courier New', monospace; font-size: 11px; padding: 6px; background: #2a2a2f; border-radius: 4px; margin-bottom: 4px;")
            self._scroll_layout.addWidget(lbl)

        self._scroll_layout.addStretch()

    def _on_toggle(self) -> None:
        vis = {name: cb.isChecked() for name, cb in self._vfx_checks.items()}
        self.visibility_changed.emit(vis)

    def get_visibility(self) -> Dict[str, bool]:
        return {name: cb.isChecked() for name, cb in self._vfx_checks.items()}
