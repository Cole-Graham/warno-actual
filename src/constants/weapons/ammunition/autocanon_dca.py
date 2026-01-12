"""DCA AutoCanon weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    
    ("DCA_4_canon_ZPU4_towed_14_5mm", "DCA", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "AimingTime": 1.2,
            },
        },
    },
    
    ("DCA_4_canons_AZP_23_Amur_23mm_late", "DCA", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 25,
            },
            "parent_membr": {
                "AimingTime": 1.2,
            },
        },
    },
    
    ("DCA_4_canons_APZ23_23mm", "DCA", None, False): { # 274
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 25,
            },
            "parent_membr": {
                "AimingTime": 1.2,
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
                "AimingTime": 1.2,
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
                "AimingTime": 1.2,
            },
        },
    },
    
    ("DCA_2_canon_ZU23_2_23mm_TOWED", "DCA", None, False): { # 261
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.2,
            },
        },
    },

    ("DCA_2_canon_ZU23_2_23mm", "DCA", None, False): { # 260
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.2,
            },
        },
    },

    ("DCA_2_canon_Jod_SP_23mm", "DCA", None, False): { # ???
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.2,
            },
        },
    },

    ("DCA_2_canon_Jod_towed_23mm", "DCA", None, False): { # ???
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 1925,
                "AimingTime": 1.2,
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
    
    ("DCA_1_canon_S60_57mm", "DCA", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "TimeBetweenTwoSalvos": 1.8,
                "SupplyCost": 8.0,
            },
        },
    },
    
    ("DCA_2_canons_S60_57mm", "DCA", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "TimeBetweenTwoFx": 0.4,
                "MaximumRangeGRU": 1575,
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 2450,
                "TimeBetweenTwoSalvos": 2.0,
                "SupplyCost": 16.0,
            },
        },
    },
}
# fmt: on
