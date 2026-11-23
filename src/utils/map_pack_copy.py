"""Copy active map, scenario, and decor packs into the mod Saved Games folder."""

import shutil
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

from src.utils.config_utils import get_mod_name, get_saved_games_warno_root
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Suffixes are the filename tail before ``.dat``. An empty string is the bare ``{stem}.dat``.
# Map files are read from Saved Games Datapacks/Maps and written to mod/Maps.
_MAP_FILE_SUFFIXES = ("", "_Shooting", "_Stickers", "_Assets", "_Definition", "_Details")
_SCENARIO_SUFFIXES = ("_Assets", "_Definition", "_Details", "_GameData", "_ScenariosData")
_DECOR_SUFFIXES = ("_Assets", "_Definition", "_Editor")


def copy_active_map_packs(config: Dict) -> None:
    """Copy allowlisted packs from the Saved Games working folders into the mod.

    Runs when ``build_config.copy_maps`` is true, on gameplay builds only. A missing
    or false ``copy_maps`` skips the copy. A file is copied when the destination is missing, the
    size differs, or the source is newer. Files already in the mod Maps,
    Scenarios, or DecorsSets folders that are not part of the allowlist are removed.
    A missing or invalid list is left untouched.
    """
    build = config.get("build_config", {})
    if not build.get("copy_maps"):
        return
    if build.get("target") != "gameplay":
        return

    packs = config.get("active_map_packs")
    if not isinstance(packs, dict):
        logger.warning("active_map_packs is missing from config; skipping map pack copy")
        return

    root = get_saved_games_warno_root(config)
    mod_root = root / "mod" / get_mod_name(config)
    map_stems = _stem_list(packs, "maps")
    scenario_stems = _stem_list(packs, "scenarios")
    decor_stems = _stem_list(packs, "decor_sets")

    map_dir = root / "Datapacks" / "Maps"
    jobs = (
        (map_stems, map_dir, mod_root / "Maps", _MAP_FILE_SUFFIXES),
        (scenario_stems, root / "Datapacks" / "Scenarios", mod_root / "Scenarios", _SCENARIO_SUFFIXES),
        (decor_stems, root / "Datapacks" / "DecorsSets", mod_root / "DecorsSets", _DECOR_SUFFIXES),
    )

    copied = unchanged = missing = removed = 0
    for stems, source_dir, dest_dir, suffixes in jobs:
        if stems is None:
            continue
        file_copied, file_unchanged, file_missing = _copy_stems(stems, source_dir, dest_dir, suffixes)
        copied += file_copied
        unchanged += file_unchanged
        missing += file_missing
        removed += _remove_unlisted(dest_dir, _expected_names(stems, suffixes))

    logger.info(
        "Map packs: copied %d, unchanged %d, missing %d, removed %d",
        copied,
        unchanged,
        missing,
        removed,
    )


def _stem_list(packs: Dict, key: str) -> List[str] | None:
    """Return stems, or None when the list is missing or not a list.

    None skips both the copy and the removal for that folder. An empty list is
    valid and clears the destination folder.
    """
    if key not in packs:
        logger.warning("active_map_packs.%s is missing; skipping those files", key)
        return None
    value = packs[key]
    if isinstance(value, str) or not isinstance(value, (list, tuple)):
        logger.warning("active_map_packs.%s must be a list of stems; skipping", key)
        return None
    stems: List[str] = []
    for item in value:
        if isinstance(item, str) and item:
            stems.append(item)
        else:
            logger.warning("Ignoring active_map_packs.%s entry that is not a name: %r", key, item)
    return stems


def _copy_stems(
    stems: Sequence[str],
    source_dir: Path,
    dest_dir: Path,
    suffixes: Sequence[str],
) -> Tuple[int, int, int]:
    copied = unchanged = missing = 0
    for stem in stems:
        for suffix in suffixes:
            name = f"{stem}{suffix}.dat"
            source = source_dir / name
            dest = dest_dir / name
            if not source.is_file():
                logger.warning("Map pack file not found: %s", source)
                missing += 1
                continue
            if dest.is_file() and not _source_should_replace(source, dest):
                unchanged += 1
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(source, dest)
            except OSError as exc:
                logger.error("Failed to copy %s: %s", source, exc)
                continue
            copied += 1
    return copied, unchanged, missing


def _expected_names(stems: Sequence[str], suffixes: Sequence[str]) -> set:
    return {f"{stem}{suffix}.dat" for stem in stems for suffix in suffixes}


def _remove_unlisted(dest_dir: Path, expected: set) -> int:
    if not dest_dir.is_dir():
        return 0
    removed = 0
    for path in dest_dir.iterdir():
        if not path.is_file() or path.name in expected:
            continue
        try:
            path.unlink()
        except OSError as exc:
            logger.error("Failed to remove %s: %s", path, exc)
            continue
        logger.info("Removed %s", path.name)
        removed += 1
    return removed


def _source_should_replace(source: Path, dest: Path) -> bool:
    src_stat = source.stat()
    dst_stat = dest.stat()
    if src_stat.st_size != dst_stat.st_size:
        return True
    return src_stat.st_mtime > dst_stat.st_mtime
