"""QThread for batch VFX generation with progress signals."""

from __future__ import annotations

from pathlib import Path
from typing import List

from PySide6.QtCore import QThread, Signal

from ..core.scaler import ScaleResult, ScalerConfig, scale_batch


class GenerateWorker(QThread):
    """Runs scale_batch in a background thread."""

    progress = Signal(int, int, object)  # done, total, ScaleResult
    finished_all = Signal(list)  # List[ScaleResult]
    error = Signal(str)

    def __init__(
        self,
        source_paths: List[Path],
        config: ScalerConfig,
        parent=None,
    ):
        super().__init__(parent)
        self._source_paths = source_paths
        self._config = config

    def run(self) -> None:
        try:
            results = scale_batch(
                self._source_paths,
                self._config,
                progress_callback=self._on_progress,
            )
            self.finished_all.emit(results)
        except Exception as exc:
            self.error.emit(str(exc))

    def _on_progress(self, done: int, total: int, result: ScaleResult) -> None:
        self.progress.emit(done, total, result)
