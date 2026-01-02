"""a2a missile definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
missiles: Dict[WeaponKey, WeaponData] = {
    ("AA_Skyflash", "A2A", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 50.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_R73_Vympel", "A2A", None, False): { # 27
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_R60M_Vympel", "A2A", None, False): { # 27
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 30.0,
            },
        },
    },

    ("AA_R40TD1", "A2A", None, False): { # 24
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 60.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_R37_Vympel", "A2A", None, False): { # 21
        "Ammunition": {
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 13300,
                "MaximalSpeedGRU": 6600,
                "TimeBetweenTwoShots": 0.7,
                "TimeBetweenTwoSalvos": 3.2,
                "AimingTime": 1.6,
                "NbTirParSalves": 2,
                "SupplyCost": 160.0,
                "AffichageMunitionParSalve": 2,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 6600,
        },
    },

    ("AA_R33_Vympel", "A2A", None, False): { # 19
        "Ammunition": {
            "hit_roll": {
                "Idling": 40,
                "Moving": 40,
            },
            "parent_membr": {
                "add": [34, "IsFireAndForget = True"],
                "TraitsToken": ['MOTION', 'F&F'],
                "MaximumRangeAirplaneGRU": 13300,
                "PhysicalDamages": 9.0,
                "TirReflexe": True,
                "ReflexShotDisabledIfPriorityTarget": True,
                "MaximalSpeedGRU": 6600,
                "TimeBetweenTwoShots": 0.7,
                "AimingTime": 1.6,
                "TimeBetweenTwoSalvos": 1.5,
                "NbTirParSalves": 2,
                "SupplyCost": 160.0,
                "AffichageMunitionParSalve": 2,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 6600,
        },
    },

    ("AA_R27R_Vympel", "A2A", None, False): { # 18
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 9275,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 50.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_R24R_Vympel", "A2A", None, False): { # 15
        "Ammunition": {
            "hit_roll": {
                "Moving": 40,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 50.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_R24MR_Vympel", "A2A", None, False): { # 15
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 50.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },
    
    ("AA_R23R_Vympel", "A2A", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 6825,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 50.0,
            },
        },
    },
    
    ("AA_R13M", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Moving": 40,
            },
            "parent_membr": {
                "PhysicalDamages": 4.0,
                "SupplyCost": 25.0,
            },
        },
    },

    ("AA_AIM9M_Sidewinder", "A2A", None, False): { # 7
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_AIM9L_Sidewinder", "A2A", None, False): { # 6
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 30.0,
            },
        },
    },

    ("AA_AIM9J_Sidewinder", "A2A", None, False): { # 5
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 25.0,
            },
        },
    },

    ("AA_AIM7M_Sparrow", "A2A", None, False): { # 4
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 50.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_AIM120A_AMRAAM", "A2A", None, False): { # 1
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 60.0,
            },
        },
    },
    
    ("AA_Matra_R530", "A2A", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 6300,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 40.0,
            },
        },
    },
    
    ("AA_Matra_Super_530F", "A2A", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 6825,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 50.0,
            },
        },
    },
    
    ("AA_Matra_Super_530D", "A2A", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 7700,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 50.0,
            },
        },
    },
}
# fmt: on
