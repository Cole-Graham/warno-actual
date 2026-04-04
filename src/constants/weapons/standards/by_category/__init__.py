"""Standards keyed by ammunition dictionary category (e.g. clu_bomb, he_bomb, small_arms).

Layout mirrors `constants.weapons.ammunition` and `constants.weapons.missiles`:
- One subpackage per weapon file (e.g. `bomb/`, `canon/`, `missiles/aa/`).
- Within each subpackage, one module per category string (e.g. `bomb/clu_bomb.py`).
"""

from .autocanon_dca import DCA_STANDARDS
from .missiles.sead import SEAD_STANDARDS
from .bomb import (
    BOMB_CATEGORY_WEAPON_WHITELIST,
    BOMB_STANDARDS,
    CLU_BOMB_WEAPON_NAMES,
)
from .types import (
    AmmunitionBlock,
    AmmunitionParams,
    CategoryStandardEntry,
    DcaCategoryStandardEntry,
    DcaExperienceUnitParams,
    HitRollStandardParams,
    RatioAmmunitionBlock,
    RatioAmmunitionParams,
    SeadCategoryStandardEntry,
    SeadArmeStandardParams,
)

__all__ = [
    "BOMB_CATEGORY_WEAPON_WHITELIST",
    "CLU_BOMB_WEAPON_NAMES",
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
    "BOMB_STANDARDS",
    "RatioAmmunitionBlock",
    "RatioAmmunitionParams",
]
