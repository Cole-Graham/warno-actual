"""Functions for modifying ButtonTexturesUnites.ndf"""

import re
from typing import Any

from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger


logger = setup_logger(__name__)

_FILENAME_FROM_MAP_STR = re.compile(
    r"FileName\s*=\s*(\"[^\"]+\"|'[^']+')",
)


def edit_gen_ui_buttontexturesunites(source_path: Any) -> None:
    """GameData/Generated/UserInterface/Textures/ButtonTexturesUnites.ndf"""

    _handle_new_units(source_path)


def _texture_filename_from_entry(texture_entry: Any) -> str:
    """Resolve FileName from a vanilla MAP row or a newly-added MAP string."""
    if isinstance(texture_entry, str):
        match = _FILENAME_FROM_MAP_STR.search(texture_entry)
        if not match:
            raise ValueError(f"Could not parse FileName from texture entry: {texture_entry!r}")
        return match.group(1)
    return texture_entry.by_key("~/ComponentState/Normal").v.by_member("FileName").v


def _handle_new_units(source_path: Any) -> None:
    """Handle new units for ButtonTexturesUnites.ndf"""

    logger.info("Creating button texture entries")

    textures_map = source_path.by_n("UnitButtonTextureAdditionalBank").v.by_member("Textures").v

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if "NewName" not in edits:
            continue

        unit_name = edits["NewName"]
        donor_texture_map = textures_map.by_key(f'"Texture_Button_Unit_{donor_name}"').v

        # Get the texture filename either from ButtonTexture override or donor unit
        if "ButtonTexture" in edits:
            # Use specified texture from another unit (may be a new unit added earlier this pass)
            specific_texture_map = textures_map.by_key(f'"Texture_Button_Unit_{edits["ButtonTexture"]}"').v
            button_texture = _texture_filename_from_entry(specific_texture_map)
        else:
            # Use donor unit's texture
            button_texture = _texture_filename_from_entry(donor_texture_map)

        # Create new texture entry
        new_entry_key = f'"Texture_Button_Unit_{unit_name}"'
        new_entry_value = (
            f"MAP [(" f"~/ComponentState/Normal, " f"TUIResourceTexture( FileName = {button_texture}" f"))]"
        )

        # Add to textures map
        textures_map.add((new_entry_key, new_entry_value))
        logger.info(f"Added button texture for {unit_name} using texture {button_texture}")
