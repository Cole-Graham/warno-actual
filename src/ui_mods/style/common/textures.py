"""Functions for modifying UI textures."""
from src.utils.logging_utils import setup_logger
# from src import ndf

logger = setup_logger(__name__)


def edit_commontextures(source_path) -> None:
    """Edit CommonTextures.ndf.
    
    Args:
        source_path: NDF file containing common texture definitions
    """
    logger.info("Editing CommonTextures.ndf")
    
    # Update cover texture paths
    cover_texture = source_path.by_namespace("CommonTexture_Couvert_Moyen").v
    cover_texture.by_member("FileName").v = '"GameData:/Assets/2D/Interface/Common/UnitsIcons/Cover/cover.png"'
    logger.debug("Updated medium cover texture path")
    
    urban_cover_texture = source_path.by_namespace("CommonTexture_Couvert_Lourd").v
    urban_cover_texture.by_member("FileName").v = '"GameData:/Assets/2D/Interface/Common/UnitsIcons/Cover/cover-box-small.png"'
    logger.debug("Updated heavy cover texture path")
