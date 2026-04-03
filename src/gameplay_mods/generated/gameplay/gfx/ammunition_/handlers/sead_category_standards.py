"""Apply SEAD (AntiRadiation) missile category standards (``Arme`` / damage family)."""

from typing import Any

from src.constants.weapons.standards import SEAD_STANDARDS


def apply_category_sead_standards(descr: Any, category: str) -> None:
    """Set ``Arme.Family`` from ``SEAD_STANDARDS`` for missile category ``AntiRadiation``."""
    if category != "AntiRadiation":
        return
    descr.v.by_m("Arme").v.by_m("Family").v = SEAD_STANDARDS["arme"]["DamageFamily"]
