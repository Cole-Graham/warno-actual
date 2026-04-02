"""Standards keyed by ammunition dictionary category (e.g. clu_bomb, he_bomb, small_arms).

Layout mirrors `constants.weapons.ammunition` and `constants.weapons.missiles`:
- One subpackage per weapon file (e.g. `bomb/`, `canon/`, `missiles/aa/`).
- Within each subpackage, one module per category string (e.g. `bomb/clu_bomb.py`).
"""

from .bomb import (
    BOMB_CATEGORY_WEAPON_WHITELIST,
    BOMB_STANDARDS,
    CLU_BOMB_WEAPON_NAMES,
)
from .types import (
    AmmunitionBlock,
    AmmunitionParams,
    CategoryStandardEntry,
    RatioAmmunitionBlock,
    RatioAmmunitionParams,
)

__all__ = [
    "BOMB_CATEGORY_WEAPON_WHITELIST",
    "CLU_BOMB_WEAPON_NAMES",
    "AmmunitionBlock",
    "AmmunitionParams",
    "CategoryStandardEntry",
    "BOMB_STANDARDS",
    "RatioAmmunitionBlock",
    "RatioAmmunitionParams",
]
