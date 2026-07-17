"""Tests for infantry small-arms quantity vs strength validation."""

from __future__ import annotations

import unittest
from typing import Any, Dict
from unittest.mock import patch

from src.data.infantry_small_arms_strength_validation import (
    EXCLUDED_AMMO_CATEGORIES,
    _OCCUPIED_SLOT_MINMAX_CATEGORIES,
    _classify_mount_role,
    _is_weapon_team_by_loadout,
    _occupied_weapon_slots,
    _should_validate_unit,
    _sum_countable_small_arms,
    build_countable_small_arms_weapons,
    build_infantry_small_arms_balance,
    resolve_infantry_mounts,
    resolve_infantry_mounts_by_turret,
    validate_infantry_small_arms_vs_strength,
)


def _sa_props() -> Dict[str, Any]:
    return {"Family": "DamageFamily_sa_full", "MinMaxCategory": None}


def _at_props() -> Dict[str, Any]:
    return {"Family": "DamageFamily_thermobarique", "MinMaxCategory": None}


def _minimal_game_db(
    unit_data: Dict[str, Any] | None = None,
    weapons: Dict[str, Any] | None = None,
    ammo_properties: Dict[str, Any] | None = None,
) -> Dict[str, Any]:
    return {
        "unit_data": unit_data or {},
        "weapons": weapons or {},
        "ammunition": {
            "ammo_properties": ammo_properties or {},
            "renames_old_new": {},
        },
    }


class TestCountableSmallArms(unittest.TestCase):
    def test_small_arms_constants_counted(self):
        game_db = _minimal_game_db(
            ammo_properties={"Ammo_FM_M16": _sa_props()},
        )
        countable = build_countable_small_arms_weapons(game_db)
        self.assertIn("FM_M16", countable)

    def test_at_and_team_weapons_excluded(self):
        game_db = _minimal_game_db(
            ammo_properties={
                "Ammo_RocketInf_RPG7": _at_props(),
                "Ammo_MMG_team_7_62mm_M60": {
                    "Family": "DamageFamily_sa_full",
                    "MinMaxCategory": "MinMax_MMG_HMG",
                },
            },
        )
        countable = build_countable_small_arms_weapons(game_db)
        self.assertNotIn("RocketInf_RPG7", countable)
        self.assertNotIn("MMG_team_7_62mm_M60", countable)

    def test_heavy_sniper_and_constants_small_arms_counted(self):
        game_db = _minimal_game_db(
            ammo_properties={
                "Ammo_SniperHvy_Barret_M82": {
                    "Family": "DamageFamily_sniper",
                    "MinMaxCategory": "MinMax_inf_sniper",
                },
            },
        )
        countable = build_countable_small_arms_weapons(game_db)
        self.assertIn("SniperHvy_Barret_M82", countable)


class TestExcludedAmmoCategories(unittest.TestCase):
    def test_atgm_in_excluded_categories(self):
        self.assertIn("ATGM", EXCLUDED_AMMO_CATEGORIES)

    def test_minmax_atgm_not_occupied_slot(self):
        self.assertNotIn("MinMax_ATGM", _OCCUPIED_SLOT_MINMAX_CATEGORIES)


class TestMountRoleClassification(unittest.TestCase):
    def setUp(self):
        self.game_db = _minimal_game_db(
            ammo_properties={
                "Ammo_FM_M16": _sa_props(),
                "Ammo_RocketInf_RPG7": _at_props(),
                "Ammo_ATGM_9K115_Metis": {"MinMaxCategory": "MinMax_ATGM"},
                "Ammo_ATGM_MILAN": {"MinMaxCategory": "MinMax_ATGM"},
                "Ammo_RocketInf_WOMBAT_RCL_120mm": {
                    "MinMaxCategory": "MinMax_CanonAP",
                },
                "Ammo_MMG_team_7_62mm_MG3": {
                    "MinMaxCategory": "MinMax_MMG_HMG",
                },
            },
        )
        self.countable = build_countable_small_arms_weapons(self.game_db)

    def test_roles(self):
        cases = [
            ("FM_M16", "countable"),
            ("RocketInf_RPG7", "specialist"),
            ("ATGM_9K115_Metis", "specialist"),
            ("ATGM_MILAN", "specialist"),
            ("RocketInf_WOMBAT_RCL_120mm", "occupied"),
            ("MMG_team_7_62mm_MG3", "team_mg"),
        ]
        for weapon, expected in cases:
            with self.subTest(weapon=weapon):
                role = _classify_mount_role(weapon, self.countable, self.game_db)
                self.assertEqual(role, expected)


class TestWeaponTeamByLoadout(unittest.TestCase):
    def _game_db(self) -> Dict[str, Any]:
        return _minimal_game_db(
            ammo_properties={
                "Ammo_RocketInf_WOMBAT_RCL_120mm": {
                    "MinMaxCategory": "MinMax_CanonAP",
                },
                "Ammo_RocketInf_WOMBAT_RCL_120mm_HE": {
                    "MinMaxCategory": "MinMax_CanonAP",
                },
                "Ammo_MMG_team_7_62mm_MG3": {
                    "MinMaxCategory": "MinMax_MMG_HMG",
                },
                "Ammo_ATGM_MILAN": {"MinMaxCategory": "MinMax_ATGM"},
                "Ammo_FM_M16": _sa_props(),
                "Ammo_RocketInf_RPG7": _at_props(),
            },
        )

    def test_wombat_dual_ammo_is_weapon_team(self):
        countable = build_countable_small_arms_weapons(self._game_db())
        mounts = {
            0: [
                ("RocketInf_WOMBAT_RCL_120mm", 1),
                ("RocketInf_WOMBAT_RCL_120mm_HE", 1),
            ],
        }
        self.assertTrue(_is_weapon_team_by_loadout(mounts, countable, self._game_db()))

    def test_hmg_team_is_weapon_team(self):
        countable = build_countable_small_arms_weapons(self._game_db())
        mounts = {0: [("MMG_team_7_62mm_MG3", 1)]}
        self.assertTrue(_is_weapon_team_by_loadout(mounts, countable, self._game_db()))

    def test_milan_only_team_is_weapon_team(self):
        countable = build_countable_small_arms_weapons(self._game_db())
        mounts = {0: [("ATGM_MILAN", 1)]}
        self.assertTrue(_is_weapon_team_by_loadout(mounts, countable, self._game_db()))

    def test_rifle_plus_rpg_not_weapon_team(self):
        countable = build_countable_small_arms_weapons(self._game_db())
        mounts = {0: [("FM_M16", 6), ("RocketInf_RPG7", 2)]}
        self.assertFalse(_is_weapon_team_by_loadout(mounts, countable, self._game_db()))


class TestShouldValidateUnit(unittest.TestCase):
    def test_infantry_in_unit_edits(self):
        edits = {"UnitRole": "infantry"}
        self.assertTrue(
            _should_validate_unit("MotRifles_SOV", {"unit_role": "infantry"}, edits),
        )

    def test_hmg_team_without_infantry_role_not_validated(self):
        self.assertFalse(
            _should_validate_unit("HMGteam_MG3_RFA", {}, {}),
        )


class TestResolveInfantryMounts(unittest.TestCase):
    def test_vanilla_single_mount(self):
        game_db = _minimal_game_db(
            weapons={
                "WeaponDescriptor_Rifles_US": {
                    "turrets": {
                        "0": {
                            "weapons": {
                                "FM_M16": {"quantity": 6},
                            },
                        },
                    },
                },
            },
        )
        mounts = resolve_infantry_mounts("Rifles_US", None, None, game_db)
        self.assertEqual(mounts, [("FM_M16", 6)])

    def test_by_turret_preserves_indices(self):
        game_db = _minimal_game_db(
            weapons={
                "WeaponDescriptor_DShV_Metis_SOV": {
                    "turrets": {
                        "0": {"weapons": {"FM_AKS_74": {"quantity": 7}}},
                        "1": {"weapons": {"SAW_RPK_74_5_56mm": {"quantity": 1}}},
                        "2": {"weapons": {"ATGM_9K115_Metis": {"quantity": 1}}},
                    },
                },
            },
        )
        by_turret = resolve_infantry_mounts_by_turret(
            "DShV_Metis_SOV", None, None, game_db,
        )
        self.assertEqual(by_turret[0], [("FM_AKS_74", 7)])
        self.assertEqual(by_turret[2], [("ATGM_9K115_Metis", 1)])

    def test_quantity_override(self):
        game_db = _minimal_game_db(
            weapons={
                "WeaponDescriptor_Rifles_US": {
                    "turrets": {
                        "0": {
                            "weapons": {
                                "FM_M16": {"quantity": 6},
                            },
                        },
                    },
                },
            },
        )
        edits = {
            "WeaponDescriptor": {
                "equipmentchanges": {
                    "quantity": {"FM_M16": 5},
                },
            },
        }
        mounts = resolve_infantry_mounts("Rifles_US", edits, None, game_db)
        self.assertEqual(mounts, [("FM_M16", 5)])

    def test_replace_swaps_mount(self):
        game_db = _minimal_game_db(
            weapons={
                "WeaponDescriptor_Rifles_US": {
                    "turrets": {
                        "0": {
                            "weapons": {
                                "RocketInf_RPG7": {"quantity": 2},
                                "FM_M16": {"quantity": 4},
                            },
                        },
                    },
                },
            },
        )
        edits = {
            "WeaponDescriptor": {
                "equipmentchanges": {
                    "replace": {
                        "RocketInf_RPG7": {
                            "new_weapon": "SAW_M249_5_56mm",
                            "swap_fire_effect": True,
                            "depiction_baked_in": False,
                        },
                    },
                },
            },
        }
        mounts = resolve_infantry_mounts("Rifles_US", edits, None, game_db)
        self.assertEqual(
            mounts,
            [("SAW_M249_5_56mm", 2), ("FM_M16", 4)],
        )

    def test_mounted_weapons_remove_he_then_replace_heat(self):
        """Dual HEAT/HE recoilless: drop HE companion, then replace HEAT."""
        game_db = _minimal_game_db(
            weapons={
                "WeaponDescriptor_Rangers_CMD_US": {
                    "turrets": {
                        "0": {"weapons": {"PM_M4_Carbine": {"quantity": 5}}},
                        "1": {"weapons": {"Sniper_M24": {"quantity": 1}}},
                        "2": {
                            "weapons": {
                                "RocketInf_M67_RCL_90mm": {"quantity": 1},
                                "RocketInf_M67_RCL_90mm_HE": {"quantity": 1},
                            },
                        },
                        "3": {"weapons": {"Grenade_SMOKE": {"quantity": 1}}},
                    },
                },
            },
        )
        edits = {
            "WeaponDescriptor": {
                "equipmentchanges": {
                    "replace": {
                        "RocketInf_M67_RCL_90mm": {
                            "new_weapon": "RocketInf_Carl_Gustav",
                            "swap_fire_effect": True,
                            "depiction_baked_in": False,
                        },
                    },
                },
                "turrets": {
                    2: {
                        "MountedWeapons": {
                            "remove": [1],
                        },
                    },
                },
            },
        }
        by_turret = resolve_infantry_mounts_by_turret(
            "Rangers_CMD_US", edits, None, game_db,
        )
        self.assertEqual(by_turret[2], [("RocketInf_Carl_Gustav", 1)])
        self.assertNotIn(
            "RocketInf_M67_RCL_90mm_HE",
            [name for name, _ in by_turret[2]],
        )

    def test_ordered_replace_list_one_mount_per_spec(self):
        """Same old_weapon on two turrets: each list entry replaces one mount."""
        game_db = _minimal_game_db(
            weapons={
                "WeaponDescriptor_MotSchutzen_DDR": {
                    "turrets": {
                        "0": {"weapons": {"FM_Mpi_AK_74N": {"quantity": 5}}},
                        "1": {"weapons": {"RocketInf_RPG7VR_64mm": {"quantity": 2}}},
                        "2": {"weapons": {"RocketInf_RPG7VR_64mm": {"quantity": 2}}},
                    },
                },
            },
            ammo_properties={
                "Ammo_FM_Mpi_AK_74N": _sa_props(),
                "Ammo_SAW_lMG_K_7_62mm": _sa_props(),
                "Ammo_RocketInf_RPG29_105mm": _at_props(),
            },
        )
        edits = {
            "WeaponDescriptor": {
                "equipmentchanges": {
                    "quantity": {
                        "FM_Mpi_AK_74N": 5,
                        "SAW_lMG_K_7_62mm": 2,
                    },
                    "replace": {
                        "RocketInf_RPG7VR_64mm": [
                            {
                                "new_weapon": "SAW_lMG_K_7_62mm",
                                "swap_fire_effect": True,
                                "depiction_baked_in": False,
                            },
                            {
                                "new_weapon": "RocketInf_RPG29_105mm",
                                "swap_fire_effect": True,
                                "depiction_baked_in": False,
                            },
                        ],
                    },
                },
            },
        }
        mounts = resolve_infantry_mounts(
            "MotSchutzen_RPG29_DDR", edits, "MotSchutzen_DDR", game_db,
        )
        self.assertEqual(
            mounts,
            [
                ("FM_Mpi_AK_74N", 5),
                ("SAW_lMG_K_7_62mm", 2),
                ("RocketInf_RPG29_105mm", 2),
            ],
        )
        countable = build_countable_small_arms_weapons(game_db)
        total, _breakdown = _sum_countable_small_arms(mounts, countable)
        self.assertEqual(total, 7)

    def test_new_unit_uses_donor_descriptor(self):
        game_db = _minimal_game_db(
            weapons={
                "WeaponDescriptor_Donor_US": {
                    "turrets": {
                        "0": {
                            "weapons": {
                                "FM_M16": {"quantity": 3},
                                "Commando_733": {"quantity": 2},
                            },
                        },
                    },
                },
            },
        )
        edits = {
            "WeaponDescriptor": {
                "equipmentchanges": {
                    "quantity": {
                        "FM_M16": 2,
                        "Commando_733": 3,
                    },
                },
            },
        }
        mounts = resolve_infantry_mounts("New_CMD_US", edits, "Donor_US", game_db)
        self.assertEqual(
            mounts,
            [("FM_M16", 2), ("Commando_733", 3)],
        )

    def test_turret_remove_drops_mounts(self):
        game_db = _minimal_game_db(
            weapons={
                "WeaponDescriptor_Gebirgs_RFA": {
                    "turrets": {
                        "0": {"weapons": {"FM_G3KA4": {"quantity": 8}}},
                        "1": {"weapons": {"Sniper_G3A3ZF": {"quantity": 1}}},
                        "2": {"weapons": {"MMG_inf__MG3_7_62mm": {"quantity": 3}}},
                    },
                },
            },
        )
        edits = {
            "WeaponDescriptor": {
                "turrets": {"remove": [1]},
                "equipmentchanges": {
                    "quantity": {
                        "FM_G3KA4": 8,
                        "MMG_inf__MG3_7_62mm": 3,
                    },
                },
            },
        }
        mounts = resolve_infantry_mounts("Gebirgs_RFA", edits, None, game_db)
        self.assertEqual(
            mounts,
            [("FM_G3KA4", 8), ("MMG_inf__MG3_7_62mm", 3)],
        )


class TestOccupiedWeaponSlots(unittest.TestCase):
    def test_single_canon_mount_per_turret(self):
        game_db = _minimal_game_db(
            ammo_properties={
                "Ammo_RocketInf_WOMBAT_RCL_120mm": {
                    "MinMaxCategory": "MinMax_CanonAP",
                },
            },
        )
        mounts_by_turret = {0: [("RocketInf_WOMBAT_RCL_120mm", 5)]}
        self.assertEqual(_occupied_weapon_slots(mounts_by_turret, game_db), 5)

    def test_dual_canon_ammo_max_per_turret(self):
        game_db = _minimal_game_db(
            ammo_properties={
                "Ammo_RocketInf_WOMBAT_RCL_120mm": {
                    "MinMaxCategory": "MinMax_CanonAP",
                },
                "Ammo_RocketInf_WOMBAT_RCL_120mm_HE": {
                    "MinMaxCategory": "MinMax_CanonAP",
                },
            },
        )
        mounts_by_turret = {
            0: [
                ("RocketInf_WOMBAT_RCL_120mm", 1),
                ("RocketInf_WOMBAT_RCL_120mm_HE", 1),
            ],
        }
        self.assertEqual(_occupied_weapon_slots(mounts_by_turret, game_db), 1)

    def test_flame_sum_per_turret(self):
        game_db = _minimal_game_db(
            ammo_properties={
                "Ammo_RocketInf_RPO_A_93mm": {
                    "MinMaxCategory": "MinMax_FLAME",
                },
            },
        )
        mounts_by_turret = {0: [("RocketInf_RPO_A_93mm", 2)]}
        self.assertEqual(_occupied_weapon_slots(mounts_by_turret, game_db), 2)

    def test_portable_atgm_does_not_occupy_slot(self):
        game_db = _minimal_game_db(
            ammo_properties={
                "Ammo_ATGM_9K115_Metis": {"MinMaxCategory": "MinMax_ATGM"},
                "Ammo_FM_M16": _sa_props(),
            },
        )
        mounts_by_turret = {
            0: [("FM_M16", 7)],
            2: [("ATGM_9K115_Metis", 1)],
        }
        self.assertEqual(_occupied_weapon_slots(mounts_by_turret, game_db), 0)

    def test_napalm_without_minmax_flame_does_not_occupy_slot(self):
        game_db = _minimal_game_db(
            ammo_properties={
                "Ammo_RocketInf_M202_Flash_66mm": {
                    "MinMaxCategory": "MinMax_inf_rocket",
                },
            },
        )
        mounts_by_turret = {
            0: [("FM_M16", 6), ("RocketInf_M202_Flash_66mm", 2)],
        }
        self.assertEqual(_occupied_weapon_slots(mounts_by_turret, game_db), 0)


class TestSumCountableSmallArms(unittest.TestCase):
    def test_rpg_excluded_from_total(self):
        countable = {"FM_M16", "SAW_M249_5_56mm"}
        mounts = [("FM_M16", 4), ("RocketInf_RPG7", 2), ("SAW_M249_5_56mm", 2)]
        total, breakdown = _sum_countable_small_arms(mounts, countable)
        self.assertEqual(total, 6)
        self.assertEqual(breakdown, {"FM_M16": 4, "SAW_M249_5_56mm": 2})


class TestBuildAndValidateBalance(unittest.TestCase):
    def _rifle_squad_db(self) -> Dict[str, Any]:
        return _minimal_game_db(
            unit_data={
                "Rifles_US": {
                    "unit_role": "infantry",
                    "strength": 6,
                },
            },
            weapons={
                "WeaponDescriptor_Rifles_US": {
                    "turrets": {
                        "0": {
                            "weapons": {
                                "FM_M16": {"quantity": 6},
                            },
                        },
                    },
                },
            },
            ammo_properties={"Ammo_FM_M16": _sa_props()},
        )

    @patch("src.data.infantry_small_arms_strength_validation.NEW_UNITS", {})
    @patch("src.data.infantry_small_arms_strength_validation.load_unit_edits")
    def test_matching_squad_passes(self, mock_load_edits):
        mock_load_edits.return_value = {
            "Rifles_US": {"UnitRole": "infantry", "strength": 6},
        }
        balance = build_infantry_small_arms_balance(self._rifle_squad_db())
        self.assertEqual(balance["Rifles_US"]["small_arms_total"], 6)
        self.assertEqual(balance["Rifles_US"]["expected_small_arms"], 6)
        self.assertFalse(validate_infantry_small_arms_vs_strength(self._rifle_squad_db(), balance))

    @patch("src.data.infantry_small_arms_strength_validation.NEW_UNITS", {})
    @patch("src.data.infantry_small_arms_strength_validation.load_unit_edits")
    def test_mismatch_reports_error(self, mock_load_edits):
        mock_load_edits.return_value = {
            "Rifles_US": {
                "UnitRole": "infantry",
                "strength": 6,
                "WeaponDescriptor": {
                    "equipmentchanges": {
                        "quantity": {"FM_M16": 5},
                    },
                },
            },
        }
        balance = build_infantry_small_arms_balance(self._rifle_squad_db())
        self.assertEqual(balance["Rifles_US"]["small_arms_total"], 5)
        self.assertTrue(validate_infantry_small_arms_vs_strength(self._rifle_squad_db(), balance))

    @patch("src.data.infantry_small_arms_strength_validation.NEW_UNITS", {})
    @patch("src.data.infantry_small_arms_strength_validation.load_unit_edits")
    def test_cmd_squad_two_weapons(self, mock_load_edits):
        game_db = _minimal_game_db(
            unit_data={
                "Rifles_CMD_US": {"unit_role": "infantry", "strength": 5},
            },
            weapons={
                "WeaponDescriptor_Rifles_CMD_US": {
                    "turrets": {
                        "0": {
                            "weapons": {
                                "FM_M16": {"quantity": 2},
                                "Commando_733": {"quantity": 3},
                            },
                        },
                    },
                },
            },
            ammo_properties={
                "Ammo_FM_M16": _sa_props(),
                "Ammo_Commando_733": _sa_props(),
            },
        )
        mock_load_edits.return_value = {
            "Rifles_CMD_US": {
                "UnitRole": "hq_inf",
                "strength": 5,
                "WeaponDescriptor": {
                    "equipmentchanges": {
                        "quantity": {
                            "FM_M16": 2,
                            "Commando_733": 3,
                        },
                    },
                },
            },
        }
        balance = build_infantry_small_arms_balance(game_db)
        self.assertEqual(balance["Rifles_CMD_US"]["small_arms_total"], 5)
        self.assertFalse(validate_infantry_small_arms_vs_strength(game_db, balance))

    @patch("src.data.infantry_small_arms_strength_validation.load_unit_edits")
    def test_motschutzen_rpg29_ordered_replace_passes(self, mock_load_edits):
        mock_load_edits.return_value = {}
        game_db = _minimal_game_db(
            unit_data={
                "MotSchutzen_RPG29_DDR": {"unit_role": "infantry", "strength": 7},
            },
            weapons={
                "WeaponDescriptor_MotSchutzen_DDR": {
                    "turrets": {
                        "0": {"weapons": {"FM_Mpi_AK_74N": {"quantity": 5}}},
                        "1": {"weapons": {"RocketInf_RPG7VR_64mm": {"quantity": 2}}},
                        "2": {"weapons": {"RocketInf_RPG7VR_64mm": {"quantity": 2}}},
                    },
                },
            },
            ammo_properties={
                "Ammo_FM_Mpi_AK_74N": _sa_props(),
                "Ammo_SAW_lMG_K_7_62mm": _sa_props(),
                "Ammo_RocketInf_RPG29_105mm": _at_props(),
            },
        )
        new_unit_data = {
            "NewName": "MotSchutzen_RPG29_DDR",
            "strength": 7,
            "UnitRole": "infantry",
            "WeaponDescriptor": {
                "equipmentchanges": {
                    "quantity": {
                        "FM_Mpi_AK_74N": 5,
                        "SAW_lMG_K_7_62mm": 2,
                    },
                    "replace": {
                        "RocketInf_RPG7VR_64mm": [
                            {
                                "new_weapon": "SAW_lMG_K_7_62mm",
                                "swap_fire_effect": True,
                                "depiction_baked_in": False,
                            },
                            {
                                "new_weapon": "RocketInf_RPG29_105mm",
                                "swap_fire_effect": True,
                                "depiction_baked_in": False,
                            },
                        ],
                    },
                },
            },
        }
        with patch(
            "src.data.infantry_small_arms_strength_validation.NEW_UNITS",
            {("MotSchutzen_DDR", 0): new_unit_data},
        ):
            balance = build_infantry_small_arms_balance(game_db)
        entry = balance["MotSchutzen_RPG29_DDR"]
        self.assertEqual(entry["small_arms_total"], 7)
        self.assertEqual(entry["expected_small_arms"], 7)
        self.assertFalse(validate_infantry_small_arms_vs_strength(game_db, balance))

    @patch("src.data.infantry_small_arms_strength_validation.load_unit_edits")
    def test_hmg_team_not_in_balance(self, mock_load_edits):
        mock_load_edits.return_value = {
            "HMGteam_MG3_RFA": {"strength": 3, "UnitRole": "infantry"},
        }
        game_db = _minimal_game_db(
            unit_data={"HMGteam_MG3_RFA": {"unit_role": "infantry", "strength": 3}},
            weapons={
                "WeaponDescriptor_HMGteam_MG3_RFA": {
                    "turrets": {
                        "0": {
                            "weapons": {
                                "MMG_team_7_62mm_MG3": {"quantity": 1},
                            },
                        },
                    },
                },
            },
            ammo_properties={
                "Ammo_MMG_team_7_62mm_MG3": {
                    "MinMaxCategory": "MinMax_MMG_HMG",
                },
            },
        )
        with patch(
            "src.data.infantry_small_arms_strength_validation.NEW_UNITS",
            {},
        ):
            balance = build_infantry_small_arms_balance(game_db)
        self.assertNotIn("HMGteam_MG3_RFA", balance)

    @patch("src.data.infantry_small_arms_strength_validation.NEW_UNITS", {})
    @patch("src.data.infantry_small_arms_strength_validation.load_unit_edits")
    def test_recoilless_emplacement_team_skipped(self, mock_load_edits):
        mock_load_edits.return_value = {
            "RCL_L6_Wombat_UK": {"strength": 5, "UnitRole": "infantry"},
        }
        game_db = _minimal_game_db(
            unit_data={"RCL_L6_Wombat_UK": {"unit_role": "infantry", "strength": 5}},
            weapons={
                "WeaponDescriptor_RCL_L6_Wombat_UK": {
                    "turrets": {
                        "0": {
                            "weapons": {
                                "RocketInf_WOMBAT_RCL_120mm": {"quantity": 1},
                                "RocketInf_WOMBAT_RCL_120mm_HE": {"quantity": 1},
                            },
                        },
                    },
                },
            },
            ammo_properties={
                "Ammo_RocketInf_WOMBAT_RCL_120mm": {
                    "MinMaxCategory": "MinMax_CanonAP",
                },
                "Ammo_RocketInf_WOMBAT_RCL_120mm_HE": {
                    "MinMaxCategory": "MinMax_CanonAP",
                },
            },
        )
        balance = build_infantry_small_arms_balance(game_db)
        self.assertNotIn("RCL_L6_Wombat_UK", balance)

    @patch("src.data.infantry_small_arms_strength_validation.NEW_UNITS", {})
    @patch("src.data.infantry_small_arms_strength_validation.load_unit_edits")
    def test_portable_metis_squad_validated(self, mock_load_edits):
        mock_load_edits.return_value = {
            "DShV_Metis_SOV": {"UnitRole": "infantry", "strength": 8},
        }
        game_db = _minimal_game_db(
            unit_data={"DShV_Metis_SOV": {"unit_role": "infantry", "strength": 8}},
            weapons={
                "WeaponDescriptor_DShV_Metis_SOV": {
                    "turrets": {
                        "0": {"weapons": {"FM_AKS_74": {"quantity": 7}}},
                        "1": {"weapons": {"SAW_RPK_74_5_56mm": {"quantity": 1}}},
                        "2": {"weapons": {"ATGM_9K115_Metis": {"quantity": 1}}},
                    },
                },
            },
            ammo_properties={
                "Ammo_FM_AKS_74": _sa_props(),
                "Ammo_SAW_RPK_74_5_56mm": _sa_props(),
                "Ammo_ATGM_9K115_Metis": {"MinMaxCategory": "MinMax_ATGM"},
            },
        )
        balance = build_infantry_small_arms_balance(game_db)
        entry = balance["DShV_Metis_SOV"]
        self.assertEqual(entry["small_arms_total"], 8)
        self.assertEqual(entry["expected_small_arms"], 8)
        self.assertEqual(entry["occupied_slots"], 0)
        self.assertFalse(validate_infantry_small_arms_vs_strength(game_db, balance))

    @patch("src.data.infantry_small_arms_strength_validation.NEW_UNITS", {})
    @patch("src.data.infantry_small_arms_strength_validation.load_unit_edits")
    def test_portable_dragon_squad_validated(self, mock_load_edits):
        mock_load_edits.return_value = {
            "Engineers_Dragon_US": {"UnitRole": "infantry", "strength": 10},
        }
        game_db = _minimal_game_db(
            unit_data={
                "Engineers_Dragon_US": {"unit_role": "infantry", "strength": 10},
            },
            weapons={
                "WeaponDescriptor_Engineers_Dragon_US": {
                    "turrets": {
                        "0": {"weapons": {"FM_M16": {"quantity": 10}}},
                        "1": {"weapons": {"M47_DRAGON_II": {"quantity": 1}}},
                    },
                },
            },
            ammo_properties={
                "Ammo_FM_M16": _sa_props(),
                "Ammo_M47_DRAGON_II": {"MinMaxCategory": "MinMax_ATGM"},
            },
        )
        balance = build_infantry_small_arms_balance(game_db)
        entry = balance["Engineers_Dragon_US"]
        self.assertEqual(entry["small_arms_total"], 10)
        self.assertEqual(entry["expected_small_arms"], 10)
        self.assertFalse(validate_infantry_small_arms_vs_strength(game_db, balance))

    @patch("src.data.infantry_small_arms_strength_validation.NEW_UNITS", {})
    @patch("src.data.infantry_small_arms_strength_validation.load_unit_edits")
    def test_milan_only_team_skipped(self, mock_load_edits):
        mock_load_edits.return_value = {
            "ATteam_Milan_1_UK": {"UnitRole": "infantry", "strength": 2},
        }
        game_db = _minimal_game_db(
            unit_data={"ATteam_Milan_1_UK": {"unit_role": "infantry", "strength": 2}},
            weapons={
                "WeaponDescriptor_ATteam_Milan_1_UK": {
                    "turrets": {
                        "0": {"weapons": {"ATGM_MILAN": {"quantity": 1}}},
                    },
                },
            },
            ammo_properties={
                "Ammo_ATGM_MILAN": {"MinMaxCategory": "MinMax_ATGM"},
            },
        )
        balance = build_infantry_small_arms_balance(game_db)
        self.assertNotIn("ATteam_Milan_1_UK", balance)


if __name__ == "__main__":
    unittest.main()
