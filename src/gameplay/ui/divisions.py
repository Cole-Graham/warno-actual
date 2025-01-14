"""Functions for modifying division UI elements."""

from src.constants.ui.divisions import DIVISION_EMBLEMS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_division_emblems(source) -> None:
    """Edit division emblems in DivisionTextures.ndf."""
    logger.info("Adding division emblem textures")
    
    for emblem_id, data in DIVISION_EMBLEMS.items():
        texture = data["texture"]
        texture_dir = data["texture_dir"]
        
        obj_entry = (
            f'Texture_Division_Emblem_{emblem_id} is TUIResourceTexture_Common'
            f'('
            f'    FileName = "GameData:{texture_dir}/{texture}"'
            f')'
        )
        map_entry = (
            f'("Texture_Division_Emblem_{emblem_id}", MAP ['
            f'(~/ComponentState/Normal, '
            f'~/Texture_Division_Emblem_{emblem_id})]),'
        )
        
        # Find insertion point and add entries
        for i, row in enumerate(source):
            if row.namespace.startswith("Texture_"):
                continue
                
            append_index = i
            textures_map_obj = source.by_n("DivisionTextureBank").v
            textures_map = textures_map_obj.by_member("Textures").v
            textures_map.add(map_entry)
            source.insert(append_index, obj_entry)
            logger.info(f"Added {emblem_id} emblem texture")
            break 