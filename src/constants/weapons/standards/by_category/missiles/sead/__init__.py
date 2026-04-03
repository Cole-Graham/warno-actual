"""SEAD / anti-radiation missile category standards."""

from ...types import SeadCategoryStandardEntry

SEAD_STANDARDS: SeadCategoryStandardEntry = {
    "arme": {
        "DamageFamily": "DamageFamily_sead_missile_wa",
    },
}

__all__ = [
    "SEAD_STANDARDS",
]
