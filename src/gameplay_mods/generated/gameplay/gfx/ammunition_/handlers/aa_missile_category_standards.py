"""Apply A2A / SAM / MANPAD AA missile category standards (``HitRollRuleDescriptor``)."""

from typing import Any, Dict

from src.constants.weapons.standards import (
    AA_ADDITIONAL_SUPPRESS_PER_LOST_PHYSICAL,
    AA_CATEGORIES,
    AA_HAGRU_STANDARDS,
)

# Categories whose non-HAGRU originals can degenerate into "anti-plane only"
# when their ``MaximumRangeHelicopterGRU`` is 0 (e.g. AA_R98MT, AA_Skyflash).
# MANPAD is excluded because every MANPAD original engages helicopters.
_AA_PLANE_ONLY_CHECK_CATEGORIES = frozenset({"A2A", "SAM"})


def _read_max_range_helicopter_gru(descr: Any) -> int | None:
    """Return ``MaximumRangeHelicopterGRU`` as int, or ``None`` if absent/unparseable."""
    membr = descr.v.by_m("MaximumRangeHelicopterGRU", False)
    if membr is None:
        return None
    try:
        return int(str(membr.v))
    except (TypeError, ValueError):
        return None


def apply_category_aa_missile_standards(descr: Any, category: str, weapon_name: str) -> None:
    """Apply AA missile category standards to ``HitRollRuleDescriptor``.

    ``DistanceToTarget = False`` (no accuracy range scaling) is applied to
    descriptors that only ever engage planes:
      * ``_HAGRU`` variants (restricted to planes by damage family).
      * Non-HAGRU SAM/A2A originals whose ``MaximumRangeHelicopterGRU`` is 0
        (helicopter-incapable by range envelope, e.g. AA_R98MT).

    All other AA missiles keep the vanilla default so range-scaled accuracy
    still applies when engaging helicopters.

    Note: this should be called *after* the per-missile dict edits have been
    applied to the descriptor, so that any dict overrides of
    ``MaximumRangeHelicopterGRU`` are reflected in the check.
    """
    if category not in AA_CATEGORIES:
        return

    is_hagru = weapon_name.endswith("_HAGRU")

    if not is_hagru:
        if category not in _AA_PLANE_ONLY_CHECK_CATEGORIES:
            return
        helo_range = _read_max_range_helicopter_gru(descr)
        if helo_range is None or helo_range > 0:
            return

    hit_roll = AA_HAGRU_STANDARDS.get("hit_roll", {})
    if "DistanceToTarget" not in hit_roll:
        return

    use_distance_scaling = hit_roll["DistanceToTarget"]
    hitroll_obj = descr.v.by_m("HitRollRuleDescriptor")
    dis_to_target_membr = hitroll_obj.v.by_m("DistanceToTarget", False)
    if dis_to_target_membr:
        dis_to_target_membr.v = str(use_distance_scaling)
    else:
        hitroll_obj.v.add(f"DistanceToTarget = {str(use_distance_scaling)}")


def apply_aa_suppress_standard(
    descr: Any,
    weapon_name: str,
    game_db: Dict[str, Any],
    logger: Any,
) -> None:
    """Set ``SuppressDamages`` from the precomputed AA suppress mapping.

    The precomputed entry stores the *intended* total suppress damage (the
    value the target should effectively receive) together with the final
    ``PhysicalDamages`` used to derive it. The engine adds
    ``AdditionalSuppressDamagePerLostPhysicalDamage * PhysicalDamages`` to the
    written ``SuppressDamages`` at runtime, so we subtract the same product
    here to cancel it out.

    Lookup uses base *weapon_name* (no ``Ammo_`` prefix, no salvo suffix)
    so the same key works for base descriptors and all salvo variants.
    """
    aa_suppress = game_db.get("ammunition", {}).get("aa_suppress_damages", {})
    entry = aa_suppress.get(weapon_name)
    if entry is None:
        return

    intended = entry.get("suppress_damage")
    physical = entry.get("physical_damage")
    if intended is None or physical is None:
        logger.warning(
            f"(aa_suppress) {weapon_name}: incomplete entry {entry}, skipping",
        )
        return

    final_suppress = int(intended) - AA_ADDITIONAL_SUPPRESS_PER_LOST_PHYSICAL * int(physical)
    descr.v.by_m("SuppressDamages").v = str(final_suppress)
    logger.debug(
        f"(aa_suppress) {weapon_name}: intended={intended}, "
        f"physical={physical}, set SuppressDamages = {final_suppress}",
    )
