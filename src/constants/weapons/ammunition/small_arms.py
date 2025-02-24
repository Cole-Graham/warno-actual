"""Small arms weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Sniper_SVD_Dragunov", "small_arms", None, False): {  #735
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sniper",
            },
            "hit_roll": {
                "BaseCriticModifier": 0,
                "Idling": 65,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 6.0,
                "TempsEntreDeuxFx": 6.0,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "PorteeMaximaleGRU": 1050,
                "PorteeMaximaleTBAGRU": 875,
                "DisplaySalveAccuracy": False,
                "TempsEntreDeuxSalves": 6.0,
                "TempsDeVisee": 6.0,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 10
            },
        },
        "BaseSupplyCost": 2,
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
                "Idling": 65,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 6.0,
                "TempsEntreDeuxFx": 6.0,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "PorteeMaximaleGRU": 1050,
                "PorteeMaximaleTBAGRU": 875,
                "DisplaySalveAccuracy": False,
                "TempsEntreDeuxSalves": 6.0,
                "TempsDeVisee": 6.0,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 10
            },
        },
        "BaseSupplyCost": 2,
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
                "Idling": 75,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 7.5,
                "TempsEntreDeuxFx": 7.5,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 6.0,
                "TempsEntreDeuxSalves": 7.5,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 5,
            },
        },
        "BaseSupplyCost": 1,
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
                "Idling": 65,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 6.0,
                "TempsEntreDeuxFx": 6.0,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "PorteeMaximaleGRU": 1050,
                "PorteeMaximaleTBAGRU": 875,
                "DisplaySalveAccuracy": False,
                "TempsEntreDeuxSalves": 6.0,
                "TempsDeVisee": 6.0,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 10
            },
        },
        "BaseSupplyCost": 2,
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
                "Idling": 75,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 7.5,
                "TempsEntreDeuxFx": 7.5,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "DisplaySalveAccuracy": False,
                "TempsEntreDeuxSalves": 7.5,
                "TempsDeVisee": 6.0,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 5,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 12,
        },
    },

    ("SAW_lMG_K_7_62mm", "small_arms", None, False): {  #720
        # todo: rename this, its 5.45mm... stupid eugen
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 30,
                "Moving": 15,
            },
            "parent_membr": {
                "Caliber": ("existing", "XUTVWWNOTF"),
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 15,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 5.0,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 75
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 10,
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
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 15,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 5.0,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 45
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 10,
        },
    },
    
    ("SAW_RPK_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 35,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 15,
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
                "TempsEntreDeuxFx": 4.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 15,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.5,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 45,
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
                "TempsEntreDeuxFx": 4.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 15,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.5,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 45,
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
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 15,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 5.0,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 45
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 10,
        },
    },
    
    ("SAW_Bren_L4A4", "small_arms", None, False): {  # 712
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 10,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.5,
                "TempsEntreDeuxSalves": 1.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 25,
        },
    },
    
    ("PM_Sterling", "small_arms", None, False): {  # 572
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_intermediate",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.5,
                "PorteeMaximaleGRU": 450,
                "PorteeMaximaleTBAGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 7,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
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
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.5,
                "PorteeMaximaleGRU": 450,
                "PorteeMaximaleTBAGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 7,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
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
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.5,
                "PorteeMaximaleGRU": 450,
                "PorteeMaximaleTBAGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 7,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
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
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.5,
                "PorteeMaximaleGRU": 450,
                "PorteeMaximaleTBAGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 7,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
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
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.5,
                "PorteeMaximaleGRU": 450,
                "PorteeMaximaleTBAGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 7,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [10, 9, 6, 4, 3, 1],
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
                "Idling": 50,
                "Moving": 40,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.5,
                "PorteeMaximaleGRU": 450,
                "PorteeMaximaleTBAGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 7,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
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
                "TempsEntreDeuxTirs": 1.0,
                "PorteeMaximaleGRU": 525,
                "PorteeMaximaleTBAGRU": 450,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [5],
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
                "TempsEntreDeuxTirs": 1.0,
                "PorteeMaximaleGRU": 525,
                "PorteeMaximaleTBAGRU": 450,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
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
                "TempsEntreDeuxTirs": 1.0,
                "PorteeMaximaleGRU": 700,
                "PorteeMaximaleTBAGRU": 625,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
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
                "TempsEntreDeuxTirs": 1.0,
                "PorteeMaximaleGRU": 700,
                "PorteeMaximaleTBAGRU": 625,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
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
                "TempsEntreDeuxTirs": 1.0,
                "PorteeMaximaleGRU": 525,
                "PorteeMaximaleTBAGRU": 450,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [6],
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
                "TempsEntreDeuxTirs": 1.0,
                "PorteeMaximaleGRU": 450,
                "PorteeMaximaleTBAGRU": 400,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 7,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
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
                "TempsEntreDeuxTirs": 1.0,
                "PorteeMaximaleGRU": 525,
                "PorteeMaximaleTBAGRU": 450,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 0.5,
                "TempsEntreDeuxSalves": 3.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [10, 8, 6, 5, 4],
        "WeaponDescriptor": {
            "Salves": 11,               
        },
    },
    
    ("MMG_turret_7_62mm_M60", "small_arms", "MMG_team_7_62mm_M60", True): {
        "Ammunition": {
            "display": "M60E3",
            "hit_roll": {
                "Idling": 40,
                "Moving": 15,
            },
            "token": "EILUZEIFXS",
            "parent_membr": {
                "TraitsToken": ['MOTION', 'tripod'],
                "TempsEntreDeuxTirs": 1.30, # was 1.25 but Eugen said it has to be multiple of game tick rate (10hz)
                "TempsEntreDeuxFx": 6.0,
                "PorteeMaximaleGRU": 1050,
                "add": [16, "PorteeMaximaleTBAGRU = 875"],
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.5,
                "TempsEntreDeuxSalves": 1.3,
                "NbTirParSalves": 4,
                "CanShootWhileMoving": "True",
                "AffichageMunitionParSalve": 20,
            },
        },
        "NbWeapons": [1],
        "BaseSupplyCost": 1,
        "WeaponDescriptor": {
            "Salves": 45,
        },
    },
    
    ("MMG_inf_L7A2_7_62mm", "small_arms", None, False): {  # 485
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 35,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.0,
                "TempsEntreDeuxFx": 4.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 30,
        },
    },
    
    ("MMG_inf_MAG_7_62mm", "small_arms", None, False): {  # 485
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 35,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.0,
                "TempsEntreDeuxFx": 4.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 30,
        },
    },

    ("MMG_inf_M240B_7_62mm", "small_arms", None, False): {  # 484
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 35,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.0,
                "TempsEntreDeuxFx": 4.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 30,
        },
    },

    ("MMG_PKT_7_62mm_x2", "small_arms", None, False): {  # 476
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1050,
                "PorteeMaximaleTBAGRU": 875,
                "PhysicalDamages": 0.14,
                "SuppressDamages": 42.0,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 0.5,
                "NbTirParSalves": 7,
                "SupplyCost": 2,
                "CanShootWhileMoving": "True",
                "AffichageMunitionParSalve": 20,
            },
        },
        "WeaponDescriptor": {
            "Salves": 260,
        },
    },

    ("MMG_PKT_7_62mm", "small_arms", None, False): {  # 475
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1050,
                "PorteeMaximaleTBAGRU": 875,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 0.5,
                "NbTirParSalves": 7,
                "SupplyCost": 1,
                "CanShootWhileMoving": "True",
                "AffichageMunitionParSalve": 10,
            },
        },
        "WeaponDescriptor": {
            "Salves": 260,
        },
    },

    ("MMG_PKM_7_62mm", "small_arms", None, False): {  # 474
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 35,
                "Moving": 20,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.30, # was 1.25 but Eugen said it has to be multiple of game tick rate (10hz)
                "TempsEntreDeuxFx": 6.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.5,
                "TempsEntreDeuxSalves": 1.3,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 30,
        },
    },

    ("MMG_inf__MG3_7_62mm", "small_arms", None, False): {  # unchanged from L7A2 - needs change
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 35,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.0,
                "TempsEntreDeuxFx": 4.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 30,
        },
    },

    ("MMG_WA_M60E3_7_62mm", "small_arms", None, False): {  # 469
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "display": "M60E3",
            "hit_roll": {
                "Idling": 35,
                "Moving": 15,
            },
            "token": "IYUAMGSZZJ", 
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.30, # was 1.25 but Eugen said it has to be multiple of game tick rate (10hz)
                "TempsEntreDeuxFx": 6.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.5,
                "TempsEntreDeuxSalves": 1.3,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 30,
        },
    },
    
    ("MMG_team_7_62mm_M60", "small_arms", None, False): { # 469
        "Ammunition": {
            "display": "M60E3",
            "token": "IYUAMGSZZJ", 
        },
    },

    ("MMG_M60E1_7_62mm", "small_arms", "MMG_WA_M60E3_7_62mm", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "display": "M60E1",
            "hit_roll": {
                "Idling": 35,
                "Moving": 10,
            },
            "token": "GVHHKBBTHW",
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "TempsEntreDeuxFx": 6.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.5,
                "TempsEntreDeuxSalves": 1.5,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [2, 1],
        "WeaponDescriptor": {
            "Salves": 30,
        },
    },
    
    ("MMG_M240_7_62mm", "small_arms", None, False): {  # 466
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 25,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.0,
                "TempsEntreDeuxFx": 4.0,
                "PorteeMaximaleGRU": 1050,
                "PorteeMaximaleTBAGRU": 875,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 45,
        },
    },
    
    ("MMG_M1919", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 25,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.0,
                "TempsEntreDeuxFx": 4.0,
                "PorteeMaximaleGRU": 1050,
                "PorteeMaximaleTBAGRU": 875,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 45,
        },
    },
    
    ("MMG_L94A1_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 25,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.0,
                "TempsEntreDeuxFx": 4.0,
                "PorteeMaximaleGRU": 1050,
                "PorteeMaximaleTBAGRU": 875,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 45,
        },
    },
    
    ("MMG_L8A2_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 25,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.0,
                "TempsEntreDeuxFx": 4.0,
                "PorteeMaximaleGRU": 1050,
                "PorteeMaximaleTBAGRU": 875,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 45,
        },
    },
    
    ("MMG_L37A2_7_62mm", "small_arms", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 25,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.0,
                "TempsEntreDeuxFx": 4.0,
                "PorteeMaximaleGRU": 1050,
                "PorteeMaximaleTBAGRU": 875,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 21,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 1.0,
                "NbTirParSalves": 4,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 45,
        },
    },
    
    ("Lance_grenade_Mk19_40mm", "AGL", None, False): {  # 451
        "Ammunition": {
            "hit_roll": {
                "Idling": 25,
                "Moving": 15,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 0.2,
                "PorteeMaximaleGRU": 1575,
                "DispersionAtMaxRangeGRU": 70,
                "RadiusSplashPhysicalDamagesGRU": 30,
                "PhysicalDamages": 0.25,
                "RadiusSplashSuppressDamagesGRU": 56,
                "SuppressDamages": 15.0,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.5,
                "TempsEntreDeuxSalves": 4.0,
                "NbTirParSalves": 8,
                "SupplyCost": 5,
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
                "TempsEntreDeuxTirs": 0.2,
                "PorteeMaximaleGRU": 1225,
                "DispersionAtMaxRangeGRU": 60,
                "RadiusSplashPhysicalDamagesGRU": 22,
                "PhysicalDamages": 0.25,
                "RadiusSplashSuppressDamagesGRU": 42,
                "SuppressDamages": 10.0,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.5,
                "TempsEntreDeuxSalves": 4.0,
                "NbTirParSalves": 10,
                "SupplyCost": 5,
                "AffichageMunitionParSalve": 10,
            },
        },
        "WeaponDescriptor": {
            "Salves": 30,
        },
    },
    
    ("HMG_team_12_7_mm_NSV_6U6", "small_arms", None, False): {  # 356
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleTBAGRU": 1225,
            },
        },
    },

    ("HMG_14_5_mm_KPVT", "small_arms", None, False): {  # 353
        "Ammunition": {
            "hit_roll": {
                "Idling": 35,
            },
            "parent_membr": {
                "PhysicalDamages": 0.14,
                "SuppressDamages": 42,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 2.0,
                "TempsEntreDeuxSalves": 1.0,
                "SupplyCost": 1,
                "AffichageMunitionParSalve": 7,
            },
        },
        "WeaponDescriptor": { 
            "Salves": 185,
        },
    },

    # FM_kbk_AKM is now deprecated
    
    ("FM_kbk_AK", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 15,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 2.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 5.5,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 15,
            },
            "token": "AYYOIYKCVF",
        },
        "Texture": "FM_kbk_AKM",
        "BaseSupplyCost": 1,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 22,
        },
    },
    
    ("FM_kbk_AK_noreflex", "small_arms", "FM_kbk_AK", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 15,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 5.5,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 15,
            },
            "token": "AYYOIYKCVF",
        },
        "Texture": "FM_kbk_AKM",
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 22,
        },
    },

    ("FM_kbk_AKMS", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 15,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 2.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 5.5,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 15,
            },
            # "token": "AYYOIYKCVF",
        },
        # "NewTexture": "kbk_akm",
        "BaseSupplyCost": 1,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 22,
        },
    },

    ("FM_kbk_AKMS_noreflex", "small_arms", "FM_kbk_AKMS", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 45,
                "Moving": 15,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.06,
                "SuppressDamages": 6,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 5.5,
                "NbTirParSalves": 5,
                "AffichageMunitionParSalve": 15,
            },
            "token": "AYYOIYKCVF",
        },
        "Texture": "FM_kbk_AKM",
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 22,
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
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
                "Idling": 40,
                "Moving": 20,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 6,
                "AffichageMunitionParSalve": 20,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [10, 9, 8, 7, 5, 4, 3, 1],
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [2],
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
                "Idling": 50,
                "Moving": 20,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 2.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 7,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 6.0,
                "NbTirParSalves": 3,
                "AffichageMunitionParSalve": 10,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 22,
        },
    },

    ("FM_G3KA4", "small_arms", None, False): {  # 296
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sa_full",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 20,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 2.0,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.07,
                "SuppressDamages": 7,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 6.0,
                "NbTirParSalves": 3,
                "AffichageMunitionParSalve": 10,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        "WeaponDescriptor": {
            "Salves": 22,
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
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
                "TempsEntreDeuxTirs": 1.5,
                "PorteeMaximaleGRU": 875,
                "PorteeMaximaleTBAGRU": 700,
                "PhysicalDamages": 0.05,
                "SuppressDamages": 5,
                "DisplaySalveAccuracy": False,
                "TirReflexe": False,
                "TempsDeVisee": 1.0,
                "TempsEntreDeuxSalves": 4.5,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 30,
            },
        },
        "BaseSupplyCost": 1,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 11,
        },
    },
}

# fmt: on
