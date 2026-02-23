"""Canon weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Canon_HEAT_73_mm_SPG9_TOWED", "recoilless", None, False): { # 241
        "Ammunition": {
            "Arme": {
                "Index": 15,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "DisplaySalveAccuracy": False,
                "SupplyCost": 8.0,
            },
        },
    },

    ("Canon_HEAT_73_mm_SPG9", "recoilless", None, False): { # 240
        "Ammunition": {
            "Arme": {
                "Index": 15,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "DisplaySalveAccuracy": False,
                "SupplyCost": 8.0,
            },
        },
    },

    ("Canon_HEAT_73_mm_SPG9D_TOWED", "recoilless", "Canon_HEAT_73_mm_SPG9_TOWED", True): {  # 707
        "Ammunition": {
            "display": "SPG-9D",
            "token": "SPG9D_PARA",
            "parent_membr": {
                "DisplaySalveAccuracy": False,
                "SupplyCost": 8.0,
            },
        },
    },
    
    ("Canon_HEAT_85mm_S53", "canon", "Canon_AP_85mm_S53", True): { # T-34 3BK-2
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_ap_missile",
                "Index": 13,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "Caliber": ("85mm HEAT", "IWLOKTOKDR"),
                "TraitsToken": ['HE', 'HEAT'],
                "MaximumRangeGRU": 1750,
                "DamageTypeEvolutionOverRangeDescriptor": "nil"
            },
        },
    },
    
    ("Canon_HEAT2_85mm_S53", "canon", "Canon_AP_85mm_S53", True): { # T-34 3BK-2M
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_ap_missile",
                "Index": 15,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "Caliber": ("85mm HEAT", "IWLOKTOKDR"),
                "TraitsToken": ['HE', 'HEAT'],
                "MaximumRangeGRU": 1750,
                "DamageTypeEvolutionOverRangeDescriptor": "nil"
            },
        },
    },
    
    ("Canon_HEAT_105mm_L7_Centurion_AVRE", "canon", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
        },
    },

    ("Canon_HEAT_152mm_Sheridan", "canon", None, False): { # 239
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
            },
        },
    },
    
    ("Canon_HE_73_mm_SPG9_TOWED", "recoilless", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PhysicalDamages": 0.85,
                "SuppressDamages": 115,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 8.0,
            },
        },
    },

    ("Canon_HE_73_mm_SPG9", "recoilless", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PhysicalDamages": 0.85,
                "SuppressDamages": 115,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 8.0,
            },
        },
    },

    ("Canon_HE_73_mm_2A28_Grom", "canon", None, False): { # 219
        "Ammunition": {
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "RadiusSplashPhysicalDamagesGRU": 33,
                "PhysicalDamages": 0.85,
                "RadiusSplashSuppressDamagesGRU": 66,
                "SuppressDamages": 115,
                # Eugen removed this and replaced it with SpeedGRU
                # "FlightTimeForSpeed": 3.3,
                "SupplyCost": 300.0,
            },
        },
    },
    
    ("Canon_HE_76mm_D56T", "canon", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "RadiusSplashPhysicalDamagesGRU": 31,
                "RadiusSplashSuppressDamagesGRU": 55,
                "SupplyCost": 8.0,
            },
        },
    },
    
    ("Canon_HE_76mm_L5A1", "canon", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 0,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'HE'],
                "CanShootWhileMoving": False,
            },
        },
    },
    
    ("Canon_HE_76mm_L23A1", "canon", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 0,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'HE'],
                "CanShootWhileMoving": False,
            },
        },
    },
    
    ("Canon_HE_85mm_S53", "canon", None, False): { # T-34 3BK-2
        "Ammunition": {
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "Caliber": ("85mm HEAT", "IWLOKTOKDR"),
                "TraitsToken": ['HE'],
                "MaximumRangeGRU": 1750,
                "RadiusSplashPhysicalDamagesGRU": 38,
                "RadiusSplashSuppressDamagesGRU": 55,
            },
        },
    },
    
    ("Canon_HE_90mm_M48", "canon", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.0,
            },
        },
    },
    
    ("Canon_HE_90mm_M48_KanJPz", "canon", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.0,
            },
        },
    },

    ("Canon_HE_165mm_AVRE", "canon", None, False): { # 217
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "PhysicalDamages": 4.0,
            },
        },
    },
    
    ("Canon_HE_165mm_AVRE_L9A1", "canon", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "PhysicalDamages": 4.0,
            },
        },
    },

    ("Canon_HE_152mm_Sheridan", "canon", None, False): { # 216
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 1.75,
            },
        },
    },
    
    ("Canon_HE_142mm_AVRE", "canon", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 875,
                "PhysicalDamages": 3,
                "AimingTime": 2.0,
            },
        },
    },
    
    ("Canon_HE_115mm_U5TS_T62M", "canon", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.4,
            },
        },
    },

    ("Canon_HE_125_mm_2A46M_late_T80UD", "canon", None, False): { # 211
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_HE_125_mm_2A46M_late", "canon", None, False): { # 210
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_HE_125_mm_2A46M_T80B", "canon", None, False): { # 209
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },
    
    ("Canon_HE_125_mm_2A46M", "canon", None, False): { # T-72S
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
            },
        },
    },

    ("Canon_HE_125_mm_2A46_T72M", "canon", None, False): { # 206
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
            },
        },
    },

    ("Canon_HE_125_mm_2A46_T64B_very_late", "canon", None, False): { # 205
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_HE_125_mm_2A46_T64A_late", "canon", None, False): { # T-64AV
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1925,
            },
        },
    },


    ("Canon_HE_125_mm_2A46_T64A", "canon", None, False): { # 204
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_HE_100mm_D10T_early", "canon", None, False): { # 171
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.15,
            },
        },
    },
    
    ("Canon_HE_100mm_D10T_Merida", "canon", None, False): { # 171
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "PhysicalDamages": 1.15,
            },
        },
    },

    ("Canon_HE_100mm_2A70", "canon", None, False): { # 169
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 43,
                "PhysicalDamages": 1.15,
                "RadiusSplashSuppressDamagesGRU": 86,
                "SupplyCost": 100.0,
            },
        },
    },
    
    ("Canon_AP_100mm_D10T_Merida", "canon", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
        },
    },
    
    ("Canon_AP_76mm_D56T", "canon", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 15, # HEAT
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
            },
        },
    },
    
    ("Canon_AP_76mm_L5A1", "canon", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 13,
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 0,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'HE', 'HEAT'],
                "CanShootWhileMoving": False,
            },
        },
    },
    
    ("Canon_AP_76mm_L23A1", "canon", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 13,
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 0,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'HE', 'HEAT'],
                "CanShootWhileMoving": False,
            },
        },
    },
    
    ("Canon_AP_73_mm_2A28_Grom", "canon", None, False): { # 148
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "SupplyCost": 300.0,
            },
        },
    },

    ("Canon_AP_125_mm_2A46M_late_T80UD", "canon", None, False): { # 139
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_AP_125_mm_2A46M_late", "canon", None, False): { # 138
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_AP_125_mm_2A46M_T80B", "canon", None, False): { # 137
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },
    
    ("Canon_AP_125_mm_2A46M", "canon", None, False): { # T-72S
        "Ammunition": {
            "Arme": {
                "Index": 31,
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
            },
        },
    },
    
    # ("Canon_AP_125_mm_2A46_T72M2", "canon", None, False): { # T-72M2 WILK
    #     "Ammunition": {
    #         "Arme": {
    #             "Index": 31,
    #         },
    #     },
    # },

    ("Canon_AP_125_mm_2A46_T72M", "canon", None, False): { # 134
        "Ammunition": {
            # "Arme": {
            #     "Index": 29,
            # },
            "hit_roll": {
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
            },
        },
    },

    ("Canon_AP_125_mm_2A46_T64B_very_late", "canon", None, False): { # 133
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_AP_125_mm_2A46_T64A_late", "canon", None, False): { # 
        "Ammunition": {
            "Arme": {
                "Index": 20, # KE
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1925,
            },
        },
    },

    ("Canon_AP_125_mm_2A46_T64A", "canon", None, False): { # 132
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },
}
# fmt: on
