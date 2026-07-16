"""Tests for ATGM infantry team strength pattern helpers."""

import unittest
from unittest.mock import MagicMock

from src.constants.unit_edits.standards.pattern.atgm_infantry_team_strength import (
    ATGM_INFANTRY_TEAM_STRENGTH_PATTERN_STANDARD,
    ATGM_TYPE_CATEGORY_TOKEN,
)
from src.gameplay_mods.generated.gameplay.gfx.unite_descriptor.handlers.atgm_infantry_team_strength import (
    apply_strength_to_atgm_team_unit,
    is_at_team_unit,
    resolve_strength_for_specialties,
    unit_has_anti_tank_missile_mount,
)


def _specialties_list(*tags: str) -> MagicMock:
    specialties = MagicMock()
    tag_mocks = []
    for tag in tags:
        row = MagicMock()
        row.v = f"'{tag}'"
        tag_mocks.append(row)
    specialties.v = tag_mocks
    return specialties


class TestAtgmInfantryTeamStrengthHelpers(unittest.TestCase):
    def test_constants(self):
        std = ATGM_INFANTRY_TEAM_STRENGTH_PATTERN_STANDARD
        self.assertEqual(std["veryheavy_strength"], 4)
        self.assertEqual(std["default_strength"], 3)
        self.assertEqual(std["type_category_token"], ATGM_TYPE_CATEGORY_TOKEN)
        self.assertEqual(ATGM_TYPE_CATEGORY_TOKEN, "JTOYRAARTS")

    def test_is_at_team_by_flag_and_name(self):
        self.assertTrue(is_at_team_unit("ATteam_TOW_US", {"is_at_team": True}))
        self.assertTrue(is_at_team_unit("Atteam_Fagot_DDR", {}))
        self.assertTrue(is_at_team_unit("ATteam_Faktoriya_SOV", None))
        self.assertFalse(is_at_team_unit("MotRifles_Metis_SOV", {}))
        self.assertFalse(is_at_team_unit("Engineers_Dragon_US", {"is_at_team": False}))

    def test_strength_tier_from_specialty(self):
        self.assertEqual(
            resolve_strength_for_specialties(
                _specialties_list("infantry_equip_veryheavy"),
            ),
            4,
        )
        self.assertEqual(
            resolve_strength_for_specialties(
                _specialties_list("infantry_equip_heavy"),
            ),
            3,
        )
        self.assertEqual(resolve_strength_for_specialties(_specialties_list()), 3)

    def test_mount_detection_atgm_vs_recoilless(self):
        game_db = {
            "weapons": {
                "WeaponDescriptor_ATteam_TOW_US": {
                    "turrets": {
                        "0": {"weapons": {"ATGM_BGM71_TOW": {}}},
                    },
                },
                "WeaponDescriptor_ATteam_CarlGustav_UK": {
                    "turrets": {
                        "0": {"weapons": {"RocketInf_Carl_Gustav": {}}},
                    },
                },
                "WeaponDescriptor_ATteam_RCL_SPG9_SOV": {
                    "turrets": {
                        "0": {
                            "weapons": {
                                "Canon_HEAT_73_mm_SPG9_TOWED": {},
                                "Canon_HE_73_mm_SPG9_TOWED": {},
                            },
                        },
                    },
                },
            },
            "ammunition": {
                "ammo_properties": {
                    "Ammo_ATGM_BGM71_TOW": {
                        "TypeCategoryName": {
                            "Token": "JTOYRAARTS",
                            "Value": "ANTI-TANK MISSILE",
                        },
                    },
                    "Ammo_RocketInf_Carl_Gustav": {
                        "TypeCategoryName": {
                            "Token": "NZWXQNJFDX",
                            "Value": "ANTI-TANK ROCKET LAUNCH.",
                        },
                    },
                    "Ammo_Canon_HEAT_73_mm_SPG9_TOWED": {
                        "TypeCategoryName": {
                            "Token": "FIQMEQMUTK",
                            "Value": "TANK GUN",
                        },
                    },
                    "Ammo_Canon_HE_73_mm_SPG9_TOWED": {
                        "TypeCategoryName": {
                            "Token": "FIQMEQMUTK",
                            "Value": "TANK GUN",
                        },
                    },
                },
            },
        }
        self.assertTrue(
            unit_has_anti_tank_missile_mount("ATteam_TOW_US", game_db),
        )
        self.assertFalse(
            unit_has_anti_tank_missile_mount("ATteam_CarlGustav_UK", game_db),
        )
        self.assertFalse(
            unit_has_anti_tank_missile_mount("ATteam_RCL_SPG9_SOV", game_db),
        )

    def test_mount_detection_with_replace_and_donor(self):
        game_db = {
            "weapons": {
                "WeaponDescriptor_ATteam_Fagot_SOV": {
                    "turrets": {
                        "0": {"weapons": {"ATGM_9K111_Fagot": {}}},
                    },
                },
            },
            "ammunition": {
                "ammo_properties": {
                    "Ammo_ATGM_9K111_Fagot": {
                        "TypeCategoryName": {
                            "Token": "JTOYRAARTS",
                            "Value": "ANTI-TANK MISSILE",
                        },
                    },
                    "Ammo_ATGM_9K111M_Fagot_M": {
                        "TypeCategoryName": {
                            "Token": "JTOYRAARTS",
                            "Value": "ANTI-TANK MISSILE",
                        },
                    },
                },
            },
        }
        edits = {
            "WeaponDescriptor": {
                "equipmentchanges": {
                    "replace": {
                        "ATGM_9K111_Fagot": {
                            "new_weapon": "ATGM_9K111M_Faktoriya",
                            "swap_fire_effect": False,
                            "depiction_baked_in": True,
                        },
                    },
                },
            },
        }
        self.assertTrue(
            unit_has_anti_tank_missile_mount(
                "ATteam_Faktoriya_SOV",
                game_db,
                edits=edits,
                donor_name="ATteam_Fagot_SOV",
            ),
        )


class TestApplyStrengthModules(unittest.TestCase):
    def test_writes_base_damage_without_squad_module(self):
        """Weapon teams (AT/HMG) have HP on TBaseDamageModuleDescriptor only."""
        max_hp = MagicMock()
        max_hp.v = "2"

        base_damage_mod = MagicMock()
        base_damage_mod.v.by_m.return_value = max_hp

        modules_list = MagicMock()

        def find_side_effect(ndf_list, obj_type):
            if obj_type == "TBaseDamageModuleDescriptor":
                return base_damage_mod
            return None

        logger = MagicMock()
        with unittest.mock.patch(
            "src.gameplay_mods.generated.gameplay.gfx.unite_descriptor.handlers"
            ".atgm_infantry_team_strength.find_obj_by_type",
            side_effect=find_side_effect,
        ):
            ok = apply_strength_to_atgm_team_unit(
                logger, "ATteam_TOW_US", modules_list, 4,
            )

        self.assertTrue(ok)
        self.assertEqual(max_hp.v, "4")

    def test_writes_soldier_count_when_squad_present(self):
        soldier = MagicMock()
        soldier.v = "8"
        max_hp = MagicMock()
        max_hp.v = "8"

        squad_mod = MagicMock()
        squad_mod.v.by_m.return_value = soldier
        base_damage_mod = MagicMock()
        base_damage_mod.v.by_m.return_value = max_hp

        modules_list = MagicMock()

        def find_side_effect(ndf_list, obj_type):
            if obj_type == "TInfantrySquadModuleDescriptor":
                return squad_mod
            if obj_type == "TBaseDamageModuleDescriptor":
                return base_damage_mod
            return None

        logger = MagicMock()
        with unittest.mock.patch(
            "src.gameplay_mods.generated.gameplay.gfx.unite_descriptor.handlers"
            ".atgm_infantry_team_strength.find_obj_by_type",
            side_effect=find_side_effect,
        ):
            ok = apply_strength_to_atgm_team_unit(
                logger, "SomeInfantry_SOV", modules_list, 3,
            )

        self.assertTrue(ok)
        self.assertEqual(soldier.v, "3")
        self.assertEqual(max_hp.v, "3")


if __name__ == "__main__":
    unittest.main()
