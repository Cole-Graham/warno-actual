import unittest

from src.constants.weapons.standards import (
    manpad_time_between_salvos_seconds,
    sam_time_between_salvos_seconds,
)


class TestSamTimeBetweenSalvosSeconds(unittest.TestCase):
    def test_salvo_1(self):
        # min(6, 1) = 1 -> 8 + 4 = 12
        self.assertEqual(sam_time_between_salvos_seconds(1), 12.0)

    def test_salvo_2(self):
        # min(6, 2) = 2 -> 8 + 8 = 16
        self.assertEqual(sam_time_between_salvos_seconds(2), 16.0)

    def test_salvo_4(self):
        # min(6, 4) = 4 -> 8 + 16 = 24
        self.assertEqual(sam_time_between_salvos_seconds(4), 24.0)

    def test_salvo_7_cap(self):
        # min(6, 6) = 6 -> 8 + 24 = 32
        self.assertEqual(sam_time_between_salvos_seconds(7), 32.0)

    def test_salvo_8_stays_capped(self):
        # min(6, 7) = 6 -> 32
        self.assertEqual(sam_time_between_salvos_seconds(8), 32.0)


class TestManpadTimeBetweenSalvosSeconds(unittest.TestCase):
    def test_salvo_1(self):
        # min(4, 0) = 0 -> 6 -> clamped to 7
        self.assertEqual(manpad_time_between_salvos_seconds(1), 7.0)

    def test_salvo_2(self):
        # min(4, 1) = 1 -> 6 + 4 = 10
        self.assertEqual(manpad_time_between_salvos_seconds(2), 10.0)

    def test_salvo_4(self):
        # min(4, 3) = 3 -> 6 + 12 = 18
        self.assertEqual(manpad_time_between_salvos_seconds(4), 18.0)

    def test_salvo_5_cap(self):
        # min(4, 4) = 4 -> 6 + 16 = 22
        self.assertEqual(manpad_time_between_salvos_seconds(5), 22.0)

    def test_floor_clamps_below_7(self):
        # min(4, -1) = -1 -> 6 - 4 = 2 -> clamped to 7
        self.assertEqual(manpad_time_between_salvos_seconds(0), 7.0)


if __name__ == "__main__":
    unittest.main()
