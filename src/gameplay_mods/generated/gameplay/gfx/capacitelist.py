"""Functions for modifying CapaciteList.ndf"""

from src.constants.capacities import (
    NO_SPRINT_CAPACITY,
    SPRINT_OK_CAPACITY,
    SPRINT_CAPACITY,
    SPRINT_ACTIVATED_CAPACITY,
    SPRINT_BEGIN_COOLDOWN_CAPACITY,
    DEPLOY_CAPACITY,
    DEPLOY_OK_CAPACITY,
    LDR_ARTY_CAPACITY,
    LDR_TNK_CAPACITY,
    MEDIUM_EQUIP_PENALTY_CAPACITY,
    NO_SWIFT_CAPACITY,
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
            new_value = "150"
            capacite_descr.v.by_m("RangeGRU").v = new_value
            logger.info(f"Updated Capacite_Choc range to {new_value}m")

        elif capacite_descr.n == "Capacite_electronic_warfare":
            new_value = "5000"
            capacite_descr.v.by_m("RangeGRU").v = new_value
            logger.info(f"Updated Capacite_electronic_warfare range to {new_value}m")

    # Add new capacities
    for i, row in enumerate(source_path, start=1):
        if row.namespace == "Capacite_Choc":
            source_path.insert(i, SPRINT_CAPACITY)
            source_path.insert(i, SPRINT_ACTIVATED_CAPACITY)
            source_path.insert(i, SPRINT_BEGIN_COOLDOWN_CAPACITY)
            source_path.insert(i, NO_SPRINT_CAPACITY)
            source_path.insert(i, SPRINT_OK_CAPACITY)
            source_path.insert(i, SWIFT_CAPACITY)
            source_path.insert(i, NO_SWIFT_CAPACITY)
            source_path.insert(i, DEPLOY_OK_CAPACITY)
            source_path.insert(i, DEPLOY_CAPACITY)
            source_path.insert(i, MEDIUM_EQUIP_PENALTY_CAPACITY)
            source_path.insert(i, LDR_TNK_CAPACITY)
            source_path.insert(i, LDR_ARTY_CAPACITY)
            break
