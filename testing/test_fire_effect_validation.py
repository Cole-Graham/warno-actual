"""Tests for fire-effect stem stripping and existence validation."""

from __future__ import annotations

import unittest
from typing import Any, Dict
from unittest.mock import patch

from src.constants.unit_edits.replace_schema import (
    fire_effect_stem_from_ammo,
    normalize_replace,
)
from src.data.fire_effect_validation import (
    collect_fire_effect_stems_from_replace,
    ensure_fire_effect_exists,
    fire_effect_exists,
    is_vehicle_style_weapon_team,
    unit_skips_infantry_fire_registry,
    validate_fire_effect_constants,
)


def _game_db_with_effects(*stems: str) -> Dict[str, Any]:
    return {
        "depiction_data": {
            "all_fire_effects": {stem: f"FireEffect_{stem}" for stem in stems},
        },
    }


class FireEffectStemTests(unittest.TestCase):
    def test_strip_salvolength(self) -> None:
        self.assertEqual(
            fire_effect_stem_from_ammo("RocketInf_RPG7VL_salvolength6"),
            "RocketInf_RPG7VL",
        )

    def test_strip_infmagazine(self) -> None:
        self.assertEqual(
            fire_effect_stem_from_ammo("MANPAD_igla_infmagazine4"),
            "MANPAD_igla",
        )

    def test_does_not_strip_x_suffix(self) -> None:
        self.assertEqual(
            fire_effect_stem_from_ammo("GatlingAir_Gsh_30_2_30mm_x2"),
            "GatlingAir_Gsh_30_2_30mm_x2",
        )


class FireEffectExistsTests(unittest.TestCase):
    def test_known_stem_accepted(self) -> None:
        game_db = _game_db_with_effects("RocketInf_RPG7VL")
        self.assertTrue(fire_effect_exists("RocketInf_RPG7VL", game_db))

    def test_salvolength_stem_rejected_via_ensure(self) -> None:
        game_db = _game_db_with_effects("RocketInf_RPG7VL")
        self.assertFalse(
            ensure_fire_effect_exists(
                "RocketInf_RPG7VL_salvolength6",
                game_db=game_db,
                context="test",
            ),
        )

    def test_bare_stem_after_strip_exists(self) -> None:
        game_db = _game_db_with_effects("RocketInf_RPG7VL")
        self.assertTrue(
            fire_effect_exists("RocketInf_RPG7VL_salvolength6", game_db),
        )

    def test_unknown_stem_rejected(self) -> None:
        game_db = _game_db_with_effects("RocketInf_RPG7VL")
        self.assertFalse(
            ensure_fire_effect_exists(
                "RocketInf_DoesNotExist",
                game_db=game_db,
                context="test",
            ),
        )

    def test_vehicle_channel_skipped(self) -> None:
        game_db = _game_db_with_effects()
        self.assertTrue(
            ensure_fire_effect_exists("weapon_effet_tag3", game_db=game_db),
        )

    def test_vehicle_channel_with_quotes_skipped(self) -> None:
        game_db = _game_db_with_effects()
        self.assertTrue(
            ensure_fire_effect_exists("'weapon_effet_tag2'", game_db=game_db),
        )

    def test_air_suffix_skipped(self) -> None:
        game_db = _game_db_with_effects()
        self.assertTrue(
            ensure_fire_effect_exists(
                "Gatling_M61_Vulcan_20mm_late_AIR",
                game_db=game_db,
            ),
        )


class SkipInfantryRegistryTests(unittest.TestCase):
    def test_hmg_mmg_team_prefixes(self) -> None:
        self.assertTrue(is_vehicle_style_weapon_team("HMGteam_NSV_para_POL"))
        self.assertTrue(is_vehicle_style_weapon_team("MMGteam_MG3_RFA"))
        self.assertFalse(is_vehicle_style_weapon_team("ATteam_Milan_1_UK"))
        self.assertFalse(is_vehicle_style_weapon_team("RCL_L6_Wombat_UK"))
        self.assertFalse(is_vehicle_style_weapon_team("Rifles_US"))
        self.assertFalse(is_vehicle_style_weapon_team("MANPAD_Stinger_C_US"))

    def test_infanterie_at_tag_skips_registry(self) -> None:
        self.assertTrue(
            unit_skips_infantry_fire_registry(
                "RCL_L6_Wombat_UK",
                {},
                {"unit_data": {"RCL_L6_Wombat_UK": {"tags": ["Infanterie_AT"]}}},
            ),
        )
        self.assertTrue(
            unit_skips_infantry_fire_registry(
                "ATteam_Milan_1_UK",
                {
                    "TagSet": {
                        "overwrite_all": ["Infanterie", "Infanterie_AT"],
                    },
                },
            ),
        )
        self.assertFalse(
            unit_skips_infantry_fire_registry(
                "Rifles_US",
                {"TagSet": {"overwrite_all": ["Infanterie"]}},
            ),
        )

    def test_heavy_equipment_and_aerial_flags(self) -> None:
        self.assertTrue(
            unit_skips_infantry_fire_registry(
                "Some_Unit",
                {"is_heavy_equipment": True, "is_infantry": True},
            ),
        )
        self.assertTrue(
            unit_skips_infantry_fire_registry(
                "Some_Jet",
                {"is_aerial": True},
            ),
        )
        self.assertFalse(
            unit_skips_infantry_fire_registry(
                "Rifles_US",
                {"is_infantry": True, "is_heavy_equipment": False},
            ),
        )

    def test_avion_tag_from_game_db(self) -> None:
        game_db = {
            "unit_data": {
                "F4E_Phantom_II_napalm_US": {"tags": ["Avion", "Air"]},
            },
        }
        self.assertTrue(
            unit_skips_infantry_fire_registry(
                "F4E_Phantom_II_napalm_US",
                {},
                game_db,
            ),
        )


class CollectAndValidateTests(unittest.TestCase):
    def test_collect_stems_from_salvolength_replace(self) -> None:
        block = {
            "RocketInf_RPG27_105mm": {
                "new_weapon": "RocketInf_RPG7VL_salvolength6",
                "swap_fire_effect": True,
                "depiction_baked_in": False,
            },
        }
        stems = collect_fire_effect_stems_from_replace(block)
        self.assertIn("RocketInf_RPG7VL", stems)
        self.assertNotIn("RocketInf_RPG7VL_salvolength6", stems)

    def test_validate_detects_unknown_depiction_fire_effect(self) -> None:
        game_db = _game_db_with_effects("FM_M16")
        depiction_payload = {
            "unit_name": "Fake_Unit",
            "valid_files": ["DepictionInfantry.ndf"],
            "DepictionInfantry_ndf": {
                ("AllWeaponSubDepiction_Fake_Unit", "TemplateAllSubWeaponDepiction"): {
                    "Operators": {
                        0: ("edit", [("FireEffectTag", "RocketInf_DoesNotExist")]),
                    },
                },
            },
        }
        with patch(
            "src.data.fire_effect_validation.load_unit_edits",
            return_value={},
        ), patch(
            "src.data.fire_effect_validation.NEW_UNITS",
            {},
        ), patch(
            "src.data.fire_effect_validation.load_depiction_edits",
            return_value={"Fake_Unit": depiction_payload},
        ), patch(
            "src.data.fire_effect_validation.NEW_DEPICTIONS",
            {},
        ):
            failed = validate_fire_effect_constants(game_db)
        self.assertTrue(failed)

    def test_validate_skips_hmg_team_vehicle_fx(self) -> None:
        game_db = _game_db_with_effects("FM_M16")
        new_units = {
            ("donor", 0): {
                "NewName": "HMGteam_NSV_para_POL",
                "is_infantry": True,
                "is_heavy_equipment": True,
                "is_ground_vehicle": True,
                "WeaponDescriptor": {
                    "equipmentchanges": {
                        "replace": {
                            "MMG_team_7_62mm_PKM": {
                                "new_weapon": "HMG_team_12_7_mm_NSV",
                                "swap_fire_effect": True,
                                "depiction_baked_in": True,
                            },
                        },
                    },
                },
            },
        }
        with patch(
            "src.data.fire_effect_validation.load_unit_edits",
            return_value={},
        ), patch(
            "src.data.fire_effect_validation.NEW_UNITS",
            new_units,
        ), patch(
            "src.data.fire_effect_validation.load_depiction_edits",
            return_value={},
        ), patch(
            "src.data.fire_effect_validation.NEW_DEPICTIONS",
            {},
        ):
            failed = validate_fire_effect_constants(game_db)
        self.assertFalse(failed)

    def test_validate_skips_vehicle_depiction_channel_tags(self) -> None:
        game_db = _game_db_with_effects("FM_M16")
        depiction_payload = {
            "unit_name": "M2_Bradley_BSV_US",
            "valid_files": ["DepictionVehicles.ndf"],
            "DepictionVehicles_ndf": {
                ("DepictionOperator_M2_Bradley_BSV_US_Weapon1", "DepictionOperator_WeaponInstantFire"): {
                    "FireEffectTag": "'weapon_effet_tag2'",
                },
            },
        }
        with patch(
            "src.data.fire_effect_validation.load_unit_edits",
            return_value={},
        ), patch(
            "src.data.fire_effect_validation.NEW_UNITS",
            {},
        ), patch(
            "src.data.fire_effect_validation.load_depiction_edits",
            return_value={"M2_Bradley_BSV_US": depiction_payload},
        ), patch(
            "src.data.fire_effect_validation.NEW_DEPICTIONS",
            {},
        ):
            failed = validate_fire_effect_constants(game_db)
        self.assertFalse(failed)

    def test_validate_accepts_known_replace_fire_effect(self) -> None:
        game_db = _game_db_with_effects("RocketInf_RPG7VL", "RocketInf_RPG27_105mm")
        unit_edits = {
            "Fake_Squad": {
                "WeaponDescriptor": {
                    "equipmentchanges": {
                        "replace": {
                            "RocketInf_RPG27_105mm": {
                                "new_weapon": "RocketInf_RPG7VL_salvolength6",
                                "swap_fire_effect": True,
                                "depiction_baked_in": False,
                            },
                        },
                    },
                },
            },
        }
        with patch(
            "src.data.fire_effect_validation.load_unit_edits",
            return_value=unit_edits,
        ), patch(
            "src.data.fire_effect_validation.NEW_UNITS",
            {},
        ), patch(
            "src.data.fire_effect_validation.load_depiction_edits",
            return_value={},
        ), patch(
            "src.data.fire_effect_validation.NEW_DEPICTIONS",
            {},
        ):
            failed = validate_fire_effect_constants(game_db)
        self.assertFalse(failed)

    def test_normalize_replace_integration(self) -> None:
        specs = normalize_replace({
            "A": {
                "new_weapon": "B_salvolength8",
                "swap_fire_effect": True,
                "depiction_baked_in": False,
            },
        })
        self.assertEqual(specs[0].new_fire_effect, "B")


if __name__ == "__main__":
    unittest.main()
