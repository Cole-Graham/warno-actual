"""Tests for static UnitId validation on new units."""

import unittest

from src.constants.new_units import (
    MIN_NEW_UNIT_ID,
    NEW_UNITS,
    highest_new_unit_id,
    validate_unit_ids,
)


class TestValidateUnitIds(unittest.TestCase):
    def test_valid_unique_ids(self) -> None:
        units = {
            ("DonorA", 0): {"NewName": "UnitA", "UnitId": 50000},
            ("DonorB", 0): {"NewName": "UnitB", "UnitId": 50001},
            ("armor_reference", 0): {"armor": {}},
        }
        validate_unit_ids(units)

    def test_duplicate_unit_id_raises(self) -> None:
        units = {
            ("DonorA", 0): {"NewName": "UnitA", "UnitId": 50000},
            ("DonorB", 0): {"NewName": "UnitB", "UnitId": 50000},
        }
        with self.assertRaises(ValueError) as ctx:
            validate_unit_ids(units)
        self.assertIn("50000", str(ctx.exception))
        self.assertIn("UnitA", str(ctx.exception))
        self.assertIn("UnitB", str(ctx.exception))

    def test_missing_unit_id_raises(self) -> None:
        units = {
            ("DonorA", 0): {"NewName": "UnitA"},
        }
        with self.assertRaises(ValueError) as ctx:
            validate_unit_ids(units)
        self.assertIn("missing UnitId", str(ctx.exception))
        self.assertIn("UnitA", str(ctx.exception))

    def test_unit_id_below_minimum_raises(self) -> None:
        units = {
            ("DonorA", 0): {"NewName": "UnitA", "UnitId": MIN_NEW_UNIT_ID - 1},
        }
        with self.assertRaises(ValueError) as ctx:
            validate_unit_ids(units)
        self.assertIn(str(MIN_NEW_UNIT_ID), str(ctx.exception))

    def test_non_int_unit_id_raises(self) -> None:
        units = {
            ("DonorA", 0): {"NewName": "UnitA", "UnitId": "50000"},
        }
        with self.assertRaises(ValueError) as ctx:
            validate_unit_ids(units)
        self.assertIn("must be an int", str(ctx.exception))

    def test_loaded_new_units_pass_validation(self) -> None:
        validate_unit_ids(NEW_UNITS)

    def test_highest_new_unit_id(self) -> None:
        units = {
            ("DonorA", 0): {"NewName": "UnitA", "UnitId": 50010},
            ("DonorB", 0): {"NewName": "UnitB", "UnitId": 50050},
            ("ref", 0): {},
        }
        self.assertEqual(highest_new_unit_id(units), 50050)
        self.assertEqual(highest_new_unit_id({}), None)
        expected = max(
            edits["UnitId"]
            for edits in NEW_UNITS.values()
            if isinstance(edits, dict) and "UnitId" in edits
        )
        self.assertEqual(highest_new_unit_id(NEW_UNITS), expected)
        self.assertGreaterEqual(expected, MIN_NEW_UNIT_ID)


if __name__ == "__main__":
    unittest.main()
