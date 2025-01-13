"""SEAD missile definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
missiles: Dict[WeaponKey, WeaponData] = {
    ("AGM_Kh28", "AntiRadiation", None, False): { # renamed from AGM_Kh28_X28
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 5600,
                "MaximalSpeedGRU": 4240,
                "MaxAccelerationGRU": 2474,
                "SupplyCost": 120,
                "TempsEntreDeuxSalves": 2.35,
            },
        },
        "BaseSupplyCost": 120,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4240,
            "MaxAccelerationGRU": 2474,
        },
    },
    
    ("AGM_Kh58U", "AntiRadiation", None, False): { # 87
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 6475,
                "MaximalSpeedGRU": 4947,
                "MaxAccelerationGRU": 2827,
                "TempsEntreDeuxSalves": 2.45,
                "SupplyCost": 150,
            },
        },
        "BaseSupplyCost": 150,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4947,
            "MaxAccelerationGRU": 2827,
        },
    },
    
    ("AGM_AS37_Martel", "AntiRadiation", None, False): { # 64
        "Ammunition": {
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 5425,
                "MaximalSpeedGRU": 3534,
                "MaxAccelerationGRU": 2297,
                "TempsEntreDeuxSalves": 2.3,
            },
        },
        "BaseSupplyCost": 130,
        "WeaponDescriptor": {
            "SalvoLengths": [2, 1],
            "units": {
                2: ["Buccaneer_S2B_SEAD_UK"],
                1: ["Jaguar_SEAD_FR", "Mirage_III_SEAD_FR"],
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 3534,
            "MaxAccelerationGRU": 2297,
        },
    },

    ("AGM_ARMAT", "AntiRadiation", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 5950,
                "MaximalSpeedGRU": 3180,
                "MaxAccelerationGRU": 1767,
                "TempsEntreDeuxSalves": 2.5,
            },
        },
        "BaseSupplyCost": 130,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 3180,
            "MaxAccelerationGRU": 1767,
        },
    },

    ("AGM_ALARM", "AntiRadiation", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 75,
                "Moving": 75,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 5775,
                "MaximalSpeedGRU": 3534,
                "MaxAccelerationGRU": 2120,
                "TempsEntreDeuxSalves": 2.45,
            },
        },
        "BaseSupplyCost": 140,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 3534,
            "MaxAccelerationGRU": 2120,
        },
    },
    
    ("AGM_AGM88_HARM", "AntiRadiation", None, False): { # 58
        "Ammunition": {
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "PorteeMaximaleGRU": 6126,
                "MaximalSpeedGRU": 4947,
                "MaxAccelerationGRU": 2827,
                "TempsEntreDeuxSalves": 2.3,
                "SupplyCost": 150
            },
        },
        "BaseSupplyCost": 150,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4947,
            "MaxAccelerationGRU": 2827,
        },
    },

    ("AGM_AGM45_Shrike", "AntiRadiation", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PorteeMaximaleGRU": 5250,
                "MaximalSpeedGRU": 3534,
                "MaxAccelerationGRU": 2120,
                "TempsEntreDeuxSalves": 2.35,
                "SupplyCost": 120,
            },
        },
        "BaseSupplyCost": 120,
        "WeaponDescriptor": {
            "SalvoLengths": [1],
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 3534,
            "MaxAccelerationGRU": 2297,
        },
    },
}
# fmt: on
