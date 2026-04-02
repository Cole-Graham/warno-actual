"""Bomb ammunition category standards (per category under this package).

To add a category:
1. Add ``<category>.py`` with ``<CATEGORY>_STANDARDS`` (``CategoryStandardEntry``) and optionally
   ``<CATEGORY>_WEAPON_NAMES`` (``FrozenSet[str]``) when standards must only apply to a subset of
   weapons from ``ammunition/bomb.py``.
2. Register ``"<category>": <CATEGORY>_STANDARDS`` in ``BOMB_STANDARDS``.
3. If using a name whitelist, add ``"<category>": <CATEGORY>_WEAPON_NAMES`` to
   ``BOMB_CATEGORY_WEAPON_WHITELIST``. Categories omitted from that dict apply to every weapon
   whose ammo dict uses that category string.
"""

from typing import FrozenSet

from ..types import AmmunitionBlock, AmmunitionParams, CategoryStandardEntry
from .clu_bomb import CLU_BOMB_STANDARDS, CLU_BOMB_WEAPON_NAMES

BOMB_STANDARDS: dict[str, CategoryStandardEntry] = {
    "clu_bomb": CLU_BOMB_STANDARDS,
}

# Categories that restrict standards to specific weapon names (see module docstring).
BOMB_CATEGORY_WEAPON_WHITELIST: dict[str, FrozenSet[str]] = {
    "clu_bomb": CLU_BOMB_WEAPON_NAMES,
}

__all__ = [
    "AmmunitionBlock",
    "AmmunitionParams",
    "BOMB_CATEGORY_WEAPON_WHITELIST",
    "BOMB_STANDARDS",
    "CategoryStandardEntry",
    "CLU_BOMB_STANDARDS",
    "CLU_BOMB_WEAPON_NAMES",
]
