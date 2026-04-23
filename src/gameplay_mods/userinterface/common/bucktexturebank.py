"""Functions for modifying BUCKTextureBank.ndf."""

from src.constants.weapons.weapon_descriptions import (
    ADDITIONAL_WEAPON_TRAIT_ICON_TEXTURES,
    _WEAPON_TRAIT_ICON_DIR,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_ui_common_bucktexturebank(source) -> None:
    """GameData/UserInterface/Use/Common/BUCKTextureBank.ndf

    Add trait icon textures to Base_AdditionalTextureBank.Textures (Texture_Trait_Icon_* section).
    """
    logger.info("Adding BUCKTextureBank trait icon textures")

    texturebank_obj = source.by_n("Base_AdditionalTextureBank").v
    textures_map = texturebank_obj.by_m("Textures").v

    insert_after_key = '"Texture_Trait_Icon_cluster"'
    insert_index = textures_map.by_k(insert_after_key).index + 1

    for trait_key, filename in ADDITIONAL_WEAPON_TRAIT_ICON_TEXTURES:
        path = f"{_WEAPON_TRAIT_ICON_DIR}/{filename}"
        entry = (
            f'        ("{trait_key}",                          MAP [(~/ComponentState/Normal, '
            f"TUIResourceTexture_Common( FileName='{path}' )), ] ),"
        )
        textures_map.insert(insert_index, entry)
        insert_index += 1
        logger.info("Added trait icon texture %s -> %s", trait_key, path)
