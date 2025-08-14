"""Functions for modifying division cost matrices."""

from typing import Any

from src.constants.division_edits.matrix_data import DIVISION_MATRICES
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_gp_decks_divisioncostmatrix(source) -> None:
    """GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf"""
    logger.info("Editing division cost matrices")
    matrix_names = []
    for matrix_name, matrix_data in DIVISION_MATRICES.items():
        try:
            matrix_names.append(matrix_name)
            index = source.by_n(matrix_name).index
            source.replace(index, matrix_data)
            logger.info(f"Updated matrix for {matrix_name}")
        except Exception as e:
            logger.error(f"Failed to update matrix {matrix_name}: {str(e)}")

    for matrix_map in source:
        if matrix_map.n.endswith("_multi") and matrix_map.n not in matrix_names:
            # multiply all values by 2 as default — for dev purposes — until we define it in DIVISION_MATRICES
            for matrix_row in matrix_map.v:
                factory_key = matrix_row.k
                card_cost_list = matrix_row.v
                for card_cost in card_cost_list:
                    card_cost.v = str(int(card_cost.v) * 2)
