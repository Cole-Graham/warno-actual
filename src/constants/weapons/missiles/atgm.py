"""atgm missile definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
missiles: Dict[WeaponKey, WeaponData] = {
    ("M47_DRAGON_II", "ATGM", None, False): { # 165
        "Ammunition": {
            "Arme": {
                "Index": 19,
            },
            "parent_membr": {
                "MinimumRangeGRU": 60,
                "MaximalSpeedGRU": 233,
            }
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 233,
        },
    },

    ("M47_DRAGON", "ATGM", None, False): { # 164
        "Ammunition": {
            "Arme": {
                "Index": 16,
            },
            "parent_membr": {
                "MinimumRangeGRU": 60,
                "MaximalSpeedGRU": 233,
            }
        },
        "SupplyCost": 50.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 233,
        },
    },
    
    ("ATGM_9K115_Metis", "ATGM", None, False): { # 138
        "Ammunition": {
            "Arme": {
                "Index": 18,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "MinimumRangeGRU": 60,
                "MaximalSpeedGRU": 350,
            }
        },
        "SupplyCost": 80.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 350,
        },
    },

    ("ATGM_Swingfire", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 22,
            },
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 350,
            },
        },
        "SupplyCost": 120.0,
        "WeaponDescriptor": {
            "SalvoLengths": [5, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 350,
        },
    },
    
    ("ATGM_MILAN_2_IFV", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 22,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 350,
            },
        },
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 350,
        },
    },
    
    ("ATGM_MILAN_IFV", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 16,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 350,
            },
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 350,
        },
    },

    ("ATGM_MILAN_2", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 22,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 350,
            },
        },
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 350,
        },
    },

    ("ATGM_MILAN", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 16,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 350,
            },
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 350,
        },
    },

    ("ATGM_MGM551C_Shillelagh", "ATGM", None, False): { # 132
        "Ammunition": {
            "Arme": {
                "Index": 18,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 466,
                "AimingTime": 6.0,
            },
        },
        "SupplyCost": 90.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("ATGM_HOT2", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 23,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            },
        },
        "SupplyCost": 160.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4, 3, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("ATGM_HOT1", "ATGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            },
        },
        "SupplyCost": 150.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4, 1],
        },

        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("ATGM_BGM71D_TOW_2A", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 24,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            }
        },
        "SupplyCost": 115.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2],
        },

        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("ATGM_BGM71D_TOW_2", "ATGM", None, False): {
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
            "SalvoLengths": [8, 4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("ATGM_BGM71C_ITOW", "ATGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            }
        },
        "SupplyCost": 80.0,
        "WeaponDescriptor": {
            "SalvoLengths": [8, 4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("ATGM_BGM71_TOW", "ATGM", None, False): {
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
            "SalvoLengths": [8, 4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("ATGM_9K111M_Faktoriya", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 19,
            },
            "display": "9K111M Faktoriya",
            "token": "TDLAGLBIVE",
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 311,
            },
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 311,
        },
    },

    ("ATGM_9K111_Fagot", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 16,
            },
            "display": "9K111 Fagot",
            "token": "LNPKSXACVZ",
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 311,
            }
        },
        "SupplyCost": 50.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 311,
        },
    },
    
    ("ATGM_9M14_MalyutkaP_IFV", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "MaximalSpeedGRU": 311,
            },
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 311,
        },
    },

    ("ATGM_9M14_MalyutkaP", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "MaximalSpeedGRU": 311,
            },
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 311,
        },
    },

    ("ATGM_9M128_Agona", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 24
            },
            "parent_membr": {
                "MaximalSpeedGRU": 544,
            },
        },
        "SupplyCost": 115.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 544,
        },
    },

    ("ATGM_9K120_Svir", "ATGM", None, False): {
        "Ammunition": {
            "display": "9K120 Svir",
            "token": "WMOWZEXCQJ",
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "MaximalSpeedGRU": 622,
            },
        },
        "SupplyCost": 80.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 622,
        },
    },

    ("ATGM_9M119_Refleks", "ATGM", None, False): {
        "Ammunition": {
            "display": "9M119 Refleks",
            "token": "ZIAPPNOKJO",
            "parent_membr": {
                "MaximumRangeGRU": 2800,
                "MaximalSpeedGRU": 622,
            },
        },
        "SupplyCost": 85.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 622,
        },
    },

    ("ATGM_9M119M_Invar", "ATGM", "ATGM_9M119_Refleks", True): {
        "Ammunition": {
            "Arme": {
                "Index": 24,
            },
            "display": "9M119M Invar",
            "token": "YUXMIRHNPX",
            "parent_membr": {
                "MaximumRangeGRU": 2800,
                "MaximalSpeedGRU": 622,
            },
        },
        "SupplyCost": 120.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 622,
        },
    },

    ("ATGM_9M117_Bastion", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 19,
            },
            "display": "9M117 Bastion",
            "token": "DIHEGBLZRU",
            "parent_membr": {
                "MaximalSpeedGRU": 739,
            },
        },
        "SupplyCost": 95.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 739,
        },
    },

    ("ATGM_9M113M_KonkursM", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 23,
            },
            "parent_membr": {
                # "Caliber": ("2.7kg TANDEM", "JDLKNWTJOR"),
                "MaximalSpeedGRU": 389,
            },
        },
        "SupplyCost": 95.0,
        "WeaponDescriptor": {
            "SalvoLengths": [5, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 389,
        },
    },

    ("ATGM_inf_9M113M_KonkursM", "ATGM", "ATGM_9M113M_KonkursM", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
            },
        },
        "SupplyCost": 95.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
    },

    ("ATGM_9M113_Konkurs", "ATGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                # "Caliber": ("2.7kg HEAT", "HNXYVDFTUM"),
                "MaximalSpeedGRU": 389,
            },
        },
        "SupplyCost": 75.0,
        "WeaponDescriptor": {
            "SalvoLengths": [5, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 389,
        },
    },

    ("ATGM_9M113_Konkurs_BMP2", "ATGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                # "Caliber": ("2.7kg HEAT", "HNXYVDFTUM"),
                "MaximalSpeedGRU": 389,
            },
        },
        "SupplyCost": 75.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 389,
        },
    },

    ("ATGM_9M112_Kobra", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 20,
            },
            "display": "9M112 Kobra",
            "token": "ILNHEHTSQR",
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 739,
            },
        },
        "SupplyCost": 80.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 739,
        },
    },

    ("ATGM_9M112M2_Kobra", "ATGM", "ATGM_9M112_Kobra", True): {
        "Ammunition": {
            "Arme": {
                "Index": 22,
            },
            "display": "9M112M2 Kobra",
            "token": "CUZYCCVUIO",
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 739,
            },
        },
        "SupplyCost": 105.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 739,
        },
    },
}
# fmt: on
