"""Rocket weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("RocketAir_Zuni_1272mm_salvolength8", "rocket", None, False): { # 637
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 21,
                "RadiusSplashSuppressDamagesGRU": 44,
                "SupplyCost": 96.0,
            },
        },
    },

    ("RocketAir_Zuni_1272mm_salvolength16", "rocket", None, False): { # 636
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 21,
                "RadiusSplashSuppressDamagesGRU": 44,
                "SupplyCost": 192.0,
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
                "SupplyCost": 108.0,
            },
        },
    },
    
    ("RocketAir_SNEB_68mm_salvolength36", "rocket", None, False): {
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
                "SupplyCost": 114.0,
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
                "NbTirParSalves": 2,
                "SupplyCost": 6.0,
                "NbSalvosShootOnPosition": 6,
                "AffichageMunitionParSalve": 2,
            },
        },
        "WeaponDescriptor": {
            "Salves": 6,
        },
    },

    ("RocketAir_S5_57mm_salvolength8", "rocket", None, False): { # 627
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,  
                "TimeBetweenTwoShots": 0.2,
                "TimeBetweenTwoFx": 0.2,
                "SupplyCost": 16.0,
            },
        },
    },
    
    ("RocketAir_S5_57mm_avion_salvolength32", "rocket", "RocketAir_S5_57mm", True): {
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
                "NbTirParSalves": 32,
                "SupplyCost": 128.0,
                "NbSalvosShootOnPosition": 2,
                "NbrProjectilesSimultanes": 2,
                "AffichageMunitionParSalve": 32,
            },
        },
    },
    
    ("RocketAir_S24_240mm_salvolength2", "rocket", None, False): { # 619
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 60,
                "RadiusSplashSuppressDamagesGRU": 80,
                "PhysicalDamages": 6.0,
                "SuppressDamages": 390, 
                "SupplyCost": 64.0,
            },
        },
    },

    ("RocketAir_S24_240mm_avion_salvolength4", "rocket", "RocketAir_S24_240mm_salvolength2", True): { # 619
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 60,
                "RadiusSplashSuppressDamagesGRU": 80,
                "PhysicalDamages": 6.0,
                "SuppressDamages": 390,
                "SupplyCost": 128.0,
                "NbTirParSalves": 4,
                "NbSalvosShootOnPosition": 1,
                "AffichageMunitionParSalve": 4,
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
                "SupplyCost": 80.0,
            },
        },
    },
    
    ("RocketAir_Hydra_70mm_salvolength76", "rocket", None, False): {
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
                "SupplyCost": 228.0,
            },
        },
    },

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
                "NbTirParSalves": 2,
                "SupplyCost": 6.0,
                "NbSalvosShootOnPosition": 7,
                "AffichageMunitionParSalve": 2,
            },
        },
        "WeaponDescriptor": {
            "Salves": 7,
        },
    },

    ("RocketAir_B8_80mm_salvolength20", "rocket", None, False): { # 594
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TimeBetweenTwoShots": 0.3,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
                "SupplyCost": 120.0,
            },
        },
    },

    ("RocketAir_B8_80mm_salvolength10", "rocket", None, False): { # 593
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TimeBetweenTwoShots": 0.3,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
                "SupplyCost": 60.0,
            },
        },
    },
}
# fmt: on
