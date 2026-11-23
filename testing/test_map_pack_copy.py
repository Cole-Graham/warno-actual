"""Copy allowlisted map packs from Saved Games into the mod folder."""

import os
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from src.utils.config_utils import get_config_ini_path, get_saved_games_warno_root
from src.utils.map_pack_copy import copy_active_map_packs

_MAP_SUFFIXES = ("", "_Shooting", "_Stickers", "_Assets", "_Definition", "_Details")
_SCENARIO_SUFFIXES = ("_Assets", "_Definition", "_Details", "_GameData", "_ScenariosData")
_DECOR_SUFFIXES = ("_Assets", "_Definition", "_Editor")


def _config(target="gameplay", **directory_overrides):
    directories = {
        "warno_mods": "C:/WARNO/Mods",
        "base_game": "sourcemod",
        "base_vip": "sourcemod vip",
        "gameplay_dev": "WARNO ACTUAL dev",
        "gameplay_release": "WARNO ACTUAL",
        "ui_only_dev": "UI dev",
        "ui_only_release": "UI release",
        "vip_dev": "WARNO ACTUAL vip",
        "config_ini_base_path": "default",
    }
    directories.update(directory_overrides)
    return {
        "build_config": {
            "write_dev": False,
            "write_vip": False,
            "target": target,
            "copy_maps": True,
        },
        "directories": directories,
        "active_map_packs": {
            "maps": ["Listed"],
            "scenarios": ["ScenarioOne"],
            "decor_sets": ["Environmentals"],
        },
    }


def _write(path: Path, body: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)


def _touch_pack(root: Path, stem: str, body: bytes = b"v1") -> None:
    for suffix in _MAP_SUFFIXES:
        _write(root / "Datapacks" / "Maps" / f"{stem}{suffix}.dat", body)


class TestSavedGamesPaths(unittest.TestCase):
    def test_default_root_and_config_ini(self):
        home = Path("C:/Users/dev")
        with patch("src.utils.config_utils.Path.home", return_value=home):
            config = _config()
            root = get_saved_games_warno_root(config)
            self.assertEqual(root, home / "Saved Games" / "EugenSystems" / "WARNO")
            self.assertEqual(
                get_config_ini_path(config),
                root / "mod" / "WARNO ACTUAL" / "Config.ini",
            )

    def test_override_root_is_parent_of_mod_folder(self):
        override = Path("D:/Custom/WARNO/mod")
        config = _config(config_ini_base_path=str(override))
        root = get_saved_games_warno_root(config)
        self.assertEqual(root, override.parent)
        self.assertEqual(
            get_config_ini_path(config),
            root / "mod" / "WARNO ACTUAL" / "Config.ini",
        )


class TestCopyActiveMapPacks(unittest.TestCase):
    def test_copies_listed_suffixes_only(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _touch_pack(root, "Listed", b"listed")
            _write(root / "Datapacks" / "Maps" / "Highway_to_Seoul.dat", b"wip")
            _write(root / "Datapacks" / "Maps" / "Highway_to_Seoul_Assets.dat", b"wip")
            for suffix in _SCENARIO_SUFFIXES:
                _write(root / "Datapacks" / "Scenarios" / f"ScenarioOne{suffix}.dat", b"scenario")
            for suffix in _DECOR_SUFFIXES:
                _write(root / "Datapacks" / "DecorsSets" / f"Environmentals{suffix}.dat", b"decor")

            config = _config(config_ini_base_path=str(root / "mod"))
            mod = root / "mod" / "WARNO ACTUAL"
            _write(mod / "Maps" / "Highway_to_Seoul_Assets.dat", b"old")
            _write(mod / "Maps" / "notes.txt", b"old")
            _write(mod / "Scenarios" / "Retired_Assets.dat", b"old")
            _write(mod / "DecorsSets" / "Retired_Assets.dat", b"old")
            copy_active_map_packs(config)

            map_names = sorted(path.name for path in (mod / "Maps").iterdir())
            scenario_names = sorted(path.name for path in (mod / "Scenarios").iterdir())
            decor_names = sorted(path.name for path in (mod / "DecorsSets").iterdir())
            self.assertEqual(map_names, sorted(f"Listed{suffix}.dat" for suffix in _MAP_SUFFIXES))
            self.assertEqual(scenario_names, [f"ScenarioOne{suffix}.dat" for suffix in _SCENARIO_SUFFIXES])
            self.assertEqual(decor_names, [f"Environmentals{suffix}.dat" for suffix in _DECOR_SUFFIXES])
            self.assertEqual((mod / "Maps" / "Listed.dat").read_bytes(), b"listed")
            self.assertEqual((mod / "Maps" / "Listed_Assets.dat").read_bytes(), b"listed")
            self.assertFalse((mod / "DatasMap").exists())
            self.assertFalse((mod / "Datapacks" / "Maps").exists())

    def test_skips_unchanged_and_replaces_newer_or_different_size(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _touch_pack(root, "Listed", b"same")
            _touch_pack(root, "Sized", b"src-longer")
            config = _config(config_ini_base_path=str(root / "mod"))
            config["active_map_packs"]["maps"] = ["Listed", "Sized"]
            config["active_map_packs"]["scenarios"] = []
            config["active_map_packs"]["decor_sets"] = []

            mod = root / "mod" / "WARNO ACTUAL"
            unchanged = mod / "Maps" / "Listed_Assets.dat"
            _write(unchanged, b"same")
            replaced = mod / "Maps" / "Listed.dat"
            _write(replaced, b"old")
            sized = mod / "Maps" / "Sized_Assets.dat"
            _write(sized, b"short")

            os.utime(root / "Datapacks" / "Maps" / "Listed_Assets.dat", (1000, 1000))
            os.utime(unchanged, (2000, 2000))
            os.utime(replaced, (1000, 1000))
            os.utime(root / "Datapacks" / "Maps" / "Listed.dat", (3000, 3000))
            os.utime(root / "Datapacks" / "Maps" / "Sized_Assets.dat", (500, 500))
            os.utime(sized, (4000, 4000))

            copy_active_map_packs(config)

            self.assertEqual(unchanged.read_bytes(), b"same")
            self.assertEqual(unchanged.stat().st_mtime, 2000)
            self.assertEqual(replaced.read_bytes(), b"same")
            self.assertEqual(sized.read_bytes(), b"src-longer")

    def test_missing_source_warns_and_does_not_raise(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = _config(config_ini_base_path=str(root / "mod"))
            config["active_map_packs"]["maps"] = ["MissingMap"]
            config["active_map_packs"]["scenarios"] = []
            config["active_map_packs"]["decor_sets"] = []
            mod = root / "mod" / "WARNO ACTUAL"
            kept = mod / "Maps" / "MissingMap_Assets.dat"
            _write(kept, b"keep")
            _write(mod / "Maps" / "Other_Assets.dat", b"drop")
            with self.assertLogs("src.utils.map_pack_copy", level="WARNING") as logs:
                copy_active_map_packs(config)
            self.assertTrue(any("MissingMap_Assets.dat" in message for message in logs.output))
            self.assertEqual(kept.read_bytes(), b"keep")
            self.assertFalse((mod / "Maps" / "Other_Assets.dat").exists())

    def test_ui_only_copies_nothing(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _touch_pack(root, "Listed", b"listed")
            extra = root / "mod" / "WARNO ACTUAL" / "Maps" / "extra.dat"
            _write(extra, b"stay")
            config = _config(target="ui_only", config_ini_base_path=str(root / "mod"))
            copy_active_map_packs(config)
            self.assertEqual(extra.read_bytes(), b"stay")
            self.assertFalse((root / "mod" / "UI release").exists())

    def test_invalid_list_does_not_remove_destination_files(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            config = _config(config_ini_base_path=str(root / "mod"))
            config["active_map_packs"]["maps"] = "Listed"
            kept = root / "mod" / "WARNO ACTUAL" / "Maps" / "Highway_to_Seoul_Assets.dat"
            _write(kept, b"stay")
            copy_active_map_packs(config)
            self.assertEqual(kept.read_bytes(), b"stay")

    def test_copy_maps_off_leaves_files_alone(self):
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            _touch_pack(root, "Listed", b"listed")
            config = _config(config_ini_base_path=str(root / "mod"))
            config["build_config"]["copy_maps"] = False
            extra = root / "mod" / "WARNO ACTUAL" / "Maps" / "extra.dat"
            _write(extra, b"stay")
            copy_active_map_packs(config)
            self.assertEqual(extra.read_bytes(), b"stay")
            self.assertFalse((root / "mod" / "WARNO ACTUAL" / "Maps" / "Listed.dat").exists())


if __name__ == "__main__":
    unittest.main()
