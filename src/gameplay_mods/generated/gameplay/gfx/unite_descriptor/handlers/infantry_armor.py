"""Apply ResistanceFamily_infanterieWA Blindage to infantry squads after edits."""

from __future__ import annotations

from typing import Any, Dict, Optional, Set

from src import ndf
from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.standards import (
    INFANTRY_ARMOR_PATTERN_STANDARD,
    infantry_wa_armor_index,
    is_excluded_hmg_team_unit,
)
from src.utils.ndf_utils import find_obj_by_type, strip_quotes

_ARMOR_PARTS = (
    "ResistanceFront",
    "ResistanceSides",
    "ResistanceRear",
    "ResistanceTop",
)


def _new_unit_edits_by_name() -> Dict[str, Dict[str, Any]]:
    by_name: Dict[str, Dict[str, Any]] = {}
    for _donor_key, edits in NEW_UNITS.items():
        if not isinstance(edits, dict):
            continue
        new_name = edits.get("NewName")
        if not new_name:
            continue
        by_name[new_name] = edits
    return by_name


def _units_with_explicit_armor_dict(
    unit_edits: Dict[str, Any],
    new_units_by_name: Dict[str, Dict[str, Any]],
) -> Set[str]:
    """Units whose constants provide an armor dict (vehicle / custom Blindage)."""
    explicit: Set[str] = set()
    for unit_name, edits in unit_edits.items():
        if isinstance(edits, dict) and isinstance(edits.get("armor"), dict):
            explicit.add(unit_name)
    for unit_name, edits in new_units_by_name.items():
        if isinstance(edits.get("armor"), dict):
            explicit.add(unit_name)
    return explicit


def _collect_tag_strings(tagset_list: Any) -> Set[str]:
    """Flatten TagSet rows into stripped tag names.

    ``TagSet.overwrite_all`` assigns ``ndf.convert(str(python_list))``, which
    nests one ``List`` of string rows inside TagSet. Vanilla TagSets are flat
    string rows. Recurse so both shapes resolve the same way.
    """
    tags: Set[str] = set()
    if tagset_list is None:
        return tags
    for row in tagset_list:
        value = row.v if hasattr(row, "v") else row
        if isinstance(value, ndf.model.List):
            tags |= _collect_tag_strings(value)
            continue
        tags.add(strip_quotes(str(value)))
    return tags


def live_tagset(modules_list: Any) -> Set[str]:
    """Return stripped tag names from live TTagsModuleDescriptor.TagSet."""
    tags_module = find_obj_by_type(modules_list.v, "TTagsModuleDescriptor")
    if tags_module is None:
        return set()
    tagset = tags_module.v.by_m("TagSet", False)
    if tagset is None:
        return set()
    return _collect_tag_strings(tagset.v)


def unit_has_infanterie_tag(modules_list: Any) -> bool:
    """True when live TagSet contains Infanterie."""
    return "Infanterie" in live_tagset(modules_list)


def resolve_live_strength(modules_list: Any) -> Optional[int]:
    """Read MaxPhysicalDamages from TBaseDamageModuleDescriptor."""
    base_damage = find_obj_by_type(modules_list.v, "TBaseDamageModuleDescriptor")
    if base_damage is None:
        return None
    strength_row = base_damage.v.by_m("MaxPhysicalDamages", False)
    if strength_row is None:
        return None
    try:
        return int(float(str(strength_row.v)))
    except (TypeError, ValueError):
        return None


def apply_wa_armor_to_damage_module(
    damage_module: Any,
    strength: int,
    std: Optional[Dict[str, Any]] = None,
) -> bool:
    """Set WA Family + Index on rewritable infantry Blindage facings.

    Returns True when at least one facing was updated.
    """
    rule = std or INFANTRY_ARMOR_PATTERN_STANDARD
    blindage = damage_module.v.by_m("BlindageProperties", False)
    if blindage is None:
        return False

    armor_family = rule["armor_family"]
    armor_index = str(infantry_wa_armor_index(strength, rule["strength_index_base"]))
    rewritable = rule["rewritable_families"]
    updated = False

    for part in _ARMOR_PARTS:
        resistance = blindage.v.by_m(part, False)
        if resistance is None:
            continue
        family_row = resistance.v.by_m("Family", False)
        if family_row is None:
            continue
        family = strip_quotes(str(family_row.v))
        if family not in rewritable:
            continue
        family_row.v = armor_family
        index_row = resistance.v.by_m("Index", False)
        if index_row is not None:
            index_row.v = armor_index
        updated = True

    return updated


def should_apply_infantry_wa_armor(
    unit_name: str,
    modules_list: Any,
    explicit_armor_units: Set[str],
    std: Optional[Dict[str, Any]] = None,
) -> bool:
    """Detection gate used by the pattern standard and tests."""
    rule = std or INFANTRY_ARMOR_PATTERN_STANDARD
    if unit_name in explicit_armor_units:
        return False
    if is_excluded_hmg_team_unit(unit_name, rule["excluded_prefixes"]):
        return False

    tags = live_tagset(modules_list)
    if "Infanterie" not in tags:
        return False
    if rule["excluded_at_team_tag"] in tags:
        return False
    return True


def apply_infantry_armor_pattern_standard(
    logger: Any,
    source_path: Any,
    game_db: Dict[str, Any],
) -> None:
    """Apply WA infantry Blindage to squads after unit_edits / new_units / ATGM."""
    std = INFANTRY_ARMOR_PATTERN_STANDARD
    unit_edits = load_unit_edits()
    new_units_by_name = _new_unit_edits_by_name()
    explicit_armor = _units_with_explicit_armor_dict(unit_edits, new_units_by_name)
    updated = 0

    for unit_descr in source_path:
        unit_name = unit_descr.namespace.replace("Descriptor_Unit_", "")
        modules_list = unit_descr.v.by_m("ModulesDescriptors")

        if not should_apply_infantry_wa_armor(
            unit_name, modules_list, explicit_armor, std,
        ):
            continue

        strength = resolve_live_strength(modules_list)
        if strength is None:
            logger.warning(
                f"Infantry WA armor: missing MaxPhysicalDamages on {unit_name}",
            )
            continue

        damage = find_obj_by_type(modules_list.v, "TDamageModuleDescriptor")
        if damage is None:
            logger.warning(
                f"Infantry WA armor: missing TDamageModuleDescriptor on {unit_name}",
            )
            continue

        if apply_wa_armor_to_damage_module(damage, strength, std):
            updated += 1

    if updated:
        logger.info(f"Infantry WA armor: updated {updated} squad(s)")
