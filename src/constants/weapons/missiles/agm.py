"""agm missile definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
missiles: Dict[WeaponKey, WeaponData] = {
    ("AGM_HOT2", "ATGM", None, False): { # 74
        "Ammunition": {
            "Arme": {
                "Index": 23,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            },
        },
        # "SupplyCost": 115.0,
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("AGM_HOT1", "ATGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            },
        },
        "SupplyCost": 90.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },
    
    ("AGM_Kh29T", "ATGM", None, False): { # 85
        "Ammunition": {
            "parent_membr": {
                # "SupplyCost": 105.0,
                "SupplyCost": 100.0,
            },
        },
    },

    ("AGM_Kh29L", "ATGM", None, False): { # 84
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 90.0
            },
        },
    },

    ("AGM_Kh23M", "ATGM", None, False): { # 77
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 60.0
            },
        },
    },

    ("AGM_BGM71D_TOW_2", "AGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 23,
            },
            "parent_membr": {
                # "Caliber": ("6.1kg HYBRID", "SVJNWQPYKO"),
                "MaximalSpeedGRU": 466,
            }
        },
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [8, 4],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },
    
    ("AGM_BGM71C_ITOW", "ATGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            }
        },
        "SupplyCost": 80.0,
        "WeaponDescriptor": {
            "SalvoLengths": [8],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },
    
    ("AGM_BGM71C_FITOW", "ATGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            }
        },
        "SupplyCost": 90.0,
        "WeaponDescriptor": {
            "SalvoLengths": [8],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },
    
    ("AGM_BGM71_TOW", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            }
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [8],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },
    
    ("AGM_AGM65D_Maverick", "ATGM", None, False): { # 56
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 80.0
            },
        },
    },
    
    ("AGM_AGM114A", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 26,
            },
            "parent_membr": {
                "TypeCategoryName": "'" + "JTOYRAARTS" + "'",
                "WeaponDescriptionToken": "'" + "CRYXRQVTBJ" + "'",
                "MinMaxCategory": "MinMax_ATGM",
            },
        },
        # "SupplyCost": 115.0,
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [16, 8, 4],
        },
    },

    ("AGM_9M17P_FalangaP", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 20,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "MaximalSpeedGRU": 350,
            },
        },
        "SupplyCost": 75.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4, 1],
        },
    },

    ("AGM_9M14_MalyutkaP", "ATGM", None, False): { # 43
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "MaximalSpeedGRU": 311,
            },
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 311,
        },
    },

    ("AGM_9M114M_KokonM", "ATGM", None, False): { # 37
        "Ammunition": {
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            },
        },
        "SupplyCost": 80.0,
        "WeaponDescriptor": {
            "SalvoLengths": [16, 8, 6, 4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("AGM_9K121_Vikhr_avion", "AGM", None, False): { # 36
        "Ammunition": {
            "Arme": {
                "Index": 24,
            },
            "hit_roll": {
                "Moving": 50,
            },
            "parent_membr": {
                "TypeCategoryName": "'" + "JTOYRAARTS" + "'",
                "WeaponDescriptionToken": "'" + "CRYXRQVTBJ" + "'",
                "MinMaxCategory": "MinMax_ATGM",
                "AimingTime": 0.0,
            },
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2],
        },
    },
    
    ("Bomb_KAB_1500L", "LGB", None, False): { # 152
        # "SupplyCost": 120.0,
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [3, 2, 1],
        },
    },
    
    ("Bomb_KAB_1500Kr", "LGB", None, False): {
        # "SupplyCost": 120.0,
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2, 1],
        },
    },

    ("Bomb_GBU_12", "LGB", None, False): { # 147
        "Ammunition": {
            "parent_membr": {
                "TraitsToken": ['MOTION', 'semiAuto', 'HE'],
                "TimeBetweenTwoSalvos": 5,
            },
        },
        # "SupplyCost": 140.0,
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2, 1],
        },
    },
    
    ("AGM_AS30L", "AGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 70.0,
            },
        },
    },
}
# fmt: on
