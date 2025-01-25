"""Functions for modifying division UI elements."""

from src.constants.ui.divisions import GRAY_EMBLEMS, DIVISION_EMBLEMS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_division_emblems(source_path) -> None:
    """Edit division emblems in DivisionTextures.ndf."""
    logger.info("Modifying/Adding division emblem textures in DivisionTextures.ndf")
    
    for division in GRAY_EMBLEMS:
        namespace_prefix = "Texture_Division_Emblem_"
        texture_obj = source_path.by_n(namespace_prefix + division).v
        filename = f'"GameData:/Assets/2D/Interface/UseOutGame/Division/Emblem/{division}_gray.png"'
        texture_obj.by_m("FileName").v = filename
        logger.info(f"Changed {division} texture to {filename.split('/')[-1]}")
        
    for emblem_namespace, data in DIVISION_EMBLEMS.items():
        _dir = data["texture_dir"]
        texture = data["texture"]
        namespace_prefix = "Texture_Division_Emblem_"
        new_entry = (
            f'{namespace_prefix}{emblem_namespace} is TUIResourceTexture_Common'
            '('
            f'  FileName = "GameData:{_dir}/{texture}"'
            ')'
        )
        
        texturebank_obj = source_path.by_n("DivisionAdditionalTextureBank")
        texturebank_index = texturebank_obj.index
        source_path.insert(texturebank_index, new_entry)
        
        textures_map = texturebank_obj.v.by_m("Textures")
        new_entry = (
            '('
            f'"{namespace_prefix}{emblem_namespace}",'
            f'MAP[(~/ComponentState/Normal, ~/{namespace_prefix}{emblem_namespace})]'
            ')'
        )
        textures_map.v.add(new_entry)
        logger.info(f"Added new texture: {namespace_prefix}{emblem_namespace}")
