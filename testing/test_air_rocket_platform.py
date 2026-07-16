"""Tests for air rocket platform pairing and remount decisions."""

import unittest
from unittest import mock
from unittest.mock import MagicMock

from src.constants.unit_edits.standards.pattern.air_rocket_platform import (
    AIR_ROCKET_DAMAGE_FAMILY,
    AIR_ROCKET_PLATFORM_PAIRS,
    build_air_rocket_platform_maps,
)
from src.gameplay_mods.generated.gameplay.gfx.weapon_descriptor.handlers.air_rocket_platform import (
    _lookup_family,
    _resolve_ammo_name,
    _unit_platform,
    apply_air_rocket_platform_standard,
)


class TestAirRocketPlatformMaps(unittest.TestCase):
    def test_b8_pair_round_trip(self):
        helo_to_avion, avion_to_helo, helo_names, avion_names = (
            build_air_rocket_platform_maps()
        )
        helo = "RocketAir_B8_80mm_salvolength40"
        avion = "RocketAir_B8_80mm_avion_salvolength40"
        self.assertEqual(helo_to_avion[helo], avion)
        self.assertEqual(avion_to_helo[avion], helo)
        self.assertIn(helo, helo_names)
        self.assertIn(avion, avion_names)
        self.assertNotIn(avion, helo_names)

    def test_hydra76_has_distinct_helo_and_avion(self):
        helo_to_avion, _, helo_names, avion_names = build_air_rocket_platform_maps()
        helo = "RocketAir_Hydra_70mm_salvolength76"
        avion = "RocketAir_Hydra_70mm_avion_salvolength76"
        self.assertEqual(helo_to_avion[helo], avion)
        self.assertIn(helo, helo_names)
        self.assertNotIn(helo, avion_names)
        self.assertIn(avion, avion_names)
        self.assertNotIn(avion, helo_names)

    def test_sneb_helo_suffix_is_same_salvo_helo_side(self):
        helo_to_avion, avion_to_helo, helo_names, avion_names = (
            build_air_rocket_platform_maps()
        )
        helo = "RocketAir_SNEB_68mm_x18_helo"
        avion = "RocketAir_SNEB_68mm_avion_salvolength18"
        self.assertEqual(helo_to_avion[helo], avion)
        self.assertEqual(avion_to_helo[avion], helo)
        self.assertIn(helo, helo_names)
        self.assertNotIn(helo, avion_names)
        self.assertNotIn(avion, helo_names)

    def test_different_salvo_lengths_are_not_paired(self):
        helo_to_avion, _, _, _ = build_air_rocket_platform_maps()
        self.assertNotEqual(
            helo_to_avion.get("RocketAir_S24_240mm_salvolength2"),
            "RocketAir_S24_240mm_avion_salvolength4",
        )
        self.assertNotEqual(
            helo_to_avion.get("RocketAir_SNEB_68mm_salvolength36"),
            "RocketAir_SNEB_68mm_avion_salvolength18",
        )
        self.assertEqual(
            helo_to_avion["RocketAir_S24_240mm_salvolength2"],
            "RocketAir_S24_240mm_avion_salvolength2",
        )
        self.assertEqual(
            helo_to_avion["RocketAir_SNEB_68mm_salvolength36"],
            "RocketAir_SNEB_68mm_avion_salvolength36",
        )
        self.assertEqual(
            helo_to_avion["RocketAir_S24_240mm_salvolength4"],
            "RocketAir_S24_240mm_avion_salvolength4",
        )

    def test_no_self_pairs(self):
        for pair in AIR_ROCKET_PLATFORM_PAIRS:
            self.assertNotEqual(
                pair["helo_ammo"],
                pair["avion_ammo"],
                msg=f"self-pair not allowed: {pair['helo_ammo']}",
            )

    def test_pairs_non_empty(self):
        self.assertGreater(len(AIR_ROCKET_PLATFORM_PAIRS), 10)


class TestAirRocketPlatformHelpers(unittest.TestCase):
    def test_unit_platform(self):
        self.assertEqual(_unit_platform({"is_helo_unit": True}), "helo")
        self.assertEqual(
            _unit_platform({"airplane_movement": {"SpeedInKmph": 800}}),
            "plane",
        )
        self.assertIsNone(_unit_platform({}))
        self.assertEqual(
            _unit_platform({"is_helo_unit": True, "airplane_movement": {}}),
            "helo",
        )

    def test_resolve_ammo_name_via_rename(self):
        old_new = {
            "RocketAir_B8_80mm_x40_avion": "RocketAir_B8_80mm_avion_salvolength40",
        }
        new_old = {v: k for k, v in old_new.items()}
        self.assertEqual(
            _resolve_ammo_name(
                "RocketAir_B8_80mm_x40_avion", old_new, new_old,
            ),
            "RocketAir_B8_80mm_avion_salvolength40",
        )
        self.assertEqual(
            _resolve_ammo_name(
                "RocketAir_B8_80mm_avion_salvolength40", old_new, new_old,
            ),
            "RocketAir_B8_80mm_avion_salvolength40",
        )

    def test_lookup_family(self):
        props = {
            "Ammo_RocketAir_B8_80mm_x40": {
                "Family": AIR_ROCKET_DAMAGE_FAMILY,
            },
        }
        old_new = {
            "RocketAir_B8_80mm_x40": "RocketAir_B8_80mm_salvolength40",
        }
        new_old = {v: k for k, v in old_new.items()}
        self.assertEqual(
            _lookup_family(
                "RocketAir_B8_80mm_salvolength40", props, old_new, new_old,
            ),
            AIR_ROCKET_DAMAGE_FAMILY,
        )


class TestAirRocketPlatformRemount(unittest.TestCase):
    def _make_mount(self, ammo_path: str) -> MagicMock:
        ammo_membr = MagicMock()
        ammo_membr.v = ammo_path
        mount = MagicMock()
        mount.v.by_m = MagicMock(
            side_effect=lambda name, *a: ammo_membr if name == "Ammunition" else None,
        )
        return mount, ammo_membr

    def _make_wd(self, unit_name: str, ammo_path: str):
        mount, ammo_membr = self._make_mount(ammo_path)
        mounted_list = MagicMock()
        mounted_list.v = [mount]
        turret = MagicMock()
        turret.v.by_m = MagicMock(
            side_effect=lambda name, *a: (
                mounted_list if name == "MountedWeaponDescriptorList" else None
            ),
        )
        turret_list = MagicMock()
        turret_list.v = [turret]
        wd = MagicMock()
        wd.namespace = f"WeaponDescriptor_{unit_name}"
        wd.v.by_m = MagicMock(
            side_effect=lambda name, *a: (
                turret_list if name == "TurretDescriptorList" else None
            ),
        )
        return wd, ammo_membr

    def test_plane_remounts_helo_b8_to_avion(self):
        wd, ammo_membr = self._make_wd(
            "Su_25_rkt2_SOV",
            "$/GFX/Weapon/Ammo_RocketAir_B8_80mm_salvolength40",
        )
        game_db = {
            "unit_data": {
                "Su_25_rkt2_SOV": {"airplane_movement": {"SpeedInKmph": 750}},
            },
            "ammunition": {
                "ammo_properties": {
                    "Ammo_RocketAir_B8_80mm_salvolength40": {
                        "Family": AIR_ROCKET_DAMAGE_FAMILY,
                    },
                },
                "renames_old_new": {},
                "renames_new_old": {},
            },
        }
        logger = MagicMock()

        with mock.patch(
            "src.gameplay_mods.generated.gameplay.gfx.weapon_descriptor.handlers.air_rocket_platform.is_valid_turret",
            return_value=True,
        ), mock.patch(
            "src.gameplay_mods.generated.gameplay.gfx.weapon_descriptor.handlers.air_rocket_platform.is_obj_type",
            return_value=True,
        ):
            apply_air_rocket_platform_standard(logger, [wd], game_db)

        self.assertEqual(
            ammo_membr.v,
            "$/GFX/Weapon/Ammo_RocketAir_B8_80mm_avion_salvolength40",
        )

    def test_helo_remounts_avion_to_helo(self):
        wd, ammo_membr = self._make_wd(
            "Mi_24P_SOV",
            "$/GFX/Weapon/Ammo_RocketAir_B8_80mm_avion_salvolength40",
        )
        game_db = {
            "unit_data": {"Mi_24P_SOV": {"is_helo_unit": True}},
            "ammunition": {
                "ammo_properties": {
                    "Ammo_RocketAir_B8_80mm_avion_salvolength40": {
                        "Family": AIR_ROCKET_DAMAGE_FAMILY,
                    },
                },
                "renames_old_new": {},
                "renames_new_old": {},
            },
        }
        logger = MagicMock()

        with mock.patch(
            "src.gameplay_mods.generated.gameplay.gfx.weapon_descriptor.handlers.air_rocket_platform.is_valid_turret",
            return_value=True,
        ), mock.patch(
            "src.gameplay_mods.generated.gameplay.gfx.weapon_descriptor.handlers.air_rocket_platform.is_obj_type",
            return_value=True,
        ):
            apply_air_rocket_platform_standard(logger, [wd], game_db)

        self.assertEqual(
            ammo_membr.v,
            "$/GFX/Weapon/Ammo_RocketAir_B8_80mm_salvolength40",
        )

    def test_unpaired_warns_and_skips(self):
        wd, ammo_membr = self._make_wd(
            "Some_Plane",
            "$/GFX/Weapon/Ammo_RocketAir_Unknown_99mm_salvolength4",
        )
        original = ammo_membr.v
        game_db = {
            "unit_data": {"Some_Plane": {"airplane_movement": {}}},
            "ammunition": {
                "ammo_properties": {
                    "Ammo_RocketAir_Unknown_99mm_salvolength4": {
                        "Family": AIR_ROCKET_DAMAGE_FAMILY,
                    },
                },
                "renames_old_new": {},
                "renames_new_old": {},
            },
        }
        logger = MagicMock()

        with mock.patch(
            "src.gameplay_mods.generated.gameplay.gfx.weapon_descriptor.handlers.air_rocket_platform.is_valid_turret",
            return_value=True,
        ), mock.patch(
            "src.gameplay_mods.generated.gameplay.gfx.weapon_descriptor.handlers.air_rocket_platform.is_obj_type",
            return_value=True,
        ):
            apply_air_rocket_platform_standard(logger, [wd], game_db)

        self.assertEqual(ammo_membr.v, original)
        logger.warning.assert_called()


if __name__ == "__main__":
    unittest.main()
