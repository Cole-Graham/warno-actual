"""Functions for modifying Divisions.ndf"""

from src.utils.logging_utils import setup_logger
from src import ModConfig

logger = setup_logger(__name__)


def edit_gen_gp_decks_divisions(source_path) -> None:
    """GameData/Generated/Gameplay/Decks/Divisions.ndf"""

    config = ModConfig.get_instance()

    hide_divs = config.config_data.get("hide_divs", [])
    if config.config_data["build_config"]["write_dev"]:
        # In dev mode, remove divisions that should be shown for testing
        dev_show_divs = config.config_data.get("dev_show_divs", [])
        divs_to_hide = [div for div in hide_divs if div not in dev_show_divs]
    else:
        # In release mode, hide all divisions in hide_divs
        divs_to_hide = hide_divs

    indices_to_remove = []
    logger.info("Modifying hidden divisions in Divisions.ndf ")    
    for division in divs_to_hide:
        div_index = source_path.by_n(f"Descriptor_Deck_Division_{division}").index
        indices_to_remove.append(div_index)

    for index in sorted(indices_to_remove, reverse=True):
        source_path.remove(index)
    
    for deck_descr in source_path:
        MaxActivationPoints = deck_descr.v.by_member("MaxActivationPoints", False)
        if MaxActivationPoints and MaxActivationPoints.v == "50":
            MaxActivationPoints.v = "100"