"""Functions for modifying district (urban block) descriptors."""

from __future__ import annotations

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type, find_obj_by_type

logger = setup_logger(__name__)

DISTRICT_HP = {
    "HLM": 180,
    "Big": 120,
    "Mid": 90,
    "Small": 45,
}

def edit_gameplay_unit_districtdescriptor(source_path) -> None:
    """GameData/Gameplay/Unit/Tactic/DistrictDescriptor.ndf

    Set KillWhenDamagesReachMax to false for every exported DistrictDescriptor so
    districts are not destroyed when physical damage reaches MaxPhysicalDamages.
    """
    _modify_district_descriptors(source_path)
    # Unfortunately disabling district kill on death means it doesn't change terrain type either,
    # because the trigger for changing terrain type is the death of the district rather than the building.
    # logger.info("Modifying DistrictDescriptor.ndf (KillWhenDamagesReachMax = false)")

    # for row in source_path:
    #     if not hasattr(row, "v"):
    #         continue
    #     if not is_obj_type(row.v, "DistrictDescriptor"):
    #         continue

    #     ns = getattr(row, "namespace", None) or "(no namespace)"
    #     _set_kill_when_damages_reach_false(row.v)
    #     logger.info(f"DistrictDescriptor {ns}: KillWhenDamagesReachMax set to false")


def _modify_district_descriptors(source_path) -> None:
    """Modify district descriptors to set their HP based on their size."""
    for district_size in DISTRICT_HP:
        district_descriptor = source_path.by_n(f"Descriptor_District_{district_size}_District", False)
        if district_descriptor is None:
            logger.warning(f"District descriptor for {district_size} not found")
            continue
        district_descriptor.v.by_m("MaxPhysicalDamages").v = str(DISTRICT_HP[district_size])
        logger.info(f"District descriptor for {district_size} set to {DISTRICT_HP[district_size]}")


def _set_kill_when_damages_reach_false(descr: ndf.model.Object) -> None:
    """Set KillWhenDamagesReachMax false on descriptor root and TDamageModuleDescriptor."""
    try:
        descr.by_m("KillWhenDamagesReachMax").v = "false"
    except Exception:
        pass

    try:
        modules_list = descr.by_m("ModulesDescriptors").v
    except Exception:
        return

    for module in modules_list:
        if not is_obj_type(module.v, "TDamageModuleDescriptor"):
            continue
        try:
            module.v.by_m("KillWhenDamagesReachMax").v = "false"
        except Exception:
            pass
