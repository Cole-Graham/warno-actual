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
                "PorteeMaximaleGRU": 1575,
            },
        },
    },
    
    ("Canon_HE_73_mm_SPG9_TOWED", "recoilless", None, False): { # 220
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PhysicalDamages": 0.85,
                "SuppressDamages": 115,
                "DisplaySalveAccuracy": False,
            },
        },
    },

    ("Canon_HE_73_mm_SPG9", "recoilless", None, False): { # 220
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PhysicalDamages": 0.85,
                "SuppressDamages": 115,
                "DisplaySalveAccuracy": False,
            },
        },
    },

    ("Canon_HE_73_mm_2A28_Grom", "canon", None, False): { # 219
        "Ammunition": {
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1400,
                "RadiusSplashPhysicalDamagesGRU": 33,
                "PhysicalDamages": 0.85,
                "RadiusSplashSuppressDamagesGRU": 66,
                "SuppressDamages": 115,
                "FlightTimeForSpeed": 5.0,
            },
        },
    },

    ("Canon_HE_165mm_AVRE", "canon", None, False): { # 217
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleGRU": 1400,
                "PhysicalDamages": 4.0,
            },
        },
    },

    ("Canon_HE_152mm_Sheridan", "canon", None, False): { # 216
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1575,
                "PhysicalDamages": 1.75,
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
                "TempsEntreDeuxTirs": 6.6,
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
                "TempsEntreDeuxTirs": 6.6,
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
                "TempsEntreDeuxTirs": 6.6,
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
                "PorteeMaximaleGRU": 2275,
                "SupplyCost": 220,
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
                "TempsEntreDeuxTirs": 6.6,
            },
        },
    },

    ("Canon_HE_125_mm_2A46_T64A", "canon", None, False): { # 204
        "Ammunition": {
            "parent_membr": {
                "TempsEntreDeuxTirs": 6.6,
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

    ("Canon_HE_100mm_2A70", "canon", None, False): { # 169
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 43,
                "PhysicalDamages": 1.15,
                "RadiusSplashSuppressDamagesGRU": 86,
                "SupplyCost": 100,
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
                "PorteeMaximaleGRU": 1400,
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
                "TempsEntreDeuxTirs": 6.6,
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
                "TempsEntreDeuxTirs": 6.6,
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
                "TempsEntreDeuxTirs": 6.6,
            },
        },
    },

    ("Canon_AP_125_mm_2A46_T72M", "canon", None, False): { # 134
        "Ammunition": {
            "Arme": {
                "Index": 29,
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 2275,
                "SupplyCost": 220,
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
                "TempsEntreDeuxTirs": 6.6,
            },
        },
    },

    ("Canon_AP_125_mm_2A46_T64A", "canon", None, False): { # 132
        "Ammunition": {
            "parent_membr": {
                "TempsEntreDeuxTirs": 6.6,
            },
        },
    },
}
# fmt: on
