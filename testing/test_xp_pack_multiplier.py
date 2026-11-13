"""Deck pack multipliers must be 0.0 or produce at least one unit."""

import math
import unittest

from src.gameplay_mods.generated.gameplay.decks.division_rules import (
    normalize_xp_multipliers,
    xp_multipliers_for_counts,
)


def _floor_units(pack_size: int, multiplier: float) -> int:
    return math.floor(pack_size * multiplier + 1e-9)


class TestXpPackMultiplier(unittest.TestCase):
    def test_zero_count_is_zero_and_one_of_twelve_fills_a_pack(self):
        text = xp_multipliers_for_counts(12, [12, 8, 4, 1, 0])
        values = [float(part) for part in text.strip("[]").split(",")]
        self.assertEqual(values[-1], 0.0)
        for count, multiplier in zip([12, 8, 4, 1], values):
            self.assertGreaterEqual(_floor_units(12, multiplier), 1)
            self.assertGreaterEqual(_floor_units(12, multiplier), 1 if count == 1 else 1)

    def test_two_decimal_ratio_that_truncates_is_raised(self):
        text = normalize_xp_multipliers(12, [0.08, 0.0])
        small, zero = [float(part) for part in text.strip("[]").split(",")]
        self.assertEqual(zero, 0.0)
        self.assertGreaterEqual(_floor_units(12, small), 1)


if __name__ == "__main__":
    unittest.main()
