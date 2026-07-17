"""Replace TCommanderModuleDescriptor with Capacite_CMD_UNIT / Capacite_LDR_INF."""

from __future__ import annotations

from typing import Any, Dict, Iterable, Optional, Set

from src.constants.unit_edits.standards import (
    COMMANDER_CAPACITE_PATTERN_STANDARD,
    resolve_commander_capacite_name,
)
from src.utils.ndf_utils import find_obj_by_type, strip_quotes

_SKILL_PREFIX = "$/GFX/EffectCapacity/Capacite_"


def _flatten_ndf_string_list(node: Any) -> Set[str]:
    """Collect string values from a TagSet, including nested lists.

    ``TagSet`` overwrite via ``ndf.convert(str(python_list))`` stores one nested
    list row (Python repr uses single-quoted strings). Vanilla TagSets are flat.
    """
    tags: Set[str] = set()
    if node is None:
        return tags
    if isinstance(node, (str, bytes)):
        tags.add(strip_quotes(str(node)))
        return tags

    try:
        rows: Iterable[Any] = node
    except TypeError:
        tags.add(strip_quotes(str(node)))
        return tags

    for row in rows:
        val = row.v if hasattr(row, "v") else row
        if isinstance(val, (str, bytes)):
            tags.add(strip_quotes(str(val)))
            continue
        # Nested list (overwrite_all convert) or other container.
        if val is not None and not isinstance(val, (int, float, bool)):
            try:
                iter(val)
            except TypeError:
                tags.add(strip_quotes(str(val)))
            else:
                tags |= _flatten_ndf_string_list(val)
        else:
            tags.add(strip_quotes(str(val)))
    return tags


def live_tagset(modules_list: Any) -> Set[str]:
    """Return stripped tag names from live TTagsModuleDescriptor.TagSet."""
    tags_module = find_obj_by_type(modules_list.v, "TTagsModuleDescriptor")
    if tags_module is None:
        return set()
    tagset = tags_module.v.by_m("TagSet", False)
    if tagset is None:
        return set()
    return _flatten_ndf_string_list(tagset.v)


def live_specialties(modules_list: Any) -> Set[str]:
    """Return stripped specialty names from live TUnitUIModuleDescriptor."""
    ui_module = find_obj_by_type(modules_list.v, "TUnitUIModuleDescriptor")
    if ui_module is None:
        return set()
    specialties = ui_module.v.by_m("SpecialtiesList", False)
    if specialties is None:
        return set()
    return _flatten_ndf_string_list(specialties.v)


def _ensure_capacite_on_unit(
    modules_list: Any,
    capacity_name: str,
) -> bool:
    """Append Capacite path to DefaultSkillList; create module if missing.

    Returns True when the capacity was newly added.
    """
    capacity_path = f"{_SKILL_PREFIX}{capacity_name}"
    capacite_module = find_obj_by_type(modules_list.v, "TCapaciteModuleDescriptor")

    if capacite_module is None:
        modules_list.v.add(
            "TCapaciteModuleDescriptor"
            "("
            f"        DefaultSkillList = [{capacity_path}]"
            ")"
        )
        return True

    default_skill_list = capacite_module.v.by_m("DefaultSkillList")
    already = default_skill_list.v.find_by_cond(
        lambda x, path=capacity_path: x.v == path,
        strict=False,
    )
    if already:
        return False
    default_skill_list.v.add(capacity_path)
    return True


def apply_commander_capacite_to_unit(
    logger: Any,
    unit_name: str,
    modules_list: Any,
    std: Optional[Dict[str, Any]] = None,
) -> bool:
    """Replace TCommanderModuleDescriptor with the matching Capacite.

    Returns True when the commander module was removed.
    """
    rule = std or COMMANDER_CAPACITE_PATTERN_STANDARD
    commander = find_obj_by_type(modules_list.v, "TCommanderModuleDescriptor")
    if commander is None:
        return False

    capacity_name = resolve_commander_capacite_name(
        live_tagset(modules_list),
        live_specialties(modules_list),
        rule,
    )
    _ensure_capacite_on_unit(modules_list, capacity_name)
    modules_list.v.remove(commander.index)
    logger.info(
        f"Replaced TCommanderModuleDescriptor with Capacite_{capacity_name} "
        f"on {unit_name}",
    )
    return True


def apply_commander_capacite_pattern_standard(
    logger: Any,
    source_path: Any,
    game_db: Dict[str, Any],
) -> None:
    """Swap remaining commander modules for CMD_UNIT / LDR_INF Capacites."""
    del game_db  # unused; signature matches other pattern standards
    std = COMMANDER_CAPACITE_PATTERN_STANDARD
    updated = 0

    for unit_descr in source_path:
        unit_name = unit_descr.namespace.replace("Descriptor_Unit_", "")
        modules_list = unit_descr.v.by_m("ModulesDescriptors")
        if apply_commander_capacite_to_unit(logger, unit_name, modules_list, std):
            updated += 1

    if updated:
        logger.info(
            f"Commander Capacite pattern: replaced TCommanderModuleDescriptor "
            f"on {updated} unit(s)",
        )
