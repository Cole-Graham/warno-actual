"""AutoCanon weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("AutoCanon_HE_30mm_M230", "autocannon", None, False): { # 28
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 40,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.1,
                "TempsEntreDeuxFx": 0.1,
                "PhysicalDamages": 0.3,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.0,
                "TempsEntreDeuxSalves": 1.5,
                "NbTirParSalves": 20,
                "SupplyCost": 10,
                "AffichageMunitionParSalve": 20,
            },
        },
        "WeaponDescriptor": {
            "Salves": 40,
        },
    },

    ("AutoCanon_HE_30mm_L21A1_RARDEN", "autocannon", None, False): { # 27
        "Ammunition": {
            "hit_roll": {
                "Idling": 65,
                "Moving": 0,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'HE', 'KINETIC'],
                "TempsEntreDeuxTirs": 0.7,
                "TempsEntreDeuxFx": 0.7,
                "PhysicalDamages": 0.40,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.8,
                "NbTirParSalves": 6,
                "CanShootWhileMoving": False,
                "AffichageMunitionParSalve": 6,
            },
        },
        "BaseSupplyCost": 2,
        "WeaponDescriptor": {
            "Salves": 38,
        },
    },

    ("AutoCanon_HE_30mm_2A72_BMP3", "autocannon", None, False): { # 25
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 25,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.20,
                "TempsEntreDeuxFx": 0.20,
                "PhysicalDamages": 0.30,
                "SuppressDamages": 18,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "BaseSupplyCost": 2,
        "WeaponDescriptor": {
            "Salves": 37,
        },
    },

    ("AutoCanon_HE_30mm_24A2_BMP2", "autocannon", None, False): { # 24
        "Ammunition": {
            "hit_roll": {
                "Idling": 45,
                "Moving": 25,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.20,
                "TempsEntreDeuxFx": 0.20,
                "PhysicalDamages": 0.30,
                "SuppressDamages": 18,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "BaseSupplyCost": 2,
        "WeaponDescriptor": {
            "Salves": 62,
        },
    },

    ("AutoCanon_HE_30mm_24A2", "autocannon", None, False): { # 23
        "Ammunition": {
            "hit_roll": {
                "Idling": 45,
                "Moving": 25,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.20,
                "TempsEntreDeuxFx": 0.20,
                "PhysicalDamages": 0.30,
                "SuppressDamages": 18,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "BaseSupplyCost": 2,
        "WeaponDescriptor": {
            "Salves": 62,
        },
    },

    ("AutoCanon_HE_25mm_M242_Bushmaster_Late", "autocannon", None, False): { # 22
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 30,
            },
            "parent_membr": {
                "PhysicalDamages": 0.25,
                "SuppressDamages": 15,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "BaseSupplyCost": 2,
        "WeaponDescriptor": {
            "Salves": 60,
        },
    },

    ("AutoCanon_HE_25mm_KBA", "autocannon", None, False): { # 21
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.40, # was 0.35 but Eugen said it has to be multiple of game tick rate (10hz)
                "TempsEntreDeuxFx": 0.40,
                "PhysicalDamages": 0.25,
                "SuppressDamages": 15,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "BaseSupplyCost": 2,
    },

    ("AutoCanon_HE_23mm_NS23", "autocannon", None, False): { # 20
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.10, # was 0.12 but Eugen said it has to be multiple of game tick rate (10hz)
                "TempsEntreDeuxFx": 0.10,
                "PhysicalDamages": 0.20,
                "SuppressDamages": 10,
                "DisplaySalveAccuracy": False,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "BaseSupplyCost": 2,
    },

    ("AutoCanon_HE_23mm_Bitube_Gsh23L", "autocannon", None, False): { # 19
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
                "Moving": 15,
            },
            "parent_membr": {
                "Caliber": ("Dual 23mm", "LNXURRBEMR"),
                "PhysicalDamages": 0.5,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "TempsEntreDeuxSalves": 0.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 16,
            },
        },
        "BaseSupplyCost": 4,
    },

    ("AutoCanon_HE_20mm_MK_20_Rh_202", "autocannon", None, False): { # 18
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "PhysicalDamages": 0.2,
                "SuppressDamages": 10,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 0.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "BaseSupplyCost": 2,
    },

    ("AutoCanon_HE_20mm_M621_GIAT_AMX30", "autocannon", None, False): { # 17
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "PhysicalDamages": 0.2,
                "SuppressDamages": 10,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 0.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "BaseSupplyCost": 2,
    },

    ("AutoCanon_HE_20mm_M621_GIAT", "autocannon", None, False): { # 16
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "PhysicalDamages": 0.2,
                "SuppressDamages": 10,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 0.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "BaseSupplyCost": 2,
    },
    
    ("AutoCanon_AP_30mm_M230", "autocannon", None, False): { # 13
        "Ammunition": {
            "Arme": {
                "Index": 6,
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 40,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.1,
                "TempsEntreDeuxFx": 0.1,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.0,
                "TempsEntreDeuxSalves": 1.5,
                "NbTirParSalves": 20,
                "SupplyCost": 10,
                "AffichageMunitionParSalve": 20,
            },
        },
        "WeaponDescriptor": {
            "Salves": 40,
        },
    },

    ("AutoCanon_AP_30mm_L21A1_RARDEN", "autocannon", None, False): { # 12
        "Ammunition": {
            "Arme": {
                "Index": 13,
            },
            "hit_roll": {
                "Idling": 65,
                "Moving": 0,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'HE', 'KINETIC'],
                "TempsEntreDeuxTirs": 0.7,
                "TempsEntreDeuxFx": 0.7,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "TempsEntreDeuxSalves": 1.8,
                "NbTirParSalves": 6,
                "SupplyCost": 2,
                "CanShootWhileMoving": False,
                "AffichageMunitionParSalve": 6,
            },
        },
        "WeaponDescriptor": {
            "Salves": 38,
        },
    },

    ("AutoCanon_AP_30mm_2A72_BMP3", "autocannon", None, False): { # 10
        "Ammunition": {
            "Arme": {
                "Index": 12,
            },
            "hit_roll": {
                "Idling": 55,
                "Moving": 30,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.20,
                "TempsEntreDeuxFx": 0.20,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 18,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.6,
                "NbTirParSalves": 8,
                "SupplyCost": 2,
                "AffichageMunitionParSalve": 8,
            },
        },
        "WeaponDescriptor": {
            "Salves": 37,
        },
    },

    ("AutoCanon_AP_30mm_24A2_BMP2", "autocannon", None, False): { # 9
        "Ammunition": {
            "Arme": {
                "Index": 12,
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 25,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.20,
                "TempsEntreDeuxFx": 0.20,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 18,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.6,
                "NbTirParSalves": 8,
                "SupplyCost": 2,
                "AffichageMunitionParSalve": 8,
            },
        },
        "WeaponDescriptor": {
            "Salves": 62,
        },
    },

    ("AutoCanon_AP_30mm_24A2", "autocannon", None, False): { # 8
        "Ammunition": {
            "Arme": {
                "Index": 7,
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 25,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.20,
                "TempsEntreDeuxFx": 0.20,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 18,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.6,
                "NbTirParSalves": 8,
                "SupplyCost": 2,
                "AffichageMunitionParSalve": 8,
            },
        },
        "WeaponDescriptor": {
            "Salves": 62,
        },
    },

    ("AutoCanon_AP_25mm_M242_Bushmaster_Late", "autocannon", None, False): { # 7
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 30,
            },
            "parent_membr": {
                "Caliber": ("25mm APFSDS", "IQRYAPQHPQ"),
                "PhysicalDamages": 0.334,
                "SuppressDamages": 15,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.6,
                "NbTirParSalves": 8,
                "SupplyCost": 2,
                "AffichageMunitionParSalve": 8,
            },
        },
        "WeaponDescriptor": {
            "Salves": 60,
        },
    },

    ("AutoCanon_AP_25mm_KBA", "autocannon", None, False): { # 6
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 25,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.40, # was 0.35 but Eugen said it has to be multiple of game tick rate (10hz)
                "TempsEntreDeuxFx": 0.40,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 15,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.6,
                "NbTirParSalves": 8,
                "SupplyCost": 2,
                "AffichageMunitionParSalve": 8,
            },
        },
    },

    ("AutoCanon_AP_23mm_NS23", "autocannon", None, False): { # 5
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.10, # was 0.12 but Eugen said it has to be multiple of game tick rate (10hz)
                "TempsEntreDeuxFx": 0.10,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 10,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 8,
                "SupplyCost": 2,
                "AffichageMunitionParSalve": 8,
            },
        },
    },

    ("AutoCanon_AP_23mm_Bitube_Gsh23L", "autocannon", None, False): { # 4
        "Ammunition": {
            "Arme": {
                "Index": 6,
            },
            "hit_roll": {
                "Idling": 25,
                "Moving": 15,
            },
            "parent_membr": {
                "Caliber": ("Dual 23mm", "LNXURRBEMR"),
                "PhysicalDamages": 0.667,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "TempsEntreDeuxSalves": 0.6,
                "NbTirParSalves": 8,
                "SupplyCost": 4,
                "AffichageMunitionParSalve": 16,
            },
        },
    },

    ("AutoCanon_AP_20mm_MK_20_Rh_202", "autocannon", None, False): { # 3
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "PhysicalDamages": 0.334,
                "SuppressDamages": 10,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 0.6,
                "NbTirParSalves": 8,
                "SupplyCost": 2,
                "AffichageMunitionParSalve": 8,
            },
        },
    },

    ("AutoCanon_AP_20mm_M621_GIAT_AMX30", "autocannon", None, False): { # 2
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "PhysicalDamages": 0.334,
                "SuppressDamages": 10,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 0.6,
                "NbTirParSalves": 8,
                "SupplyCost": 2,
                "AffichageMunitionParSalve": 8,
            },
        },
    },

    ("AutoCanon_AP_20mm_M621_GIAT", "autocannon", None, False): { # 1
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "PhysicalDamages": 0.334,
                "SuppressDamages": 10,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 0.6,
                "NbTirParSalves": 8,
                "SupplyCost": 2,
                "AffichageMunitionParSalve": 8,
            },
        },
    },
    # note: check if these aren't duplicate entries
    ("GatlingAir_M61_Vulcan_20mm", "autocannon", None, False): { # 338
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 6,
            },
        },
    },

    ("Gatling_m134_7_62mm_x2", "autocannon", None, False): { # 321
        "Ammunition": {
            "parent_membr": {
                "DisplaySalveAccuracy": False,
                "SupplyCost": 5,
            },
        },
    },

    ("Gatling_m134_7_62mm", "autocannon", None, False): { # 320
        "Ammunition": {
            "parent_membr": {
                "DisplaySalveAccuracy": False,
                "SupplyCost": 5,
            },
        },
    },

    ("Gatling_M61_Vulcan_20mm_noRadar", "autocannon", None, False): { # 319
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2275,
                "PorteeMaximaleHAGRU": 1750,
                "TempsDeVisee": 1.25,
                "SupplyCost": 15,
            },
        },
    },

    ("Gatling_M61_Vulcan_20mm_late", "autocannon", None, False): { # 317
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 2100,
                "TempsDeVisee": 1.25,
                "SupplyCost": 15,
            },
        },
    },

    ("Gatling_M61_Vulcan_20mm_TOWED", "autocannon", None, False): { # 316
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 2450,
                "PorteeMaximaleHAGRU": 2100,
                "TempsDeVisee": 1.25,
                "SupplyCost": 15,
            },
        },
    },

    ("Gatling_M197_20mm", "autocannon", None, False): { # 314
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 15,
            },
            "parent_membr": {
                "PhysicalDamages": 0.25,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.4,
                "NbTirParSalves": 30,
                "SupplyCost": 7,
                "AffichageMunitionParSalve": 30,
            },
        },
        "WeaponDescriptor": {
            "Salves": 25,
        },
    },

    ("Gatling_JakB_12_7mm", "autocannon", None, False): { # 313
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
                "Moving": 10,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1225,
                "PorteeMaximaleTBAGRU": 1225,
                "PhysicalDamages": 0.48,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 30,
                "SupplyCost": 15,
                "AffichageMunitionParSalve": 200,
            },
        },
        "WeaponDescriptor": {
            "Salves": 7,
        },
    },
    
    ("Gatling_AP_M197_20mm", "autocannon", None, False): { # 311
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
                "Moving": 15,
            },
            "parent_membr": {
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.25,
                "TempsEntreDeuxSalves": 1.4,
                "NbTirParSalves": 30,
                "SupplyCost": 7,
                "AffichageMunitionParSalve": 30,
            },
        },
        "WeaponDescriptor": {
            "Salves": 25,
        },
    },
}
# fmt: on
