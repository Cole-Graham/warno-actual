"""Apply helicopter manoeuvrability pattern standard (THelicopterMovementModuleDescriptor)."""

from typing import Any, Dict, Optional

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits.standards import (
    HELICOPTER_MOVEMENT_MANOEUVRABILITY_PATTERN_STANDARD,
)
from src.utils.ndf_utils import find_obj_by_type


def _modules_list_has_helico_flags(modules_list: Any) -> bool:
    for row in modules_list.v.inner():
        if row.v == "HelicoFlagsModuleDescriptor":
            return True
    return False


def _new_unit_has_helo_tag(unit_name: str) -> bool:
    for edits in NEW_UNITS.values():
        if edits.get("NewName") != unit_name:
            continue
        tags = edits.get("TagSet", {}).get("overwrite_all", [])
        return "Helo" in tags
    return False


def _is_new_unit_name(unit_name: str) -> bool:
    return any(edits.get("NewName") == unit_name for edits in NEW_UNITS.values())


def _new_unit_donor_is_helo(unit_name: str, unit_db: Dict[str, Any]) -> bool:
    """Donor helicopter in ``unit_data`` (new units use donor modules before new name is in DB)."""
    for donor_key, edits in NEW_UNITS.items():
        if edits.get("NewName") != unit_name:
            continue
        donor = donor_key[0]
        return bool(unit_db.get(donor, {}).get("is_helo_unit"))
    return False


def _unit_should_apply_helo_pattern(
    unit_name: str,
    unit_data: Optional[Dict[str, Any]],
    modules_list: Any,
    unit_db: Dict[str, Any],
) -> bool:
    """Match ``is_helo_unit`` in DB, donor helo, flags/tags, or a NEW_UNITS row (caller has helo module).

    Call only when ``THelicopterMovementModuleDescriptor`` is present so the final branch covers
    new helicopters before ``unit_data`` lists the new name.
    """
    if unit_data and unit_data.get("is_helo_unit"):
        return True
    if _modules_list_has_helico_flags(modules_list):
        return True
    if _new_unit_has_helo_tag(unit_name):
        return True
    if _new_unit_donor_is_helo(unit_name, unit_db):
        return True
    if _is_new_unit_name(unit_name):
        return True
    return False


def _bump_member(module_row: Any, name: str, delta: int) -> None:
    membr = module_row.v.by_m(name, None)
    if not membr:
        return
    cur = float(str(membr.v))
    membr.v = str(int(round(cur + delta)))


def apply_helicopter_movement_pattern_standard_for_unit(
    logger,
    game_db: Dict[str, Any],
    unit_name: str,
    modules_list: Any,
) -> bool:
    """Apply manoeuvrability pattern to one unit. Returns True if values were bumped."""
    std = HELICOPTER_MOVEMENT_MANOEUVRABILITY_PATTERN_STANDARD
    dq = std["torque_flat_bonus"]
    cq = std["cyclic_flat_bonus"]
    unit_db = game_db.get("unit_data") or {}
    unit_data = unit_db.get(unit_name)

    helo_mod = find_obj_by_type(modules_list.v, "THelicopterMovementModuleDescriptor")
    if not helo_mod:
        return False
    if not _unit_should_apply_helo_pattern(
        unit_name,
        unit_data,
        modules_list,
        unit_db,
    ):
        return False
    _bump_member(helo_mod, "TorqueManoeuvrability", dq)
    _bump_member(helo_mod, "CyclicManoeuvrability", cq)
    logger.debug(
        f"Helicopter movement pattern: +{dq} torque / +{cq} cyclic ({unit_name})",
    )
    return True


def apply_helicopter_movement_pattern_standard(logger, source_path, game_db) -> None:
    """Bump ``TorqueManoeuvrability`` / ``CyclicManoeuvrability`` for all helicopter units.

    Run on vanilla ``UniteDescriptor`` rows before ``unit_edits`` / ``new_units`` handlers so
    per-unit overrides take priority. New units are handled via
    ``apply_helicopter_movement_pattern_standard_for_unit`` before ``_handle_modules_list``.
    """
    applied = 0

    for unit_row in source_path:
        if not hasattr(unit_row, "namespace"):
            continue
        if not unit_row.namespace.startswith("Descriptor_Unit_"):
            continue
        unit_name = unit_row.namespace.replace("Descriptor_Unit_", "")
        modules_list = unit_row.v.by_m("ModulesDescriptors")
        if apply_helicopter_movement_pattern_standard_for_unit(
            logger, game_db, unit_name, modules_list,
        ):
            applied += 1

    if applied:
        logger.info(
            f"Helicopter movement manoeuvrability pattern applied to {applied} unit(s)",
        )
