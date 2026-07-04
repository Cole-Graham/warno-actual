import logging
import unittest
from unittest.mock import patch

from src.data.default_multi_deck_validation import (
    build_merged_division_unit_rules,
    flatten_categories_with_category,
    resolve_division_cost_matrix,
    validate_default_multi_decks,
)
from src.constants.generated.gameplay.decks import load_new_divisions


class TestDefaultMultiDeckValidation(unittest.TestCase):
    def test_build_merged_division_unit_rules_keeps_higher_card_count(self):
        div_data = {
            "division_rules": [
                {
                    "infantry": [
                        ("Test_Unit_US", 1, [0, 6, 4, 0]),
                    ],
                    "tank": [
                        ("Test_Unit_US", 3, [0, 0, 3, 2]),
                    ],
                },
            ],
        }
        merged = build_merged_division_unit_rules(div_data)
        self.assertEqual(merged["Test_Unit_US"].max_cards, 3)
        self.assertEqual(merged["Test_Unit_US"].availability, (0, 0, 3, 2))

    def test_build_merged_division_unit_rules_applies_exclusions(self):
        div_data = {
            "rule_exclusions": ["Excluded_US"],
            "division_rules": [
                {
                    "infantry": [
                        ("Excluded_US", 2, [0, 6, 4, 0]),
                        ("Allowed_US", 1, [0, 6, 4, 0]),
                    ],
                },
            ],
        }
        merged = build_merged_division_unit_rules(div_data)
        self.assertNotIn("Excluded_US", merged)
        self.assertIn("Allowed_US", merged)

    def test_resolve_division_cost_matrix_for_airborne_armored(self):
        div_key, div_data = next(
            (key, data)
            for key, data in load_new_divisions().items()
            if data.get("cfg_name") == "US_national_airborne_armored"
        )
        matrix = resolve_division_cost_matrix(div_key, div_data)
        self.assertEqual(matrix["Factory/Infantry"][:3], [2, 2, 2])
        self.assertEqual(matrix["Factory/Tanks"][-1], 4)

    def test_flatten_categories_with_category_preserves_category(self):
        categories = {
            "Tanks": [{"Descriptor_Unit_T72B1_SOV": {"vet": 1}}],
            "Logistic": [{"Descriptor_Unit_FOB_SOV": {"vet": 1}}],
        }
        flattened = flatten_categories_with_category(categories)
        self.assertEqual(flattened[0][0], "Logistic")
        self.assertEqual(flattened[1][0], "Tanks")

    def test_validate_default_multi_decks_warns_on_over_limit_activation(self):
        test_logger = logging.getLogger("test_default_multi_deck_validation_over_ap")
        with self.assertLogs(test_logger, level="WARNING") as captured:
            with patch(
                "src.data.default_multi_deck_validation.load_default_multi_decks",
                return_value={
                    "TEST_cfg": {
                        "Logistic": [
                            {"Descriptor_Unit_FOB_US": {"vet": 0}},
                            {"Descriptor_Unit_M113A2_supply_US": {"vet": 0}},
                            {"Descriptor_Unit_HEMTT_US": {"vet": 0}},
                            {"Descriptor_Unit_CH47_Super_Chinook_US": {"vet": 0}},
                            {"Descriptor_Unit_M1025_Humvee_CMD_US": {"vet": 1}},
                            {"Descriptor_Unit_M1IP_Abrams_CMD2_US": {"vet": 2}},
                            {"Descriptor_Unit_DCA_M167_Vulcan_20mm_US": {
                                "vet": 2,
                                "transport": "Descriptor_Unit_M1038_Humvee_US",
                            }},
                            {"Descriptor_Unit_M113A2_supply_US": {"vet": 0}},
                            {"Descriptor_Unit_HEMTT_US": {"vet": 0}},
                        ],
                    },
                },
            ), patch(
                "src.data.default_multi_deck_validation._divisions_by_cfg_name",
                return_value={
                    "TEST_cfg": (
                        "US_airborne_armored",
                        {
                            "cfg_name": "TEST_cfg",
                            "activation_points": 3,
                            "division_rules": [
                                {
                                    "logistic": [
                                        ("FOB_US", 9, [1, 1, 1, 1]),
                                        ("M113A2_supply_US", 9, [1, 1, 1, 1]),
                                        ("HEMTT_US", 9, [1, 1, 1, 1]),
                                        ("CH47_Super_Chinook_US", 9, [1, 1, 1, 1]),
                                        ("M1025_Humvee_CMD_US", 9, [0, 1, 1, 1]),
                                        ("M1IP_Abrams_CMD2_US", 9, [0, 0, 2, 0]),
                                        ("DCA_M167_Vulcan_20mm_US", 9, [0, 0, 2, 0], ["M1038_Humvee_US"]),
                                    ],
                                },
                            ],
                        },
                    ),
                },
            ), patch(
                "src.data.default_multi_deck_validation.resolve_division_cost_matrix",
                return_value={"Factory/Logistic": [2, 2, 2]},
            ):
                failed = validate_default_multi_decks(log=test_logger)

        self.assertTrue(failed)
        self.assertTrue(
            any("activation points" in message for message in captured.output),
        )

    def test_validate_default_multi_decks_warns_on_invalid_vet(self):
        test_logger = logging.getLogger("test_default_multi_deck_validation_invalid_vet")
        with self.assertLogs(test_logger, level="WARNING") as captured:
            with patch(
                "src.data.default_multi_deck_validation.load_default_multi_decks",
                return_value={
                    "TEST_cfg": {
                        "Infantry": [
                            {"Descriptor_Unit_Airborne_US": {"vet": 3}},
                        ],
                    },
                },
            ), patch(
                "src.data.default_multi_deck_validation._divisions_by_cfg_name",
                return_value={
                    "TEST_cfg": (
                        "US_airborne_armored",
                        {
                            "cfg_name": "TEST_cfg",
                            "activation_points": 85,
                            "division_rules": [
                                {
                                    "infantry": [
                                        ("Airborne_US", 3, [0, 6, 4, 0]),
                                    ],
                                },
                            ],
                        },
                    ),
                },
            ), patch(
                "src.data.default_multi_deck_validation.resolve_division_cost_matrix",
                return_value={"Factory/Infantry": [2, 2, 2]},
            ):
                failed = validate_default_multi_decks(log=test_logger)

        self.assertTrue(failed)
        self.assertTrue(any("vet level 3" in message for message in captured.output))

    def test_validate_default_multi_decks_warns_on_excess_card_count(self):
        test_logger = logging.getLogger("test_default_multi_deck_validation_card_count")
        with self.assertLogs(test_logger, level="WARNING") as captured:
            with patch(
                "src.data.default_multi_deck_validation.load_default_multi_decks",
                return_value={
                    "TEST_cfg": {
                        "Tanks": [
                            {"Descriptor_Unit_M1IP_Abrams_US": {"vet": 1}},
                            {"Descriptor_Unit_M1IP_Abrams_US": {"vet": 1}},
                            {"Descriptor_Unit_M1IP_Abrams_US": {"vet": 1}},
                        ],
                    },
                },
            ), patch(
                "src.data.default_multi_deck_validation._divisions_by_cfg_name",
                return_value={
                    "TEST_cfg": (
                        "US_airborne_armored",
                        {
                            "cfg_name": "TEST_cfg",
                            "activation_points": 85,
                            "division_rules": [
                                {
                                    "tank": [
                                        ("M1IP_Abrams_US", 2, [0, 6, 4, 0]),
                                    ],
                                },
                            ],
                        },
                    ),
                },
            ), patch(
                "src.data.default_multi_deck_validation.resolve_division_cost_matrix",
                return_value={"Factory/Tanks": [2, 2, 2, 2]},
            ):
                failed = validate_default_multi_decks(log=test_logger)

        self.assertTrue(failed)
        self.assertTrue(any("MaxPackNumber=2" in message for message in captured.output))

    def test_validate_default_multi_decks_warns_on_too_many_unused_activation_points(self):
        test_logger = logging.getLogger("test_default_multi_deck_validation_unused_ap")
        with self.assertLogs(test_logger, level="WARNING") as captured:
            with patch(
                "src.data.default_multi_deck_validation.load_default_multi_decks",
                return_value={
                    "TEST_cfg": {
                        "Logistic": [
                            {"Descriptor_Unit_FOB_US": {"vet": 0}},
                        ],
                    },
                },
            ), patch(
                "src.data.default_multi_deck_validation._divisions_by_cfg_name",
                return_value={
                    "TEST_cfg": (
                        "US_airborne_armored",
                        {
                            "cfg_name": "TEST_cfg",
                            "activation_points": 85,
                            "division_rules": [
                                {
                                    "logistic": [
                                        ("FOB_US", 1, [1, 1, 1, 1]),
                                    ],
                                },
                            ],
                        },
                    ),
                },
            ), patch(
                "src.data.default_multi_deck_validation.resolve_division_cost_matrix",
                return_value={"Factory/Logistic": [82]},
            ):
                failed = validate_default_multi_decks(log=test_logger)

        self.assertTrue(failed)
        self.assertTrue(any("3 unused" in message for message in captured.output))

    def test_validate_default_multi_decks_allows_up_to_two_unused_activation_points(self):
        test_logger = logging.getLogger("test_default_multi_deck_validation_two_unused_ap")
        with patch(
            "src.data.default_multi_deck_validation.load_default_multi_decks",
            return_value={
                "TEST_cfg": {
                    "Logistic": [
                        {"Descriptor_Unit_FOB_US": {"vet": 0}},
                    ],
                },
            },
        ), patch(
            "src.data.default_multi_deck_validation._divisions_by_cfg_name",
            return_value={
                "TEST_cfg": (
                    "US_airborne_armored",
                    {
                        "cfg_name": "TEST_cfg",
                        "activation_points": 85,
                        "division_rules": [
                            {
                                "logistic": [
                                    ("FOB_US", 1, [1, 1, 1, 1]),
                                ],
                            },
                        ],
                    },
                ),
            },
        ), patch(
            "src.data.default_multi_deck_validation.resolve_division_cost_matrix",
            return_value={"Factory/Logistic": [83]},
        ):
            failed = validate_default_multi_decks(log=test_logger)

        self.assertFalse(failed)

    def test_current_us_and_sov_default_decks_validate(self):
        failed = validate_default_multi_decks()
        self.assertFalse(
            failed,
            "Current US/SOV default decks should satisfy division rules and activation limits",
        )


if __name__ == "__main__":
    unittest.main()
