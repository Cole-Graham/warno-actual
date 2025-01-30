"""Damage value constants."""

# Base damage values
SNIPER_DAMAGE = [
    0.8, 0.4, 0.2, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0,
    1.0, 3.25, 1.75, 0.25, 1.0, 1.0, 1.0, 0.0, 0.0, 2.5, 0.25, 0.1, 1.25,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0
]

FULL_BALL_DAMAGE = [
    0.8, 0.4, 0.2, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0,
    1.0, 3.25, 1.75, 0.25, 1.0, 1.0, 1.0, 0.0, 0.0, 2.5, 0.25, 0.1, 1.25,
    1.0, 0.96, 0.92, 0.88, 0.84, 0.8, 0.76, 0.72, 0.68, 0.64, 0.60, 0.56, 0.52
]

DPICM_DAMAGES = [
    # DPICM 1
    [3.0, 3.0, 2.0, 0.03, 0.054, 0.04, 0.02, 0.1, 0.1, 0.1, 0.1, 0.1,
     0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
     0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.5, 0.5, 3.0,
     3.0, 2.0, 0.5, 0.5, 0.5, 0.17, 0.13, 0.14, 0.14, 0.9, 0.14,
     0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
    # DPICM 2
    [3.0, 3.0, 2.0, 0.03, 0.054, 0.04, 0.02, 0.1, 0.1, 0.1, 0.1, 0.1,
     0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
     0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.5, 0.5, 3.0,
     3.0, 2.0, 0.5, 0.5, 0.5, 0.17, 0.13, 0.14, 0.14, 0.9, 0.14,
     0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
    # DPICM 3
    [0.03, 0.03, 0.02, 0.03, 0.054, 0.04, 0.025, 0.01, 0.01, 0.01, 0.01, 0.01,
     0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
     0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.055, 0.055, 0.055, 0.03,
     0.03, 0.02, 0.055, 0.055, 0.055, 0.17, 0.13, 0.14, 0.14, 0.9, 0.14,
     0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055],
    # DPICM 4
    [3.0, 3.0, 2.0, 0.03, 0.054, 0.04, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01,
     0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
     0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.5, 0.5, 0.5, 3.0,
     3.0, 2.0, 0.05, 0.05, 0.05, 0.17, 0.13, 0.14, 0.14, 0.9, 0.14,
     0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
]

KPVT_DAMAGE = [
    1.2, 1.1, 1.0, 0.3, 2.0, 1.5, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 3.3, 2.5,
    1.7, 1.0, 1.0, 1.0, 8.0, 1.0, 3.3, 2.0, 1.0, 3.3,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, # 13 WA armor types
]

NPLM_BOMB_DAMAGE = [
    1.0, 1.0, 1.0, 1.0, 0.8, 0.4, 0.3, 0.2, 0.15, 0.1, 0.1, 0.05, 0.05,
    0.05, 0.05, 0.05, 0.05, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
    0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 8.0, 1.0, 1.25, 0.8, 0.4, 1.25,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
]

# Infantry armor edits
INFANTRY_ARMOR_EDITS = {
        71: (1.0, "artillerie 1"),
        72: (1.0, "assaut 1"),
        73: (1.0, "balle 1"),
        74: (0.2, "balleaa 1"),
        75: (1.0, "balledca 1"),
        76: (1.02, "balledca 2"),
        77: (1.36, "balledca 3"),
        78: (1.36, "balledca 4"),
        79: (1.0, "balle_mg 1"),
        80: (1.0, "bombe 1"),
        81: (1.0, "cac 1"),
        82: (1.0, "cac 2"),
        83: (1.0, "cac 3"),
        84: (1.0, "cac 4"),
        85: (0.5, "clu_sol_ap 1"),
        86: (0.5, "clu_sol_ap 2"),
        87: (0.5, "clu_sol_ap 3"),
        88: (0.5, "clu_sol_ap 4"),
        89: (0.5, "clu_sol_ap 5"),
        90: (0.5, "clu_sol_ap 6"),
        91: (0.5, "clu_sol_ap 7"),
        92: (0.5, "clu_sol_ap 8"),
        93: (0.5, "clu_sol_ap 9"),
        94: (0.5, "clu_sol_ap 10"),
        95: (0.5, "clu_sol_ap 11"),
        96: (0.5, "clu_sol_ap 12"),
        97: (0.5, "clu_sol_ap 13"),
        98: (0.5, "clu_sol_ap 14"),
        99: (0.5, "clu_sol_ap 15"),
        100: (0.0, "clu_sol_ap 16"),
        101: (4.0, "cluster 1"),
        102: (0.5, "cluster_ap 1"),
        103: (0.5, "cluster_ap 2"),
        104: (0.5, "cluster_ap 3"),
        105: (0.5, "cluster_ap 4"),
        106: (0.5, "cluster_ap 5"),
        107: (0.5, "cluster_ap 6"),
        112: (1.0, "flamme 1"),
        113: (1.0, "frag 1"),
        114: (0.85, "grenades 1"),
        115: (1.0, "he 1"),
        116: (1.0, "he_dca 1"),
        117: (1.0, "he_autocanon 1"),
        118: (1.0, "he_autocanon 2"),
        119: (1.0, "howz 1"),
        120: (1.0, "howz_bombe 1"),
        121: (1.0, "mmgballe 1"),
        122: (1.0, "mmgballe 2"),
        123: (1.0, "mmgballe 3"),
        124: (1.0, "missile_he 1"),
        125: (0.1, "pmballe 1"),
        126: (0.5, "pmballe 2"),
        127: (1.0, "pmballe 3"),
        128: (1.0, "roquette"),
        129: (1.0, "smoke"),
        130: (1.0, "superhe 1"),
        131: (1.0, "superhe_sol 1"),
        132: (1.0, "suppress 1"),
        133: (1.0, "suppressap 0.75"),
        134: (1.0, "thermobarique 1"),
        135: (1.0, "roquette_ap 1"),
        136: (1.0, "suppresdca 1"),
    }

# FMballe infantry damage edits
FMBALLE_INFANTRY_EDITS = {
    49: 1.0,    # WA Infantry 1 (14 strength)
    50: 0.96,   # WA Infantry 2 (13 strength)
    51: 0.92,   # WA Infantry 3 (12 strength)
    52: 0.88,   # WA Infantry 4 (11 strength)
    53: 0.84,   # WA Infantry 5 (10 strength)
    54: 0.8,    # WA Infantry 6 (9 strength)
    55: 0.76,   # WA Infantry 7 (8 strength)
    56: 0.72,   # WA Infantry 8 (7 strength)
    57: 0.68,   # WA Infantry 9 (6 strength)
    58: 0.64,   # WA Infantry 10 (5 strength)
    59: 0.6,    # WA Infantry 11 (4 strength)
    60: 0.56,   # WA Infantry 12 (3 strength)
    61: 0.52,   # WA Infantry 13 (2 strength)
}

# FMballe row indices
FMBALLE_ROWS = [108, 109, 110, 111]

# Damage array edits for different weapon types
DAMAGE_EDITS = {
    "FMballe_1": {  # 5.56mm
        "row": 108,
        "edits": {
            37: 2.5,    # helicopter <1 armor (1.0 is vanilla)
            38: 1.25,    # helicopter 1 armor (0.5 is vanilla)
            45: 1.75,   # vehicle <1 armor (1.25 is vanilla)
        }
    },
    # need to figure out which weapons to seperate from this category or how to balance them with same family ratio
    "HE_autocanon_1": {  # 12.7mm
        "row": 117,
        "edits": {
            37: 3.3,    # helicopter <1 armor (2.5 is vanilla)
            # 38: 2.4,    # helicopter 1 armor (0.8 is vanilla)
            # 46: 2.0,    # vehicle 1 armor (0.8 is vanilla)
            # 47: 1.0,    # vehicle 2 armor (0.4 is vanilla)
            49: 1.0,    # WA Infantry 1 (14 strength, not set by other WA inf armor function)
        }
    },
    "howz": {
        "row": 119,
        "edits": {
            4: 0.33,
            5: 0.29,
            6: 0.25,
            7: 0.21,
            8: 0.17,
            9: 0.14,
            10: 0.11,
            (11, 33): 0.08,
            40: 1.0,
            45: 1.0,
            48: 1.0,
        }
    },
    "howz_bombe": {
        "row": 120,
        "edits": {
            4: 0.66,
            5: 0.41,
            6: 0.31,
            7: 0.21,
            8: 0.17,
            9: 0.14,
            10: 0.11,
            (11, 33): 0.08,
            40: 1.0,
            45: 1.0,
            48: 1.0,
        }
    },
    "Missile_HE": {  # avion
        "row": 124,
        "edits": {
            1: 0.7,    # avion 1 armor (0.9 is vanilla)
            2: 0.6,    # avion 2 armor (0.8 is vanilla)
        }
    },
    "thermobarique": {
        "row": 134,
        "edits": {
            4: 0.25,
            5: 0.21,
            6: 0.17,
            7: 0.14,
            8: 0.11,
            9: 0.08,
            10: 0.06,
            (11, 33): 0.05,
            40: 1.0,
            45: 1.0,
            48: 1.0,
        }
    },
    "Roquette_AP_1": {  # blindage
        "row": 135,
        "edits": {
            7: 0.7,    # blindage 4 armor (0.5 is vanilla)
            8: 0.6,    # blindage 5 armor (0.5 is vanilla)
        }
    }
} 