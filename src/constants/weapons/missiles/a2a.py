"""a2a missile definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
missiles: Dict[WeaponKey, WeaponData] = {
    ("AA_Skyflash", "A2A", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "TempsEntreDeuxFx": 1.5,
                "PorteeMaximaleHAGRU": 8400,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TempsEntreDeuxSalves": 1.5,
                "SupplyCost": 50,
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
                "SupplyCost": 40,
            },
        },
    },

    ("AA_R60M_Vympel", "A2A", None, False): { # 27
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 30,
            },
        },
    },

    ("AA_R40TD1", "A2A", None, False): { # 24
        "Ammunition": {
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "TempsEntreDeuxFx": 1.5,
                "PorteeMaximaleHAGRU": 8400,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TempsEntreDeuxSalves": 1.5,
                "SupplyCost": 60,
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
                "PorteeMaximaleHAGRU": 13300,
                "MaximalSpeedGRU": 6600,
                "TempsEntreDeuxTirs": 1.0,
                "TempsEntreDeuxSalves": 4.0,
                "NbTirParSalves": 2,
                # "SupplyCost": 140,
                "SupplyCost": 100,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 6600,
        },
    },

    ("AA_R33_Vympel", "A2A", None, False): { # 19
        "Ammunition": {
            "hit_roll": {
                "Idling": 30,
                "Moving": 30,
            },
            "parent_membr": {
                "add": [34, "IsFireAndForget = True"],
                "TraitsToken": ['MOTION', 'F&F'],
                "PorteeMaximaleHAGRU": 13300,
                "PhysicalDamages": 10.0,
                "MaximalSpeedGRU": 6600,
                "TempsEntreDeuxTirs": 0.7,
                "TempsDeVisee": 1.4,
                "TempsEntreDeuxSalves": 3.0,
                "NbTirParSalves": 2,
                # "SupplyCost": 140,
                "SupplyCost": 100,
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
                "TempsEntreDeuxTirs": 1.5,
                "TempsEntreDeuxFx": 1.5,
                "PorteeMaximaleHAGRU": 9275,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TempsEntreDeuxSalves": 1.5,
                "SupplyCost": 50,
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
                "TempsEntreDeuxTirs": 1.5,
                "TempsEntreDeuxFx": 1.5,
                "PorteeMaximaleHAGRU": 8400,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TempsEntreDeuxSalves": 1.5,
                "SupplyCost": 50,
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
                "TempsEntreDeuxTirs": 1.5,
                "TempsEntreDeuxFx": 1.5,
                "PorteeMaximaleHAGRU": 8400,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TempsEntreDeuxSalves": 1.5,
                "SupplyCost": 50,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_AIM9M_Sidewinder", "A2A", None, False): { # 7
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 40,
            },
        },
    },

    ("AA_AIM9L_Sidewinder", "A2A", None, False): { # 6
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 30,
            },
        },
    },

    ("AA_AIM9J_Sidewinder", "A2A", None, False): { # 5
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 25,
            },
        },
    },

    ("AA_AIM7M_Sparrow", "A2A", None, False): { # 4
        "Ammunition": {
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "TempsEntreDeuxFx": 1.5,
                "PorteeMaximaleHAGRU": 8400,
                "MaximalSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TempsEntreDeuxSalves": 1.5,
                "SupplyCost": 50,
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
                "TempsEntreDeuxTirs": 1.5,
                "TempsEntreDeuxFx": 1.5,
                "PorteeMaximaleHAGRU": 8400,
                "TempsEntreDeuxSalves": 1.5,
                "SupplyCost": 60,
            },
        },
    },
    
    ("AA_Matra_R530", "A2A", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "TempsEntreDeuxFx": 1.5,
                "PorteeMaximaleHAGRU": 6300,
                "TempsEntreDeuxSalves": 1.5,
                "SupplyCost": 40,
            },
        },
    },
    
    ("AA_Matra_Super_530F", "A2A", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "TempsEntreDeuxFx": 1.5,
                "PorteeMaximaleHAGRU": 6825,
                "TempsEntreDeuxSalves": 1.5,
                "SupplyCost": 50,
            },
        },
    },
    
    ("AA_Matra_Super_530D", "A2A", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.5,
                "TempsEntreDeuxFx": 1.5,
                "PorteeMaximaleHAGRU": 7700,
                "TempsEntreDeuxSalves": 1.5,
                "SupplyCost": 50,
            },
        },
    },
}
# fmt: on
