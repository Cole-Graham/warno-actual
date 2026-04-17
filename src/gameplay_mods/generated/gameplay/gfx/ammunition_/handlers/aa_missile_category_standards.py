"""Apply A2A / SAM / MANPAD AA missile category standards (``HitRollRuleDescriptor``)."""

from typing import Any, Dict

from src.constants.weapons.standards import (
    A2A_STANDARDS,
    AA_ADDITIONAL_SUPPRESS_PER_LOST_PHYSICAL,
    MANPAD_STANDARDS,
    SAM_STANDARDS,
)


def apply_category_aa_missile_standards(descr: Any, category: str) -> None:
    """Set ``DistanceToTarget`` on ``HitRollRuleDescriptor`` for categories ``A2A``, ``SAM`` and ``MANPAD``."""
    if category == "A2A":
        hit_roll = A2A_STANDARDS["hit_roll"]
    elif category == "SAM":
        hit_roll = SAM_STANDARDS["hit_roll"]
    elif category == "MANPAD":
        hit_roll = MANPAD_STANDARDS["hit_roll"]
    else:
        return

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
