# What each token means in GDConstants.ndf
# 'Value_1' //Bad
# 'Value_2' //Mediocre
# 'Value_3' //Normal
# 'Value_4' //Good
# 'Value_5' //Very good
# 'Value_6' //Exceptional

# PaliersDOptiqueGRU = MAP
# [
#     (0, 'Value_1'),      //Bad
#     (1768, 'Value_2'),   //Mediocre
#     (2651, 'Value_3'),   //Normal
#     (3535, 'Value_4'),   //Good
#     (5301, 'Value_5'),   //Very good
#     (7068, 'Value_6'),   //Exceptional
# ]

# Vanilla values and actual value used for PaliersDOptiqueGRU
OPTIC_TIERS_GRU = {
    "Bad": {
        "ui_threshold": 0,
        "optic_strength": 1590.0,
    },
    "Mediocre": {
        "ui_threshold": 1768,
        "optic_strength": 2473.0,
    },
    "Normal": {
        "ui_threshold": 2651,
        "optic_strength": 3180.0,
    },
    "Good": {
        "ui_threshold": 3535,
        "optic_strength": 5300.0,
    },
    "Very good": {
        "ui_threshold": 5301,
        "optic_strength": 7067.0,
    },
    "Exceptional": {
        "ui_threshold": 7068,
        "optic_strength": 8834.0,
    },
}

# PaliersDOptiqueDAltitudeGRU = MAP
# [
#     (0, 'Value_3'),      //Normal
#     (5301, 'Value_4'),   //Good
#     (10601, 'Value_5'),  //Very good
#     (13250, 'Value_6'),  //Exceptional
# ]

# Vanilla values for PaliersDOptiqueDAltitudeGRU (HighAltittude / Plane optics)
OPTIC_TIERS_ALTITUDE_GRU = {
    "Normal": {
        "ui_threshold": 0,
        "optic_strength": 5300,
    },
    "Good": {
        "ui_threshold": 5301,
        "optic_strength": 10600,
    },
    "Very Good": {
        "ui_threshold": 10601,
        "optic_strength": 15901,
    },
    "Exceptional": {
        "ui_threshold": 13250,
        "optic_strength": 21201,
    },
}