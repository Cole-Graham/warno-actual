"""MLRS weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    
    ("RocketArt_9M55K5_300mm", "MLRS", None, False): { # SMERCH
        "Ammunition": {
            "Arme": {
                "Index": 10,
            },
            "parent_membr": {
                "ImpactHappening": "'MLRSClusterAP200m'",
                "RadiusSplashPhysicalDamagesGRU": 200,
                "RadiusSplashSuppressDamagesGRU": 267,
                "PhysicalDamages": 1.0,
                "DispersionAtMaxRangeGRU": 900,
                "DispersionAtMinRangeGRU": 380,
                "AimingTime": 18.0,
                "ShotsCountPerSalvo": 12,
                "SupplyCost": 1200.0,
                "SimultaneousShotsCount": 1,
                "AffichageMunitionParSalve": 12,
            },
        },
    },
    
    ("RocketArt_MD24F_240mm_salvolength12", "MLRS", None, False): {
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
    
    ("RocketArt_9M27F_HE_220mm", "MLRS", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 7.1,
                "SuppressDamages": 460,
                "DispersionAtMaxRangeGRU": 848,
                # "RadiusSplashPhysicalDamagesGRU": 280,
                # "RadiusSplashSuppressDamagesGRU": 373,
                "RadiusSplashPhysicalDamagesGRU": 220,
                "RadiusSplashSuppressDamagesGRU": 293,
            },
        },
    },
    
    ("RocketArt_thermobaric_127mm_salvolength21", "MLRS", None, False): { # CATFAE
        "Ammunition": {
            "parent_membr": {
                "Caliber": ("150kg TNTe", "ITCUAAMSWN"),
                "ImpactHappening": "'BombeODABRPO'",
                "TimeBetweenTwoShots": 2.5,
                "TimeBetweenTwoFx": 2.5,
                "MaximumRangeGRU": 1400,
                "DispersionAtMaxRangeGRU": 250,
                "DispersionAtMinRangeGRU": 175,
                "PhysicalDamages": 5.0,
                "SuppressDamages": 250,
                "RadiusSplashPhysicalDamagesGRU": 110,
                "RadiusSplashSuppressDamagesGRU": 147,
                "AimingTime": 15.0,
                "SimultaneousShotsCount": 1,
                "PitchForParabolic": 0.9075712, # 52 degrees
            },
        },
    },
    
    ("RocketArt_thermobaric_220mm_salvolength30", "MLRS", None, False): { # Buratino
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_thermobarique",
            },
            "parent_membr": {
                "Caliber": ("250kg TNTe", "NDOAZJCZXQ"),
                "TraitsToken": ['STAT', 'thermobaric'],
                "MaximumRangeGRU": 3000,
                "DispersionAtMaxRangeGRU": 500,
                "DispersionAtMinRangeGRU": 250,
                "PhysicalDamages": 10.0,
                "SuppressDamages": 300,
                "RadiusSplashPhysicalDamagesGRU": 160,
                "RadiusSplashSuppressDamagesGRU": 213,
                "TimeBetweenTwoSalvos": 240.0,
                "SupplyCost": 2100.0,
                # "FlightTimeForSpeed": 7.0,
                # "DistanceForSpeedGRU": 3063,
            },
        },
    },

    ("RocketArt_M26_227mm_Cluster", "MLRS", None, False): { # 651
        "Ammunition": {
            "display": "M26 'Steel Rain'",
            "token": "ULWAVTGKUK",
            "Arme": {
                "Index": 9,
            },
            "parent_membr": {
                "ImpactHappening": "'MLRSClusterAP250m'",
                "TimeBetweenTwoShots": 1.8,
                "TimeBetweenTwoFx": 1.8,
                "RadiusSplashPhysicalDamagesGRU": 250,
                "PhysicalDamages": 1,
                "RadiusSplashSuppressDamagesGRU": 333,
                "SuppressDamages": 250,
                "DispersionAtMaxRangeGRU": 1000,
                "DispersionAtMinRangeGRU": 500,
                "ProjectileSpeedGRU": 750.0,
                "AimingTime": 18.0,
                "TimeBetweenTwoSalvos": 70.0, # Experimental, realistic short reload balanced with supply cost (130s -> 70s)
                "ShotsCountPerSalvo": 12,
                "SupplyCost": 1800.0, # 960 -> 1800 (same was Wargame SMERCH)
                "SimultaneousShotsCount": 1,
                "AffichageMunitionParSalve": 12,
                "PitchForParabolic": 0.52,
            },
        },
    },

    ("RocketArt_M26_227mm", "MLRS", None, False): { # 651
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 7.2,
                "SuppressDamages": 467,
                "DispersionAtMaxRangeGRU": 848,
                # "RadiusSplashPhysicalDamagesGRU": 283,
                # "RadiusSplashSuppressDamagesGRU": 377,
                "RadiusSplashPhysicalDamagesGRU": 227,
                "RadiusSplashSuppressDamagesGRU": 297,
                "AimingTime": 18.0,
            },
        },
    },

    ("RocketArt_M21OF_122mm_salvolength12", "MLRS", None, False): { # 649
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                # "RadiusSplashPhysicalDamagesGRU": 152,
                # "RadiusSplashSuppressDamagesGRU": 203,
                "RadiusSplashPhysicalDamagesGRU": 122,
                "RadiusSplashSuppressDamagesGRU": 163,
                "SupplyCost": 174.0,
            },
        },
    },

    ("RocketArt_M21OF_122mm", "MLRS", None, False): { # 646
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                # "RadiusSplashPhysicalDamagesGRU": 152,
                # "RadiusSplashSuppressDamagesGRU": 203,
                "RadiusSplashPhysicalDamagesGRU": 122,
                "RadiusSplashSuppressDamagesGRU": 163,
                "TimeBetweenTwoSalvos": 220.0,
                "SupplyCost": 580.0,
            },
        },
    },
    
    ("RocketArt_M21OF_122mm_salvolength36", "MLRS", None, False): { # MOR. 9k55 Grad 1
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.8,
                "SuppressDamages": 400,
                "RadiusSplashPhysicalDamagesGRU": 122,
                "RadiusSplashSuppressDamagesGRU": 163,
                "TimeBetweenTwoSalvos": 220.0,
                "SupplyCost": 522.0,
            },
        },
    },

    ("RocketArt_M21OF_122mm_RM70", "MLRS", "RocketArt_M21OF_122mm", True): { # 646
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                # "RadiusSplashPhysicalDamagesGRU": 152,
                # "RadiusSplashSuppressDamagesGRU": 203,
                "RadiusSplashPhysicalDamagesGRU": 122,
                "RadiusSplashSuppressDamagesGRU": 163,
                "TimeBetweenTwoSalvos": 130.0,
                "SupplyCost": 580.0,
            },
        },
    },
    
    ("RocketArt_M21OF_122mm_cluster_RM70", "MLRS", "RocketArt_M21OF_122mm_cluster", True): {
        "Ammunition": {
            "Arme": {
                "Index": 7,
            },
            "parent_membr": {
                "ImpactHappening": "'MLRSClusterAP125m'",   
                "PhysicalDamages": 1.0,
                "RadiusSplashPhysicalDamagesGRU": 125,
                "RadiusSplashSuppressDamagesGRU": 167,
                "DispersionAtMaxRangeGRU": 600,
                "DispersionAtMinRangeGRU": 250,
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
    
    ("RocketArt_9F53_122mm_cluster_salvolength50", "MLRS", None, False): { # Prima
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_clu_sol_hefrag",
                "Index": 6,
            },
            "parent_membr": {
                "ImpactHappening": "'MLRSClusterAP125m'",
                "PhysicalDamages": 1,
                "RadiusSplashPhysicalDamagesGRU": 125,
                "RadiusSplashSuppressDamagesGRU": 167,
                "DispersionAtMaxRangeGRU": 600,
                "DispersionAtMinRangeGRU": 250,
            },
        },
    },
    
    ("MLRS_Hydra_70mm_salvolength114", "MLRS", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 2.5,
                "SuppressDamages": 180,
                # "RadiusSplashPhysicalDamagesGRU": 94,
                # "RadiusSplashSuppressDamagesGRU": 125,
                "RadiusSplashPhysicalDamagesGRU": 70,
                "RadiusSplashSuppressDamagesGRU": 93,
            },
        },
    },

    ("MLRS_140mm_towed", "MLRS", None, False): {
        "Ammunition": {
            "parent_membr": {
                # These rockets appear half the length of the 140mm rockets on BM-14M, so
                # they either need to be dropped to 122mm Grad HE, or lowered range.
                #Going with the latter for now.
                "MaximumRangeGRU": 7500,
                "PhysicalDamages": 5.1,
                "SuppressDamages": 400,
                "RadiusSplashPhysicalDamagesGRU": 140,
                "RadiusSplashSuppressDamagesGRU": 187,
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
                # "RadiusSplashPhysicalDamagesGRU": 180,
                # "RadiusSplashSuppressDamagesGRU": 240,
                "RadiusSplashPhysicalDamagesGRU": 140,
                "RadiusSplashSuppressDamagesGRU": 187,
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
