"""Remove _resolute specialty from shock units (Choc); resolute effect comes from Capacite_resolute."""

from typing import Any, Dict

from src.utils.ndf_utils import find_obj_by_type, strip_quotes

_CHOC_SPECIALTY = "_choc"
_RESOLUTE_SPECIALTY = "_resolute"


def _is_shock_unit(unit_data: Dict[str, Any], specialties_list: Any) -> bool:
    if unit_data:
        if "Choc" in unit_data.get("skills", []):
            return True
        if _CHOC_SPECIALTY in unit_data.get("specialties", []):
            return True
    for tag in specialties_list.v:
        if strip_quotes(tag.v) == _CHOC_SPECIALTY:
            return True
    return False


def remove_resolute_specialty_from_shock_unit(
    logger: Any,
    unit_name: str,
    unit_data: Dict[str, Any],
    specialties_list: Any,
) -> bool:
    """Strip _resolute from SpecialtiesList when the unit is shock (Choc)."""
    if not _is_shock_unit(unit_data, specialties_list):
        return False

    removed = False
    for tag in list(specialties_list.v):
        if strip_quotes(tag.v) == _RESOLUTE_SPECIALTY:
            specialties_list.v.remove(tag.index)
            removed = True

    if removed:
        logger.info(f"Removed _resolute specialty from shock unit {unit_name}")
    return removed


def apply_shock_no_resolute_specialty_pattern_standard(
    logger: Any,
    source_path: Any,
    game_db: Dict[str, Any],
) -> None:
    """Remove _resolute specialty from all shock units after unit_edits / new_units."""
    unit_db = game_db.get("unit_data", {})
    updated_units = 0

    for unit_descr in source_path:
        unit_name = unit_descr.namespace.replace("Descriptor_Unit_", "")
        modules_list = unit_descr.v.by_m("ModulesDescriptors")
        ui_module = find_obj_by_type(modules_list.v, "TUnitUIModuleDescriptor")
        if ui_module is None:
            continue

        specialties_list = ui_module.v.by_m("SpecialtiesList")
        if remove_resolute_specialty_from_shock_unit(
            logger,
            unit_name,
            unit_db.get(unit_name, {}),
            specialties_list,
        ):
            updated_units += 1

    if updated_units:
        logger.info(
            f"Shock no-resolute specialty: cleared _resolute on {updated_units} unit(s)",
        )
