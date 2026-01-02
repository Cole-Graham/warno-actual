"""Small arms weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Sniper_FRF1", "small_arms", None, False): {  #735
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sniper",
            },
            "hit_roll": {
                "BaseCriticModifier": 0,
                "Idling": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 9.0,
                "TimeBetweenTwoFx": 9.0,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "MaximumRangeGRU": 1050,
                "MaximumRangeHelicopterGRU": 875,
                "DisplaySalveAccuracy": False,
                "TimeBetweenTwoSalvos": 9.0,
                "AimingTime": 6.0,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 10
            },
        },
        "SupplyCost": 2.0,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 10,
        },
    },
    
    ("Sniper_FRF2", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sniper",
            },
            "hit_roll": {
                "BaseCriticModifier": 0,
                "Idling": 65,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 9.0,
                "TimeBetweenTwoFx": 9.0,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "DisplaySalveAccuracy": False,
                "AimingTime": 6.0,
                "TimeBetweenTwoSalvos": 9.0,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 5,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 12,
        },
    },
    
    ("Sniper_SVD_Dragunov", "small_arms", None, False): {  #735
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sniper",
            },
            "hit_roll": {
                "BaseCriticModifier": 0,
                "Idling": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 9.0,
                "TimeBetweenTwoFx": 9.0,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "MaximumRangeGRU": 1050,
                "MaximumRangeHelicopterGRU": 875,
                "DisplaySalveAccuracy": False,
                "TimeBetweenTwoSalvos": 9.0,
                "AimingTime": 6.0,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 10
            },
        },
        "SupplyCost": 2.0,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 10,
        },
    },

    ("Sniper_G3A3ZF", "small_arms", None, False): {  #735
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sniper",
            },
            "hit_roll": {
                "BaseCriticModifier": 0,
                "Idling": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 9.0,
                "TimeBetweenTwoFx": 9.0,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "MaximumRangeGRU": 1050,
                "MaximumRangeHelicopterGRU": 875,
                "DisplaySalveAccuracy": False,
                "TimeBetweenTwoSalvos": 9.0,
                "AimingTime": 6.0,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 10
            },
        },
        "SupplyCost": 2.0,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 10,
        },
    },

    ("Sniper_M24", "small_arms", None, False): {  # 732
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sniper",
            },
            "hit_roll": {
                "BaseCriticModifier": 0,
                "Idling": 65,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 9.0,
                "TimeBetweenTwoFx": 9.0,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "DisplaySalveAccuracy": False,
                "AimingTime": 6.0,
                "TimeBetweenTwoSalvos": 9.0,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 5,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 12,
        },
    },

    ("Sniper_M21", "small_arms", None, False): {  #731
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sniper",
            },
            "hit_roll": {
                "BaseCriticModifier": 0,
                "Idling": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 9.0,
                "TimeBetweenTwoFx": 9.0,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "MaximumRangeGRU": 1050,
                "MaximumRangeHelicopterGRU": 875,
                "DisplaySalveAccuracy": False,
                "TimeBetweenTwoSalvos": 9.0,
                "AimingTime": 6.0,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 10
            },
        },
        "SupplyCost": 2.0,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 10,
        },
    },
    
    ("Sniper_L96A1", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sniper",
            },
            "hit_roll": {
                "BaseCriticModifier": 0,
                "Idling": 65,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 9.0,
                "TimeBetweenTwoFx": 9.0,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "DisplaySalveAccuracy": False,
                "TimeBetweenTwoSalvos": 9.0,
                "AimingTime": 6.0,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 5,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 12,
        },
    },

    ("SAW_lMG_K_7_62mm", "small_arms", None, False): {  #720
        # THIS IS NOT 7.62mm!!!!!!!!!!
        # todo: rename this, its 5.45mm... stupid eugen
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 30,
                "Moving": 15,
            },
            "parent_membr": {
                "Caliber": ("existing", "XUTVWWNOTF"),
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 18,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoSalvos": 1.4,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 40
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 15,
        },
    },

    ("SAW_RPK_74_5_56mm", "small_arms", None, False): {  #719
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 18,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoSalvos": 2.2,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 40
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 15,
        },
    },
    
    ("SAW_RPK_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 65,
                "Moving": 25,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 2.5,
                "NbTirParSalves": 3,
                "AffichageMunitionParSalve": 30
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 20,
        },
    },

    ("SAW_Minimi_5_56mm", "small_arms", None, False): {  #717
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 30,
                "Moving": 15,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.2,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 18,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 1.2,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 40
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 23,
        },
    },

    ("SAW_M249_5_56mm", "small_arms", None, False): {  #716
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 30,
                "Moving": 15,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.2,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 18,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 1.2,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 40
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 23,
        },
    },
    
    ("SAW_L86A1_5_56mm", "small_arms", None, False): {  #715
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Moving": 15,
            },
            "parent_membr": {
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 18,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoSalvos": 2.2,
                "NbTirParSalves": 3,
                "AffichageMunitionParSalve": 30
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 20,
        },
    },
    
    ("SAW_Bren_L4A4", "small_arms", None, False): {  # 712
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 65,
                "Moving": 25,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 2.5,
                "NbTirParSalves": 3,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 20,
        },
    },
    
    ("PM_MAT_49", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 35,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 450,
                "MaximumRangeHelicopterGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.1,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 18,               
        },
    },
    
    ("PM_MP_5SD", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 55,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 450,
                "MaximumRangeHelicopterGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.8,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [12, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 12,               
        },
    },
    
    ("PM_Sterling", "small_arms", None, False): {  # 572
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 35,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 450,
                "MaximumRangeHelicopterGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.1,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 18,               
        },
    },
    
    ("PM_Sterling_noreflex", "small_arms", "PM_Sterling", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 35,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 450,
                "MaximumRangeHelicopterGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.1,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2],
        "WeaponDescriptor": {
            "Salves": 18,               
        },
    },

    ("PM_uzi", "small_arms", None, False): {  # 572
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 35,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 450,
                "MaximumRangeHelicopterGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.1,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 18,
        },
    },

    ("PM_uzi_noreflex", "small_arms", "PM_uzi", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 35,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 450,
                "MaximumRangeHelicopterGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.1,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 18,
        },
    },

    ("PM_Skorpion", "small_arms", None, False): {  # 571
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 35,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 450,
                "MaximumRangeHelicopterGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.1,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [10, 9, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 18,               
        },
    },
    
    ("PM_PM63_RAK", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 35,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 450,
                "MaximumRangeHelicopterGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.1,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 18,               
        },
    },
    
    ("PM_MPi_AKSU_74NK", "small_arms", None, False): {  # 568
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.0,
                "MaximumRangeGRU": 525,
                "MaximumRangeHelicopterGRU": 450,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [5],
        "WeaponDescriptor": {
            "Salves": 11,               
        },
    },
    
    ("FM_SIG_543", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.0,
                "MaximumRangeGRU": 525,
                "MaximumRangeHelicopterGRU": 450,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [8, 6, 3, 1],
        "WeaponDescriptor": {
            "Salves": 11,               
        },
    },

    ("Commando_733", "small_arms", None, False): {  # renamed from PM_M4_Carbine 564
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.0,
                "MaximumRangeGRU": 525,
                "MaximumRangeHelicopterGRU": 450,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 50,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [9, 7, 5, 4, 3, 2],
        "NewTexture": "Commando_733",
        "WeaponDescriptor": {
            "Salves": 11,               
        },
    },

    ("M16A2_Carbine", "small_arms", "Commando_733", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "display": "M16A2 Carbine",
            "hit_roll": {
                "Idling": 60,
                "Moving": 45,
            },
            "token": "SZBMRVNELN",
            "parent_membr": {
                "TimeBetweenTwoShots": 1.0,
                "MaximumRangeGRU": 700,
                "MaximumRangeHelicopterGRU": 625,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [3],
        "NewTexture": "M16A1_Carbine",
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("M16A1_Carbine", "small_arms", "Commando_733", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "display": "M16A1 Carbine",
            "token": "VDUNUQCOUY",
            "hit_roll": {
                "Idling": 50,
                "Moving": 35,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.0,
                "MaximumRangeGRU": 700,
                "MaximumRangeHelicopterGRU": 625,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [11, 8, 7, 5, 4, 3, 2],
        "NewTexture": "M16A1_Carbine",
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },
    
    ("PM_C8_Carbine", "small_arms", None, False): {  # 562
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.0,
                "MaximumRangeGRU": 525,
                "MaximumRangeHelicopterGRU": 450,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [6, 5, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,               
        },
    },

    ("PM_AS_Val", "small_arms", None, False): {  # 560
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 70,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.4,
                "MaximumRangeGRU": 450,
                "MaximumRangeHelicopterGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.1,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [5, 4],
        "WeaponDescriptor": {
            "Salves": 18,               
        },
    },
    
    ("PM_AKSU_74", "small_arms", None, False): {  # 559
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 45,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.0,
                "MaximumRangeGRU": 525,
                "MaximumRangeHelicopterGRU": 450,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 0.5,
                "TimeBetweenTwoSalvos": 3.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 50,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [10, 8, 6, 5, 4],
        "WeaponDescriptor": {
            "Salves": 11,               
        },
    },
    
    ("MMG_turret_7_62mm_M60", "small_arms", "MMG_team_7_62mm_M60", True): { # LAV_25_M1047_US_US
        "Ammunition": {
            "display": "M60E3",
            "hit_roll": {
                "Idling": 70,
                "Moving": 30,
            },
            "token": "EILUZEIFXS",
            "parent_membr": {
                "TraitsToken": ['MOTION', 'tripod'],
                "MaximumRangeGRU": 1050,
                "MaximumRangeHelicopterGRU": 875,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.3,
                "NbTirParSalves": 5,
                "CanShootWhileMoving": "True",
                "AffichageMunitionParSalve": 50,
            },
        },
        "NbWeapons": [1],
        "SupplyCost": 1.0,
        "WeaponDescriptor": {
            "Salves": 48,
        },
    },
    
    ("MMG_inf_L7A2_7_62mm", "small_arms", None, False): {  # 485
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 70,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.9,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 1.9,
                "NbTirParSalves": 2,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 36,
        },
    },
    
    ("MMG_inf_MAG_7_62mm", "small_arms", None, False): {  # 485
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 70,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.9,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 1.9,
                "NbTirParSalves": 2,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 36,
        },
    },

    ("MMG_inf_M240B_7_62mm", "small_arms", None, False): {  # 484
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 70,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.9,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 1.9,
                "NbTirParSalves": 2,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 36,
        },
    },

    ("MMG_PKT_7_62mm_x2", "small_arms", None, False): {  # 476
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 25,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.2,
                "MaximumRangeGRU": 1050,
                "MaximumRangeHelicopterGRU": 875,
                "PhysicalDamages": 0.24,
                "SuppressDamages": 48.0,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.2,
                "TimeBetweenTwoSalvos": 1.2,
                "NbTirParSalves": 5,
                "SupplyCost": 2.0,
                "CanShootWhileMoving": "True",
                "AffichageMunitionParSalve": 50,
            },
        },
        "WeaponDescriptor": {
            "Salves": 64,
        },
    },

    ("MMG_PKT_7_62mm_x3", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 25,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.2,
                "MaximumRangeGRU": 1050,
                "MaximumRangeHelicopterGRU": 875,
                "PhysicalDamages": 0.36,
                "SuppressDamages": 72.0,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.2,
                "TimeBetweenTwoSalvos": 1.2,
                "NbTirParSalves": 5,
                "SupplyCost": 2.0,
                "CanShootWhileMoving": "True",
                "AffichageMunitionParSalve": 50,
            },
        },
        "WeaponDescriptor": {
            "Salves": 64,
        },  
    },
    
    ("MMG_PKT_7_62mm_x4", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 45,
                "Moving": 15,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.2,
                "MaximumRangeGRU": 1050,
                "MaximumRangeHelicopterGRU": 875,
                "PhysicalDamages": 0.48,
                "SuppressDamages": 96.0,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.2,
                "TimeBetweenTwoSalvos": 1.2,
                "NbTirParSalves": 5,
                "SupplyCost": 2.0,
                "CanShootWhileMoving": "True",
                "AffichageMunitionParSalve": 50,
            },
        },
        "WeaponDescriptor": {
            "Salves": 20,
        },
    },

    # ("MMG_PKT_7_62mm", "small_arms", None, False): {  # 475
    #     "Ammunition": {
    #         "hit_roll": {
    #             "Idling": 40,
    #             "Moving": 20,
    #         },
    #         "parent_membr": {
    #             "MaximumRangeGRU": 1050,
    #             "MaximumRangeHelicopterGRU": 875,
    #             "PhysicalDamages": 0.05,
    #             "SuppressDamages": 24,
    #             "DisplaySalveAccuracy": False,
    #             "AimingTime": 1.0,
    #             "TimeBetweenTwoSalvos": 0.5,
    #             "NbTirParSalves": 7,
    #             "SupplyCost": 1.0,
    #             "CanShootWhileMoving": "True",
    #             "AffichageMunitionParSalve": 35,
    #         },
    #     },
    #     "WeaponDescriptor": {
    #         "Salves": 260,
    #     },
    # },

    ("MMG_PKM_7_62mm", "small_arms", None, False): {  # 474
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 70,
                "Moving": 30,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.9,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 1.9,
                "NbTirParSalves": 2,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 45,
        },
    },

    ("MMG_inf__MG3_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 70,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.8,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 1.8,
                "NbTirParSalves": 2,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 45,
        },
    },
    
    ("MMG_M240d_7_62mm", "small_arms", None, False): {
        "is_standard": (True, "7_62mm_MMG_Helo"),
        "Ammunition": {
            "hit_roll": {
                "Idling": 70,
                "Moving": 30,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.9,
                "MaximumRangeGRU": 1050,
                "MaximumRangeHelicopterGRU": 875,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 1.9,
                "NbTirParSalves": 2,
                "AffichageMunitionParSalve": 20,
            }
        },
        "SupplyCost": 1.0,
    },
    
    ("MMG_FN_MAG_7_62mm_Helo", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240d_7_62mm",
            "parent_membr": "MMG_M240d_7_62mm",
        },
        "SupplyCost": "MMG_M240d_7_62mm",
    },
        
    ("MMG_MG3_7_62mm_helo", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240d_7_62mm",
            "parent_membr": "MMG_M240d_7_62mm",
        },
        "SupplyCost": "MMG_M240d_7_62mm",
    },
    
    ("MMG_MG3S_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240d_7_62mm",
            "parent_membr": "MMG_M240d_7_62mm",
        },
        "SupplyCost": "MMG_M240d_7_62mm",
    },
    
    ("MMG_HK21_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240d_7_62mm",
            "parent_membr": "MMG_M240d_7_62mm",
        },
        "SupplyCost": "MMG_M240d_7_62mm",
    },
    
    ("MMG_M60_7_62mm_helo", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240d_7_62mm",
            "parent_membr": "MMG_M240d_7_62mm",
        },
        "SupplyCost": "MMG_M240d_7_62mm",
    },
    
    ("MMG_MG42_7_62mm_helo", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240d_7_62mm",
            "parent_membr": "MMG_M240d_7_62mm",
        },
        "SupplyCost": "MMG_M240d_7_62mm",
    },

    ("MMG_WA_M60E3_7_62mm", "small_arms", None, False): {  # 469
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "display": "M60E3",
            "hit_roll": {
                "Idling": 70,
                "Moving": 30,
            },
            "token": "IYUAMGSZZJ", 
            "parent_membr": {
                "TimeBetweenTwoShots": 1.9,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 1.9,
                "NbTirParSalves": 2,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 45,
        },
    },
    
    ("MMG_team_7_62mm_FN_MAG", "small_arms", None, False): {
        "Ammunition": {
            "is_standard": (True, "7_62mm_MMG_Team"),
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 70,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1050,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "TimeBetweenTwoSalvos": 4.3,
                "NbTirParSalves": 5,
                "SupplyCost": 2.0,
                "AffichageMunitionParSalve": 50,
            },
        },
        "NbWeapons": [1],
    },
    
    ("MMG_team_7_62mm_AANF1", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "MMG_team_7_62mm_FN_MAG",
            "hit_roll": "MMG_team_7_62mm_FN_MAG",
            "parent_membr": "MMG_team_7_62mm_FN_MAG",
        },
        "NbWeapons": "MMG_team_7_62mm_FN_MAG",
    },
    
    ("MMG_team_7_62mm_M1919", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "MMG_team_7_62mm_FN_MAG",
            "hit_roll": "MMG_team_7_62mm_FN_MAG",
            "parent_membr": "MMG_team_7_62mm_FN_MAG",
        },
        "NbWeapons": "MMG_team_7_62mm_FN_MAG",
    },
    
    ("MMG_team_7_62mm_M60", "small_arms", None, False): { # 469
        "Ammunition": {
            "display": "M60E3",
            "token": "IYUAMGSZZJ", 
            "Arme": "MMG_team_7_62mm_FN_MAG",
            "hit_roll": "MMG_team_7_62mm_FN_MAG",
            "parent_membr": "MMG_team_7_62mm_FN_MAG",
        },
        "NbWeapons": "MMG_team_7_62mm_FN_MAG",
    },
    
    ("MMG_team_7_62mm_MG3", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "MMG_team_7_62mm_FN_MAG",
            "hit_roll": "MMG_team_7_62mm_FN_MAG",
            "parent_membr": "MMG_team_7_62mm_FN_MAG",
        },
        "NbWeapons": "MMG_team_7_62mm_FN_MAG",
    },
    
    ("MMG_team_7_62mm_MG42_59", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "MMG_team_7_62mm_FN_MAG",
            "hit_roll": "MMG_team_7_62mm_FN_MAG",
            "parent_membr": "MMG_team_7_62mm_FN_MAG",
        },
        "NbWeapons": "MMG_team_7_62mm_FN_MAG",
    },
    
    ("MMG_team_7_62mm_PKM", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "MMG_team_7_62mm_FN_MAG",
            "hit_roll": "MMG_team_7_62mm_FN_MAG",
            "parent_membr": "MMG_team_7_62mm_FN_MAG",
        },
        "NbWeapons": "MMG_team_7_62mm_FN_MAG",
    },
    
    ("MMG_inf_AANF1_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 70,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.9,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 1.9,
                "NbTirParSalves": 2,
                "SupplyCost": 1.0,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 45,
        },
    },

    ("MMG_M60E1_7_62mm", "small_arms", "MMG_WA_M60E3_7_62mm", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "display": "M60E1",
            "hit_roll": {
                "Idling": 70,
                "Moving": 30,
            },
            "token": "GVHHKBBTHW",
            "parent_membr": {
                "TimeBetweenTwoShots": 1.9,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 1.9,
                "NbTirParSalves": 2,
                "SupplyCost": 1.0,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 45,
        },
    },
    
    ("MMG_M240_7_62mm", "small_arms", None, False): {
        "is_standard": (True, "7_62mm_MMG_Coax"), 
        "Ammunition": {
            "hit_roll": {
                "Idling": 70,
                "Moving": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1050,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "TimeBetweenTwoSalvos": 4.3,
                "NbTirParSalves": 5,
                "SupplyCost": 1.0,
                "AffichageMunitionParSalve": 25, 
            },
        },
        "NbWeapons": [1],
        "SupplyCost": 1.0,
    },
    
    ("MMG_L8A2_7_62mm", "small_arms", None, False): { # challenger coax
        "Ammunition": {
            "hit_roll": "MMG_M240_7_62mm",
            "parent_membr": "MMG_M240_7_62mm",
        },
        "SupplyCost": "MMG_M240_7_62mm",
        "NbWeapons": "MMG_M240_7_62mm"
    },
    
    ("MMG_L94A1_7_62mm", "small_arms", None, False): { # Warrior coax
        "Ammunition": {
            "hit_roll": "MMG_M240_7_62mm",
            "parent_membr": "MMG_M240_7_62mm",
        },
        "SupplyCost": "MMG_M240_7_62mm",
        "NbWeapons": "MMG_M240_7_62mm",
    },
    
    ("MMG_L43A1_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240_7_62mm",
            "parent_membr": "MMG_M240_7_62mm",
        },
        "SupplyCost": "MMG_M240_7_62mm",
        "NbWeapons": "MMG_M240_7_62mm",
    },
    
    ("MMG_DTM_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240_7_62mm",
            "parent_membr": "MMG_M240_7_62mm",
        },
        "SupplyCost": "MMG_M240_7_62mm",
        "NbWeapons": "MMG_M240_7_62mm",
    },
    
    ("MMG_M60_7_62mm_coax", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240_7_62mm",
            "parent_membr": "MMG_M240_7_62mm",
        },
        "SupplyCost": "MMG_M240_7_62mm",
        "NbWeapons": "MMG_M240_7_62mm",
    },
    
    ("MMG_M240_abrams_7_62mm", "small_arms", None, False): {
        "is_standard": (True, "7_62mm_MMG_Turret"),
        "Ammunition": {
            "hit_roll": {
                "Idling": 70,
                "Moving": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1050,
                "MaximumRangeHelicopterGRU": 875,
                "PhysicalDamages": 0.12,
                "SuppressDamages": 24,
                "TimeBetweenTwoSalvos": 4.3,
                "NbTirParSalves": 5,
                "SupplyCost": 1.0,
                "AffichageMunitionParSalve": 25,
            }
        },
        "SupplyCost": 1.0,
        "NbWeapons": [1],
    },
    
    ("MMG_PKT_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240_abrams_7_62mm",
            "parent_membr": "MMG_M240_abrams_7_62mm",
        },
        "SupplyCost": "MMG_M240_abrams_7_62mm",
        "NbWeapons": "MMG_M240_abrams_7_62mm",
    },
    
    ("MMG_SGMB_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240_abrams_7_62mm",
            "parent_membr": "MMG_M240_abrams_7_62mm",
        },
        "SupplyCost": "MMG_M240_abrams_7_62mm",
        "NbWeapons": "MMG_M240_abrams_7_62mm",
    },
    
    
    
    ("MMG_M60_7_62mm_veh", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240_abrams_7_62mm",
            "parent_membr": "MMG_M240_abrams_7_62mm",
        },
        "SupplyCost": "MMG_M240_abrams_7_62mm",
        "NbWeapons": "MMG_M240_abrams_7_62mm",
    },
    
    ("MMG_M60D_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240_abrams_7_62mm",
            "parent_membr": "MMG_M240_abrams_7_62mm",
        },
        "SupplyCost": "MMG_M240_abrams_7_62mm",
        "NbWeapons": "MMG_M240_abrams_7_62mm",
    },
    
    ("MMG_FN_MAG_7_62mm", "small_arms", None, False): { # Eugen using this as turret and coax
        "Ammunition": {
            "hit_roll": "MMG_M240_abrams_7_62mm",
            "parent_membr": "MMG_M240_abrams_7_62mm",
        },
        "SupplyCost": "MMG_M240_abrams_7_62mm",
        "NbWeapons": "MMG_M240_abrams_7_62mm",
    },
    
    ("MMG_L37A2_7_62mm", "small_arms", None, False): { # Saxon, chieftain turret
        "Ammunition": {
            "hit_roll": "MMG_M240_abrams_7_62mm",
            "parent_membr": "MMG_M240_abrams_7_62mm",
        },
        "SupplyCost": "MMG_M240_abrams_7_62mm",
        "NbWeapons": "MMG_M240_abrams_7_62mm",
    },
    
    ("MMG_MG3_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240_abrams_7_62mm",
            "parent_membr": "MMG_M240_abrams_7_62mm",
        },
        "SupplyCost": "MMG_M240_abrams_7_62mm",
        "NbWeapons": "MMG_M240_abrams_7_62mm",
    },
    
    ("MMG_AANF1_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240_abrams_7_62mm",
            "parent_membr": "MMG_M240_abrams_7_62mm",
        },
        "SupplyCost": "MMG_M240_abrams_7_62mm",
        "NbWeapons": "MMG_M240_abrams_7_62mm",
    },
    
    ("MMG_M1919", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": "MMG_M240_abrams_7_62mm",
            "parent_membr": "MMG_M240_abrams_7_62mm",
        },
        "SupplyCost": "MMG_M240_abrams_7_62mm",
        "NbWeapons": "MMG_M240_abrams_7_62mm",
    },
    
    ("Lance_grenade_Mk19_40mm", "AGL", None, False): {  # 451
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
                "Moving": 15,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.2,
                "MaximumRangeGRU": 1575,
                "DispersionAtMaxRangeGRU": 70,
                "RadiusSplashPhysicalDamagesGRU": 30,
                "PhysicalDamages": 0.25,
                "RadiusSplashSuppressDamagesGRU": 56,
                "SuppressDamages": 15.0,
                "DisplaySalveAccuracy": False,
                "AimingTime": 2.5,
                "TimeBetweenTwoSalvos": 4.0,
                "NbTirParSalves": 8,
                "SupplyCost": 5.0,
                "AffichageMunitionParSalve": 8,
            },
        },
        "WeaponDescriptor": {
            "Salves": 30,
        },
    },

    ("Lance_grenade_AGS17", "AGL", None, False): {  # 449
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
                "Moving": 15,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 0.2,
                "MaximumRangeGRU": 1225,
                "DispersionAtMaxRangeGRU": 60,
                "RadiusSplashPhysicalDamagesGRU": 22,
                "PhysicalDamages": 0.25,
                "RadiusSplashSuppressDamagesGRU": 42,
                "SuppressDamages": 10.0,
                "DisplaySalveAccuracy": False,
                "AimingTime": 2.5,
                "TimeBetweenTwoSalvos": 4.0,
                "NbTirParSalves": 10,
                "SupplyCost": 5.0,
                "AffichageMunitionParSalve": 10,
            },
        },
        "WeaponDescriptor": {
            "Salves": 30,
        },
    },
    
    ("HMG_team_12_7_mm_NSV_6U6", "small_arms", None, False): {
        "is_standard": (True, "DCA_12_7mm_HMG_Team"),
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_12_7",
            },
            "hit_roll": {
                "Idling": 70,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 1050,
                "PhysicalDamages": 0.20,
                "SuppressDamages": 42,
                "TimeBetweenTwoSalvos": 4.3,
                "NbTirParSalves": 5,
                "SupplyCost": 2.0,
                "AffichageMunitionParSalve": 50,
            },
        },
        "NbWeapons": [1],
    },
    
    ("HMG_team_12_7_mm_M2HB_M63", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "HMG_team_12_7_mm_NSV_6U6",
            "parent_membr": "HMG_team_12_7_mm_NSV_6U6",
        },
        "NbWeapons": "HMG_team_12_7_mm_NSV_6U6",
    },
    
    ("HMG_team_12_7_mm_DSh_AA", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "HMG_team_12_7_mm_NSV_6U6",
            "parent_membr": "HMG_team_12_7_mm_NSV_6U6",
        },
        "NbWeapons": "HMG_team_12_7_mm_NSV_6U6",
    },
    
    ("HMG_team_12_7_mm_M2HB", "small_arms", None, False): {
        "is_standard": (True, "12_7mm_HMG_Team"), 
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_12_7",
            },
            "hit_roll": {
                "Idling": 70,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 1050,
                "PhysicalDamages": 0.20,
                "SuppressDamages": 42,
                "TimeBetweenTwoSalvos": 4.3,
                "NbTirParSalves": 5,
                "SupplyCost": 2.0,
                "AffichageMunitionParSalve": 50,
            },
        },
        "NbWeapons": [1],
    },
    
    ("HMG_team_12_7_mm_DSh", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "HMG_team_12_7_mm_M2HB",
            "hit_roll": "HMG_team_12_7_mm_M2HB",
            "parent_membr": "HMG_team_12_7_mm_M2HB",
        },
        "NbWeapons": "HMG_team_12_7_mm_M2HB",
    },
    
    ("HMG_team_12_7_mm_NSV", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "HMG_team_12_7_mm_M2HB",
            "hit_roll": "HMG_team_12_7_mm_M2HB",
            "parent_membr": "HMG_team_12_7_mm_M2HB",
        },
        "NbWeapons": "HMG_team_12_7_mm_M2HB",
    },
    
    ("DCA_1_canon_KPVT_14_5mm", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_14_5",
            },
            "hit_roll": {
                "Idling": 70,
                "Moving": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1400,
                "MaximumRangeHelicopterGRU": 1925,
                "MaximumRangeAirplaneGRU": 1575,
                "PhysicalDamages": 0.24,
                "SuppressDamages": 48,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.3,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 50,
            },
        },
        "WeaponDescriptor": {
            "Salves": 48,
        },
    },

    ("HMG_14_5_mm_KPVT", "small_arms", None, False): {  # 353
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_14_5",
            },
            "hit_roll": {
                "Idling": 70,
                "Moving": 30,
            },
            "parent_membr": {
                "PhysicalDamages": 0.24,
                "SuppressDamages": 48,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.3,
                "SupplyCost": 2.0,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 50,
            },
        },
        "WeaponDescriptor": { 
            "Salves": 48,
        },
    },
    
    ("HMG_12_7_mm_avenger_M3P", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_12_7",
            },
        },
    },
    
    ("HMG_12_7_mm_M2HB", "small_arms", None, False): {
        "is_standard": (True, "12_7mm_HMG_Turret"),
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_12_7",
            },
            "hit_roll": {
                "Idling": 70,
                "Moving": 30,
            },
            "parent_membr": {
                "MaximumRangeGRU": 1225,
                "MaximumRangeHelicopterGRU": 1050,
                "PhysicalDamages": 0.20,
                "SuppressDamages": 42,
                "TimeBetweenTwoSalvos": 4.3,
                "NbTirParSalves": 5,
                "SupplyCost": 2.0,
                "AffichageMunitionParSalve": 50,
            },
        },
        "NbWeapons": [1],
    },
    
    ("HMG_12_7_mm_M85", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "HMG_12_7_mm_M2HB",
            "hit_roll": "HMG_12_7_mm_M2HB",
            "parent_membr": "HMG_12_7_mm_M2HB",
        },
        "NbWeapons": "HMG_12_7_mm_M2HB",
    },
    
    ("HMG_12_7_mm_NSVT", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "HMG_12_7_mm_M2HB",
            "hit_roll": "HMG_12_7_mm_M2HB",
            "parent_membr": "HMG_12_7_mm_M2HB",
        },
        "NbWeapons": "HMG_12_7_mm_M2HB",
    },
    
    ("HMG_12_7_mm_DShKM", "small_arms", None, False): {
        "Ammunition": {
            "Arme": "HMG_12_7_mm_M2HB",
            "hit_roll": "HMG_12_7_mm_M2HB",
            "parent_membr": "HMG_12_7_mm_M2HB",
        },
        "NbWeapons": "HMG_12_7_mm_M2HB",
    },
    
    ("HMG_12_7_mm_Afanasyev", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_12_7",
            },
        },
    },

    # FM_kbk_AKM is now deprecated
    
    ("FM_kbk_AK", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.2,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 8,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 6.0,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
            "token": "AYYOIYKCVF",
        },
        "Texture": "FM_kbk_AKM",
        "SupplyCost": 1.0,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },
    
    ("FM_kbk_AK_noreflex", "small_arms", "FM_kbk_AK", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.2,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 8,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 6.0,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
            "token": "AYYOIYKCVF",
        },
        "Texture": "FM_kbk_AKM",
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_kbk_AKMS", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.2,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 8,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 6.0,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
            # "token": "AYYOIYKCVF",
        },
        # "NewTexture": "kbk_akm",
        "SupplyCost": 1.0,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_kbk_AKMS_noreflex", "small_arms", "FM_kbk_AKMS", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 2.2,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 8,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 6.0,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
            "token": "AYYOIYKCVF",
        },
        "Texture": "FM_kbk_AKM",
        "SupplyCost": 1.0,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },
    
    ("FM_Tantal", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 25,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [5, 4, 2],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_Mpi_AK_74N", "small_arms", None, False): {  # 303
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_Mpi_AK_74N_noreflex", "small_arms", "FM_Mpi_AK_74N", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_Mpi_AKS_74NK", "small_arms", None, False): {  # 302
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_Mpi_AKS_74NK_noreflex", "small_arms", "FM_Mpi_AKS_74NK", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },
    
    ("FM_MAS_56", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 55,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 3.0,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 8,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 6.0,
                "NbTirParSalves": 2,
                "AffichageMunitionParSalve": 10,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 22,
        },
    },
    
    ("FM_FAMAS", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },
    
    ("FM_FAMAS_noreflex", "small_arms", "FM_FAMAS", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_M16A1", "small_arms", None, False): {  # 300
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 35,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.7,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [10, 9, 8, 7, 6, 5, 4, 3, 1],
        "WeaponDescriptor": {
            "Salves": 12,
        },
    },

    ("FM_M16", "small_arms", None, False): {  # 299
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_M16_noreflex", "small_arms", "FM_M16", True): {  # 299
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },
    
    ("FM_L85A1", "small_arms", None, False): {  # 297
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },
    
    ("FM_L85A1_noreflex", "small_arms", "FM_L85A1", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },
    
    ("FM_L1A1_SLR", "small_arms", None, False): {  # 296
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 3.0,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 8,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 6.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_G3KA4", "small_arms", None, False): {  # 296
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 3.0,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 8,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 6.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_AK_74", "small_arms", None, False): {  # 287
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_AK_74_noreflex", "small_arms", "FM_AK_74", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_AKS_74", "small_arms", None, False): {  # 286
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_AKS_74_noreflex", "small_arms", "FM_AKS_74", True): {  # 286
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },

    ("FM_FNC", "small_arms", None, False): {  # 299
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "MaximumRangeGRU": 875,
                "MaximumRangeHelicopterGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "AimingTime": 1.0,
                "TimeBetweenTwoSalvos": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "SupplyCost": 1.0,
        "NbWeapons": [9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },
}

# fmt: on
