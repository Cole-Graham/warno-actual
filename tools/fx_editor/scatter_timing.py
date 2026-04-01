"""Infer and redistribute anchor TWaitInSec durations for cluster scatter scaling."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src import ndf

from .scatter_emit import find_actions_list

_FALLBACK_MIN = 0.2
_FALLBACK_MAX = 0.75


def _first_wait_duration_in_simultaneous(sim: ndf.model.Object) -> Optional[float]:
    """First TWaitInSec.Duration in preorder under a TSimultaneousAction (anchor wait)."""
    if sim.type != 'TSimultaneousAction':
        return None

    def walk(node: Any) -> Optional[float]:
        if isinstance(node, ndf.model.Object):
            if node.type == 'TWaitInSec':
                for m in node:
                    if m.member == 'Duration':
                        return float(m.v)
                return None
            for m in node:
                got = walk(m.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.List):
            for row in node:
                got = walk(row.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.MemberRow):
            return walk(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                got = walk(mr.v)
                if got is not None:
                    return got
        elif isinstance(node, ndf.model.ListRow):
            return walk(node.v)
        return None

    return walk(sim)


def collect_anchor_waits_from_actions(actions: ndf.model.List) -> List[float]:
    """One first-wait duration per top-level TSimultaneousAction row (in list order)."""
    out: List[float] = []
    for row in actions:
        if not isinstance(row.v, ndf.model.Object) or row.v.type != 'TSimultaneousAction':
            continue
        w = _first_wait_duration_in_simultaneous(row.v)
        if w is not None:
            out.append(w)
    return out


def infer_anchor_bounds_from_parsed(parsed_root: ndf.model.List) -> Tuple[float, float]:
    """Return (t_min, t_default_max) from min/max of first anchor waits, or fallbacks."""
    actions = find_actions_list(parsed_root)
    if actions is None:
        return _FALLBACK_MIN, _FALLBACK_MAX
    waits = collect_anchor_waits_from_actions(actions)
    if not waits:
        return _FALLBACK_MIN, _FALLBACK_MAX
    return min(waits), max(waits)


def _round_duration_hundredth(x: float) -> float:
    return round(float(x) + 1e-12, 2)


def redistribute_anchor_waits(t_min: float, t_max: float, n: int) -> List[float]:
    """Linear spacing of anchor waits in [t_min, t_max] for n bursts (n >= 1)."""
    if n <= 0:
        return []
    t_lo = min(t_min, t_max)
    t_hi = max(t_min, t_max)
    if n == 1:
        return [_round_duration_hundredth(t_lo)]
    return [
        _round_duration_hundredth(t_lo + (t_hi - t_lo) * (i / (n - 1)))
        for i in range(n)
    ]


def count_tsimultaneous_in_actions(actions: ndf.model.List) -> int:
    n = 0
    for row in actions:
        if isinstance(row.v, ndf.model.Object) and row.v.type == 'TSimultaneousAction':
            n += 1
    return n
