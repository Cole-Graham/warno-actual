"""Canon weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {

    # WARSAW PACT
    
    ("Canon_AP_125_mm_2A46M", "canon", None, False): { # T-72AV/B/B1/B1'84/S 2A46M (3BM-32)
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
            "display": "2A46M (3BM-32)",
            "token": "OWKJYQDRIB",
        },
    },

    ("Canon_HE_125_mm_2A46M", "canon", None, False): { # T-72S (HE)
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
    
    ("Canon_AP_125_mm_2A46_T72M2", "canon", None, False): { # T-72M2 WILK 2A46-1 (3BM-26) (Could be swapped to 3BM-32?)
        "Ammunition": {
            #"Arme": {
            #    "Index": 31,
            #},
            "display": "2A46-1 (3BM-26)",
            "token": "OTYHZNLLMR",
        },
    },

    ("Canon_AP_125_mm_2A46_T72M", "canon", None, False): { # T-72M/M1/A'79/A'81/M-2/M-3 2A46-1 (3BM-26)
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
            "display": "2A46-1 (3BM-26)",
            "token": "ISVNZCPVXC",
        },
    },

    ("Canon_HE_125_mm_2A46_T72M", "canon", None, False): { # T-72M/M1/A'79/A'81/M-2/M-3 (HE)
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

    ("Canon_AP_125_mm_2A46", "canon", None, False): { # T-72/'73/'77 2A46 (3BM-22)
        "Ammunition": {
            "display": "2A46 (3BM-22)",
            "token": "KXRZMEFESV",
        },
    },

    ("Canon_AP_100mm_D10T_late", "canon", None, False): { # T-55AM2 D-10T2S (3BM-25)
        "Ammunition": {
            "display": "D-10T2S (3BM-25)",
            "token": "KADMWTFNND",
        },
    },

    ("Canon_AP_100mm_D10T_late", "canon", None, False): { # T-55AM2 D-10T2S (HE)
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.15,
            },
        },
    },

    ("Canon_AP_100mm_D10T_Merida", "canon", None, False): { # T-55AM Merdia D-10T2S (3BM-25)
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "display": "D-10T2S (3BM-25)",
            "token": "HLIZNSNRIV",
        },
    },

    ("Canon_HE_100mm_D10T_Merida", "canon", None, False): { # T-55AM Merdia (HE)
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

    ("Canon_AP_100mm_D10T_late", "canon", None, False): { # T-55A, TO-55 D-10T2S (3BM-25)
        "Ammunition": {
            "display": "D-10T2S (3BM-25)",
            "token": "MBKOYQGXJF",
        },
    },

    ("Canon_AP_100mm_D10T_early_HEAT", "canon", None, False): { # T-54B/AM D-10T2S (3BK-17M)
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "display": "D-10T2S (3BK-17M)",
            "token": "EUSQRXVKEB",
        },
    },

    ("Canon_HE_100mm_D10T_early", "canon", None, False): { # T-54B/AM, T-55A, TO-55 (HE)
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.15,
            },
        },
    },

    ("Canon_HEAT_85mm_S53", "canon", "Canon_AP_85mm_S53", True): { # T-34 S-53 (3BK-2)
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
            "display": "S-53 (3BK-2)",
            "token": "QGKCOHDYWC",
        },
    },
    
    ("Canon_HEAT2_85mm_S53", "canon", "Canon_AP_85mm_S53", True): { # T-34 S-53 (3BK-2M)
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
            "display": "S-53 (3BK-2M)",
            "token": "AABTCOGEZB",
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

    ("Canon_AP_76mm_D56T", "canon", None, False): { # PT-76B 2A16M (BK-354M)
        "Ammunition": {
            "Arme": {
                "Index": 15, # HEAT
            },
            "parent_membr": {
                "MaximumRangeGRU": 1575,
            },
            "display": "2A16M (BK-354M)",
            "token": "SHXVLQPRJF",
        },
    },

    ("Canon_HE_76mm_D56T", "canon", None, False): { # PT-76B 2A16M (HE)
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 1575,
                "RadiusSplashPhysicalDamagesGRU": 31,
                "RadiusSplashSuppressDamagesGRU": 55,
                "SupplyCost": 8.0,
            },
        },
    },

    ("Canon_AP_73_mm_2A28_Grom", "canon", None, False): { # BMP-1 2A28 (PG-15V)
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
            "display": "2A28 (PG-15V)",
            "token": "UNMNABAZNO",
        },
    },

    ("Canon_HE_73_mm_2A28_Grom", "canon", None, False): { # BMP-1 2A28 (HE)
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

    ("Canon_HEAT_73_mm_SPG9_TOWED", "recoilless", None, False): { # SPG-9 (PG9V) (Towed)
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
            "display": "SPG-9 (PG9V)",
            "token": "ACXVIKNDIJ",
        },
    },

    ("Canon_HE_73_mm_SPG9_TOWED", "recoilless", None, False): { # SPG-9 (HE) (Towed)
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

    ("Canon_HEAT_73_mm_SPG9D_TOWED", "recoilless", "Canon_HEAT_73_mm_SPG9_TOWED", True): {  # SPG-9D (PG9V) (Towed-Para)
        "Ammunition": {
            "display": "SPG-9D (PG9V)",
            "token": "SPGDPARA",
            "parent_membr": {
                "DisplaySalveAccuracy": False,
                "SupplyCost": 8.0,
            },
        },
    },

    ("Canon_HEAT_73_mm_SPG9", "recoilless", None, False): { # SPG-9 (PG9V) (Jeep/APC)
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
            "display": "SPG-9 (PG9V)",
            "token": "HJRNUEJZUU",
        },
    },

    ("Canon_HE_73_mm_SPG9", "recoilless", None, False): { # SPG-9 (Jeep/APC, HE)
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

    # USSR Only

    ("Canon_AP_125_mm_2A46M_late_T80UD", "canon", None, False): { # T-80UD 2A46M1 (3BM-42)
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
            "display": "2A46M1 (3BM-42)",
            "token": "UADUNLIGZF",
        },
    },

    ("Canon_HE_125_mm_2A46M_late_T80UD", "canon", None, False): { # T-80UD 2A46M1 (HE)
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

    ("Canon_AP_125_mm_2A46M_late", "canon", None, False): { # T-80U/U'89 2A46M1 (3BM-42)
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
            "display": "2A46M1 (3BM-42)",
            "token": "UHRORCESCA",
        },
    },

    ("Canon_HE_125_mm_2A46M_late", "canon", None, False): { # T-80U/U'89 2A46M1 (HE)
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

    ("Canon_AP_125_mm_2A46M_T80B", "canon", None, False): { # T-80B/BV/IZD.29 2A46 (3BM-32) (This should also include the T-64BV, but whatever)
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
            "display": "2A46M-1 (3BM-32)",
            "token": "KMMMXRQUBL",
        },
    },

    ("Canon_HE_125_mm_2A46M_T80B", "canon", None, False): { # T-80B/BV/IZD.29 2A46 (HE)
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

    ("Canon_AP_125_mm_2A46_T64B_very_late", "canon", None, False): { # T-64B/BV/B1/B1V 2A46-2 (3BM-32)
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
            "display": "2A46-2 (3BM-32)",
            "token": "HPRHLTLVHG",
        },
    },

    ("Canon_HE_125_mm_2A46_T64B_very_late", "canon", None, False): { # T-64B/BV/B1/B1V 2A46-2 (HE)
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

    ("Canon_AP_125_mm_2A46_T64A_late", "canon", None, False): { # T-64AV 2A46 (3BM-26)
        "Ammunition": {
            "Arme": {
                "Index": 30, # KE
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
                "MaximumRangeGRU": 1925,  
            },
            "display": "2A46 (3BM-26)",
            "token": "SURTPIJIWC",
        },
    },

    ("Canon_HE_125_mm_2A46_T64A_late", "canon", None, False): { # T-64AV (HE)
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
                "MaximumRangeGRU": 1925,
            },
        },
    },

    ("Canon_AP_125_mm_2A46_T64A", "canon", None, False): { # T-64A'83/M 2A46 (3BM-26)
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
            "display": "2A46 (3BM-26)",
            "token": "LIWPMVFLCO",
        },
    },

    ("Canon_HE_125_mm_2A46_T64A", "canon", None, False): { # T-64A 1983, T-64AM (HE)
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
        },
    },

    ("Canon_AP_115mm_2A21", "canon", None, False): { # T-64R 2A21 (3BK-15M)
        "Ammunition": {
            "Arme": {
                "Index": 18,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
            },
            "display": "2A21 (3BK-15M)",
            "token": "ESGELIGQDC",
        },
    },

    ("Canon_HE_115mm_2A21", "canon", None, False): { # T-64R (HE)
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 6.6,
                "TimeBetweenTwoSalvos": 6.6,
                "PhysicalDamages": 1.4,
            },
        },
    },

    ("Canon_AP_115mm_U5TS_T62M", "canon", None, False): { # T-62M/MD/M1/M1D/MV 2A20 (3BM-21)
        "Ammunition": {
            "display": "2A20 (3BM-21)",
            "token": "BKPFFQQSMZ",
        },
    },

    ("Canon_HE_115mm_U5TS_T62M", "canon", None, False): { # T-62M/MD/M1/M1D/MV (HE)
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 1.4,
            },
        },
    },

    ("Canon_HE_100mm_2A70", "canon", None, False): { # BMP-3 2A70 (3UOF19?)
        "Ammunition": {
            "parent_membr": {
                "RadiusSplashPhysicalDamagesGRU": 43,
                "PhysicalDamages": 1.15,
                "RadiusSplashSuppressDamagesGRU": 86,
                "SupplyCost": 100.0,
            },
            "display": "2A70 (3UOF19)",
            "token": "WOJVALWXLE",
        },
    },

    # WARSAW PACT AT GUNS

    ("Canon_AP_100mm_2A29R_Ruta", "canon", None, False): { # MT-12R Ruta 2A29 (3BM-34)
        "Ammunition": {
            "display": "2A29 (3BM-34)",
            "token": "YJMRACXBEZ",
            "parent_membr": {
                "PhysicalDamages": 1.15,
            },
        },
    },

    ("Canon_AP_100mm_2A29_Rapira", "canon", None, False): { # MT-12 2A29 (3BM-24)
        "Ammunition": {
            "display": "2A29 (3BM-24)",
            "token": "VLXFNDJKVP",
            "parent_membr": {
                "PhysicalDamages": 1.15,
            },
        },
    },

    ("Canon_AP_125mm_2A45_Sprut", "canon", None, False): { # Sprut-B 2A45 (3BM-42)
        "Ammunition": {
            "display": "2A45 (3BM-42)",
            "token": "YWGRIPIKZD",
        },
    },

    ("Canon_AP_KSM25_100mm", "canon", None, False): { # KSM-65 (BR-412D) (This is a guess, and an experiment. The vanilla version has a wild amount of pen for the APBC that this gun actually had as far as I know, but could fire much faster)
        "Ammunition": {
            "Arme": {
                "Index": 22,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoSalvos": 3.0,
            },
            "display": "KSM-65 (BR-412D)",
            "token": "RQFPASQQYH",
        },
    },

    ("Canon_HE__KSM25_100mm", "canon", None, False): { # KSM-65 (BR-412D) (This is a guess, and an experiment. The vanilla version has a wild amount of pen for the APBC that this gun actually had as far as I know, but could fire much faster)
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 3.0,
                "TimeBetweenTwoSalvos": 3.0,
                "PhysicalDamages": 1.15,
            },
        },
    },

    ("Canon_AP_85mm_D48", "canon", None, False): { # D-48 2A15 (BR-372)
        "Ammunition": {
            "display": "2A15 (BR-372)",
            "token": "DDZMIZIWBL",
        },
    },

    ("Canon_AP_85mm_D44", "canon", None, False): { # D-44 (BR-365P)
        "Ammunition": {
            "display": "D-44 (BR-365P)",
            "token": "RBGZQGTFLS",
        },
    },

    ("Canon_AP_85mm_K52", "canon", None, False): { # K-52 (BR-365P)
        "Ammunition": {
            "display": "K-52 (BR-365P)",
            "token": "BFUPVRLXDT",
        },
    },

    ("Canon_AP_57mm_ZiS2", "canon", None, False): { # Zis-2 (BR-271N)
        "Ammunition": {
            "display": "K-52 (BR-271N)",
            "token": "TGQYOOGISZ",
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

    ("Canon_AP_120_mm_L11A5_Mk1_4", "canon", None, False): { # Cheiftian Mk1/4 L11A1 (L31A7) 
        "Ammunition": {
            "Arme": {
                "Index": 17, # HEAT
            },
            "parent_membr": {
                "SuppressDamages": 243,
            },
            "display": "L11A1 (L31A7) [HESH]",
            "token": "ESZSAANXXP",
        },
    },

    ("Canon_AP_105mm_L7_Centurion", "canon", None, False): { # Centurion Mk13 L7A3 (L64A4)
        "Ammunition": {
            "display": "L7A3 (L64A4)",
            "token": "HVFSAXIYDV",
        },
    },

    ("Canon_HEAT_105mm_L7_Centurion_AVRE", "canon", None, False): { # Centurion Mk12 AVRE 105mm, Currently modeled with a HEAT round that wasn't actually issued
        "Ammunition": {
            "Arme": {
                "Index": 15, # HEAT
            },
            "parent_membr": {
                "SuppressDamages": 213,
            },
            "display": "L7A3 (L35) [HESH]",
            "token": "XOIJZEAMFO",
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
