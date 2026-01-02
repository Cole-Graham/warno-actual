"""Functions for modifying game constants."""

from typing import List, Tuple, Union
import ndf_parse as ndf

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gameplay_constantes_hitrollconstants(source_path) -> None:
    """GameData/Gameplay/Constantes/HitRollConstants.ndf

    Args:
        source_path: The NDF file being edited
    """
    logger.info("------------- editing HitRollConstants.ndf -------------")

    hitroll_params = source_path.by_n("HitRollParams")
    range_modifiers_table = hitroll_params.v.by_m("RangeModifiersTable")
    new_values = """[
        (0.05, 300),
        (0.17, 250),
        (0.33, 200),
        (0.50, 70),
        (0.67, 30),
        (1.00, 0),
        (9999, 0)
    ]"""
    range_modifiers_table.v = ndf.convert(new_values)
    logger.info("Set range modifiers table to new values")
