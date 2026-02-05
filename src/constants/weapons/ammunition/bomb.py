"""Bomb weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Bomb_ZB500_500kg_Napalm_salvolength4", "napalm_bomb", None, False): { # 93
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 240.0,
            },
        },
    },
    
    ("Bomb_ZB500_500kg_Napalm_salvolength6", "napalm_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 280.0,
            },
        },
    },
    
    ("Bomb_Matra_400kg_salvolength4", "he_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 315.0,
            },
        },
    },
    
    ("Bomb_Mk84_920kg_salvolength4", "he_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 360.0,
            },
        },
    },
    
    ("Bomb_Mk84_920kg_salvolength2", "he_bomb", "Bomb_Mk84_920kg_salvolength4", True): {
        "Ammunition": {
            "parent_membr": {
                "ShotsCountPerSalvo": 2,
                "SupplyCost": 240.0,
                "AffichageMunitionParSalve": 2,
            },
        },
    },
    
    ("Bomb_Mk83_450kg_salvolength2", "he_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 190.0,
            },
        },
    },
    
    ("Bomb_Mk82_250kg_salvolength12", "he_bomb", None, False): { # 74
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 400.0,
            },
        },
    },
    
    ("Bomb_Mk82_250kg_salvolength8", "he_bomb", None, False): { # 78
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 320.0,
            },
        },
    },

    ("Bomb_Mk82_250kg_salvolength6", "he_bomb", None, False): { # 77
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 280.0,
            },
        },
    },

    ("Bomb_Mk82_250kg_salvolength4", "he_bomb", None, False): { # 76
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 240.0,
            },
        },
    },

    ("Bomb_Mk82_250kg_salvolength2", "he_bomb", None, False): { # 75
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 160.0,
            },
        },
    },
    
    ("Bomb_Mk81_119kg_salvolength4", "he_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 150.0,
            },
        },
    },
    
    ("Bomb_Mk81_119kg_salvolength2", "he_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 100.0,
            },
        },
    },
    
    ("Bomb_Bidons_Speciaux_Napalm_salvolength4", "napalm_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 120.0,
            },
        },
    },
    
    ("Bomb_Mk77_340kg_Napalm_salvolength8", "napalm_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "ShotsCountPerSalvo": 8,
                "SupplyCost": 260.0,
                "AffichageMunitionParSalve": 8,
            },
        },
    },
    
    ("Bomb_Mk77_340kg_Napalm_salvolength5", "napalm_bomb", "Bomb_Mk77_340kg_Napalm_salvolength4", True): { # 71
        "Ammunition": {
            "parent_membr": {
                "ShotsCountPerSalvo": 5,
                "SupplyCost": 200.0,
                "AffichageMunitionParSalve": 5,
            },
        },
    },
    
    ("Bomb_Mk77_340kg_Napalm_salvolength4", "napalm_bomb", None, False): { # 71
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 180.0,
            },
        },
    },
    
    ("Bomb_Mk77_340kg_Napalm_salvolength3", "napalm_bomb", "Bomb_Mk77_340kg_Napalm_salvolength4", True): { # 71
        "Ammunition": {
            "parent_membr": {
                "ShotsCountPerSalvo": 3,
                "SupplyCost": 150.0,
                "AffichageMunitionParSalve": 3,
            },
        },
    },

    ("Bomb_Mk77_340kg_Napalm_salvolength2", "napalm_bomb", None, False): { # 70
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 120.0,
            },
        },
    },
    
    ("Bomb_ODAB_500PM_500kg_Thermobaric_salvolength2", "thermo_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 20.0,
                "SupplyCost": 160.0,
            },
        },
    },
    
    ("Bomb_ODAB_500PM_500kg_Thermobaric_salvolength4", "thermo_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 20.0,
                "SupplyCost": 240.0,
            },
        },
    },
    
    ("Bomb_ODAB_500PM_500kg_Thermobaric_salvolength6", "thermo_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 20.0,
                "SupplyCost": 300.0,
            },
        },
    },
    
    ("Bomb_ODAB_500PM_500kg_Thermobaric_salvolength8", "thermo_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "PhysicalDamages": 20.0,
                "SupplyCost": 360.0,
            },
        },
    },
    
    ("Bomb_Mk18_RET_513kg_salvolength6", "he_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 420.0,
            },
        },
    },
    
    ("Bomb_Mk18_RET_513kg_salvolength4", "he_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 315.0,
            },
        },
    },
    
    ("Bomb_FAB_500kg_salvolength8", "he_bomb", None, False): { # 58
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 540.0,
            },
        },
    },

    ("Bomb_FAB_500kg_salvolength6", "he_bomb", None, False): { # 58
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 450.0,
            },
        },
    },

    ("Bomb_FAB_500kg_salvolength4", "he_bomb", None, False): { # 57
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 360.0,
            },
        },
    },

    ("Bomb_FAB_250kg_salvolength4", "he_bomb", None, False): { # 54
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 280.0,
            },
        },
    },
    
    ("Bomb_CLU_RBK_250kg_salvolength4", "clu_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 280.0,
            },
        },
    },
    
    ("Bomb_CLU_RBK_500kg_salvolength2", "clu_bomb", None, False): { # 56
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 240.0,
            },
        },
    },
    
    ("Bomb_CLU_RBK_500kg_salvolength4", "clu_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 360.0,
            },
        },
    },
    
    ("Bomb_CLU_RBK_500kg_salvolength6", "clu_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 460.0,
            },
        },
    },
    
    ("Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength12", "clu_bomb", None, False): { # 44
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 630.0,
            },
        },
    },


    ("Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength8", "clu_bomb", None, False): { # 44
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 420.0,
            },
        },
    },

    ("Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength5", "clu_bomb", None, False): { # 43
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 320.0,
            },
        },
    },

    ("Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength4", "clu_bomb", None, False): { # 42
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 270.0,
            },
        },
    },

    ("Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength2", "clu_bomb", None, False): { # 41
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 180.0,
            },
        },
    },
    
    ("Bomb_BL755_cluster_264kg_salvolength4", "clu_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 315.0,
            },
        },
    },
    
    ("Bomb_BLG66_Belouga_cluster_305kg_salvolength4", "clu_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 360.0,
            },
        },
    },
}
# fmt: on
