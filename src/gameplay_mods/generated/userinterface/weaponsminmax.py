"""Functions for editing weapon min/max values."""

from typing import Any

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_ui_weaponsminmax(source_path: Any) -> None:
    """GameData/Generated/UserInterface/WeaponsMinMax.ndf"""
    logger.info("Editing weapons min/max values")

    root_obj = source_path.by_n("MinMaxValuesInterfaceHelper")
    weapons_map = root_obj.v.by_m("WeaponsMinMaxValues")
    
    minmax_atgm = weapons_map.v.by_key("~/MinMax_ATGM")
    minmax_atgm.v.by_m("Penetration").v.by_m("Min").v = "10"
    logger.debug("Changed ATGM UI color scaling minimum to 10 AP")

    minmax_bombe = weapons_map.v.by_key("~/MinMax_Bombe")
    penetration_bombe = minmax_bombe.v.by_m("Penetration")
    penetration_bombe.v.by_m("Min").v = "6"
    penetration_bombe.v.by_m("Max").v = "12"
    logger.debug("Changed Bombe UI color scaling minimum to 6 AP")
    logger.debug("Changed Bombe UI color scaling maximum to 12 AP")
