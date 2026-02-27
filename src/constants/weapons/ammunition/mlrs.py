"""MLRS weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    
    ("RocketArt_9M55K5_300mm", "MLRS", None, False): { # SMERCH
        "Ammunition": {
            "Arme": {
                "Index": 4,
                "Family": "DamageFamily_dpicm",
            },
            "parent_membr": {
                "SuppressDamages": 85,
                "RadiusSplashPhysicalDamagesGRU": 250,
                "RadiusSplashSuppressDamagesGRU": 300,
                "DispersionAtMaxRangeGRU": 900,
                "DispersionAtMinRangeGRU": 300,
                "AimingTime": 18.0,
                "ShotsCountPerSalvo": 48,
                "SupplyCost": 1200.0,
                "SimultaneousShotsCount": 4,
                "AffichageMunitionParSalve": 12,
            },
        },
    },
    
    ("RocketArt_M24F_240mm_salvolength12", "MLRS", None, False): { # BM-24M
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 8.6,
                "SuppressDamages": 540,
                "DispersionAtMaxRangeGRU": 560,
                "DispersionAtMinRangeGRU": 240,
                "RadiusSplashPhysicalDamagesGRU": 240,
                "RadiusSplashSuppressDamagesGRU": 320,
                "SupplyCost": 960.0,
            },
        },
    },
    
    ("RocketArt_thermobaric_220mm_salvolength30", "MLRS", None, False): { # 657
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_thermobarique",
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'thermobaric'],
                "MaximumRangeGRU": 3000,
                "DispersionAtMaxRangeGRU": 700,
                "DispersionAtMinRangeGRU": 350,
                "PhysicalDamages": 10.0,
                "SuppressDamages": 467,
                "RadiusSplashPhysicalDamagesGRU": 220,
                "RadiusSplashSuppressDamagesGRU": 293,
                "TimeBetweenTwoSalvos": 240.0,
                "SupplyCost": 2100.0,
                "FlightTimeForSpeed": 7.0,
                "DistanceForSpeedGRU": 3063,
            },
        },
    },

    ("RocketArt_M26_227mm_Cluster", "MLRS", None, False): { # 651
        "Ammunition": {
            "display": "M26 'Steel Rain'",
            "token": "ULWAVTGKUK",
            "Arme": {
                "Index": 3,
                "Family": "DamageFamily_dpicm",
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.8,
                "TimeBetweenTwoFx": 1.8,
                "RadiusSplashPhysicalDamagesGRU": 400,
                "PhysicalDamages": 3,
                "RadiusSplashSuppressDamagesGRU": 533,
                "SuppressDamages": 20,
                "DispersionAtMaxRangeGRU": 1500,
                "DispersionAtMinRangeGRU": 500,
                "AimingTime": 18.0,
                "TimeBetweenTwoSalvos": 130.0,
                "ShotsCountPerSalvo": 144,
                "SupplyCost": 960.0,
                "SimultaneousShotsCount": 12,
                "AffichageMunitionParSalve": 12,
            },
        },
    },

    ("RocketArt_M26_227mm", "MLRS", None, False): { # 651
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 7.2,
                "SuppressDamages": 467,
                "DispersionAtMaxRangeGRU": 848,
                "RadiusSplashPhysicalDamagesGRU": 283,
                "RadiusSplashSuppressDamagesGRU": 377,
                "AimingTime": 18.0,
            },
        },
    },

    ("RocketArt_M21OF_122mm_salvolength12", "MLRS", None, False): { # 649
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
                "SupplyCost": 174.0,
            },
        },
    },

    ("RocketArt_M21OF_122mm", "MLRS", None, False): { # 646
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
                "TimeBetweenTwoSalvos": 220.0,
                "SupplyCost": 580.0,
            },
        },
    },

    ("RocketArt_M21OF_122mm_RM70", "MLRS", "RocketArt_M21OF_122mm", True): { # 646
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
                "TimeBetweenTwoSalvos": 130.0,
                "SupplyCost": 580.0,
            },
        },
    },
    
    ("RocketArt_M21OF_122mm_napalm", "MLRS", None, False): { # BM-21 [NPLM]
        "Ammunition": {
            "parent_membr": {
                "ImpactHappening": "'Roquette110Mm130MmClusterNapalm'",
                "PhysicalDamages": 0.5,
                "SuppressDamages": 50,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
                "TimeBetweenTwoSalvos": 220.0,
                "SupplyCost": 290.0,
                "FireDescriptor": "$/GFX/Weapon/Descriptor_Fire_Incendiary_53m",
            },
        },
    },
    
    ("RocketArt_M21OF_122mm_RM70_napalm", "MLRS", "RocketArt_M21OF_122mm_napalm", True): { # RM-70 [NPLM]
        "Ammunition": {
            "parent_membr": {
                "ImpactHappening": "'Roquette110Mm130MmClusterNapalm'",
                "PhysicalDamages": 0.5,
                "SuppressDamages": 50,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
                "TimeBetweenTwoSalvos": 130.0,
                "SupplyCost": 290.0,
                "FireDescriptor": "$/GFX/Weapon/Descriptor_Fire_Incendiary_53m",
            },
        },
    },
    
    ("MLRS_Hydra_70mm_salvolength114", "MLRS", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 2.5,
                "SuppressDamages": 180,
                "RadiusSplashPhysicalDamagesGRU": 94,
                "RadiusSplashSuppressDamagesGRU": 125,
            },
        },
    },

    ("MLRS_140mm_towed", "MLRS", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 5.1,
                "SuppressDamages": 400,
                "RadiusSplashPhysicalDamagesGRU": 180,
                "RadiusSplashSuppressDamagesGRU": 240,
            },
        },
    },

    # ("RocketArt_M14OF_140mm_salvolength12", "MLRS", None, False): {
    #     "Ammunition": {
    #         "parent_membr": {
    #             "PhysicalDamages": 5.1,
    #             "SuppressDamages": 400,
    #             "RadiusSplashPhysicalDamagesGRU": 180,
    #             "RadiusSplashSuppressDamagesGRU": 240,
    #         },
    #     },
    # },

    ("RocketArt_M14OF_140mm_salvolength16", "MLRS", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 5.1,
                "SuppressDamages": 400,
                "RadiusSplashPhysicalDamagesGRU": 180,
                "RadiusSplashSuppressDamagesGRU": 240,
            },
        },
    },

    ("RocketArt_LARS_110mm", "MLRS", None, False): { # 646
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
                "TimeBetweenTwoSalvos": 132.0,
                "SupplyCost": 522.0,
            },
        },
    },
}
# fmt: on
