"""Apply A2A / SAM / MANPAD AA missile category standards (``HitRollRuleDescriptor``)."""

from typing import Any

from src.constants.weapons.standards import A2A_STANDARDS, MANPAD_STANDARDS, SAM_STANDARDS


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
