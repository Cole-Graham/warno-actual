"""Functions for editing WeaponTextures.ndf"""

from pathlib import Path
from typing import Any, Set

from src.constants.weapons import ammunitions
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Repo: assets/gameplaymod/2d/.../panel_info — same layout as asset copy (see asset_utils).
_PANEL_INFO_DIR = (
    Path(__file__).resolve().parents[5]
    / "assets"
    / "gameplaymod"
    / "2d"
    / "interface"
    / "common"
    / "unitsicons"
    / "armes"
    / "panel_info"
)


def _add_texture_resource_and_map(
    source_path: Any,
    texture_bank: Any,
    insert_index: int,
    stem: str,
) -> None:
    texture_file = (
        f'"GameData:/Assets/2D/Interface/Common/UnitsIcons/Armes/Panel_Info/{stem}.png"'
    )
    new_entry = (
        f"Texture_Interface_Weapon_{stem} is TUIResourceTexture_Common"
        f"("
        f"    FileName = {texture_file}"
        f")"
    )
    source_path.insert(insert_index, new_entry)

    new_map_entry = (
        f'("Texture_Interface_Weapon_{stem}", MAP ['
        f"    (~/ComponentState/Normal, ~/Texture_Interface_Weapon_{stem})"
        f"]),"
    )
    texture_bank.v.by_m("Textures").v.add(new_map_entry)  # noqa
    logger.debug(f"Added texture and map entry for {stem}")


def edit_gen_ui_weapontextures(source_path: Any) -> None:
    """GameData/Generated/UserInterface/Textures/WeaponTextures.ndf"""
    logger.info("Editing weapon textures")

    # Find texture bank
    append_index, texture_bank = 0, ""
    for i, row in enumerate(source_path, start=0):
        if row.namespace == "WeaponAdditionalTextureBank":
            append_index = i
            texture_bank = row
            break

    if not texture_bank:
        logger.error("WeaponAdditionalTextureBank not found in WeaponTextures.ndf")
        return

    # Case-insensitive dedupe: same stem must not be registered twice (cooker / bank map).
    registered_fold: Set[str] = set()

    def try_register(stem: str) -> bool:
        k = stem.casefold()
        if k in registered_fold:
            return False
        registered_fold.add(k)
        return True

    # NewTexture value is the stem used by ammunition.py for InterfaceWeaponTexture
    # (Texture_Interface_Weapon_<NewTexture>), not the tuple weapon id — see
    # _apply_weapon_edits / _apply_missile_edits. FileName must match that stem + .png.
    for (_weapon, _category, _donor, _is_new), data in ammunitions.items():
        if data is None:
            continue

        for data_root, data_value in data.items():
            if data_root != "NewTexture":
                continue
            stem = str(data_value)
            if not try_register(stem):
                continue
            _add_texture_resource_and_map(
                source_path, texture_bank, append_index, stem,
            )

    # ATGM / panel_info icons: stems match PNG basename (e.g. dragon_wa.png)
    if _PANEL_INFO_DIR.is_dir():
        for png_path in sorted(_PANEL_INFO_DIR.glob("*.png")):
            stem = png_path.stem
            if not try_register(stem):
                continue
            _add_texture_resource_and_map(
                source_path, texture_bank, append_index, stem,
            )
            logger.debug(f"Added panel_info texture and map entry for {stem}")
    else:
        logger.warning(f"panel_info directory not found: {_PANEL_INFO_DIR}")
