"""Visual preview of parabolic artillery: fixed target range + pitch; derived horizontal SpeedGRU for impact at R."""

from __future__ import annotations

import json
import math
import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk
from typing import Any, Dict, Optional, Tuple

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def _repo_root_for_dev() -> Path:
    """tools/artillery_arc_preview/main.py -> repo root."""
    return Path(__file__).resolve().parents[2]


def _app_state_dir() -> Path:
    """Writable directory for user_state.json (next to exe when frozen, else package dir)."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


_REPO_ROOT = _repo_root_for_dev()
if not getattr(sys, "frozen", False):
    if str(_REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(_REPO_ROOT))

import tools.artillery_arc_preview.trajectory as tr
from tools.artillery_arc_preview.trajectory import (
    horizontal_speed_gru_for_range_and_pitch,
    max_range_horizontal_pitch,
    pitch_band_for_fixed_target_range,
    release_height_cluster_cylinder_gru,
    trajectory_arc_xy,
)

STATE_PATH = _app_state_dir() / "user_state.json"

PRESETS: Dict[str, Dict[str, Any]] = {
    "Custom": {},
    "Example MLRS (illustrative)": {
        "SpeedGRU": 420.0,
        "PitchForParabolic": 0.52,
        "TargetRangeGRU": 20000.0,
        "MinRangeGRU": 2000.0,
        "MaxRangeGRU": 35000.0,
    },
}

DEFAULT_STATE: Dict[str, Any] = {
    "speed_gru": 420.0,
    "target_range": 20000.0,
    "min_range": "2000",
    "max_range": "35000",
    "g": 9.81,
    "graph_y_floor": 10000.0,
    "design_min_range": "2000",
    "design_max_range": "35000",
    "design_dispersion": "500",
    "design_pitch_slider_rad": 0.52,
}


def _merge_state(raw: Dict[str, Any]) -> Dict[str, Any]:
    out = dict(DEFAULT_STATE)
    for k, v in raw.items():
        if k in DEFAULT_STATE:
            out[k] = v
    # Older saves used pitch_rad without design_pitch_slider_rad
    if "design_pitch_slider_rad" not in raw and "pitch_rad" in raw:
        try:
            out["design_pitch_slider_rad"] = float(raw["pitch_rad"])
        except (TypeError, ValueError):
            pass
    return out


def _format_gru(x: float) -> str:
    if abs(x - round(x)) < 1e-6:
        return str(int(round(x)))
    return f"{x:g}"


def load_state() -> Dict[str, Any]:
    if not STATE_PATH.is_file():
        return dict(DEFAULT_STATE)
    try:
        with open(STATE_PATH, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            return _merge_state(data)
    except (OSError, json.JSONDecodeError):
        pass
    return dict(DEFAULT_STATE)


# Tk Scale only lands on from_ + n * resolution. Bounds must sit on that grid or the
# slider can stop one step outside the intended [lo, hi] (e.g. 0.034 vs 0.0343 at res 0.001).
PITCH_SLIDER_RESOLUTION = 0.0001


def _quantize_pitch_slider_bounds(lo: float, hi: float, res: float) -> Tuple[float, float]:
    """Shrink [lo, hi] to tick-aligned endpoints inside the interval (ceil lo, floor hi)."""
    lo_s = math.ceil(lo / res - 1e-9) * res
    hi_s = math.floor(hi / res + 1e-9) * res
    if lo_s < hi_s - 1e-12:
        return (lo_s, hi_s)
    return (lo, hi)


def _fallback_pitch_band_for_target(r_target: float, g: float) -> Tuple[float, float]:
    """Wide pitch band when design min/max are missing; v implied ∈ [v_lo, v_hi] GRU/s for fixed R."""
    v_lo, v_hi = 100.0, 800.0
    lo = max(tr.PITCH_MIN_RAD, math.atan(r_target * g / (2.0 * v_hi * v_hi)))
    hi = min(tr.PITCH_MAX_RAD, math.atan(r_target * g / (2.0 * v_lo * v_lo)))
    if lo >= hi - 1e-6:
        return (tr.PITCH_MIN_RAD + 0.01, min(tr.PITCH_MAX_RAD - 0.01, 1.2))
    return (lo, hi)


def save_state(data: Dict[str, Any]) -> None:
    try:
        STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(STATE_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except OSError:
        pass


class ArtilleryArcApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Artillery arc preview (target range + pitch → derived SpeedGRU)")
        self.root.geometry("1060x880")

        st = load_state()

        self._speed_gru = tk.DoubleVar(value=float(st["speed_gru"]))
        self._target_range = tk.DoubleVar(value=float(st["target_range"]))
        self._min_range = tk.StringVar(value=str(st.get("min_range", "")))
        self._max_range = tk.StringVar(value=str(st.get("max_range", "")))
        self._g = tk.DoubleVar(value=float(st["g"]))
        self._graph_y_floor = tk.DoubleVar(value=float(st.get("graph_y_floor", 10000.0)))
        self._preset = tk.StringVar(value="Custom")

        self._design_min = tk.StringVar(value=str(st.get("design_min_range", "")))
        self._design_max = tk.StringVar(value=str(st.get("design_max_range", "")))
        self._design_dispersion = tk.StringVar(value=str(st.get("design_dispersion", "500")))
        self._design_pitch_slider_rad = tk.DoubleVar(
            value=float(st.get("design_pitch_slider_rad", DEFAULT_STATE["design_pitch_slider_rad"])),
        )
        # Snapped bounds last applied to Scale (must match _quantize_pitch_slider_bounds + resolution)
        self._pitch_band_lo_snap = 0.01
        self._pitch_band_hi_snap = 1.4

        self._save_timer: Optional[str] = None

        main = ttk.Frame(root, padding=8)
        main.pack(fill=tk.BOTH, expand=True)

        hint = ttk.Label(
            main,
            text=(
                "Fixed same-elevation target range R (GRU): pitch sets loft; horizontal speed is derived so impact "
                "stays at R — v_x = √(R·g/(2·tan(pitch))). The pitch slider sweeps arc shape (apex/flight time) for "
                "that R. Reference SpeedGRU + design min/max range only bracket the slider (optional)."
            ),
            font=("Segoe UI", 8),
            foreground="#444",
            wraplength=1020,
        )
        hint.pack(fill=tk.X, pady=(0, 6))

        ctrl = ttk.LabelFrame(main, text="Preview", padding=8)
        ctrl.pack(fill=tk.X)

        row0 = ttk.Frame(ctrl)
        row0.pack(fill=tk.X, pady=2)
        ttk.Label(row0, text="Preset:").pack(side=tk.LEFT)
        ttk.Combobox(
            row0,
            textvariable=self._preset,
            values=list(PRESETS.keys()),
            state="readonly",
            width=32,
        ).pack(side=tk.LEFT, padx=(8, 0))
        ttk.Button(row0, text="Apply preset", command=self._apply_preset).pack(side=tk.LEFT, padx=(12, 0))

        grid = ttk.Frame(ctrl)
        grid.pack(fill=tk.X, pady=6)

        def add_num(r: int, label: str, var: tk.Variable, width: int = 14) -> None:
            ttk.Label(grid, text=label).grid(row=r, column=0, sticky=tk.W, pady=2)
            ttk.Entry(grid, textvariable=var, width=width).grid(row=r, column=1, sticky=tk.W, padx=8)

        add_num(0, "Target range GRU (same-elevation impact)", self._target_range)
        ttk.Label(
            grid,
            text="PitchForParabolic: slider below — horizontal speed is computed so the round lands at the target range.",
            font=("Segoe UI", 8),
            foreground="#444",
        ).grid(row=1, column=0, columnspan=3, sticky=tk.W, pady=2)
        add_num(2, "Min range GRU (optional guide)", self._min_range)
        add_num(3, "Max range GRU (optional guide)", self._max_range)
        add_num(4, "Gravity g (GRU/s²)", self._g)
        add_num(5, "Graph height floor (GRU)", self._graph_y_floor)

        btn_row = ttk.Frame(ctrl)
        btn_row.pack(fill=tk.X, pady=(8, 0))
        ttk.Button(btn_row, text="Redraw", command=self._redraw).pack(side=tk.LEFT)

        design = ttk.LabelFrame(
            main,
            text="Range band: pitch slider (arc shape at fixed target range)",
            padding=8,
        )
        design.pack(fill=tk.X, pady=(8, 0))

        dg = ttk.Frame(design)
        dg.pack(fill=tk.X)
        ttk.Label(dg, text="Reference SpeedGRU (band only)").grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Entry(dg, textvariable=self._speed_gru, width=14).grid(row=0, column=1, padx=6)
        ttk.Label(
            dg,
            text="With preview target R + g, brackets pitch using R_min…R_max at this reference speed.",
            font=("Segoe UI", 8),
            foreground="#444",
        ).grid(row=0, column=2, columnspan=2, sticky=tk.W, padx=(8, 0))
        ttk.Label(dg, text="Min range GRU").grid(row=1, column=0, sticky=tk.W, pady=2)
        ttk.Entry(dg, textvariable=self._design_min, width=14).grid(row=1, column=1, padx=6)
        ttk.Label(dg, text="Max range GRU").grid(row=1, column=2, sticky=tk.W)
        ttk.Entry(dg, textvariable=self._design_max, width=14).grid(row=1, column=3, padx=6)
        ttk.Label(dg, text="Dispersion GRU (optional)").grid(row=2, column=0, sticky=tk.W, pady=2)
        ttk.Entry(dg, textvariable=self._design_dispersion, width=14).grid(row=2, column=1, padx=6)
        ttk.Label(
            design,
            text=(
                "Preview target range fixes impact distance. Slider pitch changes loft; derived horizontal speed "
                "keeps impact at that R. Reference SpeedGRU + weapon R_min/R_max define the pitch slider interval "
                "(or use fallback band if min/max are invalid). Dispersion uses preview target for cluster height."
            ),
            font=("Segoe UI", 8),
            foreground="#444",
            wraplength=1000,
        ).pack(anchor=tk.W, pady=(4, 0))

        self._band_bounds_label = ttk.Label(design, text="", font=("Segoe UI", 9))
        self._band_bounds_label.pack(anchor=tk.W, pady=(6, 0))

        slider_row = ttk.Frame(design)
        slider_row.pack(fill=tk.X, pady=(4, 0))
        ttk.Label(slider_row, text="PitchForParabolic (rad)").pack(side=tk.LEFT)
        self._pitch_deg_label = ttk.Label(slider_row, text="", font=("Segoe UI", 9), foreground="#333")
        self._pitch_deg_label.pack(side=tk.LEFT, padx=(8, 0))
        self._pitch_band_scale = tk.Scale(
            slider_row,
            from_=0.01,
            to=1.4,
            orient=tk.HORIZONTAL,
            length=520,
            resolution=PITCH_SLIDER_RESOLUTION,
            variable=self._design_pitch_slider_rad,
        )
        self._pitch_band_scale.pack(side=tk.LEFT, padx=(12, 0), fill=tk.X, expand=True)
        self._band_result = tk.Text(design, height=9, width=96, font=("Consolas", 9), wrap=tk.WORD)
        self._band_result.pack(fill=tk.X, pady=(6, 0))

        self._info = ttk.Label(main, text="", font=("Consolas", 9), justify=tk.LEFT)

        chart_frame = ttk.Frame(main)
        chart_frame.pack(fill=tk.BOTH, expand=True, pady=(8, 0))

        self.fig = Figure(figsize=(9, 4.8), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=chart_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self._info.pack(fill=tk.X, pady=(4, 0))

        for v in (self._g, self._graph_y_floor):
            v.trace_add("write", lambda *_: (self._schedule_save(), self._redraw()))
        self._speed_gru.trace_add("write", lambda *_: (self._schedule_save(), self._refresh_band_slider()))
        self._target_range.trace_add("write", lambda *_: (self._schedule_save(), self._refresh_band_slider()))
        for sv in (self._min_range, self._max_range):
            sv.trace_add("write", lambda *_: (self._schedule_save(), self._redraw()))
        for dv in (
            self._design_min,
            self._design_max,
            self._design_dispersion,
        ):
            dv.trace_add("write", lambda *_: (self._schedule_save(), self._refresh_band_slider()))
        self._design_pitch_slider_rad.trace_add(
            "write",
            lambda *_: (
                self._schedule_save(),
                self._snap_pitch_slider_value(),
                self._update_pitch_deg_label(),
                self._update_band_readout(),
                self._redraw(),
            ),
        )

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
        self._update_pitch_deg_label()
        self._refresh_band_slider()
        self._redraw()

    def _snap_pitch_slider_value(self, *_args: object) -> None:
        """Keep DoubleVar on Scale tick grid and inside last snapped [lo, hi] (avoids sub-lo values)."""
        try:
            lo = self._pitch_band_lo_snap
            hi = self._pitch_band_hi_snap
            res = PITCH_SLIDER_RESOLUTION
            pr = float(self._design_pitch_slider_rad.get())
            pr = max(lo, min(hi, pr))
            n = round((pr - lo) / res)
            pr2 = lo + n * res
            pr2 = max(lo, min(hi, pr2))
            if abs(pr2 - pr) > 1e-12:
                self._design_pitch_slider_rad.set(pr2)
        except (tk.TclError, AttributeError, ValueError):
            pass

    def _update_pitch_deg_label(self, *_args: object) -> None:
        try:
            pr = float(self._design_pitch_slider_rad.get())
            self._pitch_deg_label.config(text=f"≈ {math.degrees(pr):.2f}°")
        except tk.TclError:
            self._pitch_deg_label.config(text="")

    def _schedule_save(self) -> None:
        if self._save_timer is not None:
            self.root.after_cancel(self._save_timer)
        self._save_timer = self.root.after(450, self._flush_save)

    def _flush_save(self) -> None:
        self._save_timer = None
        save_state(self._gather_state())

    def _gather_state(self) -> Dict[str, Any]:
        return {
            "speed_gru": float(self._speed_gru.get()),
            "target_range": float(self._target_range.get()),
            "min_range": self._min_range.get(),
            "max_range": self._max_range.get(),
            "g": float(self._g.get()),
            "graph_y_floor": float(self._graph_y_floor.get()),
            "design_min_range": self._design_min.get(),
            "design_max_range": self._design_max.get(),
            "design_dispersion": self._design_dispersion.get(),
            "design_pitch_slider_rad": float(self._design_pitch_slider_rad.get()),
        }

    def _save_state_now(self) -> None:
        save_state(self._gather_state())

    def _on_close(self) -> None:
        self._save_state_now()
        self.root.destroy()

    def _parse_float(self, s: str) -> Optional[float]:
        s = (s or "").strip()
        if not s:
            return None
        try:
            return float(s)
        except ValueError:
            return None

    def _apply_preset(self) -> None:
        name = self._preset.get()
        data = PRESETS.get(name) or {}
        if "SpeedGRU" in data:
            self._speed_gru.set(float(data["SpeedGRU"]))
        if "PitchForParabolic" in data:
            self._design_pitch_slider_rad.set(float(data["PitchForParabolic"]))
        if "TargetRangeGRU" in data:
            self._target_range.set(float(data["TargetRangeGRU"]))
        if "MinRangeGRU" in data:
            self._design_min.set(str(data["MinRangeGRU"]))
            self._min_range.set(str(data["MinRangeGRU"]))
        if "MaxRangeGRU" in data:
            self._design_max.set(str(data["MaxRangeGRU"]))
            self._max_range.set(str(data["MaxRangeGRU"]))
        self._refresh_band_slider()
        self._redraw()

    def _ylim_top(self, apex_y: float, floor_y: float) -> float:
        return max(floor_y, max(apex_y * 1.08, 1.0))

    def _draw_config_annotation(self, vx: float, pitch_rad: float, r_target: float) -> None:
        txt = (
            f"Target range (impact) = {r_target:.1f} GRU\n"
            f"Derived SpeedGRU (horizontal) = {vx:g} GRU/s\n"
            f"PitchForParabolic = {pitch_rad:.6f} rad ({math.degrees(pitch_rad):.2f}°)\n"
            f"Same-elevation range at this pitch/speed = {r_target:.1f} GRU"
        )
        self.ax.text(
            0.02,
            0.98,
            txt,
            transform=self.ax.transAxes,
            fontsize=9,
            verticalalignment="top",
            horizontalalignment="left",
            bbox={
                "boxstyle": "round,pad=0.4",
                "facecolor": "white",
                "edgecolor": "#bbbbbb",
                "alpha": 0.96,
            },
            family="monospace",
            zorder=15,
        )

    def _refresh_band_slider(self, *_args: object) -> None:
        self._schedule_save()
        try:
            vx_ref = float(self._speed_gru.get())
            g = float(self._g.get())
            t_target = float(self._target_range.get())
            r_min = self._parse_float(self._design_min.get())
            r_max = self._parse_float(self._design_max.get())
            if t_target <= 0:
                self._band_bounds_label.config(
                    text="Enter preview target range > 0 GRU (impact distance) to build the pitch band.",
                )
                self._redraw()
                return
            if g <= 0:
                self._band_bounds_label.config(text="g must be positive.")
                self._redraw()
                return
            if r_min is None or r_max is None or r_min <= 0 or r_max <= 0 or r_min > r_max:
                self._band_bounds_label.config(
                    text="Design min/max invalid — using fallback pitch band (≈ v ∈ [100, 800] GRU/s implied).",
                )
                lo, hi = _fallback_pitch_band_for_target(t_target, g)
            elif vx_ref <= 0:
                self._band_bounds_label.config(
                    text="Reference SpeedGRU must be positive for weapon band — using fallback pitch band.",
                )
                lo, hi = _fallback_pitch_band_for_target(t_target, g)
            else:
                try:
                    lo, hi = pitch_band_for_fixed_target_range(vx_ref, g, t_target, r_min, r_max)
                    self._band_bounds_label.config(
                        text=(
                            f"Pitch band for impact at {t_target:.0f} GRU (ref. v = {vx_ref:g}): "
                            f"{lo:.4f}–{hi:.4f} rad ({math.degrees(lo):.1f}°–{math.degrees(hi):.1f}°)"
                        ),
                    )
                except ValueError as e:
                    self._band_bounds_label.config(text=f"Band fallback ({e}).")
                    lo, hi = _fallback_pitch_band_for_target(t_target, g)
            lo = max(tr.PITCH_MIN_RAD, lo)
            hi = min(tr.PITCH_MAX_RAD, hi)
            if lo >= hi - 1e-6:
                self._band_bounds_label.config(text="Invalid pitch band.")
                self._redraw()
                return
            res = PITCH_SLIDER_RESOLUTION
            lo_s, hi_s = _quantize_pitch_slider_bounds(lo, hi, res)
            self._pitch_band_lo_snap = lo_s
            self._pitch_band_hi_snap = hi_s
            self._pitch_band_scale.config(from_=lo_s, to=hi_s, resolution=res)
            cur = float(self._design_pitch_slider_rad.get())
            cur = max(lo_s, min(hi_s, cur))
            n = round((cur - lo_s) / res)
            cur = lo_s + n * res
            cur = max(lo_s, min(hi_s, cur))
            self._design_pitch_slider_rad.set(cur)
            self._update_band_readout()
            self._redraw()
        except (tk.TclError, ValueError) as e:
            self._band_bounds_label.config(text=str(e))
            self._redraw()

    def _update_band_readout(self, *_args: object) -> None:
        self._schedule_save()
        self._band_result.delete("1.0", tk.END)
        try:
            vx_ref = float(self._speed_gru.get())
            g = float(self._g.get())
            pr = float(self._design_pitch_slider_rad.get())
            t_target = float(self._target_range.get())
            r_min = self._parse_float(self._design_min.get())
            r_max = self._parse_float(self._design_max.get())
            if t_target <= 0:
                self._band_result.insert(tk.END, "Enter preview target range > 0 GRU.")
                return
            vx = horizontal_speed_gru_for_range_and_pitch(t_target, pr, g)
            if r_min is None or r_max is None or r_min <= 0 or r_max <= 0 or r_min > r_max or vx_ref <= 0:
                lo, hi = _fallback_pitch_band_for_target(t_target, g)
            else:
                try:
                    lo, hi = pitch_band_for_fixed_target_range(vx_ref, g, t_target, r_min, r_max)
                except ValueError:
                    lo, hi = _fallback_pitch_band_for_target(t_target, g)
            lo = max(tr.PITCH_MIN_RAD, lo)
            hi = min(tr.PITCH_MAX_RAD, hi)
            lo_s, hi_s = _quantize_pitch_slider_bounds(lo, hi, PITCH_SLIDER_RESOLUTION)
            if pr < lo_s - 1e-8 or pr > hi_s + 1e-8:
                self._band_result.insert(
                    tk.END,
                    f"Move slider: pitch {pr:.6f} rad outside snapped band [{lo_s:.6f}, {hi_s:.6f}] "
                    f"(physics [{lo:.6f}, {hi:.6f}]).",
                )
                return

            r_check = max_range_horizontal_pitch(vx, pr, g)
            lines = [
                f"Preview target range (impact) = {t_target:.1f} GRU",
                f"PitchForParabolic = {pr:.6f} rad  ({math.degrees(pr):.2f}°)",
                f"Derived SpeedGRU (horizontal) = {vx:g} GRU/s",
                f"Check: R = 2·SpeedGRU²·tan(pitch)/g = {r_check:.2f} GRU",
                "",
            ]
            disp = self._parse_float(self._design_dispersion.get())
            if disp is not None and 0 < disp < t_target:
                try:
                    h = release_height_cluster_cylinder_gru(vx, pr, g, t_target, disp)
                    lines.append(
                        f"Est. cluster release height (dispersion cylinder): ~{h:.1f} GRU  "
                        f"(side view, x = R−dispersion)",
                    )
                except ValueError as e:
                    lines.append(str(e))

            self._band_result.insert(tk.END, "\n".join(lines))
        except (tk.TclError, ValueError) as e:
            self._band_result.insert(tk.END, str(e))

    def _redraw(self, *_args: object) -> None:
        try:
            pr = float(self._design_pitch_slider_rad.get())
            target_r = float(self._target_range.get())
            g = float(self._g.get())
            floor_y = float(self._graph_y_floor.get())
            if target_r <= 0:
                raise ValueError("Target range must be > 0 GRU (same-elevation impact distance)")
            if pr <= tr.PITCH_MIN_RAD or pr >= tr.PITCH_MAX_RAD:
                raise ValueError("PitchForParabolic must be in (0, pi/2) radians")
            if g <= 0 or floor_y <= 0:
                raise ValueError("g and graph floor must be positive")
            vx = horizontal_speed_gru_for_range_and_pitch(target_r, pr, g)
        except (tk.TclError, ValueError) as e:
            self._info.config(text=str(e))
            return

        mr = self._parse_float(self._max_range.get())
        mn = self._parse_float(self._min_range.get())

        self.ax.clear()
        self.ax.set_facecolor("#f8f8f8")

        try:
            xs, ys, r_full, t_flight, apex_y = trajectory_arc_xy(vx, pr, g)
        except ValueError as e:
            self.ax.axhline(0, color="#333", linewidth=0.8)
            self.ax.set_title("Cannot plot trajectory")
            self.ax.text(0.5, 0.45, str(e), transform=self.ax.transAxes, ha="center", va="center", color="#a00")
            self._draw_config_annotation(vx, pr, target_r)
            self.ax.set_ylim(0, self._ylim_top(0.0, floor_y))
            self.fig.tight_layout()
            self.canvas.draw()
            self._info.config(text=str(e))
            return

        y_plot_peak = max(ys) if ys else 0.0
        y_top = self._ylim_top(y_plot_peak, floor_y)

        self.ax.plot(xs, ys, color="#1f77b4", linewidth=2.0, label="Trajectory (impact at target range)")
        self.ax.fill_between(xs, 0, ys, color="#1f77b4", alpha=0.12)
        self.ax.axhline(0, color="#333", linewidth=0.8)

        self.ax.scatter([0.0, r_full], [0.0, 0.0], color="#c0392b", s=36, zorder=5, label="Launch / impact")

        if mn is not None and mn > 0:
            self.ax.axvline(mn, color="#2e7d32", linestyle=":", linewidth=1, label=f"Min guide ({mn:.0f})")
        if mr is not None and mr > 0:
            self.ax.axvline(mr, color="#888", linestyle="--", linewidth=1, label=f"Max guide ({mr:.0f})")

        self._draw_config_annotation(vx, pr, target_r)

        self.ax.set_xlabel("Ground range (GRU)")
        self.ax.set_ylabel("Height (GRU)")
        title_extra = (
            f" — impact {r_full:.0f} GRU (= target), derived v = {vx:g} GRU/s, "
            f"flight {t_flight:.2f} s, apex {apex_y:.1f} GRU"
        )
        self.ax.set_title(f"Side view{title_extra}")
        self.ax.set_xlim(left=0)
        self.ax.set_ylim(0, y_top)
        self.ax.legend(loc="upper right", fontsize=8)
        self.ax.grid(True, alpha=0.35)
        self.fig.tight_layout()
        self.canvas.draw()

        lines = [
            f"Target range (impact) = {target_r:.2f} GRU",
            f"Derived SpeedGRU = {vx:g} GRU/s (horizontal)",
            f"PitchForParabolic = {pr:.6f} rad ({math.degrees(pr):.2f}°)",
            f"Ballistic flight time = {t_flight:.3f} s",
            f"Apex height = {apex_y:.2f} GRU",
            f"Y-axis top: {y_top:.0f} GRU (floor {floor_y:.0f})",
        ]
        if mr is not None and mr > 0 and target_r > mr:
            lines.append("Note: target beyond max range guide line.")
        self._info.config(text="\n".join(lines))


def main() -> None:
    root = tk.Tk()
    ArtilleryArcApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
