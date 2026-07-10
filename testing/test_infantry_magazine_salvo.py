"""Tests for infantry AT/AA magazine salvolength helpers."""

from __future__ import annotations

import unittest

from src.data.infantry_magazine_salvo import (
    INFANTRY_MAGAZINE_CATEGORIES,
    _vanilla_salves_for_ammo,
    existing_vehicle_salvo_lengths,
    is_dedicated_weapon_team_unit,
    is_infantry_magazine_category,
    magazine_ammo_name,
    magazine_suffix_kind,
    parse_magazine_length,
    shared_salvo_index_companions,
    strip_magazine_suffixes,
    unify_shared_pool_magazine_length,
    _salves_override_for_ammo,
)


class InfantryMagazineSalvoTests(unittest.TestCase):
    def test_strip_and_parse_suffixes(self) -> None:
        self.assertEqual(strip_magazine_suffixes("RocketInf_RPG7_salvolength6"), "RocketInf_RPG7")
        self.assertEqual(strip_magazine_suffixes("MANPAD_FIM92_infmagazine8"), "MANPAD_FIM92")
        self.assertEqual(parse_magazine_length("RocketInf_RPG7_salvolength6"), 6)
        self.assertIsNone(parse_magazine_length("RocketInf_RPG7"))

    def test_dedicated_team_names(self) -> None:
        self.assertTrue(is_dedicated_weapon_team_unit("MANPAD_Stinger_C_US"))
        self.assertTrue(is_dedicated_weapon_team_unit("ATteam_Milan_1_UK"))
        self.assertTrue(is_dedicated_weapon_team_unit("HMGteam_M60_US"))
        self.assertFalse(is_dedicated_weapon_team_unit("MANPAD_Stinger_C_Rifles_US"))
        self.assertFalse(is_dedicated_weapon_team_unit("Rifles_US"))

    def test_collision_uses_infmagazine(self) -> None:
        # TOW has vehicle SalvoLengths including 8
        lengths = existing_vehicle_salvo_lengths("ATGM_BGM71D_TOW_2")
        self.assertIn(8, lengths)
        self.assertEqual(magazine_suffix_kind("ATGM_BGM71D_TOW_2", 8), "infmagazine")
        self.assertEqual(
            magazine_ammo_name("ATGM_BGM71D_TOW_2", 8),
            "ATGM_BGM71D_TOW_2_infmagazine8",
        )

    def test_rocketinf_uses_salvolength(self) -> None:
        self.assertEqual(magazine_suffix_kind("RocketInf_RPG7VL", 6), "salvolength")
        self.assertEqual(
            magazine_ammo_name("RocketInf_RPG7VL", 6),
            "RocketInf_RPG7VL_salvolength6",
        )

    def test_salves_override_ignores_replace_donor(self) -> None:
        edits = {
            "WeaponDescriptor": {
                "Salves": {
                    "MMG_inf_M240B_7_62mm": 30,
                    "FM_M16": 11,
                },
                "equipmentchanges": {
                    "replace": {
                        "MMG_inf_M240B_7_62mm": {
                            "new_weapon": "M47_DRAGON_II",
                        },
                    },
                },
            },
        }
        self.assertIsNone(_salves_override_for_ammo(edits, "M47_DRAGON_II"))
        edits["WeaponDescriptor"]["Salves"]["M47_DRAGON_II"] = 6
        self.assertEqual(_salves_override_for_ammo(edits, "M47_DRAGON_II"), 6)

    def test_salves_override_reads_magazine_key_suffix(self) -> None:
        edits = {
            "WeaponDescriptor": {
                "Salves": {
                    "M47_DRAGON_II_salvolength8": 1,
                },
            },
        }
        self.assertEqual(_salves_override_for_ammo(edits, "M47_DRAGON_II"), 8)

    def test_salves_override_shared_pool_companions(self) -> None:
        edits = {
            "WeaponDescriptor": {
                "Salves": {
                    "RocketInf_M67_RCL_90mm_salvolength8": 1,
                },
            },
        }
        companions = {
            "RocketInf_M67_RCL_90mm",
            "RocketInf_M67_RCL_90mm_HE",
        }
        self.assertEqual(
            _salves_override_for_ammo(
                edits,
                "RocketInf_M67_RCL_90mm_HE",
                companions,
            ),
            8,
        )

    def test_unify_shared_pool_magazine_length(self) -> None:
        self.assertEqual(unify_shared_pool_magazine_length([6, 8]), 8)
        self.assertEqual(unify_shared_pool_magazine_length([8, None]), 8)  # type: ignore[list-item]
        self.assertIsNone(unify_shared_pool_magazine_length([1, 0]))
        self.assertIsNone(unify_shared_pool_magazine_length([]))

    def test_shared_salvo_index_companions_m67(self) -> None:
        import json
        from pathlib import Path

        weapons = json.loads(
            Path("src/data/database/weapons.json").read_text(encoding="utf-8"),
        )
        game_db = {"weapons": weapons, "ammunition": {}}
        companions = shared_salvo_index_companions(
            "LightRifles_RCL_US",
            "RocketInf_M67_RCL_90mm",
            game_db,
        )
        self.assertIn("RocketInf_M67_RCL_90mm", companions)
        self.assertIn("RocketInf_M67_RCL_90mm_HE", companions)

    def test_napalm_rpo_is_magazine_category(self) -> None:
        self.assertIn("napalm", INFANTRY_MAGAZINE_CATEGORIES)
        self.assertTrue(is_infantry_magazine_category("RocketInf_RPO_RYS"))
        self.assertTrue(is_infantry_magazine_category("RocketInf_RPO_A_93mm"))

    def test_vanilla_salves_resolves_metis_rename(self) -> None:
        """Vanilla mounts keep Metis_M; constants use renamed Metis."""
        import json
        from pathlib import Path

        weapons = json.loads(
            Path("src/data/database/weapons.json").read_text(encoding="utf-8"),
        )
        game_db = {"weapons": weapons, "ammunition": {}}
        self.assertEqual(
            _vanilla_salves_for_ammo(
                "Luftsturmjager_Metis_DDR",
                None,
                "ATGM_9K115_Metis",
                game_db,
            ),
            6,
        )


if __name__ == "__main__":
    unittest.main()
