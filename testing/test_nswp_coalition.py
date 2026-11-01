"""NSWP coalition divisions combine member nation rule tables."""

import unittest
from pathlib import Path

from src.constants.generated.gameplay.decks import load_new_divisions
from src.constants.generated.gameplay.decks.new_divisions.NSWP_new_divs import (
    NSWP_COALITION,
    nswp_new_divs,
)
from src.constants.generated.gameplay.decks.new_divisions.POL_new_divs import pol_new_divs
from src.constants.generated.gameplay.decks.new_divisions.RDA_new_divs import rda_new_divs
from src.constants.generated.gameplay.decks.new_divisions.TCH_new_divs import tch_new_divs
from src.constants.generated.gameplay.decks.new_divisions.new_divisionrules import (
    RDA_airborne_newdivisionrules,
    RDA_armored_newdivisionrules,
    RDA_global_newdivisionrules,
    TCH_airborne_newdivisionrules,
    TCH_armored_newdivisionrules,
    TCH_global_newdivisionrules,
    TCH_mechanized_newdivisionrules,
    TCH_motorized_newdivisionrules,
)
from src.constants.generated.gameplay.decks.new_divisions.new_divisionrules.POL_newdivisionrules import (
    POL_airborne_newdivisionrules,
    POL_global_newdivisionrules,
    POL_marines_newdivisionrules,
)

_EMBLEM_DIR = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "gameplaymod"
    / "2d"
    / "interface"
    / "useoutgame"
    / "division"
    / "emblem"
)


def _primary_units(rule_dicts):
    names = set()
    for rules_dict in rule_dicts:
        for rows in rules_dict.values():
            if not isinstance(rows, list):
                continue
            for row in rows:
                if isinstance(row, tuple) and row and isinstance(row[0], str):
                    names.add(row[0])
    return names


class TestNswpCoalition(unittest.TestCase):
    def test_source_declares_coalition_without_copying_rules(self):
        general = nswp_new_divs["NSWP_general"]
        self.assertEqual(general["coalition"], NSWP_COALITION)
        self.assertNotIn("division_rules", general)
        self.assertEqual(general["emblem"], "NSWP_all")

    def test_loader_combines_member_rule_tables(self):
        loaded = load_new_divisions()
        self.assertIn("NSWP_general", loaded)
        self.assertNotIn("RDA_general", loaded)
        self.assertNotIn("POL_general", loaded)
        self.assertNotIn("TCH_general", loaded)
        self.assertNotIn("division_rules", nswp_new_divs["NSWP_general"])

        general_rules = loaded["NSWP_general"]["division_rules"]
        self.assertIs(general_rules[0], RDA_airborne_newdivisionrules)
        self.assertIs(general_rules[1], RDA_armored_newdivisionrules)
        self.assertIn(POL_airborne_newdivisionrules, general_rules)
        self.assertIn(TCH_airborne_newdivisionrules, general_rules)
        self.assertIn(RDA_global_newdivisionrules, general_rules)
        self.assertIn(POL_global_newdivisionrules, general_rules)
        self.assertIn(TCH_global_newdivisionrules, general_rules)
        self.assertIn(TCH_mechanized_newdivisionrules, general_rules)
        self.assertIn(TCH_motorized_newdivisionrules, general_rules)
        self.assertNotIn(POL_marines_newdivisionrules, general_rules)

        airborne_rules = loaded["NSWP_airborne"]["division_rules"]
        self.assertIn(RDA_airborne_newdivisionrules, airborne_rules)
        self.assertIn(TCH_airborne_newdivisionrules, airborne_rules)
        self.assertIn(RDA_global_newdivisionrules, airborne_rules)
        self.assertNotIn(RDA_armored_newdivisionrules, airborne_rules)
        self.assertNotIn(TCH_armored_newdivisionrules, airborne_rules)

        ids = []
        for table in (loaded, rda_new_divs, pol_new_divs, tch_new_divs):
            for div_data in table.values():
                if isinstance(div_data, dict) and "division_id" in div_data:
                    ids.append(div_data["division_id"])
        self.assertEqual(len(ids), len(set(ids)))

    def test_standouts_and_emblem_files(self):
        loaded = load_new_divisions()
        nswp = {key: data for key, data in loaded.items() if key.startswith("NSWP_")}
        self.assertEqual(len(nswp), 10)
        for div_key, div_data in nswp.items():
            present = _primary_units(div_data["division_rules"])
            for unit in div_data["standout_units"]:
                self.assertIn(unit, present, div_key)
            emblem_path = _EMBLEM_DIR / f"{div_data['emblem']}.png"
            self.assertTrue(emblem_path.is_file(), emblem_path.name)

    def test_exclusions_and_transport_overrides_merge_rda_and_pol(self):
        live_types = set()
        for table in (rda_new_divs, pol_new_divs):
            for nation_key in table:
                live_types.add(nation_key.split("_", 1)[1])

        for div_type in sorted(live_types):
            nswp = nswp_new_divs.get(f"NSWP_{div_type}")
            if nswp is None:
                continue
            exclusions = []
            overrides = {}
            for table, prefix in ((rda_new_divs, "RDA"), (pol_new_divs, "POL")):
                nation = table.get(f"{prefix}_{div_type}", {})
                for unit in nation.get("rule_exclusions", []):
                    if unit not in exclusions:
                        exclusions.append(unit)
                overrides.update(nation.get("transport_overrides", {}))
            if exclusions:
                self.assertEqual(nswp["rule_exclusions"], exclusions, div_type)
            else:
                self.assertNotIn("rule_exclusions", nswp, div_type)
            if overrides:
                self.assertEqual(nswp["transport_overrides"], overrides, div_type)
            else:
                self.assertNotIn("transport_overrides", nswp, div_type)

        for div_data in nswp_new_divs.values():
            for unit in div_data.get("rule_exclusions", []):
                self.assertFalse(unit.endswith("_TCH"), unit)
            for unit in div_data.get("transport_overrides", {}):
                self.assertFalse(unit.endswith("_TCH"), unit)

        airborne_armored = nswp_new_divs["NSWP_airborne_armored"]
        self.assertEqual(
            airborne_armored["rule_exclusions"],
            [
                "BRDM_2_CMD_DDR",
                "BTR_50_CMD2_DDR",
                "HMGteam_PKM_DDR",
                "ATteam_RCL_SPG9_DDR",
                "ATteam_Fagot_DDR",
                "ATteam_FagotM_DDR",
                "ATteam_Konkurs_DDR",
                "MANPAD_Strela_2M_DDR",
                "HMGteam_PKM_POL",
                "HMGteam_NSV_POL",
                "HMGteam_AGS17_POL",
                "DCA_ZU_23_2_POL",
            ],
        )
        self.assertEqual(
            set(airborne_armored["transport_overrides"]),
            {"MotRifles_CMD2_DDR", "Rifles_CMD2_POL"},
        )
        self.assertEqual(
            set(nswp_new_divs["NSWP_armored_mechanized"]["transport_overrides"]),
            {
                "MotRifles_CMD2_DDR",
                "MotRifles_DDR",
                "MotRifles_HMG_DDR",
                "MotRifles_RPG27_DDR",
                "MotSchutzen_DDR",
                "MotSchutzen_RPG29_DDR",
                "Rifles_CMD2_POL",
            },
        )
        self.assertEqual(
            len(nswp_new_divs["NSWP_armored_motorized"]["transport_overrides"]),
            9,
        )

        loaded = load_new_divisions()
        self.assertEqual(
            loaded["NSWP_general"]["rule_exclusions"],
            nswp_new_divs["NSWP_general"]["rule_exclusions"],
        )
        self.assertEqual(
            loaded["NSWP_mechanized_motorized"]["transport_overrides"],
            nswp_new_divs["NSWP_mechanized_motorized"]["transport_overrides"],
        )

    def test_tch_rule_tables_only_list_moderna(self):
        self.assertEqual(
            TCH_armored_newdivisionrules["tank"],
            [("T72M2_Moderna_TCH", 2, [0, 6, 4, 0])],
        )
        armored_without_tank = {
            key: rows
            for key, rows in TCH_armored_newdivisionrules.items()
            if key != "tank"
        }
        self.assertEqual(_primary_units([armored_without_tank]), set())
        for rules_dict in (
            TCH_airborne_newdivisionrules,
            TCH_global_newdivisionrules,
            TCH_mechanized_newdivisionrules,
            TCH_motorized_newdivisionrules,
        ):
            self.assertTrue(rules_dict)
            self.assertEqual(_primary_units([rules_dict]), set())


if __name__ == "__main__":
    unittest.main()
