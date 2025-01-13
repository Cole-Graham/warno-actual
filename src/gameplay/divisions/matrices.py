"""Functions for modifying division cost matrices."""

from src.dics.division_edits.matrix_data import DIVISION_MATRICES
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_division_matrices(source) -> None:
    """Edit division cost matrices in DivisionCostMatrix.ndf."""
    logger.info("Editing division cost matrices")
    
    for matrix_name, matrix_data in DIVISION_MATRICES.items():
        try:
            index = source.by_n(matrix_name).index
            source.replace(index, matrix_data)
            logger.info(f"Updated matrix for {matrix_name}")
        except Exception as e:
            logger.error(f"Failed to update matrix {matrix_name}: {str(e)}") 