"""Functions for modifying division cost matrices."""

from typing import Any

from src.constants.division_edits.matrix_data import DIVISION_MATRICES
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_division_matrices(source) -> None:
    """GameData/Generated/Gameplay/Decks/DivisionCostMatrix.ndf"""
    logger.info("Editing division cost matrices")

    for matrix_name, matrix_data in DIVISION_MATRICES.items():
        try:
            index = source.by_n(matrix_name).index
            source.replace(index, matrix_data)
            logger.info(f"Updated matrix for {matrix_name}")
        except Exception as e:
            logger.error(f"Failed to update matrix {matrix_name}: {str(e)}")


def deck_ap_points(source_path: Any) -> None:
    """Edit deck AP points in Divisions.ndf."""
    logger.info("Editing deck AP points")

    divisions = [
        "FR_5e_Blindee",
        "US_3rd_Arm",
        "US_8th_Inf",
        "US_11ACR",
        "US_82nd_Airborne",
        "UK_2nd_Infantry",
        "SOV_27_Gds_Rifle",
        "SOV_76_VDV",
        "SOV_119IndTkBrig",
        "RDA_7_Panzer",
        "POL_20_Pancerna",
        "POL_4_Zmechanizowana",
        "RDA_KdA_Bezirk_Erfurt",
        "RFA_TerrKdo_Sud",
    ]

    for deck_descr in source_path:
        for division in divisions:
            if deck_descr.namespace == f"Descriptor_Deck_Division_{division}_multi":
                deck_descr.v.by_member("MaxActivationPoints").v = "100"
