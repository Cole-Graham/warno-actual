"""USA unit edits."""

# from typing import Any, Dict

# fmt: off
usa_unit_edits = {
    # Infantry armor reference
    "Infantry_armor_reference": {
        "armor": {
            "front": (None, "ResistanceFamily_infanterieWA"),
            "sides": (None, "ResistanceFamily_infanterieWA"),
            "rear": (None, "ResistanceFamily_infanterieWA"),
            "top": (None, "ResistanceFamily_infanterieWA"),
        },
    },
    
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
        "availability": [0, 4, 0, 0],
        "SpecialtiesList": {
            "remove_specs": ["'_para'"],
        },
        "ButtonTexture": "M1025_Humvee_CMD_US",
        "DeploymentShift": 0,
    },

    "M1025_Humvee_CMD_US": {
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
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
        "CommandPoints": 195,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    ("AutoCanon_AP_25mm_M242_Bushmaster_Late", "AutoCanon_AP_25mm_M242_Bushmaster_APDS"),
                    ("AutoCanon_HE_25mm_M242_Bushmaster_Late", "AutoCanon_HE_25mm_M242_Bushmaster_APDS"),
                ],
            },
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 3, 0],
        "UpgradeFromUnit": "M577_CMD2_US",
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M240_7_62mm": 48,
            },
        },
    },

    "M2A2_Bradley_Leader_US": {
        "CommandPoints": 195,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 0, 2],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M240_7_62mm": 48,
            },
        },
    },

    # US INF
    "Rifles_half_CMD_US": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
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
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
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
        "remove_zone_capture": None,
    },

    "Rifles_CMD_US": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
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
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
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
        "remove_zone_capture": None,
    },

    "NatGuard_CMD_US": {
        "armor": "Infantry_armor_reference",
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "Engineer_CMD_US": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
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
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
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
        "WeaponDescriptor": {
            "Salves": {
                "insert": [(2, 8)], # (salves_index, salves)
            },
            "equipmentchanges": {
                "insert": [(2, "RocketInf_M72A3_LAW_66mm")], # (turret, weapon)
                "insert_edits": {
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "SalvoStockIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
            },
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "remove_zone_capture": None,
    },

    "Rangers_CMD_US": {
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
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
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry_sf", "Texture_sf"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
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
        "remove_zone_capture": None,
    },

    "Airborne_Engineer_CMD_US": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
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
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_choc',
                '_para',
                'infantry_equip_medium',
            ],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 10,
                    "MMG_inf_M240B_7_62mm": 2,
                },
            },
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "remove_zone_capture": None,
    },

    "Airborne_CMD_US": {
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
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
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
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
                "FM_M16": 11,
                "RocketInf_AT4_83mm": 8,
            },
        },
        "remove_zone_capture": None,
    },

    "AeroRifles_CMD_US": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
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
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "remove_zone_capture": None,
    },

    "Aero_half_CMD_US": { # Not in use (redundant with AB FIRETEAM units)
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
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
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "strength": 4,
        "remove_zone_capture": None,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 3,
                },
            },
        },
    },

    "AeroEngineer_CMD_US": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
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
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_choc',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "remove_zone_capture": None,
    },

    "GreenBerets_CMD_US": {
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
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
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_sf',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Commando_733", "M16A1_Carbine")],
            },
            "Salves": {
                "M16A1_Carbine": 11,
            },
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 0, 3],
        "max_speed": 26,
        "remove_zone_capture": None,
    },
    
    "MP_CMD_US": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR MP LEADER",
            "token": "LLUPBPNLWT",
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
                "UNITE_MP_CMD_US",
                "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_mp',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "remove_zone_capture": None,
    },

    "Engineers_US": {
        "CommandPoints": 50,
        "GameName": {
            "display": "ENGINEERS",
        },
        "armor": "Infantry_armor_reference",
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
        "UpgradeFromUnit": "Engineers_Flash_US",
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_WA_M60E3_7_62mm": False,
                },
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
        "armor": "Infantry_armor_reference",
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
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 8,
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
        "GameName": {
            "display": "AIRBORNE ENGINEERS",
        },
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 8,
                    "MMG_inf_M240B_7_62mm": 2,
                },
            },
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
        "armor": "Infantry_armor_reference",
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
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 11,
                "RocketInf_M202_Flash_66mm": 2,
            },
        },
    },

    "Airborne_Engineers_Flash_US": {
        "GameName": {
            "display": "AB ENGINEERS [FLASH]",
        },
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 26,
        "strength": 6,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                # AnimateOnlyOneSoldier (False when quantity of a given small arm weapon is > 1)
                "animate": {
                    "SAW_M249_5_56mm": False,
                },
                "replace": [("MMG_inf_M240B_7_62mm", "SAW_M249_5_56mm")],
                "quantity": {
                    "SAW_M249_5_56mm": 2,
                },
            },
            "Salves": {
                "SAW_M249_5_56mm": 23,
            },
        },
    },

    "NatGuard_Engineers_Flam_US": {
        "GameName": {
            "display": "N.G. ENGINEERS [FLAM]",
        },
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [6, 0, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
            "Salves": {
                "flamethrower_M2": 15,
            },
        },
    },

    "NatGuard_Engineers_M67_US": {
        "GameName": {
            "display": "N.G. ENGINEERS [M67]",
        },
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [6, 0, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_M67_RCL_90mm": 8,
            },
        },
    },

    "Engineers_Dragon_US": {
        "GameName": {
            "display": "ENGINEERS [DRAGON]",
        },
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
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
                "FM_M16": 11,
                "M47_DRAGON": 8,
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
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Airborne_MP_US": {
        "GameName": {
            "display": "AIRBORNE MP PATROL",
        },
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [0, 12, 9, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "MP_US": {
        "GameName": {
            "display": "MP PATROL",
        },
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [0, 12, 9, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 3,
                    "MMG_WA_M60E3_7_62mm": 2,
                },
            },
            "Salves": {
                "FM_M16": 11,
            },
        },
    },

    "Airborne_MP_RCL_US": {
        "GameName": {
            "display": "AB MP PATROL [M67]",
        },
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [0, 9, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 11,
            },
        },
    },

    "MP_RCL_US": {
        "GameName": {
            "display": "MP PATROL [M67]",
        },
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [0, 9, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 11,
                "RocketInf_M67_RCL_90mm": 8,
            },
        },
    },
    
    "MP_Combat_USAF_US": { # USAF SECURITY
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [0, 8, 6, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "MP_Patrol_USAF_US": { # USAF SECURITY PATROL
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "availability": [0, 7, 5, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "MANPAD_FIM92_A": 6,
            },
        },
    },
    
    "Security_USMC_US": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [0, 8, 6, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
    },
    
    "LightRifles_LAW_US": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "LightRifles_Viper_US": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "LightRifles_RCL_US": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 7,
                    "SAW_M249_5_56mm": 2,
                },
            },
            "Salves": {
                "RocketInf_AT4_83mm": 6,
            },
        },
    },
    
    "LightRifles_AT4_US": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "LightRifles_Dragon_US": {
        "CommandPoints": 45,
        "GameName": {
            "display": "LIGHT RIFLES [DRAGON]",
        },
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Rifles_HMG_US": { # GUNNERS
        "GameName": {
            "display": "GUNNERS",
        },
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Airborne_HMG_US": {  # AIRBORNE GUNNERS
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "AeroRifles_US": {  # AIR CAV TROOPERS
        "GameName": {
            "display": "AIR CAV TROOPERS",
        },
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Rifles_Cavalry_US": {  # DISMOUNT TROOPERS WIP
        "GameName": {
            "display": "DISMOUNT. TROOPERS",
        },
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [12, 9, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        # "Divisions": {
        #     "remove": ["US_11ACR"],
        # },
        "Salves": {
            "FM_M16": 11,
            "SAW_M249_5_56mm": 30,
            "RocketInf_AT4_83mm": 4,
        },
    },

    "Rifles_US": {  # MECH. RIFLES (DRAGON)
        "GameName": {
            "display": "MECH. RIFLES [DRAGON]",
        },
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 11,
            },
        },
    },

    "Rifles_LAW_US": {  # MECH. RIFLES (LAW)
        "GameName": {
            "display": "MECH. RIFLES [LAW]",
        },
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_inf_M240B_7_62mm": False,
                },
                "quantity": {
                    "FM_M16": 6,
                    "MMG_inf_M240B_7_62mm": 2,
                },
            },
        },
    },

    "Rifles_half_LAW_US": {
        "GameName": {
            "display": "FIRETEAM [LAW]",
        },
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
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
        "armor": "Infantry_armor_reference",
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
            "equipmentchanges": {
                "replace": [
                    ("MMG_WA_M60E3_7_62mm", "MMG_inf_M240B_7_62mm", "MMG_M60_7_62mm", "MMG_inf_M240B_7_62mm"),
                ]
            },
            "Salves": {
                "FM_M16": 11,
                "SAW_M249_5_56mm": 30,
                "MMG_inf_M240B_7_62mm": 36,
                "RocketInf_AT4_83mm": 4,
            },
        },
    },

    "Ranger_US": {
        "GameName": {
            "display": "RANGERS",
        },
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
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
        "CommandPoints": 65,
        "armor": "Infantry_armor_reference",
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
                "M16A1_Carbine": 11,
            },
        },
    },

    "DeltaForce_US": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Commando_733", "M16A2_Carbine")],
            },
            "Salves": {
                "M16A2_Carbine": 11,
            },
        },
    },

    "Airborne_US": {
        "GameName": {
            "display": "AIRBORNE",
        },
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
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
                "FM_M16": 11,
                "MMG_inf_M240B_7_62mm": 36,
                "RocketInf_AT4_83mm": 6,
            },
        },
    },

    "Airborne_half_LAW_US": {  # AB FIRETEAM (AT-4)
        "GameName": {
            "display": "AB FIRETEAM [AT4]",
        },
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 26,
        "strength": 6,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_M249_5_56mm": False,
                },
                "quantity": {
                    "FM_M16": 4,
                    "SAW_M249_5_56mm": 2,
                },
            },
            "Salves": {
                "FM_M16": 11,
                "SAW_M249_5_56mm": 23,
                "RocketInf_AT4_83mm": 4,
            },
        },
    },

    "Airborne_half_Dragon_US": {
        "GameName": {
            "display": "AB FIRETEAM [DRAGON]",
        },
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 20,
        "strength": 6,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_inf_M240B_7_62mm": False,
                },
                "replace": [
                    ("SAW_M249_5_56mm", "MMG_inf_M240B_7_62mm", "SAW_M249_5_56mm", "MMG_inf_M240B_7_62mm")
                ],
                "quantity": {
                    "MMG_inf_M240B_7_62mm": 2,
                },
            },
            "Salves": {
                "MMG_inf_M240B_7_62mm": 36,
                "M47_DRAGON_II": 4,
            },
        },
    },

    "AeroRifles_AB_US": {
        "GameName": {
            "display": "AERO-RIFLES",
        },
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
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
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
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
        "strength": 10,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 8,
                },
            },
            "Salves": {
                "FM_M16": 11,
                "SAW_M249_5_56mm": 23,
                "M47_DRAGON_II": 8,
            },
        },
    },

    "Aero_half_AT4_US": { # Not in use (redundant with AB FIRETEAM units)
        "GameName": {
            "display": "AERO-FIRETEAM [AT4]",
        },
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
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
                "FM_M16": 11,
                "SAW_M249_5_56mm": 30,
                "RocketInf_AT4_83mm": 4,
            },
        },
    },

    "AeroRifles_AT4_US": {
        "GameName": {
            "display": "AERO-RIFLES [AT4]",
        },
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 11,
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
        "armor": "Infantry_armor_reference",
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
                "FM_M16": 11,
                "SAW_M249_5_56mm": 30,
                "MMG_WA_M60E3_7_62mm": 30,
                "M47_DRAGON_II": 4,
            },
        }
    },

    "Rifles_half_LAW_NG_US": {
        "CommandPoints": 20,
        "GameName": {
            "display": "N.G. FIRETEAM [LAW]",
        },
        "armor": "Infantry_armor_reference",
        "availability": [12, 0, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "Rifles_half_Dragon_NG_US": {
        "CommandPoints": 25,
        "GameName": {
            "display": "N.G. FIRETEAM [DRAGON]",
        },
        "armor": "Infantry_armor_reference",
        "availability": [12, 0, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
            "Salves": {
                "M47_DRAGON": 4,
            },
        }
    },
    
    "NatGuard_LAW_US": {
        "CommandPoints": 30,
        "GameName": {
            "display": "N.G. RIFLES [LAW]",
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [12, 0, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "NatGuard_M67_US": {
        "CommandPoints": 35,
        "GameName": {
            "display": "N.G. RIFLES [M67]",
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "availability": [12, 0, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_M60E1_7_62mm": False,
                },
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
                "quantity": {
                    "FM_M16A1": 7,
                    "MMG_M60E1_7_62mm": 2,
                },
            },
        },
    },

    "NatGuard_Dragon_US": {
        "CommandPoints": 35,
        "GameName": {
            "display": "N.G. RIFLES [DRAGON]",
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "availability": [12, 0, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    ("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm"),
                    ("M47_DRAGON_II", "M47_DRAGON")
                ],
            },
        },
    },

    "Aero_half_Dragon_US": { # Not in use (redundant with AB FIRETEAM units)
        "GameName": {
            "display": "AERO-FIRETEAM [DRAGON]",
        },
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
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
                "FM_M16": 11,
                "SAW_M249_5_56mm": 30,
                "M47_DRAGON_II": 4,
            },
        }
    },
    
    "Groupe_AT_US": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [10, 7, 0, 0],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "SAW_M249_5_56mm")],
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AnimateOnlyOneSoldier": True,
                        "NbWeapons": 1,
                        "SalvoStockIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "SalvoStockIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                    3: {
                        "turret_edits": {
                            "YulBoneOrdinal": 4,
                        },
                        "SalvoStockIndex": 3,
                        "HandheldEquipmentKey": "'WeaponAlternative_4'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_4'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_4'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_4"],
                    },
                },
                "quantity": {
                    "FM_M16": 6,
                },
            },
            "Salves": {
                "insert": [(1, 23)],
            },
        },
    },
    
    "Navy_SEAL_US": {
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [0, 0, 8, 6],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    ("Commando_733", "M16A2_Carbine"),
                    ("MMG_M60E3_7_62mm", "MMG_WA_M60E3_7_62mm")
                ],
            },
            "Salves": {
                "M16A2_Carbine": 11,
                "Grenade_Satchel_Charge": 5,
            },
        },
    },
    
    "GreenBerets_US": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [0, 0, 8, 6],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Commando_733", "M16A1_Carbine")],
            },
            "Salves": {
                "M16A1_Carbine": 11,
            },
        },
        "UpgradeFromUnit": "GreenBerets_CMD_US",
    },

    "GreenBerets_ODA_US": {
        "GameName": {
            "display": "GREEN BERETS [ODA]",
        },
        "CommandPoints": 75,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 0, 3],
        "max_speed": 26,
        "armor": "Infantry_armor_reference",
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16", "M16A1_Carbine")],
            },
            "Salves": {
                "M16A1_Carbine": 11,
                "SAW_M249_5_56mm": 30,
                "Sniper_M21": 10,
                "RocketInf_AT4_83mm": 9,
            },
        }
    },

    "HMGteam_M60_Aero_US": {
        "CommandPoints": "HMGteam_M60_US",
        "GameName": {
            "display": "AERO-M60 7.62mm",
        },
        "strength": "HMGteam_M60_US",
        "max_speed": "HMGteam_M60_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_US",
        },
    },

    "HMGteam_M60_AB_US": {
        "is_standard": (True, "Para_7_62mm_MMG_Team"), 
        "CommandPoints": 15,
        "GameName": {
            "display": "AB M60 7.62mm",
        },
        "strength": 4,
        "max_speed": 26, 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "HMGteam_M60_NG_US": {
        "is_standard": (True, "Reservist_7_62mm_MMG_Team"), 
        "CommandPoints": 15,
        "GameName": {
            "display": "NG M60 7.62mm",
        },
        "strength": 4,
        "max_speed": 26, 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "HMGteam_M60_US": {
        "is_standard": (True, "7_62mm_MMG_Team"), 
        "CommandPoints": 15,
        "GameName": {
            "display": "M60 7.62mm",
        },
        "strength": 4,
        "max_speed": 26, 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "HMGteam_M2HB_US": {
        "is_standard": (True, "12_7mm_HMG_Team"), 
        "CommandPoints": 25,
        "GameName": {
            "display": "M2HB 12.7mm",
        },
        "strength": 5,
        "max_speed": 14, 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },
    
    "HMGteam_M2HB_NG_US": {
        "is_standard": (True, "Reservist_12_7mm_HMG_Team"), 
        "CommandPoints": 25,
        "strength": 5,
        "max_speed": 14, 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "HMGteam_M2HB_Aero_US": {
        "CommandPoints": "HMGteam_M2HB_US",
        "GameName": {
            "display": "AB M2HB 12.7mm",
        },
        "strength": "HMGteam_M2HB_US",
        "max_speed": "HMGteam_M2HB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_US",
        },
    },
    
    "HMGteam_M2HB_AB_US": {
        "is_standard": (True, "Para_12_7mm_HMG_Team"), 
        "CommandPoints": 25,
        "GameName": {
            "display": "AB M2HB 12.7mm",
        },
        "strength": 5,
        "max_speed": 14, 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },
    
    "HMGteam_Mk19_US": {
        "GameName": {
            "display": "Mk.19 40mm",
        },
        "is_standard": (True, "40mm_Mk19_Team"), 
        "CommandPoints": 30,
        "strength": 5,
        "max_speed": 14, 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "UpgradeFromUnit": "HMGteam_M2HB_US",
    },
    
    "HMGteam_Mk19_AB_US": {
        "GameName": {
            "display": "AB Mk.19 40mm",
        },
        "is_standard": (True, "Para_40mm_Mk19_Team"), 
        "CommandPoints": 30,
        "strength": 5,
        "max_speed": 14, 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "UpgradeFromUnit": "HMGteam_M2HB_AB_US",
    },
    
    "ATteam_RCL_M40A1_NG_US": {
        "CommandPoints": 35,
        "strength": 5,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "availability": [10, 0, 0, 0],
    },
    
    "ATteam_TOW_US": {
        "CommandPoints": 35,
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "availability": [9, 0, 0, 0],
    },

    "ATteam_ITOW_US": {
        "GameName": {
            "display": "I-TOW",
        },
        "CommandPoints": 50,
        "availability": [6, 4, 0, 0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "ATteam_TOW2_US": {
        "GameName": {
            "display": "TOW-2",
        },
        "CommandPoints": 65,
        "availability": [4, 3, 0, 0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },
    
    "ATteam_TOW2A_US": {
        "CommandPoints": 75,
        "availability": [4, 3, 0, 0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "UpgradeFromUnit": "ATteam_TOW2_US",
    },

    "ATteam_TOW2_Aero_US": {
        "GameName": {
            "display": "AERO TOW-2",
        },
        "CommandPoints": 65,
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
        "GameName": {
            "display": "AB TOW-2",
        },
        "CommandPoints": 65,
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
        "availability": [0, 12, 9, 0],
    },
    
    "M151C_RCL_NG_US": {
        "CommandPoints": 25,
        "availability": [12, 0, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_M40A1_RCL_106mm": 16,
            },
        },
    },
    
    "Gama_Goat_trans_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "M151_MUTT_trans_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "CUCV_trans_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "CUCV_MP_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "CUCV_HMG_US": {
        "CommandPoints": 15,
    },
    
    "CUCV_AGL_US": {
        "CommandPoints": 20,
    },

    "M35_trans_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "M998_Humvee_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "M1025_Humvee_MP_US": {
        "CommandPoints": 20,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "CGage_Peacekeeper_US": {
        "CommandPoints": 20,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "M1038_Humvee_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "M998_Humvee_HMG_US": {
        "CommandPoints": 15,
    },
    
    "M998_Humvee_AGL_US": {
        "CommandPoints": 20,
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
        "Factory": "EFactory/Art",
        "IdentifiedTextures": ["Texture_RTS_H_appui", "Texture_appui"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "_leader",
        "SpecialtiesList": {
            "overwrite_all": [],
        },
        "MenuIconTexture": "Texture_RTS_H_appui",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Transport",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 0, 0],
        "remove_zone_capture": None,
    },
    
    "Mortier_M29_81mm_US": {
        "CommandPoints": 30,
        "availability": [6, 5, 4, 0],
    },
    
    "81mm_mortar_Aero_US": {
        "CommandPoints": 35,
        "availability": [0, 6, 5, 4],
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
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 35,
            },
        },
    },
    
    "Howz_M102_105mm_US": {
        "CommandPoints": 60,
        "availability": [0, 4, 3, 0],
    },
    
    "Howz_M119_105mm_US": {
        "CommandPoints": 60,
        "availability": [4, 3, 0, 0],
    },
    
    "Howz_M198_155mm_US": {
        "CommandPoints": 110,
        "availability": [3, 2, 0, 0],
    },
    
    "Howz_M198_155mm_Copperhead_US": {
        "CommandPoints": 135,
        "availability": [3, 2, 0, 0],
    },

    "M106A2_HOWZ_US": { # M106A2 mortar carrier, 107mm M30 Mortar
        "CommandPoints": 60,
        "availability": [4, 3, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 35,
            },
        },
    },

    "M109A2_HOWZ_US": {
        "CommandPoints": 180,
        "availability": [3, 2, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 35,
            },
        },
    },

    "M110A2_HOWZ_US": {
        "CommandPoints": 220,
        "availability": [2, 0, 1, 0]
    },
    
    "M60A1_AVLM_US": {
        "CommandPoints": 70,
        "availability": [3, 2, 0, 0],
    },
    
    "MLRS_XM477_Slammer_US": {
        "CommandPoints": 95,
        "availability": [0, 4, 3, 0],
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
                0: {
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
        "UnitRole": "armor",
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
        "UnitRole": "armor",
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
        "UnitRole": "armor",
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
        "UnitRole": "armor",
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
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },
    
    "M60A1_RISE_Passive_CMD_US": {
        "CommandPoints": 95,
        "GameName": {
            "display": "#LDR M60A1 RISE LDR.",
            "token": "ETJTTJZGYR",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M60A1_RISE_Passive_CMD_US",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
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
                "UNITE_M551A1_TTS_Sheridan_CMD_US",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_amphibie',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 0, 4],
        "remove_zone_capture": None,
    },

    "M113A3_US": {
        "CommandPoints": 15,
        "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "M113A1_NG_US": {
        "CommandPoints": 15,
        "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M113_Dragon_US": {
        "CommandPoints": 15,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("M47_DRAGON_Bipied", "M47_DRAGON_II")],
            },
        },
    },
    
    "M151A2_TOW_NG_US": { # N.G. M151A2 I-TOW
        "CommandPoints": 40,
        "availability": [10, 0, 0, 0],
    },
    
    "M1025_Humvee_TOW_US": {
        "GameName": {
            "display": "M1025 HUMVEE TOW-2",
        },
        "CommandPoints": 65,
        "stealth": 1.5,
        "availability": [0, 6, 4, 0],
    },

    "M1025_Humvee_TOW_para_US": {
        "GameName": {
            "display": "AB M1025 HUMVEE TOW-2",
        },
        "CommandPoints": 65,
        "stealth": 1.5,
        "availability": [0, 6, 4, 0],
    },
    
    "CUCV_Hellfire_US": {
        "CommandPoints": 120,
        "availability": [0, 4, 3, 0],
    },

    "M901A1_ITW_US": {  # TOW 2
        "CommandPoints": 65,
        "availability": [8, 6, 0, 0],
        "UpgradeFromUnit": "M901_TOW_US",
    },

    "M901_TOW_US": {  # ITOW
        "CommandPoints": 50,
        "availability": [8, 6, 0, 0],
    },
    
    "M113A2_TOW_US": { # N.G. M150A2 TOW-2
        "CommandPoints": 50,
        "availability": [8, 6, 0, 0],
    },

    "M728_CEV_US": {
        "CommandPoints": 65,
        "availability": [8, 6, 0, 0],
    },
    
    "M2_Bradley_IFV_NG_US": {
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    ("AutoCanon_AP_25mm_M242_Bushmaster_Late", "AutoCanon_AP_25mm_M242_Bushmaster_APDS"),
                    ("AutoCanon_HE_25mm_M242_Bushmaster_Late", "AutoCanon_HE_25mm_M242_Bushmaster_APDS"),
                ],
            },
        },
    },

    "M2A1_Bradley_IFV_US": {
        "CommandPoints": 65,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    ("AutoCanon_AP_25mm_M242_Bushmaster_Late", "AutoCanon_AP_25mm_M242_Bushmaster_APDS"),
                    ("AutoCanon_HE_25mm_M242_Bushmaster_Late", "AutoCanon_HE_25mm_M242_Bushmaster_APDS"),
                ],
            },
            "Salves": {
                "MMG_M240_7_62mm": 48,
            },
        },
    },

    "M2A2_Bradley_IFV_US": {
        "CommandPoints": 85,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M240_7_62mm": 48,
            },
        },
    },

    "M1A1HA_Abrams_US": {
        "CommandPoints": 310,
        "Divisions": {
            "default": {
                "cards": 2,
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
        "UpgradeFromUnit": "M60A3_Patton_NG_US",
    },

    "M60A3_ERA_Patton_US": {
        "CommandPoints": 120,
        "GameName": {
            "display": "M60A3 (TTS) ERA",
        },
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SpecialtiesList": {
            "overwrite_all": [
                '_smoke_launcher',
                '_era',
            ],
        },
        "capacities": {
            "remove_capacities": ["reserviste"],
        },
        "availability": [0, 8, 6, 0],
        "UpgradeFromUnit": "M60A3_Patton_US",
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
        "availability": [10, 7, 0, 0],
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
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 25,
            },
        },
    },
    
    "M113A1_ACAV_NG_US": {
        "CommandPoints": 25,
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 35,
            },
        },
    },

    "M113_ACAV_US": {
        "CommandPoints": 35,
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 35,
            },
        },
    },

    "M1025_Humvee_scout_US": {
        "CommandPoints": 25,
        "ButtonTexture": "M1025_Humvee_HMG_LUX",
        "UpgradeFromUnit": None,
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 35,
            },
        },
    },

    "M1025_Humvee_AGL_US": {
        "CommandPoints": 30,
    },

    "M1025_Humvee_AGL_nonPara_US": {
        "CommandPoints": 30,
    },

    "M998_Humvee_Delta_US": {
        "CommandPoints": 30,
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
            "OpticalStrengths": {
                "EOpticalStrength/Standard": 233.475,
                "EOpticalStrength/LowAltitude": 233.475,
            },
        },
        "availability": [8, 0, 0, 0],
    },
    
    "M1025_Humvee_GVLLD_US": {
        "CommandPoints": 30,
        "availability": [8, 0, 0, 0],
    },

    "M113A1_TOW_US": {
        "CommandPoints": 50,
        "availability": [8, 6, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 35,
            },
        },
    },
    
    "FAV_HMG_US": {
        "CommandPoints": 30,
        "availability": [12, 9, 0, 0],
    },
    
    "FAV_AGL_US": {
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
    },
    
    "FAV_TOW_US": {
        "CommandPoints": 75,
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
        "CommandPoints": 105,
        "availability": [4, 3, 0, 0],
        "TagSet": {
            "add_tags": ['"Vehicule_Transport_Arme"'],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    ("AutoCanon_AP_25mm_M242_Bushmaster_Late", "AutoCanon_AP_25mm_M242_Bushmaster_APDS"),
                    ("AutoCanon_HE_25mm_M242_Bushmaster_Late", "AutoCanon_HE_25mm_M242_Bushmaster_APDS"),
                ],
            },
            "Salves": {
                "MMG_M240_7_62mm": 48,
            },
        },
        "SpecialtiesList": {
            "overwrite_all": [
                '_transport1',
                '_ifv',
                '_smoke_launcher',
            ],
        },
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
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
        "CommandPoints": 140,
        "availability": [3, 2, 0, 0],
        "TagSet": {
            "add_tags": ['"Vehicule_Transport_Arme"'],
        },
        "SpecialtiesList": {
            "overwrite_all": [
                '_transport1',
                '_ifv',
                '_smoke_launcher',
            ],
        },
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "Divisions": {
            "US_11ACR": {
                "cards": 1,
            },
        },
        "UpgradeFromUnit": "Cav_Scout_Dragon_M3A2_US",
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M240_7_62mm": 48,
            },
        },
    },

    "M551A1_ACAV_Sheridan_US": {
        "CommandPoints": 50,
        "availability": [0, 6, 4, 0],
    },

    "M1A1_Abrams_reco_US": {
        "availability": [0, 3, 2, 0],
        "CommandPoints": 245,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },

    "OH58C_Scout_US": {
        "GameName": {
            "display": "#RECO2 OH-58C SCOUT",
        },
        "CommandPoints": 40,
        "availability": [0, 4, 3, 0],
    },

    "OH58D_Combat_Scout_US": {
        "CommandPoints": 60,
        "availability": [0, 4, 3, 0],
        "ECM": -0.1,
    },

    "OH58D_Kiowa_Warrior_US": {
        "GameName": {
            "display": "#RECO3 OH-58D KIOWA WR.",
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 2,
            },
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
    
    "MQM_105_Aquila_US": {
        "CommandPoints": 50,
        "availability": [0, 4, 0, 0],
    },
    
    "A37B_Dragonfly_US": {
        "CommandPoints": 70,
        "availability": [0, 3, 2, 0],
        "UpgradeFromUnit": "MQM_105_Aquila_US",
    },
    
    "OA10A_US": {
        "CommandPoints": 220,
        "availability": [0, 2, 0, 0],
        "UpgradeFromUnit": "A37B_Dragonfly_US",
    },

    "Airborne_Scout_US": {
        "GameName": {
            "display": "#RECO2 AIRBORNE SCOUTS",
        },
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 11,
            },
        },
    },

    "Scout_US": {
        "GameName": {
            "display": "#RECO2 SCOUTS",
        },
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
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
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 11,
                "SAW_M249_5_56mm": 30,
                "insert": [(2, 4)], # (salves_index, salves)
            },
            "equipmentchanges": {
                "insert": [(2, "RocketInf_M72A3_LAW_66mm")], # (turret, weapon)
                "insert_edits": {
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "SalvoStockIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
                "replace": [
                    ("MMG_inf_M240B_7_62mm", "SAW_M249_5_56mm", "MMG_inf_M240B_7_62mm", "SAW_M249_5_56mm")
                ],
            },
        },
    },
    
    "Pathfinder_NG_US": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "SAW_M249_5_56mm")],
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AnimateOnlyOneSoldier": True,
                        "NbWeapons": 1,
                        "SalvoStockIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "SalvoStockIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                    3: {
                        "turret_edits": {
                            "YulBoneOrdinal": 4,
                        },
                        "SalvoStockIndex": 3,
                        "HandheldEquipmentKey": "'WeaponAlternative_4'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_4'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_4'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_4"],
                    },
                },
                "quantity": {
                    "FM_M16": 3,
                },
            },
            "Salves": {
                "insert": [(1, 23)],
            },
        },
    },

    "HvyScout_NG_US": {
        "armor": "Infantry_armor_reference",
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "HvyScout_NG_Dragon_US": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [8, 0, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },
    
    "Scout_Aero_US": {
        "CommandPoints": 40,
        "availability": [0, 4, 3, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_WA_M60E3_7_62mm": False,
                },
                "quantity": {
                    "FM_M16": 8,
                    "MMG_WA_M60E3_7_62mm": 2,
                },
            },
        },
    },

    "LRRP_US": {
        "GameName": {
            "display": "#RECO2 LRS",
        },
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
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
            "Salves": {
                "M16A1_Carbine": 11,
            },
        },
    },
    
    "LRRP_Aero_US": {
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
        "availability": [0, 4, 3, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Sniper_US": {
        "GameName": {
            "display": "#RECO2 SNIPERS",
        },
        "armor": "Infantry_armor_reference",
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
    
    "Sniper_M82_US": {
        "GameName": {
            "display": "#RECO2 SNIPERS [M82]",
        },
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    # US AA
    "M274_Mule_M2HB_US": {
        "CommandPoints": 15,
        "UpgradeFromUnit": "DCA_M167A2_Vulcan_20mm_Aero_US",
    },
    
    "MANPAD_Stinger_C_US": {
        "GameName": {
            "display": "STINGER C",
            "token": "XQYDBWCBAP",
        },
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
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
                "FM_M16": 11,
                "MANPAD_FIM92": 6,
            },
        },
    },

    "MANPAD_Stinger_C_Aero_US": {
        "armor": "Infantry_armor_reference",
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16", "FM_M16_noreflex")],
            },
        },
    },

    "MANPAD_Stinger_C_para_US": {
        "armor": "Infantry_armor_reference",
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
                "FM_M16": 11,
                "MANPAD_FIM92": 6,
            },
        },
    },
    
    "MANPAD_Stinger_NG_US": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 5, 4],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16A1", "FM_M16A1_noreflex")],
            },
        },
    },
    
    "MANPAD_Redeye_US": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [12, 9, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16A1", "FM_M16A1_noreflex")],
            },
        },
    },
    
    "M42_Duster_US": {
        "CommandPoints": 35,
        "availability": [10, 0, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_Bofors_40mm": 17,
            },
        },
        "UpgradeFromUnit": "M274_Mule_M2HB_US",
    },

    "M163_CS_US": {
        "CommandPoints": 40,
        "availability": [8, 6, 0, 0],
        "UpgradeFromUnit": "M42_Duster_US",
    },

    "M163_PIVADS_US": {
        "CommandPoints": 65,
        "availability": [7, 5, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "Gatling_M61_Vulcan_20mm_late": 25,
            },
        },
    },
    
    "DCA_M167_Vulcan_20mm_nonPara_US": { # M167A1 VADS 20mm
        "CommandPoints": 25,
        "Factory": "EFactory/Logistic",
        "availability": [12, 9, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "FOB_US",
    },

    "DCA_M167A2_Vulcan_20mm_US": { # M167A2 VADS 20mm
        "CommandPoints": 30,
        "Divisions": {
            "add": ["US_3rd_Arm", "US_8th_Inf"],
            "is_transported": True,
            "needs_transport": True,
            "default": {
                "cards": 1,
                "Transports": ["M113A3_US"],
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": None,
    },
    
    "DCA_M167_Vulcan_20mm_US": { # AB M167A1 VADS 20mm
        "CommandPoints": 25,
        "Factory": "EFactory/Logistic",
        "Divisions": {
            "default": {
                "Transports": ["M113A3_US"],
                "cards": 1,
            },
            "US_82nd_Airborne": {
                "Transports": ["M1038_Humvee_US"],
            },
        },
        "availability": [0, 12, 9, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "DCA_M167_Vulcan_20mm_nonPara_US",
    },
    
    "DCA_M167A2_Vulcan_20mm_Aero_US": { # AERO-M167A2 PIVADS 20mm
        "CommandPoints": 30,
        "GameName": {
            "display": "AERO-M167A2 VADS 20mm",
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 10, 7, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "DCA_M167A2_Vulcan_20mm_US",
    },

    "M998_Avenger_US": {
        "CommandPoints": 100,
        "availability": [0, 5, 3, 0],
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_avenger_M3P": 17,
            },
        },
    },
    
    "M998_Avenger_nonPara_US": {
        "CommandPoints": 100,
        "availability": [5, 3, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_avenger_M3P": 17,
            },
        },
        "UpgradeFromUnit": None,
    },
    
    "DCA_XM85_Chaparral_US": {
        "CommandPoints": 130,
        "availability": [4, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "M48_Chaparral_MIM72F_US": {
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 220,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "CommandPoints": 130,
        "availability": [0, 3, 2, 0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },
    
    "DCA_XMIM_115A_Roland_US": {
        "CommandPoints": 150,
        "GameName": {
            "display": "XM1058 ROLAND",
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 300,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "capacities": {
            "remove_capacities": ["reserviste"],
        },
        "availability": [0, 4, 3, 0],
        "SpecialtiesList": {
            "overwrite_all": [
                'verygood_airoptics',
            ],
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "UpgradeFromUnit": "M48_Chaparral_MIM72F_US",
    },

    "DCA_I_Hawk_US": {
        "CommandPoints": 90,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 300,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "availability": [4, 3, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "US_8th_Inf": {
                "Transports": ["M35_supply_US"],
            },
            "US_11ACR": {
                "Transports": ["M35_supply_US"],
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    # US HELI
    "UH1H_Huey_US": {
        "CommandPoints": 45,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M60_7_62mm_helo": 80,
            },
        },
    },
    
    "UH60A_Black_Hawk_US": {
        "CommandPoints": 60,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M240d_7_62mm": 120,
            },
        },
    },

    "CH47_Chinook_US": {
        "CommandPoints": 60,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "MH47D_Super_Chinook_US": {
        "CommandPoints": 65,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
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
    
    "UH1M_gunship_US": {
        "CommandPoints": 70,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [6, 0, 0, 0],
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
    "A37B_Dragonfly_HE_US": {
        "CommandPoints": 75,
        "availability": [0, 4, 0, 0],
    },
    
    "A37B_Dragonfly_NPLM_US": {
        "CommandPoints": 75,
        "availability": [0, 6, 0, 0],
    },
    
    "A6E_Intruder_SEAD_US": {
        "CommandPoints": 165,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "availability": [0, 2, 0, 1],
    },
    
    "A6E_Intruder_US": {
        "CommandPoints": 160,
        "availability": [0, 3, 0, 0],
    },
    
    "A7D_Corsair_II_US": { # A-7D CORSAIR II [HE] (4x Mk 84)
        "CommandPoints": 200,
        "availability": [0, 2, 0, 0],
    },
    
    "A7D_Corsair_II_RKT_US": { # A-7D CORSAIR II [RKT] (114x Hydra)
        "CommandPoints": 160,
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketAir_Hydra_70mm_x38_avion", "RocketAir_Hydra_70mm_x114_avion")],
            },
            "turrets": {
                2: {
                    "MountedWeapons": {
                        "RocketAir_Hydra_70mm_x114_avion": {
                            "WeaponShootDataPropertyName": [
                                "WeaponShootData_0_3",
                                "WeaponShootData_1_3",
                                "WeaponShootData_2_3",
                                "WeaponShootData_3_3",
                                "WeaponShootData_4_3",
                                "WeaponShootData_5_3"
                            ],
                        },
                    },
                },
            },
            "Salves": {
                "RocketAir_Hydra_70mm_x114_avion": 1,
            },
        },
    },
    
    "A7D_Corsair_II_CLU_US": { # A-7D CORSAIR II [CLU] (12x Mk-20 Rockeye II)
        "CommandPoints": 190,
        "availability": [0, 2, 0, 0],
    },
    
    "A7D_Corsair_II_AT_US": { # A-7D CORSAIR II [AT] (4x AGM-65B)
        "CommandPoints": 210,
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_AGM65B_Maverick": 2,
            },
        },
    },
    
    "EA6B_Prowler_US": {
        "CommandPoints": 260,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 12500.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "availability": [0, 2, 0, 1],
    },
    
    "F117_Nighthawk_US": {
        "GameName": {
            "display": "F-117A NIGHTHAWK",
        },
        "CommandPoints": 260,
        "availability": [0, 0, 0, 1],
        "max_speed": 750,
        "UpgradeFromUnit": "F15E_StrikeEagle_US",
    },
    
    "F4E_Phantom_II_AA_US": {
        "CommandPoints": 165,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "availability": [0, 3, 2, 0],
    },
    
    "F15C_Eagle_AA2_US": {
        "CommandPoints": 265,
        "ECM": -0.45,
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1375,
            },
        },
        "availability": [0, 2, 0, 1],
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
    
    "F15E_StrikeEagle_US": {
        "CommandPoints": 290,
        "GameName": {
            "display": "F-15E STRIKE EAGLE [PGB]",
        },
        "ECM": -0.45,
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1375,
            },
        },
        "availability": [0, 0, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "Bomb_GBU_10_salvolength2": 1,
            },
        },
    },

    "F4_Wild_Weasel_US": { # AGM-45 5250m (should be 5000m missile range probably)
        "CommandPoints": 190,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                0: {
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
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "availability": [0, 2, 0, 0],
    },


    "F4E_Phantom_II_CBU_US": {
        "CommandPoints": 165,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "availability": [0, 2, 0, 0],
    },

    "F4E_Phantom_II_napalm_US": {
        "CommandPoints": 165,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
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
    },

    "F111F_Aardvark_LGB_US": {  # 4x GBU-12
        "CommandPoints": 210,
        "GameName": {
            "display": "F-111F AARDVARK [PGB]",
        },
        "WeaponDescriptor": {
            "Salves": {
                "Bomb_GBU_12_salvolength4": 1,
            },
            "equipmentchanges": {
                "replace": [("Bomb_GBU_12_salvolength2", "Bomb_GBU_12_salvolength4")],
            },
        },
    },
    
    "F111F_Aardvark_LGB2_US": { # 4x GBU-10
        "CommandPoints": 260,
        "GameName": {
            "display": "F-111F AARDVARK [PGB2]",
        },
        "UpgradeFromUnit": "F111F_Aardvark_LGB_US",
        "WeaponDescriptor": {
            "Salves": {
                "Bomb_GBU_10_salvolength4": 1,
            },
            "equipmentchanges": {
                "replace": [("Bomb_GBU_10_salvolength2", "Bomb_GBU_10_salvolength4")],
            },
        },
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

    "EF111_Raven_US": { # EW
        "CommandPoints": 180,
        "max_speed": 1400,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 12500.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
            },
        },
        "availability": [0, 0, 2, 0],
    },

    "F16C_LGB_US": {
        "CommandPoints": 225,
        "GameName": {
            "display": "F-16CG [PGB]",
        },
        "ECM": -0.35,
        "WeaponDescriptor": {
            "Salves": {
                "Bomb_GBU_12_salvolength2": 1,
            },
            "equipmentchanges": {
                "replace": [("Bomb_GBU_12", "Bomb_GBU_12_salvolength2")],
            },
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "availability": [0, 0, 0, 1],
        "UpgradeFromUnit": "F16E_TER_HE_US",
    },

    "F16E_AGM_US": {  # 4x AGM-65D, 2x AIM-9M
        "CommandPoints": 250,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_AGM65D_Maverick": 2,
            },
        },
    },
    
    "FA16_CAS_US": {
        "CommandPoints": 260,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("AA_AIM9L_Sidewinder", "AA_AIM9M_Sidewinder")],
            },
            "Salves": {
                "AGM_AGM65D_Maverick": 2,
            },
        },
    },

    "F16E_HE_US": {
        "CommandPoints": 200,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "availability": [0, 2, 0, 0],
    },

    "F16E_TER_HE_US": {  # 12x mk82 + , 11 ACR
        "CommandPoints": 225,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "availability": [0, 2, 0, 0],
    },

    "F16E_napalm_US": {
        "CommandPoints": 200,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
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

    "F16E_SEAD_US": { # AGM-88 5950m
        "CommandPoints": 220,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
                "EOpticalStrength/HighAltitude": 375,
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
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "availability": [0, 2, 0, 0],
    },
    
    "F16E_TER_CLU_US": {
        "CommandPoints": 225,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
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
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
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
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "availability": [0, 3, 2, 0],
        "UpgradeFromUnit": "F16E_AA_US",
    },

    "A10_Thunderbolt_II_US": {  # 8x mk.82, 2x AIM-9M
        "CommandPoints": 220,
        "max_speed": 500,
        "availability": [0, 2, 0, 0],
    },

    "A10_Thunderbolt_II_Rkt_US": {  # 76x Hydra, 2x AIM-9M
        "CommandPoints": 220,
        "max_speed": 500,
        "availability": [0, 2, 0, 0],
    },

    "A10_Thunderbolt_II_ATGM_US": {  # 4x AGM-65D, 2x AIM-9M
        "CommandPoints": 240,
        "max_speed": 500,
        "availability": [0, 2, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_AGM65D_Maverick": 2,
            },
        },
    },
}
