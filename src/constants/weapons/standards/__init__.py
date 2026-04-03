"""Weapon balance standards (data consumed by ammunition / weapon descriptor handlers).

Subpackages:
- pattern: rules applied by matching NDF traits, namespaces, calibers, range members, etc.
- by_category: rules keyed by weapon category from ammo dictionaries; subpackages mirror
  ammunition/missiles types, with one module per category (e.g. by_category/bomb/clu_bomb.py).
"""

from .by_category import (
    BOMB_CATEGORY_WEAPON_WHITELIST,
    CLU_BOMB_WEAPON_NAMES,
    AmmunitionBlock,
    AmmunitionParams,
    CategoryStandardEntry,
    DCA_STANDARDS,
    DcaCategoryStandardEntry,
    DcaExperienceUnitParams,
    HitRollStandardParams,
    SEAD_STANDARDS,
    SeadArmeStandardParams,
    SeadCategoryStandardEntry,
    BOMB_STANDARDS,
    RatioAmmunitionBlock,
    RatioAmmunitionParams,
)
from .pattern import (
    AIM_TIME_STANDARDS,
    AimTimeRule,
    CANON_HE_DAMAGE_BY_CALIBER,
    CANON_HE_DAMAGE_EXCEPTIONS,
    HE_BOMB_DAMAGE_BY_WEIGHT,
    HE_BOMB_NAME_MATCH,
    HE_BOMB_TRAIT_TOKENS,
    WEAPON_RANGE_MEMBERS_TO_CHECK,
)

__all__ = [
    "AIM_TIME_STANDARDS",
    "AimTimeRule",
    "AmmunitionBlock",
    "AmmunitionParams",
    "CategoryStandardEntry",
    "DCA_STANDARDS",
    "DcaCategoryStandardEntry",
    "DcaExperienceUnitParams",
    "HitRollStandardParams",
    "SEAD_STANDARDS",
    "SeadArmeStandardParams",
    "SeadCategoryStandardEntry",
    "BOMB_CATEGORY_WEAPON_WHITELIST",
    "CLU_BOMB_WEAPON_NAMES",
    "RatioAmmunitionBlock",
    "RatioAmmunitionParams",
    "CANON_HE_DAMAGE_BY_CALIBER",
    "CANON_HE_DAMAGE_EXCEPTIONS",
    "HE_BOMB_DAMAGE_BY_WEIGHT",
    "HE_BOMB_NAME_MATCH",
    "HE_BOMB_TRAIT_TOKENS",
    "WEAPON_RANGE_MEMBERS_TO_CHECK",
    "BOMB_STANDARDS",
]
