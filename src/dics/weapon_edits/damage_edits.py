"""Damage edit constants."""

# Infantry armor edits
INFANTRY_ARMOR_EDITS = {
    71: (1.0, "artillerie 1"),
    72: (1.0, "assaut 1"),
    # ... (all the infantry edits)
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
            37: 1.5,    # helicopter <1 armor (1.0 is vanilla)
            45: 1.75,   # vehicle <1 armor (1.25 is vanilla)
        }
    },
    "HE_autocanon_1": {  # 12.7mm
        "row": 117,
        "edits": {
            37: 3.3,    # helicopter <1 armor (2.5 is vanilla)
            49: 1.0,    # WA Infantry 1 (14 strength)
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