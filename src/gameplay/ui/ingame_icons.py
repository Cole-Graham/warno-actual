"""Functions for modifying in-game UI icons."""

from src.constants.ui.icons import INGAME_ICONS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_ingame_icons(source) -> None:
    """Edit in-game icons in UseInGameTextures.ndf."""
    logger.info("Adding new in-game icons")
    
    texturebank_obj = source.by_n("UseInGame_AdditionalTextureBank").v
    textures_map = texturebank_obj.by_m("Textures").v
    
    for icon_id, data in INGAME_ICONS.items():
        texture = data["texture"]
        texture_dir = data["texture_dir"]
        
        # Create texture entry
        icon_entry = (
            f'("icone_{icon_id}", MAP ['
            f'(~/ComponentState/Normal, TUIResourceTexture_Common('
            f'    FileName = "GameData:{texture_dir}/{texture}"'
            f'))]'
            f'),'
        )
        
        # Find insertion point if specified
        if "insert_after" in data:
            insert_index = textures_map.by_k(f'"{data["insert_after"]}"').index + 1
            textures_map.insert(insert_index, icon_entry)
        else:
            textures_map.add(icon_entry)
            
        logger.info(f"Added icon: icone_{icon_id}") 