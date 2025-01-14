"""Bomb weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Bomb_ZB500_500kg_Napalm_x4", "napalm_bomb", None, False): { # 93
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 240,
            },
        },
    },
    
    ("Bomb_Mk83_450kg_x2", "he_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 190,
            },
        },
    },
    
    ("Bomb_Mk82_250kg_x8", "he_bomb", None, False): { # 78
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 320,
            },
        },
    },

    ("Bomb_Mk82_250kg_x6", "he_bomb", None, False): { # 77
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 280,
            },
        },
    },

    ("Bomb_Mk82_250kg_x4", "he_bomb", None, False): { # 76
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 240,
            },
        },
    },

    ("Bomb_Mk82_250kg_x2", "he_bomb", None, False): { # 75
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 160,
            },
        },
    },

    ("Bomb_Mk82_250kg_x12", "he_bomb", None, False): { # 74
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 400,
            },
        },
    },
    
    ("Bomb_Mk77_340kg_Napalm_x4", "napalm_bomb", None, False): { # 71
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 180,
            },
        },
    },

    ("Bomb_Mk77_340kg_Napalm_x2", "napalm_bomb", None, False): { # 70
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 120,
            },
        },
    },
    
    ("Bomb_Mk18_RET_513kg_x6", "he_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 420,
            },
        },
    },
    
    ("Bomb_Mk18_RET_513kg_x4", "he_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 315,
            },
        },
    },

    ("Bomb_FAB_500kg_x6", "napalm_bomb", None, False): { # 58
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 450,
            },
        },
    },

    ("Bomb_FAB_500kg_x4", "napalm_bomb", None, False): { # 57
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 360,
            },
        },
    },

    ("Bomb_FAB_250kg_x4", "napalm_bomb", None, False): { # 54
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 280,
            },
        },
    },
    
    ("Bomb_CLU_RBK_500kg_x2", "clu_bomb", None, False): { # 56
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 240,
            },
        },
    },

    ("Bomb_CBU_Mk20_Rockeye_II_250kg_x8", "clu_bomb", None, False): { # 44
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 420,
            },
        },
    },

    ("Bomb_CBU_Mk20_Rockeye_II_250kg_x5", "clu_bomb", None, False): { # 43
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 320,
            },
        },
    },

    ("Bomb_CBU_Mk20_Rockeye_II_250kg_x4", "clu_bomb", None, False): { # 42
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 270,
            },
        },
    },

    ("Bomb_CBU_Mk20_Rockeye_II_250kg_x2", "clu_bomb", None, False): { # 41
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 180,
            },
        },
    },
    
    ("Bomb_BL755_cluster_264kg_x4", "clu_bomb", None, False): {
        "Ammunition": {
            "parent_membr": {
                "SupplyCost": 315,
            },
        },
    },
}
# fmt: on