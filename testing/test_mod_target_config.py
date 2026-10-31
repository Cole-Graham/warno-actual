"""Destination and source mod selection from write_dev / write_vip."""

import unittest
from pathlib import Path

from config.config_loader import ConfigLoader
from src.utils.config_utils import get_base_mod_name, get_mod_name, get_mod_src_path, is_dev_build


def _config(write_dev=True, write_vip=False, target="gameplay"):
    return {
        "build_config": {
            "write_dev": write_dev,
            "write_vip": write_vip,
            "target": target,
        },
        "directories": {
            "warno_mods": "C:/WARNO/Mods",
            "base_game": "sourcemod",
            "base_vip": "sourcemod vip",
            "gameplay_dev": "WARNO ACTUAL dev",
            "gameplay_release": "WARNO ACTUAL",
            "ui_only_dev": "UI dev",
            "ui_only_release": "UI release",
            "vip_dev": "WARNO ACTUAL vip",
        },
    }


class TestModTargetConfig(unittest.TestCase):
    def test_template_has_vip_keys(self):
        data = ConfigLoader("config/config.template.YAML").load()
        self.assertIn("write_vip", data["build_config"])
        self.assertEqual(data["directories"]["base_vip"], "sourcemod vip")
        self.assertEqual(data["directories"]["vip_dev"], "WARNO ACTUAL vip")

    def test_release_gameplay_uses_release_mod(self):
        config = _config(write_dev=False, write_vip=False)
        self.assertFalse(is_dev_build(config))
        self.assertEqual(get_base_mod_name(config), "sourcemod")
        self.assertEqual(get_mod_name(config), "WARNO ACTUAL")
        self.assertEqual(get_mod_src_path(config), Path("C:/WARNO/Mods/sourcemod"))

    def test_dev_gameplay_uses_dev_mod(self):
        config = _config(write_dev=True, write_vip=False)
        self.assertTrue(is_dev_build(config))
        self.assertEqual(get_mod_name(config), "WARNO ACTUAL dev")

    def test_write_vip_ignores_write_dev_and_uses_vip_mods(self):
        config = _config(write_dev=False, write_vip=True, target="gameplay")
        self.assertTrue(is_dev_build(config))
        self.assertEqual(get_base_mod_name(config), "sourcemod vip")
        self.assertEqual(get_mod_name(config), "WARNO ACTUAL vip")
        self.assertEqual(get_mod_src_path(config), Path("C:/WARNO/Mods/sourcemod vip"))

    def test_write_vip_ui_uses_ui_dev_mod(self):
        config = _config(write_dev=False, write_vip=True, target="ui_only")
        self.assertEqual(get_base_mod_name(config), "sourcemod vip")
        self.assertEqual(get_mod_name(config), "UI dev")

    def test_release_ui_uses_ui_release_mod(self):
        config = _config(write_dev=False, write_vip=False, target="ui_only")
        self.assertEqual(get_mod_name(config), "UI release")


if __name__ == "__main__":
    unittest.main()
