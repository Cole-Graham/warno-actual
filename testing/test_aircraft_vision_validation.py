"""Tests for aircraft Standard vision vs weapon ground range validation."""

from __future__ import annotations

import unittest
from typing import Any, Dict
from unittest.mock import patch

from src.data.aircraft_vision_validation import (
    _collect_mounted_ammo_bases,
    _effective_maximum_range_gru,
    _is_aircraft,
    _resolve_standard_vision,
    validate_aircraft_vision_vs_weapon_range,
)


def _minimal_game_db(
    unit_data: Dict[str, Any] | None = None,
    weapons: Dict[str, Any] | None = None,
    ammo_properties: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    return {
        "unit_data": unit_data or {},
        "weapons": weapons or {},
        "ammunition": {"ammo_properties": ammo_properties or {}},
    }


class TestIsAircraft(unittest.TestCase):
    def test_fixed_wing_by_movement(self):
        self.assertTrue(_is_aircraft({"airplane_movement": {}}))

    def test_helicopter_by_flag(self):
        self.assertTrue(_is_aircraft({"is_helo_unit": True}))

    def test_by_avion_tag(self):
        self.assertTrue(_is_aircraft({"tags": ["Avion", "Other"]}))

    def test_by_helico_tag(self):
        self.assertTrue(_is_aircraft({"tags": ["Helico"]}))

    def test_non_aircraft(self):
        self.assertFalse(_is_aircraft({"tags": ["Infantry"]}))


class TestResolveStandardVision(unittest.TestCase):
    def test_vanilla_optics(self):
        vision = _resolve_standard_vision(
            {"optics": {"standard_range": 3500.0}},
            None,
        )
        self.assertEqual(vision, 3500.0)

    def test_edits_override_vanilla(self):
        vision = _resolve_standard_vision(
            {"optics": {"standard_range": 3500.0}},
            {"optics": {"VisionRangesGRU": {"EVisionRange/Standard": 10000.0}}},
        )
        self.assertEqual(vision, 10000.0)


class TestCollectMountedAmmoBases(unittest.TestCase):
    def test_vanilla_mounts(self):
        game_db = _minimal_game_db(
            weapons={
                "WeaponDescriptor_TestPlane_US": {
                    "turrets": {
                        "0": {"weapons": {"AGM_Maverick_x2": {}}},
                    },
                },
            },
        )
        bases = _collect_mounted_ammo_bases("TestPlane_US", game_db, None)
        self.assertEqual(bases, {"AGM_Maverick"})

    def test_equipmentchanges_replace(self):
        game_db = _minimal_game_db(
            weapons={
                "WeaponDescriptor_TestPlane_US": {
                    "turrets": {
                        "0": {"weapons": {"Rocket_Old_x38": {}}},
                    },
                },
            },
        )
        edits = {
            "WeaponDescriptor": {
                "equipmentchanges": {
                    "replace": {
                        "Rocket_Old_x38": {
                            "new_weapon": "Rocket_New_x114",
                            "swap_fire_effect": False,
                            "depiction_baked_in": False,
                        },
                    },
                },
            },
        }
        bases = _collect_mounted_ammo_bases("TestPlane_US", game_db, edits)
        self.assertEqual(bases, {"Rocket_New"})

    def test_donor_descriptor_for_new_unit(self):
        game_db = _minimal_game_db(
            weapons={
                "WeaponDescriptor_DonorPlane_US": {
                    "turrets": {
                        "0": {"weapons": {"Bomb_FAB500": {}}},
                    },
                },
            },
        )
        bases = _collect_mounted_ammo_bases(
            "NewPlane_US",
            game_db,
            None,
            donor_name="DonorPlane_US",
        )
        self.assertEqual(bases, {"Bomb_FAB500"})


class TestEffectiveMaximumRangeGru(unittest.TestCase):
    def test_vanilla_lookup(self):
        game_db = _minimal_game_db(
            ammo_properties={
                "Ammo_Missile_Test": {"MaximumRangeGRU": 5250},
            },
        )
        self.assertEqual(_effective_maximum_range_gru("Missile_Test", game_db), 5250.0)

    def test_vanilla_standards_remap(self):
        game_db = _minimal_game_db(
            ammo_properties={
                "Ammo_Canon_Test": {"MaximumRangeGRU": 1200},
            },
        )
        self.assertEqual(_effective_maximum_range_gru("Canon_Test", game_db), 1225.0)

    def test_missing_range_returns_none(self):
        game_db = _minimal_game_db(ammo_properties={})
        self.assertIsNone(_effective_maximum_range_gru("ECM_Pod", game_db))

    @patch("src.data.aircraft_vision_validation._constants_maximum_range_gru")
    def test_constants_override_beats_vanilla(self, mock_constants):
        mock_constants.return_value = 7000.0
        game_db = _minimal_game_db(
            ammo_properties={
                "Ammo_Missile_Test": {"MaximumRangeGRU": 5250},
            },
        )
        self.assertEqual(_effective_maximum_range_gru("Missile_Test", game_db), 7000.0)


class TestValidateAircraftVision(unittest.TestCase):
    def _aircraft_unit(self, vision: float) -> Dict[str, Any]:
        return {
            "airplane_movement": {},
            "tags": ["Avion"],
            "optics": {"standard_range": vision},
        }

    @patch("src.data.aircraft_vision_validation.collect_newdivisionrules_unit_names")
    @patch("src.data.aircraft_vision_validation.load_unit_edits")
    def test_pass_when_vision_meets_weapon_range(self, mock_load_edits, mock_div_rules):
        mock_load_edits.return_value = {}
        mock_div_rules.return_value = {"Plane_OK_US"}
        game_db = _minimal_game_db(
            unit_data={"Plane_OK_US": self._aircraft_unit(5000.0)},
            weapons={
                "WeaponDescriptor_Plane_OK_US": {
                    "turrets": {"0": {"weapons": {"Missile_x2": {}}}},
                },
            },
            ammo_properties={"Ammo_Missile": {"MaximumRangeGRU": 3000}},
        )
        self.assertFalse(validate_aircraft_vision_vs_weapon_range(game_db))

    @patch("src.data.aircraft_vision_validation.collect_newdivisionrules_unit_names")
    @patch("src.data.aircraft_vision_validation.load_unit_edits")
    def test_fail_when_vision_below_weapon_range(self, mock_load_edits, mock_div_rules):
        mock_load_edits.return_value = {}
        mock_div_rules.return_value = {"Plane_BAD_US"}
        game_db = _minimal_game_db(
            unit_data={"Plane_BAD_US": self._aircraft_unit(1000.0)},
            weapons={
                "WeaponDescriptor_Plane_BAD_US": {
                    "turrets": {"0": {"weapons": {"Missile_x2": {}}}},
                },
            },
            ammo_properties={"Ammo_Missile": {"MaximumRangeGRU": 3000}},
        )
        self.assertTrue(validate_aircraft_vision_vs_weapon_range(game_db))

    @patch("src.data.aircraft_vision_validation.collect_newdivisionrules_unit_names")
    @patch("src.data.aircraft_vision_validation.load_unit_edits")
    def test_skip_violation_when_unit_not_in_division_rules(self, mock_load_edits, mock_div_rules):
        mock_load_edits.return_value = {}
        mock_div_rules.return_value = set()
        game_db = _minimal_game_db(
            unit_data={"Plane_BAD_US": self._aircraft_unit(1000.0)},
            weapons={
                "WeaponDescriptor_Plane_BAD_US": {
                    "turrets": {"0": {"weapons": {"Missile_x2": {}}}},
                },
            },
            ammo_properties={"Ammo_Missile": {"MaximumRangeGRU": 3000}},
        )
        self.assertFalse(validate_aircraft_vision_vs_weapon_range(game_db))

    @patch("src.data.aircraft_vision_validation.collect_newdivisionrules_unit_names")
    @patch("src.data.aircraft_vision_validation.load_unit_edits")
    def test_non_aircraft_skipped(self, mock_load_edits, mock_div_rules):
        mock_load_edits.return_value = {}
        mock_div_rules.return_value = {"Tank_US"}
        game_db = _minimal_game_db(
            unit_data={
                "Tank_US": {
                    "tags": ["Char"],
                    "optics": {"standard_range": 500.0},
                },
            },
            weapons={
                "WeaponDescriptor_Tank_US": {
                    "turrets": {"0": {"weapons": {"Canon_AP": {}}}},
                },
            },
            ammo_properties={"Ammo_Canon_AP": {"MaximumRangeGRU": 3000}},
        )
        self.assertFalse(validate_aircraft_vision_vs_weapon_range(game_db))

    @patch("src.data.aircraft_vision_validation.collect_newdivisionrules_unit_names")
    @patch("src.data.aircraft_vision_validation.load_unit_edits")
    def test_weapon_without_ground_range_ignored(self, mock_load_edits, mock_div_rules):
        mock_load_edits.return_value = {}
        mock_div_rules.return_value = {"Plane_ECM_US"}
        game_db = _minimal_game_db(
            unit_data={"Plane_ECM_US": self._aircraft_unit(1000.0)},
            weapons={
                "WeaponDescriptor_Plane_ECM_US": {
                    "turrets": {
                        "0": {"weapons": {"ECM_Pod": {}, "Missile_x2": {}}},
                    },
                },
            },
            ammo_properties={"Ammo_Missile": {"MaximumRangeGRU": 800}},
        )
        self.assertFalse(validate_aircraft_vision_vs_weapon_range(game_db))


if __name__ == "__main__":
    unittest.main()
