"""Create infantry magazine-style salvolength / infmagazine ammo variants."""

from __future__ import annotations

from typing import Any, Dict, List, Optional
from uuid import uuid4

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def _read_float_member(descr: Any, member: str) -> Optional[float]:
    membr = descr.v.by_m(member, False)
    if membr is None:
        return None
    try:
        return float(str(membr.v))
    except (TypeError, ValueError):
        return None


def _set_member(descr: Any, member: str, value: Any) -> None:
    membr = descr.v.by_m(member, False)
    if membr is None:
        return
    membr.v = str(value)


def apply_infantry_magazine_timing(variant: Any, base_descr: Any, length: int) -> None:
    """Copy base salvo reload onto shot reload; set magazine shot count and supply."""
    base_salvo_time = _read_float_member(base_descr, "TimeBetweenTwoSalvos")
    if base_salvo_time is not None:
        _set_member(variant, "TimeBetweenTwoShots", base_salvo_time)
        _set_member(variant, "TimeBetweenTwoFx", base_salvo_time)

    _set_member(variant, "ShotsCountPerSalvo", length)
    _set_member(variant, "AffichageMunitionParSalve", length)
    # Magazine packs many shots into one salvo; UI must not show per-salvo accuracy.
    _set_member(variant, "DisplaySalveAccuracy", False)

    base_cost = _read_float_member(base_descr, "SupplyCost")
    if base_cost is not None:
        _set_member(variant, "SupplyCost", base_cost * length)


def create_infantry_magazine_variants(
    source_path: Any,
    base_descr: Any,
    weapon_name: str,
    variant_entries: List[Dict[str, Any]],
) -> None:
    """Create or update ``Ammo_{weapon}_salvolength{N}`` / ``_infmagazine{N}`` clones.

    ``variant_entries`` items: ``{"length": int, "kind": "salvolength"|"infmagazine"}``.
    Timing is taken from ``base_descr`` (1-shot) before vehicle salvo-reload scaling.
    """
    if not variant_entries:
        return

    for entry in variant_entries:
        length = int(entry["length"])
        if length <= 1:
            continue
        kind = entry.get("kind") or "salvolength"
        if kind == "infmagazine":
            namespace = f"Ammo_{weapon_name}_infmagazine{length}"
        else:
            namespace = f"Ammo_{weapon_name}_salvolength{length}"

        existing = source_path.by_n(namespace, strict=False)
        if existing:
            apply_infantry_magazine_timing(existing, base_descr, length)
            logger.info("Updated infantry magazine variant %s", namespace)
            continue

        variant = base_descr.copy()
        variant.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
        variant.namespace = namespace
        apply_infantry_magazine_timing(variant, base_descr, length)
        source_path.add(variant)
        logger.info("Created infantry magazine variant %s", namespace)


def variants_for_weapon(
    game_db: Dict[str, Any],
    weapon_name: str,
) -> List[Dict[str, Any]]:
    """Look up precomputed magazine variants for a base weapon name."""
    ammo_db = game_db.get("ammunition") or {}
    data = ammo_db.get("infantry_at_aa_magazine_salvos") or {}
    by_weapon = data.get("variants_by_weapon") or {}
    return list(by_weapon.get(weapon_name) or [])
