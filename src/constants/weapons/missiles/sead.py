"""Missile edits"""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
missiles: Dict[WeaponKey, WeaponData] = {
    ("AGM_Kh25MP", "AntiRadiation", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 5250,
                "SpeedGRU": 3534,
                "MaxAccelerationGRU": 2120,
                "TimeBetweenTwoSalvos": 2.3,
                "SupplyCost": 120.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 3534,
            "MaxAccelerationGRU": 2297,
            "AutoGyr": 1.57079633
        },
    },
    
    ("AGM_Kh28", "AntiRadiation", None, False): { # renamed from AGM_Kh28_X28
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
            },
            "parent_membr": {
                "MaximumRangeGRU": 5600,
                "SpeedGRU": 4240,
                "MaxAccelerationGRU": 2474,
                "SupplyCost": 120.0,
                "TimeBetweenTwoSalvos": 2.3,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4240,
            "MaxAccelerationGRU": 2474,
            "AutoGyr": 1.57079633
        },
    },
    
    ("AGM_Kh58U", "AntiRadiation", None, False): { # 87
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
            },
            "parent_membr": {
                "MaximumRangeGRU": 6475,
                "SpeedGRU": 4947,
                "MaxAccelerationGRU": 2827,
                "TimeBetweenTwoSalvos": 2.4,
                "SupplyCost": 150.0,
            },
        },

        "MissileDescriptor": {
            "MaxSpeedGRU": 4947,
            "MaxAccelerationGRU": 2827,
            "AutoGyr": 1.57079633,
        },
    },
    
    ("AGM_AS37_Martel", "AntiRadiation", None, False): { # 64
        "Ammunition": {
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "MaximumRangeGRU": 5425,
                "SpeedGRU": 3534,
                "MaxAccelerationGRU": 2297,
                "TimeBetweenTwoSalvos": 2.3,
            },
        },
        "SupplyCost": 130.0,
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
            "AutoGyr": 1.57079633,
        },
    },

    ("AGM_ARMAT", "AntiRadiation", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "MaximumRangeGRU": 5950,
                "SpeedGRU": 3180,
                "MaxAccelerationGRU": 1767,
                "TimeBetweenTwoSalvos": 2.5,
                "SupplyCost": 130.0,
            },
        },

        "MissileDescriptor": {
            "MaxSpeedGRU": 3180,
            "MaxAccelerationGRU": 1767,
            "AutoGyr": 1.57079633,
        },
    },

    ("AGM_ALARM", "AntiRadiation", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 75,
                "Moving": 75,
            },
            "parent_membr": {
                "MaximumRangeGRU": 5775,
                "SpeedGRU": 3534,
                "MaxAccelerationGRU": 2120,
                "TimeBetweenTwoSalvos": 2.4,
                "SupplyCost": 140.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 3534,
            "MaxAccelerationGRU": 2120,
            "AutoGyr": 1.57079633,
        },
    },
    
    ("AGM_AGM88_HARM", "AntiRadiation", None, False): { # 58
        "Ammunition": {
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "MaximumRangeGRU": 6125,
                "SpeedGRU": 4947,
                "MaxAccelerationGRU": 2827,
                "TimeBetweenTwoSalvos": 2.3,
                "SupplyCost": 150.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4947,
            "MaxAccelerationGRU": 2827,
            "AutoGyr": 1.57079633,
        },
    },

    ("AGM_AGM45_Shrike", "AntiRadiation", None, False): {
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeGRU": 5250,
                "SpeedGRU": 3534,
                "MaxAccelerationGRU": 2120,
                "TimeBetweenTwoSalvos": 2.3,
                "SupplyCost": 120.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 3534,
            "MaxAccelerationGRU": 2297,
            "AutoGyr": 1.57079633
        },
    },
}
# fmt: on
