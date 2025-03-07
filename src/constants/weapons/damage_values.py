"""Damage value constants."""

VANILLA_LAST_ROW = 139 # used for log warning if Eugen changed the damage array
VANILLA_LAST_COLUMN = 48 + 13 # 13 is the number of WA armor levels, we add them before this check (yeah...not optimal)

# formatting is usually 13 values per row, except WA infantry armor has a dedicated row
SNIPER_DAMAGE = [
    # sniper 1
    [0.8, 0.4, 0.2, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 3.25, 1.75,
     0.25, 1.0, 1.0, 1.0, 0.0, 0.0, 2.5, 0.25, 0.1, 1.25,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], # 13 WA armor levels
    # sniper 2 (modified version of he_autocanon 2)
    [1.0, 1.0, 1.0, 0.3, 2.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
     0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.5, 1.0,
     0.0, 1.0, 1.0, 1.0, 8.0, 1.0, 2.5, 2.0, 1.0, 2.0,
     1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], # 13 WA armor levels
]

SA_INTERMEDIATE_DAMAGE_RATIOS = [ # DON'T ADD 13 WA armor levels, the code combines SA_INF_ARMOR_DAMAGE_RATIOS and SA_INTERMEDIATE_DAMAGE_RATIOS
    0.8, 0.4, 0.2, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 2.25, 1.25,
    0.25, 1.0, 1.0, 1.0, 0.0, 0.0, 1.75, 0.25, 0.1, 1.25,
]

# Only used on infantry 7.62mm weapons, vehicle turrets remain on fm_balle 1 damage family
SA_FULL_DAMAGE_RATIOS = [ # DON'T ADD 13 WA armor levels, the code combines SA_INF_ARMOR_DAMAGE_RATIOS and SA_FULL_DAMAGE_RATIOS
    0.8, 0.4, 0.2, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 3.25, 1.75,
    0.25, 1.0, 1.0, 1.0, 0.0, 0.0, 2.5, 0.25, 0.1, 1.25,
]

SA_INF_ARMOR_DAMAGE_RATIOS = [ # small arms, i.e. intermediate and full size calibers (5.56, 5.45, 7.62mm, etc.)
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0 ], # 2 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96], # 3 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92], # 4 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88], # 5 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84], # 6 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8 ], # 7 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76], # 8 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72], # 9 strength
    [1.0,  1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72, 0.68], # 10 strength
    [1.0,  1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72, 0.68, 0.64], # 11 strength
    [1.0,  1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72, 0.68, 0.64, 0.6 ], # 12 strength
    [1.0,  1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72, 0.68, 0.64, 0.6,  0.56], # 13 strength
    [1.0,  0.96, 0.92, 0.88, 0.84, 0.8,  0.76, 0.72, 0.68, 0.64, 0.6,  0.56, 0.52], # 14 strength
]

DPICM_DAMAGES = [
    # DPICM 1
    [3.0, 3.0, 2.0, 0.03, 0.054, 0.04, 0.02, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
     0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
     0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.5, 0.5, 3.0, 3.0, 2.0, 0.5,
     0.5, 0.5, 0.17, 0.13, 0.14, 0.14, 0.9, 0.14,
     0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05], # 13 WA armor levels
    # DPICM 2
    [3.0, 3.0, 2.0, 0.03, 0.054, 0.04, 0.02, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
     0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
     0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.5, 0.5, 3.0, 3.0, 2.0, 0.5,
     0.5, 0.5, 0.17, 0.13, 0.14, 0.14, 0.9, 0.14,
     0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05], # 13 WA armor levels
    # DPICM 3
    [0.03, 0.03, 0.02, 0.03, 0.054, 0.04, 0.025, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
     0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
     0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.055, 0.055, 0.055, 0.03, 0.03,
     0.02, 0.055, 0.055, 0.055, 0.17, 0.13, 0.14, 0.14, 0.9, 0.14,
     0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055, 0.055], # 13 WA armor levels
    # DPICM 4
    [3.0, 3.0, 2.0, 0.03, 0.054, 0.04, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
     0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
     0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.5, 0.5, 0.5, 3.0, 3.0, 2.0,
     0.05, 0.05, 0.05, 0.17, 0.13, 0.14, 0.14, 0.9, 0.14,
     0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05] # 13 WA armor levels
]

TWELVE_SEVEN_MM_DAMAGE = [
    1.2, 1.1, 1.0, 0.3, 3.5, 1.5, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 3.3, 2.5,
    1.7, 1.0, 1.0, 1.0, 8.0, 1.0, 5.0, 3.5, 1.0, 3.3,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, # 13 WA armor levels
]

FOURTEEN_FIVE_MM_DAMAGE = [
    1.2, 1.1, 1.0, 0.3, 5.0, 2.0, 1.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 3.3, 2.5,
    1.7, 1.0, 1.0, 1.0, 8.0, 1.0, 7.0, 5.0, 1.0, 3.3,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, # 13 WA armor levels
]

NPLM_BOMB_DAMAGE = [
    1.0, 1.0, 1.0, 1.0, 0.8, 0.4, 0.3, 0.2, 0.15, 0.1, 0.1, 0.05, 0.05,
    0.05, 0.05, 0.05, 0.05, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
    0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 8.0, 1.0, 1.25, 0.8, 0.4, 1.25,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, # 13 WA armor levels
]

PGB_BOMB_DAMAGE = [
    3.0, 2.0, 1.0, 1.33, 1.0, 0.75, 0.4, 0.375, 0.375, 0.375, 0.375, 0.375, 0.25,
    0.25, 0.25, 0.25, 0.25, 0.25, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125,
    0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 0.125, 1.0, 1.0, 1.0, 3.0, 2.0,
    1.0, 1.5, 1.0, 1.0, 1.0, 1.0, 1.25, 0.75, 0.75, 1.25,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, # 13 WA armor levels
]

MANPAD_HAGRU_DAMAGE = [
    1.0, 0.9, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 8.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, # 13 WA armor levels
]

MANPAD_TBAGRU_DAMAGE = [
    1.0, 0.9, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 8.0, 1.0, 1.0, 1.0, 1.0, 1.0,
    1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, # 13 WA armor levels
]

# Infantry armor edits
INFANTRY_ARMOR_EDITS = {
        71: (5.0, "ap_missile_sead 1"),
        72: (5.0, "ap_missile_sead 2"),
        73: (5.0, "ap_missile_sead 3"),
        74: (1.0, "artillerie 1"),
        75: (1.0, "assaut 1"),
        76: (1.0, "balle 1"),
        77: (0.2, "balleaa 1"),
        78: (1.0, "balledca 1"),
        79: (1.02, "balledca 2"),
        80: (1.36, "balledca 3"),
        81: (1.36, "balledca 4"),
        82: (1.0, "balle_mg 1"),
        83: (1.0, "bombe 1"),
        84: (1.0, "cac 1"),
        85: (1.0, "cac 2"),
        86: (1.0, "cac 3"),
        87: (1.0, "cac 4"),
        88: (0.5, "clu_sol_ap 1"),
        89: (0.5, "clu_sol_ap 2"),
        90: (0.5, "clu_sol_ap 3"),
        91: (0.5, "clu_sol_ap 4"),
        92: (0.5, "clu_sol_ap 5"),
        93: (0.5, "clu_sol_ap 6"),
        94: (0.5, "clu_sol_ap 7"),
        95: (0.5, "clu_sol_ap 8"),
        96: (0.5, "clu_sol_ap 9"),
        97: (0.5, "clu_sol_ap 10"),
        98: (0.5, "clu_sol_ap 11"),
        99: (0.5, "clu_sol_ap 12"),
        100: (0.5, "clu_sol_ap 13"),
        101: (0.5, "clu_sol_ap 14"),
        102: (0.5, "clu_sol_ap 15"),
        103: (0.0, "clu_sol_ap 16"),
        104: (4.0, "cluster 1"),
        105: (0.5, "cluster_ap 1"),
        106: (0.5, "cluster_ap 2"),
        107: (0.5, "cluster_ap 3"),
        108: (0.5, "cluster_ap 4"),
        109: (0.5, "cluster_ap 5"),
        110: (0.5, "cluster_ap 6"),
        115: (1.0, "flamme 1"),
        116: (1.0, "frag 1"),
        117: (0.85, "grenades 1"),
        118: (1.0, "he 1"),
        119: (1.0, "he_dca 1"),
        120: (1.0, "he_autocanon 1"),
        121: (1.0, "he_autocanon 2"),
        122: (1.0, "howz 1"),
        123: (1.0, "howz_bombe 1"),
        124: (1.0, "mmgballe 1"),
        125: (1.0, "mmgballe 2"),
        126: (1.0, "mmgballe 3"),
        127: (1.0, "missile_he 1"),
        128: (0.1, "pmballe 1"),
        129: (0.5, "pmballe 2"),
        130: (1.0, "pmballe 3"),
        131: (1.0, "roquette"),
        132: (1.0, "smoke"),
        133: (1.0, "superhe 1"),
        134: (1.0, "superhe_sol 1"),
        135: (1.0, "suppress 1"),
        136: (1.0, "suppressap 0.75"),
        137: (1.0, "thermobarique 1"),
        138: (1.0, "roquette_ap 1"),
        139: (1.0, "suppresdca 1"),
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
FMBALLE_ROWS = [111, 112, 113, 114]

# Damage array edits for different weapon types
DAMAGE_EDITS = {
    "ap_missile_12": { # wtf eugen poland bias?
        "row": 51,
        "edits": {
            5: 6.0,
        }
    },
    
    "clu_sol_ap_16": {
        "row": 103,
        "edits": {
            6: 7.0,    # 3 top armor (4.25 is vanilla)
        }
    },
    "FMballe_1": {  # 5.56mm
        "row": 111,
        "edits": {
            37: 2.5,    # helicopter <1 armor (1.0 is vanilla)
            38: 1.25,    # helicopter 1 armor (0.5 is vanilla)
            45: 1.75,   # vehicle <1 armor (1.25 is vanilla)
        }
    },
    # need to figure out which weapons to seperate from this category or how to balance them with same family ratio
    "HE_autocanon_1": {  # 12.7mm
        "row": 120,
        "edits": {
            37: 3.3,    # helicopter <1 armor (2.5 is vanilla)
            # 38: 2.4,    # helicopter 1 armor (0.8 is vanilla)
            # 46: 2.0,    # vehicle 1 armor (0.8 is vanilla)
            # 47: 1.0,    # vehicle 2 armor (0.4 is vanilla)
            49: 1.0,    # WA Infantry 1 (14 strength, not set by other WA inf armor function)
        }
    },
    "howz": {
        "row": 122,
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
        "row": 123,
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
        "row": 127,
        "edits": {
            1: 0.7,    # avion 1 armor (0.9 is vanilla)
            2: 0.6,    # avion 2 armor (0.8 is vanilla)
        }
    },
    "thermobarique": {
        "row": 137,
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
            45: 3.0,
            46: 2.0,
            48: 1.0,
        }
    },
    "Roquette_AP_1": {  # blindage
        "row": 138,
        "edits": {
            7: 0.7,    # blindage 4 armor (0.5 is vanilla)
            8: 0.6,    # blindage 5 armor (0.5 is vanilla)
        }
    }
}
