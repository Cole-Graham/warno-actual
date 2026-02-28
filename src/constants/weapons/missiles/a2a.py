"""a2a missile definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
missiles: Dict[WeaponKey, WeaponData] = {
    ("AA_Skyflash", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "SpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "AimingTime": 0.3,
                "TimeBetweenTwoSalvos": 1.5,
                "SupplyCost": 50.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_R73_Vympel", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 70,
                "Moving": 70,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_R60M_Vympel", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 30.0,
            },
        },
    },
    
    ("AA_R60M_Vympel_Helo", "A2A", "AA_R60M_Vympel", True): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "AimingTime": 0.3,
                "SupplyCost": 30.0,
            },
        },
    },

    ("AA_R40TD1", "A2A", None, False): { # 24
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "SpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.5,
                "AimingTime": 0.3,
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
            "hit_roll": {
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 13300,
                "SpeedGRU": 6600,
                "TimeBetweenTwoShots": 0.7,
                "TimeBetweenTwoSalvos": 3.2,
                "AimingTime": 1.6,
                "ShotsCountPerSalvo": 2,
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
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "add": [34, "IsFireAndForget = True"],
                "TraitsToken": ['MOTION', 'F&F'],
                "MaximumRangeAirplaneGRU": 13300,
                "PhysicalDamages": 9.0,
                "TirReflexe": True,
                "ReflexShotDisabledIfPriorityTarget": True,
                "SpeedGRU": 6600,
                "TimeBetweenTwoShots": 0.7,
                "AimingTime": 1.6,
                "TimeBetweenTwoSalvos": 1.5,
                "ShotsCountPerSalvo": 2,
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
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 9275,
                "SpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.5,
                "AimingTime": 0.3,
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
                "Idling": 45,
                "Moving": 45,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "SpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.5,
                "AimingTime": 0.3,
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
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "SpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.5,
                "AimingTime": 0.3,
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
            "hit_roll": {
                "Idling": 45,
                "Moving": 45,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 6825,
                "TimeBetweenTwoSalvos": 1.5,
                "AimingTime": 0.3,
                "SupplyCost": 50.0,
            },
        },
    },
    
    ("AA_R13M", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "PhysicalDamages": 4.0,
                "AimingTime": 0.3,
                "SupplyCost": 25.0,
            },
        },
    },
    
    ("AA_R3R", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "AimingTime": 0.3,
            },
        },
    },

    ("AA_AIM9M_Sidewinder", "A2A", None, False): { # 7
        "Ammunition": {
            "hit_roll": {
                "Idling": 70,
                "Moving": 70,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_AIM9L_Sidewinder", "A2A", None, False): { # 6
        "Ammunition": {
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 30.0,
            },
        },
    },

    ("AA_AIM9J_Sidewinder", "A2A", None, False): { # 5
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 25.0,
            },
        },
    },
    
    ("AA_AIM7F_Sparrow", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 7700,
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "TimeBetweenTwoSalvos": 1.5,
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_AIM7M_Sparrow", "A2A", None, False): { # 4
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "SpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.5,
                "AimingTime": 0.3,
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
            "hit_roll": {
                "Idling": 70,
                "Moving": 70,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 8400,
                "TimeBetweenTwoSalvos": 1.5,
                "AimingTime": 0.3,
                "SupplyCost": 60.0,
            },
        },
    },
    
    ("AA_Matra_R530", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 45,
                "Moving": 45,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 6300,
                "TimeBetweenTwoSalvos": 1.5,
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },
    
    ("AA_Matra_Super_530F", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 6825,
                "TimeBetweenTwoSalvos": 1.5,
                "AimingTime": 0.3,
                "SupplyCost": 50.0,
            },
        },
    },
    
    ("AA_Matra_Super_530D", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.5,
                "TimeBetweenTwoFx": 1.5,
                "MaximumRangeAirplaneGRU": 7700,
                "TimeBetweenTwoSalvos": 1.5,
                "AimingTime": 0.3,
                "SupplyCost": 50.0,
            },
        },
    },
    
    ("AA_R550_Magic_II", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
                "DistanceToTarget": False,
            },
            "parent_membr": {
                "AimingTime": 0.3,
            },
        },
    },
}
# fmt: on
