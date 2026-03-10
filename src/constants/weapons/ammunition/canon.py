"""Canon weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Canon_HEAT_73_mm_SPG9_TOWED", "recoilless", None, False): { # 241
        "Ammunition": {
            "Arme": {
                "Index": 15,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "DisplaySalveAccuracy": False,
                "SupplyCost": 8.0,
            },
        },
    },

    ("Canon_HEAT_73_mm_SPG9", "recoilless", None, False): { # 240
        "Ammunition": {
            "Arme": {
                "Index": 15,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "DisplaySalveAccuracy": False,
                "SupplyCost": 8.0,
            },
        },
    },

    ("Canon_HEAT_73_mm_SPG9D_TOWED", "recoilless", "Canon_HEAT_73_mm_SPG9_TOWED", True): {  # 707
        "Ammunition": {
            "display": "SPG-9D",
            "token": "SPG9D_PARA",
            "parent_membr": {
                "DisplaySalveAccuracy": False,
                "SupplyCost": 8.0,
            },
        },
    },
    
    ("Canon_HEAT_85mm_S53", "canon", "Canon_AP_85mm_S53", True): { # T-34 3BK-2
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_ap_missile",
                "Index": 13,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "Caliber": ("85mm HEAT", "IWLOKTOKDR"),
                "TraitsToken": ['HE', 'HEAT'],
                "MaximumRangeGRU": 1750,
                "DamageTypeEvolutionOverRangeDescriptor": "nil"
            },
        },
    },
    
    ("Canon_HEAT2_85mm_S53", "canon", "Canon_AP_85mm_S53", True): { # T-34 3BK-2M
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_ap_missile",
                "Index": 15,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "Caliber": ("85mm HEAT", "IWLOKTOKDR"),
                "TraitsToken": ['HE', 'HEAT'],
                "MaximumRangeGRU": 1750,
                "DamageTypeEvolutionOverRangeDescriptor": "nil"
            },
        },
    },
    
    ("Canon_AP_100mm_D10T_early_HEAT", "canon", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 16,
            },
        },
    },

    ("Canon_AP_115mm_2A21", "canon", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 18,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_AP_100mm_D10T_early_HEAT", "canon", None, False): { # 239
        "Ammunition": {
            "Arme": {
                "Index": 16,
            },
        },
    },
    
    ("Canon_HE_73_mm_SPG9_TOWED", "recoilless", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PhysicalDamages": 0.85,
                "SuppressDamages": 115,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 8.0,
            },
        },
    },

    ("Canon_HE_73_mm_SPG9", "recoilless", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PhysicalDamages": 0.85,
                "SuppressDamages": 115,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 8.0,
            },
        },
    },

    ("Canon_HE_73_mm_2A28_Grom", "canon", None, False): { # 219
        "Ammunition": {
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "RadiusSplashPhysicalDamagesGRU": 33,
                "PhysicalDamages": 0.85,
                "RadiusSplashSuppressDamagesGRU": 66,
                "SuppressDamages": 115,
                # Eugen removed this and replaced it with SpeedGRU
                # "FlightTimeForSpeed": 3.3,
                "SupplyCost": 300.0,
            },
        },
    },
    
    ("Canon_HE_76mm_D56T", "canon", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "RadiusSplashPhysicalDamagesGRU": 31,
                "RadiusSplashSuppressDamagesGRU": 55,
                "SupplyCost": 8.0,
            },
        },
    },
    
    ("Canon_HE_85mm_S53", "canon", None, False): { # T-34 3BK-2
        "Ammunition": {
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "Caliber": ("85mm HEAT", "IWLOKTOKDR"),
                "TraitsToken": ['HE'],
                "MaximumRangeGRU": 1750,
                "RadiusSplashPhysicalDamagesGRU": 38,
                "RadiusSplashSuppressDamagesGRU": 55,
            },
        },
    },
    
    ("Canon_HE_115mm_U5TS_T62M", "canon", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.4,
            },
        },
    },

    ("Canon_HE_115mm_2A21", "canon", None, False): { # 211
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
                "PhysicalDamages": 1.4,
            },
        },
    },

    ("Canon_HE_125_mm_2A46M_late_T80UD", "canon", None, False): { # 211
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_HE_125_mm_2A46M_late", "canon", None, False): { # 210
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_HE_125_mm_2A46M_T80B", "canon", None, False): { # 209
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },
    
    ("Canon_HE_125_mm_2A46M", "canon", None, False): { # T-72S
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
            },
        },
    },

    ("Canon_HE_125_mm_2A46_T72M", "canon", None, False): { # 206
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
            },
        },
    },

    ("Canon_HE_125_mm_2A46_T64B_very_late", "canon", None, False): { # 205
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_HE_125_mm_2A46_T64A_late", "canon", None, False): { # T-64AV
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
                "MaximumRangeGRU": 1925,
            },
        },
    },


    ("Canon_HE_125_mm_2A46_T64A", "canon", None, False): { # 204
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_HE_100mm_D10T_early", "canon", None, False): { # 171
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.15,
            },
        },
    },
    
    ("Canon_HE_100mm_D10T_Merida", "canon", None, False): { # 171
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "PhysicalDamages": 1.15,
            },
        },
    },

    ("Canon_HE_100mm_2A70", "canon", None, False): { # 169
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 43,
                "PhysicalDamages": 1.15,
                "RadiusSplashSuppressDamagesGRU": 86,
                "SupplyCost": 100.0,
            },
        },
    },
    
    ("Canon_AP_100mm_D10T_Merida", "canon", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
        },
    },
    
    ("Canon_AP_76mm_D56T", "canon", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 15, # HEAT
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
            },
        },
    },
    
    ("Canon_AP_73_mm_2A28_Grom", "canon", None, False): { # 148
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "SupplyCost": 300.0,
            },
        },
    },
    
    ("Canon_AP_125_mm_2A46M", "canon", None, False): { # T-72S
        "Ammunition": {
            "Arme": {
                "Index": 31,
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
            },
        },
    },
    
    # ("Canon_AP_125_mm_2A46_T72M2", "canon", None, False): { # T-72M2 WILK
    #     "Ammunition": {
    #         "Arme": {
    #             "Index": 31,
    #         },
    #     },
    # },

    ("Canon_AP_125_mm_2A46_T72M", "canon", None, False): { # T72M
        "Ammunition": {
            # "Arme": {
            #     "Index": 29,
            # },
            "hit_roll": {
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 2275,
            },
        },
    },

    ("Canon_AP_125_mm_2A46M_late_T80UD", "canon", None, False): { # T-80UD
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_AP_125_mm_2A46M_late", "canon", None, False): { # T-80U/89
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_AP_125_mm_2A46M_T80B", "canon", None, False): { # T-80B/BV/IZD. 29
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_AP_125_mm_2A46_T64B_very_late", "canon", None, False): { # T-64B/BV/B1/B1V
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_AP_125_mm_2A46_T64A_late", "canon", None, False): { # T-64AV 
        "Ammunition": {
            "Arme": {
                "Index": 30, # KE
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
                "MaximumRangeGRU": 1925,  
            },
        },
    },

    ("Canon_AP_125_mm_2A46_T64A", "canon", None, False): { # T-64A 1983, T-64AM
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },
    
    # UNITED KINGDOM

    ("Canon_AP_120_mm_L11A5_Challenger_DU", "canon", None, False): { # Challanger Mk3 L11A5 (L26A1)
        "Ammunition": {
            "display": "L11A5 (L26A1)",
            "token": "SVUWSIWOMZ",
        },
    },

    ("Canon_AP_120_mm_L11A5_Challenger", "canon", None, False): { # Challanger Mk2 L11A5 (L23A1)
        "Ammunition": {
            "display": "L11A5 (L23A1)",
            "token": "AQXRAAHWKX",
        },
    },

    ("Canon_AP_120_mm_L11A5_Mk10", "canon", None, False): { # Cheiftian Mk10/11 L11A5 (L23A1)
        "Ammunition": {
            "display": "L11A5 (L23A1)",
            "token": "XOHWOBENKZ",
        },
    },

    ("Canon_AP_120_mm_L11A5_Mk9", "canon", None, False): { # Cheiftian Mk9 L11A5 (L23A1)
        "Ammunition": {
            "display": "L11A5 (L23A1)",
            "token": "LSJITDGNSW",
        },
    },

    ("Canon_AP_120_mm_L11A5_Mk6", "canon", None, False): { # Cheiftian Mk6/2 L11A5 (L15A5)
        "Ammunition": {
            "display": "L11A5 (L15A5)",
            "token": "TJBDCIUPVY",
        },
    },

    # ("Canon_AP_120_mm_L11A5_Mk1_4", "canon", None, False): { # Cheiftian Mk1/4 L11A1 (L15A3) 
    #     "Ammunition": {
    #         "display": "L11A1 (L15A3)",
    #         "token": "ESZSAANXXP",
    #     },
    # },

    ("Canon_AP_105mm_L7_Centurion", "canon", None, False): { # Centurion Mk13 L7A3 (L64A4)
        "Ammunition": {
            "display": "L7A3 (L64A4)",
            "token": "HVFSAXIYDV",
        },
    },

    ("Canon_HEAT_105mm_L7_Centurion_AVRE", "canon", None, False): { # Centurion Mk12 AVRE 105mm, Currently modeled with a HEAT round that wasn't actually issued
        "Ammunition": {
            "Arme": {
                "Index": 17, # HEAT
            },
            #"display": "L7A3 (L35)",
            #"token": "XOIJZEAMFO",
        },
    },
    
    ("Canon_AP_76mm_L23A1", "canon", None, False): { # Scorpion L23A1 (L29) HESH
        "Ammunition": {
            "Arme": {
                "Index": 13,
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 0,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'HE', 'HEAT'],
                "CanShootWhileMoving": False,
            },
            "display": "L23A1 (L29)",
            "token": "JIMVFYAGOH",
        },
    },

    ("Canon_HE_76mm_L23A1", "canon", None, False): { # Scorpion L23A1 (HE)
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 0,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'HE'],
                "CanShootWhileMoving": False,
            },
        },
    },

    ("Canon_AP_76mm_L5A1", "canon", None, False): { # Saladin L5A1 (L29) HESH
        "Ammunition": {
            "Arme": {
                "Index": 13,
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 0,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'HE', 'HEAT'],
                "CanShootWhileMoving": False,
            },
            "display": "L5A1 (L29)",
            "token": "JIMVFYAGOH",
        },
    },

    ("Canon_HE_76mm_L5A1", "canon", None, False): { # Saladin L5A1 (HE)
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 0,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'HE'],
                "CanShootWhileMoving": False,
            },
        },
    },

    ("Canon_HE_165mm_AVRE_L9A1", "canon", None, False): { # Centurion Mk5 AVRE 165mm L9A1 (L33A1) HESH
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "PhysicalDamages": 4.0,
            },
            "display": "L9A1 (L33A1)",
            "token": "UMAXJWHIJY",
        },
    },

    # UNITED STATES OF AMERICA

    ("Canon_AP_120_mm_L52_M68_HA", "canon", None, False): { # M1A1(HA) Abrams M256 (M829A1)
        "Ammunition": {
            "display": "M256 (M829A1)",
            "token": "ZHOKJRHTGG",
        },
    },

    ("Canon_AP_120_mm_L52_M68", "canon", None, False): { # M1A1 Abrams M256 (M829)
        "Ammunition": {
            "display": "M256 (M829)",
            "token": "LONFWANPHJ",
        },
    },

    ("Canon_AP_105mm_M68_M1_MOD", "canon", None, False): { # M1 Abrams MOD M68A1 (XM900E1)
        "Ammunition": {
            "display": "M68A1 (XM900E1)",
            "token": "ZBSIXJNGSM",
        },
    },

    ("Canon_AP_105mm_M68_M1", "canon", None, False): { # M1 Abrams/M1IP Abrams M68A1 (M833)
        "Ammunition": {
            "display": "M68A1 (M833)",
            "token": "FLWXGHUNDQ",
        },
    },

    ("Canon_AP_105mm_M68_late", "canon", None, False): { # M60A3 (TTS) M68A1 (M774)
        "Ammunition": {
            "display": "M68A1 (M774)",
            "token": "ECMORFUAWR",
        },
    },

    ("Canon_AP_105mm_M68_M48A5", "canon", None, False): { # M48A5 M68 (M883)
        "Ammunition": {
            "display": "M68 (M883)",
            "token": "RRHZCAUUMM",
        },
    },

    ("Canon_AP_105mm_M68", "canon", None, False): { # M60A1 M68A1 (M774)
        "Ammunition": {
            "display": "M68A1 (M774)",
            "token": "MWZRKGFQKN",
        },
    },

    ("Canon_HEAT_152mm_Sheridan", "canon", None, False): { # M551 Sheridan M81E1 (M409)
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
            },
            "display": "M81E1 (M409)",
            "token": "WHTWLAHRHH",
        },
    },

    ("Canon_HE_152mm_Sheridan", "canon", None, False): { # M551 Sheridan (HE)
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "PhysicalDamages": 1.75,
            },
        },
    },

    ("Canon_HE_165mm_AVRE", "canon", None, False): { # M728 CEV M135 (M123) HESH
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "PhysicalDamages": 4.0,
            },
            "display": "M135 (M123)",
            "token": "SIYPXALDAK",
        },
    },

    # WEST GERMANY

    ("Canon_AP_120mm_L44_late_2A4", "canon", None, False): { # Leopard 2A4(C) L44 (DM33)
        "Ammunition": {
            "display": "L44 (DM33)",
            "token": "UGOZPAHBEW",
        },
    },

    ("Canon_AP_120mm_L44_late", "canon", None, False): { # Leopard 2A3 L44 (DM23)
        "Ammunition": {
            "display": "L44 (DM23)",
            "token": "XEBVLAROMY",
        },
    },

    ("Canon_AP_120_mm_L44_late87", "canon", None, False): { # Leopard 2A1 L44 (DM13)
        "Ammunition": {
            "display": "L44 (DM13)",
            "token": "LFFDMTHT",
            "Arme": {
                "Index": 29, # KE
            },
        },
    },

    ("Canon_AP_105mm_L7A3_Leo1A5", "canon", None, False): { # Leopard 1A5 L7A3 (DM33)
        "Ammunition": {
            "display": "L7A3 (DM33)",
            "token": "PGWOXXQUEX",
        },
    },

    ("Canon_AP_105mm_L7A3_Leo1A4", "canon", None, False): { # Leopard 1A4 L7A3 (DM23)
        "Ammunition": {
            "display": "L7A3 (DM23)",
            "token": "CIZCZKQPLD",
        },
    },

    ("Canon_AP_105mm_L7A3_Leo1A1A2", "canon", None, False): { # Leopard 1A1A2 L7A3 (DM33)
        "Ammunition": {
            "display": "L7A3 (DM33)",
            "token": "VNIEZEXJWM",
        },
    },

    ("Canon_AP_105mm_L7A3", "canon", None, False): { # Leopard 1A1A1 L7A3 (DM23)
        "Ammunition": {
            "display": "L7A3 (DM23)",
            "token": "EKYWPOSPXA",
        },
    },

    ("Canon_AP_105mm_L7A3_M48", "canon", None, False): { # M48A2GA2 L7A3 (DM23)
        "Ammunition": {
            "display": "L7A3 (DM23)",
            "token": "VGISRCHYTN",
        },
    },

    ("Canon_AP_90mm_M48", "canon", None, False): { # M48A2CGA1 M41 (M332) APCR
        "Ammunition": {
            "display": "M41 (M332)",
            "token": "QVTVRPBMCP",
        },
    },

    ("Canon_HE_90mm_M48", "canon", None, False): { # M48A2CGA1 M41 (HE)
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.0,
            },
        },
    },
    
    ("Canon_AP_90mm_KanJPz", "canon", None, False): { # Kanon Jagdpanzer (M332) APCR
        "Ammunition": {
            "display": "BK90/L40 (M332)",
            "token": "LRLCUBCDLE",
        },
    },

    ("Canon_HE_90mm_M48_KanJPz", "canon", None, False): { # Kanon Jagdpanzer (HE)
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.0,
            },
        },
    },
    
    # FRANCE

    ("Canon_HE_142mm_AVRE", "canon", None, False): { # French Demo Gun HESH
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 875,
                "PhysicalDamages": 3,
                "AimingTime": 2.0,
            },
        },
    },
}
# fmt: on
