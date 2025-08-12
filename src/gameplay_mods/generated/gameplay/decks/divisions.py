"""Functions for modifying Divisions.ndf"""

from src.constants.generated.gameplay.decks import divs_not_released
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import ModConfig

logger = setup_logger(__name__)


def edit_decks_divisions(source_path) -> None:
    """GameData/Generated/Gameplay/Decks/Divisions.ndf"""

    config = ModConfig.get_instance()

    divs_to_hide = (
        divs_not_released if not config.config_data["build_config"]["write_dev"] else config.config_data["hide_divs"]
    )

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