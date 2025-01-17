"""Functions for modifying division UI elements."""

from src.constants.ui.divisions import GRAY_EMBLEMS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_division_emblems(source_path) -> None:
    """Edit division emblems in DivisionTextures.ndf."""
    logger.info("Adding division emblem textures")
    
    for division in GRAY_EMBLEMS:
        namespace_prefix = "Texture_Division_Emblem_"
        texture_obj = source_path.by_n(namespace_prefix + division).v
        filename = f'"GameData:/Assets/2D/Interface/UseOutGame/Division/Emblem/{division}_gray.png"'
        texture_obj.by_m("FileName").v = filename
        logger.info(f"Changed {division} texture to {filename.split('/')[-1]}")