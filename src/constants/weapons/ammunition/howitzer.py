"""Howitzer weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Howz_Canon_M201A1_Howitzer_203mm_late", "howitzer", None, False): { # 433
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 15.0,
                "TimeBetweenTwoFx": 16.0,
                "PhysicalDamages": 6,
                "SuppressDamages": 450,
                "RadiusSplashPhysicalDamagesGRU": 203,
                "RadiusSplashSuppressDamagesGRU": 271,
                "TimeBetweenTwoSalvos": 50.0,
                "NbTirParSalves": 2,
                "SupplyCost": 80.0,
                "AffichageMunitionParSalve": 2,
            },
        },
    },
    
    ("Howz_Canon_M201A1_Howitzer_203mm_late_SMOKE", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 15.0,
                "TimeBetweenTwoFx": 16.0,
                "TimeBetweenTwoSalvos": 50.0,
                "NbTirParSalves": 2,
                "AffichageMunitionParSalve": 2,
            },
        },
    },
    
    ("Howz_Canon_2A44_Howitzer_203mm_late", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 10.0,
                "TimeBetweenTwoFx": 11.0,
                "PhysicalDamages": 6,
                "SuppressDamages": 450,
                "RadiusSplashPhysicalDamagesGRU": 203,
                "RadiusSplashSuppressDamagesGRU": 271,
                "TimeBetweenTwoSalvos": 50.0,
            },
        },
    },
    
    ("Howz_Canon_2A44_Howitzer_203mm_late_SMOKE", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 10.0,
                "TimeBetweenTwoFx": 11.0,
                "TimeBetweenTwoSalvos": 50.0,
            },
        },
    },
    
    ("Howz_Canon_GCT_Howitzer_155mm", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 357,
                "RadiusSplashPhysicalDamagesGRU": 155,
                "RadiusSplashSuppressDamagesGRU": 207,
            },
        },
    },

    ("Howz_Canon_M185_L39_Howitzer_155mm", "howitzer", None, False): { # 427
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 357,
                "RadiusSplashPhysicalDamagesGRU": 155,
                "RadiusSplashSuppressDamagesGRU": 207,
            },
        },
    },

    ("Howz_Canon_FH70_SP_Howitzer_155mm", "howitzer", None, False): { # 427
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 357,
                "RadiusSplashPhysicalDamagesGRU": 155,
                "RadiusSplashSuppressDamagesGRU": 207,
            },
        },
    },
    
    ("Howz_Canon_M118_Howitzer_105mm", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 5.0,
                "PhysicalDamages": 3.0,
                "SuppressDamages": 187,
                "RadiusSplashPhysicalDamagesGRU": 105,
                "RadiusSplashSuppressDamagesGRU": 140,
                "NbTirParSalves": 5,
                "SupplyCost": 100.0,
                "AffichageMunitionParSalve": 5,
            },
        },
    },
    
    ("Howz_Canon_M118_Howitzer_105mm_SMOKE", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 5.0,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 5,
            },
        },
    },
    
    ("Howz_Canon_M113A1_Howitzer_175mm_late", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 5.4,
                "SuppressDamages": 405,
                "RadiusSplashPhysicalDamagesGRU": 175,
                "RadiusSplashSuppressDamagesGRU": 233,
            },
        },
    },

    ("Howz_Canon_M102_Howitzer_105mm", "howitzer", None, False): { # 409
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 5.0,
                "PhysicalDamages": 3.0,
                "SuppressDamages": 187,
                "RadiusSplashPhysicalDamagesGRU": 105,
                "RadiusSplashSuppressDamagesGRU": 140,
                "NbTirParSalves": 5,
                "SupplyCost": 100.0,
                "AffichageMunitionParSalve": 5,
            },
        },
    },
    
    ("Howz_Canon_M102_Howitzer_105mm_SMOKE", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 5.0,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 5,
            },
        },
    },
    
    ("Howz_Canon_FH70_Howitzer_155mm", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 357,
                "RadiusSplashPhysicalDamagesGRU": 155,
                "RadiusSplashSuppressDamagesGRU": 207,
            },
        },
    },
    
    ("Howz_Canon_DANA_SP_152mm", "howitzer", None, False): { # 389
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
            },
        },
    },
    
    ("Howz_Canon_M30_Howitzer_122mm", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.3,
                "SuppressDamages": 281,
                "RadiusSplashPhysicalDamagesGRU": 122,
                "RadiusSplashSuppressDamagesGRU": 163,
            },
        },
    },

    ("Howz_Canon_D30_Howitzer_122mm", "howitzer", None, False): { # 393
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.3,
                "SuppressDamages": 281,
                "RadiusSplashPhysicalDamagesGRU": 122,
                "RadiusSplashSuppressDamagesGRU": 163,
            },
        },
    },
    
    ("Howz_Canon_M46_Howitzer_130mm", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.6,
                "SuppressDamages": 300,
                "RadiusSplashPhysicalDamagesGRU": 130,
                "RadiusSplashSuppressDamagesGRU": 174,
            },
        },
    },

    ("Howz_Canon_D22_Howitzer_152mm_late_guided", "howitzer", None, False): { # 391
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
            },
        },
    },

    ("Howz_Canon_D22_Howitzer_152mm_late", "howitzer", None, False): { # 389
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
            },
        },
    },
    
    ("Howz_Canon_D20_Howitzer_152mm", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
            },
        },
    },
    
    ("Howz_Canon_D20_towed_152mm", "howitzer", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
            },
        },
    },
    
    ("Howz_Canon_2A65_towed_152mm", "howitzer", None, False): { # 376
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
            },
        },
    },
    
    ("Howz_Canon_2A36_towed_152mm", "howitzer", None, False): { # 362
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
            },
        },
    },

    ("Howz_Canon_2A18_Howitzer_122mm", "howitzer", None, False): { # 357
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 3.3,
                "SuppressDamages": 281,
                "RadiusSplashPhysicalDamagesGRU": 122,
                "RadiusSplashSuppressDamagesGRU": 163,
            },
        },
    },
}
# fmt: on
