"""Functions for modifying BUCKTextureBank.ndf."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Same directory as vanilla Texture_Trait_Icon_* entries (see BUCKTextureBank.ndf traits section).
_TRAIT_ICON_DIR = "GameData:/Assets/2D/Interface/Common/traits"

# New Texture_Trait_Icon_* rows (inserted after Texture_Trait_Icon_cluster).
ADDITIONAL_TRAIT_ICON_TEXTURES = (
    ("Texture_Trait_Icon_clusterHEAT", "cluster-heat.png"),
    ("Texture_Trait_Icon_clusterHEFrag", "cluster-hefrag.png"),
    ("Texture_Trait_Icon_biglyHE", "bigly-he.png"),
)


def edit_ui_common_bucktexturebank(source) -> None:
    """GameData/UserInterface/Use/Common/BUCKTextureBank.ndf

    Add trait icon textures to Base_AdditionalTextureBank.Textures (Texture_Trait_Icon_* section).
    """
    logger.info("Adding BUCKTextureBank trait icon textures")

    texturebank_obj = source.by_n("Base_AdditionalTextureBank").v
    textures_map = texturebank_obj.by_m("Textures").v

    insert_after_key = '"Texture_Trait_Icon_cluster"'
    insert_index = textures_map.by_k(insert_after_key).index + 1

    for trait_key, filename in ADDITIONAL_TRAIT_ICON_TEXTURES:
        path = f"{_TRAIT_ICON_DIR}/{filename}"
        entry = (
            f'        ("{trait_key}",                          MAP [(~/ComponentState/Normal, '
            f"TUIResourceTexture_Common( FileName='{path}' )), ] ),"
        )
        textures_map.insert(insert_index, entry)
        insert_index += 1
        logger.info("Added trait icon texture %s -> %s", trait_key, path)
