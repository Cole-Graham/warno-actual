"""Functions for modifying game constants."""

from typing import List, Tuple, Union

# from src.utils.logging_utils import setup_logger

# logger = setup_logger(__name__)


def edit_gameplay_constantes_gdconstants(source_path) -> None:
    """GameData/Gameplay/Constantes/GDConstants.ndf

    Args:
        source_path: The NDF file being edited
    """
    # logger.info("------------- editing GDConstants.ndf -------------")

    for row in source_path:
        if row.namespace == "Constantes":
            row.v.by_m("StunEffectDuration").v = "2.5"
            # logger.info("Set stun effect duration to 2.5")

        elif row.namespace == "WargameConstantes":
            edits: List[Tuple[str, str, Union[str, int], Union[str, None]]] = [
                ("value", "ConquestPossibleScores", "[2000, 3000, 4000]", None),
                ("map", "BaseIncome", 21, "ECombatRule/Conquest"),
                ("map", "TimeBeforeEarningCommandPointsSkirmish", 6, "ECombatRule/Conquest"),
                ("value", "DefaultArgentInitial", 2000, None),
                # ("value", "ArgentInitialSetting", "[1000, 1500, 2000, 2500, 3000, 3500]", None)
            ]

            membr = row.v.by_m
            for membr_type, var, edit, key in edits:
                if membr_type == "map":
                    membr(var).v.by_k(key).v = str(edit)
                    # logger.info(f"Set {var} to {edit}")
                elif membr_type == "value":
                    membr(var).v = str(edit)
                    # logger.info(f"Set {var} to {edit}")

        elif row.namespace == "ModernWarfareConstantes":
            row.v.by_m("FrontSideAngleInDeg").v = "75"
            # logger.info("Set FrontSideAngleInDeg to 75")
            
            # Values in splash ratios correspond to enum EDamageType
            # i.e. [Suppress, Physical, Stun]
            # EDamageType is TBaseClass
            # (
            #     Suppress  is 0
            #     Physical  is 1
            #     Stun      is 2
            #     Length    is 3
            # )
            # SplashRatioDamage is the damage ratio at the edge of the splash radius
            # SplashRatioDistance is the % of the splash radius at which damage BEGINS to fall off
            # The WARNO engine only recalculates splash damage every X amount of distance, so very small
            # splash radiuses will feel very binary.
            row.v.by_m("SplashRatioDamage").v = "[0.15, 0.15, 0.05]"
            row.v.by_m("SplashRatioDistance").v = "[0.15, 0.15, 0.10]"
