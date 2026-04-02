"""Aiming time standardization rules for Ammunition.ndf (TypeCategoryName + current AimingTime -> target)."""

from typing import List, TypedDict


class AimTimeRule(TypedDict):
    type_category: str
    current: tuple[str, ...]
    target: str
    label: str


AIM_TIME_STANDARDS: List[AimTimeRule] = [
    {
        "type_category": "'FIQMEQMUTK'",
        "current": ("3.0", "2.0"),
        "target": "1.5",
        "label": "Tank Gun",
    },
    {
        "type_category": "'NZWXQNJFDX'",
        "current": ("1.5",),
        "target": "1.0",
        "label": "Rocket Launcher",
    },
    {
        "type_category": "'GUQUYPXNMN'",
        "current": ("2.5",),
        "target": "1.0",
        "label": "HMG Vehicle",
    },
    {
        "type_category": "'BBQBDWUTJX'",
        "current": ("2.2", "2.0"),
        "target": "1.0",
        "label": "MMG Vehicle",
    },
]
