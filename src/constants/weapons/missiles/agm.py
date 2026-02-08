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
            "hit_roll": {
                "Idling": 70,
            },
            "parent_membr": {
                "SpeedGRU": 739,
            },
        },
        "SupplyCost": 115.0,
        "WeaponDescriptor": {
            "SalvoLengths": [6, 4, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 739,
        },
    },

    ("AGM_HOT1", "ATGM", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 65,
            },
            "parent_membr": {
                "SpeedGRU": 739,
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
    
    ("AGM_Kh66", "ATGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 60.0,
                "SpeedGRU": 2800,
                "MaxAccelerationGRU": 1400,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 2800,
            "MaxAccelerationGRU": 1400,
        },
    },
    
    ("AGM_Kh29T", "ATGM", None, False): { # 85
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 3500,
                "AimingTime": 0.3,
                "ShotsCountPerSalvo": 2,
                "SimultaneousShotsCount": 1,
                "AffichageMunitionParSalve": 2,
                "SupplyCost": 210.0,
                "SpeedGRU": 2800,
                "MaxAccelerationGRU": 1400,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 2800,
            "MaxAccelerationGRU": 1400,
        },
    },

    ("AGM_Kh29L", "ATGM", None, False): { # 84
        "Ammunition": {
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 90.0,
                "SpeedGRU": 2800,
                "MaxAccelerationGRU": 1400,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 2800,
            "MaxAccelerationGRU": 1400,
        },
    },

    ("AGM_Kh23M", "ATGM", None, False): { # 77
        "Ammunition": {
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 60.0,
                "SpeedGRU": 2800,
                "MaxAccelerationGRU": 1400,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 2800,
            "MaxAccelerationGRU": 1400,
        },
    },

    ("AGM_BGM71D_TOW_2", "AGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 23,
            },
            "parent_membr": {
                # "Caliber": ("6.1kg HYBRID", "SVJNWQPYKO"),
                "SpeedGRU": 466,
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
                "SpeedGRU": 466,
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
                "SpeedGRU": 466,
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
                "SpeedGRU": 466,
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
    
    ("AGM_AGM65B_Maverick", "ATGM", None, False): { # 56
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 3500,
                "AimingTime": 0.3,
                "ShotsCountPerSalvo": 2,
                "SimultaneousShotsCount": 1,
                "AffichageMunitionParSalve": 2,
                "SupplyCost": 160.0
            },
        },
    },
    
    ("AGM_AGM65D_Maverick", "ATGM", None, False): { # 56
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 3500,
                "AimingTime": 0.3,
                "ShotsCountPerSalvo": 2,
                "SimultaneousShotsCount": 1,
                "AffichageMunitionParSalve": 2,
                "SupplyCost": 160.0
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
        "SupplyCost": 115.0,
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
                "SpeedGRU": 350,
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
                "SpeedGRU": 311,
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
                "SpeedGRU": 622,
            },
        },
        "SupplyCost": 80.0,
        "WeaponDescriptor": {
            "SalvoLengths": [16, 8, 6, 4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 622,
        },
    },
    
    ("AGM_9K121_Vikhr", "ATGM", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 24,
            },
            "hit_roll": {
                "Moving": 50,
            },
            "parent_membr": {
                "SpeedGRU": 2800,
                "MaxAccelerationGRU": 1400,
            },
        },
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [12],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 2800,
            "MaxAccelerationGRU": 1400,
        },
    },
    
    ("AGM_9K121_Vikhr_avion_ripple2", "AGM", None, False): { # 36
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
                "SpeedGRU": 2800,
                "MaxAccelerationGRU": 1400,
                "AimingTime": 0.3,
            },
        },
        "SupplyCost": 90.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 2800,
            "MaxAccelerationGRU": 1400,
        },
    },
    
    ("Bomb_KAB_500Kr", "LGB", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_pgb_bomb",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
            },
            "parent_membr": {
                "add": [34, "IsFireAndForget = True"],
                "TraitsToken": ['MOTION', 'F&F', 'HE'],
                "TimeBetweenTwoShots": 1.2,
                "TimeBetweenTwoFx": 1.2,
                "MaximumRangeGRU": 3850,
                "AngleDispersion": 0.008726646,
                "DispersionAtMaxRangeGRU": 250,
                "DispersionAtMinRangeGRU": 250,
                "RadiusSplashPhysicalDamagesGRU": 100,
                "RadiusSplashSuppressDamagesGRU": 133,
                "SpeedGRU": 1400,
                "MaxAccelerationGRU": 700,
                "TimeBetweenTwoSalvos": 1.2,
                "NbSalvosShootOnPosition": 1,
                "SimultaneousShotsCount": 1,
            },
        },
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 1400,
            "MaxAccelerationGRU": 700,
            "AutoGyr": 0.5235988, # 30 degrees
        },
    },
    
    ("Bomb_KAB_1500L", "LGB", None, False): { # 152
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_pgb_bomb",
            },
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "add": [34, "IsFireAndForget = True"],
                "Caliber": ("Laser Designation", "KNIPQIBDLF"),
                "TraitsToken": ['MOTION', 'F&F', 'HE'],
                "TimeBetweenTwoShots": 0.7,
                "TimeBetweenTwoFx": 0.7,
                "MaximumRangeGRU": 3850,
                "AngleDispersion": 0.008726646,
                "DispersionAtMaxRangeGRU": 500,
                "DispersionAtMinRangeGRU": 500,
                "RadiusSplashPhysicalDamagesGRU": 120,
                "RadiusSplashSuppressDamagesGRU": 160,
                "SpeedGRU": 1400,
                "MaxAccelerationGRU": 700,
                "TimeBetweenTwoSalvos": 0.7,
                "SimultaneousShotsCount": 1,
            },
        },
        "SupplyCost": 160.0,
        "WeaponDescriptor": {
            "SalvoLengths": [3, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 1400,
            "MaxAccelerationGRU": 700,
            "AutoGyr": 0.5235988, # 30 degrees
        },
    },
    
    ("Bomb_KAB_1500Kr", "LGB", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_pgb_bomb",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
            },
            "parent_membr": {
                "add": [34, "IsFireAndForget = True"],
                "TraitsToken": ['MOTION', 'F&F', 'HE'],
                "TimeBetweenTwoShots": 1.2,
                "TimeBetweenTwoFx": 1.2,
                "MaximumRangeGRU": 3850,
                "AngleDispersion": 0.008726646,
                "DispersionAtMaxRangeGRU": 500,
                "DispersionAtMinRangeGRU": 500,
                "RadiusSplashPhysicalDamagesGRU": 120,
                "RadiusSplashSuppressDamagesGRU": 160,
                "SpeedGRU": 1400,
                "MaxAccelerationGRU": 700,
                "TimeBetweenTwoSalvos": 1.2,
                "NbSalvosShootOnPosition": 1,
            },
        },
        "SupplyCost": 160.0,
        "WeaponDescriptor": {
            "SalvoLengths": [3, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 1400,
            "MaxAccelerationGRU": 700,
            "AutoGyr": 0.5235988, # 30 degrees
        },
    },
    
    ("Bomb_GBU_10", "LGB", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_pgb_bomb",
            },
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "add": [34, "IsFireAndForget = True"],
                "Caliber": ("Laser Designation", "KNIPQIBDLF"),
                "TraitsToken": ['MOTION', 'F&F', 'HE'],
                "TimeBetweenTwoShots": 0.7,
                "TimeBetweenTwoFx": 0.7,
                "MaximumRangeGRU": 3850,
                "AngleDispersion": 0.008726646,
                "DispersionAtMaxRangeGRU": 500,
                "DispersionAtMinRangeGRU": 500,
                "RadiusSplashPhysicalDamagesGRU": 120,
                "RadiusSplashSuppressDamagesGRU": 160,
                "SpeedGRU": 1400,
                "MaxAccelerationGRU": 700,
                "TimeBetweenTwoSalvos": 0.7,
                "SimultaneousShotsCount": 1,
            },
        },
        "SupplyCost": 140.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 1400,
            "MaxAccelerationGRU": 700,
            "AutoGyr": 0.5235988, # 30 degrees
        },
    },

    ("Bomb_GBU_12", "LGB", None, False): { # 147
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_pgb_bomb",
            },
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "add": [34, "IsFireAndForget = True"],
                "Caliber": ("Laser Designation", "KNIPQIBDLF"),
                "TraitsToken": ['MOTION', 'F&F', 'HE'],
                "TimeBetweenTwoShots": 0.7,
                "TimeBetweenTwoFx": 0.7,
                "MaximumRangeGRU": 3850,
                "AngleDispersion": 0.008726646,
                "DispersionAtMaxRangeGRU": 150,
                "DispersionAtMinRangeGRU": 150,
                "RadiusSplashPhysicalDamagesGRU": 90,
                "RadiusSplashSuppressDamagesGRU": 120,
                "SpeedGRU": 1400,
                "MaxAccelerationGRU": 700,
                "TimeBetweenTwoSalvos": 0.7,
                "SimultaneousShotsCount": 1,
            },
        },
        "SupplyCost": 85.0,
        "WeaponDescriptor": {
            "SalvoLengths": [4, 2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 1400,
            "MaxAccelerationGRU": 700,
            "AutoGyr": 0.5235988, # 30 degrees
        },
    },
    
    # "CPU-123" is a made up term for GBU-16 by Eduard Brassin scale models
    ("Bomb_CPU_123", "LGB", None, False): {
        "Ammunition": {
            "display": "GBU-16",
            "token": "THMDZGKPIM",
            "Arme": {
                "Family": "DamageFamily_pgb_bomb",
            },
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "add": [34, "IsFireAndForget = True"],
                "Caliber": ("Laser Designation", "KNIPQIBDLF"),
                "TraitsToken": ['MOTION', 'F&F', 'HE'],
                "TimeBetweenTwoShots": 0.7,
                "TimeBetweenTwoFx": 0.7,
                "MaximumRangeGRU": 3850,
                "AngleDispersion": 0.008726646,
                "DispersionAtMaxRangeGRU": 250,
                "DispersionAtMinRangeGRU": 250,
                "RadiusSplashPhysicalDamagesGRU": 100,
                "RadiusSplashSuppressDamagesGRU": 133,
                "SpeedGRU": 1400,
                "MaxAccelerationGRU": 700,
                "TimeBetweenTwoSalvos": 0.7,
                "SimultaneousShotsCount": 1,
            },
        },
        "SupplyCost": 100.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 1400,
            "MaxAccelerationGRU": 700,
            "AutoGyr": 0.5235988, # 30 degrees
        },
    },
    
    ("Bomb_GBU_27", "LGB", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_pgb_bomb",
            },
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "add": [34, "IsFireAndForget = True"],
                "Caliber": ("Laser Designation", "KNIPQIBDLF"),
                "TraitsToken": ['MOTION', 'F&F', 'HE'],
                "TimeBetweenTwoShots": 0.7,
                "TimeBetweenTwoFx": 0.7,
                "MaximumRangeGRU": 3850,
                "AngleDispersion": 0.008726646,
                "DispersionAtMaxRangeGRU": 500,
                "DispersionAtMinRangeGRU": 500,
                "RadiusSplashPhysicalDamagesGRU": 120,
                "RadiusSplashSuppressDamagesGRU": 160,
                "SpeedGRU": 1400,
                "MaxAccelerationGRU": 700,
                "TimeBetweenTwoSalvos": 0.7,
                "SimultaneousShotsCount": 1,
            },
        },
        "SupplyCost": 140.0,
        "WeaponDescriptor": {
            "SalvoLengths": [2, 1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 1400,
            "MaxAccelerationGRU": 700,
            "AutoGyr": 0.5235988, # 30 degrees
        },
    },
    
    ("AGM_AS30L", "AGM", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SpeedGRU": 2800,
                "MaxAccelerationGRU": 1400,
                "AimingTime": 0.3,
                "SupplyCost": 70.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 2800,
            "MaxAccelerationGRU": 1400,
        },
    },
}
# fmt: on
