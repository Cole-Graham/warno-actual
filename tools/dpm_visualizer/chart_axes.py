"""Matplotlib axis helpers for DPM charts."""

import math

from matplotlib.ticker import FixedLocator, FuncFormatter, LogLocator, NullFormatter, ScalarFormatter

from .constants import format_dpm_y_axis_tick

# Multi-decade log ticks: 25, 50, 75, 100, 150, 200, 300, 500, 750, 1000, ...
_LOG_DPM_DENSE_SUBS = (1.0, 1.5, 2.0, 2.5, 3.0, 5.0, 7.5)
# Within a single decade: 400, 500, 600, 700, ...
_LOG_DPM_INTRA_DECADE_SUBS = tuple(float(i) for i in range(1, 10))


def _log_decade_span(ymin: float, ymax: float) -> float:
    if ymin <= 0 or ymax <= ymin:
        return 0.0
    return math.log10(ymax) - math.log10(ymin)


def _log_dpm_tick_subs(ymin: float, ymax: float) -> tuple[float, ...]:
    """Pick log tick density based on how much of the axis spans an order of magnitude."""
    if _log_decade_span(ymin, ymax) < 0.85:
        return _LOG_DPM_INTRA_DECADE_SUBS
    return _LOG_DPM_DENSE_SUBS


def _plotted_y_range(ax) -> tuple[float | None, float | None]:
    """Minimum and maximum positive finite Y values currently drawn on the axis."""
    ymin = math.inf
    ymax = -math.inf

    for line in ax.lines:
        for y in line.get_ydata():
            y = float(y)
            if y > 0 and math.isfinite(y):
                ymin = min(ymin, y)
                ymax = max(ymax, y)

    for collection in ax.collections:
        offsets = collection.get_offsets()
        if len(offsets) == 0:
            continue
        for y in offsets[:, 1]:
            y = float(y)
            if y > 0 and math.isfinite(y):
                ymin = min(ymin, y)
                ymax = max(ymax, y)

    if not math.isfinite(ymin) or not math.isfinite(ymax):
        return None, None
    return ymin, ymax


def _log_dpm_major_ticks(ymin: float, ymax: float) -> list[float]:
    """Major ticks anchored at the plotted minimum, then log-spaced upward."""
    ticks = [ymin]
    subs = _log_dpm_tick_subs(ymin, ymax)
    start_exp = int(math.floor(math.log10(ymin)))
    end_exp = int(math.ceil(math.log10(ymax)))
    upper = ymax * 1.02

    for exp in range(start_exp, end_exp + 1):
        base = 10.0 ** exp
        for multiplier in subs:
            tick = multiplier * base
            if tick > ymin * 1.000001 and tick <= upper:
                ticks.append(tick)

    return sorted(set(ticks))


def _log_axis_bottom(data_ymin: float, auto_lo: float) -> float:
    """Y-axis floor below the lowest data tick (headroom toward 0, no extra label)."""
    if auto_lo < data_ymin:
        return auto_lo
    return data_ymin * (10 ** -0.2)


def apply_dpm_y_axis_scale(ax, use_log_scale: bool) -> None:
    """Apply linear or logarithmic DPM scaling with plain numeric tick labels."""
    if use_log_scale:
        ax.set_yscale("log")
        data_ymin, data_ymax = _plotted_y_range(ax)
        if data_ymin is not None and data_ymax is not None and data_ymax > data_ymin:
            auto_lo, auto_hi = ax.get_ylim()
            bottom = _log_axis_bottom(data_ymin, auto_lo)
            top = max(auto_hi, data_ymax * 1.02)
            ax.set_ylim(bottom=bottom, top=top)
            ticks = _log_dpm_major_ticks(data_ymin, data_ymax)
            ax.yaxis.set_major_locator(FixedLocator(ticks))
        else:
            ymin, ymax = ax.get_ylim()
            subs = _log_dpm_tick_subs(ymin, ymax)
            ax.yaxis.set_major_locator(LogLocator(base=10, subs=subs))
        ax.yaxis.set_minor_formatter(NullFormatter())
        ax.yaxis.set_major_formatter(FuncFormatter(format_dpm_y_axis_tick))
        ax.tick_params(axis="y", which="minor", left=False, labelleft=False)
        ax.yaxis.get_offset_text().set_visible(False)
        return

    ax.set_yscale("linear")
    linear_formatter = ScalarFormatter(useOffset=False)
    linear_formatter.set_scientific(False)
    ax.yaxis.set_major_formatter(linear_formatter)
    ax.yaxis.get_offset_text().set_visible(False)
    ax.set_ylim(bottom=0)
