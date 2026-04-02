"""Weapon range remap standards: member name -> {old_gru: new_gru}."""

from typing import Dict

WEAPON_RANGE_MEMBERS_TO_CHECK: Dict[str, Dict[int, int]] = {
    "MaximumRangeGRU": {
        1200: 1225,
        1250: 1225,
    },
    "MaximumRangeHelicopterGRU": {
        1425: 1400,
        1500: 1575,
        2475: 2450,
        2650: 2625,
    },
    "MaximumRangeAirplaneGRU": {
        1950: 1925,
        2300: 2275,
    },
}
