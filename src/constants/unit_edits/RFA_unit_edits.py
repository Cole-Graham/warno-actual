rfa_unit_edits = {
    # RFA LOG
    "Iltis_RFA": {
        "CommandPoints": 145,
        "TrueAvail": [0, 3, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },

    # RFA INF
    "Panzergrenadier_CMD_RFA": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDR PANZERGRENADIER LDR.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Rifles_CMD_US",
                "Unite",
            ],
        },
        "strength": 6,
        "WeaponAssignment": [
                (0, [1]),
                (1, [0]),
                (2, [0]),
                (3, [0]),
                (4, [0, 3]),
                (5, [0, 2])
            ],
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                'infantry_equip_heavy',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "TrueAvail": [0, 0, 7, 5],
        "max_speed": 20,
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_M72A3_LAW_66mm": 6,
            },
        },
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "Panzergrenadier_IFV_RFA": {  # PZ.GRENADIER
        "GameName": {
            "display": "PANZERGRENADIER"
        },
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "TrueAvail": [12, 9, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "ATteam_Milan_2_RFA": {
        "CommandPoints": 45,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "TrueAvail": [6, 4, 0, 0],
    },

    "Unimog_trans_RFA": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "Iltis_trans_RFA": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    # RFA ART
    "M113_PzMorser_RFA": {
        "GameName": {
            "display": "PzMrs M113A1G"
        },
        "CommandPoints": 75,
        "TrueAvail": [4, 3, 0, 0],
    },

    "M109A3G_HOWZ_RFA": {
        "CommandPoints": 170,
        "TrueAvail": [3, 2, 0, 0],
    },

    # RFA TANK
    "TPZ_Fuchs_1_RFA": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "Marder_1A3_RFA": {
        "CommandPoints": 40,
    },

    "Jaguar_2_RFA": {
        "CommandPoints": 75,
    },

    "Marder_1A3_MILAN_RFA": {
        "CommandPoints": 50,
    },

    # RFA REC
    "BGS_RFA": {
        "GameName": {
            "display": "#RECO2 BGS STREIFE"
        },
        "CommandPoints": 15,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },

    "M113_GreenArcher_RFA": {
        # "optics": {
        #     "OpticalStrength": 233.475
        # },
        "TrueAvail": [8, 0, 0, 0],
    },

    # RFA AA
    "MANPAD_Redeye_RFA": {  # Fliegerfaust
        "CommandPoints": 20,
        "TrueAvail": [12, 9, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("PM_uzi", "PM_uzi_noreflex")],
            },
        },
    },
}
