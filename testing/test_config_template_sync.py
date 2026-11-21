"""Developer config.yaml picks up missing keys from the template."""

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from config.config_loader import ConfigLoader

_REQUIRED = """\
build_config:
  write_dev: true
  write_vip: false
  target: "gameplay"
directories:
  warno_mods: "C:/template"
  base_game: "sourcemod"
  base_vip: "sourcemod vip"
  gameplay_dev: "dev"
  ui_only_dev: "ui dev"
  gameplay_release: "release"
  ui_only_release: "ui release"
  vip_dev: "vip"
asset_config:
  target_dir: "GameData"
"""


def _write_pair(directory: Path, template: str, local: str | None) -> tuple[Path, Path]:
    template_path = directory / "config.template.YAML"
    template_path.write_text(template, encoding="utf-8", newline="\n")
    local_path = directory / "config.yaml"
    if local is not None:
        local_path.write_text(local, encoding="utf-8", newline="\n")
    return template_path, local_path


class TestConfigTemplateSync(unittest.TestCase):
    def test_missing_section_is_inserted_without_overwriting_local_values(self):
        template = _REQUIRED + """\

# copied from the template
active_map_packs:
  maps:
    - "Alpha"
  scenarios:
    - "Bravo"
  decor_sets:
    - "Env"
hide_divs:
  - "Keep"
  - "Drop"
"""
        local = """\
build_config:
  write_dev: false
  write_vip: false
  target: "gameplay"
directories:
  warno_mods: "D:/mine"
  base_game: "sourcemod"
  base_vip: "sourcemod vip"
  gameplay_dev: "dev"
  ui_only_dev: "ui dev"
  gameplay_release: "release"
  ui_only_release: "ui release"
  vip_dev: "vip"
asset_config:
  target_dir: "GameData"
hide_divs:
  - "Keep"
"""
        with TemporaryDirectory() as tmp:
            _, local_path = _write_pair(Path(tmp), template, local)
            with self.assertLogs("config.config_loader", level="WARNING") as logs:
                data = ConfigLoader(str(local_path)).load()
            self.assertTrue(any("active_map_packs" in message for message in logs.output))
            self.assertFalse(data["build_config"]["write_dev"])
            self.assertEqual(data["directories"]["warno_mods"], "D:/mine")
            self.assertEqual(list(data["active_map_packs"]["maps"]), ["Alpha"])
            self.assertEqual(list(data["hide_divs"]), ["Keep"])
            text = local_path.read_text(encoding="utf-8")
            self.assertLess(text.index("active_map_packs:"), text.index("hide_divs:"))
            self.assertIn("# copied from the template", text)

    def test_missing_nested_key_is_added(self):
        template = _REQUIRED + """\
active_map_packs:
  maps: []
"""
        local = """\
build_config:
  write_dev: false
  write_vip: false
  target: "gameplay"
directories:
  warno_mods: "D:/mine"
  base_game: "sourcemod"
  base_vip: "sourcemod vip"
  gameplay_dev: "dev"
  ui_only_dev: "ui dev"
  gameplay_release: "release"
  ui_only_release: "ui release"
asset_config:
  target_dir: "GameData"
active_map_packs:
  maps: []
"""
        with TemporaryDirectory() as tmp:
            _, local_path = _write_pair(Path(tmp), template, local)
            with self.assertLogs("config.config_loader", level="WARNING") as logs:
                data = ConfigLoader(str(local_path)).load()
            self.assertTrue(any("directories.vip_dev" in message for message in logs.output))
            self.assertEqual(data["directories"]["warno_mods"], "D:/mine")
            self.assertEqual(data["directories"]["vip_dev"], "vip")

    def test_existing_shorter_list_is_not_extended_or_warned(self):
        template = _REQUIRED + """\
active_map_packs:
  maps:
    - "Alpha"
hide_divs:
  - "Keep"
  - "Drop"
"""
        local = """\
build_config:
  write_dev: false
  write_vip: false
  target: "gameplay"
directories:
  warno_mods: "D:/mine"
  base_game: "sourcemod"
  base_vip: "sourcemod vip"
  gameplay_dev: "dev"
  ui_only_dev: "ui dev"
  gameplay_release: "release"
  ui_only_release: "ui release"
  vip_dev: "vip"
asset_config:
  target_dir: "GameData"
active_map_packs:
  maps:
    - "Alpha"
hide_divs:
  - "Keep"
"""
        with TemporaryDirectory() as tmp:
            _, local_path = _write_pair(Path(tmp), template, local)
            before = local_path.read_bytes()
            with self.assertNoLogs("config.config_loader", level="WARNING"):
                data = ConfigLoader(str(local_path)).load()
            self.assertEqual(list(data["hide_divs"]), ["Keep"])
            self.assertEqual(local_path.read_bytes(), before)

    def test_loading_the_template_does_not_rewrite_it(self):
        template = _REQUIRED + """\
active_map_packs:
  maps: []
"""
        with TemporaryDirectory() as tmp:
            template_path, _ = _write_pair(Path(tmp), template, None)
            before = template_path.read_bytes()
            data = ConfigLoader(str(template_path)).load()
            self.assertEqual(template_path.read_bytes(), before)
            self.assertIn("active_map_packs", data)

    def test_second_load_does_not_write_or_warn(self):
        template = _REQUIRED + """\
active_map_packs:
  maps:
    - "Alpha"
hide_divs:
  - "Keep"
"""
        local = """\
build_config:
  write_dev: false
  write_vip: false
  target: "gameplay"
directories:
  warno_mods: "D:/mine"
  base_game: "sourcemod"
  base_vip: "sourcemod vip"
  gameplay_dev: "dev"
  ui_only_dev: "ui dev"
  gameplay_release: "release"
  ui_only_release: "ui release"
  vip_dev: "vip"
asset_config:
  target_dir: "GameData"
hide_divs:
  - "Keep"
"""
        with TemporaryDirectory() as tmp:
            _, local_path = _write_pair(Path(tmp), template, local)
            ConfigLoader(str(local_path)).load()
            after_first = local_path.read_bytes()
            with self.assertNoLogs("config.config_loader", level="WARNING"):
                ConfigLoader(str(local_path)).load()
            self.assertEqual(local_path.read_bytes(), after_first)

    def test_template_lists_the_release_mod_packs(self):
        data = ConfigLoader("config/config.template.YAML").load()
        self.assertFalse(data["build_config"]["copy_maps"])
        packs = data["active_map_packs"]
        self.assertEqual(
            list(packs["maps"]),
            ["_3x3_HighwayToSeoul", "NuclearWinter", "Potato_field", "WA_3x3_Punchvalley"],
        )
        self.assertEqual(len(list(packs["scenarios"])), 32)
        self.assertEqual(list(packs["decor_sets"]), ["Environmentals", "EnvModels"])
        self.assertNotIn("Highway_to_Seoul", list(packs["maps"]))
        self.assertNotIn("_4x4_Alsfeld", list(packs["maps"]))
        text = Path("config/config.template.YAML").read_text(encoding="utf-8")
        self.assertLess(text.index("active_map_packs:"), text.index("hide_divs:"))
        self.assertGreater(text.index("active_map_packs:"), text.index("config_ini_base_path:"))


if __name__ == "__main__":
    unittest.main()
