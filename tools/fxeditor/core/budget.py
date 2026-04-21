"""TActionCall budget system: cap total calls, derive N_capped per target radius."""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Optional

from .ndf_io import count_taction_calls, find_actions_list, list_tsimultaneous_rows


@dataclass
class BudgetReport:
    target_m: float
    n_ideal: int
    n_effective: int
    estimated_calls: int
    constrained: bool


def compute_calls_per_site(total_calls: int, n_sites: int) -> float:
    if n_sites <= 0:
        return float(total_calls)
    return total_calls / n_sites


def compute_budget(
    source_total_calls: int,
    n0: int,
    source_m: float,
    target_radii: List[float],
    cap: int,
    *,
    min_sites: int = 3,
) -> List[BudgetReport]:
    """For each target radius, compute ideal vs effective site count."""
    if n0 <= 0 or source_m <= 0:
        return []
    calls_per_site = compute_calls_per_site(source_total_calls, n0)
    n_budget = int(math.floor(cap / calls_per_site)) if calls_per_site > 0 else cap
    n_budget = max(min_sites, n_budget)

    reports: List[BudgetReport] = []
    for target_m in target_radii:
        sf = target_m / source_m
        n_ideal = max(min_sites, round(n0 * sf))
        n_eff = min(n_ideal, n_budget)
        est_calls = int(round(n_eff * calls_per_site))
        reports.append(BudgetReport(
            target_m=target_m,
            n_ideal=n_ideal,
            n_effective=n_eff,
            estimated_calls=est_calls,
            constrained=n_eff < n_ideal,
        ))
    return reports


def count_source_taction_calls(parsed_root) -> int:
    return count_taction_calls(parsed_root)


def breakpoint_radius(
    source_total_calls: int,
    n0: int,
    source_m: float,
    cap: int,
) -> Optional[float]:
    """Radius at which the budget starts constraining (N_ideal == N_budget)."""
    if n0 <= 0 or source_m <= 0 or source_total_calls <= 0:
        return None
    calls_per_site = source_total_calls / n0
    n_budget = math.floor(cap / calls_per_site)
    if n_budget <= 0:
        return 0.0
    return source_m * n_budget / n0
