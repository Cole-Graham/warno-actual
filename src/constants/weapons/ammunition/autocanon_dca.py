"""DCA AutoCanon weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("DCA_4_canons_APZ23_23mm", "DCA", None, False): { # 274
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 25,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 2275,
                "AimingTime": 1.25,
            },
        },
    },

    ("DCA_2_canons_2A38M_30mm", "DCA", None, False): { # 262
        "Ammunition": {
            "hit_roll": {
                "Idling": 45,
                "Moving": 30,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "SuppressDamages": 60,
                "AimingTime": 1.25,
                "NbTirParSalves": 16,
                "AffichageMunitionParSalve": 128,
            },
        },
    },
    
    ("DCA_2_canons_HS_831_30mm", "DCA", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "AimingTime": 1.25,
            },
        },
    },
    
    ("DCA_2_canon_ZU23_2_23mm_TOWED", "DCA", None, False): { # 261
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.25,
            },
        },
    },

    ("DCA_2_canon_ZU23_2_23mm", "DCA", None, False): { # 260
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.25,
            },
        },
    },

    ("DCA_2_canon_Jod_SP_23mm", "DCA", None, False): { # ???
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.25,
            },
        },
    },

    ("DCA_2_canon_Jod_towed_23mm", "DCA", None, False): { # ???
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.25,
            },
        },
    },
    
    ("DCA_1_canon_53T2_20mm", "DCA", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
            },
        },
    },
}
# fmt: on
