"""Tests for ``replace_schema.normalize_replace``."""

from __future__ import annotations

import unittest

from src.constants.unit_edits.replace_schema import ReplaceSpec, normalize_replace


class NormalizeReplaceTests(unittest.TestCase):
    def test_dict_list_value_duplicate_mount_order(self) -> None:
        block = {
            "RocketInf_RPG7VR_64mm": [
                {
                    "new_weapon": "SAW_RPK_74_5_56mm",
                    "swap_fire_effect": True,
                    "depiction_baked_in": False,
                },
                {
                    "new_weapon": "RocketInf_RPG29_105mm",
                    "swap_fire_effect": True,
                    "depiction_baked_in": False,
                },
            ],
        }
        specs = normalize_replace(block)
        self.assertEqual(len(specs), 2)
        self.assertIsInstance(specs[0], ReplaceSpec)
        self.assertIsInstance(specs[1], ReplaceSpec)
        self.assertEqual(specs[0].old_weapon, "RocketInf_RPG7VR_64mm")
        self.assertEqual(specs[0].new_weapon, "SAW_RPK_74_5_56mm")
        self.assertEqual(specs[1].old_weapon, "RocketInf_RPG7VR_64mm")
        self.assertEqual(specs[1].new_weapon, "RocketInf_RPG29_105mm")

    def test_dict_single_mapping_unchanged(self) -> None:
        specs = normalize_replace({
            "A": {
                "new_weapon": "B",
                "swap_fire_effect": False,
                "depiction_baked_in": True,
            },
        })
        self.assertEqual(len(specs), 1)
        self.assertEqual(specs[0].old_weapon, "A")
        self.assertEqual(specs[0].new_weapon, "B")
        self.assertFalse(specs[0].swap_fire_effect)
        self.assertTrue(specs[0].depiction_baked_in)

    def test_salvolength_stripped_from_default_fire_effects(self) -> None:
        specs = normalize_replace({
            "RocketInf_RPG27_105mm": {
                "new_weapon": "RocketInf_RPG7VL_salvolength6",
                "swap_fire_effect": True,
                "depiction_baked_in": False,
            },
        })
        self.assertEqual(len(specs), 1)
        self.assertEqual(specs[0].new_weapon, "RocketInf_RPG7VL_salvolength6")
        self.assertEqual(specs[0].old_fire_effect, "RocketInf_RPG27_105mm")
        self.assertEqual(specs[0].new_fire_effect, "RocketInf_RPG7VL")

    def test_infmagazine_stripped_from_default_fire_effects(self) -> None:
        specs = normalize_replace({
            "MANPAD_igla": {
                "new_weapon": "MANPAD_igla_infmagazine4",
                "swap_fire_effect": True,
                "depiction_baked_in": False,
            },
        })
        self.assertEqual(len(specs), 1)
        self.assertEqual(specs[0].new_fire_effect, "MANPAD_igla")

    def test_old_new_effect_magazine_suffixes_stripped(self) -> None:
        specs = normalize_replace({
            "RocketInf_PzF_44": {
                "new_weapon": "RocketInf_PzF_3_salvolength6",
                "swap_fire_effect": True,
                "depiction_baked_in": False,
                "old_new_effect": (
                    "RocketInf_PzF_44_salvolength4",
                    "RocketInf_PzF_3_salvolength6",
                ),
            },
        })
        self.assertEqual(len(specs), 1)
        self.assertEqual(specs[0].old_fire_effect, "RocketInf_PzF_44")
        self.assertEqual(specs[0].new_fire_effect, "RocketInf_PzF_3")


if __name__ == "__main__":
    unittest.main()
