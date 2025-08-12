"""Functions for editing weapon textures."""

from typing import Any

from src.constants.weapons import ammunitions
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_weapontextures(source: Any) -> None:
    """GameData/Generated/UserInterface/Textures/WeaponTextures.ndf"""
    logger.info("Editing weapon textures")

    # Find texture bank
    append_index, texture_bank = 0, ""
    for i, row in enumerate(source, start=0):
        if row.namespace == "WeaponAdditionalTextureBank":
            append_index = i
            texture_bank = row
            break

    # Add textures for new weapons
    for (weapon, category, donor, is_new), data in ammunitions.items():
        if data is None:
            continue

        for data_root, data_value in data.items():
            if data_root == "NewTexture":
                texture_file = f'"GameData:/Assets/2D/Interface/Common/UnitsIcons/Armes/Panel_Info/{weapon}.png"'

                # Add texture resource
                new_entry = (
                    f"Texture_Interface_Weapon_{weapon} is TUIResourceTexture_Common"
                    f"("
                    f"    FileName = {texture_file}"
                    f")"
                )
                source.insert(append_index, new_entry)

                # Add texture map entry
                new_map_entry = (
                    f'("Texture_Interface_Weapon_{weapon}", MAP ['
                    f"    (~/ComponentState/Normal, ~/Texture_Interface_Weapon_{weapon})"
                    f"]),"
                )
                texture_bank.v.by_m("Textures").v.add(new_map_entry)  # noqa
                logger.debug(f"Added texture and map entry for {weapon}")
