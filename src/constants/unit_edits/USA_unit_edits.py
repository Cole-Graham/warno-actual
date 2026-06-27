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
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },

    "UH60A_CO_US": {
        "CommandPoints": 145,
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
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
        "TagSet": {"add_tags": ['"CMD_Unit"']},
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
        "TagSet": {"add_tags": ['"CMD_Unit"']},
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
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },

    "M1025_Humvee_CMD_USMC_US": {
        "CommandPoints": 145,
        "availability": [0, 3, 0, 0],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "TagSet": {"add_tags": ['"CMD_Unit"']},
        "UpgradeFromUnit": "M1025_Humvee_CMD_US",
    },

    "LAV_C_US": {
        "CommandPoints": 160,
        "availability": [0, 3, 0, 0],
        "strength": "LAV_25_M1047_US_US",
        "armor": "LAV_25_M1047_US_US",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },

    "AAVC_7A1_CMD_USMC_US": {
        "CommandPoints": 150,
        "availability": [0, 3, 0, 0],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },

    "M2A1_Bradley_Leader_US": {
        "CommandPoints": 195,
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "AutoCanon_AP_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_AP_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "AutoCanon_HE_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_HE_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
            "Salves": {
                "MMG_M240_7_62mm": 48,
            },
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 3, 0],
        "UpgradeFromUnit": "M577_CMD2_US",
    },

    "M2A2_Bradley_Leader_US": {
        "CommandPoints": 195,
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
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
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "FIRETEAM",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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
        "remove_zone_capture": None,
    },
    
    "Rifles_half_Cav_CMD_US": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "CAV. TROOPERS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_IFV",
                "UNITE_Rifles_half_Cav_CMD_US",
                "Unite",
            ],
        },
        "strength": 6,
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_ifv',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "RocketInf_M72A3_LAW_66mm": {
                        "new_weapon": "RocketInf_AT4_83mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                        "old_new_effect": ("RocketInf_M72_LAW_66mm", "RocketInf_AT4_83mm"),
                    },
                },
                "quantity": {
                    "FM_M16": 6,
                },
            },
            "Salves": {
                "RocketInf_AT4_83mm": 4,
            },
        },
        "remove_zone_capture": None,
    },

    "Rifles_CMD_US": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MECH. RIFLES",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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
                "replace": {
                    "MMG_WA_M60E3_7_62mm": {
                        "new_weapon": "MMG_M60E1_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "MMG_M60E1_7_62mm": 45,
            },
        },
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },

    "Engineer_CMD_US": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "ENGINEERS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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
                        "AmmoBoxIndex": 2,
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
            "display": "RANGERS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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
        "IdentifiedTextures": ["Texture_RTS_H_Infantry_sf", "Texture_sf"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_sf',
                '_choc',
                'infantry_equip_medium',
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
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "Commando_733": {
                        "new_weapon": "M16A1_Carbine",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "quantity": {
                    "M16A1_Carbine": 8,
                },
            },
            "turrets": {
                2: {
                    "MountedWeapons": {
                        "RocketInf_M67_RCL_90mm": {
                            # For some reason I have the prefix hardcoded into the script when changing ammunition
                            # ($/GFX/Weapon/Ammo_)
                            "Ammunition": "RocketInf_Carl_Gustav",
                            "EffectTag": '"FireEffect_RocketInf_Carl_Gustav"',
                        },
                        # Insertions are handled first so factor that into the indices, and keep in mind
                        # that the list is sorted in reverse order to prevent index-shifting issues when
                        # removing multiple weapons
                        "remove": [1],
                    },
                },
            },
            "Salves": {
                "M16A1_Carbine": 7,
                "RocketInf_Carl_Gustav": 7,
            },
        },
        "remove_zone_capture": None,
    },

    "Airborne_Engineer_CMD_US": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "AB ENGINEERS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "AIRBORNE",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "AERO-RIFLES",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "remove_zone_capture": None,
    },

    "Aero_half_CMD_US": { # Not in use (redundant with AB FIRETEAM units)
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "AERO-FIRETEAM",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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
            "display": "AERO-ENGINEERS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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
            "display": "GREEN BERETS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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
                "replace": {
                    "Commando_733": {
                        "new_weapon": "M16A1_Carbine",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
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
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MP LEADER",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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

    "Rifles_USMC_CMD_US": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "USMC RIFLEMEN",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Rifles_USMC_CMD_US",
                "Unite",
            ],
        },
        "strength": 6,
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_resolute',
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
                    "FM_M16": 6,
                },
            },
            "Salves": {
                "RocketInf_M72A3_LAW_66mm": 6,
            },
        },
        "remove_zone_capture": None,
    },

    "Engineer_USMC_CMD_US": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "USMC ENGINEERS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Engineer_USMC_CMD_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_resolute',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "MMG_M60E3_7_62mm": {
                        "new_weapon": "MMG_WA_M60E3_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "quantity": {
                    "FM_M16": 9,
                    "MMG_WA_M60E3_7_62mm": 3,
                },
                "animate": {
                    "MMG_WA_M60E3_7_62mm": False,
                },
            },
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 4, 3],
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
                    "FM_M16": 8,
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
                "replace": {
                    "MMG_WA_M60E3_7_62mm": {
                        "new_weapon": "MMG_M60E1_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "MMG_M60E1_7_62mm": 45,
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
                "replace": {
                    "MMG_inf_M240B_7_62mm": {
                        "new_weapon": "SAW_M249_5_56mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
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
                "replace": {
                    "MMG_WA_M60E3_7_62mm": {
                        "new_weapon": "MMG_M60E1_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "MMG_M60E1_7_62mm": 45,
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
                "replace": {
                    "M47_DRAGON": {
                        "new_weapon": "M47_DRAGON_II",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },

    "Engineers_USMC_US": {
        "CommandPoints": 50,
        "GameName": {
            "display": "USMC ENGINEERS",
        },
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
                "replace": {
                    "MMG_M60E3_7_62mm": {
                        "new_weapon": "MMG_WA_M60E3_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "animate": {
                    "MMG_WA_M60E3_7_62mm": False,
                },
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
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "availability": [0, 12, 9, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "strength": 8,
        "UpgradeFromUnit": "MP_RCL_US",
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 4,
                    "FM_M16A1": 3,
                    "MMG_WA_M60E3_7_62mm": 1,
                },
                "insert": [
                    (0, "FM_M16A1"),
                    (3, "RocketInf_M72A3_LAW_66mm"),
                ],
                "insert_edits": {
                    0: {  # M16A1 (newly inserted)
                        "turret_edits": {
                            "YulBoneOrdinal": 1,
                        },
                        "AmmoBoxIndex": 0,
                        "HandheldEquipmentKey": "'WeaponAlternative_1'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_1'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_1'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_1"],
                    },
                    1: {  # M16 (bumped from vanilla 0)
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                    2: {  # MMG (bumped from vanilla 1)
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                    3: {  # LAW (newly inserted)
                        "turret_edits": {
                            "YulBoneOrdinal": 4,
                        },
                        "AmmoBoxIndex": 3,
                        "HandheldEquipmentKey": "'WeaponAlternative_4'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_4'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_4'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_4"],
                    },
                },
            },
            "Salves": {
                "FM_M16": 11,
                "MMG_WA_M60E3_7_62mm": 45,
                "insert": [
                    (0, 11),
                    (3, 4),
                ],
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
        "UpgradeFromUnit": "MP_CMD_US",
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
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_AT4_83mm": 6,
            },
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

    "Rifles_USMC_LAW_US": {
        "CommandPoints": 40,
        "GameName": {
            "display": "USMC RIFLEMEN [LAW]",
        },
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 11,
                    "SAW_M249_5_56mm": 2,
                },
            },
        },
    },

    "Rifles_USMC_AT4_US": {
        "CommandPoints": 50,
        "GameName": {
            "display": "USMC RIFLEMEN [AT4]",
        },
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_AT4_83mm": 9,
            },
        },
    },

    "Rifles_USMC_Dragon_US": {
        "CommandPoints": 50,
        "GameName": {
            "display": "USMC RIFLEMEN [DRAGON]",
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

    "Rifles_USMC_HMG_US": { # USMC GUNNERS
        "GameName": {
            "display": "USMC GUNNERS",
        },
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "MMG_M60E3_7_62mm": {
                        "new_weapon": "MMG_WA_M60E3_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "quantity": {
                    "FM_M16": 4,
                    "MMG_WA_M60E3_7_62mm": 3,
                },
            },
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

    "AeroRifles_USMC_US": {  # USMC AERO-RIFLEMEN
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "strength": 6,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 4,
                },
            },
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
                "replace": {
                    "MMG_WA_M60E3_7_62mm": {
                        "new_weapon": "MMG_inf_M240B_7_62mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                        "old_new_effect": ("MMG_M60_7_62mm", "MMG_inf_M240B_7_62mm"),
                    },
                },
            },
            "Salves": {
                "FM_M16": 11,
                "SAW_M249_5_56mm": 30,
                "MMG_inf_M240B_7_62mm": 36,
                "RocketInf_AT4_83mm": 4,
            },
        },
    },
    
    "Rifles_half_Cav_AT4_US": {
        "GameName": {
            "display": "CAV. TROOPERS [AT4]",
        },
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [12, 9, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_AT4_83mm": 4,
            },
        },
    },
    
    "Rifles_half_Cav_Dragon_US": {
        "GameName": {
            "display": "CAV. TROOPERS [DRAGON]",
        },
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "availability": [12, 9, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "M47_DRAGON_II": 6,
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
                "replace": {
                    "Commando_733": {
                        "new_weapon": "M16A1_Carbine",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                    "RocketInf_M72A3_LAW_66mm": {
                        "new_weapon": "RocketInf_AT4_83mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                        "old_new_effect": ("RocketInf_M72_LAW_66mm", "RocketInf_AT4_83mm"),
                    },
                },
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
                "replace": {
                    "Commando_733": {
                        "new_weapon": "M16A1_Carbine",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "M16A1_Carbine": 11,
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
                "replace": {
                    "SAW_M249_5_56mm": {
                        "new_weapon": "MMG_inf_M240B_7_62mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
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
        "CommandPoints": 50,
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
                "replace": {
                    "MMG_WA_M60E3_7_62mm": {
                        "new_weapon": "MMG_M60E1_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "MMG_M60E1_7_62mm": 45,
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
                "replace": {
                    "MMG_WA_M60E3_7_62mm": {
                        "new_weapon": "MMG_M60E1_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "MMG_M60E1_7_62mm": 45,
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
                "replace": {
                    "MMG_WA_M60E3_7_62mm": {
                        "new_weapon": "MMG_M60E1_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "MMG_M60E1_7_62mm": 45,
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
                "replace": {
                    "MMG_WA_M60E3_7_62mm": {
                        "new_weapon": "MMG_M60E1_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "quantity": {
                    "FM_M16A1": 7,
                    "MMG_M60E1_7_62mm": 2,
                },
            },
            "Salves": {
                "MMG_M60E1_7_62mm": 45,
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
                "replace": {
                    "MMG_WA_M60E3_7_62mm": {
                        "new_weapon": "MMG_M60E1_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                    "M47_DRAGON_II": {
                        "new_weapon": "M47_DRAGON",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "animate": {
                    "MMG_M60E1_7_62mm": False,
                },
                "quantity": {
                    "FM_M16A1": 7,
                    "MMG_M60E1_7_62mm": 2,
                },
            },
            "Salves": {
                "MMG_M60E1_7_62mm": 45,
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
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                    3: {
                        "turret_edits": {
                            "YulBoneOrdinal": 4,
                        },
                        "AmmoBoxIndex": 3,
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

    "Groupe_AT_USMC_US": { # This unit needs an overveiw, im not sure about it
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "strength": 6,
        "max_speed": 20,
        "availability": [0, 8, 6, 0],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
         "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 6,
                },
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
                "replace": {
                    "Commando_733": {
                        "new_weapon": "M16A2_Carbine",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                    "MMG_M60E3_7_62mm": {
                        "new_weapon": "MMG_WA_M60E3_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "M16A2_Carbine": 11,
                "RocketInf_AT4_83mm": 5,
                "Grenade_Satchel_Charge": 4,
            },
        },
        "UpgradeFromUnit": "GreenBerets_ODA_US",
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
                "replace": {
                    "Commando_733": {
                        "new_weapon": "M16A1_Carbine",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
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
                "replace": {
                    "FM_M16": {
                        "new_weapon": "M16A1_Carbine",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
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
        "UpgradeFromUnit": None,
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
        "UpgradeFromUnit": None,
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
        "UpgradeFromUnit": None,
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
        "UpgradeFromUnit": "HMGteam_M60_AB_US",
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
    
    "HMGteam_M2HB_M63_US": {
        "CommandPoints": "HMGteam_M2HB_M63_UK",
        "GameName": {
            "display": "M2HB 12.7mm M63",
        },
        "strength": "HMGteam_M2HB_M63_UK",
        "max_speed": "HMGteam_M2HB_M63_UK",
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },
    
    "HMGteam_M2HB_M63_USMC_US": {
        "CommandPoints": "HMGteam_M2HB_M63_UK",
        "GameName": {
            "display": "USMC 12.7mm M63",
        },
        "strength": "HMGteam_M2HB_M63_UK",
        "max_speed": "HMGteam_M2HB_M63_UK", 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "UpgradeFromUnit": "HMGteam_M2HB_M63_US",
    },
    
    "HMGteam_Mk19_US": {
        "GameName": {
            "display": "Mk.19 40mm",
        },
        "is_standard": (True, "40mm_Mk19_Team"), 
        "CommandPoints": 35,
        "strength": 5,
        "max_speed": 14, 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "UpgradeFromUnit": "HMGteam_M2HB_M63_USMC_US",
        # "UpgradeFromUnit": None,
    },
    
    "HMGteam_Mk19_USMC_US": {
        "GameName": {
            "display": "USMC Mk.19 40mm",
        },
        "is_standard": (True, "40mm_Mk19_Team"), 
        "CommandPoints": 35,
        "strength": 5,
        "max_speed": 14, 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "UpgradeFromUnit": "HMGteam_Mk19_US",
    },
    
    "HMGteam_Mk19_AB_US": {
        "GameName": {
            "display": "AB Mk.19 40mm",
        },
        "is_standard": (True, "Para_40mm_Mk19_Team"), 
        "CommandPoints": 35,
        "strength": 5,
        "max_speed": 14, 
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "UpgradeFromUnit": "HMGteam_Mk19_USMC_US",
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
    
    "ATteam_TOW2_USMC_US": {
        "GameName": {
            "display": "USMC TOW-2",
        },
        "CommandPoints": 65,
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
        "UpgradeFromUnit": "ATteam_TOW2_USMC_US",
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
    
    "ATteam_TOW2A_US": {
        "CommandPoints": 75,
        "availability": [4, 3, 0, 0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "UpgradeFromUnit": "ATteam_TOW2_para_US",
    },
    
    "M274_Mule_ITOW_US": {
        "CommandPoints": 45,
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
        "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "CGage_Peacekeeper_US": {
        "CommandPoints": 20,
         "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "Dragoon_300_US": {
        "CommandPoints": 15,
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
        "capacities": {
            "add_capacities": ["LDR_ARTY"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 60,
        "GameName": {
            "display": "M577 TACFIRE FCV",
            "token": "ZTSGIUUUVJ", # Don't remove or logistic tab version will get renamed as well
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_M577_US",
                "Unite",
                "Vehicule",
            ],
        },
        "Factory": "Factory/Art",
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

    "81mm_mortar_USMC_US": {
        "CommandPoints": 35,
        "availability": [6, 5, 4, 0],
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
        "CommandPoints": 55,
        "availability": [4, 3, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 35,
            },
        },
    },

    "LAV_M_81mm_US": {  # LAV-M mortar carrier, M252 81mm Mortar
        "CommandPoints": 60,
        "availability": [4, 3, 0, 0],
        "strength": "LAV_25_M1047_US_US",
        "armor": "LAV_25_M1047_US_US",
    },
    
    "CATFAE_US": {
        "CommandPoints": 125,
        "availability": [3, 2, 0, 0],
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

    "Howz_M198_155mm_USMC_US": {
        "CommandPoints": 110,
        "availability": [3, 2, 0, 0],
    },
    
    "Howz_M198_155mm_Copperhead_US": {
        "CommandPoints": 135,
        "availability": [3, 2, 0, 0],
    },

    "M106A2_HOWZ_US": { # M106A2 mortar carrier, 107mm M30 Mortar
        "CommandPoints": 70,
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

    "M109A2_USMC_US": {
        "CommandPoints": 180,
        "availability": [3, 2, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 35,
            },
        },
    },
    
    "M109A2_Copperhead_US": {
        "CommandPoints": 210,
        "availability": [2, 0, 1, 0],
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

    "M110A2_USMC_US": {
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
        "CommandPoints": 320,
        "Divisions": {
            "add": ["US_8th_Inf"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 2,
            },
        },
        # "WeaponDescriptor": {
        #     "turrets": {
        #         0: {
        #             "AngleRotationMaxPitch": 1.0,
        #         },
        #     },
        # },
        "availability": [0, 1, 0, 0],
    },

    # US TANK
    "M1A1HA_Abrams_CMD_US": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 325,
        "GameName": {
            "display": "M1A1(HA) ABRAMS",
            "token": "CIOEKZVEAY",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1A1HA_Abrams_CMD_US",
                "Unite",
            ],
        },
        "armor": {
            "top": (5, None),
        },
        "max_speed": "M1_Abrams_US",
        "road_speed_display": "M1_Abrams_US",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 225,
        "GameName": {
            "display": "M1A1 ABRAMS",
            "token": "JARUASHKDH",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1A1_Abrams_CMD_US",
                "Unite",
            ],
        },
        "armor": {
            "top": (5, None),
        },
        "max_speed": "M1_Abrams_US",
        "road_speed_display": "M1_Abrams_US",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 200,
        "GameName": {
            "display": "M1IP ABRAMS",
            "token": "TSLINICZXV",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1IP_Abrams_CMD_US",
                "Unite"
            ],
        },
        "armor": {
            "top": (5, None),
        },
        "max_speed": "M1_Abrams_US",
        "road_speed_display": "M1_Abrams_US",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 170,
        "GameName": {
            "display": "M1 ABRAMS",
            "token": "JMIRJBBLPW",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1_Abrams_CMD_US",
                "Unite"
            ],
        },
        "armor": {
            "top": (4, None),
        },
        "max_speed": "M1_Abrams_US",
        "road_speed_display": "M1_Abrams_US",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 105,
        "GameName": {
            "display": "M60A3 (TTS)",
            "token": "OZPDFIGTWN",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M60A3_CMD_US",
                "Unite"
            ],
        },
        "armor": {
            "top": (3, None),
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 90,
        "GameName": {
            "display": "M60A1 RISE",
            "token": "ETJTTJZGYR",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M60A1_RISE_Passive_CMD_US",
                "Unite"
            ],
        },
        "armor": {
            "top": (3, None),
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
        "availability": [0, 0, 5, 0],
        "remove_zone_capture": None,
    },

    "M60A1_RISE_Passive_USMC_CMD_US": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 90,
        "GameName": {
            "display": "USMC M60A1",
            "token": "CBDJCYPIXI",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M60A1_RISE_Passive_USMC_CMD_US",
                "Unite"
            ],
        },
        "armor": {
            "top": (3, None),
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_resolute',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 5, 0],
        "remove_zone_capture": None,
    },

    "M551A1_TTS_Sheridan_CMD_US": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 50,
        "GameName": {
            "display": "M551 TTS SHERIDAN",
            "token": "NBZRAJWZXD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_Unit",
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
        "CommandPoints": 20,
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
                "replace": {
                    "M47_DRAGON_Bipied": {
                        "new_weapon": "M47_DRAGON_II",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
    },

    "AAVP_7A1_USMC_US": {
        "CommandPoints": 25,
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

    "M1025_Humvee_TOW_USMC_US": {
        "GameName": {
            "display": "USMC M1025 HUMVEE TOW-2",
        },
        "CommandPoints": 65,
        "stealth": 1.5,
        "availability": [0, 6, 4, 0],
    },
    
    "CUCV_Hellfire_US": {
        "CommandPoints": 120,
        "availability": [0, 4, 3, 0],
    },

    "LAV_AT_US": {  # TOW 2
        "CommandPoints": 75,
        "availability": [0, 6, 4, 0],
        "strength": "LAV_25_M1047_US_US",
        "armor": "LAV_25_M1047_US_US",
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
        "armor": {
            "top": (3, None),
        },
    },

    "M728A1_CEV_US": {
        "CommandPoints": 75,
        "availability": [0, 8, 6, 0],
        "armor": {
            "top": (3, None),
        },
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
                "replace": {
                    "AutoCanon_AP_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_AP_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "AutoCanon_HE_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_HE_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
    },

    "M2A1_Bradley_IFV_US": {
        "CommandPoints": 65,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "AutoCanon_AP_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_AP_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "AutoCanon_HE_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_HE_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
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
    
    "M2A2_BRAT_US": {
        "CommandPoints": 100,
        "max_speed": 55,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M240_7_62mm": 48,
            },
        },
    },
    
    "M2_Bradley_BSV_US": {
        "CommandPoints": 50,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M240_7_62mm": 48,
                "ATGM_BGM71C_ITOW_IFV_salvolength2": 3,
            },
            "turrets": {
                0: {
                    "MountedWeapons": {
                        "insert": {
                            "0:AutoCanon_AP_25mm_M242_Bushmaster_Late": {
                                "Ammunition": "$/GFX/Weapon/Ammo_AutoCanon_AP_25mm_M242_Bushmaster_APDS",
                            },
                        },
                        "AutoCanon_HE_25mm_M242_Bushmaster_Late_BSV": {
                            "HandheldEquipmentKey": "'WeaponAlternative_2'",
                            "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                            "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                            "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                        },
                    },
                },
                1: {
                    "MountedWeapons": {
                        "ATGM_BGM71C_ITOW_x2_IFV": {
                            "HandheldEquipmentKey": "'WeaponAlternative_3'",
                            "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                            "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                            "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                        },
                    },
                },
                2: {
                    "MountedWeapons": {
                        "MMG_M240_7_62mm": {
                            "HandheldEquipmentKey": "'WeaponAlternative_4'",
                            "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_4'",
                            "WeaponIgnoredPropertyName": "'WeaponIgnored_4'",
                            "WeaponShootDataPropertyName": ["WeaponShootData_0_4"],
                        },
                    },
                },
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
        "armor": {
            "top": (5, None),
        },
        "max_speed": "M1_Abrams_US",
        "road_speed_display": "M1_Abrams_US",
    },

    "M1A1_Abrams_US": {
        # "GameName": {
        #     "display": "#3RDARM M1A1 ABRAMS",
        #     "token": "YEMPBPBTNZ",
        # },
        "CommandPoints": 225,
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
        "armor": {
            "top": (5, None),
        },
        "max_speed": "M1_Abrams_US",
        "road_speed_display": "M1_Abrams_US",
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
        "armor": {
            "top": (5, None),
        },
        "max_speed": "M1_Abrams_US",
        "road_speed_display": "M1_Abrams_US",
    },

    "M1_Abrams_US": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [6, 4, 0, 0],
        "armor": {
            "top": (4, None),
        },
        "max_speed": 70,
        "road_speed_display": 80,
    },

    "M1_Abrams_NG_US": {
        "CommandPoints": 150,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [6, 0, 0, 0],
        "armor": {
            "top": (4, None),
        },
        "max_speed": "M1_Abrams_US",
        "road_speed_display": "M1_Abrams_US",
    },
    
    "M1_Abrams_MOD_US": {
        "CommandPoints": 225,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 4, 3, 0],
        "armor": {
            "top": (4, None),
        },
        "max_speed": "M1_Abrams_US",
        "road_speed_display": "M1_Abrams_US",
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
        "armor": {
            "top": (3, None),
        },
    },

    "M60A3_ERA_Patton_US": {
        "CommandPoints": 125,
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
        "armor": {
            "top": (3, None),
        },
    },

    "M60A3_Patton_NG_US": {
        "CommandPoints": 110,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [10, 7, 0, 0],
        "armor": {
            "top": (3, None),
        },
    },

    "M60A1_RISE_Passive_US": {
        "CommandPoints": 80,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [10, 7, 0, 0],
        "armor": {
            "top": (3, None),
        },
    },

    "M60A1_RISE_Passive_USMC_US": {
        "CommandPoints": 90,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [10, 7, 0, 0],
        "armor": {
            "top": (3, None),
        },
    },

    "M60A1_RISE_Passive_USMC_ERA_US": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 8, 6, 0],
        "armor": {
            "top": (3, None),
        },
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
        "UpgradeFromUnit": "FAV_trans_US",
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
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 35,
            },
        },
        "UpgradeFromUnit": "M151A2_scout_US",
    },
    
    "M1025_Humvee_scout_USMC_US": {
        "CommandPoints": 25,
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_M2HB": 35,
            },
        },
        "UpgradeFromUnit": "M1025_Humvee_scout_US",
    },

    "M1025_Humvee_AGL_US": {
        "CommandPoints": 30,
        "UpgradeFromUnit": None,
    },
    
    "M1025_Humvee_AGL_USMC_US": {
        "CommandPoints": 30,
        "UpgradeFromUnit": "M1025_Humvee_AGL_nonPara_US",
    },

    "M1025_Humvee_AGL_nonPara_US": {
        "CommandPoints": 30,
        "UpgradeFromUnit": "M1025_Humvee_scout_USMC_US",
    },

    "M998_Humvee_Delta_US": {
        "CommandPoints": 30,
        "UpgradeFromUnit": "M1025_Humvee_AGL_nonPara_US",
    },

    "M981_FISTV_US": {
        "CommandPoints": 30,
        "GameName": {
            "display": "M981 FISTV",
            "token": "JKFBZFRBYZ",
        },
        "TagSet": {
            "add_tags": ['"reco_radar"'],
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/Standard": 8834.0,
                "EOpticalStrength/LowAltitude": 8834.0,
            },
        },
        "availability": [8, 0, 0, 0],
        "UpgradeFromUnit": "M548A2_Jammer_US",
    },
    
    "M1025_Humvee_GVLLD_US": {
        "CommandPoints": 35,
        "availability": [8, 0, 0, 0],
        "UpgradeFromUnit": "M981_FISTV_US",
    },
    
    "M548A2_Jammer_US": {
        "CommandPoints": 25,
        "availability": [6, 0, 0, 0],
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
    
    "FAV_trans_US": {
        "CommandPoints": 25,
    },
    
    "FAV_HMG_US": {
        "CommandPoints": 30,
        "availability": [12, 9, 0, 0],
        "UpgradeFromUnit": "M151A2_FAV_USMC_US",
    },
    
    "FAV_AGL_US": {
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
    },
    
    "FAV_TOW_US": {
        "CommandPoints": 75,
        "availability": [8, 6, 0, 0],
    },

    "M151A2_FAV_USMC_US": {
        "CommandPoints": 30,
        "availability": [0, 0, 10, 7],
    },

    "LAV_MEWSS_US": { # Jammer + Sigint + VG optics + Smoke
        "CommandPoints": 30,
        "availability": [0, 6, 0, 0],
        "strength": "LAV_25_M1047_US_US",
        "armor": "LAV_25_M1047_US_US",
        "UpgradeFromUnit": "M1025_Humvee_GVLLD_US",
    },

    "LAV_25_M1047_US_US": {
        "CommandPoints": 70,
        "availability": [0, 4, 3, 0],
        "strength": 10,
        "armor": {
            "front": (1, None),
        },
        "stealth": 1.0,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_turret_7_62mm_M60": 60,
                "MMG_M240_7_62mm": 48,
            },
            "equipmentchanges": {
                "replace": {
                    "AutoCanon_AP_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_AP_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "AutoCanon_HE_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_HE_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "MMG_team_7_62mm_M60": {
                        "new_weapon": "MMG_turret_7_62mm_M60",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
        "UpgradeFromUnit": "FAV_TOW_US",
    },
    
    "LAV_25_US": { # Transport (Marines)
        "CommandPoints": 65,
        "strength": "LAV_25_M1047_US_US",
        "armor": "LAV_25_M1047_US_US",
        "stealth": "LAV_25_M1047_US_US",
        "WeaponDescriptor": {
            "Salves": {
                "MMG_turret_7_62mm_M60": 60,
                "MMG_M240_7_62mm": 48,
            },
            "equipmentchanges": {
                "replace": {
                    "AutoCanon_AP_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_AP_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "AutoCanon_HE_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_HE_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "MMG_team_7_62mm_M60": {
                        "new_weapon": "MMG_turret_7_62mm_M60",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
        "UpgradeFromUnit": "M1025_Humvee_AGL_USMC_US",
    },
    
    "M3_Bradley_CFV_US": {
        "CommandPoints": 85,
        "availability": [6, 4, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "AutoCanon_AP_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_AP_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "AutoCanon_HE_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_HE_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
            "Salves": {
                "MMG_M240_7_62mm": 48,
            },
        },
        "UpgradeFromUnit": "M551A1_ACAV_Sheridan_US",
    },

    "M3A1_Bradley_CFV_US": {
        "CommandPoints": 105,
        "availability": [4, 3, 0, 0],
        "TagSet": {
            "add_tags": ['"Vehicule_Transport_Arme"'],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "AutoCanon_AP_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_AP_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "AutoCanon_HE_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_HE_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
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
    
    "M3_ETAS_US": {
        "CommandPoints": 105,
        "availability": [4, 3, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "AutoCanon_AP_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_AP_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "AutoCanon_HE_25mm_M242_Bushmaster_Late": {
                        "new_weapon": "AutoCanon_HE_25mm_M242_Bushmaster_APDS",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "ATGM_BGM71C_ITOW_salvolength2": {
                        "new_weapon": "ATGM_BGM71C_ITOW_ETAS_IFV_salvolength2",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
            "Salves": {
                "ATGM_BGM71C_ITOW_ETAS_IFV_salvolength2": 3,
                "MMG_M240_7_62mm": 48,
            },
        },
        "UpgradeFromUnit": "LAV_MEWSS_US",
    },
    
    "M48A5_reco_NG_US": {
        "CommandPoints": 90,
        "availability": [8, 0, 0, 0],
        "UpgradeFromUnit": "M3_Bradley_CFV_US",
    },
    
    "M60A1_RISE_Passive_reco_US": {
        "CommandPoints": 90,
        "availability": [6, 0, 0, 0],
        "armor": {
            "top": (3, None),
        },
    },

    "M551A1_ACAV_Sheridan_US": {
        "CommandPoints": 50,
        "availability": [0, 6, 4, 0],
        "UpgradeFromUnit": "M113A1_TOW_US",
    },

    "M1A1_Abrams_reco_US": {
        "availability": [0, 3, 2, 0],
        "CommandPoints": 245,
        "armor": {
            "top": (5, None),
        },
        "max_speed": 70,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "UpgradeFromUnit": "M60A1_RISE_Passive_reco_US",
    },

    "OH58A_reco_NG_US": {
        "CommandPoints": 30,
        "availability": [6, 0, 0, 0],
    },

    "OH58C_Scout_US": {
        "GameName": {
            "display": "OH-58C SCOUT",
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
            "display": "OH-58D KIOWA WR.",
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

    "UH1N_TwinHuey_reco_US": {
        "CommandPoints": 70,
        "strength": 6,
        "availability": [0, 4, 3, 0], # Maybe this should be 0/3/2/0?
    },

    "EH60A_EW_US": {
        "CommandPoints": 105,
        "Divisions": {
            "add": ["US_3rd_Arm"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 0, 0],
        "UpgradeFromUnit": "UH1N_TwinHuey_reco_US",
    },
    
    "MQM_105_Aquila_US": {
        "CommandPoints": 50,
        "availability": [0, 4, 0, 0],
    },
    
    "YCQM_121A_Pave_Tiger_US": {
        "CommandPoints": 80,
    },
    
    "A37B_Dragonfly_US": {
        "CommandPoints": 70,
        "availability": [0, 3, 2, 0],
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 4550.0,
            },
        },
        "UpgradeFromUnit": "MQM_105_Aquila_US",
    },

    "OV10_Bronco_US": {
        "CommandPoints": 130,
        "availability": [0, 3, 2, 0],
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "RocketAir_Zuni_1272mm_avion_salvolength8": 2,
        #     },
        #     "equipmentchanges": {
        #         "replace": {
        #             "RocketAir_Zuni_1272mm_salvolength4": {
        #                 "new_weapon": "RocketAir_Zuni_1272mm_avion_salvolength8",
        #                 "swap_fire_effect": False,
        #                 "depiction_baked_in": False,
        #             },
        #         },
        #     },
        # },
        "UpgradeFromUnit": "A37B_Dragonfly_US",
    },
    
    "OA10A_US": {
        "CommandPoints": 220,
        "ECM": "A10_Thunderbolt_II_US",
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 2625.0,
            },
        },
        "availability": [0, 2, 0, 0],
        "UpgradeFromUnit": "OV10_Bronco_US",
    },

    "Airborne_Scout_US": {
        "GameName": {
            "display": "AIRBORNE SCOUTS",
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
            "display": "SCOUTS",
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
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
                "replace": {
                    "MMG_inf_M240B_7_62mm": {
                        "new_weapon": "SAW_M249_5_56mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },
    
    "Scout_LAI_USMC_US": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [8, 6, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "UpgradeFromUnit": None,
    },
    
    "Scout_USMC_US": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "strength": 6,
        "availability": [8, 6, 0, 0],
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
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
            },
            "Salves": {
                "insert": [(1, 30)],
            },
        },
        "UpgradeFromUnit": "Scout_LAI_USMC_US",
    },
    
    "Scout_Cav_US": { # CAVALRY SCOUTS
        "CommandPoints": 30,
        "availability": [12, 9, 0, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "MMG_WA_M60E3_7_62mm")],
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AnimateOnlyOneSoldier": True,
                        "NbWeapons": 1,
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
                "quantity": {
                    "FM_M16": 5,
                },
            },
            "Salves": {
                "insert": [(1, 45)],
            },
        },
        "UpgradeFromUnit": None,
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
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                    3: {
                        "turret_edits": {
                            "YulBoneOrdinal": 4,
                        },
                        "AmmoBoxIndex": 3,
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
                "replace": {
                    "MMG_WA_M60E3_7_62mm": {
                        "new_weapon": "MMG_M60E1_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "MMG_M60E1_7_62mm": 45,
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
                "animate": {
                    "MMG_M60E1_7_62mm": False,
                },
                "replace": {
                    "MMG_WA_M60E3_7_62mm": {
                        "new_weapon": "MMG_M60E1_7_62mm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "quantity": {
                    "FM_M16": 6,
                    "MMG_M60E1_7_62mm": 2,
                },
            },
            "Salves": {
                "MMG_M60E1_7_62mm": 45,
            },
        },
        "UpgradeFromUnit": "Scout_Cav_US",
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
        "UpgradeFromUnit": "Airborne_Scout_US",
    },

    "LRRP_US": {
        "GameName": {
            "display": "LRS",
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
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "Commando_733": {
                        "new_weapon": "M16A1_Carbine",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "M16A1_Carbine": 11,
            },
        },
        "UpgradeFromUnit": "DeltaForce_US",
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
    
    "LRRP_FOLT_US": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "ForceRecon_USMC_US": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "RocketInf_M72A3_LAW_66mm": {
                        "new_weapon": "RocketInf_AT4_83mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                        "old_new_effect": ("RocketInf_M72_LAW_66mm", "RocketInf_AT4_83mm"),
                    },
                },
            },
        },
        "UpgradeFromUnit": "Sniper_USMC_US",
    },
    
    "DeltaForce_US": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "Commando_733": {
                        "new_weapon": "M16A2_Carbine",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "M16A2_Carbine": 11,
            },
        },
        "UpgradeFromUnit": "LRRP_FOLT_US",
    },

    "Sniper_US": {
        "GameName": {
            "display": "SNIPERS",
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
    
    "Sniper_USMC_US": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "UpgradeFromUnit": "Scout_USMC_US",
    },
    
    "Sniper_M82_US": {
        "GameName": {
            "display": "SNIPERS [M82]",
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
        "CommandPoints": 55,
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
                "replace": {
                    "FM_M16": {
                        "new_weapon": "FM_M16_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "FM_M16": 11,
                "MANPAD_FIM92": 6,
            },
        },
    },

    "MANPAD_Stinger_C_Aero_US": {
        "CommandPoints": "MANPAD_Stinger_C_US",
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_M16": {
                        "new_weapon": "FM_M16_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
        "UpgradeFromUnit": "MANPAD_Stinger_C_USMC_US",
    },

    "MANPAD_Stinger_C_para_US": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "AB STINGER C",
            "token": "VVEXCPXVQB",
        },
        "CommandPoints": "MANPAD_Stinger_C_US",
        "availability": [0, 7, 5, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_M16": {
                        "new_weapon": "FM_M16_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "FM_M16": 11,
                "MANPAD_FIM92": 6,
            },
        },
    },
    
    "MANPAD_Stinger_C_USMC_US": {
        "CommandPoints": "MANPAD_Stinger_C_US",
        "GameName": {
            "display": "USMC STINGER C",
        },
        "armor": "Infantry_armor_reference",
        "availability": [7, 5, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_M16": {
                        "new_weapon": "FM_M16_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "FM_M16": 11,
                "MANPAD_FIM92": 6,
            },
        },
        "UpgradeFromUnit": "MANPAD_Stinger_C_US",
    },
    
    "MANPAD_Stinger_NG_US": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [9, 0, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_M16A1": {
                        "new_weapon": "FM_M16A1_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },
    
    "MANPAD_Redeye_US": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [12, 0, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_M16A1": {
                        "new_weapon": "FM_M16A1_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },
    
    "M42_Duster_US": {
        "CommandPoints": 50,
        "availability": [10, 0, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_Bofors_40mm_Duster": 12,
            },
        },
        "UpgradeFromUnit": "M274_Mule_M2HB_US",
    },

    "M163_CS_US": {
        "CommandPoints": 40,
        "availability": [8, 6, 0, 0],
        "UpgradeFromUnit": "M42_Duster_US",
        "WeaponDescriptor": {
            "Salves": {
                "Gatling_M61_Vulcan_20mm_noRadar": 21,
            },
        },
    },

    "M163_PIVADS_US": {
        "CommandPoints": 85,
        "TagSet": {
            "add_tags": ['"AA_radar"'],
        },
        "availability": [7, 5, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "Gatling_M61_Vulcan_20mm_late": 21,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'radar_fcs'"],
        },
    },
    
    "DCA_M167_Vulcan_20mm_nonPara_US": { # M167A1 VADS 20mm
        "CommandPoints": 40,
        "TagSet": {
            "add_tags": ['"AA_radar"'],
        },
        "Factory": "Factory/Logistic",
        "availability": [12, 9, 0, 0],
        "max_speed": 6,
        
        "WeaponDescriptor": {
            "Salves": {
                "Gatling_M61_Vulcan_20mm_TOWED": 8,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'radar_fcs'"],
        },
        "UpgradeFromUnit": "FOB_US",
    },

    "DCA_M167A2_Vulcan_20mm_US": { # M167A2 VADS 20mm
        "CommandPoints": 50,
        "TagSet": {
            "add_tags": ['"AA_radar"'],
        },
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
        
        "UpgradeFromUnit": None,
        "WeaponDescriptor": {
            "Salves": {
                "Gatling_M61_Vulcan_20mm_late_TOWED": 8,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'radar_fcs'"],
        },
    },
    
    "DCA_M167_Vulcan_20mm_US": { # AB M167A1 VADS 20mm
        "CommandPoints": 40,
        "TagSet": {
            "add_tags": ['"AA_radar"'],
        },
        "Factory": "Factory/Logistic",
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
        
        "WeaponDescriptor": {
            "Salves": {
                "Gatling_M61_Vulcan_20mm_TOWED": 8,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'radar_fcs'"],
        },
        "UpgradeFromUnit": "DCA_M167_Vulcan_20mm_nonPara_US",
        
    },
    
    "DCA_M167A2_Vulcan_20mm_Aero_US": { # AERO-M167A2 PIVADS 20mm
        "CommandPoints": 50,
        "TagSet": {
            "add_tags": ['"AA_radar"'],
        },
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
        
        "WeaponDescriptor": {
            "Salves": {
                "Gatling_M61_Vulcan_20mm_late_TOWED": 8,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'radar_fcs'"],
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
        "CommandPoints": 80,
        "strength": 6,
        "availability": [4, 3, 0, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 7800,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "M48_Chaparral_MIM72F_US": {
        "armor": {
            "front": (1, "ResistanceFamily_blindage"),
        },
        "strength": 10,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 7800,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
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
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "capacities": {
            "remove_capacities": ["reserviste"],
        },
        "strength": 10,
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
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "strength": 6,
        "availability": [5, 4, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "US_8th_Inf": {
                "Transports": ["M35_supply_trans_US"],
            },
            "US_11ACR": {
                "Transports": ["M35_supply_trans_US"],
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },
    
    "DCA_I_Hawk_USMC_US": {
        "CommandPoints": 90,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "strength": 6,
        "availability": [6, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "UpgradeFromUnit": "DCA_I_Hawk_US",
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
    
    "UH1N_TwinHuey_US": { # 10% ECM, 8 HP
        "CommandPoints": 45,
        "strength": 6,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "UH1N_TwinHuey_RKT_US": { # 10% ECM, 8 HP
        "CommandPoints": 70,
        "strength": 6,
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
    
    "CH46E_SeaKnight_trans_US": {
        "CommandPoints": 60,
        "strength": 10,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
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
    
    "CH53_Sea_Stallion_US": {
        "CommandPoints": 60,
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
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 130,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 3, 2, 0],
    },
    
    "AH1F_CNITE_US": { # 10% ECM, 4x TOW-2, 38x Hydra
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 150,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "US_11ACR": {
                "cards": 3,
            },
        },
        "availability": [0, 0, 3, 2],
    },

    "AH1F_Cobra_US": {
        "XP": {
            "pack": "helico_attack",
        },
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
        "XP": {
            "pack": "helico_attack",
        },
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
        "XP": {
            "pack": "helico_attack",
        },
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
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 4, 3, 0],
    },
    
    "AH1W_SuperCobra_Hydra_US": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 125,  
    },
    
    "AH1W_SuperCobra_AA_US": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 140,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "AA_AIM9L_Sidewinder": {
                        "new_weapon": "AA_AIM9L_Sidewinder_Helo",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },
    
    "AH1W_SuperCobra_AT_US": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 175,
    },
    
    "AH1W_SuperCobra_SEAD_US": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 150,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 175000.0,
            },
        },
    },

    "AH64_Apache_US": {  # 8x Hellfire / Hydra
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 200,
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "AH64_Apache_emp1_US": {  # 16x Hellfire
        "XP": {
            "pack": "helico_attack",
        },
        "GameName": {
            "display": "AH-64A APACHE [AT]",
        },
        "CommandPoints": 215,
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 3,
            },
        },
        "availability": [0, 2, 0, 1],
        "UpgradeFromUnit": "AH64_Apache_US",
    },

    "AH64_Apache_emp2_US": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 160,
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
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
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 230,
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 2, 0, 1],
        "UpgradeFromUnit": "AH64_Apache_emp1_US",
    },

    # US AIR
    "A37B_Dragonfly_HE_US": {
        "CommandPoints": 75,
        "availability": [0, 4, 0, 0],
    },
    
    "A37B_Dragonfly_NPLM_US": {
        "CommandPoints": 65,
        "availability": [0, 6, 0, 0],
    },
    
    "Harrier_AV8B_RKT_US": {
        "CommandPoints": 120,
        "ECM": -0.25,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "RocketAir_Zuni_1272mm_salvolength16": {
                        "new_weapon": "RocketAir_Zuni_1272mm_avion_salvolength16",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },
    
    "Harrier_AV8B_thermo_US": {
        "CommandPoints": 140,
        "ECM": -0.35,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 4, 0, 0],
    },
    
    "Harrier_AV8B_US": { # 4x Mk 83
        "CommandPoints": 150,
        "ECM": -0.35,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 4, 0, 0],
    },
    
    "Harrier_AV8B_TER_US": { # 12x Mk 82
        "CommandPoints": 150,
        "ECM": -0.35,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 4, 0, 0],
    },
    
    "A6E_Intruder_US": { # Napalm
        "CommandPoints": 150,
        "ECM": -0.25, # No room for Jammer, could make room if we wanted
        "availability": [0, 4, 0, 0],
    },
    
    "A6E_Intruder_SWIP_AT_US": {
        "CommandPoints": 210,
        "ECM": -0.35,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 4550.0,
            },
        },
        "max_speed": 1025,
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMaxPitch": 1.047198, # 60 degrees
                    "AngleRotationMinPitch": -1.047198,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 3, 0, 0],
    },
    
    "A6E_Intruder_SEAD_US": {
        "CommandPoints": 180,
        "ECM": -0.45,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 175000.0,
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMax": 0.9599311,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 1],
    },
    
    "A7D_Corsair_II_US": { # A-7D CORSAIR II [HE] (4x Mk 84)
        "CommandPoints": 230,
        "ECM": -0.35,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 0],
    },
    
    "A7D_Corsair_II_RKT_US": { # A-7D CORSAIR II [RKT] (114x Hydra)
        "CommandPoints": 160,
        "ECM": -0.25,
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            # "equipmentchanges": {
            #     "replace": {
            #         "RocketAir_Hydra_70mm_x114_avion": {
            #             "new_weapon": "RocketAir_Hydra_70mm_x114_avion",
            #             "swap_fire_effect": False,
            #             "depiction_baked_in": False,
            #         },
            #     },
            # },
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
        "CommandPoints": 210,
        "ECM": -0.35,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 0],
    },
    
    "A7D_Corsair_II_AT_US": { # A-7D CORSAIR II [AT] (4x AGM-65B)
        "CommandPoints": 240,
        "ECM": -0.35,
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_AGM65B_Maverick": 2,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
    },
    
    "EA6B_Prowler_US": {
        "CommandPoints": 280,
        "ECM": -0.60,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 12500.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 175000.0,
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMax": 0.9599311,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
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
        "SpecialtiesList": {
            "add_specs": ["'_noise_stealth'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "Bomb_GBU_27": {
                        "new_weapon": "Bomb_GBU_27_salvolength2",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True, # No need to swap depiction
                    },
                },
            },
            "Salves": {
                "Bomb_GBU_27_salvolength2": 1,
            },
        },
    },
    
    "F4E_Phantom_II_AA_US": {
        "CommandPoints": 170,
        "ECM": -0.25,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 3, 2, 0],
    },
    
    "F14A_Tomcat_AA_US": {
        "CommandPoints": 235,
        "ECM": -0.35,
        "max_speed": 1050,
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1200,
            },
        },
        "availability": [0, 2, 0, 1],
    },
    
    "F14A_Tomcat_AA2_US": {
        "CommandPoints": 340,
        "ECM": -0.35,
        "availability": [0, 2, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AA_AIM54_Phoenix": 2,
            },
        },
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
        "CommandPoints": 310,
        "ECM": -0.45,
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1375,
            },
        },
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AA_AIM9M_Sidewinder": 4,
            },
        },
    },
    
    "F15E_StrikeEagle_US": {
        "CommandPoints": 310,
        "GameName": {
            "display": "F-15E STRIKE EAGLE [PGB]",
        },
        "max_speed": 1325,
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
        "CommandPoints": 180,
        "ECM": -0.35,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 175000.0,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMax": 0.9599311,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "F4E_Phantom_II_HE_US": {
        "CommandPoints": 175,
        "ECM": -0.25,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 2, 0, 0],
    },


    "F4E_Phantom_II_CBU_US": {
        "CommandPoints": 220,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 2, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength2": {
                        "new_weapon": "Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength5",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
    },

    "F4E_Phantom_II_napalm_US": {
        "CommandPoints": 175,
        "ECM": -0.25,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 3, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "Bomb_Mk77_340kg_Napalm_salvolength2": {
                        "new_weapon": "Bomb_Mk77_340kg_Napalm_salvolength5",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                        "old_new_effect": ("Bomb_Mk77_340kg_Napalm_x2", "Bomb_Mk77_340kg_Napalm_x4"),
                    },
                },
            },
        },
    },

    "F111E_Aardvark_US": {  # 12x mk82, 3rd Armored
        "CommandPoints": 220,
        "ECM": -0.40,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "F111F_Aardvark_US": {
        "CommandPoints": 220,
        "ECM": -0.40,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "F111F_Aardvark_LGB_US": {  # 4x GBU-12
        "CommandPoints": 260,
        "GameName": {
            "display": "F-111F AARDVARK [PGB]",
        },
        "ECM": -0.50,
        "WeaponDescriptor": {
            "Salves": {
                "Bomb_GBU_12_salvolength4": 1,
            },
            "equipmentchanges": {
                "replace": {
                    "Bomb_GBU_12_salvolength2": {
                        "new_weapon": "Bomb_GBU_12_salvolength4",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
    },
    
    "F111F_Aardvark_LGB2_US": { # 4x GBU-10
        "CommandPoints": 310,
        "GameName": {
            "display": "F-111F AARDVARK [PGB2]",
        },
        "ECM": -0.50,
        "UpgradeFromUnit": "F111F_Aardvark_LGB_US",
        "WeaponDescriptor": {
            "Salves": {
                "Bomb_GBU_10_salvolength4": 1,
            },
            "equipmentchanges": {
                "replace": {
                    "Bomb_GBU_10_salvolength2": {
                        "new_weapon": "Bomb_GBU_10_salvolength4",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
    },

    "F111E_Aardvark_CBU_US": {  # 8x Mk-20 Rockeye, 3rd Armored
        "CommandPoints": 210,
        "ECM": -0.40,
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

    "F111F_Aardvark_CBU_US": {  # 24x Mk-20 Rockeye
        "CommandPoints": 280,
        "ECM": -0.50,
        "availability": [0, 2, 0, 0],
        "alternatives": {
            "mesh": "F111F_Sweep40_US",
        },
        "WeaponDescriptor": {
            "Salves": {
                "insert": [(1, 1)],
            },
            "SalvoIsMainSalvo": [True, True],
            "turrets": {
                0: {
                    "Tag": '"tourelle1"',
                    "YulBoneOrdinal": 1,
                },
            },
            "equipmentchanges": {
                "replace": {
                    "Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength8": {
                        "new_weapon": "Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength12",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "insert": [(1, "Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength12")],
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "Tag": '"tourelle2"',
                            "YulBoneOrdinal": 2,
                        },
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'", "'_jammer_air'"],
        },
    },

    "F111E_Aardvark_napalm_US": {  # 4x Mk-77 napalm, 3rd Armored
        "CommandPoints": 220,
        "ECM": -0.40,
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
                "replace": {
                    "Bomb_Mk77_340kg_Napalm_salvolength4": {
                        "new_weapon": "Bomb_Mk77_340kg_Napalm_salvolength8",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                        "old_new_effect": ("Bomb_Mk77_340kg_Napalm_x4", "Bomb_Mk77_340kg_Napalm_x6"),
                    },
                },
            },
        },
    },

    "F111F_Aardvark_napalm_US": {  # 4x Mk-77 napalm, 82nd Airborne
        "CommandPoints": 220,
        "ECM": -0.40,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 3, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "Bomb_Mk77_340kg_Napalm_salvolength4": {
                        "new_weapon": "Bomb_Mk77_340kg_Napalm_salvolength8",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                        "old_new_effect": ("Bomb_Mk77_340kg_Napalm_x4", "Bomb_Mk77_340kg_Napalm_x6"),
                    },
                },
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
                "EOpticalStrength/AntiRadar": 175000.0,
            },
        },
        "availability": [0, 0, 2, 0],
    },

    "F16C_LGB_US": {
        "CommandPoints": 240,
        "GameName": {
            "display": "F-16CG [PGB]",
        },
        "ECM": -0.35,
        "WeaponDescriptor": {
            "Salves": {
                "Bomb_GBU_12_salvolength2": 1,
            },
            "equipmentchanges": {
                "replace": {
                    "Bomb_GBU_12": {
                        "new_weapon": "Bomb_GBU_12_salvolength2",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 0, 0, 1],
        "UpgradeFromUnit": "F16E_TER_HE_US",
    },

    "F16E_AGM_US": {  # 4x AGM-65D, 2x AIM-9M
        "CommandPoints": 275,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_AGM65D_Maverick": 2,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
    },
    
    "FA16_CAS_US": {
        "CommandPoints": 240,
        "ECM": -0.25,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "AA_AIM9L_Sidewinder": {
                        "new_weapon": "AA_AIM9M_Sidewinder",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "AGM_AGM65D_Maverick": (2, False),
            },
        },
    },

    "F16E_HE_US": {
        "CommandPoints": 200,
        "ECM": -0.25,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 2, 0, 0],
    },

    "F16E_TER_HE_US": {  # 12x mk82 + 2x AIM-9M
        "CommandPoints": 230,
        "ECM": -0.35,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 2, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
    },

    "F16E_napalm_US": {
        "CommandPoints": 200,
        "ECM": -0.25,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "Bomb_Mk77_340kg_Napalm_salvolength2": {
                        "new_weapon": "Bomb_Mk77_340kg_Napalm_salvolength4",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                        "old_new_effect": ("Bomb_Mk77_340kg_Napalm_x2", "Bomb_Mk77_340kg_Napalm_x4"),
                    },
                },
            },
        },
    },

    "F16E_SEAD_US": { # AGM-88 5950m
        "CommandPoints": 220,
        "ECM": -0.45,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 175000.0,
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "AngleRotationMax": 0.9599311,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "availability": [0, 2, 0, 1],
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
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
        "ECM": -0.25,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "WeaponDescriptor": {
            "SalvoIsMainSalvo": [False, False, False],
            "Salves": {
                "AA_AIM9M_Sidewinder": 4,
            },
        },
        "availability": [0, 2, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
    },
    
    "F16E_TER_CLU_US": {
        "CommandPoints": 270,
        "alternatives": {
            "mesh": "F16E_TER_2T_US",
        },
        "ECM": -0.35,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 2, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "insert": [(2, 1)],
            },
            "SalvoIsMainSalvo": [False, True, True, False],
            # "turrets": {
            #     0: {
            #         "Tag": '"tourelle1"',
            #         "YulBoneOrdinal": 1,
            #     },
            # },
            "equipmentchanges": {
                "replace": {
                    "Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength8": {
                        "new_weapon": "Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength6",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "insert": [(2, "Bomb_CBU_Mk20_Rockeye_II_250kg_salvolength6")],
                "insert_edits": {
                    2: {
                        "turret_edits": {
                            "Tag": '"tourelle3"',
                            "YulBoneOrdinal": 3,
                        },
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                    3: {
                        "turret_edits": {
                            "Tag": '"tourelle4"',
                            "YulBoneOrdinal": 4,
                        },
                        "AmmoBoxIndex": 3,
                        "HandheldEquipmentKey": "'WeaponAlternative_4'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_4'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_4'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_4"],
                    },
                },
            },
        },
    },

    "F16E_AA_US": {
        "CommandPoints": 200,
        "ECM": -0.25,
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
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 0, 2, 0],
        "UpgradeFromUnit": None,
    },

    "F16E_AA2_US": {  # 3x + 3x AIM-9M
        "CommandPoints": 180,
        "ECM": -0.25,
        "Divisions": {
            "remove": ["US_11ACR"],
            "add": ["US_8th_Inf"],
            "default": {
                "cards": 1,
            },
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 13250,
            },
        },
        "availability": [0, 3, 2, 0],
        "UpgradeFromUnit": "F16E_AA_US",
    },

    "F18_Hornet_AA_US": {  # 4x AIM-7P, 2x AIM-9M
        "GameName": {
            "display": "F/A-18A HORNET [AA2]", # Intentionally reversed
        },
        "CommandPoints": 265,
        "ECM": -0.45,
        "availability": [0, 2, 0, 1],
        "UpgradeFromUnit": "F18_Hornet_AA2_US", # Intentionally reversed
    },

    "F18_Hornet_AA2_US": {  # 2x AIM-7M, 6x AIM-9M 
        "GameName": {
            "display": "F/A-18A HORNET [AA]", # Intentionally reversed
        },
        "CommandPoints": 250,
        "ECM": -0.45,
        "availability": [0, 2, 0, 1],
        "UpgradeFromUnit": None, # Intentionally reversed
    },

    "F18_Hornet_SEAD_US": {  # 2x AIM-7M, 2x AIM-9M, 2x AGM-88 HARM
        "CommandPoints": 290,
        "ECM": -0.55,
        "availability": [0, 2, 0, 1],
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 6125.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 175000.0,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                3: {
                    "AngleRotationMax": 0.9599311,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "UpgradeFromUnit": "F18_Hornet_AA_US", # Intentionally reversed
    },

    "A10_Thunderbolt_II_US": {  # 8x mk.82, 2x AIM-9M
        "CommandPoints": 230,
        "max_speed": 500,
        "ECM": -0.25,
        "availability": [0, 2, 0, 0],
    },

    "A10_Thunderbolt_II_Rkt_US": {  # 76x Hydra, 2x AIM-9M
        "CommandPoints": 240,
        "max_speed": 500,
        "ECM": "A10_Thunderbolt_II_US",
        "availability": [0, 2, 0, 0],
    },

    "A10_Thunderbolt_II_ATGM_US": {  # 4x AGM-65D, 2x AIM-9M
        "CommandPoints": 260,
        "max_speed": 500,
        "ECM": "A10_Thunderbolt_II_US",
        "availability": [0, 2, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_AGM65D_Maverick": 2,
            },
        },
    },
}
