"""Rocket weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("RocketAir_Zuni_1272mm_x8", "rocket", None, False): { # 637
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 21,
                "RadiusSplashSuppressDamagesGRU": 44,
                "SupplyCost": 96,
            },
        },
    },

    ("RocketAir_Zuni_1272mm_x16", "rocket", None, False): { # 636
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 21,
                "RadiusSplashSuppressDamagesGRU": 44,
                "SupplyCost": 192,
            },
        },
    },
    
    ("RocketAir_SNEB_68mm_x36", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TempsEntreDeuxTirs": 0.1,
                "TempsEntreDeuxFx": 0.1,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 114,
                "NbSalvosShootOnPosition": 1,
            },
        },
    },
    
    ("RocketAir_SNEB_68mm_x12", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 20,
            },
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TempsEntreDeuxTirs": 0.2,
                "TempsEntreDeuxFx": 0.2,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "TempsEntreDeuxSalves": 0.55,
                "NbTirParSalves": 2,
                "SupplyCost": 6,
                "NbSalvosShootOnPosition": 6,
                "AffichageMunitionParSalve": 2,
            },
        },
        "WeaponDescriptor": {
            "Salves": 6,
        },
    },

    ("RocketAir_S5_57mm_x8", "rocket", None, False): { # 627
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,  
                "TempsEntreDeuxTirs": 0.2,
                "TempsEntreDeuxFx": 0.2,
                "SupplyCost": 16,
            },
        },
    },
    
    ("RocketAir_S5_57mm_x32_avion", "rocket", "RocketAir_S5_57mm", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },                
            "parent_membr": {
                "PorteeMaximaleGRU": 2450,
                "RadiusSplashPhysicalDamagesGRU": 9,
                "RadiusSplashSuppressDamagesGRU": 15,  
                "TempsEntreDeuxTirs": 0.1,
                "TempsEntreDeuxFx": 0.1,
                "NbTirParSalves": 32,
                "SupplyCost": 128,
                "NbSalvosShootOnPosition": 2,
                "NbrProjectilesSimultanes": 2,
                "AffichageMunitionParSalve": 32,
            },
        },
    },
    
    ("RocketAir_S24_240mm_x2", "rocket", None, False): { # 619
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 60,
                "RadiusSplashSuppressDamagesGRU": 80,
                "PhysicalDamages": 6.0,
                "SuppressDamages": 390, 
                "SupplyCost": 64,
            },
        },
    },

    ("RocketAir_S13_122mm_x20", "rocket", None, False): { # 618
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 18,
                "RadiusSplashSuppressDamagesGRU": 36,
                "PhysicalDamages": 1.25,
                "SuppressDamages": 125, 
                "SupplyCost": 160,
            },
        },
    },
    
    ("RocketAir_S13_122mm_x10_avion", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 30,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 18,
                "RadiusSplashSuppressDamagesGRU": 36,
                "PhysicalDamages": 1.25,
                "SuppressDamages": 125, 
                "SupplyCost": 80,
            },
        },
    },

    ("RocketAir_S13_122mm_x10", "rocket", None, False): { # 616
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
                "SupplyCost": 80,
            },
        },
    },
    
    ("RocketAir_Hydra_70mm_x76", "rocket", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 20,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 2625,
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TempsEntreDeuxTirs": 0.1,
                "TempsEntreDeuxFx": 0.1,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 228,
            },
        },
    },

    ("RocketAir_Hydra_70mm_x19", "rocket", None, False): { # 609
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TempsEntreDeuxTirs": 0.2,
                "TempsEntreDeuxFx": 0.2,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "SupplyCost": 114,
            },
        },
    },

    ("RocketAir_Hydra_70mm_x14", "rocket", None, False): { # 608
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 20,
            },
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 14,
                "RadiusSplashSuppressDamagesGRU": 21,
                "TempsEntreDeuxTirs": 0.2,
                "TempsEntreDeuxFx": 0.2,
                "PhysicalDamages": 0.75,
                "SuppressDamages": 75,
                "TempsEntreDeuxSalves": 0.55,
                "NbTirParSalves": 2,
                "SupplyCost": 6,
                "NbSalvosShootOnPosition": 7,
                "AffichageMunitionParSalve": 2,
            },
        },
        "WeaponDescriptor": {
            "Salves": 7,
        },
    },

    ("RocketAir_B8_80mm_x20", "rocket", None, False): { # 594
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TempsEntreDeuxTirs": 0.25,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
                "SupplyCost": 120,
            },
        },
    },

    ("RocketAir_B8_80mm_x10", "rocket", None, False): { # 593
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 15,
                "RadiusSplashSuppressDamagesGRU": 28,
                "TempsEntreDeuxTirs": 0.25,
                "PhysicalDamages": 0.9,
                "SuppressDamages": 90,
                "SupplyCost": 60,
            },
        },
    },
}
# fmt: on
