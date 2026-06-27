"""Tests for kinetic AP penetration level scaling in the DPM visualizer."""

import unittest

from tools.dpm_visualizer.calculations import (
    effective_kinetic_ap_damage_level,
    is_kinetic_ap_damage_family,
    segment_dpm_by_kinetic_ap_level,
)


class TestKineticApDamageLevel(unittest.TestCase):
    def test_bushmaster_late_at_max_range(self):
        # NDF index 13 @ 175m; 1750m max range -> index 4 at max range
        self.assertEqual(effective_kinetic_ap_damage_level(13, 175.0, 1750.0), 13)
        self.assertEqual(effective_kinetic_ap_damage_level(13, 1750.0, 1750.0), 4)

    def test_penetration_step_at_max_range_threshold(self):
        # Steps align with max_range - N*175m (not offset by 25m sample step)
        self.assertEqual(effective_kinetic_ap_damage_level(13, 1401.0, 1750.0), 5)
        self.assertEqual(effective_kinetic_ap_damage_level(13, 1400.0, 1750.0), 6)
        self.assertEqual(effective_kinetic_ap_damage_level(13, 1375.0, 1750.0), 6)

    def test_close_range_band(self):
        self.assertEqual(effective_kinetic_ap_damage_level(13, 175.0, 1750.0), 13)
        self.assertEqual(effective_kinetic_ap_damage_level(13, 100.0, 1750.0), 13)

    def test_floor_at_level_one(self):
        self.assertEqual(effective_kinetic_ap_damage_level(3, 1750.0, 1750.0), 1)

    def test_kinetic_family_detection(self):
        self.assertTrue(is_kinetic_ap_damage_family("DamageFamily_ap"))
        self.assertTrue(is_kinetic_ap_damage_family("ap"))
        self.assertFalse(is_kinetic_ap_damage_family("DamageFamily_he"))
        self.assertFalse(is_kinetic_ap_damage_family("DamageFamily_ap_missile"))

    def test_segment_dpm_splits_at_ap_steps(self):
        props = {
            "damage_family": "ap",
            "damage_level": 13,
            "max_range": 1750.0,
        }
        ranges = [1401.0, 1400.0, 1375.0]
        dpm = [10.0, 20.0, 20.0]
        segments = segment_dpm_by_kinetic_ap_level(ranges, dpm, props)
        self.assertEqual(len(segments), 2)
        self.assertEqual(segments[0][0], [1401.0])
        self.assertEqual(segments[1][0], [1400.0, 1375.0])


if __name__ == "__main__":
    unittest.main()
