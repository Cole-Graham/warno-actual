"""Timeline events for scatter animation: TWaitInSec + TActionCall within each TSimultaneousAction."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .scatter_emit import find_actions_list
from .scatter_extract import (
    _action_short_from_taction,
    _mobile_position_from_simultaneous,
    _parse_float3_plus_par,
    extract_scatter_points_with_vfx,
    ndf_xy_to_gameplay_m,
)
from .scatter_model import load_scatter_calibration_yaml


@dataclass
class TimelineEvent:
    t_s: float
    burst_index: int
    vfx_short: str
    x_gameplay_m: float
    y_gameplay_m: float


def _par_position_ndf_from_taction(tac: ndf.model.Object) -> Optional[Tuple[float, float]]:
    if tac.type != 'TActionCall':
        return None
    for member in tac:
        if member.member != 'NamedParams' or not isinstance(member.v, ndf.model.Map):
            continue
        for map_row in member.v:
            key = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
            if key != 'parPositionRelative':
                continue
            s = ndf.printer.string(map_row.v).strip()
            return _parse_float3_plus_par(s)
    return None


def _list_row_child_v(row: Any) -> Any:
    """``ListRow.v``; ndf_parse may validate on access after batch mutations — never raise to callers."""
    try:
        return row.v
    except Exception:
        return None


def _events_in_sequential_with_calls(
    seq: ndf.model.Object,
) -> List[Tuple[float, str, Optional[ndf.model.Object]]]:
    """Per TSequentialAction: cumulative waits before each TActionCall; one entry per call."""
    if seq.type != 'TSequentialAction':
        return []
    cumulative = 0.0
    last_wait = 0.0
    out: List[Tuple[float, str, Optional[ndf.model.Object]]] = []
    for m in seq:
        if m.member != 'Actions' or not isinstance(m.v, ndf.model.List):
            continue
        try:
            wait_rows = list(m.v)
        except Exception:
            continue
        for row in wait_rows:
            o = _list_row_child_v(row)
            if o is None or not isinstance(o, ndf.model.Object):
                continue
            if o.type == 'TWaitInSec':
                for mm in o:
                    if mm.member == 'Duration':
                        last_wait = float(mm.v)
            elif o.type == 'TActionCall':
                cumulative += last_wait
                last_wait = 0.0
                vfx = _action_short_from_taction(o)
                if vfx:
                    out.append((cumulative, vfx, o))
    return out


def build_timeline_events(
    parsed_root: ndf.model.List,
    *,
    ref_m: Optional[float] = None,
    anchor_r: Optional[float] = None,
) -> List[TimelineEvent]:
    """Parallel bursts: each TSimultaneousAction has t=0; sibling sequentials use absolute times (reset per branch).

    Burst indices match ``extract_scatter_points_with_vfx`` / ``project.bursts`` order (one index per scatter point).
    """
    if ref_m is None or anchor_r is None:
        ref_m, anchor_r = load_scatter_calibration_yaml()
    pts = extract_scatter_points_with_vfx(parsed_root)
    if not pts:
        return []
    actions = find_actions_list(parsed_root)
    if actions is None:
        return []

    events: List[TimelineEvent] = []
    pi = 0

    for row in actions:
        if not isinstance(row.v, ndf.model.Object) or row.v.type != 'TSimultaneousAction':
            continue
        sim = row.v
        mob = _mobile_position_from_simultaneous(sim)

        if mob is not None:
            if pi >= len(pts):
                break
            gx, gy = ndf_xy_to_gameplay_m(mob[0], mob[1], ref_m, anchor_r)
            igx = float(int(round(gx)))
            igy = float(int(round(gy)))
            burst_idx = pi
            pi += 1
            for m in sim:
                if m.member != 'Actions' or not isinstance(m.v, ndf.model.List):
                    continue
                try:
                    seq_rows = list(m.v)
                except Exception:
                    continue
                for seq_row in seq_rows:
                    seq = _list_row_child_v(seq_row)
                    if not isinstance(seq, ndf.model.Object) or seq.type != 'TSequentialAction':
                        continue
                    for t_s, vfx, _tac in _events_in_sequential_with_calls(seq):
                        events.append(
                            TimelineEvent(
                                t_s=t_s,
                                burst_index=burst_idx,
                                vfx_short=vfx,
                                x_gameplay_m=igx,
                                y_gameplay_m=igy,
                            ),
                        )
        else:
            for m in sim:
                if m.member != 'Actions' or not isinstance(m.v, ndf.model.List):
                    continue
                try:
                    seq_rows = list(m.v)
                except Exception:
                    continue
                for seq_row in seq_rows:
                    seq = _list_row_child_v(seq_row)
                    if not isinstance(seq, ndf.model.Object) or seq.type != 'TSequentialAction':
                        continue
                    for t_s, vfx, tac in _events_in_sequential_with_calls(seq):
                        if tac is None:
                            continue
                        p_ndf = _par_position_ndf_from_taction(tac)
                        if p_ndf is None:
                            continue
                        if pi >= len(pts):
                            break
                        gx, gy = ndf_xy_to_gameplay_m(p_ndf[0], p_ndf[1], ref_m, anchor_r)
                        igx = float(int(round(gx)))
                        igy = float(int(round(gy)))
                        burst_idx = pi
                        pi += 1
                        events.append(
                            TimelineEvent(
                                t_s=t_s,
                                burst_index=burst_idx,
                                vfx_short=vfx,
                                x_gameplay_m=igx,
                                y_gameplay_m=igy,
                            ),
                        )

    events.sort(key=lambda e: (e.t_s, e.burst_index))
    return events


def timeline_end_time_s(events: List[TimelineEvent]) -> float:
    if not events:
        return 0.0
    return max(e.t_s for e in events)
