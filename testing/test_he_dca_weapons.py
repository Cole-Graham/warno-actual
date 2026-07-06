"""Tests for he_dca _AIR precomputation and air-only DCA direct edits."""

import json
import unittest
from pathlib import Path

from src.constants.weapons.ammunition.autocanon_dca import weapons as dca_weapons
from src.constants.weapons.spaag_air import SPAAG_AIR_AIMING_TIME, SPAAG_AIR_DAMAGE_FAMILY
from src.data.constants_precomputation import build_he_dca_weapons

_DB_PATH = Path(__file__).resolve().parents[1] / "src" / "data" / "database" / "ammunition.json"

_AIR_ONLY_DCA = (
    "DCA_1_canon_KS19_100mm",
    "DCA_1_canon_KS30_130mm",
    "DCA_1_canon_KS19_100mm_radar",
    "DCA_1_canon_KS30_130mm_radar",
)


def _load_ammo_db() -> dict:
    with open(_DB_PATH, encoding="utf-8") as f:
        return json.load(f)


class TestHeDcaWeaponsPrecompute(unittest.TestCase):
    def setUp(self):
        self.game_db = {"ammunition": _load_ammo_db()}

    def test_air_only_dca_excluded_from_auto_air_map(self):
        result = build_he_dca_weapons(self.game_db)
        for weapon_name in _AIR_ONLY_DCA:
            self.assertNotIn(
                weapon_name,
                result,
                f"{weapon_name} should not receive auto _AIR clone/mount",
            )

    def test_dual_role_spaag_included(self):
        result = build_he_dca_weapons(self.game_db)
        self.assertIn("DCA_1_canon_53T2_20mm", result)

    def test_air_only_dca_constants_have_direct_air_edits(self):
        for weapon_name in _AIR_ONLY_DCA:
            key = next(k for k in dca_weapons if k[0] == weapon_name)
            ammo = dca_weapons[key]["Ammunition"]
            self.assertEqual(
                ammo.get("Arme", {}).get("Family"),
                SPAAG_AIR_DAMAGE_FAMILY,
                weapon_name,
            )
            self.assertEqual(
                ammo.get("parent_membr", {}).get("AimingTime"),
                SPAAG_AIR_AIMING_TIME,
                weapon_name,
            )
            self.assertIn("SuppressDamages", ammo.get("parent_membr", {}), weapon_name)

    def test_ks19_and_ks30_suppress_air_values(self):
        ks19 = dca_weapons[("DCA_1_canon_KS19_100mm", "DCA", None, False)]
        ks30 = dca_weapons[("DCA_1_canon_KS30_130mm", "DCA", None, False)]
        self.assertEqual(ks19["Ammunition"]["parent_membr"]["SuppressDamages"], 80)
        self.assertEqual(ks30["Ammunition"]["parent_membr"]["SuppressDamages"], 103)


if __name__ == "__main__":
    unittest.main()
