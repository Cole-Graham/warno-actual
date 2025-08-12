"""Functions for modifying ConditionsDescriptor.ndf"""

from src.constants.effects.capacities import CONDITIONS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gfx_conditionsdescriptor(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/ConditionsDescriptor.ndf"""
    logger.info("Modifying conditions")

    for condition in CONDITIONS:
        source_path.add(condition)