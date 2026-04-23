"""Functions for modifying UseInGameTextures.ndf"""

from src.constants.ui.icons import INGAME_ICONS, INGAME_ICON_EDITS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_ui_ingame_useingametextures(source) -> None:
    """GameData/UserInterface/Use/InGame/UseInGameTextures.ndf

    Edit in-game icons in UseInGameTextures.ndf.
    """
    logger.info("Adding new in-game icons")

    texturebank_obj = source.by_n("UseInGame_AdditionalTextureBank").v
    textures_map = texturebank_obj.by_m("Textures").v

    for icon_id, data in INGAME_ICONS.items():
        texture = data["texture"]
        texture_dir = data["texture_dir"].rstrip("/")
        path = f"GameData:{texture_dir}/{texture}"

        # Create texture entry
        icon_entry = (
            f'("icone_{icon_id}", MAP ['
            f'    (~/ComponentState/Normal, TUIResourceTexture_Common(FileName = "{path}" ))]'
            f')'
        )

        # Find insertion point if specified
        if "insert_after" in data:
            insert_index = textures_map.by_k(f'"{data["insert_after"]}"').index + 1
            textures_map.insert(insert_index, icon_entry)
        else:
            textures_map.add(icon_entry)

        logger.info("Added icon: icone_%s", icon_id)

    for icon_id, data in INGAME_ICON_EDITS.items():
        namespace = f"{data['prefix']}{icon_id}"
        d = data["new_texture_dir"].rstrip("/")
        path = f"GameData:{d}/{data['new_texture']}"
        row = source.by_n(namespace, False)
        if not row:
            logger.error(
                "INGAME_ICON_EDITS: NDF object not found (expected vanilla %s); skipped",
                namespace,
            )
            continue
        row.v.by_m("FileName").v = f'"{path}"'
        logger.info("Set %s FileName to %s", namespace, path)
