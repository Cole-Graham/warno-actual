"""Functions for modifying CapaciteList.ndf"""

from src.constants import CQC_RANGE
from src.constants.capacities import (
    SPRINT_CAPACITY,
    CHOC_INRANGE_CAPACITY,
    CHOC_INRANGE_FEEDBACK_CAPACITY,
    CMD_UNIT_CAPACITY,
    DEPLOY_CAPACITY,
    DEPLOY_OK_CAPACITY,
    LDR_ARTY_CAPACITY,
    LDR_INF_CAPACITY,
    LDR_TNK_CAPACITY,
    MEDIUM_EQUIP_PENALTY_CAPACITY,
    MEDIUM_EQUIP_PENALTY_SF_CAPACITY,
    NO_SWIFT_CAPACITY,
    RELOAD_PENALTY_CAPACITY,
    SWIFT_CAPACITY,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_gp_gfx_capacitelist(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/CapaciteList.ndf"""
    logger.info("Modifying capacities")

    # Edit capacities
    for capacite_descr in source_path:
        if capacite_descr.n == "Capacite_Choc":
            new_range_value = str(CQC_RANGE)
            capacite_descr.v.by_m("RangeGRU").v = new_range_value
            conditions = capacite_descr.v.by_m("Conditions", False)
            if conditions:
                already_present = conditions.v.find_by_cond(
                    lambda row: row.v == "~/ConditionNotInMovement",
                    strict=False,
                )
                if not already_present:
                    conditions.v.add("~/ConditionNotInMovement")
            else:
                capacite_descr.v.add("Conditions = [~/ConditionNotInMovement,]")
            logger.info(
                f"Updated Capacite_Choc range to {new_range_value}m "
                f"and require ConditionNotInMovement",
            )

        elif capacite_descr.n == "Capacite_Choc_feedback":
            conditions = capacite_descr.v.by_m("Conditions", False)
            if conditions:
                already_present = conditions.v.find_by_cond(
                    lambda row: row.v == "~/ConditionTagNotRaisedInUnit_choc_inrange_1",
                    strict=False,
                )
                if not already_present:
                    conditions.v.add("~/ConditionTagNotRaisedInUnit_choc_inrange_1")
            else:
                capacite_descr.v.add(
                    "Conditions = ["
                    "~/ConditionTagNotRaisedInUnit_choc_ok,"
                    "~/ConditionTagNotRaisedInUnit_choc_inrange_1,"
                    "]",
                )
            logger.info(
                "Updated Capacite_Choc_feedback to require choc_inrange not raised",
            )

        elif capacite_descr.n == "Capacite_electronic_warfare":
            new_range_value = "5000"
            capacite_descr.v.by_m("RangeGRU").v = new_range_value
            logger.info(f"Updated Capacite_electronic_warfare range to {new_range_value}m")

    # Add new capacities
    for i, row in enumerate(source_path, start=1):
        if row.namespace == "Capacite_Choc":
            source_path.insert(i, CHOC_INRANGE_FEEDBACK_CAPACITY)
            source_path.insert(i, CHOC_INRANGE_CAPACITY)
            source_path.insert(i, SPRINT_CAPACITY)
            source_path.insert(i, SWIFT_CAPACITY)
            source_path.insert(i, NO_SWIFT_CAPACITY)
            source_path.insert(i, DEPLOY_OK_CAPACITY)
            source_path.insert(i, DEPLOY_CAPACITY)
            source_path.insert(i, MEDIUM_EQUIP_PENALTY_CAPACITY)
            source_path.insert(i, MEDIUM_EQUIP_PENALTY_SF_CAPACITY)
            source_path.insert(i, LDR_TNK_CAPACITY)
            source_path.insert(i, LDR_ARTY_CAPACITY)
            source_path.insert(i, LDR_INF_CAPACITY)
            source_path.insert(i, CMD_UNIT_CAPACITY)
            source_path.insert(i, RELOAD_PENALTY_CAPACITY)
            break
