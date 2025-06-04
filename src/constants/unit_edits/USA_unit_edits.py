"""USA unit edits."""

# from typing import Any, Dict

# fmt: off
usa_unit_edits = {
    # US LOG
    "OH58C_CMD_US": {
        "CommandPoints": 115,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 0, 0],
    },

    "UH60A_CO_US": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 3, 0, 0],
        "UpgradeFromUnit": "OH58C_CMD_US",
    },

    "M151_MUTT_CMD_US": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 4, 0, 0],
    },

    "M1025_Humvee_CMD_para_US": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            # "remove": ["US_82nd_Airborne"],
            # airborne humvee becomes redundant with regular after FWD deploy changes, just give regular one to 82ab
            # but not in the same patch as changing tacom transports, to avoid potential deckwipes
        },
        "availability": [0, 3, 0, 0],
        "SpecialtiesList": {
            "remove_specs": ["'_para'"],
        },
        "ButtonTexture": "M1025_Humvee_CMD_US",
        "DeploymentShift": 0,
    },

    "M1025_Humvee_CMD_US": {
        "CommandPoints": 145,
        "availability": [0, 3, 0, 0],
        "Divisions": {
            # "add": ['US_82nd_Airborne'],
            # airborne humvee redundant with regular after FWD deploy changes, just give regular one to 82ab imo
            # but not in the same patch as changing tacom transports, to avoid potential deckwipes
            "US_82nd_Airborne": {
                "cards": 2,
            },
        },
    },

    "M2A1_Bradley_Leader_US": {
        "CommandPoints": 180,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 3, 0],
        "UpgradeFromUnit": "M577_CMD2_US",
    },

    "M2A2_Bradley_Leader_US": {
        "CommandPoints": 180,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 0, 2],
    },

    "CH47_Super_Chinook_US": {
        "UpgradeFromUnit": "UH60A_Supply_US",
    },

    # US INF
    "Rifles_half_CMD_US": {
        "CommandPoints": 30,
        "GameName": {
            "token": "CPCIJQLHML",
            "display": "#LDR FIRETEAM LDR.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_IFV",
                "UNITE_Rifles_half_CMD_US",
                "Unite",
            ],
        },
        "strength": 6,
        "WeaponAssignment": [
                (0, [0, ]),
                (1, [0, ]),
                (2, [1, ]),
                (3, [1, ]),
                (4, [1, 3]),
                (5, [1, 2]),
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
                '_ifv',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 2,
                    "Commando_733": 4,
                },
            },
            "Salves": {
                "RocketInf_M72A3_LAW_66mm": 6,
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "Rifles_CMD_US": {
        "CommandPoints": 30,
        "GameName": {
            "token": "SVWNZUYPNE",
            "display": "#LDR MECH. RIFLES LDR.",
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
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_M72A3_LAW_66mm": 6,
            },
        },
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "NatGuard_CMD_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "Engineer_CMD_US": {
        "CommandPoints": 55,
        "GameName": {
            "display": "#LDR ENGINEERS LDR.",
            "token": "DBEBRUEYSP",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Engineer_CMD_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        # "SortingOrder": 20040,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                '_leader',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "Divisions": {
            "US_11ACR": {
                "Transports": ["M1038_Humvee_US", "M113A3_US"],
            }
        },
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [1, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, ]),
                (6, [0, ]),
                (7, [0, ]),
                (8, [0, ]),
                (9, [0, ]),
                (10, [0, 2, ]),
            ],
        "WeaponDescriptor": {
            "Salves": {
                "add": [(2, 8)], # (turret, salves)
            },
            "equipmentchanges": {
                "add": [(2, "RocketInf_M72A3_LAW_66mm")], # (turret, weapon)
            },
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "Rangers_CMD_US": {
        "CommandPoints": 70,
        "GameName": {
            "display": "#LDR RANGERS LDR.",
            "token": "WPUCULQQND",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Rangers_CMD_US",
                "Unite",
                "noSIGINT",
            ],
        },
        "strength": 9,
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, ]),
                (6, [0, ]),
                (7, [0, 3]),
                (8, [0, 2]),
            ],
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry_sf", "Texture_sf"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                '_sf',
                '_choc',
                'infantry_equip_heavy',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry_sf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_8th_Inf": {
                "Transports": ["M1038_Humvee_US", "UH60A_Black_Hawk_US"]
            },
        },
        "availability": [0, 0, 0, 3],
        "max_speed": 20,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Commando_733", "M16A1_Carbine")],
                "quantity": {
                    "M16A1_Carbine": 7,
                },
            },
            "Salves": {
                "M16A1_Carbine": 7,
                "RocketInf_M67_RCL_90mm": 10,
            },
        },
        "unique_count": 2,
        "surrogates": 9,
        "selector_tactic": "(2, 9)",
        "selector_tactic_obj": "02_09",
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "Airborne_Engineer_CMD_US": {
        "CommandPoints": 55,
        "GameName": {
            "display": "#LDR AB ENGINEERS LDR.",
            "token": "LRTQFDCCCB",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Airborne_Engineer_CMD_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        # "SortingOrder": 20040,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                '_leader',
                '_choc',
                '_para',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "Airborne_CMD_US": {
        "CommandPoints": 65,
        "GameName": {
            "display": "#LDR AIRBORNE LDR.",
            "token": "BHVJUDTEVR",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Standard",
                "UNITE_Airborne_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20060,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                '_choc',
                '_para',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "RocketInf_AT4_83mm": 8,
            },
        },
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "AeroRifles_CMD_US": {
        "CommandPoints": 45,
        "GameName": {
            "display": "#LDR AERO-RIFLES LDR.",
            "token": "TVWIKAOSVP",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Standard",
                "UNITE_AeroRifles_CMD_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20060,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "Aero_half_CMD_US": {
        "CommandPoints": 35,
        "GameName": {
            "display": "#LDR AERO-FIRETEAM LDR.",
            "token": "MHGSSCNBFO",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Standard",
                "UNITE_AeroRifles_CMD_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20045,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 41,
        # "UnitDefenseValue": 41,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 6, 4],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "AeroEngineer_CMD_US": {
        "CommandPoints": 55,
        "GameName": {
            "display": "#LDR AERO-ENGINEERS LDR.",
            "token": "OWQFQTLBJN",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_AeroEngineer_CMD_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        # "SortingOrder": 20085,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 31,
        # "UnitDefenseValue": 31,
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                '_leader',
                '_choc',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "GreenBerets_CMD_US": {
        "CommandPoints": 75,
        "GameName": {
            "display": "#LDR GREEN BERETS LDR.",
            "token": "KFNXNJOXZS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Standard",
                "UNITE_GreenBerets_CMD_US",
                "Unite",
                "noSIGINT",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20100,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 41,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_sf',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 0, 2],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "Engineers_US": {
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 2,
            },
            "US_8th_Inf": {
                "Transports": ["M35_trans_US", "M113A3_US"],  # no change, just reversed display order
            },
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [1, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, ]),
                (6, [0, ]),
                (7, [0, ]),
                (8, [0, ]),
                (9, [0, 2]),
            ],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "MMG_WA_M60E3_7_62mm": 2,
                },
            },
            "Salves": {
                "Grenade_Satchel_Charge": 6,
            },
        },
    },

    "NatGuard_Engineers_US": {
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "AeroEngineers_US": {
        "CommandPoints": 50,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [1, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, ]),
                (6, [0, ]),
                (7, [0, ]),
                (8, [0, ]),
                (9, [0, 2]),
            ],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "MMG_WA_M60E3_7_62mm": 2,
                },
            },
            "Salves": {
                "Grenade_Satchel_Charge": 6,
            },
        },
    },

    "Airborne_Engineers_US": {
        "CommandPoints": 50,
        # "GameName": {
        #     "display": "AIRBORNE ASSAULT ENG.",
        #     "token": "TXOZWRNEVU",
        # },
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "Grenade_Satchel_Charge": 6,
            },
        },
    },

    "Engineers_Flash_US": {
        "GameName": {
            "display": "ENGINEERS [FLASH]",
        },
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 2,
            },
            "US_8th_Inf": {
                "Transports": ["M151_MUTT_trans_US", "M113A3_US"],  # no change, just reversed display order
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "RocketInf_M202_Flash_66mm": 2,
            },
        },
    },

    "Airborne_Engineers_Flash_US": {
        "GameName": {
            "display": "AB ENGINEERS [FLASH]",
        },
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_inf_M240B_7_62mm", "MMG_WA_M60E3_7_62mm")],
            },
            "Salves": {
                "FM_M16": 9,
                "MMG_WA_M60E3_7_62mm": 18,
                "RocketInf_M202_Flash_66mm": 2,
            },
        },
    },

    "NatGuard_Engineers_Flam_US": {
        "GameName": {
            "display": "NG ENGINEERS [FLAM]",
        },
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
            "Salves": {
                "PM_GreaseGun": 40,
                "FM_M16A1": 7,
                "MMG_M60E1_7_62mm": 18,
                "flamethrower_M2": 15,
            },
        },
    },

    "NatGuard_Engineers_M67_US": {
        "GameName": {
            "display": "NG ENGINEERS [M67]",
        },
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16A1": 10,
                "RocketInf_M67_RCL_90mm": 8,
            },
        },
    },

    "Engineers_Dragon_US": {
        "GameName": {
            "display": "ENGINEERS [DRAGON]",
        },
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 2,
            },
            "US_8th_Inf": {
                "Transports": ["M35_trans_US", "M113A3_US"],  # no change, just reversed display order
            },
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "M47_DRAGON": 6,
            },
            "equipmentchanges": {
                "replace": [("M47_DRAGON", "M47_DRAGON_II")],
            },
        },
    },

    "Airborne_Dragon_US": {
        "GameName": {
            "display": "AIRBORNE [DRAGON]",
        },
        "CommandPoints": 50,
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Airborne_MP_US": {
        "CommandPoints": 20,
        "availability": [0, 12, 9, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "MP_US": {
        "CommandPoints": 20,
        "availability": [0, 12, 9, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [1, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
            ],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "MMG_WA_M60E3_7_62mm": 2,
                },
            },
            "Salves": {
                "FM_M16": 7,
            },
        },
    },

    "Airborne_MP_RCL_US": {
        "GameName": {
            "display": "AB MP PATROL [M67]",
        },
        "CommandPoints": 25,
        "availability": [0, 9, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
            },
        },
    },

    "MP_RCL_US": {
        "GameName": {
            "display": "MP PATROL [M67]",
        },
        "CommandPoints": 25,
        "availability": [0, 9, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "RocketInf_M67_RCL_90mm": 6,
            },
        },
    },

    "Rifles_HMG_US": { # GUNNERS
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Airborne_HMG_US": {  # AIRBORNE GUNNERS
        "CommandPoints": 35,
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "AeroRifles_US": {  # AIR CAV TROOPERS
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Rifles_Cavalry_US": {  # DISMOUNT TROOPERS WIP
        "CommandPoints": 35,
        "availability": [12, 9, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        # "Divisions": {
        #     "remove": ["US_11ACR"],
        # },
        "Salves": {
            "FM_M16": 9,
            "SAW_M249_5_56mm": 30,
            "RocketInf_AT4_83mm": 4,
        },
    },

    "Rifles_US": {  # MECH. RIFLES (DRAGON)
        "GameName": {
            "display": "MECH. RIFLES [DRAGON]",
        },
        "CommandPoints": 45,
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
            },
        },
    },

    "Rifles_LAW_US": {  # MECH. RIFLES (LAW)
        "GameName": {
            "display": "MECH. RIFLES [LAW]",
        },
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Rifles_half_LAW_US": {
        "GameName": {
            "display": "FIRETEAM [LAW]",
        },
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "US_24th_Inf": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 3,
                "Transports": ["M1038_Humvee_US", "M2A1_Bradley_IFV_US", "M2A2_Bradley_IFV_US"],
            },
            "US_8th_Inf": {
                "cards": 2,
            },
        },
        "availability": [12, 9, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Rifles_half_AT4_US": {
        "GameName": {
            "display": "FIRETEAM [AT4]",
        },
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 2,
                "Transports": ["M1038_Humvee_US", "M2A1_Bradley_IFV_US", "M2A2_Bradley_IFV_US"],
            },
        },
        "availability": [12, 9, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "SAW_M249_5_56mm": 30,
                "MMG_WA_M60E3_7_62mm": 18,
                "RocketInf_AT4_83mm": 4,
            },
        },
    },

    "Ranger_US": {
        "CommandPoints": 65,
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    ("Commando_733", "M16A1_Carbine"),
                    ("RocketInf_M72A3_LAW_66mm", "RocketInf_AT4_83mm", "RocketInf_M72_LAW_66mm", "RocketInf_AT4_83mm"),
                ],
            },
            "Salves": {
                "M16A1_Carbine": 11,
                "RocketInf_AT4_83mm": 6,
            },
        },
    },

    "Ranger_Dragon_US": {
        "GameName": {
            "display": "RANGERS [DRAGON]",
        },
        "CommandPoints": 70,
        "availability": [0, 0, 4, 3],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Commando_733", "M16A1_Carbine")],
            },
            "Salves": {
                "M16A1_Carbine": 7,
            },
        },
    },

    "DeltaForce_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Commando_733", "M16A2_Carbine")],
            },
        },
    },

    "Airborne_US": {
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "MMG_inf_M240B_7_62mm": 36,
                "RocketInf_AT4_83mm": 6,
            },
        },
    },

    "Airborne_half_LAW_US": {  # AB FIRETEAM (AT-4)
        "GameName": {
            "display": "AB FIRETEAM [AT4]",
        },
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponAssignment": [
            (0, [1, ]),
            (1, [1, ]),
            (2, [0, ]),
            (3, [0, ]),
            (4, [0, 2, ]),
        ],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 3,
                    "SAW_M249_5_56mm": 2,
                },
            },
            "Salves": {
                "FM_M16": 9,
                "SAW_M249_5_56mm": 30,
                "RocketInf_AT4_83mm": 4,
            },
        },
    },

    "Airborne_half_Dragon_US": {
        "GameName": {
            "display": "AB FIRETEAM [DRAGON]",
        },
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "SAW_M249_5_56mm": 30,
                "M47_DRAGON_II": 4,
            },
        },
    },

    "AeroRifles_AB_US": {
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "AeroRifles_Dragon_US": {
        "GameName": {
            "display": "AERO-RIFLES [DRAGON]",
        },
        "CommandPoints": 40,
        "Divisions": {
            "add": ["US_82nd_Airborne"],
            "is_transported": True,
            "needs_transport": True,
            "US_82nd_Airborne": {
                "cards": 1,
                "Transports": ["UH60A_Black_Hawk_US"],
            },
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "SAW_M249_5_56mm": 30,
                "M47_DRAGON_II": 4,
            },
        },
    },

    "Aero_half_AT4_US": {
        "GameName": {
            "display": "AERO-FIRETEAM [AT4]",
        },
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "SAW_M249_5_56mm": 30,
                "RocketInf_AT4_83mm": 4,
            },
        },
    },

    "AeroRifles_AT4_US": {
        "GameName": {
            "display": "AERO-RIFLES [AT4]",
        },
        "CommandPoints": 65,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "SAW_M249_5_56mm": 30,
                "RocketInf_AT4_83mm": 9,
            },
        },
    },

    "Rifles_half_Dragon_US": {
        "GameName": {
            "display": "FIRETEAM [DRAGON]",
        },
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "US_24th_Inf": {
                "cards": 2,
            },
            "US_3rd_Arm": {
                "cards": 3,
            },
        },
        "availability": [12, 9, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "SAW_M249_5_56mm": 30,
                "MMG_WA_M60E3_7_62mm": 18,
                "M47_DRAGON_II": 4,
            },
        }
    },

    "Rifles_half_LAW_NG_US": {
        "GameName": {
            "display": "NG FIRETEAM [LAW]",
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "Rifles_half_Dragon_NG_US": {
        "GameName": {
            "display": "NG FIRETEAM [DRAGON]",
        },
        "CommandPoints": 30,
        "availability": [15, 12, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
            "Salves": {
                "FM_M16A1": 10,
                "MMG_M60E1_7_62mm": 18,
                "M47_DRAGON": 4,
            },
        }
    },

    "NatGuard_M67_US": {
        "GameName": {
            "display": "NG RIFLES [M67]",
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "NatGuard_LAW_US": {
        "GameName": {
            "display": "NG RIFLES [LAW]",
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "NatGuard_Dragon_US": {
        "GameName": {
            "display": "NG RIFLES [DRAGON]",
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "Aero_half_Dragon_US": {
        "GameName": {
            "display": "AERO-FIRETEAM [DRAGON]",
        },
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "SAW_M249_5_56mm": 30,
                "M47_DRAGON_II": 4,
            },
        }
    },

    "GreenBerets_ODA_US": {
        "GameName": {
            "display": "GREEN BERETS [ODA]",
        },
        "CommandPoints": 85,
        "availability": [0, 0, 0, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16", "M16A1_Carbine")],
            },
            "Salves": {
                "M16A1_Carbine": 9,
                "SAW_M249_5_56mm": 30,
                "Sniper_M21": 10,
                "RocketInf_AT4_83mm": 9,
            },
        }
    },

    "HMGteam_M60_Aero_US": {
        "GameName": {
            "display": "AERO-M60 7.62mm",
        },
    },

    "HMGteam_M60_AB_US": {
        "GameName": {
            "display": "AB M60 7.62mm",
        },
    },

    "HMGteam_M60_NG_US": {
        "GameName": {
            "display": "NG M60 7.62mm",
        },
    },

    "HMGteam_M60_US": {
        "GameName": {
            "display": "M60 7.62mm",
        },
    },

    "HMGteam_M2HB_US": {
        "GameName": {
            "display": "M2HB 12.7mm",
        },
    },

    "HMGteam_M2HB_AB_US": {
        "GameName": {
            "display": "AB M2HB 12.7mm",
        },
    },

    "HMGteam_M2HB_Aero_US": {
        "GameName": {
            "display": "AB M2HB 12.7mm",
        },
    },

    "ATteam_ITOW_US": {
        "CommandPoints": 60,
        "availability": [6, 4, 0, 0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "ATteam_TOW2_US": {
        "CommandPoints": 75,
        "availability": [4, 3, 0, 0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "ATteam_TOW2_Aero_US": {
        "CommandPoints": 75,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 4, 3, 0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "ATteam_TOW2_para_US": {
        "CommandPoints": 75,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 4, 3, 0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "M274_Mule_RCL_US": {
        "CommandPoints": 30,
        "availability": [0, 9, 7, 0],
    },

    "M151_MUTT_trans_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M35_trans_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M998_Humvee_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M1038_Humvee_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    # US ARTILLERY
    "M577_US": {
        "CommandPoints": 60,
        "GameName": {
            "display": "#LDR M577 TACFIRE FCV",
            "token": "ZTSGIUUUVJ",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_M577_US",
                "Unite",
                "Vehicule",
            ],
        },
        "Factory": "EDefaultFactories/Art",
        "IdentifiedTextures": ["Texture_RTS_H_appui", "Texture_appui"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_appui",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Transport",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 2, 0, 0],
        "remove_zone_capture": None,
    },

    "Mortier_107mm_US": {
        "CommandPoints": 40,
        "availability": [5, 4, 3, 0],
    },

    "Mortier_107mm_Airborne_US": {
        "CommandPoints": 40,
        "availability": [0, 5, 4, 3],
    },

    "M125_HOWZ_US": {  # M125 mortar carrier, M29A1 81mm Mortar
        "CommandPoints": 45,
        "availability": [4, 3, 0, 0],
    },
    "Howz_M102_105mm_US": {
        "CommandPoints": 60,
        "availability": [0, 4, 3, 0],
    },

    "M106A2_HOWZ_US": {
        "CommandPoints": 60,
        "availability": [4, 3, 0, 0],
    },

    "M109A2_HOWZ_US": {
        "CommandPoints": 180,
        "availability": [3, 2, 0, 0],
    },

    "M110A2_HOWZ_US": {
        "CommandPoints": 220,
        "availability": [2, 0, 1, 0],
    },

    "M270_MLRS_US": {
        "CommandPoints": 240,
        "availability": [0, 1, 0, 0],
        "Divisions": {
            "remove": ["US_8th_Inf"]
        },
    },

    "M270_MLRS_cluster_US": {
        "GameName": {
            "display": "M270 MLRS",
            # "token": "MYQQNJCCAK",
        },
        "CommandPoints": 300,
        "Divisions": {
            "add": ["US_8th_Inf"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 2,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "AngleRotationMaxPitch": 1.0,
                },
            },
        },
        "availability": [0, 1, 0, 0],
    },

    # US TANK
    "M1A1HA_Abrams_CMD_US": {
        "CommandPoints": 330,
        "GameName": {
            "display": "#LDR M1A1(HA) ABRAMS LDR.",
            "token": "CIOEKZVEAY",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1A1HA_Abrams_CMD_US",
                "Unite",
            ],
        },
        # "SortingOrder": 20340,
        # "UnitAttackValue": 561,
        # "UnitDefenseValue": 561,
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 0, 2],
        "remove_zone_capture": None,
    },

    "M1A1_Abrams_CMD_US": {
        "CommandPoints": 255,
        "GameName": {
            "display": "#LDR M1A1 ABRAMS LDR.",
            "token": "JARUASHKDH",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1A1_Abrams_CMD_US",
                "Unite",
            ],
        },
        # "SortingOrder": 20290,
        # "UnitAttackValue": 461,
        # "UnitDefenseValue": 461,
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 2,  # no other ldr tanks in the div
            },
        },
        "availability": [0, 0, 3, 0],
        "remove_zone_capture": None,
    },

    "M1IP_Abrams_CMD_US": {
        "CommandPoints": 215,
        "GameName": {
            "display": "#LDR M1IP ABRAMS LDR.",
            "token": "TSLINICZXV",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1IP_Abrams_CMD_US",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 2, 0],
        "remove_zone_capture": None,
    },

    "M1_Abrams_CMD_US": {
        "CommandPoints": 185,
        "GameName": {
            "display": "#LDR M1 ABRAMS LDR.",
            "token": "JMIRJBBLPW",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1_Abrams_CMD_US",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 3, 0],
        "remove_zone_capture": None,
    },

    "M60A3_CMD_US": {
        "CommandPoints": 120,
        "GameName": {
            "display": "#LDR M60A3 (TTS) LDR.",
            "token": "OZPDFIGTWN",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M60A3_CMD_US",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'armor',
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },

    "M551A1_TTS_Sheridan_CMD_US": {
        "CommandPoints": 65,
        "GameName": {
            "display": "#LDR M551 TTS SHERIDAN LDR.",
            "token": "NBZRAJWZXD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "M551A1_TTS_Sheridan_CMD_US",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_amphibie',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 0, 4],
        "remove_zone_capture": None,
    },

    "M113A3_US": {
        "CommandPoints": 15,
        "orders": {
            "add_orders": ["sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M113A1_NG_US": {
        "CommandPoints": 15,
        "orders": {
            "add_orders": ["sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M113_Dragon_US": {
        "CommandPoints": 15,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("M47_DRAGON", "M47_DRAGON_II")],
            },
        },
    },

    "M1025_Humvee_TOW_para_US": {
        "GameName": {
            "display": "AB M1025 HUMVEE TOW-2",
        },
        "CommandPoints": 65,
        "stealth": 1.5,
        "availability": [0, 6, 4, 0],
    },

    "M901A1_ITW_US": {  # TOW 2
        "CommandPoints": 65,
        "availability": [8, 6, 0, 0],
    },

    "M901_TOW_US": {  # ITOW
        "CommandPoints": 50,
        "availability": [8, 6, 0, 0],
    },

    "M728_CEV_US": {
        "CommandPoints": 65,
        "availability": [8, 6, 0, 0],
    },

    "M2A1_Bradley_IFV_US": {
        "CommandPoints": 70,
    },

    "M2A2_Bradley_IFV_US": {
        "CommandPoints": 85,
    },

    "M1A1HA_Abrams_US": {
        "CommandPoints": 310,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [0, 0, 3, 2],
    },

    "M1A1_Abrams_US": {
        # "GameName": {
        #     "display": "#3RDARM M1A1 ABRAMS",
        #     "token": "YEMPBPBTNZ",
        # },
        "CommandPoints": 220,
        "Divisions": {
            "remove": ["US_8th_Inf"],
            "default": {
                "cards": 5,
            },
            "US_11ACR": {
                "cards": 4,
            },
        },
        "availability": [5, 3, 0, 0],
    },

    "M1IP_Abrams_US": {
        "CommandPoints": 190,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "US_24th_Inf": {
                "cards": 3,
            },
            "US_101st_Airmobile": {
                "cards": 2,
            },
            "NATO_Garnison_Berlin": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 4, 3],
    },

    "M1_Abrams_US": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [6, 4, 0, 0],
    },

    "M1_Abrams_NG_US": {
        "CommandPoints": 150,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [6, 0, 0, 0],
    },

    "M60A3_Patton_US": {
        "CommandPoints": 105,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [8, 6, 0, 0],
    },

    "M60A3_ERA_Patton_US": {
        "CommandPoints": 110,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [6, 4, 0, 0],
    },

    "M60A3_Patton_NG_US": {
        "CommandPoints": 110,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [10, 7, 0, 0],
    },

    "M60A1_RISE_Passive_US": {
        "CommandPoints": 80,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [10, 8, 0, 0],
    },

    "M551A1_TTS_Sheridan_US": {
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 10, 8, 0],
    },

    # US RECON
    "M151A2_scout_US": {
        "CommandPoints": 25,
    },

    "M113_ACAV_US": {
        "CommandPoints": 35,
    },

    "M1025_Humvee_scout_US": {
        "CommandPoints": 25,
        "ButtonTexture": "M1025_Humvee_HMG_LUX",
        "UpgradeFromUnit": None,
    },

    "M1025_Humvee_AGL_US": {
        "CommandPoints": 30,
    },

    "M1025_Humvee_AGL_nonPara_US": {
        "CommandPoints": 30,
    },

    "M998_Humvee_Delta_US": {
        "UpgradeFromUnit": "M1025_Humvee_AGL_US",
    },

    "M981_FISTV_US": {
        "CommandPoints": 25,
        "GameName": {
            "display": "#RECO3 M981 FISTV",
            "token": "JKFBZFRBYZ",
        },
        # "TagSet": {  # already added - this makes it show twice in the NDF
        #     "add_tags": ['"reco_radar"'],
        # },
        "optics": {
            "OpticalStrength": 233.475
        },
        "availability": [8, 0, 0, 0],
    },

    "M113A1_TOW_US": {
        "CommandPoints": 50,
        "availability": [8, 6, 0, 0],
    },

    "LAV_25_M1047_US_US": {
        "CommandPoints": 70,
        "availability": [0, 4, 3, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_turret_7_62mm_M60": 60,
                "MMG_M240_7_62mm": 48,
            },
            "equipmentchanges": {
                "replace": [("MMG_team_7_62mm_M60", "MMG_turret_7_62mm_M60")],
            },
        },
    },

    "M3A1_Bradley_CFV_US": {
        "CommandPoints": 115,
        "availability": [4, 3, 0, 0],
        "TagSet": {
            "add_tags": ['"Vehicule_Transport_Arme"'],
        },
        "SpecialtiesList": {
            "overwrite_all": [
                'reco',
                '_transport1',
                '_ifv',
                '_smoke_launcher',
            ],
        },
        "orders": {
            "add_orders": ["UnloadFromTransport", "UnloadAtPosition", "LoadUnit"]
        },
        "Divisions": {
            "US_3rd_Arm": {
                "cards": 1,
            },
            "US_8th_Inf": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 1,
            },
        },
        "UpgradeFromUnit": "Cav_Scout_Dragon_M3A1_US",
    },

    "M3A2_Bradley_CFV_US": {
        "CommandPoints": 145,
        "availability": [3, 2, 0, 0],
        "TagSet": {
            "add_tags": ['"Vehicule_Transport_Arme"'],
        },
        "SpecialtiesList": {
            "overwrite_all": [
                'reco',
                '_transport1',
                '_ifv',
                '_smoke_launcher',
            ],
        },
        "orders": {
            "add_orders": ["UnloadFromTransport", "UnloadAtPosition", "LoadUnit"]
        },
        "Divisions": {
            "US_11ACR": {
                "cards": 1,
            },
        },
        "UpgradeFromUnit": "Cav_Scout_Dragon_M3A2_US",
    },

    "M551A1_ACAV_Sheridan_US": {
        "CommandPoints": 50,
        "availability": [0, 4, 3, 0],
    },

    "M1A1_Abrams_reco_US": {
        "availability": [0, 3, 2, 0],
        "CommandPoints": 250,
    },

    "OH58C_Scout_US": {
        "GameName": {
            "display": "#RECO2 OH-58C SCOUT",
        },
        "CommandPoints": 40,
        "availability": [0, 4, 3, 0],
    },

    "OH58D_Combat_Scout_US": {
        "availability": [0, 4, 3, 0],
        "ECM:": -0.1,
    },

    "OH58D_Kiowa_Warrior_US": {
        "GameName": {
            "display": "#RECO3 OH-58D KIOWA WR.",
        },
        "availability": [0, 3, 2, 0],
        "ECM": -0.1,
    },

    "EH60A_EW_US": {
        "Divisions": {
            "add": ["US_3rd_Arm"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 0, 0],
    },

    "Airborne_Scout_US": {
        "CommandPoints": 25,
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
            },
        },
    },

    "Scout_US": {
        "CommandPoints": 20,
        "availability": [8, 6, 0, 0],
        "Divisions": {
            "is_transported": True,
            "needs_transport": False,
            "default": {
                "cards": 3,
                "Transports": [
                    "M151_MUTT_trans_US",
                    "M151A2_scout_US",
                    "M113A3_US",
                    "M113_ACAV_US",
                ],
            },
            "US_11ACR": {
                "cards": 2,
                "Transports": [
                    "M998_Humvee_US",
                    "M1025_Humvee_scout_US",
                    "M1025_Humvee_AGL_nonPara_US",
                    # "M113A3_US",
                    # "M113_ACAV_US",
                ],
            },
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, 2, ]),
            ],
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 11,
                "SAW_M249_5_56mm": 45,
                "add": [(2, 4)], # (salves_index, salves)
            },
            "equipmentchanges": {
                "add": [(2, "RocketInf_M72A3_LAW_66mm")], # (turret, weapon)
                "replace": [
                    ("MMG_inf_M240B_7_62mm", "SAW_M249_5_56mm", "MMG_inf_M240B_7_62mm", "SAW_M249_5_56mm")
                ],
            },
        },
    },

    "HvyScout_NG_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "HvyScout_NG_Dragon_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "LRRP_US": {
        "CommandPoints": 70,
        "availability": [0, 0, 4, 3],
        "Divisions": {
            "default": {
                "Transports": ["M998_Humvee_US", "UH60A_Black_Hawk_US"],
            },
            "US_11ACR": {
                "Transports": [
                    "M998_Humvee_US",
                    "M1025_Humvee_scout_US",
                    "M1025_Humvee_AGL_nonPara_US",
                ],
            },
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    ("Commando_733", "M16A1_Carbine"),
                    ("RocketInf_M72A1_LAW_66mm", "RocketInf_M72A3_LAW_66mm"),
                ],
            },
        },
        "DeploymentShift": 0,
    },

    "Sniper_US": {
        "GameName": {
            "display": "#RECO2 SNIPERS",
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "Divisions": {
            "US_3rd_Arm": {
                "cards": 1,
            },
        },
    },

    # US AA
    "MANPAD_Stinger_C_US": {
        "GameName": {
            "display": "STINGER C",
            "token": "XQYDBWCBAP",
        },
        "CommandPoints": 45,
        "Divisions": {
            "remove": ["US_82nd_Airborne"],
            "default": {
                "cards": 2,
            },
            "NATO_Garnison_Berlin": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 3,
                # "Transports": ["M151_MUTT_trans_US", "M2A1_Bradley_IFV_US"],
            },
            "US_8th_Inf": {
                "cards": 3,
            },
        },
        "availability": [7, 5, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16", "FM_M16_noreflex")],
            },
            "Salves": {
                "FM_M16": 7,
                "MANPAD_FIM92": 6,
            },
        },
    },

    "MANPAD_Stinger_C_Aero_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16", "FM_M16_noreflex")],
            },
        },
    },

    "MANPAD_Stinger_C_para_US": {
        "GameName": {
            "display": "AB STINGER C",
            "token": "VVEXCPXVQB",
        },
        "CommandPoints": 45,
        "availability": [0, 7, 5, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16", "FM_M16_noreflex")],
            },
            "Salves": {
                "FM_M16": 7,
                "MANPAD_FIM92": 6,
            },
        },
    },

    "M163_CS_US": {
        "CommandPoints": 40,
        "availability": [8, 6, 0, 0],
    },

    "M163_PIVADS_US": {
        "CommandPoints": 65,
        "availability": [7, 5, 0, 0],
        # "SpecialtiesList": {
        #     "add_specs": ["'normal_airoptics'"],
        # },
    },

    "DCA_M167_Vulcan_20mm_US": {
        "CommandPoints": 25,
        "Factory": "EDefaultFactories/Logistic",
        "Divisions": {
            "default": {
                "Transports": ["M113A3_US"],
                "cards": 1,
            },
            "US_82nd_Airborne": {
                "Transports": ["M1038_Humvee_US"],
            },
        },
        "availability": [0, 8, 6, 0],
        "max_speed": 4,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "FOB_US",
    },

    "DCA_M167A2_Vulcan_20mm_US": {
        "CommandPoints": 25,
        "Factory": "EDefaultFactories/Logistic",
        "Divisions": {
            "add": ["US_3rd_Arm", "US_8th_Inf"],
            "is_transported": True,
            "needs_transport": True,
            "default": {
                "cards": 1,
                "Transports": ["M113A3_US"],
            },
            # "UK_2nd_Infantry": {
            #     "cards": 1,
            #     "Transports": ["LandRover_UK"],
            # },
        },
        "availability": [6, 4, 0, 0],
        "max_speed": 4,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "FOB_US",
    },

    "M998_Avenger_US": {
        "CommandPoints": 100,
        "availability": [0, 5, 3, 0],
    },

    "M48_Chaparral_MIM72F_US": {
        "optics": {
            "OpticalStrengthAltitude": 220,
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "CommandPoints": 130,
        "availability": [0, 3, 2, 0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "DCA_I_Hawk_US": {
        "CommandPoints": 90,
        "optics": {
            "OpticalStrengthAltitude": 300,
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "availability": [4, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    # US HELI
    "UH60A_Black_Hawk_US": {
        "CommandPoints": 60,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M240d_7_62mm": 60,
                "special": {
                    "MMG_M240d_7_62mm": (0, 60),
                },
            },
        },
    },

    "CH47_Chinook_US": {
        "CommandPoints": 60,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "AH6C_Little_Bird_US": {
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 0, 6],
    },

    "AH6G_Little_Bird_US": {
        "CommandPoints": 60,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 0, 4],
    },

    "OH58_CS_US": {
        "CommandPoints": 75,
        "availability": [0, 4, 3, 0],
    },

    "MH_60A_DAP_US": {
        "CommandPoints": 120,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 0, 3],
    },

    "AH1F_ATAS_US": {
        "CommandPoints": 130,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 3, 2, 0],
    },
    
    "AH1F_CNITE_US": { # 10% ECM, 4x TOW-2, 38x Hydra
        "CommandPoints": 135,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "US_11ACR": {
                "cards": 3,
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "AH1F_Cobra_US": {
        "CommandPoints": 120,
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "US_101st_Airmobile": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 1,
            },
        },
        "availability": [0, 4, 3, 0],
    },

    "AH1S_Cobra_US": {
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "US_3rd_Arm": {
                "cards": 2,
            },
            "US_82nd_Airborne": {
                "cards": 1,
            },
            "US_101st_Airmobile": {
                "cards": 1,
            },
        },
        "availability": [0, 4, 3, 0],
    },

    "AH1F_Hog_US": { # 76x Hydra
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 2,
            },
            "US_8th_Inf": {
                "cards": 2,
            },
            "US_11ACR": {
                "cards": 2,
            },
        },
        "availability": [0, 4, 3, 0],
    },

    "AH1F_HeavyHog_US": {
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 4, 3, 0],
    },

    "AH64_Apache_US": {  # 8x Hellfire / Hydra
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "AH64_Apache_emp1_US": {  # 16x Hellfire
        "GameName": {
            "display": "AH-64A APACHE [AT]",
        },
        "CommandPoints": 215,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 3,
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "AH64_Apache_emp2_US": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 3,
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "AH64_Apache_ATAS_US": {
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 2, 0, 1],
    },

    # US AIR
    "F4E_Phantom_II_AA_US": {
        "CommandPoints": 165,
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 3, 2, 0],
    },

    "F15C_Eagle_AA_US": {
        "CommandPoints": 290,
        "ECM": -0.45,
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1375,
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "F4_Wild_Weasel_US": {
        "CommandPoints": 190,
        "optics": {
            "SpecializedOpticalStrengths": {
                "EVisionUnitType/AntiRadar": 1850.0,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "F4E_Phantom_II_HE_US": {
        "CommandPoints": 165,
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 2, 0, 0],
    },


    "F4E_Phantom_II_CBU_US": {
        "CommandPoints": 165,
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 2, 0, 0],
    },

    "F4E_Phantom_II_napalm_US": {
        "CommandPoints": 165,
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 3, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    (
                        "Bomb_Mk77_340kg_Napalm_salvolength2", "Bomb_Mk77_340kg_Napalm_salvolength5",
                        "Bomb_Mk77_340kg_Napalm_x2", "Bomb_Mk77_340kg_Napalm_x4"
                    ),
                ],
            },
        },
    },

    "F111E_Aardvark_US": {  # 12x mk82, 3rd Armored
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "F111F_Aardvark_US": {
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
        "UpgradeFromUnit": "F111F_Aardvark_LGB2_US",
    },

    "F111F_Aardvark_LGB_US": {  # 4x GBU-12
        "CommandPoints": 210,
    },

    "F111E_Aardvark_CBU_US": {  # 8x Mk-20 Rockeye, 3rd Armored
        "CommandPoints": 190,
        "Divisions": {
            "add": ["US_11ACR"],
            "default": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "F111F_Aardvark_CBU_US": {  # 8x Mk-20 Rockeye, 82nd Airborne
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "F111E_Aardvark_napalm_US": {  # 4x Mk-77 napalm, 3rd Armored
        "CommandPoints": 190,
        "Divisions": {
            "add": ["US_11ACR"],
            "default": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 3, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    (
                        "Bomb_Mk77_340kg_Napalm_salvolength4", "Bomb_Mk77_340kg_Napalm_salvolength8",
                        "Bomb_Mk77_340kg_Napalm_x4", "Bomb_Mk77_340kg_Napalm_x6"
                    ),
                ],
            },
        },
    },

    "F111F_Aardvark_napalm_US": {  # 4x Mk-77 napalm, 82nd Airborne
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 3, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    (
                        "Bomb_Mk77_340kg_Napalm_salvolength4", "Bomb_Mk77_340kg_Napalm_salvolength8",
                        "Bomb_Mk77_340kg_Napalm_x4", "Bomb_Mk77_340kg_Napalm_x6"
                    ),
                ],
            },
        },
    },

    "EF111_Raven_US": {
        "CommandPoints": 180,
        "max_speed": 1400,
        "availability": [0, 0, 2, 0],
    },

    "F16C_LGB_US": {
        "CommandPoints": 225,
        "ECM": -0.35,
        "WeaponDescriptor": {
            "Salves": {
                "Bomb_GBU_12_salvolength2": 1,
            },
            "equipmentchanges": {
                "replace": [("Bomb_GBU_12", "Bomb_GBU_12_salvolength2", "Bomb_GBU_12_x1", "Bomb_GBU_12_x2")],
            },
        },
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 1, 0, 0],
        "UpgradeFromUnit": "F16E_TER_HE_US",
    },

    "F16E_AGM_US": {  # 4x AGM-65D, 2x AIM-9M
        "CommandPoints": 200,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 2, 0, 0],
    },

    "F16E_HE_US": {
        "CommandPoints": 200,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 2, 0, 0],
    },

    "F16E_TER_HE_US": {  # 12x mk82 + , 11 ACR
        "CommandPoints": 225,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 2, 0, 0],
    },

    "F16E_napalm_US": {
        "CommandPoints": 200,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    (
                        "Bomb_Mk77_340kg_Napalm_salvolength2", "Bomb_Mk77_340kg_Napalm_salvolength4",
                        "Bomb_Mk77_340kg_Napalm_x2", "Bomb_Mk77_340kg_Napalm_x4"
                    ),
                ],
            },
        },
    },

    "F16E_SEAD_US": {
        "CommandPoints": 220,
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "WeaponDescriptor": {
            "turrets": {
                2: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "F16E_CBU_US": {
        "CommandPoints": 200,
        "Divisions": {
            "remove": ["US_11ACR"],
            "default": {
                "cards": 1,
            },
            "US_8th_Inf": {
                "cards": 2,
            },
        },
        "ECM": -0.35,
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 2, 0, 0],
    },

    "F16E_AA_US": {
        "CommandPoints": 220,
        "ECM": -0.35,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_8th_Inf": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 2,
            },
        },
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 0, 2, 0],
        "UpgradeFromUnit": None,
    },

    "F16E_AA2_US": {  # 3x + 3x AIM-9M
        "CommandPoints": 180,
        "Divisions": {
            "remove": ["US_11ACR"],
            "add": ["US_8th_Inf"],
            "default": {
                "cards": 1,
            },
        },
        "ECM": -0.35,
        "optics": {
            "OpticalStrengthAltitude": 375,
        },
        "availability": [0, 3, 2, 0],
        "UpgradeFromUnit": "F16E_AA_US",
    },

    "A10_Thunderbolt_II_US": {  # 8x mk.82, 2x AIM-9M
        "CommandPoints": 220,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 500,
            },
        },
        "max_speed": 500,
        "availability": [0, 2, 0, 0],
    },

    "A10_Thunderbolt_II_Rkt_US": {  # 76x Hydra, 2x AIM-9M
        "CommandPoints": 220,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 500,
            },
        },
        "max_speed": 500,
        "availability": [0, 2, 0, 0],
    },

    "A10_Thunderbolt_II_ATGM_US": {  # 76x Hydra, 2x AIM-9M
        "CommandPoints": 240,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 500,
            },
        },
        "max_speed": 500,
        "availability": [0, 2, 0, 0],
    },
}
