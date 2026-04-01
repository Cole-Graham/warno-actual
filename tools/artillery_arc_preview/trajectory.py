"""Parabolic artillery preview for constant horizontal speed + launch pitch (PitchForParabolic, SpeedGRU).

Engine model (upcoming): horizontal speed v_x = SpeedGRU (GRU/s), launch pitch from horizontal =
PitchForParabolic (rad), strictly in (0, pi/2). Vertical component v_y0 = v_x * tan(pitch).

Same launch and landing height:

    x(t) = v_x * t
    y(t) = v_y0 * t - g t^2 / 2

Ground range to first impact: R = 2 v_x^2 tan(pitch) / g
Flight time: T = 2 v_y0 / g = 2 v_x tan(pitch) / g

Height along ground distance x (0 <= x <= R):

    y(x) = x tan(pitch) - g x^2 / (2 v_x^2)
"""

from __future__ import annotations

import math
from typing import List, Optional, Tuple

PITCH_MIN_RAD = 1e-6
PITCH_MAX_RAD = math.pi / 2 - 1e-6


def vertical_speed_gru(speed_horizontal_gru: float, pitch_rad: float) -> float:
    return speed_horizontal_gru * math.tan(pitch_rad)


def max_range_horizontal_pitch(speed_horizontal_gru: float, pitch_rad: float, g: float) -> float:
    """Same-elevation impact range for constant horizontal speed and launch pitch."""
    if g <= 0:
        raise ValueError("g must be positive")
    return 2.0 * speed_horizontal_gru * speed_horizontal_gru * math.tan(pitch_rad) / g


def flight_time_full_arc(speed_horizontal_gru: float, pitch_rad: float, g: float) -> float:
    return 2.0 * speed_horizontal_gru * math.tan(pitch_rad) / g


def height_at_horizontal_x(
    speed_horizontal_gru: float,
    pitch_rad: float,
    g: float,
    x_gru: float,
) -> float:
    """Height at ground distance x along the aim plane (side view)."""
    if x_gru < 0:
        raise ValueError("x must be non-negative")
    t = math.tan(pitch_rad)
    return t * x_gru - 0.5 * g * x_gru * x_gru / (speed_horizontal_gru * speed_horizontal_gru)


def pitch_rad_for_range_to_same_elevation(
    speed_horizontal_gru: float,
    g: float,
    range_gru: float,
) -> float:
    """Unique launch pitch (rad) so the round lands at range_gru with same launch/landing height."""
    if speed_horizontal_gru <= 0 or g <= 0 or range_gru <= 0:
        raise ValueError("speed, g, and range must be positive")
    return math.atan(g * range_gru / (2.0 * speed_horizontal_gru * speed_horizontal_gru))


def pitch_band_rad_for_range_interval(
    speed_horizontal_gru: float,
    g: float,
    r_min: float,
    r_max: float,
) -> Tuple[float, float]:
    """Monotone: for fixed horizontal speed, range R = 2 v_x^2 tan(theta)/g => one pitch interval."""
    if r_min <= 0 or r_max <= 0 or r_min > r_max:
        raise ValueError("need 0 < r_min <= r_max")
    lo = pitch_rad_for_range_to_same_elevation(speed_horizontal_gru, g, r_min)
    hi = pitch_rad_for_range_to_same_elevation(speed_horizontal_gru, g, r_max)
    return (lo, hi)


def horizontal_speed_gru_for_range_and_pitch(range_gru: float, pitch_rad: float, g: float) -> float:
    """Horizontal speed (GRU/s) so same-elevation impact is at range_gru for the given launch pitch.

    R = 2 v_x^2 tan(pitch) / g  =>  v_x = sqrt(R g / (2 tan(pitch))).
    """
    if range_gru <= 0 or g <= 0:
        raise ValueError("range and g must be positive")
    if pitch_rad <= PITCH_MIN_RAD or pitch_rad >= PITCH_MAX_RAD:
        raise ValueError("PitchForParabolic must be in (0, pi/2) radians")
    t = math.tan(pitch_rad)
    if t <= 0:
        raise ValueError("tan(pitch) must be positive")
    return math.sqrt(range_gru * g / (2.0 * t))


def pitch_band_for_fixed_target_range(
    v_ref: float,
    g: float,
    r_target: float,
    r_min: float,
    r_max: float,
) -> Tuple[float, float]:
    """Pitch interval (rad) for arcs that land at r_target while varying loft.

    Uses reference horizontal speed v_ref only to relate weapon min/max range to two reference
    pitches p_rmin, p_rmax (same-elevation shots at r_min and r_max at speed v_ref). For each,
    the horizontal speed that would land at r_target at that loft is v = sqrt(r_target g / (2 tan(p))).
    Pitch values that hit r_target with v between those two implied speeds form [pitch_lo, pitch_hi].
    """
    if r_target <= 0 or g <= 0 or v_ref <= 0:
        raise ValueError("r_target, g, and reference speed must be positive")
    if r_min <= 0 or r_max <= 0 or r_min > r_max:
        raise ValueError("need 0 < r_min <= r_max")
    p_rmin = pitch_rad_for_range_to_same_elevation(v_ref, g, r_min)
    p_rmax = pitch_rad_for_range_to_same_elevation(v_ref, g, r_max)
    t_min = math.tan(p_rmin)
    t_max = math.tan(p_rmax)
    if t_min <= 0 or t_max <= 0:
        raise ValueError("invalid pitch band")
    v_low = math.sqrt(r_target * g / (2.0 * t_min))
    v_high = math.sqrt(r_target * g / (2.0 * t_max))
    v_lo = min(v_low, v_high)
    v_hi = max(v_low, v_high)
    if v_lo <= 0:
        raise ValueError("invalid implied speed bounds")
    # p = atan(r g / (2 v^2)); lower pitch at higher v
    pitch_lo = math.atan(r_target * g / (2.0 * v_hi * v_hi))
    pitch_hi = math.atan(r_target * g / (2.0 * v_lo * v_lo))
    pitch_lo = max(PITCH_MIN_RAD, pitch_lo)
    pitch_hi = min(PITCH_MAX_RAD, pitch_hi)
    if pitch_lo >= pitch_hi - 1e-9:
        raise ValueError("degenerate pitch band")
    return (pitch_lo, pitch_hi)


def trajectory_arc_xy(
    speed_horizontal_gru: float,
    pitch_rad: float,
    g: float,
    *,
    num_points: int = 192,
    x_max_gru: Optional[float] = None,
) -> Tuple[List[float], List[float], float, float, float]:
    """Return (xs, ys, r_max, t_flight, apex_y). If x_max_gru is set, clip plot to [0, min(R, x_max)]."""
    if speed_horizontal_gru <= 0:
        raise ValueError("SpeedGRU must be positive")
    if pitch_rad <= PITCH_MIN_RAD or pitch_rad >= PITCH_MAX_RAD:
        raise ValueError("PitchForParabolic must be in (0, pi/2) radians")
    r_full = max_range_horizontal_pitch(speed_horizontal_gru, pitch_rad, g)
    t_total = flight_time_full_arc(speed_horizontal_gru, pitch_rad, g)
    vy0 = vertical_speed_gru(speed_horizontal_gru, pitch_rad)
    apex_y = vy0 * vy0 / (2.0 * g)

    x_end = r_full
    if x_max_gru is not None:
        x_end = min(r_full, max(0.0, x_max_gru))

    if num_points < 2:
        num_points = 2
    xs: List[float] = []
    ys: List[float] = []
    for i in range(num_points):
        u = i / (num_points - 1)
        x = x_end * u
        y = height_at_horizontal_x(speed_horizontal_gru, pitch_rad, g, x)
        xs.append(x)
        ys.append(max(0.0, y))

    return xs, ys, r_full, t_total, apex_y


def release_height_cluster_cylinder_gru(
    speed_horizontal_gru: float,
    pitch_rad: float,
    g: float,
    r_target: float,
    dispersion_radius_gru: float,
) -> float:
    """Height when horizontal offset to aimpoint equals dispersion (cylinder entry), side view."""
    if dispersion_radius_gru <= 0 or dispersion_radius_gru >= r_target:
        raise ValueError("dispersion must be positive and less than target range")
    x = r_target - dispersion_radius_gru
    return height_at_horizontal_x(speed_horizontal_gru, pitch_rad, g, x)

