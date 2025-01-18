"""Shared FOB modifications."""

from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def add_fob_minimap_texture(source_path):    
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

def add_fob_minimap_module(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/BuildingDescriptors.ndf"""
    logger.info("Adding FOB minimap texture module")
    
    for fob_descr in source_path:
        modules_list = fob_descr.v.by_m("ModulesDescriptors").v
        insert_index = -1
        
        # Find insertion point after production module
        for i, module in enumerate(modules_list):
            if not isinstance(module.v, ndf.model.Object):
                continue
            if module.v.type == "TProductionModuleDescriptor":
                insert_index = i
                break
                
        if insert_index >= 0:
            minimap_module = (
                'TMinimapDisplayModuleDescriptor'
                '('
                '    Texture = "Texture_Minimap_Unit_fob"'
                '    FollowUnitOrientation = False'
                ')'
            )
            modules_list.insert(insert_index, minimap_module)
            logger.info("Added FOB minimap texture module") 