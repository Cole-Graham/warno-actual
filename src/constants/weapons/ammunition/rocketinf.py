"""AT, RCL, Napalm launcher, etc."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("RocketInf_WOMBAT_RCL_120mm_TOWED", "recoilless", None, False): { # 707
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1750,
                "DisplaySalveAccuracy": False,
            },
        },
    },
    
    ("RocketInf_WOMBAT_RCL_120mm_HE_TOWED", "recoilless", None, False): { # 706
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1750,
                "PhysicalDamages": 1.5,
                "DisplaySalveAccuracy": False,
            },
        },
    },
    
    ("RocketInf_WOMBAT_RCL_120mm_HE", "recoilless", None, False): { # 705
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1750,
                "PhysicalDamages": 1.5,
                "DisplaySalveAccuracy": False,
            },
        },
    },
    
    ("RocketInf_WOMBAT_RCL_120mm", "recoilless", None, False): { # 704
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1750,
                "DisplaySalveAccuracy": False,
            },
        },
    },
    
    ("RocketInf_RPO_RYS", "napalm", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 525,
                "DisplaySalveAccuracy": False,
                "PhysicalDamages": 1.3,
            },
        },
    },

    ("RocketInf_RPO_A_93mm", "napalm", None, False): { # 702
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_thermobarique",
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'thermobaric'],
                "ImpactHappening": ['BombeODAB'],
                "PorteeMaximaleGRU": 700,
                "RadiusSplashPhysicalDamagesGRU": 93,
                "PhysicalDamages": 2.0,
                "RadiusSplashSuppressDamagesGRU": 124,
                "SuppressDamages": 216,
                "DisplaySalveAccuracy": False,
                "TimeBetweenTwoSalvos": 5.0,
            },
        },
    },

    ("RocketInf_RPG7VR_64mm", "medium_at", None, False): { # 698
        "Ammunition": {
            "Arme": {
                "Index": 22,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 525,
                "DisplaySalveAccuracy": False,
            },
        },
    },

    ("RocketInf_RPG7VL", "medium_at", None, False): { # 697
        "Ammunition": {
            "Arme": {
                "Index": 19,
            },
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 700,
                "DisplaySalveAccuracy": False,
            },
        },
    },
    
    ("RocketInf_RPG76_Komar", "light_at", None, False): { # 697
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleGRU": 450,
                "DisplaySalveAccuracy": False,
                "TimeBetweenTwoSalvos": 3.0,
            },
        },
    },

    ("RocketInf_RPG7", "medium_at", None, False): { # 694 (RPG-7VM)
        "Ammunition": {
            "Arme": {
                "Index": 15,
            },
            "hit_roll": {
                "Idling": 60,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 875,
                "DisplaySalveAccuracy": False,
            },
        },
    },

    ("RocketInf_RPG29_105mm", "heavy_at", None, False): { # 690
        "Ammunition": {
            "Arme": {
                "Index": 22,
            },
            "hit_roll": {
                "Idling": 60,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 875,
                "DisplaySalveAccuracy": False,
            },
        },
    },

    ("RocketInf_RPG27_105mm", "medium_at", None, False): { # 689
        "Ammunition": {
            "Arme": {
                "Index": 22,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 450,
                "DisplaySalveAccuracy": False,
            },
        },
    },

    ("RocketInf_RPG26_72_5mm", "light_at", None, False): { # 688
        "Ammunition": {
            "Arme": {
                "Index": 18,
            },
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 525,
                "DisplaySalveAccuracy": False,
            },
        },
    },

    ("RocketInf_RPG22_72_5mm", "light_at", None, False): { # 687
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 450,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },

    ("RocketInf_RPG18_64mm", "light_at", None, False): { # 685
        "Ammunition": {
            "Arme": {
                "Index": 15,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 450,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },
    
    ("RocketInf_RPG16", "light_at", None, False): { # 684
        "Ammunition": {
            "parent_membr": {
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },
    
    ("RocketInf_LRAC_73", "medium_at", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 15,
            },
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 525,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },
    
    ("RocketInf_LRAC_F1", "medium_at", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 17,
            },
            "hit_roll": {
                "Idling": 60,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 875,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 15,
            },
        },
    },
    
    ("RocketInf_APILAS", "heavy_at", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 875,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 20,
            },
        },
    },

    ("RocketInf_M72A1_LAW_66mm", "light_at", None, False): { # 681
        "Ammunition": {
            "Arme": {
                "Index": 12,
            },
            "hit_roll": {
                "Idling": 45,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 525,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },

    ("RocketInf_M72A3_LAW_66mm", "light_at", None, False): { # 680
        "Ammunition": {
            "Arme": {
                "Index": 14,
            },
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 525,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },

    ("RocketInf_M67_RCL_90mm_HE", "recoilless", None, False): { # 679
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "TimeBetweenTwoFx": 6.6,
                "PorteeMaximaleGRU": 875,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },

    ("RocketInf_M67_RCL_90mm", "recoilless", None, False): { # 678
        "Ammunition": {
            "Arme": {
                "Index": 14,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "TimeBetweenTwoFx": 6.6,
                "PorteeMaximaleGRU": 875,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },

    ("RocketInf_M40A1_RCL_106mm_TOWED", "recoilless", None, False): { # 677
        "Ammunition": {
            "Arme": {
                "Index": 16,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1750,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },

    ("RocketInf_M40A1_RCL_106mm_HE_TOWED", "recoilless", None, False): { # 676
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1750,
                "PhysicalDamages": 1.25,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },

    ("RocketInf_M40A1_RCL_106mm_HE", "recoilless", None, False): { # 675
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1750,
                "PhysicalDamages": 1.25,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },

    ("RocketInf_M40A1_RCL_106mm", "recoilless", None, False): { # 674
        "Ammunition": {
            "Arme": {
                "Index": 16,
            },
            "hit_roll": {
                "Idling": 40,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 1750,
                "DisplaySalveAccuracy": False,
                "SupplyCost": 10,
            },
        },
    },

    ("RocketInf_M202_Flash_66mm", "napalm", None, False): { # 673
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 450,
                "PhysicalDamages": 0.8,
                "DisplaySalveAccuracy": False,
                "FireDescriptor": "$/GFX/Weapon/Descriptor_Fire_NapalmLeger_53m",
            },
        },
    },
    
    ("RocketInf_LAW_80", "medium_at", None, False): { # 669
        "Ammunition": {
            "Arme": {
                "Index": 21,
            },
            "hit_roll": {
                "Idling": 60,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 875,
            },
        },
    },
    
    ("RocketInf_Carl_Gustav", "medium_at", None, False): { # 667
        "Ammunition": {
            "Arme": {
                "Index": 18,
            },
            "hit_roll": {
                "Idling": 65,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 875,
            },
        },
    },
    
    ("RocketInf_Carl_Gustav", "medium_at", None, False): { # 667
        "Ammunition": {
            "Arme": {
                "Index": 18,
            },
            "hit_roll": {
                "Idling": 65,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 875,
            },
        },
    },

    ("RocketInf_AT4_83mm", "medium_at", None, False): { # 661
        "Ammunition": {
            "Arme": {
                "Index": 18,
            },
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 700,
            },
        },
    },
    
    ("RocketInf_PzF_44", "medium_at", None, False): {
        "Ammunition": {
            "Arme": {
                "Index": 16,
            },
            "hit_roll": {
                "Idling": 50,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 700,
            },
        },
    },
}
# fmt: on
