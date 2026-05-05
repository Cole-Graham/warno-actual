"""Functions for modifying game constants."""

from typing import List, Tuple, Union
from src.constants import TANDEM_MODIFIER
from src.constants.weapons.standards import (
    AA_ADDITIONAL_SUPPRESS_PER_LOST_PHYSICAL,
)


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
            row.v.by_m("StunEffectDuration").v = "3.0"
            # logger.info("Set stun effect duration to 3.0")

        elif row.namespace == "WargameConstantes":
            edits: List[Tuple[str, str, Union[str, int], Union[str, None]]] = [
                ("value", "ConquestPointsDefaultIndex", 0, None),
                ("value", "ConquestPossibleScores", "[3500, 4000]", None),
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
            
            row.v.by_m("TandemModifierValue").v = str(TANDEM_MODIFIER)
            
            # 25 is default value for AdditionalSuppressDamagePerLostPhysicalDamage
            # Re-applying it here in case Eugen decided to change it without me realizing it
            row.v.by_m("AdditionalSuppressDamagePerLostPhysicalDamage").v = str(AA_ADDITIONAL_SUPPRESS_PER_LOST_PHYSICAL)
            
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
            # e.g. For a radius of 100m, 0.15 means the damage starts to fall off at 15m from the center.
            # The WARNO engine only recalculates splash damage every ? amount of distance, so very small
            # splash radiuses will feel very binary. I haven't determined the exact value yet.
            row.v.by_m("SplashRatioDamage").v = "[0.05, 0.05, 0.05]"
            row.v.by_m("SplashRatioDistance").v = "[0.15, 0.15, 0.10]"
