"""Functions for modifying out-game textures."""
from typing import Any, Dict

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

def edit_useoutgametextures(source_path) -> None:
    """Edit UseOutGameTextures.ndf.
    
    Args:
        source: NDF file containing out-game texture definitions
    """
    logger.info("Editing UseOutGameTextures.ndf")
    
    # Define new textures
    new_textures = _get_new_textures()
    
    # Find texture bank
    texture_bank_index = None
    textures_map = None
    
    for row in source_path:
        if not isinstance(row.v, ndf.model.Object) or not is_obj_type(row.v, "TBUCKToolAdditionalTextureBank"):
            continue
            
        texture_bank_index = row.index
        textures_map = row.v.by_member("Textures").v
        break
    
    if texture_bank_index is None or textures_map is None:
        logger.error("Could not find texture bank")
        return
    
    # Add new textures
    _add_new_textures(source_path, texture_bank_index, textures_map, new_textures)
    
    logger.debug("Added new textures")

def _get_new_textures() -> Dict[str, Dict[str, Any]]:
    """Get new texture definitions."""
    return {
        "rd_map_small": {
            "texture_dir": r"/Assets/2D/Interface/UseOutGame/TagMod",
            "title": (None, None),
            "description": (None, (None,)),
            "texture": "red_dragon_map_44x44.png",
        },
        "wa_logo_small": {
            "texture_dir": r"/Assets/2D/Interface/UseOutGame/TagMod",
            "title": (None, None),
            "description": (None, (None,)),
            "texture": "wa_logo_small.png",
        },
    }

def _add_new_textures(source_path, index: int, textures_map: Any, new_textures: Dict[str, Dict[str, Any]]) -> None:
    """Add new textures to source_path."""
    for texture, data in new_textures.items():
        file_name = data["texture"]
        
        # Add texture object
        obj_entry = f'''\
OutgameTexture_Mod_{texture} is TUIResourceTexture_Common
(
    FileName = "GameData:{data["texture_dir"]}/{file_name}"
)'''
        source_path.insert(index, obj_entry)
        
        # Add texture mapping
        map_entry = f'''\
("OutgameTexture_Mod_{texture}", MAP [
(~/ComponentState/Normal, ~/OutgameTexture_Mod_{texture})])'''
        textures_map.add(map_entry) 