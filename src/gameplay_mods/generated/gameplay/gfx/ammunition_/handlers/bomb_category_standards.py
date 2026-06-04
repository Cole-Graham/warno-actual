"""Apply bomb ammunition category standards (fixed values at edit time).

CLU bomb dispersion ratios are precomputed in ``build_clu_bomb_dispersion`` and
applied after dict edits via ``apply_clu_bomb_dispersion_standard``.

Extends by adding entries to ``BOMB_STANDARDS`` and optionally
``BOMB_CATEGORY_WEAPON_WHITELIST`` in ``constants.weapons.standards.by_category``.
"""

from typing import Any, Dict

from src.constants.weapons.standards import (
    BOMB_CATEGORY_WEAPON_WHITELIST,
    BOMB_STANDARDS,
)


def apply_category_bomb_standards(
    descr: Any,
    category: str,
    weapon_name: str,
    game_db: Dict[str, Any],
    logger: Any,
) -> None:
    """Apply ``BOMB_STANDARDS[category]`` fixed values when the weapon is allowed."""
    entry = BOMB_STANDARDS.get(category)
    if not entry:
        return

    allowed = BOMB_CATEGORY_WEAPON_WHITELIST.get(category)
    if allowed is not None and weapon_name not in allowed:
        logger.debug(
            f"(bomb standards) skip {weapon_name}: not allowed for bomb category {category!r}",
        )
        return

    membr = descr.v.by_m

    for key, value in entry.get("fixed_values", {}).get("ammunition", {}).items():
        if membr(key, False) is None:
            logger.debug(
                f"(bomb standards) {descr.n}: skip fixed {key} (member missing)",
            )
            continue
        membr(key).v = str(value)


def apply_clu_bomb_dispersion_standard(
    descr: Any,
    weapon_name: str,
    game_db: Dict[str, Any],
    logger: Any,
) -> None:
    """Write precomputed CLU bomb dispersion after ``parent_membr`` dict edits.

    Lookup uses base *weapon_name* (no ``Ammo_`` prefix) so the same key works
    for base descriptors and all salvo variants.
    """
    dispersion_map = game_db.get("ammunition", {}).get("clu_bomb_dispersion", {})
    entry = dispersion_map.get(weapon_name)
    if entry is None:
        return

    membr = descr.v.by_m
    for key, value in entry.items():
        if membr(key, False) is None:
            logger.debug(
                f"(clu_bomb_dispersion) {descr.n}: skip {key} (member missing)",
            )
            continue
        membr(key).v = str(int(value))
        logger.debug(
            f"(clu_bomb_dispersion) {descr.n}: set {key} = {value}",
        )
