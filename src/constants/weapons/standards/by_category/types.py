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


class HitRollStandardParams(TypedDict, total=False):
    """Defaults applied to HitRollRuleDescriptor (ammunition / missile descriptors)."""

    DistanceToTarget: bool
    BaseCriticModifier: int
    Idling: int
    Moving: int


class DcaCategoryStandardEntry(TypedDict):
    """Category-wide defaults for autocannon DCA (ammunition dict category ``DCA``)."""

    hit_roll: HitRollStandardParams


class SeadArmeStandardParams(TypedDict):
    """Maps to ``Arme`` member ``Family`` (via ``arme.DamageFamily`` in missile constants)."""

    DamageFamily: str


class SeadCategoryStandardEntry(TypedDict):
    """SEAD missiles (missile dict category ``AntiRadiation`` / ``sead.py``)."""

    arme: SeadArmeStandardParams
