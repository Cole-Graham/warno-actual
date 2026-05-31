"""Tests for supply transport variants and new-unit vehicle depiction patches."""

import unittest

from src.constants.new_units import NEW_UNITS
from src.constants.new_units.new_depictions import NEW_DEPICTIONS
from src.constants.new_units.new_depictions._supply_transport import towed_supply_vehicle_depiction
from src.constants.supply_transport_variants import (
    SUPPLY_TRANSPORT_VARIANT_CONFIG,
    build_supply_transport_new_units,
    compute_transport_stats,
    make_supply_transport_name,
)
from src.gameplay_mods.generated.gameplay.gfx.depictions import depictionvehicles
from src.gameplay_mods.generated.gameplay.gfx.depictions.depictionvehicles import (
    _mesh_stem_for_subdepiction_generator,
)


class TestSupplyTransportStats(unittest.TestCase):
    def test_command_points_are_multiples_of_five(self):
        for donor in SUPPLY_TRANSPORT_VARIANT_CONFIG:
            entry = build_supply_transport_new_units()[(donor, 0)]
            self.assertEqual(entry["CommandPoints"] % 5, 0, donor)

    def test_bedford_transport_cp_is_30_not_28(self):
        entry = build_supply_transport_new_units()[("Bedford_MJ_4t_UK", 0)]
        self.assertEqual(entry["CommandPoints"], 30)
        self.assertEqual(entry["Supply"]["SupplyCapacity"], 1000.0)

    def test_supply_dict_has_required_keys(self):
        for donor in SUPPLY_TRANSPORT_VARIANT_CONFIG:
            entry = build_supply_transport_new_units()[(donor, 0)]
            self.assertIn("Supply", entry, donor)
            self.assertIn("SupplyCapacity", entry["Supply"], donor)
            self.assertIn("SupplyDescriptor", entry["Supply"], donor)

    def test_m1038_uses_supply_dict_not_modules_add(self):
        entry = NEW_UNITS[("M1038_Humvee_US", 0)]
        self.assertIn("Supply", entry)
        self.assertEqual(entry["Supply"]["SupplyDescriptor"], "SquadSupply")
        self.assertEqual(entry["Supply"]["SupplyCapacity"], 675.0)
        self.assertEqual(entry["Supply"]["SupplyPriority"], -1)
        for module in entry.get("modules_add", []):
            self.assertNotIn("TSupplyModuleDescriptor", module)

    def test_compute_transport_stats_formula(self):
        capacity, cp = compute_transport_stats(35)
        self.assertEqual(cp, 20)
        self.assertEqual(capacity, 650.0)

    def test_make_supply_transport_name_bedford(self):
        self.assertEqual(
            make_supply_transport_name("Bedford_MJ_4t_UK"),
            "Bedford_MJ_4t_supply_trans_UK",
        )

    def test_specialties_list_includes_supply_and_transport(self):
        entry = build_supply_transport_new_units()[("Unimog_S_404_RFA", 0)]
        self.assertEqual(entry["SpecialtiesList"], ["_transport2", "_supply_squad"])
        entry = build_supply_transport_new_units()[("M35_supply_US", 0)]
        self.assertEqual(entry["SpecialtiesList"], ["_transport2", "_supply_primary"])

    def test_towed_mesh_uses_donor_for_supply_transport_clones(self):
        self.assertEqual(
            _mesh_stem_for_subdepiction_generator("M35_supply_trans_US"),
            "M35_supply_US",
        )
        self.assertEqual(
            _mesh_stem_for_subdepiction_generator("Rover_101FC_supply_trans_UK"),
            "Rover_101FC_supply_UK",
        )
        self.assertEqual(
            _mesh_stem_for_subdepiction_generator("M35_supply_US"),
            "M35_supply_US",
        )

    def test_game_name_tokens_have_no_digits(self):
        for donor in SUPPLY_TRANSPORT_VARIANT_CONFIG:
            token = SUPPLY_TRANSPORT_VARIANT_CONFIG[donor]["game_name"]["token"]
            self.assertFalse(any(c.isdigit() for c in token), f"{donor}: {token}")

    def test_all_variants_have_new_depictions(self):
        for donor in SUPPLY_TRANSPORT_VARIANT_CONFIG:
            new_name = make_supply_transport_name(donor)
            self.assertIn(
                new_name.lower(),
                NEW_DEPICTIONS,
                f"Missing NEW_DEPICTIONS for {new_name}",
            )
            depiction = NEW_DEPICTIONS[new_name.lower()]
            expected = towed_supply_vehicle_depiction(new_name)
            self.assertEqual(
                depiction["DepictionVehicles_ndf"],
                expected["DepictionVehicles_ndf"],
            )

    def test_all_variants_in_new_units(self):
        generated = build_supply_transport_new_units()
        self.assertEqual(len(generated), len(SUPPLY_TRANSPORT_VARIANT_CONFIG))
        for key, entry in generated.items():
            self.assertIn(key, NEW_UNITS)
            self.assertEqual(NEW_UNITS[key]["NewName"], entry["NewName"])
            self.assertTrue(entry.get("tow_only"))


class TestDepictionVehiclesNewUnitPatchPass(unittest.TestCase):
    def test_apply_pass_skips_string_keys(self):
        """String-key sections are for full custom NDF, not tuple-key patches."""

        class FakeList:
            def __init__(self):
                self.add_calls = 0

            def add(self, _entry):
                self.add_calls += 1

        class FakeVehicle:
            def __init__(self):
                self.v = FakeList()

        source_path = type("Source", (), {"by_n": lambda self, _n: None})()

        original_new_units = depictionvehicles.NEW_UNITS
        original_new_depictions = depictionvehicles.NEW_DEPICTIONS
        try:
            depictionvehicles.NEW_UNITS = {
                ("Donor_X", 0): {
                    "NewName": "Donor_X_trans_US",
                    "is_ground_vehicle": True,
                },
            }
            depictionvehicles.NEW_DEPICTIONS = {
                "donor_x_trans_us": {
                    "DepictionVehicles_ndf": {
                        "TacticVehicleDepictionRegistration": "raw ndf string",
                        (None, "TacticVehicleDepictionRegistration"): {
                            "SubDepictionGenerators": {
                                "TowedUnitSubDepictionGenerator": {"add": None},
                            },
                        },
                    },
                },
            }

            handle_calls = []

            def fake_find(_source, unit_name, _obj_type):
                self.assertEqual(unit_name, "Donor_X_trans_US")
                return FakeVehicle()

            def fake_handle(unit_name, vehicle_depiction, edits):
                handle_calls.append((unit_name, edits))

            depictionvehicles.find_obj_by_blackhole_key = fake_find
            depictionvehicles._handle_vehicle_depiction = fake_handle

            depictionvehicles._apply_new_unit_vehicle_depiction_edits(source_path)

            self.assertEqual(len(handle_calls), 1)
            self.assertIn("SubDepictionGenerators", handle_calls[0][1])
        finally:
            depictionvehicles.NEW_UNITS = original_new_units
            depictionvehicles.NEW_DEPICTIONS = original_new_depictions


if __name__ == "__main__":
    unittest.main()
