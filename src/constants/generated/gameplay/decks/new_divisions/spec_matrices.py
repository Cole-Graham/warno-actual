"""Activation Point matrices for National divisions."""

spec_tags = {
    "general": ["DEFAULT", "infantryReg", "DC_PWR1"],
    "airborne": ["DEFAULT", "infantryReg","DC_PWR1"],
    "armored": ["DEFAULT", "armored", "DC_PWR1"],
    "mechanized": ["DEFAULT", "infantryReg", "DC_PWR1"],
    "motorized": ["DEFAULT", "infantryReg", "DC_PWR1"],
}

spec_matrices = {
    "general": {
        "EFactory/Art": [2, 3, 4, 5, 6],
        "EFactory/DCA": [2, 2, 3, 4, 5],
        "EFactory/Defense": [],
        "EFactory/Helis": [2, 2, 3, 4, 5],
        "EFactory/Infantry": [2, 2, 2, 2, 2, 3, 4, 5],
        "EFactory/Logistic": [2, 2, 2, 2, 2, 2, 2, 3, 3],
        "EFactory/Planes": [2, 2, 4, 5, 6, 8],
        "EFactory/Recons": [2, 2, 2, 2, 2, 2, 3],
        "EFactory/Tanks": [2, 2, 2, 2, 3, 3, 3, 3],
    },
    "airborne": {
        "EFactory/Art": [2, 3, 4, 4, 6],
        "EFactory/DCA": [2, 2, 3, 4, 4],
        "EFactory/Defense": [],
        "EFactory/Helis": [2, 2, 2, 3, 3, 4, 5],
        "EFactory/Infantry": [2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4],
        "EFactory/Logistic": [2, 2, 2, 2, 2, 2, 3, 3],
        "EFactory/Planes": [2, 2, 3, 3, 4, 6, 8],
        "EFactory/Recons": [2, 2, 2, 3, 3, 3, 3],
        "EFactory/Tanks": [2, 2, 3, 3],
    },
    "armored": {
        "EFactory/Art": [2, 3, 4, 5, 6],
        "EFactory/DCA": [2, 2, 3, 4, 6],
        "EFactory/Defense": [],
        "EFactory/Helis": [2, 2, 2, 3, 4],
        "EFactory/Infantry": [2, 2, 2, 2, 3, 3, 4, 5],
        "EFactory/Logistic": [2, 2, 2, 2, 2, 2, 3, 3, 3],
        "EFactory/Planes": [2, 2, 4, 5, 6, 8],
        "EFactory/Recons": [2, 2, 2, 2, 2, 3, 4],
        "EFactory/Tanks": [2, 2, 2, 2, 2, 2, 3, 3],
    },
    "mechanized": {
        "EFactory/Art": [2, 2, 4, 4, 5, 6],
        "EFactory/DCA": [2, 2, 4, 4, 6],
        "EFactory/Defense": [],
        "EFactory/Helis": [2, 2, 3, 4],
        "EFactory/Infantry": [2, 2, 2, 2, 2, 2, 3, 4, 4, 5],
        "EFactory/Logistic": [2, 2, 2, 2, 2, 2, 2, 3, 3],
        "EFactory/Planes": [2, 2, 3, 4, 5, 8],
        "EFactory/Recons": [2, 2, 2, 2, 2, 2, 3],
        "EFactory/Tanks": [2, 2, 2, 2, 2, 2, 2, 3],
    },
}