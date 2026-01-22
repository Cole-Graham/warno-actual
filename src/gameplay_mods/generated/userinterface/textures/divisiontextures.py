"""Functions for modifying DivisionTextures.ndf"""

from typing import Any

from src.constants.generated.gameplay.decks import load_new_divisions
from src.constants.ui.divisions import GRAY_EMBLEMS, DIVISION_EMBLEMS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Texture directory for new division emblems
NEW_DIVISION_EMBLEM_DIR = "/Assets/2D/Interface/UseOutGame/Division/Emblem"
NAMESPACE_PREFIX = "Texture_Division_Emblem_"


def edit_gen_ui_divisiontextures(source_path) -> None:
    """GameData/Generated/UserInterface/Textures/DivisionTextures.ndf"""
    logger.info("Modifying/Adding division emblem textures in DivisionTextures.ndf")
    _add_existing_division_emblems(source_path)
    _add_new_division_emblems(source_path)


def _add_existing_division_emblems(source_path: Any) -> None:
    """Add division emblem textures from DIVISION_EMBLEMS."""
    logger.info("Adding existing division emblem textures")
    
    for emblem_namespace, data in DIVISION_EMBLEMS.items():
        _dir = data["texture_dir"]
        texture = data["texture"]
        new_entry = (
            f'{NAMESPACE_PREFIX}{emblem_namespace} is TUIResourceTexture_Common'
            f'('
            f'    FileName = "GameData:{_dir}/{texture}"'
            f')'
        )

        texturebank_obj = source_path.by_n("DivisionAdditionalTextureBank")
        texturebank_index = texturebank_obj.index
        source_path.insert(texturebank_index, new_entry)

        textures_map = texturebank_obj.v.by_m("Textures")
        new_entry = (
            f'('
            f'    "{NAMESPACE_PREFIX}{emblem_namespace}",'
            f'    MAP[(~/ComponentState/Normal, ~/{NAMESPACE_PREFIX}{emblem_namespace})]'
            f')'
        )
        textures_map.v.add(new_entry)
        logger.info(f"Added new texture: {NAMESPACE_PREFIX}{emblem_namespace}")


def _add_new_division_emblems(source_path: Any) -> None:
    """Create division emblem textures for new national divisions.
    
    Texture file names are based on the keys in new divisions dictionaries (e.g., 'US_general' -> 'US_general.png').
    """
    new_divisions = load_new_divisions()
    
    if not new_divisions:
        logger.info("No new divisions to create emblems for")
        return
    
    logger.info("Creating division emblem textures for new national divisions")
    
    texturebank_obj = source_path.by_n("DivisionAdditionalTextureBank")
    texturebank_index = texturebank_obj.index
    textures_map = texturebank_obj.v.by_m("Textures")
    
    for div_key, div_data in new_divisions.items():
        # Texture file name is the same as the division key with .png extension
        texture_filename = f"{div_key}.png"
        emblem_namespace = div_key
        
        # Check if texture already exists
        texture_namespace = f"{NAMESPACE_PREFIX}{emblem_namespace}"
        try:
            existing_texture = source_path.by_n(texture_namespace, False)
            if existing_texture:
                logger.debug(f"Texture {texture_namespace} already exists, skipping")
                continue
        except (AttributeError, KeyError):
            pass  # Texture doesn't exist, which is expected
        
        # Create texture entry
        new_entry = (
            f'{texture_namespace} is TUIResourceTexture_Common'
            f'('
            f'    FileName = "GameData:{NEW_DIVISION_EMBLEM_DIR}/{texture_filename}"'
            f')'
        )
        
        # Insert texture entry
        source_path.insert(texturebank_index, new_entry)
        
        # Add to textures map
        map_entry = (
            f'('
            f'    "{texture_namespace}",'
            f'    MAP[(~/ComponentState/Normal, ~/{texture_namespace})]'
            f')'
        )
        textures_map.v.add(map_entry)
        logger.info(f"Added new division emblem texture: {texture_namespace} -> {texture_filename}")
    
    logger.info("Finished creating division emblem textures for new divisions")