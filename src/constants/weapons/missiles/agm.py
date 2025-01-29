"""agm missile definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
missiles: Dict[WeaponKey, WeaponData] = {
    ("AGM_HOT2", "ATGM", None, False): { # 74
        "Ammunition": {
            "Arme": {
                "Index": 24,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            },
        },
        "BaseSupplyCost": 115,
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
        "BaseSupplyCost": 90,
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
                "SupplyCost": 105
            },
        },
    },

    ("AGM_Kh29L", "ATGM", None, False): { # 84
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 90
            },
        },
    },

    ("AGM_Kh23M", "ATGM", None, False): { # 77
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 60
            },
        },
    },
    
    ("AGM_BGM71C_ITOW_salvolength8", "ATGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            }
        },
        "BaseSupplyCost": 80,
        "WeaponDescriptor": {
            "SalvoLengths": [8],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },
    
    ("AGM_BGM71C_FITOW_salvolength8", "ATGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            }
        },
        "BaseSupplyCost": 90,
        "WeaponDescriptor": {
            "SalvoLengths": [8],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },
    
    ("AGM_BGM71_TOW_salvolength8", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            }
        },
        "BaseSupplyCost": 60,
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
                "SupplyCost": 80
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
        "BaseSupplyCost": 115,
        "WeaponDescriptor": {
            "SalvoLengths": [16, 8, 4, 2, 1],
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
                "PorteeMaximaleGRU": 2625,
                "MaximalSpeedGRU": 350,
            },
        },
        "BaseSupplyCost": 75,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 1],
        },
    },

    ("AGM_9M14_MalyutkaP_salvolength6", "ATGM", None, False): { # 43
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 2450,
                "MaximalSpeedGRU": 311,
            },
        },
        "BaseSupplyCost": 60,
        "WeaponDescriptor": {
            "SalvoLengths": [6],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 311,
        },
    },
    
    ("AGM_9M14_MalyutkaP_salvolength4", "ATGM", None, False): { # 43
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 2450,
                "MaximalSpeedGRU": 311,
            },
        },
        "BaseSupplyCost": 60,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
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
        "BaseSupplyCost": 80,
        "WeaponDescriptor": {
            "SalvoLengths": [16, 8, 6, 4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("AGM_9K121_Vikhr_x16_avion", "AGM", None, False): { # 36
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
                "TempsDeVisee": 0.0,
            },
        },
    },
    
    ("Bomb_KAB_1500L_salvolength3", "LGB", None, False): { # 152
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 360,
            }
        },
    },

    ("Bomb_GBU_12_salvolength2", "LGB", None, False): { # 147
        "Ammunition": {
            "parent_membr": {
                "TraitsToken": ['MOTION', 'semiAuto', 'HE'],
                "TempsEntreDeuxSalves": 5,
                "SupplyCost": 280,
            },
        },
    },
}
# fmt: on
