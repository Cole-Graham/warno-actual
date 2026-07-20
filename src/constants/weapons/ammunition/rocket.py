"""Rocket weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("RocketAir_Zuni_1272mm_salvolength8", "rocket", None, False): { # 637
        "Ammunition": {
            "parent_membr": {
                # TODO: Decide if I want to scale helo rocket stats the same as any other rockets (caliber + 1 tier = splash radius)
                # "PhysicalDamages": 1.5,
                # "SuppressDamages": 162,
                "RadiusSplashPhysicalDamagesGRU": 21,
                "RadiusSplashSuppressDamagesGRU": 44,
                # "TimeBetweenTwoShots": 0.5,
                # "TimeBetweenTwoFx": 0.5,
            },
        },
    },

    # ("RocketAir_Zuni_1272mm_salvolength16", "rocket", None, False): { # 636
    #     "Ammunition": {
    #         "parent_membr": {
    #             "RadiusSplashPhysicalDamagesGRU": 21,
    #             "RadiusSplashSuppressDamagesGRU": 44,
    #             "SupplyCost": 192.0,
    #         },
    #     },
    # },

    ("RocketAir_Zuni_1272mm_avion_salvolength8", "rocket", "RocketAir_Zuni_1272mm_salvolength8", True): { # Zuni's on the German F4F
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "RadiusSplashPhysicalDamagesGRU": 21,
                "RadiusSplashSuppressDamagesGRU": 44,
                "SupplyCost": 60.0,
            },
        },
    },
    
    ("RocketAir_Zuni_1272mm_avion_salvolength16", "rocket", "RocketAir_Zuni_1272mm_salvolength16", True): { # Zuni's on the German F4F
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "RadiusSplashPhysicalDamagesGRU": 21,
                "RadiusSplashSuppressDamagesGRU": 44,
                "SupplyCost": 90.0,
            },
        },
    },

    ("RocketAir_Zuni_1272mm_salvolength24", "rocket", "RocketAir_Zuni_1272mm_x24_avion", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "RadiusSplashPhysicalDamagesGRU": 21,
                "RadiusSplashSuppressDamagesGRU": 44,
            },
        },
    },

    ("RocketAir_Zuni_1272mm_x24_avion", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "RadiusSplashPhysicalDamagesGRU": 21,
                "RadiusSplashSuppressDamagesGRU": 44,
                "SupplyCost": 120.0,
            },
        },
    },
    
    ("RocketAir_SNEB_68mm_x18_helo", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
            },
        },
    },
    
    ("RocketAir_SNEB_68mm_avion_salvolength18", "rocket", "RocketAir_SNEB_68mm_x18_helo", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "TimeBetweenTwoSalvos": 2.0,
                "SupplyCost": 30.0,
            },
        },
    },
    
    ("RocketAir_SNEB_68mm_salvolength36", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "NbSalvosShootOnPosition": 1,
            },
        },
    },

    ("RocketAir_SNEB_68mm_avion_salvolength36", "rocket", "RocketAir_SNEB_68mm_salvolength36", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 60.0,
                "NbSalvosShootOnPosition": 1,
            },
        },
    },
    
    ("RocketAir_SNEB_68mm_salvolength12", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 20,
            },
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "TimeBetweenTwoSalvos": 0.5,
                "ShotsCountPerSalvo": 2,
                "SupplyCost": 6.0,
                "NbSalvosShootOnPosition": 6,
                "AffichageMunitionParSalve": 2,
            },
        },
        "WeaponDescriptor": {
            "Salves": 6,
        },
    },

    ("RocketAir_SNEB_68mm_avion_salvolength12", "rocket", "RocketAir_SNEB_68mm_salvolength12", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 20.0,
            },
        },
    },

    ("RocketAir_SNEB_68mm_avion_salvolength38", "rocket", "RocketAir_SNEB_68mm_salvolength38", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 60.0,
            },
        },
    },

    ("RocketAir_S5_57mm_salvolength8", "rocket", None, False): { # 627
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,  
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
            },
        },
    },
    
    ("RocketAir_S5_57mm_salvolength16", "rocket", None, False): { # 627
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,  
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
            },
        },
    },

    ("RocketAir_S5_57mm_avion_salvolength8", "rocket", "RocketAir_S5_57mm_salvolength8", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "SupplyCost": 15.0,
            },
        },
    },

    ("RocketAir_S5_57mm_avion_salvolength16", "rocket", "RocketAir_S5_57mm_salvolength16", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "SupplyCost": 25.0,
            },
        },
    },

    ("RocketAir_S5_57mm_avion_salvolength64", "rocket", "RocketAir_S5_57mm_salvolength64", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "SupplyCost": 50.0,
            },
        },
    },

    ("RocketAir_S5_57mm_avion_salvolength96", "rocket", "RocketAir_S5_57mm_salvolength96", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "SupplyCost": 70.0,
            },
        },
    },
    
    ("RocketAir_S5_57mm_avion_salvolength32", "rocket", "RocketAir_S5_57mm_salvolength32", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },                
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,  
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "ShotsCountPerSalvo": 32,
                "SupplyCost": 35.0,
                "NbSalvosShootOnPosition": 2,
                "SimultaneousShotsCount": 2,
                "AffichageMunitionParSalve": 32,
            },
        },
    },

     ("RocketAir_Grom_57mm_salvolength16", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },                
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,  
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "AffichageMunitionParSalve": 16,
            },
        },
    },

    ("RocketAir_Grom_57mm_avion_salvolength16", "rocket", "RocketAir_Grom_57mm_salvolength16", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },                
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,  
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "ShotsCountPerSalvo": 32,
                "SupplyCost": 25.0,
                "NbSalvosShootOnPosition": 2,
                "SimultaneousShotsCount": 2,
                "AffichageMunitionParSalve": 16,
            },
        },
    },

    ("RocketAir_122_JROF_L_122mm_avion_salvolength4", "rocket", "RocketAir_122_JROF_L_122mm_salvolength4", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "SupplyCost": 40.0,
            },
        },
    },

    ("RocketAir_CRV7_70mm_avion_salvolength38", "rocket", "RocketAir_CRV7_70mm_salvolength38", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "SupplyCost": 60.0,
            },
        },
    },

    ("RocketAir_CRV7_70mm_avion_salvolength19", "rocket", "RocketAir_CRV7_70mm_salvolength19", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "SupplyCost": 30.0,
            },
        },
    },

    ("RocketAir_SBAT_70mm_avion_salvolength7", "rocket", "RocketAir_SBAT_70mm_salvolength7", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "SupplyCost": 15.0,
            },
        },
    },

    ("RocketAir_SBAT_127mm_salvolength8", "rocket", "RocketAir_SBAT_127mm_x8_avion", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
            },
        },
    },

    ("RocketAir_SBAT_127mm_x8_avion", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "SupplyCost": 50.0,
            },
        },
    },

    ("RocketAir_FFAR_70mm_x24_avion", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "SupplyCost": 40.0,
            },
        },
    },

    ("RocketAir_HVAR_127mm_avion_salvolength8", "rocket", "RocketAir_HVAR_127mm_salvolength8", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "SupplyCost": 50.0,
            },
        },
    },

    ("RocketAir_TBrandt_100mm_avion_salvolength8", "rocket", "RocketAir_TBrandt_100mm_salvolength8", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "SupplyCost": 40.0,
            },
        },
    },

    ("RocketAir_122_JROF_L_122mm_salvolength54", "rocket", "RocketAir_122_JROF_L_122mm_x54_avion", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
            },
        },
    },
     
    ("RocketAir_S25O_420mm_salvolength2", "rocket", None, False): {
        "Ammunition": {
            "parent_membr": {
                "Caliber": ("60kg TNTe", "IFSVBUYZTU"),
                "MaximumRangeGRU": 2275,
                "RadiusSplashPhysicalDamagesGRU": 90,
                "RadiusSplashSuppressDamagesGRU": 120,
                "PhysicalDamages": 7.2,
                "SuppressDamages": 420,
                "SupplyCost": 80.0,
            },
        },
    },

    ("RocketAir_S25O_420mm_avion_salvolength2", "rocket", "RocketAir_S25O_420mm_salvolength2", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "Caliber": ("60kg TNTe", "IFSVBUYZTU"),
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 90,
                "RadiusSplashSuppressDamagesGRU": 120,
                "PhysicalDamages": 7.2,
                "SuppressDamages": 420,
                "SupplyCost": 60.0,
            },
        },
    },
    
    ("RocketAir_S24_240mm_salvolength2", "rocket", None, False): { # 619
        "Ammunition": {
            "parent_membr": {
                "Caliber": ("30kg TNTe", "YCGKZDIBDZ"),
                "RadiusSplashPhysicalDamagesGRU": 60,
                "RadiusSplashSuppressDamagesGRU": 80,
                "PhysicalDamages": 6.0,
                "SuppressDamages": 390, 
                "SupplyCost": 80.0,
            },
        },
    },

    ("RocketAir_S24_240mm_avion_salvolength2", "rocket", "RocketAir_S24_240mm_salvolength2", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "Caliber": ("30kg TNTe", "YCGKZDIBDZ"),
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 60,
                "RadiusSplashSuppressDamagesGRU": 80,
                "PhysicalDamages": 6.0,
                "SuppressDamages": 390,
                "SupplyCost": 60.0,
            },
        },
    },

    ("RocketAir_S24_240mm_salvolength4", "rocket", "RocketAir_S24_240mm_salvolength2", True): {
        "Ammunition": {
            "parent_membr": {
                "Caliber": ("30kg TNTe", "YCGKZDIBDZ"),
                "MaximumRangeGRU": 2275,
                "RadiusSplashPhysicalDamagesGRU": 60,
                "RadiusSplashSuppressDamagesGRU": 80,
                "PhysicalDamages": 6.0,
                "SuppressDamages": 390,
                "SupplyCost": 120.0,
                "ShotsCountPerSalvo": 4,
                "NbSalvosShootOnPosition": 1,
                "AffichageMunitionParSalve": 4,
            },
        },
    },

    ("RocketAir_S24_240mm_avion_salvolength4", "rocket", "RocketAir_S24_240mm_salvolength2", True): { # 619
        "Ammunition": {
            "parent_membr": {
                "Caliber": ("30kg TNTe", "YCGKZDIBDZ"),
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 60,
                "RadiusSplashSuppressDamagesGRU": 80,
                "PhysicalDamages": 6.0,
                "SuppressDamages": 390,
                "SupplyCost": 80.0,
                "ShotsCountPerSalvo": 4,
                "NbSalvosShootOnPosition": 1,
                "AffichageMunitionParSalve": 4,
            },
        },
    },
    
    ("RocketAir_S24_240mm_salvolength3", "rocket", None, False): {
        "Ammunition": {
            "parent_membr": {
                "Caliber": ("30kg TNTe", "YCGKZDIBDZ"),
                "MaximumRangeGRU": 2275,
                "RadiusSplashPhysicalDamagesGRU": 60,
                "RadiusSplashSuppressDamagesGRU": 80,
                "PhysicalDamages": 6.0,
                "SuppressDamages": 390,
                "SupplyCost": 100.0,
            },
        },
    },

    ("RocketAir_S24_240mm_avion_salvolength3", "rocket", "RocketAir_S24_240mm_salvolength3", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "Caliber": ("30kg TNTe", "YCGKZDIBDZ"),
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 60,
                "RadiusSplashSuppressDamagesGRU": 80,
                "PhysicalDamages": 6.0,
                "SuppressDamages": 390,
                "SupplyCost": 70.0,
            },
        },
    },

    ("RocketAir_S13_122mm_avion_salvolength20", "rocket", "RocketAir_S13_122mm_salvolength20", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 18,
                "RadiusSplashSuppressDamagesGRU": 36,
                "PhysicalDamages": 1.25,
                "SuppressDamages": 125,
                "SupplyCost": 120.0,
            },
        },
    },

    ("RocketAir_S13_122mm_salvolength20", "rocket", None, False): { # 618
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 18,
                "RadiusSplashSuppressDamagesGRU": 36,
                "PhysicalDamages": 1.25,
                "SuppressDamages": 125, 
                "SupplyCost": 160.0,
            },
        },
    },
    
    ("RocketAir_S13_122mm_avion_salvolength10", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 18,
                "RadiusSplashSuppressDamagesGRU": 36,
                "PhysicalDamages": 1.25,
                "SuppressDamages": 125, 
                "SupplyCost": 80.0,
            },
        },
    },

    ("RocketAir_S13_122mm_salvolength10", "rocket", None, False): { # 616
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 18,
                "RadiusSplashSuppressDamagesGRU": 36,
                "PhysicalDamages": 1.25,
                "SuppressDamages": 125, 
                "SupplyCost": 100.0,
            },
        },
    },
    
    ("RocketAir_Hydra_70mm_salvolength76", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 228.0,
            },
        },
    },

    ("RocketAir_Hydra_70mm_avion_salvolength76", "rocket", "RocketAir_Hydra_70mm_salvolength76", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 140.0,
            },
        },
    },
    
    ("RocketAir_Hydra_70mm_salvolength38", "rocket", "RocketAir_Hydra_70mm_x38_avion", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 114.0,
                "SimultaneousShotsCount": 1,
            },
        },
    },

    ("RocketAir_Hydra_70mm_x38_avion", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 60.0,
                "SimultaneousShotsCount": 6,
            },
        },
    },

    ("RocketAir_Hydra_70mm_salvolength114", "rocket", "RocketAir_Hydra_70mm_x114_avion", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "RadiusSplashPhysicalDamagesGRU": 70,
                "RadiusSplashSuppressDamagesGRU": 105,
                "PhysicalDamages": 1.8,
                "SuppressDamages": 189,
                "ShotsCountPerSalvo": 114,
                "SupplyCost": 342.0,
                "NbSalvosShootOnPosition": 1,
                "SimultaneousShotsCount": 1,
                "AffichageMunitionParSalve": 114,
            },
        },
    },
    
    ("RocketAir_Hydra_70mm_x114_avion", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 0,
                "Moving": 0,
            },
            "parent_membr": {
                "add": [33, "ComputeArmorFromImpactLocation = True"],
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "MaximumRangeGRU": 3625,
                "MinimumRangeGRU": 350,
                "SalvoShotsSorted": True,
                "RadiusSplashPhysicalDamagesGRU": 70,
                "RadiusSplashSuppressDamagesGRU": 105,
                "PhysicalDamages": 1.8,
                "SuppressDamages": 189,
                "TargetOnlyOneUnitInDistrict": False,
                "ShotsCountPerSalvo": 114,
                "SupplyCost": 180.0,
                "NbSalvosShootOnPosition": 1,
                "SimultaneousShotsCount": 6,
                "AffichageMunitionParSalve": 114,
            },
        },
    },
    
    # ("RocketAir_Hydra_70mm_x114_avion", "rocket", "RocketAir_Hydra_70mm_x38_avion", True): {
    #     "Ammunition": {
    #         "hit_roll": {
    #             "Idling": 15,
    #             "Moving": 15,
    #         },
    #         "parent_membr": {
    #             "MaximumRangeGRU": 2800,
    #             "RadiusSplashPhysicalDamagesGRU": 14,
    #             "RadiusSplashSuppressDamagesGRU": 21,
    #             "TimeBetweenTwoShots": 0.1,
    #             "TimeBetweenTwoFx": 0.1,
    #             "PhysicalDamages": 0.75,
    #             "SuppressDamages": 75,
    #             "ShotsCountPerSalvo": 114,
    #             "SupplyCost": 342.0,
    #             "NbSalvosShootOnPosition": 1,
    #             "SimultaneousShotsCount": 6,
    #             "AffichageMunitionParSalve": 114,
    #         },
    #     },
    # },

    ("RocketAir_Hydra_70mm_salvolength19", "rocket", None, False): { # 609
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 114.0,
            },
        },
    },

    ("RocketAir_Hydra_70mm_avion_salvolength19", "rocket", "RocketAir_Hydra_70mm_salvolength19", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 30.0,
            },
        },
    },

    ("RocketAir_Hydra_70mm_x31_M229", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
            },
        },
    },

    ("RocketAir_Hydra_70mm_x31_M229_avion", "rocket", "RocketAir_Hydra_70mm_x31_M229", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
            },
        },
    },

    ("RocketAir_JRRO_130_130mm_salvolength8", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
            },
        },
    },

    ("RocketAir_JRRO_130_130mm_avion_salvolength8", "rocket", "RocketAir_JRRO_130_130mm_salvolength8", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
            },
        },
    },

    ("RocketAir_Hydra_70mm_salvolength14", "rocket", None, False): { # 608
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 20,
            },
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "TimeBetweenTwoSalvos": 0.5,
                "ShotsCountPerSalvo": 2,
                "SupplyCost": 6.0,
                "NbSalvosShootOnPosition": 7,
                "AffichageMunitionParSalve": 2,
            },
        },
        "WeaponDescriptor": {
            "Salves": 7,
        },
    },

    ("RocketAir_B8_80mm_salvolength80", "rocket", None, False): { # 594
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
            },
        },
    },

    ("RocketAir_B8_80mm_avion_salvolength80", "rocket", "RocketAir_B8_80mm_salvolength80", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
                "SupplyCost": 120.0,
            },
        },
    },

    ("RocketAir_B8_80mm_salvolength40", "rocket", None, False): { # 594
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
            },
        },
    },
    
    ("RocketAir_B8_80mm_avion_salvolength40", "rocket", None, False): { # 594
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
                "SupplyCost": 80.0,
            },
        },
    },

    ("RocketAir_B8_80mm_salvolength20", "rocket", None, False): { # Mi-8TV UPK, Sokol
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
            },
        },
    },

    ("RocketAir_B8_80mm_avion_salvolength20", "rocket", "RocketAir_B8_80mm_salvolength20", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
                "SupplyCost": 50.0,
            },
        },
    },
    
    ("RocketAir_B8_80mm_salvolength10", "rocket", None, False): { # 594
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 2275,
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
            },
        },
    },

    ("RocketAir_B8_80mm_Avion_salvolength10", "rocket", "RocketAir_B8_80mm_salvolength10", True): { # 593
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
                "SupplyCost": 35.0,
            },
        },
    },

    # SNEB Pod's maybe should be swapped to 1 salvo of 36 rather than 2 salvos of 18? Would Fix the issue of the Gina not being able to dump all its rockets



}
# fmt: on
