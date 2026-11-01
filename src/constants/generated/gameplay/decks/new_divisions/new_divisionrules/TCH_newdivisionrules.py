"""Division rules for Czechoslovakia (TCH).

NSWP loads these dicts by name. Filling a list is enough for those units to
join the matching coalition divisions.
"""

TCH_airborne_newdivisionrules = {
    "logistic": [],
    "infantry": [],
    "artillery": [],
    "tank": [],
    "recon": [],
    "aa": [],
    "heli": [],
    "planes": [],
}

TCH_armored_newdivisionrules = {
    "logistic": [],
    "infantry": [],
    "artillery": [],
    "tank": [
        ("T72M2_Moderna_TCH", 2, [0, 0, 4, 3]),
    ],
    "recon": [],
    "aa": [],
    "heli": [],
}

TCH_mechanized_newdivisionrules = {
    "logistic": [],
    "infantry": [],
    "artillery": [],
    "tank": [],
    "recon": [],
    "aa": [],
    "heli": [],
    "planes": [],
}

TCH_motorized_newdivisionrules = {
    "logistic": [],
    "infantry": [],
    "artillery": [],
    "tank": [],
    "recon": [],
    "aa": [],
    "heli": [],
    "planes": [],
}

TCH_global_newdivisionrules = {
    "planes": [],
}
