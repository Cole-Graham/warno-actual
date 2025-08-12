"""Functions for modifying game constants."""

from typing import List, Tuple, Union

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_constantes_gdconstants(source_path) -> None:
    """GameData/Gameplay/Constantes/GDConstants.ndf

    Args:
        source_path: The NDF file being edited
    """
    logger.info("------------- editing GDConstants.ndf -------------")

    for row in source_path:
        if row.namespace == "Constantes":
            row.v.by_m("StunEffectDuration").v = "2.5"
            logger.info("Set stun effect duration to 2.5")

        elif row.namespace == "WargameConstantes":
            edits: List[Tuple[str, str, Union[str, int], Union[str, None]]] = [
                ("value", "ConquestPossibleScores", "[2000, 3000, 4000]", None),
                ("map", "BaseIncome", 21, "ECombatRule/Conquest"),
                ("map", "TimeBeforeEarningCommandPoints", 6, "ECombatRule/Conquest"),
                ("value", "DefaultArgentInitial", 2000, None),
            ]

            membr = row.v.by_m
            for membr_type, var, edit, key in edits:
                if membr_type == "map":
                    membr(var).v.by_k(key).v = str(edit)
                    logger.info(f"Set {var} to {edit}")
                elif membr_type == "value":
                    membr(var).v = str(edit)
                    logger.info(f"Set {var} to {edit}")

        elif row.namespace == "ModernWarfareConstantes":
            row.v.by_m("FrontSideAngleInDeg").v = "75"
            logger.info("Set FrontSideAngleInDeg to 75")

            row.v.by_m("SplashRatioDamage").v = "[0.15, 0.15, 0.01]"
            row.v.by_m("SplashRatioDistance").v = "[0.15, 0.15, 0.1]"
            logger.info("Set splash ratios: Damage=[0.15, 0.15, 0.01], Distance=[0.15, 0.15, 0.1]")
