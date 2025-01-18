"""UI FOB modifications."""

from src.utils.logging_utils import setup_logger


logger = setup_logger(__name__)

def edit_minimapicons(source_path):    
    """GameData/Generated/UserInterface/Textures/MinimapIcons.ndf"""
    for i, obj in enumerate(source_path, start=0):
        if obj.namespace == "MinimapIconAdditionalTextureBank":
            texture_bank = obj.v
            append_texture = i
            break

    textures_map = texture_bank.by_member("Textures").v
    textures_list = ["fob"]
    for texture in textures_list:
        new_texture = (
            f'Texture_Minimap_Unit_{texture} is TUIResourceTexture_Common'
            f'('
            f'    FileName = "GameData:/Assets/2D/Interface/UseInGame/Minimap/{texture}.png"'
            f')'
        )
        source_path.insert(append_texture, new_texture)
    
        new_entry = (
            f'("Texture_Minimap_Unit_{texture}", MAP [(~/ComponentState/Normal, ~/Texture_Minimap_Unit_{texture})])'
        )
        textures_map.add(new_entry)
        logger.info(f"Added {texture} texture to MinimapIcons.ndf")