import unittest

from src.gameplay_mods.generated.gameplay.gfx.ammunition_.missiles import (
    _has_explicit_time_between_salvos,
)


class TestHasExplicitTimeBetweenSalvos(unittest.TestCase):
    def test_explicit_in_parent_membr(self):
        data = {
            "Ammunition": {
                "parent_membr": {
                    "TimeBetweenTwoSalvos": 12.0,
                },
            },
        }
        self.assertTrue(_has_explicit_time_between_salvos(data))

    def test_missing_override(self):
        data = {
            "Ammunition": {
                "parent_membr": {
                    "AimingTime": 0.3,
                },
            },
        }
        self.assertFalse(_has_explicit_time_between_salvos(data))

    def test_empty_ammunition(self):
        self.assertFalse(_has_explicit_time_between_salvos({}))


if __name__ == "__main__":
    unittest.main()
