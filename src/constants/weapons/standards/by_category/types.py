"""Shared TypedDicts for category-keyed weapon standards (all ammunition / missile types)."""

from typing import Tuple, TypedDict


class AmmunitionParams(TypedDict, total=False):
    PhysicalDamages: int


class AmmunitionBlock(TypedDict):
    ammunition: AmmunitionParams


# Each ratio: (multiplier, base_member_name) — target member = round(multiplier * value(base_member)).
class RatioAmmunitionParams(TypedDict, total=False):
    DispersionAtMaxRangeGRU: Tuple[float, str]
    DispersionAtMinRangeGRU: Tuple[float, str]


class RatioAmmunitionBlock(TypedDict):
    ammunition: RatioAmmunitionParams


class CategoryStandardEntry(TypedDict):
    fixed_values: AmmunitionBlock
    ratios: RatioAmmunitionBlock
