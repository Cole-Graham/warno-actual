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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 8400,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "AimingTime": 0.3,
                "TimeBetweenTwoSalvos": 1.4,
                "SupplyCost": 50.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_Skyflash_SuperTEMP", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 8400,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "AimingTime": 0.3,
                "TimeBetweenTwoSalvos": 1.4,
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
            "Arme": {
                "Family": "DamageFamily_a2a_tbagru",
            },
            "hit_roll": {
                "Idling": 70,
                "Moving": 70,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_R73_Vympel_HAGRU", "A2A", "AA_R73_Vympel", True): { # 27
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_hagru",
            },
            "hit_roll": {
                "Idling": 70,
                "Moving": 70,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },
    
    ("AA_R73_Vympel_NoOBS", "A2A", "AA_R73_Vympel", True): { # 27
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_tbagru",
            },
            "hit_roll": {
                "Idling": 70,
                "Moving": 70,
            },
            "parent_membr": {
                "TraitsToken": ['MOTION', 'F&F'],
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_R73_Vympel_NoOBS_HAGRU", "A2A", "AA_R73_Vympel", True): { # 27
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_hagru",
            },
            "hit_roll": {
                "Idling": 70,
                "Moving": 70,
            },
            "parent_membr": {
                "TraitsToken": ['MOTION', 'F&F'],
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_R60M_Vympel", "A2A", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_tbagru",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 30.0,
            },
        },
        "WeaponDescriptor": {
            "SalvoLengths": [2, 1],
        },
    },

    ("AA_R60M_Vympel_HAGRU", "A2A", "AA_R60M_Vympel", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_hagru",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 30.0,
            },
        },
        "WeaponDescriptor": {
            "SalvoLengths": [2, 1],
        },
    },
    
    ("AA_R60M_Vympel_helo", "A2A", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_tbagru",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "AimingTime": 0.3,
                "SupplyCost": 30.0,
            },
        },
        "MissileDescriptor": {
            "AutoGyr": 2.617994,
        },
    },
    
    ("AA_R60M_Vympel_helo_HAGRU", "A2A", "AA_R60M_Vympel_helo", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_hagru",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "AimingTime": 0.3,
                "SupplyCost": 30.0,
            },
        },
    },

    ("AA_R40RD1", "A2A", None, False): { # 24
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 8400,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.4,
                "AimingTime": 0.3,
                "SupplyCost": 60.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_R40TD1", "A2A", None, False): { # 24
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 8400,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.4,
                "AimingTime": 0.3,
                "SupplyCost": 60.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_R98MR", "A2A", None, False): { # 24
        "Ammunition": {
            "hit_roll": {
                "Idling": 55,
                "Moving": 55,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 6300,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.4,
                "AimingTime": 0.3,
                "SupplyCost": 60.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_R98MT", "A2A", None, False): { # 24
        "Ammunition": {
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 6300,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.4,
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
            "Arme": {
                "Family": "DamageFamily_missile_he_bigly",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
            },
            "parent_membr": {
                "TraitsToken": ['MOTION', 'F&F', 'biglyHE'],
                "MaximumRangeAirplaneGRU": 13300,
                "PhysicalDamages": 8.0,
                "SuppressDamages": 350, # 210 against vet 3 targets, will still stun in 1 hit
                "TirReflexe": True,
                "ReflexShotDisabledIfPriorityTarget": True,
                "ProjectileSpeedGRU": 6600,
                "TimeBetweenTwoShots": 0.7,
                "TimeBetweenTwoSalvos": 3.0,
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
            "Arme": {
                "Family": "DamageFamily_missile_he_bigly",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 40,
            },
            "parent_membr": {
                "add": [34, "IsFireAndForget = True"],
                "TraitsToken": ['MOTION', 'F&F', 'biglyHE'],
                "MaximumRangeAirplaneGRU": 13300,
                "PhysicalDamages": 8.0,
                "SuppressDamages": 350, # 210 against vet 3 targets, will still stun in 1 hit
                "TirReflexe": True,
                "ReflexShotDisabledIfPriorityTarget": True,
                "ProjectileSpeedGRU": 6600,
                "TimeBetweenTwoShots": 0.7,
                "AimingTime": 1.6,
                "TimeBetweenTwoSalvos": 3.0,
                "ShotsCountPerSalvo": 2,
                "SupplyCost": 160.0,
                "AffichageMunitionParSalve": 2,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 6600,
        },
    },

    ("AA_R27ER_Vympel", "A2A", None, False): { # Experimental
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 10125,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.4,
                "AimingTime": 0.3,
                "SupplyCost": 50.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_R27R_Vympel", "A2A", None, False): { # 18
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 9275,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.4,
                "AimingTime": 0.3,
                "SupplyCost": 65.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_R27T_Vympel", "A2A", None, False): { # IR Vympel
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 7700,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.4,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 8400,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.4,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 8400,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.4,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 6825,
                "TimeBetweenTwoSalvos": 1.4,
                "AimingTime": 0.3,
                "SupplyCost": 50.0,
            },
        },
    },
    
    ("AA_R13M", "A2A", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_tbagru",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 3850,
                "PhysicalDamages": 4.0,
                "AimingTime": 0.3,
                "SupplyCost": 25.0,
            },
        },
    },

    ("AA_R13M_HAGRU", "A2A", "AA_R13M", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_hagru",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 3850,
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
            },
            "parent_membr": {
                "AimingTime": 0.3,
            },
        },
    },

    ("AA_AIM9M_Sidewinder", "A2A", None, False): { # 7
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_tbagru",
            },
            "hit_roll": {
                "Idling": 70,
                "Moving": 70,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_AIM9M_Sidewinder_HAGRU", "A2A", "AA_AIM9M_Sidewinder", True): { # 7
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_hagru",
            },
            "hit_roll": {
                "Idling": 70,
                "Moving": 70,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_AIM9L_Sidewinder_upgrade", "A2A", None, False): { # 7
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_tbagru",
            },
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_AIM9L_Sidewinder_upgrade_HAGRU", "A2A", "AA_AIM9L_Sidewinder_upgrade", True): { # 7
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_hagru",
            },
            "hit_roll": {
                "Idling": 65,
                "Moving": 65,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 40.0,
            },
        },
    },

    ("AA_AIM9L_Sidewinder", "A2A", None, False): { # 6
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_tbagru",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 30.0,
            },
        },
    },

    ("AA_AIM9L_Sidewinder_HAGRU", "A2A", "AA_AIM9L_Sidewinder", True): { # 6
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_hagru",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "AimingTime": 0.3,
                "SupplyCost": 30.0,
            },
        },
    },
    
    ("AA_AIM9L_Sidewinder_Helo", "A2A", "AA_AIM9L_Sidewinder", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_tbagru",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 3325,
                "MissileDescriptor": "~/Descriptor_Missile_AA_AIM9L_Sidewinder_Helo",
            },
        },
        "MissileDescriptor": {
            "AutoGyr": 2.617994,
        },
    },
    
    ("AA_AIM9L_Sidewinder_Helo_HAGRU", "A2A", "AA_AIM9L_Sidewinder_Helo", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_hagru",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "MaximumRangeHelicopterGRU": 2625,
                "MaximumRangeAirplaneGRU": 3325,
            },
        },
    },

    ("AA_AIM9J_Sidewinder", "A2A", None, False): { # 5
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_tbagru",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 3850,
                "AimingTime": 0.3,
                "SupplyCost": 25.0,
            },
        },
    },

    ("AA_AIM9J_Sidewinder_HAGRU", "A2A", "AA_AIM9J_Sidewinder", True): { # 5
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_hagru",
            },
            "hit_roll": {
                "Idling": 50,
                "Moving": 50,
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 3850,
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
            },
            "parent_membr": {
                "MaximumRangeAirplaneGRU": 7700,
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "TimeBetweenTwoSalvos": 1.4,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 8400,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.4,
                "AimingTime": 0.3,
                "SupplyCost": 50.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },

    ("AA_AIM7P_Sparrow", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 8400,
                "ProjectileSpeedGRU": 4946,
                "MaxAccelerationGRU": 2826,
                "TimeBetweenTwoSalvos": 1.4,
                "AimingTime": 0.3,
                "SupplyCost": 50.0,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 4946,
            "MaxAccelerationGRU": 2826,
        },
    },
    
    ("AA_AIM54_Phoenix", "A2A", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_missile_he_bigly",
            },
            "hit_roll": {
                "Idling": 40,
                "Moving": 40,
            },
            "parent_membr": {
                "TraitsToken": ['MOTION', 'F&F', 'biglyHE'],
                "MaximumRangeAirplaneGRU": 13300,
                "PhysicalDamages": 8.0,
                "SuppressDamages": 350, # 210 against vet 3 targets, will still stun in 1 hit
                "TirReflexe": True,
                "ReflexShotDisabledIfPriorityTarget": True,
                "ProjectileSpeedGRU": 7200,
                "TimeBetweenTwoShots": 0.7,
                "AimingTime": 1.6,
                "TimeBetweenTwoSalvos": 3.0,
                "ShotsCountPerSalvo": 2,
                "SupplyCost": 160.0,
                "AffichageMunitionParSalve": 2,
            },
        },
        "MissileDescriptor": {
            "MaxSpeedGRU": 7200,
        },
    },

    ("AA_AIM120A_AMRAAM", "A2A", None, False): { # 1
        "Ammunition": {
            "hit_roll": {
                "Idling": 70,
                "Moving": 70,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 8400,
                "TimeBetweenTwoSalvos": 1.4,
                "AimingTime": 0.3,
                "SupplyCost": 60.0,
            },
        },
    },
    
    ("AA_R77_Vympel", "A2A", None, False): {
        "Ammunition": {
            "hit_roll": {
                "Idling": 70,
                "Moving": 70,
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 8400,
                "TimeBetweenTwoSalvos": 1.4,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 6300,
                "TimeBetweenTwoSalvos": 1.4,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 6825,
                "TimeBetweenTwoSalvos": 1.4,
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
            },
            "parent_membr": {
                "TimeBetweenTwoShots": 1.4,
                "TimeBetweenTwoFx": 1.4,
                "MaximumRangeAirplaneGRU": 7700,
                "TimeBetweenTwoSalvos": 1.4,
                "AimingTime": 0.3,
                "SupplyCost": 50.0,
            },
        },
    },
    
    ("AA_R550_Magic_II", "A2A", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_tbagru",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "AimingTime": 0.3,
            },
        },
    },

    ("AA_R550_Magic_II_HAGRU", "A2A", "AA_R550_Magic_II", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_a2a_hagru",
            },
            "hit_roll": {
                "Idling": 60,
                "Moving": 60,
            },
            "parent_membr": {
                "AimingTime": 0.3,
            },
        },
    },
}
# fmt: on
