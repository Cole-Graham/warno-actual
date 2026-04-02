"""Apply bomb ammunition category standards (fixed values + ratio × base member).

Extends by adding entries to ``BOMB_STANDARDS`` and optionally ``BOMB_CATEGORY_WEAPON_WHITELIST``
in ``constants.weapons.standards.by_category.bomb`` — see that package's docstring.
"""

from typing import Any, Dict, Optional

from src.constants.weapons.standards import (
    BOMB_CATEGORY_WEAPON_WHITELIST,
    BOMB_STANDARDS,
)


def _parse_numeric_value(value: Any) -> Optional[float]:
    try:
        if isinstance(value, (int, float)):
            return float(value)
        if isinstance(value, str):
            if "." in value:
                return float(value)
            return float(int(value))
    except (TypeError, ValueError):
        return None
    return None


def apply_category_bomb_standards(
    descr: Any,
    category: str,
    weapon_name: str,
    game_db: Dict[str, Any],
    logger: Any,
) -> None:
    """Apply ``BOMB_STANDARDS[category]`` when the weapon is allowed for that bomb category."""
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

    for key, spec in entry.get("ratios", {}).get("ammunition", {}).items():
        if not isinstance(spec, tuple) or len(spec) != 2:
            logger.warning(
                f"(bomb standards) {descr.n}: invalid ratio spec for {key!r} (expected "
                f"(multiplier, base_member_name)), got {spec!r}",
            )
            continue

        ratio, base_member = spec[0], spec[1]
        if not isinstance(ratio, (int, float)) or not isinstance(base_member, str):
            logger.warning(
                f"(bomb standards) {descr.n}: invalid ratio tuple for {key!r}: {spec!r}",
            )
            continue

        if membr(key, False) is None:
            logger.debug(
                f"(bomb standards) {descr.n}: skip ratio {key} (member missing)",
            )
            continue

        base_val: Optional[float] = None
        base_membr = membr(base_member, False)
        if base_membr is not None:
            base_val = _parse_numeric_value(base_membr.v)
        if base_val is None:
            props = game_db.get("ammunition", {}).get("ammo_properties", {}).get(descr.n, {})
            raw = props.get(base_member)
            if raw is not None:
                base_val = float(raw)
        if base_val is None:
            logger.warning(
                f"(bomb standards) {descr.n}: no {base_member} on descriptor or game_db; "
                f"skipping ratio for {key}",
            )
            continue

        scaled = float(ratio) * base_val
        membr(key).v = str(int(round(scaled)))
        logger.info(
            f"(bomb standards) {descr.n}: set {key} = {membr(key).v} "
            f"({ratio} * {base_member} {base_val})",
        )
