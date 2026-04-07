"""Radius falloff curve: interpolation and position-bias resampling.

Repositions bursts so radial density follows the curve; no quantity reduction.
"""

from __future__ import annotations

import hashlib
import math
from typing import Dict, List, Optional, Sequence, Tuple

FALLOFF_SAMPLES = 11

_BIAS_SEED = int.from_bytes(
    hashlib.sha256(b"fxeditor_falloff_bias_v1").digest()[:8], "big",
)


def _splitmix64(x: int) -> int:
    x = (x + 0x9E3779B97F4A7C15) & 0xFFFFFFFFFFFFFFFF
    z = x
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9 & 0xFFFFFFFFFFFFFFFF
    z = (z ^ (z >> 27)) * 0x94D049BB133111EB & 0xFFFFFFFFFFFFFFFF
    return (z ^ (z >> 31)) & 0xFFFFFFFFFFFFFFFF


def _det_u01(slot: int) -> float:
    x = (_BIAS_SEED ^ (int(slot) * 0xC6BC279692B5C323)) & 0xFFFFFFFFFFFFFFFF
    return (_splitmix64(x) & 0xFFFFFFFFFFFFFFFF) / float(2**64)


def align_curve(curve: Sequence[float], n: int = FALLOFF_SAMPLES) -> List[float]:
    if n <= 0:
        return []
    if len(curve) >= n:
        return [float(x) for x in curve[:n]]
    out = [float(x) for x in curve]
    out.extend([100.0] * (n - len(out)))
    return out


def interp_falloff_pct(curve: Sequence[float], r_norm: float) -> float:
    """Linear interpolation: r_norm in [0,1] (center -> edge)."""
    n = len(curve)
    if n == 0:
        return 100.0
    if n == 1:
        return float(curve[0])
    r = max(0.0, min(1.0, float(r_norm)))
    x = r * (n - 1)
    i = min(int(math.floor(x)), n - 2)
    t = x - i
    return float(curve[i]) + t * (float(curve[min(i + 1, n - 1)]) - float(curve[i]))


def _weight_at(curve: List[float], r_norm: float) -> float:
    pct = interp_falloff_pct(curve, r_norm)
    return max(1e-15, pct / 100.0)


def _sample_r_norm_from_marginal(
    curve: List[float],
    u: float,
    *,
    n_steps: int = 129,
) -> float:
    """Inverse-CDF sample of r_norm with marginal density proportional to w(r)*r on the disk."""
    n = max(8, n_steps)
    r_grid = [j / (n - 1) for j in range(n)]
    seg_mass: List[float] = []
    for j in range(n - 1):
        r0, r1 = r_grid[j], r_grid[j + 1]
        dr = r1 - r0
        w0 = _weight_at(curve, r0)
        w1 = _weight_at(curve, r1)
        seg_mass.append(0.5 * (r0 * w0 + r1 * w1) * dr)
    z = sum(seg_mass)
    if z < 1e-30:
        return max(0.0, min(1.0, float(u)))
    uu = max(0.0, min(1.0, float(u))) * z
    acc = 0.0
    for j, m in enumerate(seg_mass):
        if acc + m >= uu - 1e-15:
            if m < 1e-30:
                return r_grid[j]
            t = (uu - acc) / m
            return r_grid[j] + t * (r_grid[j + 1] - r_grid[j])
        acc += m
    return 1.0


def apply_falloff_position_bias(
    positions: List[Tuple[float, float]],
    curve: Sequence[float],
    target_radius_m: float,
) -> List[Tuple[float, float]]:
    """Reposition bursts so radial distribution follows the falloff curve.

    Does NOT change the count. Each burst gets a new (x, y) from the curve-biased
    radial density. Deterministic per burst index.
    """
    if not positions or not curve:
        return list(positions)
    aligned = align_curve(curve)
    # check if curve is effectively flat 100%
    if all(abs(v - 100.0) < 1e-6 for v in aligned):
        return list(positions)

    tr = max(float(target_radius_m), 1e-9)
    out: List[Tuple[float, float]] = []
    for i, (ox, oy) in enumerate(positions):
        u_r = _det_u01(i * 2 + 11)
        u_th = _det_u01(i * 2 + 104729)
        r_norm = _sample_r_norm_from_marginal(aligned, u_r)
        r_game = r_norm * tr
        theta = 2.0 * math.pi * u_th
        gx = r_game * math.cos(theta)
        gy = r_game * math.sin(theta)
        gx = float(int(round(gx)))
        gy = float(int(round(gy)))
        h = math.hypot(gx, gy)
        if h > tr and h > 1e-9:
            gx = float(int(round(gx * tr / h)))
            gy = float(int(round(gy * tr / h)))
        out.append((gx, gy))
    return out


def default_curve() -> List[float]:
    """Flat 100% everywhere (no bias)."""
    return [100.0] * FALLOFF_SAMPLES


# ── Preset generators ────────────────────────────────────────────

def linear_ramp(start: float = 100.0, end: float = 15.0) -> List[float]:
    return [start + (end - start) * i / (FALLOFF_SAMPLES - 1) for i in range(FALLOFF_SAMPLES)]


def quadratic_ramp(start: float = 100.0, end: float = 15.0) -> List[float]:
    return [start + (end - start) * (i / (FALLOFF_SAMPLES - 1)) ** 2 for i in range(FALLOFF_SAMPLES)]


def sqrt_ramp(start: float = 100.0, end: float = 15.0) -> List[float]:
    return [start + (end - start) * math.sqrt(i / (FALLOFF_SAMPLES - 1)) for i in range(FALLOFF_SAMPLES)]


def smoothstep_ramp(start: float = 100.0, end: float = 15.0) -> List[float]:
    def ss(t: float) -> float:
        return t * t * (3 - 2 * t)
    return [start + (end - start) * ss(i / (FALLOFF_SAMPLES - 1)) for i in range(FALLOFF_SAMPLES)]


def fourth_root_ramp(start: float = 100.0, end: float = 15.0) -> List[float]:
    return [start + (end - start) * (i / (FALLOFF_SAMPLES - 1)) ** 0.25 for i in range(FALLOFF_SAMPLES)]
