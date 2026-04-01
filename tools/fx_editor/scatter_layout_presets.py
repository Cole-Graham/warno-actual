"""Shared gameplay disk layout (used by scatter UI and batch cluster variations).

Base positions use area-uniform float sampling on the target disk. When ``source_xy`` is present,
scaled template residuals are added on top. Per-burst segment clip to the disk boundary still put
many points on the rim (the chord meets the circle). A **global** residual scale κ = min_j t_j
(max t with ‖A+tB‖≤R per burst) applies the same κ to all bursts so almost all land **inside** the
disk, not on the perimeter. Residual is also damped when target ≫ source.
"""

from __future__ import annotations

import hashlib
import math
from typing import List, Tuple


def _hypot_sq(x: float, y: float) -> float:
    return x * x + y * y


def _clamp_disk_xy(x: float, y: float, radius_m: float) -> Tuple[float, float]:
    """Project ``(x,y)`` onto the circle of radius ``radius_m`` (origin-centered). Last resort only."""
    if radius_m <= 0:
        return 0.0, 0.0
    d = math.hypot(x, y)
    if d <= radius_m + 1e-9:
        return x, y
    if d < 1e-15:
        return 0.0, 0.0
    s = radius_m / d
    return x * s, y * s


def _max_t_segment_in_closed_disk(ax: float, ay: float, bx: float, by: float, r: float) -> float:
    """Largest ``t`` in ``[0, 1]`` with ``‖(ax+t*bx, ay+t*by)‖ ≤ r`` (chord inside disk, not radial from origin)."""
    r2 = r * r + 1e-9
    if _hypot_sq(ax + bx, ay + by) <= r2:
        return 1.0
    if _hypot_sq(ax, ay) > r2:
        return 0.0
    lo, hi = 0.0, 1.0
    for _ in range(56):
        mid = 0.5 * (lo + hi)
        if _hypot_sq(ax + mid * bx, ay + mid * by) <= r2:
            lo = mid
        else:
            hi = mid
    return lo


def _uniform_disk_points_deterministic(n: int, radius_m: float, salt: str) -> List[Tuple[float, float]]:
    """Area-uniform samples on a disk (sqrt factor for uniform area)."""
    r = max(1e-6, float(radius_m))
    out: List[Tuple[float, float]] = []
    for j in range(n):
        raw = hashlib.sha256(f'{salt}\0udisk\0{j}'.encode('utf-8')).digest()
        u1 = int.from_bytes(raw[0:8], 'big') / (2**64)
        u2 = int.from_bytes(raw[8:16], 'big') / (2**64)
        rr = math.sqrt(max(u1, 1e-15)) * r
        th = 2 * math.pi * u2
        cx, cy = rr * math.cos(th), rr * math.sin(th)
        if _hypot_sq(cx, cy) <= r * r + 1e-9:
            out.append((cx, cy))
        else:
            out.append(_clamp_disk_xy(cx, cy, r))
    return out


def hex_grid_bursts_gameplay_m(preset_n: int, r_m: float) -> List[Tuple[float, float]]:
    """Float samples on concentric rings (reference for residual pairing with source templates)."""
    r = max(1.0, r_m)
    rings = max(1, preset_n // 6)
    pts: List[Tuple[float, float]] = [(0.0, 0.0)]
    for ring in range(1, rings + 1):
        frac = ring / rings
        rr = r * frac * (1.0 - 0.11 * frac)
        k = max(6, ring * 6)
        for i in range(k):
            th = 2 * math.pi * i / k
            pts.append((rr * math.cos(th), rr * math.sin(th)))
    return pts


def hex_grid_first_n_bursts(n: int, r_m: float) -> List[Tuple[float, float]]:
    if n <= 0:
        return []
    p = 6
    while True:
        pts = hex_grid_bursts_gameplay_m(p, r_m)
        if len(pts) >= n:
            return pts[:n]
        p += 6
        if p > 10000:
            raise ValueError('Could not generate enough hex points')


def gameplay_hex_with_source_residual(
    n_target: int,
    target_radius_m: float,
    source_radius_m: float,
    source_xy: List[Tuple[float, float]],
    *,
    jitter_salt: str = '',
) -> List[Tuple[float, float]]:
    """Place ``n_target`` bursts: uniform disk base + globally scaled residual (κ) to avoid rim pile-up."""
    r = max(1.0, float(target_radius_m))
    salt = jitter_salt or f'residual:{target_radius_m:g}:{source_radius_m:g}'
    if n_target <= 0:
        return []

    if not source_xy:
        return _uniform_disk_points_deterministic(n_target, r, salt + ':base')

    ns = len(source_xy)
    sr = max(1e-6, float(source_radius_m))
    hex_src = hex_grid_first_n_bursts(ns, max(1.0, sr))
    if len(hex_src) != ns:
        return _uniform_disk_points_deterministic(n_target, r, salt + ':fallback')

    hex_tgt = _uniform_disk_points_deterministic(n_target, r, salt + ':tgt')
    scale = r / sr
    # When target ≫ source, raw (target/source)*residual pushes most points outside the disk;
    # radial clamp then put ~all of them on the rim. Damp toward source-sized offsets in target space.
    # Initial damp (kappa will further shrink B so the whole batch stays in-disk).
    residual_damp = min(1.0, 2.0 * (sr / r))

    t_list: List[float] = []
    for j in range(n_target):
        i = j % ns
        ax, ay = hex_tgt[j]
        if _hypot_sq(ax, ay) > r * r + 1e-6:
            ax, ay = _clamp_disk_xy(ax, ay, r)
        rx = source_xy[i][0] - hex_src[i][0]
        ry = source_xy[i][1] - hex_src[i][1]
        bx = rx * scale * residual_damp
        by = ry * scale * residual_damp
        t_list.append(_max_t_segment_in_closed_disk(ax, ay, bx, by, r))

    kappa = min(t_list) if t_list else 1.0
    kappa *= 1.0 - 1e-6

    out: List[Tuple[float, float]] = []
    for j in range(n_target):
        i = j % ns
        ax, ay = hex_tgt[j]
        if _hypot_sq(ax, ay) > r * r + 1e-6:
            ax, ay = _clamp_disk_xy(ax, ay, r)
        rx = source_xy[i][0] - hex_src[i][0]
        ry = source_xy[i][1] - hex_src[i][1]
        bx = rx * scale * residual_damp
        by = ry * scale * residual_damp
        px, py = ax + kappa * bx, ay + kappa * by
        if _hypot_sq(px, py) > r * r + 1e-6:
            px, py = _clamp_disk_xy(px, py, r)
        out.append((px, py))
    return out
