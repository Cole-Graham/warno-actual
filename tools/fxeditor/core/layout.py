"""Vogel spiral disk layout with jitter and template index assignment."""

from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass
from typing import List, Optional, Tuple

GOLDEN_ANGLE = math.pi * (3.0 - math.sqrt(5.0))

_LAYOUT_MIX_SEED = int.from_bytes(
    hashlib.sha256(b"fxeditor_layout_jitter_v1").digest()[:8], "big",
)


def _splitmix64(x: int) -> int:
    x = (x + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
    z = x
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9 & 0xFFFFFFFFFFFFFFFF
    z = (z ^ (z >> 27)) * 0x94D049BB133111EB & 0xFFFFFFFFFFFFFFFF
    return (z ^ (z >> 31)) & 0xFFFFFFFFFFFFFFFF


def _det_u01(index: int) -> float:
    x = (_LAYOUT_MIX_SEED ^ (index * 0xD6E8FEB866772FD1)) & 0xFFFFFFFFFFFFFFFF
    return (_splitmix64(x) & 0xFFFFFFFFFFFFFFFF) / float(2**64)


@dataclass
class BurstPosition:
    x_gameplay_m: float
    y_gameplay_m: float
    template_index: int
    delay_s: Optional[float] = None


def vogel_spiral_layout(
    n_target: int,
    radius_m: float,
    *,
    jitter_frac: float = 0.15,
) -> List[Tuple[float, float]]:
    """Generate *n_target* positions on a disk of *radius_m* using a Vogel spiral.

    ``jitter_frac`` adds a small deterministic radial perturbation to break visible spiral artefacts.
    """
    if n_target <= 0:
        return []
    if n_target == 1:
        return [(0.0, 0.0)]
    out: List[Tuple[float, float]] = []
    for i in range(n_target):
        r = radius_m * math.sqrt((i + 0.5) / n_target)
        theta = i * GOLDEN_ANGLE
        # deterministic jitter
        jr = _det_u01(i * 2) * jitter_frac * radius_m / math.sqrt(n_target)
        jt = _det_u01(i * 2 + 1) * 2.0 * math.pi
        x = r * math.cos(theta) + jr * math.cos(jt)
        y = r * math.sin(theta) + jr * math.sin(jt)
        # clamp to disk
        h = math.hypot(x, y)
        if h > radius_m and h > 1e-9:
            x *= radius_m / h
            y *= radius_m / h
        out.append((float(int(round(x))), float(int(round(y)))))
    return out


def build_burst_positions(
    n_target: int,
    radius_m: float,
    templates: list,
    source_waits: List[float],
    *,
    diversity_ceiling: Optional[int] = None,
    jitter_frac: float = 0.15,
) -> List[BurstPosition]:
    """Full burst list with template indices and per-site delays."""
    from .grouping import distinct_placeable_template_indices

    nt = len(templates)
    if nt == 0:
        return []

    first_indices = distinct_placeable_template_indices(templates)
    n_patterns = len(first_indices)
    if diversity_ceiling is None:
        floor = n_patterns
    else:
        floor = min(n_patterns, max(1, int(diversity_ceiling)))
    n_eff = max(max(1, int(n_target)), floor)

    # template index list: first cover distinct patterns, then round-robin
    indices = list(first_indices[:floor])
    for j in range(n_eff - len(indices)):
        indices.append((len(indices) + j) % nt)

    positions = vogel_spiral_layout(n_eff, radius_m, jitter_frac=jitter_frac)

    out: List[BurstPosition] = []
    for i in range(n_eff):
        x, y = positions[i] if i < len(positions) else (0.0, 0.0)
        ti = indices[i] if i < len(indices) else i % nt
        delay = source_waits[ti % len(source_waits)] if source_waits else None
        out.append(BurstPosition(
            x_gameplay_m=x,
            y_gameplay_m=y,
            template_index=ti,
            delay_s=delay,
        ))
    return out
