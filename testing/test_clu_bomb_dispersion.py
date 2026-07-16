"""Tests for CLU bomb dispersion precomputation."""

import unittest

from src.data.constants_precomputation import build_clu_bomb_dispersion


class TestCluBombDispersion(unittest.TestCase):
    def test_rockeye_salvo8_ratio_from_constants_radius(self):
        game_db = {
            "ammunition": {
                "ammo_properties": {
                    "Ammo_Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength8": {
                        "RadiusSplashPhysicalDamagesGRU": 117,
                    },
                },
            },
        }
        result = build_clu_bomb_dispersion(game_db)
        entry = result["Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength8"]
        self.assertEqual(entry["DispersionAtMaxRangeGRU"], 130)
        self.assertEqual(entry["DispersionAtMinRangeGRU"], 130)

    def test_mw1_dispenser_explicit_dispersion(self):
        game_db = {"ammunition": {"ammo_properties": {}}}
        result = build_clu_bomb_dispersion(game_db)
        entry = result["MW1_dispenser"]
        self.assertEqual(entry["DispersionAtMaxRangeGRU"], 80)
        self.assertEqual(entry["DispersionAtMinRangeGRU"], 80)

    def test_rockeye_salvo2_uses_tighter_ratio(self):
        game_db = {"ammunition": {"ammo_properties": {}}}
        result = build_clu_bomb_dispersion(game_db)
        entry = result["Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength2"]
        # RadiusSplashPhysicalDamagesGRU = 100; salvolength2 ratio = 0.7
        self.assertEqual(entry["DispersionAtMaxRangeGRU"], 70)
        self.assertEqual(entry["DispersionAtMinRangeGRU"], 70)


if __name__ == "__main__":
    unittest.main()
