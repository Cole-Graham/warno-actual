"""Mortier weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Mortier_Vasilek_indirect_82mm_towed", "mortar", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.8,
                "SuppressDamages": 191,
                "RadiusSplashPhysicalDamagesGRU": 82,
                "RadiusSplashSuppressDamagesGRU": 109,
            },
        },
    },
    
    ("Mortier_Vasilek_indirect_82mm_SMOKE_towed", "mortar", "Mortier_Vasilek_indirect_82mm_towed", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_he",
            },
            "parent_membr": {
                "ImpactHappening": ['MortierM30107MmSmoke'],
                "PhysicalDamages": 0.12,
                "SuppressDamages": 7.0,
                "RadiusSplashPhysicalDamagesGRU": 2,
                "RadiusSplashSuppressDamagesGRU": 0,
                "SupplyCost": 5.0,
                "SmokeDescriptor": "$/GFX/Weapon/Descriptor_Smoke_Fumi81mm",
                "FireTriggeringProbability": 0.05,
            },
        },
        "BaseSupplyCost": 5.0,
        "NbWeapons": [1],
    },
    
    ("Mortier_Vasilek_indirect_82mm", "mortar", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.8,
                "SuppressDamages": 191,
                "RadiusSplashPhysicalDamagesGRU": 82,
                "RadiusSplashSuppressDamagesGRU": 109,
            },
        },
    },
    
    ("Mortier_Vasilek_indirect_82mm_SMOKE", "mortar", "Mortier_Vasilek_indirect_82mm", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_he",
            },
            "parent_membr": {
                "ImpactHappening": ['MortierM30107MmSmoke'],
                "PhysicalDamages": 0.12,
                "SuppressDamages": 7.0,
                "RadiusSplashPhysicalDamagesGRU": 2,
                "RadiusSplashSuppressDamagesGRU": 0,
                "SupplyCost": 5.0,
                "SmokeDescriptor": "$/GFX/Weapon/Descriptor_Smoke_Fumi81mm",
                "FireTriggeringProbability": 0.05,
            },
        },
        "BaseSupplyCost": 5.0,
        "NbWeapons": [1],
    },

    ("Mortier_Vasilek_82mm_towed", "mortar", None, False): { # 554
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.8,
                "SuppressDamages": 191,
                "RadiusSplashPhysicalDamagesGRU": 82,
                "RadiusSplashSuppressDamagesGRU": 109,
            },
        },
    },
    
    ("Mortier_Vasilek_82mm_SMOKE_towed", "mortar", "Mortier_Vasilek_82mm_towed", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_he",
            },
            "parent_membr": {
                "ImpactHappening": ['MortierM30107MmSmoke'],
                "PhysicalDamages": 0.12,
                "SuppressDamages": 7.0,
                "RadiusSplashPhysicalDamagesGRU": 2,
                "RadiusSplashSuppressDamagesGRU": 0,
                "SupplyCost": 5.0,
                "SmokeDescriptor": "$/GFX/Weapon/Descriptor_Smoke_Fumi81mm",
                "FireTriggeringProbability": 0.05,
            },
        },
        "BaseSupplyCost": 5.0,
        "NbWeapons": [1],
    },

    ("Mortier_Vasilek_82mm", "mortar", None, False): { # 553
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.8,
                "SuppressDamages": 191,
                "RadiusSplashPhysicalDamagesGRU": 82,
                "RadiusSplashSuppressDamagesGRU": 109,
            },
        },
    },
    
    ("Mortier_Vasilek_82mm_SMOKE", "mortar", "Mortier_Vasilek_82mm", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_he",
            },
            "parent_membr": {
                "ImpactHappening": ['MortierM30107MmSmoke'],
                "PhysicalDamages": 0.12,
                "SuppressDamages": 7.0,
                "RadiusSplashPhysicalDamagesGRU": 2,
                "RadiusSplashSuppressDamagesGRU": 0,
                "SupplyCost": 5.0,
                "SmokeDescriptor": "$/GFX/Weapon/Descriptor_Smoke_Fumi81mm",
                "FireTriggeringProbability": 0.05,
            },
        },
        "BaseSupplyCost": 5.0,
        "NbWeapons": [1],
    },
    
    ("Mortier_RT61_120mm", "mortar", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.6,
                "SuppressDamages": 265,
                "RadiusSplashPhysicalDamagesGRU": 120,
                "RadiusSplashSuppressDamagesGRU": 160,
            },
        },
    },

    ("Mortier_PM43_120mm", "mortar", None, False): { # 543
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.6,
                "SuppressDamages": 265,
                "RadiusSplashPhysicalDamagesGRU": 120,
                "RadiusSplashSuppressDamagesGRU": 160,
            },
        },
    },

    ("Mortier_M30_towed_107mm", "mortar", None, False): { # 537
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.3,
                "SuppressDamages": 239,
                "RadiusSplashPhysicalDamagesGRU": 107,
                "RadiusSplashSuppressDamagesGRU": 143,
            },
        },
    },

    ("Mortier_M30_107mm", "mortar", None, False): { # 534
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.3,
                "SuppressDamages": 239,
                "RadiusSplashPhysicalDamagesGRU": 107,
                "RadiusSplashSuppressDamagesGRU": 143,
            },
        },
    },

    ("Mortier_M29_81mm", "mortar", None, False): { # 532
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.8,
                "SuppressDamages": 189,
                "RadiusSplashPhysicalDamagesGRU": 81,
                "RadiusSplashSuppressDamagesGRU": 108,
            },
        },
    },
    
    ("Mortier_81mm_TOWED", "mortar", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.8,
                "SuppressDamages": 189,
                "RadiusSplashPhysicalDamagesGRU": 81,
                "RadiusSplashSuppressDamagesGRU": 108,
            },
        },
    },
    
    ("Mortier_81mm", "mortar", None, False): { # 532
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.8,
                "SuppressDamages": 189,
                "RadiusSplashPhysicalDamagesGRU": 81,
                "RadiusSplashSuppressDamagesGRU": 108,
            },
        },
    },

    ("Mortier_2S12_120mm", "mortar", None, False): { # 510
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.6,
                "SuppressDamages": 265,
                "RadiusSplashPhysicalDamagesGRU": 120,
                "RadiusSplashSuppressDamagesGRU": 160,
            },
        },
    },

    ("Mortier_Tampella_120mm", "mortar", None, False): { # 510
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.6,
                "SuppressDamages": 265,
                "RadiusSplashPhysicalDamagesGRU": 120,
                "RadiusSplashSuppressDamagesGRU": 160,
            },
        },
    },

    ("Mortier_Tampella_towed_120mm", "mortar", None, False): { # 510
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.6,
                "SuppressDamages": 265,
                "RadiusSplashPhysicalDamagesGRU": 120,
                "RadiusSplashSuppressDamagesGRU": 160,
            },
        },
    },

    ("Mortier_2B14_82mm_TOWED", "mortar", None, False): { # 509
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.8,
                "SuppressDamages": 191,
                "RadiusSplashPhysicalDamagesGRU": 82,
                "RadiusSplashSuppressDamagesGRU": 109,
            },
        },
    },
    
    ("Howz_Canon_2A60_Howitzer_120mm_SMOKE", "mortar", None, False): { # 371
        "Ammunition": {
            "parent_membr": {
                "TempsDeVisee": 12,
                "TimeBetweenTwoSalvos": 20.0,
            },
        },
    },

    ("Howz_Canon_2A60_Howitzer_120mm", "mortar", None, False): { # 370
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.6,
                "SuppressDamages": 265,
                "TempsDeVisee": 12,
                "TimeBetweenTwoSalvos": 20.0,
                "RadiusSplashPhysicalDamagesGRU": 120,
                "RadiusSplashSuppressDamagesGRU": 160,
                "SupplyCost": 90,
            },
        },
    },

    ("Howz_Canon_2A51_Howitzer_120mm_SMOKE", "mortar", None, False): { # 369
        "Ammunition": {
            "parent_membr": {
                "TempsDeVisee": 12,
                "TimeBetweenTwoSalvos": 20.0,
            },
        },
    },

    ("Howz_Canon_2A51_Howitzer_120mm", "mortar", None, False): { # 368
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.6,
                "SuppressDamages": 265,
                "RadiusSplashPhysicalDamagesGRU": 120,
                "RadiusSplashSuppressDamagesGRU": 160,
                "TempsDeVisee": 12,
                "TimeBetweenTwoSalvos": 20.0,
                "SupplyCost": 90,
            },
        },
    },
}
# fmt: on
