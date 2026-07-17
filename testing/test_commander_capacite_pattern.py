"""Tests for commander Capacite pattern classification helpers."""

import unittest

from src import ndf
from src.constants.capacities import CMD_UNIT_CAPACITY, LDR_INF_CAPACITY
from src.constants.unit_edits.standards.pattern.commander_capacite import (
    CMD_UNIT_CAPACITY_NAME,
    COMMANDER_CAPACITE_PATTERN_STANDARD,
    LDR_INF_CAPACITY_NAME,
    resolve_commander_capacite_name,
)
from src.gameplay_mods.generated.gameplay.gfx.unite_descriptor.handlers.commander_capacite import (
    _flatten_ndf_string_list,
)


class TestCommanderCapacitePatternHelpers(unittest.TestCase):
    def test_infantry_ldr_nato(self):
        self.assertEqual(
            resolve_commander_capacite_name({"Infanterie", "LDR_Unit"}),
            LDR_INF_CAPACITY_NAME,
        )

    def test_infantry_ldr_sov(self):
        self.assertEqual(
            resolve_commander_capacite_name({"Infanterie", "LDR_SOV_Unit"}),
            LDR_INF_CAPACITY_NAME,
        )

    def test_infantry_ldr_via_specialty(self):
        self.assertEqual(
            resolve_commander_capacite_name(
                {"Infanterie"},
                {"_leader"},
            ),
            LDR_INF_CAPACITY_NAME,
        )

    def test_infantry_cmd_unit_stays_cmd(self):
        self.assertEqual(
            resolve_commander_capacite_name(
                {"Infanterie", "LDR_Unit", "CMD_Unit"},
            ),
            CMD_UNIT_CAPACITY_NAME,
        )

    def test_vehicle_cmd(self):
        self.assertEqual(
            resolve_commander_capacite_name({"CMD_Unit", "Char_CMD", "Commandant"}),
            CMD_UNIT_CAPACITY_NAME,
        )

    def test_vehicle_without_cmd_tag_defaults_cmd(self):
        self.assertEqual(
            resolve_commander_capacite_name({"Char", "Commandant"}),
            CMD_UNIT_CAPACITY_NAME,
        )

    def test_ldr_vehicle_without_infanterie_is_cmd(self):
        # Tank/arty LDR should already have removed TCommander; if present, CMD_UNIT.
        self.assertEqual(
            resolve_commander_capacite_name({"LDR_Unit", "Char"}),
            CMD_UNIT_CAPACITY_NAME,
        )

    def test_standard_exports_match_names(self):
        std = COMMANDER_CAPACITE_PATTERN_STANDARD
        self.assertEqual(std["cmd_capacity"], CMD_UNIT_CAPACITY_NAME)
        self.assertEqual(std["ldr_inf_capacity"], LDR_INF_CAPACITY_NAME)

    def test_ldr_inf_forbids_artillerie_cmd_does_not(self):
        self.assertIn('"Artillerie"', LDR_INF_CAPACITY)
        self.assertNotIn('"Artillerie"', CMD_UNIT_CAPACITY)
        self.assertIn("RangeGRU = 550", LDR_INF_CAPACITY)
        self.assertIn("RangeGRU = 900", CMD_UNIT_CAPACITY)

    def test_flatten_nested_tagset_from_overwrite_convert(self):
        nested = ndf.convert(str(["AllUnits", "LDR_Unit", "Infanterie", "Unite"]))
        tags = _flatten_ndf_string_list(nested)
        self.assertEqual(tags, {"AllUnits", "LDR_Unit", "Infanterie", "Unite"})
        self.assertEqual(
            resolve_commander_capacite_name(tags),
            LDR_INF_CAPACITY_NAME,
        )


if __name__ == "__main__":
    unittest.main()
