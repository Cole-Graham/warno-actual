"""Repair mod folder layout after ndf mod sync from base_game."""

import shutil
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple

from src.utils.config_utils import get_mod_dst_path, get_mod_name, get_mod_src_path
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

RESOURCE_PACK_TYPES = ("MeshPack", "TextureProxy")


def ensure_mod_folder_layout(config: Dict) -> None:
    """Fix Localisation and ResourcePacks paths to use mod_name instead of base_game."""
    ensure_localisation_layout(config)
    ensure_resource_packs_layout(config)


def ensure_localisation_layout(config: Dict) -> None:
    """Ensure LocalisationDicos.ndf and CSV directory use mod_name, not base_game."""
    mod_name = get_mod_name(config)
    base_game = config['directories']['base_game']
    mod_dst_path = get_mod_dst_path(config)
    localisation_dir = mod_dst_path / "GameData" / "Localisation"
    base_game_subdir = localisation_dir / base_game
    mod_name_subdir = localisation_dir / mod_name

    logger.info(f"Checking Localisation layout (mod_name: {mod_name}, base_game: {base_game})")

    mod_name_subdir.mkdir(parents=True, exist_ok=True)
    _relocate_mod_named_subdir(localisation_dir, base_game, mod_name, "Localisation")

    wrong_ndf_path = base_game_subdir / "LocalisationDicos.ndf"
    correct_ndf_path = mod_name_subdir / "LocalisationDicos.ndf"
    source_ndf_path = _find_source_ndf(
        get_mod_src_path(config),
        "Localisation",
        base_game,
        "LocalisationDicos.ndf",
    )

    if not _ensure_descriptor_ndf(
        wrong_ndf_path,
        correct_ndf_path,
        source_ndf_path,
        "LocalisationDicos.ndf",
    ):
        return

    _rewrite_ndf_path_prefixes(
        correct_ndf_path,
        [(f"Localisation/{base_game}/", f"Localisation/{mod_name}/")],
        mod_name,
        base_game,
        "LocalisationDicos.ndf",
    )
    _remove_stale_subdir(base_game_subdir, mod_name_subdir, "LocalisationDicos.ndf")


def ensure_resource_packs_layout(config: Dict) -> None:
    """Ensure ResourcePacks.ndf and pack directories use mod_name, not base_game."""
    mod_name = get_mod_name(config)
    base_game = config['directories']['base_game']
    mod_dst_path = get_mod_dst_path(config)
    resource_packs_dir = mod_dst_path / "GameData" / "ResourcePacks"
    base_game_subdir = resource_packs_dir / base_game
    mod_name_subdir = resource_packs_dir / mod_name

    logger.info(f"Checking ResourcePacks layout (mod_name: {mod_name}, base_game: {base_game})")

    mod_name_subdir.mkdir(parents=True, exist_ok=True)
    _relocate_mod_named_subdir(resource_packs_dir, base_game, mod_name, "ResourcePacks")

    for pack_type in RESOURCE_PACK_TYPES:
        _relocate_mod_named_subdir(
            resource_packs_dir / pack_type,
            base_game,
            mod_name,
            f"ResourcePacks/{pack_type}",
        )

    wrong_ndf_path = base_game_subdir / "ResourcePacks.ndf"
    correct_ndf_path = mod_name_subdir / "ResourcePacks.ndf"
    source_ndf_path = _find_source_ndf(
        get_mod_src_path(config),
        "ResourcePacks",
        base_game,
        "ResourcePacks.ndf",
    )

    if not _ensure_descriptor_ndf(
        wrong_ndf_path,
        correct_ndf_path,
        source_ndf_path,
        "ResourcePacks.ndf",
    ):
        return

    replacements = [
        (f"MeshPack/{base_game}/", f"MeshPack/{mod_name}/"),
        (f"TextureProxy/{base_game}/", f"TextureProxy/{mod_name}/"),
        (f"/{base_game}/", f"/{mod_name}/"),
    ]
    _rewrite_ndf_path_prefixes(
        correct_ndf_path,
        replacements,
        mod_name,
        base_game,
        "ResourcePacks.ndf",
    )
    _remove_stale_subdir(base_game_subdir, mod_name_subdir, "ResourcePacks.ndf")

    for pack_type in RESOURCE_PACK_TYPES:
        stale_pack_dir = resource_packs_dir / pack_type / base_game
        correct_pack_dir = resource_packs_dir / pack_type / mod_name
        if stale_pack_dir.exists() and stale_pack_dir != correct_pack_dir:
            _remove_stale_subdir(stale_pack_dir, correct_pack_dir)


def _find_source_ndf(
    mod_src_path: Path,
    section: str,
    base_game: str,
    filename: str,
) -> Optional[Path]:
    expected = mod_src_path / "GameData" / section / base_game / filename
    if expected.exists():
        return expected
    for found_file in mod_src_path.rglob(filename):
        if section in found_file.parts:
            logger.debug(f"  Found {filename} at: {found_file}")
            return found_file
    return None


def _ensure_descriptor_ndf(
    wrong_path: Path,
    correct_path: Path,
    source_path: Optional[Path],
    label: str,
) -> bool:
    correct_path.parent.mkdir(parents=True, exist_ok=True)

    logger.debug(f"  Correct path: {correct_path}")
    logger.debug(f"  Wrong path: {wrong_path}")
    logger.debug(f"  Source file found: {source_path}")

    if correct_path.exists():
        return True

    if wrong_path.exists():
        try:
            logger.info(f"Moving {label} from wrong location to correct location")
            logger.info(f"  From: {wrong_path}")
            logger.info(f"  To: {correct_path}")
            shutil.move(str(wrong_path), str(correct_path))
            logger.info(f"Successfully moved {label} to correct location")
            return True
        except Exception as e:
            logger.error(f"Failed to move {label}: {e}")
            return False

    if source_path and source_path.exists():
        try:
            logger.info(f"Copying {label} from base_game mod")
            logger.info(f"  From: {source_path}")
            logger.info(f"  To: {correct_path}")
            shutil.copy2(str(source_path), str(correct_path))
            logger.info(f"Successfully copied {label} from base_game mod")
            return True
        except Exception as e:
            logger.error(f"Failed to copy {label} from base_game mod: {e}")
            return False

    logger.error(f"{label} not found in base_game mod; cannot copy file")
    return False


def _rewrite_ndf_path_prefixes(
    ndf_path: Path,
    replacements: Iterable[Tuple[str, str]],
    mod_name: str,
    base_game: str,
    label: str,
) -> None:
    if not ndf_path.exists():
        return

    try:
        logger.info(f"Fixing paths in {label} at {ndf_path}")
        with open(ndf_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        updated_content = content
        updated_count = 0
        for old, new in replacements:
            count = updated_content.count(old)
            if count:
                updated_content = updated_content.replace(old, new)
                updated_count += count

        if updated_content != original_content:
            with open(ndf_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            logger.info(f"Updated {updated_count} path(s) in {label}")
        elif f"/{mod_name}/" in content:
            logger.debug(f"Paths in {label} already use mod_name '{mod_name}'")
        else:
            logger.warning(f"Paths in {label} don't contain expected mod name '{mod_name}'")

        if f"/{base_game}/" in updated_content:
            logger.warning(f"{label} still contains base_game path segment '{base_game}' after rewrite")
    except Exception as e:
        logger.error(f"Failed to fix {label}: {e}")


def _relocate_mod_named_subdir(
    parent: Path,
    base_game: str,
    mod_name: str,
    label: str,
) -> None:
    wrong_dir = parent / base_game
    correct_dir = parent / mod_name

    if not wrong_dir.exists() or wrong_dir == correct_dir:
        return

    correct_dir.mkdir(parents=True, exist_ok=True)

    try:
        logger.info(f"Merging {label}/{base_game} into {label}/{mod_name}")
        for item in wrong_dir.iterdir():
            target = correct_dir / item.name
            if target.exists():
                logger.warning(f"Skipping {item.name}: already exists at {target}")
                continue
            shutil.move(str(item), str(target))
            logger.debug(f"  Moved {item.name} to {target}")
    except Exception as e:
        logger.error(f"Failed to merge files in {label}: {e}")


def _remove_stale_subdir(
    stale_dir: Path,
    correct_dir: Path,
    blocking_filename: Optional[str] = None,
) -> None:
    if not stale_dir.exists() or stale_dir == correct_dir:
        return

    if blocking_filename:
        blocking_file = stale_dir / blocking_filename
        if blocking_file.exists():
            logger.warning(
                f"Cannot remove {stale_dir.name} subdirectory: "
                f"{blocking_filename} still exists there",
            )
            return

    try:
        if any(stale_dir.iterdir()):
            logger.warning(f"Cannot remove {stale_dir}: directory is not empty")
            return
        logger.info(f"Removing incorrect {stale_dir.name} subdirectory: {stale_dir}")
        shutil.rmtree(stale_dir)
        logger.info(f"Successfully removed {stale_dir.name} subdirectory")
    except Exception as e:
        logger.error(f"Failed to remove {stale_dir}: {e}")
