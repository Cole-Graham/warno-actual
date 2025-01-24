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
                "PorteeMinimaleGRU": 60,
                "MaximalSpeedGRU": 233,
            }
        },
        "BaseSupplyCost": 60,
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
                "PorteeMinimaleGRU": 60,
                "MaximalSpeedGRU": 233,
            }
        },
        "BaseSupplyCost": 50,
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
                "PorteeMaximaleGRU": 1575,
                "PorteeMinimaleGRU": 60,
                "MaximalSpeedGRU": 350,
            }
        },
        "BaseSupplyCost": 80,
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
        "BaseSupplyCost": 120,
        "WeaponDescriptor": {
            "SalvoLengths": [5, 2, 1],
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
        "BaseSupplyCost": 100,
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
                "Idling": 40,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 350,
            },
        },
        "BaseSupplyCost": 90,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 990,
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
                "TempsDeVisee": 6.0,
            },
        },
        "BaseSupplyCost": 90,
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
                "Index": 24,
            },
            "parent_membr": {
                "MaximalSpeedGRU": 466,
            },
        },
        "BaseSupplyCost": 160,
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
        "BaseSupplyCost": 150,
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
        "BaseSupplyCost": 115,
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
        "BaseSupplyCost": 100,
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
        "BaseSupplyCost": 80,
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
        "BaseSupplyCost": 60,
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
        "BaseSupplyCost": 60,
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
        "BaseSupplyCost": 50,
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
                "PorteeMaximaleGRU": 2450,
                "MaximalSpeedGRU": 311,
            },
        },
        "BaseSupplyCost": 60,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4, 1],
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
        "BaseSupplyCost": 115,
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
                "PorteeMaximaleGRU": 2625,
                "MaximalSpeedGRU": 622,
            },
        },
        "BaseSupplyCost": 80,
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
                "PorteeMaximaleGRU": 2800,
                "MaximalSpeedGRU": 622,
            },
        },
        "BaseSupplyCost": 85,
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
                "PorteeMaximaleGRU": 2800,
                "MaximalSpeedGRU": 622,
            },
        },
        "BaseSupplyCost": 120,
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
        "BaseSupplyCost": 95,
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
        "BaseSupplyCost": 95,
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
                "PorteeMaximaleGRU": 2450,
            },
        },
        "BaseSupplyCost": 95,
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
        "BaseSupplyCost": 75,
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
        "BaseSupplyCost": 75,
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
        "BaseSupplyCost": 80,
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
        "BaseSupplyCost": 105,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 739,
        },
    },
}
# fmt: on
