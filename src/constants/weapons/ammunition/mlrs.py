"""MLRS weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("RocketArt_thermobaric_220mm_salvolength30", "MLRS", None, False): { # 657
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_thermobarique",
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'thermobaric'],
                "PorteeMaximaleGRU": 3000,
                "DispersionAtMaxRangeGRU": 700,
                "DispersionAtMinRangeGRU": 350,
                "PhysicalDamages": 7.2,
                "SuppressDamages": 467,
                "RadiusSplashPhysicalDamagesGRU": 220,
                "RadiusSplashSuppressDamagesGRU": 293,
                "TempsEntreDeuxSalves": 240.0,
                "SupplyCost": 2100,
                "FlightTimeForSpeed": 7.0,
                "DistanceForSpeedGRU": 3063,
            },
        },
    },

    ("RocketArt_M26_227mm_Cluster", "MLRS", None, False): { # 651
        "Ammunition": {
            "displayname": "M26 'Steel Rain'",
            "nametoken": "ULWAVTGKUK",
            "Arme": {
                "Index": 3,
                "Family": "DamageFamily_dpicm",
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 1.8,
                "TempsEntreDeuxFx": 1.8,
                "RadiusSplashPhysicalDamagesGRU": 400,
                "PhysicalDamages": 3,
                "RadiusSplashSuppressDamagesGRU": 533,
                "SuppressDamages": 20,
                "DispersionAtMaxRangeGRU": 1500,
                "DispersionAtMinRangeGRU": 500,
                "TempsEntreDeuxSalves": 130.0,
                "NbTirParSalves": 144,
                "SupplyCost": 960,
                "NbrProjectilesSimultanes": 12,
                "AffichageMunitionParSalve": 12,
            },
        },
    },

    ("RocketArt_M26_227mm", "MLRS", None, False): { # 651
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 7.2,
                "SuppressDamages": 467,
                "DispersionAtMaxRangeGRU": 848,
                "RadiusSplashPhysicalDamagesGRU": 283,
                "RadiusSplashSuppressDamagesGRU": 377,
            },
        },
    },

    ("RocketArt_M21OF_122mm_salvolength12", "MLRS", None, False): { # 649
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
                "SupplyCost": 174,
            },
        },
    },

    ("RocketArt_M21OF_122mm", "MLRS", None, False): { # 646
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
                "TempsEntreDeuxSalves": 220.0,
                "SupplyCost": 580,
            },
        },
    },

    ("RocketArt_M21OF_122mm_RM70", "MLRS", "RocketArt_M21OF_122mm", True): { # 646
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 4.2,
                "SuppressDamages": 350,
                "RadiusSplashPhysicalDamagesGRU": 152,
                "RadiusSplashSuppressDamagesGRU": 203,
                "TempsEntreDeuxSalves": 155.0,
                "SupplyCost": 580,
            },
        },
        "BaseSupplyCost": 580,
        "NbWeapons": [1],
    },
}
# fmt: on
