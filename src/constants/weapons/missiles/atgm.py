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
            "hit_roll": {
                "Idling": 55,
            },
            "parent_membr": {
                "MinimumRangeGRU": 60,
                "ProjectileSpeedGRU": 233,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_dragon_wa'",
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
            "hit_roll": {
                "Idling": 55,
            },
            "parent_membr": {
                "MinimumRangeGRU": 60,
                "ProjectileSpeedGRU": 233,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_dragon_wa'",
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
                "ProjectileSpeedGRU": 350,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_metis_wa'",
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
                "Index": 23,
            },
            "hit_roll": {
                "Idling": 60,
            },
            "parent_membr": {
                "add": [65, "HasDeploymentTime = True"],
                "ProjectileSpeedGRU": 350,
                "NoiseDissimulationMalus": 1.0,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_swingfire_wa'",
            },
        },
        "SupplyCost": 95.0,
        "WeaponDescriptor": {
            "SalvoLengths": [5, 4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 350,
        },
    },

    ("ATGM_Swingfire_noisy", "ATGM", "ATGM_Swingfire", True): {
        "Ammunition": {
            "Arme": {
                "Index": 23,
            },
            "hit_roll": {
                "Idling": 60,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 350,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_swingfire_wa'",
                "TandemCharge": True, # For inverted tandem logic
            },
        },
        "SupplyCost": 95.0,
        "WeaponDescriptor": {
            "SalvoLengths": [5, 4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 350,
        },
    },
    
    ("ATGM_MILAN_2_IFV", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 23,
            },
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 350,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_milan_wa'",
            },
        },
        "SupplyCost": 90.0,
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
                "Idling": 50,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 350,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_milan_wa'",
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
                "Index": 23,
            },
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 350,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_milan_wa'",
            },
        },
        "SupplyCost": 90.0,
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
                "Idling": 50,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 350,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_milan_wa'",
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
                "Idling": 50,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 466,
                "AimingTime": 6.0,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_shillelagh_wa'",
            },
        },
        "SupplyCost": 75.0,
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
                "Index": 26,
            },
            "hit_roll": {
                "Idling": 70,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 739,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_hot_wa'",
            },
        },
        "SupplyCost": 115.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4, 3, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 739,
        },
    },

    ("ATGM_HOT1", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 23,
            },
            "hit_roll": {
                "Idling": 65,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 739,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_hot_wa'",
            },
        },
        "SupplyCost": 90.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4, 1],
        },

        "MissileDescriptor": {
            "MaxSpeedGRU": 739,
        },
    },
    
    ("ATGM_AS11", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 20,
            },
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 350,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_as11_wa'",
            },
        },
        "SupplyCost": 70.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 350,
        },
    },
    
    ("ATGM_GLHL", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 26,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 1060,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_hellfire_wa'",
            },
        },
        "SupplyCost": 115.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 1060,
        },
    },
    
    ("ATGM_BGM71D_TOW_2A_IFV", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 25,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 466,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_tow2a_wa'",
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
    
    ("ATGM_BGM71D_TOW_2_IFV", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 24,
            },
            "parent_membr": {
                # "Caliber": ("6.1kg HYBRID", "SVJNWQPYKO"),
                "ProjectileSpeedGRU": 466,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_tow2a_wa'",
            }
        },
        "SupplyCost": 100.0,
        "WeaponDescriptor": {            
            "SalvoLengths": [2],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("ATGM_BGM71D_TOW_2A", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 25,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 466,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_tow2a_wa'",
            }
        },
        "SupplyCost": 115.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2, 1],
        },

        "MissileDescriptor": {
            "MaxSpeedGRU": 466,
        },
    },

    ("ATGM_BGM71D_TOW_2", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 24,
            },
            "parent_membr": {
                # "Caliber": ("6.1kg HYBRID", "SVJNWQPYKO"),
                "ProjectileSpeedGRU": 466,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_tow2a_wa'",
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
                "ProjectileSpeedGRU": 466,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_tow2a_wa'",
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
    
    ("ATGM_BGM71C_ITOW_ETAS_IFV", "ATGM", "ATGM_BGM71C_ITOW", True): {
        "Ammunition": {
            "parent_membr": {
                "ProjectileSpeedGRU": 466,
                "TimeBetweenTwoSalvos": 30.0,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_tow2a_wa'",
                "TandemCharge": True, # For inverted tandem logic
            },
        },
        "SupplyCost": 80.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2],
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
                "ProjectileSpeedGRU": 466,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_tow_wa'",
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
    
    ("ATGM_9K111M_Faktoriya_IFV", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 19,
            },
            "display": "9K111M Faktoriya",
            "token": "TDLAGLBIVE",
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 311,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_fagot_wa'",
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

    ("ATGM_9K111M_Faktoriya", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 19,
            },
            "display": "9K111M Faktoriya",
            "token": "TDLAGLBIVE",
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 311,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_fagot_wa'",
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

    ("ATGM_9K111_Fagot", "ATGM", "ATGM_9K111M_Faktoriya", True): {
        "Ammunition": {
            "Arme": {
                "Index": 16,
            },
            "display": "9K111 Fagot",
            "token": "LNPKSXACVZ",
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 311,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_fagot_wa'",
                "TandemCharge": True, # For inverted tandem logic
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
                "Idling": 50,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "ProjectileSpeedGRU": 233,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_malyutka_wa'",
            },
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 233,
        },
    },

    ("ATGM_9M14_MalyutkaP", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "ProjectileSpeedGRU": 233,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_malyutka_wa'",
            },
        },
        "SupplyCost": 60.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 233,
        },
    },

    ("ATGM_9M128_Agona", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 25
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 544,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_agona_wa'",
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
            "Arme": {
                "Index": 22,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "ProjectileSpeedGRU": 622,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_svir_wa'",
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
    
    ("ATGM_9M114M_KokonM", "ATGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "ProjectileSpeedGRU": 622,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_kokon_wa'",
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
    
    ("ATGM_9M114M_Ataka", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 26,
            },
            "hit_roll": {
                "Idling": 60,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 1060,
                "TimeBetweenTwoSalvos": 8.0,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_ataka_wa'",
            },
        },
        "SupplyCost": 80.0,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 1060,
        },
    },

    ("ATGM_9M119_Refleks", "ATGM", None, False): {
        "Ammunition": {
            "display": "9M119 Refleks",
            "token": "ZIAPPNOKJO",
            "Arme": {
                "Index": 22,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2800,
                "ProjectileSpeedGRU": 622,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_refleks_wa'",
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
    
    # Eugen added their own version of this missile, but pretty sure they modeled it innacurately.
    # ("ATGM_9M119M_Invar", "ATGM", "ATGM_9M119_Refleks", True): {
    ("ATGM_9M119M_Invar", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 25,
            },
            "display": "9M119M Invar",
            "token": "YUXMIRHNPX",
            "parent_membr": {
                "MaximumRangeGRU": 2800,
                "ProjectileSpeedGRU": 622,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_invar_wa'",
                "TandemCharge": False, # For inverted tandem logic
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
                "ProjectileSpeedGRU": 739,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_bastion_wa'",
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
    
    ("ATGM_9M117_Bastion_IFV", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 19,
            },
            "display": "9M117 Bastion",
            "token": "DIHEGBLZRU",
            "parent_membr": {
                "ProjectileSpeedGRU": 739,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_bastion_wa'",
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
                "Index": 24,
            },
            "parent_membr": {
                # "Caliber": ("2.7kg TANDEM", "JDLKNWTJOR"),
                "ProjectileSpeedGRU": 389,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_konkursM_wa'",
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

    # TODO: Find out why this is sourcing ATGM_9M113M_KonkursM_salvolength5 for the donor
    ("ATGM_inf_9M113M_KonkursM", "ATGM", "ATGM_9M113M_KonkursM", True): {
        "Ammunition": {
            "Arme": {
                "Index": 24,
            },
            "hit_roll": {
                "Idling": 60,
            },
            "parent_membr": {
                "TimeBetweenTwoSalvos": 8.0,
                "MaximumRangeGRU": 2450,
                "ProjectileSpeedGRU": 389,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_konkursM_wa'",
                "TandemCharge": False, # For inverted tandem logic
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
                "ProjectileSpeedGRU": 389,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_konkurs_wa'",
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
                "ProjectileSpeedGRU": 389,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_konkurs_wa'",
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
                "ProjectileSpeedGRU": 739,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_kobra_wa'",
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
                "Index": 23,
            },
            "display": "9M112M2 Kobra",
            "token": "CUZYCCVUIO",
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "ProjectileSpeedGRU": 739,
                "InterfaceWeaponTexture": "'Texture_Interface_Weapon_kobra_wa'",
                "TandemCharge": False, # For inverted tandem logic
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
