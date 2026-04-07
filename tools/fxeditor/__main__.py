"""Entry point: python -m tools.fxeditor"""

from __future__ import annotations

import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)


def main() -> None:
    from PySide6.QtWidgets import QApplication
    from PySide6.QtCore import Qt

    app = QApplication.instance() or QApplication(sys.argv)
    app.setStyle("Fusion")

    # Dark palette
    from PySide6.QtGui import QPalette, QColor
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(45, 45, 50))
    palette.setColor(QPalette.WindowText, QColor(210, 210, 215))
    palette.setColor(QPalette.Base, QColor(35, 35, 40))
    palette.setColor(QPalette.AlternateBase, QColor(50, 50, 55))
    palette.setColor(QPalette.ToolTipBase, QColor(60, 60, 65))
    palette.setColor(QPalette.ToolTipText, QColor(210, 210, 215))
    palette.setColor(QPalette.Text, QColor(210, 210, 215))
    palette.setColor(QPalette.Button, QColor(55, 55, 60))
    palette.setColor(QPalette.ButtonText, QColor(210, 210, 215))
    palette.setColor(QPalette.BrightText, QColor(255, 60, 60))
    palette.setColor(QPalette.Link, QColor(93, 173, 226))
    palette.setColor(QPalette.Highlight, QColor(70, 130, 180))
    palette.setColor(QPalette.HighlightedText, QColor(240, 240, 245))
    app.setPalette(palette)

    from .ui.main_window import MainWindow
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
