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
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.3,
                "SuppressDamages": 30,
                "SalvoShotsSorted": False,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.0,
                "TimeBetweenTwoSalvos": 1.5,
                "NbTirParSalves": 20,
                "SupplyCost": 10,
                "AffichageMunitionParSalve": 20,
            },
        },
        "WeaponDescriptor": {
            "Salves": 40,
        },
    },
    
    ("AutoCanon_HE_30mm_Bitube_Gsh30k_burst", "autocannon", "AutoCanon_HE_30mm_Bitube_Gsh30k", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
                "Moving": 10,
            },
            "parent_membr": {
                "ImpactHappening": ['Gsh301'],
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 1.2,
                "SuppressDamages": 125,
                "DisplaySalveAccuracy": False,
                "TimeBetweenTwoSalvos": 5.0,
                "NbTirParSalves": 10,
                "SupplyCost": 30,
                "AffichageMunitionParSalve": 50,
            },
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
                "TimeBetweenTwoShots": 0.7,
                "TimeBetweenTwoFx": 0.7,
                "PhysicalDamages": 0.40,
                "SuppressDamages": 30,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.8,
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
                "TimeBetweenTwoShots": 0.20,
                "TimeBetweenTwoFx": 0.20,
                "PhysicalDamages": 0.30,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.6,
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
                "TimeBetweenTwoShots": 0.20,
                "TimeBetweenTwoFx": 0.20,
                "PhysicalDamages": 0.30,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.6,
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
                "TimeBetweenTwoShots": 0.20,
                "TimeBetweenTwoFx": 0.20,
                "PhysicalDamages": 0.30,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.6,
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
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.6,
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
                "TimeBetweenTwoShots": 0.40, # was 0.35 but Eugen said it has to be multiple of game tick rate (10hz)
                "TimeBetweenTwoFx": 0.40,
                "PhysicalDamages": 0.25,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.6,
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
                "TimeBetweenTwoShots": 0.10, # was 0.12 but Eugen said it has to be multiple of game tick rate (10hz)
                "TimeBetweenTwoFx": 0.10,
                "PhysicalDamages": 0.20,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "TimeBetweenTwoSalvos": 1.0,
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
                "PhysicalDamages": 0.4,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "TimeBetweenTwoSalvos": 0.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 16,
            },
        },
        "BaseSupplyCost": 4,
    },

    ("AutoCanon_HE_20mm_MK_20_Rh_202", "autocannon", None, False): { # 18
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
                "Moving": 15,
            },
            "parent_membr": {
                "ImpactHappening": ['CanonPetitFK20HEFI'],
                "PhysicalDamages": 0.2,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
    },
    
    ("AutoCanon_HE_M693_F1_20mm", "autocannon", None, False): { # 17
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "ImpactHappening": ['CanonPetitFK20HEFI'],
                "PhysicalDamages": 0.2,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
    },
    
    ("AutoCanon_HE_M693_F1_20mm_15acc", "autocannon", "AutoCanon_HE_M693_F1_20mm", True): { # 17
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
                "Moving": 10,
            },
            "parent_membr": {
                "ImpactHappening": ['CanonPetitFK20HEFI'],
                "PhysicalDamages": 0.2,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
    },

    ("AutoCanon_HE_20mm_M621_GIAT_AMX30", "autocannon", None, False): { # 17
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "ImpactHappening": ['CanonPetitFK20HEFI'],
                "PhysicalDamages": 0.2,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
    },

    ("AutoCanon_HE_20mm_M621_GIAT", "autocannon", None, False): { # 16
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "ImpactHappening": ['CanonPetitFK20HEFI'],
                "PhysicalDamages": 0.2,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
    },
    
    ("AutoCanon_HE_T20_20mm", "autocannon", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "add": [
                    (17, "MaximumRangeAirplaneGRU = 1575"),
                    (17, "MinimumRangeHelicopterGRU = 35"),
                    (17, "MinimumRangeAirplaneGRU = 35"),
                ],
                "ImpactHappening": ['CanonPetitFK20HEFI'],
                "MaximumRangeHelicopterGRU": 2100,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 0.8,
                "PhysicalDamages": 0.2,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
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
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 25,
                "SalvoShotsSorted": False,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.0,
                "TimeBetweenTwoSalvos": 1.5,
                "NbTirParSalves": 20,
                "SupplyCost": 10,
                "AffichageMunitionParSalve": 20,
            },
        },
        "WeaponDescriptor": {
            "Salves": 40,
        },
    },
    
    ("AutoCanon_AP_30mm_Bitube_Gsh30k_burst", "autocannon", "AutoCanon_AP_30mm_Bitube_Gsh30k", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 15,
                "Moving": 10,
            },
            "parent_membr": {
                "ImpactHappening": ['Gsh301'],
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoFx": 0.1,
                "PhysicalDamages": 1.337,
                "SuppressDamages": 125,
                "DisplaySalveAccuracy": False,
                "TimeBetweenTwoSalvos": 5.0,
                "NbTirParSalves": 10,
                "SupplyCost": 30,
                "AffichageMunitionParSalve": 50,
            },
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
                "TimeBetweenTwoShots": 0.7,
                "TimeBetweenTwoFx": 0.7,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 30,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.8,
                "NbTirParSalves": 6,
                "CanShootWhileMoving": False,
                "AffichageMunitionParSalve": 6,
            },
        },
        "WeaponDescriptor": {
            "Salves": 38,
        },
        "BaseSupplyCost": 2,
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
                "TimeBetweenTwoShots": 0.20,
                "TimeBetweenTwoFx": 0.20,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "WeaponDescriptor": {
            "Salves": 37,
        },
        "BaseSupplyCost": 2,
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
                "TimeBetweenTwoShots": 0.20,
                "TimeBetweenTwoFx": 0.20,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "WeaponDescriptor": {
            "Salves": 62,
        },
        "BaseSupplyCost": 2,
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
                "TimeBetweenTwoShots": 0.20,
                "TimeBetweenTwoFx": 0.20,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "WeaponDescriptor": {
            "Salves": 62,
        },
        "BaseSupplyCost": 2,
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
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "WeaponDescriptor": {
            "Salves": 60,
        },
        "BaseSupplyCost": 2,
    },

    ("AutoCanon_AP_25mm_KBA", "autocannon", None, False): { # 6
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 25,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.40, # was 0.35 but Eugen said it has to be multiple of game tick rate (10hz)
                "TimeBetweenTwoFx": 0.40,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.6,
                "NbTirParSalves": 8,
                "AffichageMunitionParSalve": 8,
            },
        },
        "BaseSupplyCost": 2,
    },

    ("AutoCanon_AP_23mm_NS23", "autocannon", None, False): { # 5
        "Ammunition": {
            "hit_roll": {
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.10, # was 0.12 but Eugen said it has to be multiple of game tick rate (10hz)
                "TimeBetweenTwoFx": 0.10,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 25,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.0,
                "NbTirParSalves": 8,
                "SupplyCost": 2,
                "AffichageMunitionParSalve": 8,
            },
        },
        "BaseSupplyCost": 2,
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
                "TimeBetweenTwoSalvos": 0.6,
                "NbTirParSalves": 8,
                "SupplyCost": 4,
                "AffichageMunitionParSalve": 16,
            },
        },
    },

    ("AutoCanon_AP_20mm_MK_20_Rh_202", "autocannon", None, False): { # 3
        "Ammunition": {
            "Arme": {
                "Index": 10,
            },
            "hit_roll": {
                "BaseCriticModifier": 68,
                "Idling": 25,
                "Moving": 15,
            },
            "parent_membr": {
                "PhysicalDamages": 0.334,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
    },
    
    ("AutoCanon_AP_M693_F1_20mm", "autocannon", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 10,
            },
            "hit_roll": {
                "BaseCriticModifier": 68,
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "PhysicalDamages": 0.334,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
    },
    
    ("AutoCanon_AP_M693_F1_20mm_15acc", "autocannon", "AutoCanon_AP_M693_F1_20mm", True): {
        "Ammunition": {
            "Arme": {
                "Index": 10,
            },
            "hit_roll": {
                "BaseCriticModifier": 68,
                "Idling": 15,
                "Moving": 10,
            },
            "parent_membr": {
                "PhysicalDamages": 0.334,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
    },

    ("AutoCanon_AP_20mm_M621_GIAT_AMX30", "autocannon", None, False): { # 2
        "Ammunition": {
            "Arme": {
                "Index": 10,
            },
            "hit_roll": {
                "BaseCriticModifier": 68,
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "PhysicalDamages": 0.334,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
    },

    ("AutoCanon_AP_20mm_M621_GIAT", "autocannon", None, False): { # 1
        "Ammunition": {
            "Arme": {
                "Index": 10,
            },
            "hit_roll": {
                "BaseCriticModifier": 68,
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "PhysicalDamages": 0.334,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 1.0,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
    },
    
    ("AutoCanon_AP_T20_20mm", "autocannon", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_ap",
                "Index": 10,
            },
            "hit_roll": {
                "BaseCriticModifier": 68,
                "Idling": 20,
                "Moving": 10,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.1,
                "TimeBetweenTwoSalvos": 0.8,
                "PhysicalDamages": 0.334,
                "SuppressDamages": 20,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "NbTirParSalves": 15,
                "AffichageMunitionParSalve": 25,
            },
        },
        "BaseSupplyCost": 5,
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
                "MaximumRangeHelicopterGRU": 2275,
                "MaximumRangeAirplaneGRU": 1750,
                "AimingTime": 1.25,
                "SupplyCost": 15,
            },
        },
    },

    ("Gatling_M61_Vulcan_20mm_late", "autocannon", None, False): { # 317
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 2100,
                "AimingTime": 1.25,
                "SupplyCost": 15,
            },
        },
    },

    ("Gatling_M61_Vulcan_20mm_TOWED", "autocannon", None, False): { # 316
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2450,
                "MaximumRangeAirplaneGRU": 2100,
                "AimingTime": 1.25,
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
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.4,
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
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 1225,
                "PhysicalDamages": 0.48,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.0,
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
                "AimingTime": 1.25,
                "TimeBetweenTwoSalvos": 1.4,
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
