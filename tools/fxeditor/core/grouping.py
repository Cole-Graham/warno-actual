"""Composite site model and effect group analysis.

Identifies which TSimultaneousAction blocks belong together as a single
logical sub-impact (composite event) and groups blocks by VFX signature.
"""

from __future__ import annotations

import math
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .ndf_io import (
    _list_row_child_v,
    action_short_from_taction,
    find_actions_list,
    first_taction_short_in_simultaneous,
    iter_taction_call_objects,
    list_tsimultaneous_rows,
    mobile_position_from_simultaneous,
    parse_float3_plus_par,
    simultaneous_is_nil_mobile,
)


# ── Composite Site Model ──────────────────────────────────────────

def _par_float3_from_taction(tac: ndf.model.Object) -> Optional[Tuple[float, float]]:
    if tac.type != "TActionCall":
        return None
    for member in tac:
        if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
            continue
        for mr in member.v:
            key = strip_quotes(str(mr.k)) if mr.k is not None else ""
            if key != "parPositionRelative":
                continue
            s = ndf.printer.string(mr.v).strip()
            return parse_float3_plus_par(s)
    return None


def _reference_columns_from_nil_sim(
    sim: ndf.model.Object,
    max_len: Optional[int] = None,
) -> List[Tuple[float, float]]:
    """R[j] lattice from first nil-Mobile simultaneous."""
    out: List[Tuple[float, float]] = []
    seen: set[Tuple[float, float]] = set()
    if sim.type != "TSimultaneousAction":
        return out
    for m in sim:
        if m.member != "Actions" or not isinstance(m.v, ndf.model.List):
            continue
        for seq_row in m.v:
            seq = _list_row_child_v(seq_row)
            if not isinstance(seq, ndf.model.Object) or seq.type != "TSequentialAction":
                continue
            for sm in seq:
                if sm.member != "Actions" or not isinstance(sm.v, ndf.model.List):
                    continue
                for wr in sm.v:
                    o = _list_row_child_v(wr)
                    if not isinstance(o, ndf.model.Object) or o.type != "TActionCall":
                        continue
                    p = _par_float3_from_taction(o)
                    if p is None:
                        continue
                    key = (round(p[0], 4), round(p[1], 4))
                    if key in seen:
                        return out
                    seen.add(key)
                    out.append((p[0], p[1]))
                    if max_len is not None and len(out) >= max_len:
                        return out
                    break
    return out


@dataclass(frozen=True)
class CompositeSiteModel:
    """Ground anchors G + reference columns R; site count is max(len(G), len(R))."""

    G_ndf: Tuple[Tuple[float, float], ...]
    R_ndf: Tuple[Tuple[float, float], ...]
    primary_vfx: Tuple[str, ...]
    ref_m: float
    anchor_r: float

    @property
    def n_sites(self) -> int:
        return max(len(self.G_ndf), len(self.R_ndf))

    def canonical_ndf_xy(self, site_j: int) -> Tuple[float, float]:
        if site_j < len(self.G_ndf):
            return self.G_ndf[site_j]
        if site_j < len(self.R_ndf):
            return self.R_ndf[site_j]
        if self.G_ndf:
            return self.G_ndf[-1]
        return self.R_ndf[-1]

    def assign_site(self, px: float, py: float) -> int:
        if self.n_sites == 0:
            return 0
        best_j = 0
        best_d = float("inf")
        s = self.ref_m / self.anchor_r if self.anchor_r > 0 else 1.0
        g1x, g1y = px * s, py * s
        for j in range(self.n_sites):
            cand: List[float] = []
            if j < len(self.G_ndf):
                gx, gy = self.G_ndf[j][0] * s, self.G_ndf[j][1] * s
                cand.append(math.hypot(g1x - gx, g1y - gy))
            if j < len(self.R_ndf):
                rx, ry = self.R_ndf[j][0] * s, self.R_ndf[j][1] * s
                cand.append(math.hypot(g1x - rx, g1y - ry))
            if cand:
                d = min(cand)
                if d < best_d:
                    best_d = d
                    best_j = j
        return best_j


def build_composite_site_model(
    parsed_root: ndf.model.List,
    *,
    ref_m: float,
    anchor_r: float,
) -> Optional[CompositeSiteModel]:
    actions = find_actions_list(parsed_root)
    if actions is None:
        return None
    G: List[Tuple[float, float]] = []
    primaries: List[str] = []
    first_nil_idx: Optional[int] = None
    for i, row in enumerate(actions):
        sim = row.v
        if not isinstance(sim, ndf.model.Object) or sim.type != "TSimultaneousAction":
            continue
        if simultaneous_is_nil_mobile(sim):
            first_nil_idx = i
            break
        mob = mobile_position_from_simultaneous(sim)
        if mob is None:
            continue
        G.append((mob[0], mob[1]))
        primaries.append(first_taction_short_in_simultaneous(sim))
    if not G:
        return None
    R: List[Tuple[float, float]] = []
    if first_nil_idx is not None:
        nil_row = actions[first_nil_idx]
        nil_sim = nil_row.v
        if isinstance(nil_sim, ndf.model.Object) and nil_sim.type == "TSimultaneousAction":
            R = _reference_columns_from_nil_sim(nil_sim, max_len=None)
    return CompositeSiteModel(
        G_ndf=tuple(G),
        R_ndf=tuple(R),
        primary_vfx=tuple(primaries),
        ref_m=float(ref_m),
        anchor_r=float(anchor_r),
    )


# ── Effect Group Analysis ────────────────────────────────────────

def _events_in_sequential(seq: ndf.model.Object) -> List[Tuple[float, str, ndf.model.Object]]:
    """(cumulative_t, vfx_short, taction_obj) for each TActionCall in a TSequentialAction."""
    if seq.type != "TSequentialAction":
        return []
    out: List[Tuple[float, str, ndf.model.Object]] = []
    t = 0.0
    for sm in seq:
        if sm.member != "Actions" or not isinstance(sm.v, ndf.model.List):
            continue
        for wr in sm.v:
            o = _list_row_child_v(wr)
            if not isinstance(o, ndf.model.Object):
                continue
            if o.type == "TWaitInSec":
                for m in o:
                    if m.member == "Duration":
                        t += float(m.v)
            elif o.type == "TActionCall":
                s = action_short_from_taction(o)
                if s:
                    out.append((round(t, 6), s, o))
    return out


def _signature_and_timing(
    sim: ndf.model.Object,
) -> Tuple[Optional[Tuple[Tuple[str, ...], ...]], List[List[Tuple[float, str]]]]:
    """Per-branch VFX signature + timing ladder."""
    sig_parts: List[Tuple[str, ...]] = []
    timing_branches: List[List[Tuple[float, str]]] = []
    for m in sim:
        if m.member != "Actions" or not isinstance(m.v, ndf.model.List):
            continue
        for seq_row in m.v:
            seq = _list_row_child_v(seq_row)
            if not isinstance(seq, ndf.model.Object) or seq.type != "TSequentialAction":
                continue
            entries = _events_in_sequential(seq)
            branch_vfx = tuple(vfx for _, vfx, _ in entries)
            if branch_vfx:
                sig_parts.append(branch_vfx)
                timing_branches.append([(t, vfx) for t, vfx, _ in entries])
    if not sig_parts:
        return None, []
    return tuple(sig_parts), timing_branches


def _position_flags(sim: ndf.model.Object) -> Tuple[bool, bool, bool]:
    has_mobile = mobile_position_from_simultaneous(sim) is not None
    has_rel = False
    has_rand = False

    def walk(n: Any) -> None:
        nonlocal has_rel, has_rand
        if isinstance(n, ndf.model.Object):
            if n.type == "TActionCall":
                for member in n:
                    if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
                        continue
                    for mr in member.v:
                        key = strip_quotes(str(mr.k)) if mr.k is not None else ""
                        if key == "parPositionRelative":
                            has_rel = True
                        elif key == "parRandomPosition":
                            has_rand = True
            for m in n:
                walk(m.v)
        elif isinstance(n, ndf.model.List):
            for row in n:
                rv = _list_row_child_v(row)
                if rv is not None:
                    walk(rv)
        elif isinstance(n, ndf.model.MemberRow):
            walk(n.v)
        elif isinstance(n, ndf.model.Map):
            for mr in n:
                walk(mr.v)
        elif isinstance(n, ndf.model.ListRow):
            lr = _list_row_child_v(n)
            if lr is not None:
                walk(lr)

    walk(sim)
    return has_mobile, has_rel, has_rand


def _format_position_summary(mobile: bool, rel: bool, rnd: bool) -> str:
    parts: List[str] = []
    if mobile:
        parts.append("Global Mobile anchor")
    if rel:
        parts.append("parPositionRelative per call")
    if rnd:
        parts.append("parRandomPosition per call")
    return "; ".join(parts) if parts else "No positional hooks"


@dataclass
class EffectGroupRow:
    pattern: Tuple[Tuple[str, ...], ...]
    count: int
    effects: str
    timing: str
    positioning: str
    branch_timings: List[List[Tuple[float, str]]] = field(default_factory=list)


def _format_signature(sig: Tuple[Tuple[str, ...], ...]) -> str:
    return " || ".join(" → ".join(branch) for branch in sig)


def _format_burst_timing_histogram(sims: List[ndf.model.Object]) -> str:
    c: Counter = Counter()
    for sim in sims:
        for m in sim:
            if m.member != "Actions" or not isinstance(m.v, ndf.model.List):
                continue
            for seq_row in m.v:
                seq = _list_row_child_v(seq_row)
                if not isinstance(seq, ndf.model.Object) or seq.type != "TSequentialAction":
                    continue
                ev = _events_in_sequential(seq)
                if ev:
                    c[round(ev[0][0], 6)] += 1
                break
            break
    if not c:
        return ""
    parts: List[str] = []
    for t in sorted(c.keys()):
        n = c[t]
        parts.append(f"{t:g}s" if n == 1 else f"{t:g}s x {n}")
    return ", ".join(parts)


def analyze_effect_groups(parsed_root: ndf.model.List) -> List[EffectGroupRow]:
    """Group TSimultaneousAction bursts sharing the same per-branch VFX pattern."""
    actions = find_actions_list(parsed_root)
    if actions is None:
        return []
    buckets: Dict[Tuple[Tuple[str, ...], ...], List[ndf.model.Object]] = defaultdict(list)
    for row in actions:
        sim = _list_row_child_v(row)
        if sim is None or not isinstance(sim, ndf.model.Object) or sim.type != "TSimultaneousAction":
            continue
        sig, _ = _signature_and_timing(sim)
        if sig is None:
            continue
        buckets[sig].append(sim)

    rows: List[EffectGroupRow] = []
    for sig, sims in buckets.items():
        _, rep_timings = _signature_and_timing(sims[0])
        timing = _format_burst_timing_histogram(sims)
        pos_strs = [_format_position_summary(*_position_flags(s)) for s in sims]
        unique_pos = sorted(set(pos_strs))
        positioning = unique_pos[0] if len(unique_pos) == 1 else "Mixed: " + "; ".join(unique_pos)
        rows.append(EffectGroupRow(
            pattern=sig,
            count=len(sims),
            effects=_format_signature(sig),
            timing=timing,
            positioning=positioning,
            branch_timings=rep_timings,
        ))
    rows.sort(key=lambda r: (-r.count, r.effects))
    return rows


def format_effect_group_block(row: EffectGroupRow, index: int) -> str:
    lines: List[str] = [
        f"── Group {index}  —  ×{row.count} burst(s) with this pattern",
        f"Position: {row.positioning}",
    ]
    if row.timing:
        lines.append(f"Timing: {row.timing}")
    lines.append("")
    label = "Parallel branches:" if len(row.branch_timings) > 1 else "Single branch:"
    lines.append(f"  {label}")
    for bi, branch in enumerate(row.branch_timings, start=1):
        lines.append(f"    Branch {bi}")
        if not branch:
            lines.append("      (no TActionCall)")
        else:
            for t, vfx in branch:
                lines.append(f"      t={t:g}s  →  {vfx}")
    lines.append("")
    return "\n".join(lines)


def distinct_placeable_template_indices(templates: List[Any]) -> List[int]:
    """One index per distinct VFX signature pattern."""
    seen: Set[Any] = set()
    out: List[int] = []
    for i, row in enumerate(templates):
        sim = row.v
        if not isinstance(sim, ndf.model.Object) or sim.type != "TSimultaneousAction":
            continue
        sig, _ = _signature_and_timing(sim)
        key = sig if sig is not None else ("__nosig__", i)
        if key in seen:
            continue
        seen.add(key)
        out.append(i)
    return out
