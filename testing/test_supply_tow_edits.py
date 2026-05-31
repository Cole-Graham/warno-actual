"""Tests for supply unit tow-capable edits and depiction registration."""

import unittest

from src.constants.unit_edits import load_depiction_edits
from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits

SUPPLY_TOW_UNITS = [
    "CUCV_US",
    "LAV_L_US",
    "M812_supply_US",
    "HEMTT_US",
    "AEC_Militant_UK",
    "Bedford_TM_6x6_supply_UK",
    "DaimlerBenz_Typ1017_supply_RFA",
    "MAN_Kat_6x6_RFA",
]

MECHANIZED_SUPPLY_UNITS = [
    "M113A1G_supply_RFA",
    "M113A2_supply_US",
    "FV432_supply_UK",
    "MTLB_supply_DDR",
    "MTLB_supply_SOV",
    "M992A2_supply_US",
    "M548A2_supply_US",
    "PTS_2_Naval_supply_SOV",
    "PTS_M_supply_POL",
    "PTS_M_supply_DDR",
]

_REQUIRED_TOW_ORDERS = {
    "EOrderType/UnloadFromTransport",
    "EOrderType/UnloadAtPosition",
    "EOrderType/Load",
}


class TestSupplyTowEdits(unittest.TestCase):
    def test_supply_unit_edits_have_tow_block(self):
        for unit_name in SUPPLY_TOW_UNITS:
            edits = supply_unit_edits[unit_name]
            self.assertTrue(edits.get("tow_only"), unit_name)
            add_orders = set(edits.get("orders", {}).get("add_orders", []))
            self.assertTrue(_REQUIRED_TOW_ORDERS <= add_orders, unit_name)
            specs = edits.get("SpecialtiesList", {}).get("add_specs", [])
            self.assertIn("'_transport2'", specs, unit_name)

    def test_mechanized_supply_units_are_not_tow_capable(self):
        for unit_name in MECHANIZED_SUPPLY_UNITS:
            edits = supply_unit_edits[unit_name]
            self.assertFalse(edits.get("tow_only"), unit_name)
            add_orders = set(edits.get("orders", {}).get("add_orders", []))
            self.assertFalse(_REQUIRED_TOW_ORDERS & add_orders, unit_name)

    def test_m113a2_supply_keeps_upgrade_from(self):
        self.assertEqual(
            supply_unit_edits["M113A2_supply_US"]["UpgradeFromUnit"],
            "M1038_Humvee_supply_US",
        )

    def test_depiction_edits_register_towed_generator(self):
        depiction_edits = load_depiction_edits()
        for unit_name in SUPPLY_TOW_UNITS:
            self.assertIn(unit_name, depiction_edits, unit_name)
            vehicle_edits = depiction_edits[unit_name]["DepictionVehicles_ndf"]
            registration = vehicle_edits[(None, "TacticVehicleDepictionRegistration")]
            self.assertIn("SubDepictionGenerators", registration, unit_name)
            self.assertIn(
                "TowedUnitSubDepictionGenerator",
                registration["SubDepictionGenerators"],
                unit_name,
            )


if __name__ == "__main__":
    unittest.main()
