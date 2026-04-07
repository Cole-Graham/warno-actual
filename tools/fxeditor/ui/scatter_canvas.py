"""2D scatter preview widget with QPainter — VFX-colored dots, radius circles, timeline scrubber."""

from __future__ import annotations

import hashlib
import math
from typing import Dict, List, Optional, Set, Tuple

from PySide6.QtCore import QPointF, QRectF, Qt, Signal
from PySide6.QtGui import QBrush, QColor, QPainter, QPen, QFont
from PySide6.QtWidgets import QWidget, QToolTip


def _vfx_color(name: str) -> QColor:
    """Stable hash-based color for a VFX short name."""
    h = int(hashlib.md5(name.encode()).hexdigest()[:6], 16)
    hue = h % 360
    return QColor.fromHsv(hue, 200, 220)


class ScatterDot:
    __slots__ = ("x", "y", "vfx", "index", "delay_s", "template_index")

    def __init__(
        self,
        x: float,
        y: float,
        vfx: str,
        index: int,
        delay_s: float = 0.0,
        template_index: int = 0,
    ):
        self.x = x
        self.y = y
        self.vfx = vfx
        self.index = index
        self.delay_s = delay_s
        self.template_index = template_index


class ScatterCanvas(QWidget):
    """2D top-down scatter preview of burst positions."""

    dot_hovered = Signal(int)  # burst index

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(400, 400)
        self.setMouseTracking(True)

        self._dots: List[ScatterDot] = []
        self._target_radius_m: float = 250.0
        self._view_radius_m: float = 300.0
        self._visible_vfx: Set[str] = set()
        self._timeline_t: Optional[float] = None
        self._hovered_index: int = -1
        self._taction_count: int = 0
        self._taction_cap: int = 600
        self._tsim_count: int = 0

    def set_dots(self, dots: List[ScatterDot]) -> None:
        self._dots = list(dots)
        self._visible_vfx = {d.vfx for d in dots}
        self.update()

    def set_target_radius(self, r: float) -> None:
        self._target_radius_m = max(1.0, float(r))
        self.update()

    def set_view_radius(self, r: float) -> None:
        self._view_radius_m = max(1.0, float(r))
        self.update()

    def set_vfx_visibility(self, vis: Dict[str, bool]) -> None:
        self._visible_vfx = {k for k, v in vis.items() if v}
        self.update()

    def set_timeline_t(self, t: Optional[float]) -> None:
        self._timeline_t = t
        self.update()

    def set_taction_info(self, count: int, cap: int) -> None:
        self._taction_count = count
        self._taction_cap = cap
        self.update()

    def set_tsim_count(self, count: int) -> None:
        self._tsim_count = count
        self.update()

    def _world_to_screen(self, wx: float, wy: float) -> QPointF:
        w = self.width()
        h = self.height()
        side = min(w, h) - 20
        scale = side / (2.0 * self._view_radius_m) if self._view_radius_m > 0 else 1.0
        cx, cy = w / 2.0, h / 2.0
        return QPointF(cx + wx * scale, cy - wy * scale)

    def _world_radius_to_px(self, r: float) -> float:
        side = min(self.width(), self.height()) - 20
        scale = side / (2.0 * self._view_radius_m) if self._view_radius_m > 0 else 1.0
        return r * scale

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        p.fillRect(self.rect(), QColor(30, 30, 35))

        center = self._world_to_screen(0, 0)

        # Crosshair axes
        pen_axis = QPen(QColor(60, 60, 70), 1, Qt.DashLine)
        p.setPen(pen_axis)
        p.drawLine(QPointF(0, center.y()), QPointF(self.width(), center.y()))
        p.drawLine(QPointF(center.x(), 0), QPointF(center.x(), self.height()))

        # Target radius circle
        tr_px = self._world_radius_to_px(self._target_radius_m)
        pen_target = QPen(QColor(120, 120, 140), 1.5, Qt.DashLine)
        p.setPen(pen_target)
        p.setBrush(Qt.NoBrush)
        p.drawEllipse(center, tr_px, tr_px)

        # Dots
        dot_r = max(3.0, min(8.0, tr_px / max(1, len(self._dots)) * 2))
        for dot in self._dots:
            if dot.vfx not in self._visible_vfx:
                continue
            fired = True
            alpha = 255
            if self._timeline_t is not None:
                if dot.delay_s > self._timeline_t:
                    fired = False
                    alpha = 60

            color = _vfx_color(dot.vfx)
            color.setAlpha(alpha)
            pt = self._world_to_screen(dot.x, dot.y)

            p.setPen(Qt.NoPen)
            p.setBrush(QBrush(color))
            p.drawEllipse(pt, dot_r, dot_r)

            if fired and self._timeline_t is not None:
                ring_pen = QPen(QColor(255, 215, 0, alpha), 1.5)
                p.setPen(ring_pen)
                p.setBrush(Qt.NoBrush)
                p.drawEllipse(pt, dot_r + 2, dot_r + 2)

            if dot.index == self._hovered_index:
                hover_pen = QPen(QColor(255, 255, 255), 2.0)
                p.setPen(hover_pen)
                p.setBrush(Qt.NoBrush)
                p.drawEllipse(pt, dot_r + 4, dot_r + 4)

        # TActionCall count overlay
        font = QFont("Segoe UI", 9)
        p.setFont(font)
        if self._taction_count > 0:
            if self._taction_count > self._taction_cap:
                tc_color = QColor(220, 80, 60)
            elif self._taction_count > self._taction_cap * 0.85:
                tc_color = QColor(220, 180, 40)
            else:
                tc_color = QColor(160, 200, 160)
            p.setPen(tc_color)
            p.drawText(
                QRectF(10, self.height() - 30, 300, 25),
                Qt.AlignLeft | Qt.AlignVCenter,
                f"TActionCalls: {self._taction_count} / {self._taction_cap}",
            )

        # Header overlay
        visible_count = sum(1 for d in self._dots if d.vfx in self._visible_vfx)
        total_count = len(self._dots)
        tsim_text = f"  |  TSimultaneous: {self._tsim_count}" if self._tsim_count > 0 else ""
        p.setPen(QColor(180, 180, 190))
        p.drawText(
            QRectF(10, 8, 500, 20),
            Qt.AlignLeft | Qt.AlignVCenter,
            f"Dots: {visible_count}/{total_count}{tsim_text}  |  Radius: {self._target_radius_m:g}m",
        )

        p.end()

    def mouseMoveEvent(self, event):
        pos = event.position() if hasattr(event, "position") else event.localPos()
        best = -1
        best_d = 15.0
        for dot in self._dots:
            if dot.vfx not in self._visible_vfx:
                continue
            pt = self._world_to_screen(dot.x, dot.y)
            d = math.hypot(pos.x() - pt.x(), pos.y() - pt.y())
            if d < best_d:
                best_d = d
                best = dot.index
        if best != self._hovered_index:
            self._hovered_index = best
            self.update()
            if best >= 0:
                dot = next((d for d in self._dots if d.index == best), None)
                if dot:
                    QToolTip.showText(
                        event.globalPosition().toPoint() if hasattr(event, "globalPosition") else event.globalPos().toPoint(),
                        f"#{dot.index}  {dot.vfx}\n"
                        f"pos: ({dot.x:g}, {dot.y:g})m\n"
                        f"delay: {dot.delay_s:g}s",
                    )
            self.dot_hovered.emit(best)

    def leaveEvent(self, event):
        self._hovered_index = -1
        self.update()
