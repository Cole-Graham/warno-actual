"""Apply artillery deployment pattern standard (TWeaponDeploymentModuleDescriptor)."""

from typing import Any, Dict

from src.constants.unit_edits.standards.pattern.artillery_deployment import (
    ARTILLERY_PACKUP_TIME,
)
from src.utils.ndf_utils import find_obj_by_type


def apply_artillery_deployment_pattern_standard(
    logger,
    source_path: Any,
    game_db: Dict[str, Any],
) -> None:
    """Set deployment/packup times on artillery units from precomputed mapping."""
    deployment_data = game_db.get("deployment_time_units", {})
    unit_deployment_seconds = deployment_data.get("unit_deployment_seconds", {})
    if not unit_deployment_seconds:
        return

    updated = 0
    added = 0
    for unit_name, deploy_seconds in unit_deployment_seconds.items():
        unit_descr = source_path.by_n(f"Descriptor_Unit_{unit_name}", strict=False)
        if not unit_descr:
            logger.warning(f"Artillery deployment: unit descriptor not found for {unit_name}")
            continue

        modules_list = unit_descr.v.by_m("ModulesDescriptors")
        dep_module = find_obj_by_type(modules_list.v, "TWeaponDeploymentModuleDescriptor")
        if dep_module is None:
            modules_list.v.add(
                "TWeaponDeploymentModuleDescriptor("
                f"    TimeForWeaponDeployment = {deploy_seconds}"
                f"    TimeForWeaponPacking = {ARTILLERY_PACKUP_TIME}"
                ")",
            )
            added += 1
            logger.debug(f"Added TWeaponDeploymentModuleDescriptor to {unit_name} ({deploy_seconds}s)")
        else:
            dep_module.v.by_m("TimeForWeaponDeployment").v = str(deploy_seconds)
            dep_module.v.by_m("TimeForWeaponPacking").v = str(ARTILLERY_PACKUP_TIME)
            updated += 1

    logger.info(
        f"Artillery deployment pattern: {added} modules added, {updated} modules updated",
    )
