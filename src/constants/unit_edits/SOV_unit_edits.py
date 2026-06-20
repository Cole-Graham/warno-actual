"""Soviet unit edits."""

# from typing import Any, Dict

# fmt: off
sov_unit_edits = {
    #SOV LOG
    "UAZ_469_CMD_SOV": { # BELOZOR
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    
    "UAZ_469_CMD_Naval_SOV": { # MORSKAYA BELOZOR
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    
    "BMP_1_CMD_POTOK2_SOV": {
        "CommandPoints": 155,
        "availability": [0, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "UpgradeFromUnit": "MTLB_CMD2_SOV",
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    
    "BMD_1_CMD_SOV": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 0, 3, 0],
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    
    "BMD_1K_CMD_SOV": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 3, 0, 0],
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },

    "BMP_1_CMD_SOV": {
        "CommandPoints": 170,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 0, 3, 0],
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },

    "BMD_2_CMD_SOV": {
        "CommandPoints": 175,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 0, 3, 0],
        "TagSet": {"add_tags": ['"CMD_Unit"']},
        
    },

    "LUAZ_967M_CMD_VDV_SOV": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'", '_para'],
        },
        "ButtonTexture": "LUAZ_967M_SOV",
        "DeploymentShift": 0,
        "UpgradeFromUnit": "UAZ_469_CMD_SOV",
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    
    "UAZ_469_CMD_VDV_SOV": { # Desant. Belozor
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "DeploymentShift": 0,
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },

    "BMP_2_CMD_SOV": {
        "CommandPoints": 185,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 0, 3, 0],
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    
    "BRDM_2_CMD_SOV": {
        "CommandPoints": 155,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "strength": 8,
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 3, 0, 0],
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },

    "BTR_60_CMD_SOV": {
        "CommandPoints": 175,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "strength": 10,
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 0, 3, 0],
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },

    "BTR_80_CMD_SOV": {
        "CommandPoints": 185,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "strength": 10,
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 0, 3, 0],
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },

    "Mi_8K_CMD_SOV": {
        "CommandPoints": 145,
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
    },

    # SOV INF
    "MotRifles_CMD_SOV": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOTOSTRELKI",
            # "token": "ZJRMUWLPVH",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_IFV",
                "UNITE_MotRifles_CMD_SOV",
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
                'leader_sov',
                '_ifv',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_157_Rifle": {
                "cards": 1,
            },
            "SOV_25_Tank": {
                "cards": 2,
            },
            "SOV_39_Gds_Rifle": {
                "cards": 3,
            },
            "SOV_6IndMSBrig": {
                "cards": 1,
            },
            "SOV_79_Gds_Tank": {
                "cards": 2,
            },
        },
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 5,
                },
            },
            "Salves": {
                "RocketInf_RPG22_72_5mm": 6,
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "remove_zone_capture": None,
    },
    
    "MotRifles_CMD_TTsko_SOV": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOTOSTRELKI",
            # "token": "ZJRMUWLPVH",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_IFV",
                "UNITE_MotRifles_CMD_TTsko_SOV",
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
                'leader_sov',
                '_ifv',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_27_Gds_Rifle": {
                "Transports": [
                    'GAZ_66_SOV',
                    'BTR_80_SOV',
                    'BMP_1P_SOV',
                    'BMP_2AG_SOV',
                    'BMP_3_SOV',
                ],
            },
        },
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 5,
                },
            },
            "Salves": {
                "RocketInf_RPG22_72_5mm": 6,
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "remove_zone_capture": None,
    },

    "Engineers_CMD_TTsko_SOV": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SAPERY",
            # "token": "QCNBGTPZWL",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Engineers_CMD_TTsko_SOV",
                "Unite"
            ],
        },
        "strength": 8,
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "Divisions": {
            "SOV_27_Gds_Rifle": {
                "Transports": ["GAZ_66_SOV", "MTLB_transp_SOV"],
            },
        },
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 8,
                },
            },
            "Salves": {
                "RocketInf_RPG18_64mm": 7,
            },
        },
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "remove_zone_capture": None,
    },

    "Engineers_CMD_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SAPERY [RPG-7]",
            # "token": "AGYMPGDUXA",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Engineers_CMD_SOV",
                "Unite"
            ],
        },
        "strength": 8,
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "Divisions": {
            "SOV_119IndTkBrig": {
                "Transports": ["GAZ_66_SOV", "BTR_60_SOV"],
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 8,
                },
            },
        },
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "remove_zone_capture": None,
    },

    "Spetsnaz_CMD_SOV": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SPETSNAZ",
            # "token": "CKLQCEBSOY",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Spetsnaz_CMD_SOV",
                "Unite",
                "noSIGINT",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry_sf", "Texture_sf"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_sf',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry_sf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "SOV_119IndTkBrig": {
                "Transports": ["GAZ_66B_SOV", "BTR_60_SOV"],
            },
        },
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "remove_zone_capture": None,
    },

    "VDV_CMD_SOV": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "DESANTNIKI",
            # "token": "JSBZIJKKJJ",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_IFV",
                "UNITE_VDV_CMD_SOV",
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
                'leader_sov',
                '_ifv',
                '_choc',
                '_para',
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
        "availability": [0, 0, 4, 3],
        "max_speed": 20,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_AKSU_74": 5,
                },
            },
            "Salves": {
                "PM_AKSU_74": 7,
                "SAW_RPK_74_5_56mm": 18,
                "MANPAD_igla": 4,
                "Grenade_SMOKE": 3,
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "remove_zone_capture": None,
    },
    
    "DShV_CMD_SOV": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "DSh.",
            # "token": "JSBZIJKKJJ",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_DShV_CMD_SOV",
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
                'leader_sov',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_AKSU_74": 5,
                },
            },  
        },
    },

    "Engineers_CMD_VDV_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "DESANT. SAPERY",
            # "token": "SWFVKVIZVT",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Engineers_CMD_TTsko_SOV",
                "Unite"
            ],
        },
        "strength": 8,
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_choc',
                '_para',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AKS_74": 8,
                },
            },
            "Salves": {
                "FM_AKS_74": 11,
                "RocketInf_RPG7": 6,
            },
        },
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "remove_zone_capture": None,
    },

    "KGB_BorderGuard_CMD_SOV": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "POGRANVOISK KGB",
            "token": "LLUPBPHFST",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Standard",
                "UNITE_KGB_BorderGuard_CMD_SOV",
                "Unite",
            ],
        },
        "strength": 9,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 9,
                },
            },
            "Salves": {
                "FM_AK_74": 11,
            },
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
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
    
    "Naval_Rifle_CMD_SOV": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOR. PEKHOTA KOM.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Naval_Rifle_CMD_SOV",
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
                'leader_sov',
                '_resolute',
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
        "availability": [0, 0, 4, 3],
        "max_speed": 20,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_AKSU_74": 5,
                },
            },
        },
        "selector_tactic": "(2, 5)",
        "selector_tactic_obj": "02_05",
        "remove_zone_capture": None,
    },
    
    "Naval_VDV_CMD_SOV": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "DESANT. MOR. KOMROTI",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Naval_VDV_CMD_SOV",
                "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_resolute',
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
        "availability": [0, 0, 6, 4],
        "max_speed": 26,
        "remove_zone_capture": None,
    },
    
    "Engineers_CMD_Naval_SOV": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOR. SAPERI KOMROTI",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Engineers_CMD_Naval_SOV",
                "Unite",
            ],
        },
        "strength": 8,
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_resolute',
                '_choc',
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
            "equipmentchanges": {
                "quantity": {
                    "FM_AKS_74": 8,
                },
            },
        },
        "selector_tactic": "(2, 5)",
        "selector_tactic_obj": "02_05",
        "remove_zone_capture": None,
    },

    "Engineers_SOV": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SAPERY",
        },
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_119IndTkBrig": {
                "cards": 2,
            },
        },
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 36,
                "Grenade_Satchel_Charge": 5,
            },
        },
        "UpgradeFromUnit": "Engineers_CMD_SOV"
    },

    "Engineers_TTsko_SOV": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SAPERY",
        },
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 36,
                "Grenade_Satchel_Charge": 5,
            },
        },
    },

    "Engineers_Reserve_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 35,
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "UpgradeFromUnit": "Engineers_Flam_SOV"
    },


    "Engineers_VDV_SOV": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "DESANT. SAPERY",
        },
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_RPK_74_5_56mm": False,
                },
                "quantity": {
                    "FM_AKS_74": 3,
                    "SAW_RPK_74_5_56mm": 2,
                },
            },
            "Salves": {
                "Grenade_Satchel_Charge": 4,
            },
        },
    },
    
    "Engineers_DShV_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_RPK_74_5_56mm": False,
                },
                "quantity": {
                    "FM_AKS_74": 3,
                    "SAW_RPK_74_5_56mm": 2,
                },
            },
            "Salves": {
                "Grenade_Satchel_Charge": 4,
            },
        },
    },
    
    "Engineers_Naval_SOV": {
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 9, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_RPK_74_5_56mm": False,
                },
                "quantity": {
                    "FM_AKS_74": 3,
                    "SAW_RPK_74_5_56mm": 2,
                },
            },
            "Salves": {
                "Grenade_Satchel_Charge": 4,
            },
        },
    },

    "Engineers_Flam_SOV": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SAPERY [RPO]",
        },
        "CommandPoints": 55,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_119IndTkBrig": {
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
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 36,
                "RocketInf_RPO_A_93mm": 4,
            },
        },
    },

    "Engineers_Flam_TTsko_SOV": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SAPERY [RPO]",
        },
        "CommandPoints": 55,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 36,
                "RocketInf_RPO_A_93mm": 4,
            },
        },
    },

    "Engineers_Flam_Reserve_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 35,
        "availability": [8, 0, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "Engineers_Reserve_SOV"
    },

    "Engineers_Flam_VDV_SOV": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "DESANT. SAPERY [RPO]",
        },
        "CommandPoints": 45,
        "availability": [0, 9, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 11,
            },
        },
    },
    
    "Engineers_Flam_DShV_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 45,
        "availability": [0, 9, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 11,
            },
        },
    },
    
    "Engineers_Flam_Naval_SOV": {
        "CommandPoints": 45,
        "availability": [0, 9, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "MotRifles_SOV": { # MOTOPEKHOTA
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOTOPEKHOTA",
        },
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "SOV_119IndTkBrig": {
                "cards": 2,
            },
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "availability": [10, 7, 0, 0],
        "strength": 8,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_RPK_74_5_56mm": False,
                },
                "quantity": {
                    "FM_AK_74": 6,
                    "SAW_RPK_74_5_56mm": 2,
                },
            },
        },
    },

    "MotRifles_RPG22_SOV": { # MOTOPEKHOTA [RPG-22]
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOTOPEKHOTA [RPG-22]",
        },
        "CommandPoints": 25,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "strength": 8,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 7,
                },
            },
            "Salves": {
                "FM_AK_74": 11,
                "SAW_RPK_74_5_56mm": 18,
                "RocketInf_RPG22_72_5mm": 6,
            },
        },
        "availability": [10, 7, 0, 0],
    },

    "MotRifles_TTsko_SOV": {  # MOTOSTRELKI [RPG-27]
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOTOSTRELKI [RPG-27]",
        },
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [12, 9, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "UpgradeFromUnit": "MotRifles_RPG7VL_TTsko_SOV",
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "SAW_RPK_74_5_56mm": 18,
                "RocketInf_RPG27_105mm": 5,
            },
        },
    },

    "MotRifles_BTR_TTsko_SOV": {  # MOTOSTRELKI [RPG-26]
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOTOSTRELKI [RPG-26]",
        },
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle": {
                "cards": 2,
                "Transports": ["GAZ_66_SOV", "BMP_1P_SOV"],
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_ifv'"],
        },
        "UpgradeFromUnit": "MotRifles_CMD_TTsko_SOV",
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "SAW_RPK_74_5_56mm": {
                        "new_weapon": "MMG_PKM_7_62mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 36,
                "RocketInf_RPG26_72_5mm": 6,
            },
        },
    },
    
    "MotRifles_MVD_SOV": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOTOSTRELKI MVD",
        },
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "MotRifles_BTR_SOV": {  # MOTOPEKHOTA [RPG-7VR]
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOTOPEKHOTA [RPG-7VR]",
        },
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'", "'_ifv'"],
        },
        "UpgradeFromUnit": "MotRifles_SOV",
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_PKM_7_62mm": False,
                },
                "quantity": {
                    "FM_AK_74": 6,
                    "MMG_PKM_7_62mm": 2,
                },
                "replace": {
                    "SAW_RPK_74_5_56mm": {
                        "new_weapon": "MMG_PKM_7_62mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 36,
            },
        },
    },
    
    "MotRifles_RPG7VS_SOV": { # MOTOPEKHOTA [RPG-7VS]
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOTOPEKHOTA [RPG-7VS]",
        },
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "strength": 8,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 7,
                },
            },
            "Salves": {
                "FM_AK_74": 11,
                "SAW_RPK_74_5_56mm": 18,
                "RocketInf_RPG7VS_85mm": 6,
            },
        },
    },

    "MotRifles_Metis_TTsko_SOV": { # MOTOSTRELKI [METIS]
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOTOSTRELKI [METIS]",
        },
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "strength": 7,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 6,
                },
            },
            "Salves": {
                "FM_AK_74": 11,
                "SAW_RPK_74_5_56mm": 18,
                "ATGM_9K115_Metis": 6,
            },
        },
        "UpgradeFromUnit": "MotRifles_TTsko_SOV",
    },

    "MotRifles_Metis_SOV": { # MOTOPEKHOTA [METIS]
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOTOPEKHOTA [METIS]",
        },
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "MotRifles_BTR_SOV",
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "SAW_RPK_74_5_56mm": 18,
                "ATGM_9K115_Metis": 6,
            },
        },
    },

    "VDV_Mech_SOV": {  # RPK, SVD, RPG-7VL
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "DESANTNIKI [SVD]",
        },
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 2,
            },
            "SOV_76_VDV": {
                "cards": 3,
            },
        },
        "availability": [0, 8, 6, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 11,
            },
        },
    },

    "VDV_SOV": {  # 2x RPK, SVD, RPG-7VR
        "armor": "Infantry_armor_reference",
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 3,
            },
            "SOV_76_VDV": {
                "cards": 2,
            },
        },
        "availability": [0, 8, 6, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "strength": 9,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_RPK_74_5_56mm": False,
                },
                "quantity": {
                    "FM_AKS_74": 7,
                    "SAW_RPK_74_5_56mm": 2,
                },
            },
            "Salves": {
                "FM_AKS_74": 11,
            },
        },
    },

    "VDV_Combine_SOV": {  # RPK, RPG-22, RPG-7VL
        "armor": "Infantry_armor_reference",
        "CommandPoints": 45,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 11,
                "RocketInf_RPG22_72_5mm": 4,
            },
        },
    },

    "VDV_Afgantsy_SOV": {
        "CommandPoints": 35,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "armor": "Infantry_armor_reference",
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "SAW_RPK_74_5_56mm": {
                        "new_weapon": "MMG_PKM_7_62mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "MMG_PKM_7_62mm": 36,
            },
        },
    },
    
    "DShV_Afgantsy_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 60,
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "VDV_Metis_SOV": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "DESANTNIKI [METIS]",
        },
        "CommandPoints": 45,
        "availability": [0, 7, 5, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "VDV_Afgantsy_RPG7VL_SOV",
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_RPK_74_5_56mm": False,
                },
                "quantity": {
                    "FM_AKS_74": 5,
                    "SAW_RPK_74_5_56mm": 2,
                },
            },
            "Salves": {
                "FM_AKS_74": 11,
                "ATGM_9K115_Metis": 6,
            },
        },
    },
    
    "DShV_Metis_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 45,
        "availability": [0, 7, 5, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "DShV_SOV": { # DSh. [RPG-7], 1x RPK-74 , SVD, RPG-7VL
        "CommandPoints": 40,
        "availability": [0, 8, 6, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "strength": 8,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AKS_74": 6,
                },
            },
        },
    },
    
    "DShV_RPG16_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 35,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "DShV_Hvy_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 55,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AKS_74": 11,
                    "SAW_RPK_74_5_56mm": 3,
                },
            },
        },
    },

    "Reserve_SOV": { # Rez. 9 AK74, 1 RPK, RPG-7VM
        "CommandPoints": 35,
        "availability": [12, 0, 0, 0],
        "strength": 10,
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 9,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Partisan_SOV": { # Rez. 8 AKM, 1 DP28, RPG-2
        "CommandPoints": 30,
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "MP_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 12, 9, 0],
        "max_speed": 26,
        "strength": 8,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            # Mixed-model loadout: 5 MP_SOV + 3 Reserve_SOV
            # Vanilla turrets: T0=FM_AK_74 (qty=4)
            # Target turrets:  T0=FM_AK_74(x5), T1=SAW_RPK_74_5_56mm(x2 animate=True),
            #                  T2=RocketInf_RPG7(x1 animate=True)
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 6,
                },
                "insert": [
                    (1, "SAW_RPK_74_5_56mm"),
                    (2, "RocketInf_RPG7"),
                ],
                "insert_edits": {
                    1: {  # SAW_RPK (newly inserted, donor Reserve_SOV)
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                    2: {  # RocketInf_RPG7 (newly inserted, donor Reserve_SOV)
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
            # Vanilla Salves: [FM_AK_74=104]. Target: [11, 18, 4].
            "Salves": {
                "FM_AK_74": 11,
                "insert": [
                    (1, 18),
                    (2, 4),
                ],
            },
        },
    },
    
    "MP_Combat_SOV": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [0, 8, 6, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "KGB_BorderGuard_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "KGB_BorderGuard_Aero_SOV": {
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "VDV_HMG_SOV": {  # Desant.Pulemetchiki
        "armor": "Infantry_armor_reference",
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "DShV_HMG_SOV": { # DSh. Pulemetchiki
        "armor": "Infantry_armor_reference",
        "CommandPoints": 35,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "MotRifles_HMG_SOV": {  # Pulemetchiki
        "GameName": {
            "display": "PULEMETCHIKI [BTR]",
        },
        "armor": "Infantry_armor_reference",
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 36,
                "RocketInf_RPG22_72_5mm": 6,
            },
        },
    },

    "MotRifles_HMG_TTsko_SOV": {  # Pulemetchiki
        "armor": "Infantry_armor_reference",
        "CommandPoints": 35,
        "strength": 8,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 5,
                },
            },
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 36,
                "RocketInf_RPG22_72_5mm": 6,
            },
        },
    },

    "Reserve_HMG_SOV": {  # Rez. Pulemetchiki
        "armor": "Infantry_armor_reference",
        "CommandPoints": 25,
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "FireSupport_TTsko_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [12, 9, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPG29_105mm": 6,
            },
        },
    },
    
    "FireSupport_Naval_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [12, 9, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPG29_105mm": 6,
            },
        },
    },
    
    "OMON_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_RPK_74_5_56mm": False,
                },
                "quantity": {
                    "PM_AKSU_74": 5,
                    "SAW_RPK_74_5_56mm": 2,
                },
            },
        },
    },
    
    "URSN_SOV": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 6, 4],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Spetsnaz_SOV": {
        "CommandPoints": 75,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPO_A_93mm": 4,
            },
        },
    },
    
    "Spetsnaz_Naval_SOV": {
        "CommandPoints": 75,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "RocketInf_RPO_A_93mm": {
                        "new_weapon": "RocketInf_RPO_RYS",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "RocketInf_RPO_RYS": 6,
            },
        },
    },

    "Spetsnaz_Vympel_SOV": {  # Spetsgruppa Vympel
        "CommandPoints": 75,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "PM_AKSU_74": 9,
                "RocketInf_RPG27_105mm": 6,
            },
        },
    },

    "Spetsnaz_FireSupport_SOV": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 8, 6],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPG29_105mm": 6,
            },
        },
    },
    
    "Naval_Rifle_Reserve_SOV": {
        "CommandPoints": 25,
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Naval_Rifle_RPG22_SOV": {
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Naval_Rifle_SVD_SOV": {
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "UpgradeFromUnit": "Naval_Rifle_RPG22_SOV",
    },
    
    "Naval_Rifle_SOV": { # RPG-7VR
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_RPK_74_5_56mm": False,
                },
                "quantity": {
                    "FM_AKS_74": 7,
                    "SAW_RPK_74_5_56mm": 2,
                },
            },
            "Salves": {
                "FM_AKS_74": 11,
                "RocketInf_RPG7VR_64mm": 7,
            },
        },
        "UpgradeFromUnit": "Naval_Rifle_SVD_SOV",
    },
    
    "Naval_Rifle_Hvy_SOV": {
        "CommandPoints": 50,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPG7VL": 9,
            },
        },
        "UpgradeFromUnit": "Naval_Rifle_SOV",
    },
    
    "Naval_VDV_Reserve_SOV": {
        "CommandPoints": 40,
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_RPK_74_5_56mm": False,
                },
                "quantity": {
                    "FM_AKS_74": 9,
                    "SAW_RPK_74_5_56mm": 2,
                },
            },
        },
    },
    
    "Naval_VDV_SOV": {
        "CommandPoints": 40,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_RPK_74_5_56mm": False,
                },
                "quantity": {
                    "FM_AKS_74": 7,
                    "SAW_RPK_74_5_56mm": 2,
                },
            },
            "Salves": {
                "RocketInf_RPG7": 7,
            },
        },
    },
    
    "HMGteam_Maxim_Reserve_SOV": {
        "CommandPoints": "HMGteam_M60_NG_US",
        "strength": "HMGteam_M60_NG_US",
        "max_speed": "HMGteam_M60_NG_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_NG_US",
        },
    },

    "HMGteam_PKM_SOV": {
        "CommandPoints": "HMGteam_M60_US",
        "GameName": {
            "display": "PKM 7.62mm",
        },
        "strength": "HMGteam_M60_US",
        "max_speed": "HMGteam_M60_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_US",
        },    
    },

    "HMGteam_PKM_TTsko_SOV": {
        "CommandPoints": "HMGteam_M60_US",
        "GameName": {
            "display": "PKM 7.62mm",
        },    
        "strength": "HMGteam_M60_US",
        "max_speed": "HMGteam_M60_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_US",
        },
    },

    "HMGteam_PKM_VDV_SOV": {
        "CommandPoints": "HMGteam_M60_AB_US",
        "GameName": {
            "display": "DESANT. PKM 7.62mm",
        },
        "strength": "HMGteam_M60_AB_US",
        "max_speed": "HMGteam_M60_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_AB_US",
        },
    },

    "HMGteam_PKM_DShV_SOV": {
        "GameName": {
            "display": "DSh PKM 7.62mm",
        },
    },
    
    "HMGteam_PKM_Naval_VDV_SOV": {
        "CommandPoints": "HMGteam_M60_AB_US",
        "strength": "HMGteam_M60_AB_US",
        "max_speed": "HMGteam_M60_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_AB_US",
        },
    },

    "HMGteam_NSV_SOV": {
        "CommandPoints": "HMGteam_M2HB_US",
        "GameName": {
            "display": "NSV 12.7mm",
        },
        "strength": "HMGteam_M2HB_US",
        "max_speed": "HMGteam_M2HB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_US",
        },
        "UpgradeFromUnit": "HMGteam_DShK_AA_SOV",
    },

    "HMGteam_NSV_TTsko_SOV": {
        "CommandPoints": "HMGteam_M2HB_US",
        "GameName": {
            "display": "NSV 12.7mm",
        },
        "strength": "HMGteam_M2HB_US",
        "max_speed": "HMGteam_M2HB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_US",
        },
    },

    "HMGteam_NSV_DShV_SOV": {
        "CommandPoints": "HMGteam_M2HB_US",
        "GameName": {
            "display": "DSh NSV 12.7mm",
        },
        "strength": "HMGteam_M2HB_US",
        "max_speed": "HMGteam_M2HB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_US",
        },
    },

    "HMGteam_NSV_VDV_SOV": {
        "CommandPoints": "HMGteam_M2HB_AB_US",
        "GameName": {
            "display": "DESANT. NSV 12.7mm",
        },
        "strength": "HMGteam_M2HB_AB_US",
        "max_speed": "HMGteam_M2HB_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_AB_US",
        },
    },

    "HMGteam_NSV_6U6_VDV_SOV": { # Défense Contre Avions
        "is_standard": (True, "Para_DCA_12_7_HMG_Team"), 
        "CommandPoints": 25,
        "GameName": {
            "display": "DESANT. 6U6 12.7mm",
        },
        "strength": 5,
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },
    
    "HMGteam_DShK_AA_SOV": {
        "CommandPoints": "HMGteam_M2HB_M63_UK",
        "GameName": {
            "display": "REZ. DShK 12.7mm (AA)",
        },
        "strength": "HMGteam_M2HB_M63_UK",
        "max_speed": "HMGteam_M2HB_M63_UK",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_M63_UK",
        },
        "UpgradeFromUnit": "HMGteam_PKM_SOV",
    },

    "HMGteam_AGS17_SOV": {
        "is_standard": (True, "30mm_AGS17_Team"), 
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "strength": 5,
        "max_speed": 14,
        "availability": [0, 10, 7, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "UpgradeFromUnit": "HMGteam_NSV_SOV",
    },

    "HMGteam_AGS17_TTsko_SOV": {
        "CommandPoints": "HMGteam_AGS17_SOV",
        "strength": "HMGteam_AGS17_SOV",
        "max_speed": "HMGteam_AGS17_SOV",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 10, 7, 0],
        "SpecialtiesList": {
            "add_specs": "HMGteam_AGS17_SOV",
        },
    },
    
    "HMGteam_AGS17_DShV_SOV": {
        "CommandPoints": "HMGteam_AGS17_SOV",
        "strength": "HMGteam_AGS17_SOV",
        "max_speed": "HMGteam_AGS17_SOV",
        "SpecialtiesList": {
            "add_specs": "HMGteam_AGS17_SOV",
        },
    },

    "HMGteam_AGS17_VDV_SOV": {
        "is_standard": (True, "Para_30mm_AGS17_Team"), 
        "CommandPoints": 30,
        "strength": 5,
        "max_speed": 14,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 10, 7, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },
    
    "HMGteam_AGS17_Naval_SOV": {
        "CommandPoints": "HMGteam_AGS17_SOV",
        "strength": "HMGteam_AGS17_SOV",
        "max_speed": "HMGteam_AGS17_SOV",
        "SpecialtiesList": {
            "add_specs": "HMGteam_AGS17_SOV",
        },
        "availability": [10, 7, 0, 0],
    },

    "ATteam_RCL_SPG9_VDV_SOV": {
        "strength": 5,
        "CommandPoints": 30,
        "availability": [0, 10, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "ATteam_RCL_SPG9_SOV": {
        "strength": 5,
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "FireSupport_TTsko_SOV",
    },
    
    "ATteam_RCL_SPG9_Naval_SOV": {
        "strength": 5,
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "FireSupport_Naval_SOV",
    },
    
    "ATteam_RCL_SPG9_Naval_VDV_SOV": {
        "strength": 5,
        "CommandPoints": 30,
        "availability": [0, 10, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "ATteam_Fagot_SOV": {
        "CommandPoints": 25,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "ATGM_9K111M_Faktoriya": {
                        "new_weapon": "ATGM_9K111_Fagot",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
    },

    "Atteam_Fagot_DShV_SOV": {
        "CommandPoints": 25,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "ATGM_9K111M_Faktoriya": {
                        "new_weapon": "ATGM_9K111_Fagot",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
    },

    "Atteam_Fagot_VDV_SOV": {
        "CommandPoints": 25,
        "availability": [0, 9, 7, 5],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "ATGM_9K111M_Faktoriya": {
                        "new_weapon": "ATGM_9K111_Fagot",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
    },
    
    "Atteam_Fagot_Naval_VDV_SOV": {
        "CommandPoints": 25,
        "availability": [0, 9, 7, 5],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "ATGM_9K111M_Faktoriya": {
                        "new_weapon": "ATGM_9K111_Fagot",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
    },

    "Atteam_Konkurs_VDV_SOV": {
        "CommandPoints": 45,
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
        "UpgradeFromUnit": "ATteam_Faktoriya_VDV_SOV",
    },

    "ATteam_Konkurs_TTsko_SOV": {
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [6, 4, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "ATteam_Faktoriya_SOV",
    },
    
    "Atteam_Konkurs_Naval_SOV": {
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [6, 4, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "ATteam_KonkursM_TTsko_SOV": {
        "CommandPoints": 60,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [4, 3, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "ATGM_9M113M_KonkursM": {
                        "new_weapon": "ATGM_inf_9M113M_KonkursM",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
    },
    
    "UAZ_469_AGL_VDV_SOV": {
        "CommandPoints": 20,
        "availability": [0, 12, 9, 0],
    },

    "UAZ_469_AGL_SOV": {
        "CommandPoints": 20,
        "availability": [12, 9, 0, 0],
    },

    "UAZ_469_SPG9_VDV_SOV": {
        "CommandPoints": 25,
        "availability": [0, 12, 9, 0],
    },

    "LUAZ_967M_SPG9_SOV": {
        "CommandPoints": 25,
        "availability": [0, 12, 9, 0],
    },

    "LUAZ_967M_SPG9_VDV_SOV": {
        "CommandPoints": 25,
        "availability": [0, 12, 9, 0],
    },

    "LUAZ_967M_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    # removed in landjut patch?
    # "LUAZ_967M_VDV_SOV": {
    #     "CommandPoints": 15,
    #     "SpecialtiesList": {
    #         "add_specs": ["'refundable_unit'",],
    #     },
    # },

    "UAZ_469_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "UAZ_469_MP_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "UAZ_452_MP_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Ural_4320_trans_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "ZIL_131_Naval_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "GAZ_46_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "GAZ_66_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "GAZ_66B_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "KrAZ_255B_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    # SOV ARTILLERY
    "MTLB_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_ARTY"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 60,
        "GameName": {
            "display": "MT-LBu MASHINA",
            "token": "PUEZYZBZLF", # Don't remove or logistic tab version will get renamed as well
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_MTLB_CMD_SOV",
                "Unite",
                "Vehicule",
            ],
        },
        "Factory": "Factory/Art",
        "IdentifiedTextures": ["Texture_RTS_H_appui", "Texture_appui"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "leader_sov",
        "SpecialtiesList": {
            "overwrite_all": [
                '_amphibie',
            ],
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

    "Mortier_2B14_82mm_VDV_SOV": {
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 5, 4, 3],
    },
    
    "Mortier_M43_82mm_SOV": {
        "CommandPoints": 35,
    },

    "Mortier_2B9_Vasilek_nonPara_SOV": {
        "CommandPoints": 40,
        "orders": {
            "add_orders": ["EOrderType/ShootOnPositionSmoke", "EOrderType/ShootOnPositionWithoutCorrectionSmoke"],
        },
        "availability": [4, 3, 2, 0],
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "MountedWeapons": {
                        "insert": {
                            "Mortier_Vasilek_indirect_82mm_towed": {
                                "Ammunition": "$/GFX/Weapon/Ammo_Mortier_Vasilek_indirect_82mm_SMOKE_towed",
                                "DispersionRadiusOffColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOffThickness": -0.1,
                                "DispersionRadiusOnColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOnThickness": -0.1,
                                "EffectTag": "'FireEffect_Mortier_Vasilek_indirect_82mm_towed'",
                                "HandheldEquipmentKey": "'WeaponAlternative_3'",
                                "ShowDispersion": False,
                                "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                                "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                                "WeaponShootDataPropertyName": ['WeaponShootData_0_3'],
                            },
                        },
                    },
                },
            },
        },
    },

    "Mortier_2B9_Vasilek_SOV": {
        "CommandPoints": 40,
        "orders": {
            "add_orders": ["EOrderType/ShootOnPositionSmoke", "EOrderType/ShootOnPositionWithoutCorrectionSmoke"],
        },
        "availability": [0, 4, 3, 2],
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "MountedWeapons": {
                        "add": {
                            "Mortier_Vasilek_indirect_82mm_towed": {  # donor
                                "Ammunition": "$/GFX/Weapon/Ammo_Mortier_Vasilek_indirect_82mm_SMOKE_towed",
                                "DispersionRadiusOffColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOffThickness": -0.1,
                                "DispersionRadiusOnColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOnThickness": -0.1,
                                "EffectTag": "'FireEffect_Mortier_Vasilek_indirect_82mm_towed'",
                                "HandheldEquipmentKey": "'WeaponAlternative_3'",
                                "ShowDispersion": False,
                                "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                                "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                                "WeaponShootDataPropertyName": ['WeaponShootData_0_3'],
                            },
                        },
                    },
                },
            },
        },
    },
    
    "Mortier_2B9_Vasilek_Naval_SOV": {
        "CommandPoints": 40,
        "orders": {
            "add_orders": ["EOrderType/ShootOnPositionSmoke", "EOrderType/ShootOnPositionWithoutCorrectionSmoke"],
        },
        "availability": [4, 3, 2, 0],
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "MountedWeapons": {
                        "add": {
                            "Mortier_Vasilek_indirect_82mm_towed": {  # donor
                                "Ammunition": "$/GFX/Weapon/Ammo_Mortier_Vasilek_indirect_82mm_SMOKE_towed",
                                "DispersionRadiusOffColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOffThickness": -0.1,
                                "DispersionRadiusOnColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOnThickness": -0.1,
                                "EffectTag": "'FireEffect_Mortier_Vasilek_indirect_82mm_towed'",
                                "HandheldEquipmentKey": "'WeaponAlternative_3'",
                                "ShowDispersion": False,
                                "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                                "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                                "WeaponShootDataPropertyName": ['WeaponShootData_0_3'],
                            },
                        },
                    },
                },
            },
        },
    },

    "Mortier_2S12_120mm_SOV": {
        "CommandPoints": 45,
        "availability": [5, 4, 3, 0],
    },
    
    "Mortier_2S12_120mm_TTsko_SOV": {
        "CommandPoints": 45,
        "availability": [5, 4, 3, 0],
    },

    "Mortier_2S12_120mm_VDV_SOV": {
        "CommandPoints": 45,
        "availability": [0, 5, 4, 3],
    },
    
    "Mortier_2S12_120mm_Naval_VDV_SOV": {
        "CommandPoints": 45,
        "availability": [0, 5, 4, 3],
    },

    "MTLB_Vasilek_SOV": {
        "CommandPoints": 65,
        "orders": {
            "add_orders": ["EOrderType/ShootOnPositionSmoke", "EOrderType/ShootOnPositionWithoutCorrectionSmoke"],
        },
        "availability": [4, 3, 2, 0],
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "MountedWeapons": {
                        "insert": {
                            "Mortier_Vasilek_indirect_82mm": {  # donor
                                "Ammunition": "$/GFX/Weapon/Ammo_Mortier_Vasilek_indirect_82mm_SMOKE",
                                "DispersionRadiusOffColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOffThickness": -0.1,
                                "DispersionRadiusOnColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOnThickness": -0.1,
                                "EffectTag": "'FireEffect_Mortier_Vasilek_indirect_82mm'",
                                "HandheldEquipmentKey": "'WeaponAlternative_4'",
                                "ShowDispersion": False,
                                "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_4'",
                                "WeaponIgnoredPropertyName": "'WeaponIgnored_4'",
                                "WeaponShootDataPropertyName": ['WeaponShootData_0_4'],
                            },
                        },
                    },
                },
            },
        },
    },

    "Mortier_Nona_K_120mm_SOV": {
        "CommandPoints": 75,
        "availability": [0, 3, 2, 0],
    },

    "2S9_Nona_SOV": {
        "GameName": {
            "display": "2S9 NONA-S",
        },
        "CommandPoints": 85,
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            "Salves": {
                "Howz_Canon_2A51_Howitzer_120mm": 6,
            },
        },
    },
    
    "2S9_1_Sviristelka_SOV": {
        "CommandPoints": 85,
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            "Salves": {
                "Howz_Canon_2A51_Howitzer_120mm": 6,
            },
        },
    },

    "2S23_Nona_SVK_SOV": {
        "GameName": {
            "display": "2S23 NONA-SVK",
        },
        "CommandPoints": 95,
        "availability": [3, 2, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "Howz_Canon_2A60_Howitzer_120mm": 6,
                "MMG_PKT_7_62mm": 44,
            },
        },
    },

    "Mortier_240mm_M240_Cluster_SOV": {
        "CommandPoints": 200,
        "availability": [3, 2, 0, 0],
    },
    
    "Mortier_240mm_M240_SOV": {
        "CommandPoints": 200,
        "availability": [3, 2, 0, 0],
    },
    
    "2S4_Tyulpan_SOV": {
        "CommandPoints": 170,
        "availability": [3, 2, 0, 0],
    },

    "Howz_BS3_100mm_SOV": {
        "CommandPoints": 55,
        "availability": [6, 0, 0, 0],
    },

    "Howz_D30_122mm_SOV": {
        "CommandPoints": 85,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [5, 4, 3, 0],
        "UpgradeFromUnit": "Howz_BS3_100mm_SOV",
    },
    
    "Howz_D30_122mm_VDV_SOV": {
        "CommandPoints": 85,
        "availability": [0, 5, 4, 3],
    },
    
    "Howz_D20_152mm_SOV": {
        "CommandPoints": 95,
        "availability": [3, 2, 0, 0],
        "UpgradeFromUnit": "Howz_D30_122mm_VDV_SOV",
    },

    "Howz_2A36_Giatsint_B_SOV": {
        "GameName": {
            "display": "2A36 GIATSINT-B 152mm",
        },
        "CommandPoints": 110,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [3, 2, 0, 0],
        "UpgradeFromUnit": "Howz_D20_152mm_SOV",
    },
    
    "2S5_GiatsintS_SOV": {
        "CommandPoints": 220,
    },

    "Howz_MstaB_150mm_SOV": {
        "GameName": {
            "display": "2A65 MSTA-B 152mm",
        },
        "CommandPoints": 110,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [3, 2, 0, 0],
        "UpgradeFromUnit": "Howz_2A36_Giatsint_B_SOV",
    },

    "2S1_Gvozdika_SOV": {
        "CommandPoints": 110,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_56_AirAslt_Brig": {
                "cards": 1,
            },
            "SOV_6IndMSBrig": {
                "cards": 3,
            },
        },
        "availability": [3, 2, 0, 0],
    },
    
    "2S1_Gvozdika_Naval_SOV": {
        "CommandPoints": 110,
        "availability": [3, 2, 0, 0],
    },

    "2S3M_Akatsiya_SOV": {
        "CommandPoints": 180,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [3, 2, 0, 0],
    },

    "2S3M1_Akatsiya_SOV": {
        "CommandPoints": 220,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_56_AirAslt_Brig": {
                "cards": 1,
            },
            "SOV_6IndMSBrig": {
                "cards": 3,
            },
        },
        "availability": [2, 0, 1, 0],
    },
    
    "Howz_B4M_203mm_SOV": {
        "CommandPoints": 170,
        "availability": [3, 0, 0, 0],
    },
    
    "Howz_Br5M_280mm_SOV": {
        "CommandPoints": 200,
        "availability": [3, 0, 0, 0],
    },
    
    "2S7M_Malka_SOV": {
        "CommandPoints": 260,
        "availability": [2, 0, 1, 0],
    },
    
    "2S19_MstaS_SOV": {
        "CommandPoints": 230,
        "availability": [2, 0, 1, 0],
    },
    
    "A222_Bereg_SOV": {
        "CommandPoints": 260,
        "availability": [2, 0, 1, 0],
    },
    
    "BM14M_SOV": {
        "CommandPoints": 180,
    },

    "BM21V_GradV_SOV": {
        "CommandPoints": 95,
        "availability": [0, 3, 2, 0],
    },

    "BM21_Grad_SOV": {
        "CommandPoints": 195,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [3, 2, 0, 0],
    },
    
    "BM21_1_Grad_Naval_SOV": {
        "CommandPoints": "BM21_Grad_SOV",
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [3, 2, 0, 0],
    },
    
    "BM24M_SOV": {
        "CommandPoints": 240,
        "availability": [2, 0, 1, 0],
    },
    
    "BM27_Uragan_SOV": {
        "CommandPoints": 290,
        "availability": [0, 1, 0, 0],
    },
    
    "Prima_SOV": {
        "CommandPoints": 225,
        "availability": [2, 0, 1, 0],
    },

    "TOS1_Buratino_SOV": {
        "CommandPoints": 250,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 2, 0, 0],
        "strength": 10,
        "armor": {
            "front": (15, None),
        },
        # Need to edit the model to support adding smoke, on hold for now (temporarily increased armor in the meantime)
        # "WeaponDescriptor": {
        #     "equipmentchanges": {
        #         "insert": [(1, "SMOKE_Vehicle_Grenadex8")],
        #         "insert_edits": {
        #             1: {
        #                 "turret_edits": {
        #                     "Tag": "tourelle2",
        #                     "YulBoneOrdinal": 2,
        #                 },
        #                 "AmmoBoxIndex": 1,
        #                 "HandheldEquipmentKey": "'WeaponAlternative_2'",
        #                 "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
        #                 "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
        #                 "WeaponShootDataPropertyName": ["WeaponShootData_0_2", "WeaponShootData_1_2", "WeaponShootData_2_2", "WeaponShootData_3_2"],
        #             },
        #         },
        #     },
        #     "Salves": {
        #         "insert": [(1, 8)],
        #     },
        # },
    },

    "UR67_SOV": { # 2 Shot Mineclearer
        "CommandPoints": "BTR_50_MRF_DDR",
        "availability": "BTR_50_MRF_DDR",
        # "CommandPoints": 50,
        # "availability": [3, 2, 0, 0],
    },
    
    "BM30_Smerch_SOV": {
        "CommandPoints": 290,
        "availability": [0, 1, 0, 0],
    },

    # SOV TANK
    "T10M_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 90,
        "GameName": {
            "token": "PFCNKRFVF",
            "display": "REZ. T-10MK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T10M_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },

    "T55A_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 80,
        "GameName": {
            "token": "PFCNKJHHF",
            "display": "REZ. T-55AK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T55A_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 6, 0],
        "remove_zone_capture": None,
    },

    "T55AM_1_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 110,
        "GameName": {
            "token": "PFCNJZNOHF",
            "display": "T-55AM-1K",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T55AM_1_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },
    
    "T55AM_CMD_SOV": { # MOR. T-55AMK
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 110,
        "GameName": {
            "display": "MOR. T-55AMK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T55AM_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_resolute',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },

    "T62MD_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 115,
        "armor": {
            "top": (3, None),
        },
        "GameName": {
            "token": "LARNJZNOHF",
            "display": "T-62MDK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T62MD_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },

    "T62M_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 115,
        "armor": {
            "top": (3, None),
        },
        "GameName": {
            "token": "LARNJZNGAB",
            "display": "T-62MK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T62M_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },
    
    "T64A_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 130,
        "armor": {
            "top": (3, None),
        },
        "GameName": {
            "display": "T-64A Obr. 83",
            "token": "SOVTSITAK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T64A_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 3, 0],
        "remove_zone_capture": None,
    },

    "T64B_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 175,
        "armor": {
            "top": (3, None),
        },
        "GameName": {
            "display": "T-64B",
            "token": "SOVTSITBK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T64B_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 3, 0],
        "remove_zone_capture": None,
    },

    "T64BV_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 200,
        "armor": {
            "top": (4, None),
        },
        "GameName": {
            "display": "T-64BVK",
            "token": "SOVTSITBVK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T64BV_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_smoke_launcher',
                '_era',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 2, 0],
        "remove_zone_capture": None,
    },

    "T72_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 110,
        "armor": {
            "top": (2, None),
        },
        "GameName": {
            "display": "T-72K Obr. 73",
            "token": "OALRSXERYB",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T72_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 3, 0],
        "remove_zone_capture": None,
    },
    
    "T72M_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 160,
        "armor": {
            "top": (2, None),
        },
        "GameName": {
            "display": "T-72AK Obr. 79",
            "token": "SOVTSETASK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T72M_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 3, 0],
        "remove_zone_capture": None,
    },

    "T72M1_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 185,
        "armor": {
            "top": (3, None),
        },
        "GameName": {
            "display": "T-72AK Obr. 81",
            "token": "SOVTSETAEK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T72M1_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 3, 0],
        "remove_zone_capture": None,
    },

    "T72B_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 215,
        "armor": {
            "top": (4, None),
        },
        "GameName": {
            "display": "T-72BK",
            "token": "SOVTSETBK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T72B_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_smoke_launcher',
                '_era',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 2, 0],
        "remove_zone_capture": None,
    },

    "T80B_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 200,
        "armor": {
            "top": (3, None),
        },
        "GameName": {
            "display": "T-80BK",
            "token": "SOVTEBK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T80B_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 3, 0],
        "remove_zone_capture": None,
    },

    "T80BV_CMD_SOV": {
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 225,
        "armor": {
            "front": (18, None),
            "top": (4, None),
        },
        "GameName": {
            "display": "T-80BVK",
            "token": "YWAOJLFAFW",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T80BV_CMD_SOV",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_smoke_launcher',
                '_era',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 2, 0],
        "remove_zone_capture": None,
    },

    # "T80U_CMD_SOV": {
    #     "CommandPoints": 270,
    #     "GameName": {
    #         "display": "#LDRSOV T-80UK",
    #         "token": "SOVTEUK",
    #     },
    #     "TagSet": {
    #         "overwrite_all": [
    #             "AllUnits",
    #             "AllowedForMissileRoE",
    #             "Char",
    #             "GroundUnits",
    #             "UNITE_T80U_CMD_SOV",
    #             "Unite",
    #         ],
    #     },
    #     "WeaponDescriptor":{
    #         "Salves": {
    #             "remove": ["ATGM_9M119M_Refleks"],
    #         },
    #     },
    #     "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
    #     "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
    #     "UnitRole": "armor",
    #     "SpecialtiesList": {
    #         "overwrite_all": [
    #             'leader_sov',
    #             '_smoke_launcher',
    #             '_era',
    #         ],
    #     },
    #     "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
    #     "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
    #     "availability": [0, 0, 0, 2],
    #     "remove_zone_capture": None,
    # },


    "MTLB_transp_SOV": {
        "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "PTS_M_SOV": {
        "CommandPoints": 15,
        "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "GTMU_1D_SOV": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "GTMU_1D_AGS_SOV": {
        "CommandPoints": 15,
    },

    "BTR_D_SOV": {
        "CommandPoints": 20,
    },

    "BTR_D_Robot_SOV": {  # 10x Konkurs, 2x PKT
        "CommandPoints": 30,
    },

    "BTR_152K_SOV": {
        "CommandPoints": 20,
        "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "BTR_152A_SOV": {
        "CommandPoints": 25,
        "strength": 10,
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZPU4_14_5mm": 192,
            },
        },
    },

    "BTR_60_SOV": {
        "CommandPoints": 20,
        "strength": 10,
    },

    "BTR_60_Naval_SOV": {
        "CommandPoints": 20,
        "strength": 10,
    },

    "BTR_70_SOV": {
        "CommandPoints": 25,
        "strength": 10,
    },

    "BTR_70D_SOV": {
        "CommandPoints": 25,
        "strength": 10,
    },

    "BTR_70_S5_SOV": {
        "CommandPoints": 35,
        "strength": 10,
    },

    "BTR_70_S8_SOV": {
        "CommandPoints": 40,
        "strength": 10,
    },

    "BTR_70_Rys_SOV": {
        "CommandPoints": 30,
        "strength": 10,
    },

    "BTR_70_AGS_SOV": {
        "CommandPoints": 30,
        "strength": 10,
    },

    "BTR_70_MP_SOV": {
        "CommandPoints": 25,
        "strength": 10,
    },

    "BTR_80_SOV": {
        "CommandPoints": 25,
        "strength": 10,
    },
    
    "BTR_80_Naval_SOV": {
        "CommandPoints": 25,
        "strength": 10,
    },

    "BMP_1_SP2_SOV": { # (Malyutka, no smoke)
        "CommandPoints": 25,
    },

    "BMP_1P_SOV": { # (Faktoriya, smoke)
        "CommandPoints": 40,
        "GameName": {
            "display": "BMP-1P [FAKTORIYA]",
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya_IFV": 6,
            }
        },
    },
    
    "BMP_1PG_SOV": { # (Faktoriya, AGS-17, no smoke)
        "CommandPoints": 40,
    },
    
    "BMP_1P_Konkurs_SOV": { # (Konkurs, Faktoriya, smoke)
        "CommandPoints": 50,
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9M113_Konkurs_BMP2": 6,
            },
        },
    },
    
    "BMD_1_SOV": {
        "CommandPoints": 20,
    },
    
    "BMD_1P_SOV": {
        "CommandPoints": 30,
    },

    "BMD_2_SOV": {
        "CommandPoints": 40,
    },
    
    "BMP_2_MVD_SOV": {
        "CommandPoints": 40,
    },

    "BMP_2_SOV": {
        "CommandPoints": 55,
    },

    "BMP_2D_SOV": {
        "CommandPoints": 55,
    },

    "BMP_2AG_SOV": {
        "CommandPoints": 60,
    },

    "BMP_3_SOV": {
        "CommandPoints": 85,
    },

    "BMD_3_SOV": {
        "CommandPoints": 80,
        "TagSet": {
            "add_tags": ['"Vehicule_Transport_Arme"'],
        },
        "SpecialtiesList": {
            "overwrite_all": [
                '_transport1',
                '_ifv',
                '_amphibie',
                '_smoke_launcher',
            ],
        },
        "capacities": {
            "add_capacities": ["IFV"],
        },
        "IdentifiedTextures": ["Texture_RTS_H_ifv", "Texture_ifv"],
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "UnitRole": "ifv",
        "UpgradeFromUnit": "BMD_2_SOV",
    },

     "LUAZ_967M_Fagot_SOV": {
        "CommandPoints": 35,
        "GameName": {
            "display": "LuAZ-967M FAKTORIYA",
            "token": "KYODTOGRYC",
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": 4,
            },
        },
        "UpgradeFromUnit": None,
    },
    
    "LUAZ_967M_Fagot_VDV_SOV": {
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": "LUAZ_967M_Fagot_SOV",
            },
        },
         "GameName": {
            "display": "DESANT. LuAZ FAKTORIYA",
            "token": "SXGTONCUAP",
        },
        "UpgradeFromUnit": "LUAZ_967M_Fagot_SOV",
    },
    
    "UAZ_469_Konkurs_VDV_SOV": {
        "CommandPoints": 40,
        "availability": [0, 8, 6, 0],
        "UpgradeFromUnit": "LUAZ_967M_Fagot_VDV_SOV",
    },

    "BRDM_2_Malyu_P_SOV": {
        "strength": 8,
        "CommandPoints": 40,
        "stealth": 1.5,
        "availability": [10, 7, 0, 0],
        "UpgradeFromUnit": "UAZ_469_Konkurs_VDV_SOV",
    },

    "BRDM_2_Falanga_P_SOV": {
        "strength": 8,
        "CommandPoints": 50,
        "stealth": 1.5,
        "availability": [8, 6, 0, 0],
        "UpgradeFromUnit": "BRDM_2_Malyu_P_SOV",
    },
    
    "BRDM_2_Konkurs_SOV": {
        "strength": 8,
        "CommandPoints": 50,
        "stealth": 1.5,
        "availability": [8, 6, 0, 0],
        "UpgradeFromUnit": "BRDM_2_Falanga_P_SOV",
    },
    
    "BRDM_2_Konkurs_Naval_SOV": {
        "strength": 8,
        "CommandPoints": 50,
        "stealth": 1.5,
        "availability": [8, 6, 0, 0],
    },

    "BRDM_2_Konkurs_M_SOV": {
        "strength": 8,
        "CommandPoints": 65,
        "stealth": 1.5,
        "availability": [8, 6, 0, 0],
        "UpgradeFromUnit": "BRDM_2_Konkurs_SOV",
    },

    "MTLB_Shturm_SOV": {
        "CommandPoints": 60,
        "availability": [6, 4, 0, 0],
        "UpgradeFromUnit": "BRDM_2_Konkurs_M_SOV",
    },
    
    "MTLB_Shturm_Ataka_SOV": {
        "CommandPoints": 160,
        "availability": [0, 4, 3, 0],
        "UpgradeFromUnit": "MTLB_Shturm_SOV",
    },
    
    "AT_D44_85mm_VDV_SOV": {
        "CommandPoints": 35,
        "availability": [0, 9, 7, 5],
    },

    "AT_KSM65_100mm_SOV": {
        "CommandPoints": 40,
        "availability": [9, 7, 5, 0],
    },

    "AT_T12_Rapira_SOV": {
        "GameName": {
            "display": "MT-12 RAPIRA 100mm",
        },
        "CommandPoints": 55,
        "availability": [6, 4, 0, 0],
    },
    
    "AT_T12_Rapira_Naval_SOV": {
        "CommandPoints": 55,
        "availability": [6, 4, 0, 0],
    },
    
    "AT_T12R_Ruta_SOV": {
        "CommandPoints": 65,
        "availability": [6, 4, 0, 0],
        "UpgradeFromUnit": "AT_T12_Rapira_SOV",
    },
    
    "AT_2A45_SprutB_SOV": {
        "GameName": {
            # "display": "2A45M SPRUT-B",
            "display": "2A45 SPRUT-A",
        },
        "CommandPoints": 55,
        "availability": [7, 5, 0, 0],
    },

    "TO_55_SOV": {
        "CommandPoints": 60,
        "availability": [8, 6, 0, 0],
    },

    "ISU_152K_SOV": {
        "CommandPoints": 180,
        "availability": [3, 2, 0, 0],
    },

    "IS2M_SOV": {
        "CommandPoints": 55,
        "availability": [12, 0, 0, 0],
    },

    "T10M_SOV": {
        "CommandPoints": 80,
        "availability": [10, 0, 0, 0],
        "GameName": {
            "display": "REZ. T-10M",
        },
    },

    "T54B_SOV": {
        "CommandPoints": 70,
        "availability": [10, 0, 0, 0],
    },

    "T55A_SOV": {
        "CommandPoints": 70,
        "availability": [10, 0, 0, 0],
    },
    
    "T55A_obr81_SOV": {
        "CommandPoints": 80,
        "availability": [8, 6, 0, 0],
        "GameName": {
            "display": "T-55A Obr. 81",
        },
        "SpecialtiesList": {
            "overwrite_all": [
                '_smoke_launcher',
            ],
        },
        "capacities": {
            "remove_capacities": ["reserviste"],
        },
    },  

    "T55AM_1_SOV": {
        "CommandPoints": 130,
        "availability": [0, 6, 4, 0],
    },
    
    "T55AM_SOV": { # MOR. T-55AM
        "CommandPoints": 130,
        "availability": [0, 6, 4, 0],
    },
    
    "T55AMD_SOV": { # MOR. T-55AMD
        "CommandPoints": 140,
        "availability": [0, 6, 4, 0],
    },

    "T55AMV_SOV": { # MOR. T-55AMV
        "CommandPoints": 140,
        "availability": [0, 0, 4, 3],
        "armor": {
            "front": (12, None),
        },
        "max_speed": 50,
    },

    "T62M1_SOV": {
        "CommandPoints": 115,
        "armor": {
            "top": (3, None),
        },
        "availability": [8, 6, 0, 0],
    },

    "T62MD1_SOV": { # T62M1 with +1 side and rear armor
        "CommandPoints": 115,
        "armor": {
            "top": (3, None),
        },
        "availability": [8, 6, 0, 0],
    },
    
    "T62M_SOV": {
        "CommandPoints": 140,
        "armor": {
            "top": (3, None),
        },
        "availability": [0, 6, 4, 0],
    },

    "T62MD_SOV": { # T62M with +1 side and rear armor
        "CommandPoints": 140,
        "armor": {
            "top": (3, None),
        },
        "availability": [0, 6, 4, 0],
    },
    
    "T62MV_SOV": {
        "CommandPoints": 140,
        "armor": {
            "front": (12, None),
            "top": (3, None),
        },
        "max_speed": 50,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 0, 0, 3],
    },
    
    "T62M_APS_SOV": {
        "CommandPoints": 170,
        "armor": {
            "front": (12, None),
            "top": (3, None),
        },
        "availability": [0, 0, 0, 3],
    },

    "T64R_SOV": {
        "CommandPoints": 95,
        "armor": {
            "top": (2, None),
        },
        "availability": [8, 6, 0, 0],
    },
    
    "T64A_Obr81_SOV": {
        "CommandPoints": 110,
        "armor": {
            "top": (2, None),
        },
        "availability": [6, 4, 0, 0],
        "UpgradeFromUnit": "T64R_SOV",
    },

    "T64A_SOV": { # T-64A Obr. 83
        "CommandPoints": 125,
        "armor": {
            "top": (3, None), # Minor top armor and internal layout improvements came with Obr. 83
        },
        "availability": [6, 4, 0, 0],
        "UpgradeFromUnit": "T64A_Obr81_SOV",
    },
    
    "T64A_Obr84_SOV": {
        "CommandPoints": 140,
        "armor": {
            "top": (3, None),
        },
        "availability": [6, 4, 0, 0],
        "UpgradeFromUnit": "T64A_SOV",
    },

    "T64AV_SOV": {
        "CommandPoints": 160,
        "armor": {
            "top": (4, None),
        },
        "availability": [6, 4, 0, 0],
        "UpgradeFromUnit": "T64A_SOV",
    },
    
    "T64AM_SOV": {  # Not a real tank, removed from vanilla
        "CommandPoints": 140,
        "armor": {
            "top": (3, None),
        },
        "availability": [0, 6, 4, 0],
        # "UpgradeFromUnit": "T64AV_SOV",
    },

    "T64B1_SOV": {
        "CommandPoints": 165,
        "armor": {
            "top": (3, None),
        },
        "availability": [6, 4, 0, 0],
    },

    "T64BV1_SOV": {
        "CommandPoints": 190,
        "armor": {
            "top": (4, None),
        },
        "availability": [0, 6, 4, 0],
    },

    "T64B_SOV": {
        "CommandPoints": 175,
        "armor": {
            "top": (3, None),
        },
        "availability": [6, 4, 0, 0],
    },

    "T64BV_SOV": {
        "CommandPoints": 215,
        "armor": {
            "top": (4, None),
        },
        "availability": [0, 4, 3, 0],
    },

    "T72_SOV": {
        "CommandPoints": 110,
        "armor": {
            "top": (2, None),
        },
        "availability": [8, 6, 0, 0],
        "GameName": {
            "display": "T-72 Obr. 73",
        },
    },

    "T72_obr77_SOV": {
        "CommandPoints": 125,
        "armor": {
            "top": (2, None),
        },
        "availability": [8, 6, 0, 0],
    },

    "T72M_SOV": {
        "CommandPoints": 150,
        "armor": {
            "top": (2, None),
        },
        "availability": [6, 4, 0, 0],
    },

    "T72M1_SOV": {
        "CommandPoints": 175,
        "armor": {
            "top": (3, None),
        },
        "availability": [0, 6, 4, 0],
    },

    "T72AV_SOV": {
        "CommandPoints": 195,
        "armor": {
            "top": (4, None),
        },
        "availability": [0, 6, 4, 0],
        "UpgradeFromUnit":  "T72M1_SOV",
    },

    "T72B1_early_SOV": {
        "CommandPoints": 190,
        "armor": {
            "top": (3, None),
        },
        "availability": [6, 4, 0, 0],
    },

    "T72B1_SOV": {
        "CommandPoints": 215,
        "armor": {
            "top": (4, None),
        },
        "availability": [0, 6, 4, 0],
    },

    "T72B_SOV": {
        "CommandPoints": 230,
        "armor": {
            "top": (4, None),
        },
        "availability": [0, 0, 3, 2],
    },

    "T80B_SOV": {
        "CommandPoints": 200,
        "armor": {
            "top": (3, None),
        },
        "availability": [6, 4, 0, 0],
    },

    "T80BV_SOV": {
        "armor": {
            "front": (18, None),
            "top": (4, None),
        },
        "CommandPoints": 235,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_79_Gds_Tank": {
                "cards": 3,
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "ATGM_9M112_Kobra": {
                        "new_weapon": "ATGM_9M112M2_Kobra",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
        "availability": [0, 4, 3, 0],
    },

    "T80BV_Beast_SOV": {
        "armor": {
            "front": (18, None),
            "top": (4, None),
        },
        "CommandPoints": 255,
        "availability": [0, 0, 4, 3],
    },

    "T80U_SOV": {
        "CommandPoints": 270,
        "armor": {
            "top": (4, None),
        },
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 4, 3, 0],
    },

    "T80UD_SOV": {
        "CommandPoints": 315,
        "armor": {
            "top": (4, None),
        },
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [0, 0, 3, 2],
    },

    "T80U_Obr89_SOV": {
        "CommandPoints": 325,
        "armor": {
            "top": (4, None),
        },
        "availability": [0, 0, 3, 2],
    },

    # SOV RECON
    "UAZ_469_Reco_SOV": {
        "CommandPoints": 25,
    },
    
    "BTR_40_SOV": {
        "CommandPoints": 20,
    },

    "LUAZ_967M_AGL_VDV_SOV": {
        "CommandPoints": 30,
    },

    "LUAZ_967M_AGL_SOV": {
        "CommandPoints": 30,
    },

    "BTR_D_reco_SOV": {
        "CommandPoints": 25,
    },
    
    "BMP_1P_reco_SOV": {
        "CommandPoints": 50,
    },

    "BMP_2_reco_SOV": {
        "CommandPoints": 80,
    },

    "BMP_2D_reco_SOV": {
        "CommandPoints": 80,
    },

    "BTR_60_reco_SOV": {
        "CommandPoints": 30,
        "strength": 10,
    },

    "BTR_80_reco_SOV": {
        "CommandPoints": 35,
        "strength": 10,
    },
    
    "PT76B_Naval_SOV": {
        "CommandPoints": 30,
        "availability": [8, 6, 0, 0],
    },

    "BRM_1_SOV": {
        "CommandPoints": 55,
        "availability": [6, 4, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_6IndMSBrig": {
                "cards": 3,
            },
        },
        "UpgradeFromUnit": "BMD_1_Reostat_SOV",
    },

    "BMD_1_Reostat_SOV": {
        "CommandPoints": 30,
        "availability": [0, 8, 0, 0],
        "UpgradeFromUnit": "MTLB_Taran_SIGINT_SOV",
    },
    
    "BMD_1_Reostat_Naval_SOV": {
        "CommandPoints": 30,
        "availability": [0, 8, 0, 0],
    },

    "ZSU_23_Shilka_reco_SOV": {
        "CommandPoints": 70,
        "availability": [0, 4, 3, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_4_canons_AZP_23_Amur_23mm_PSNR": 53,
            },
        },
    },

    "BMD_3_reco_SOV": {
        "CommandPoints": 105,
        "availability": [0, 4, 3, 0],
        "TagSet": {
            "add_tags": ['"Vehicule_Transport_Arme"'],
        },
        "SpecialtiesList": {
            "overwrite_all": [
                '_transport1',
                '_ifv',
                '_amphibie',
                '_smoke_launcher',
            ],
        },
        "capacities": {
            "add_capacities": ["IFV"],
        },
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]
        },
        "UpgradeFromUnit": "Scout_VDV_SOV",
    },
    
    "T55AMD_reco_SOV": {
        "CommandPoints": 160,
        "max_speed": 50,
        "availability": [0, 4, 3, 0],
    },

    "T64B1_reco_SOV": {
        "CommandPoints": 190,
        "armor": {
            "top": (3, None),
        },
        "availability": [3, 2, 0, 0],
    },

    "BRDM_2_SOV": {
        "strength": 8,
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_6IndMSBrig": {
                "cards": 1,
            },
        },
        "availability": [8, 6, 0, 0],
    },
    
    "BRDM_2_Naval_SOV": {
        "strength": 8,
        "CommandPoints": 35,
        "availability": [8, 6, 0, 0],
        "UpgradeFromUnit": "BRDM_2_SOV",
    },

    "BTR_40A_SOV": {
        "CommandPoints": 35,
        "availability": [8, 6, 0, 0],
    },

    "MTLB_BMAN_SOV": { # Honestly, 60 points is just a wild guess, this thing is so unique
        "CommandPoints": 60,
        "availability": [6, 4, 0, 0],
    },

    "GAZ_66_SIGINT_SOV": {
        "CommandPoints": 20,
        "availability": [6, 0, 0, 0],
    },
    
    "MTLB_Taran_SIGINT_SOV": {
        "CommandPoints": 20,
        "availability": [6, 0, 0, 0],
    },

    "SNAR_10_SOV": { # SNAR-10 (Counter Battery Radar)
        "CommandPoints": 30,
        "availability": [6, 0, 0, 0],
    },
    
    "Scout_SOV": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [8, 6, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },

    "Scout_TTsko_SOV": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [8, 6, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },
    
    "Scout_Naval_SOV": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [0, 8, 6, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },
    
    "Scout_Naval_VDV_SOV": {
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
            "add_specs": ["'infantry_equip_medium'"],
        },
        "strength": 8,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "Sniper_VSS_Vintorez_double": False,
                },
                "quantity": {
                    "PM_AS_Val": 6,
                    "Sniper_VSS_Vintorez_double": 2,
                },
                "replace": {
                    "Sniper_VSS_Vintorez": {
                        "new_weapon": "Sniper_VSS_Vintorez_double",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },

    "Scout_VDV_SOV": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [0, 8, 6, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },

    "Engineers_Scout_SOV": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            # "display": "RAZVEDKA SAPERY",
            "display": "RAZV. SAPERY",
        },
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 4, 3, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "UpgradeFromUnit": "HvyScout_RPG7VL_SOV",
    },

    "Engineers_Scout_TTsko_SOV": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            # "display": "RAZVEDKA SAPERY",
            "display": "RAZV. SAPERY",
        },
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 4, 3, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "UpgradeFromUnit": "HvyScout_TTsko_SOV",
    },

    "HvyScout_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 30,
        "availability": [7, 5, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "strength": 8,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "SAW_RPK_74_5_56mm": {
                        "new_weapon": "MMG_PKM_7_62mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
                "quantity": {
                    "FM_AK_74": 7
                },
            },
            "Salves": {
                "MMG_PKM_7_62mm": 36,
            },
        },
        "UpgradeFromUnit": "Scout_SOV",
    },

    "HvyScout_TTsko_SOV": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "availability": [7, 5, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "SAW_RPK_74_5_56mm": {
                        "new_weapon": "MMG_PKM_7_62mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "MMG_PKM_7_62mm": 36,
            },
        },
        "UpgradeFromUnit": "Scout_TTsko_SOV",
    },
    
    "HvyScout_Reserve_SOV": {
        "armor": "Infantry_armor_reference",
        "CommandPoints": 30,
        "availability": [7, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "HvyScout_DShV_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 5, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AKS_74": 5,
                    "SAW_RPK_74_5_56mm": 2,
                },
            },
        },
        "UpgradeFromUnit": None,
    },

    "Scout_SIGINT_SOV": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },

    "Scout_LRRP_SOV": {  # Spetsnaz GRU (GSR)
        "CommandPoints": 65,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "UpgradeFromUnit": "Engineers_Scout_Jouk_SOV",
    },

    "Engineers_Scout_Jouk_SOV": {  # INZH. RAZVEDKA (GSR)
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
        "availability": [0, 4, 3, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "UpgradeFromUnit": "KGB_BorderGuard_LRRP_SOV",
    },

    "Scout_Spetsnaz_SOV": { # Spetzrazvedka (GSR)
        "CommandPoints": 65,
        "armor": "Infantry_armor_reference",
        "availability": [0, 4, 3, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Scout_Spetsnaz_Naval_SOV": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "KGB_BorderGuard_LRRP_SOV": { # Spetzrazvedka (GSR)
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [0, 4, 3, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Sniper_Spetsnaz_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "strength": 3,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "Sniper_VSS_Vintorez_double": False,
                },
                "quantity": {
                    "Sniper_VSS_Vintorez_double": 2,
                },
                "replace": {
                    "Sniper_VSS_Vintorez": {
                        "new_weapon": "Sniper_VSS_Vintorez_double",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "insert": [(2, "RocketInf_RPG26_72_5mm")],
                "insert_edits": {
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "NbWeapons": 1,
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
            },
            "Salves": {
                "Sniper_VSS_Vintorez_double": 20,
                "insert": [(2, 4)],
            },
        },
    },

    "Scout_Spetsnaz_VDV_SOV": { # Desant Spetzrazvedka
        "CommandPoints": 65,
        "armor": "Infantry_armor_reference",
        "availability": [0, 4, 3, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Scout_SpetsnazGRU_Stinger_SOV": { # SpetzGRU with Stinger
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "MANPAD_FIM92_A": 4,
            },
        },
    },

    "Alfa_Group_SOV": {
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_M72A3_LAW_66mm": 7,
            },
        },
    },

    "Alouette_III_SOV": {
        "availability": [0, 6, 0, 0],
    },
    
    "Mi_2_reco_SOV": {
        "availability": [0, 6, 0, 0],
    },
    
    "Mi_8R_SOV": { # Mi-8MTA, Exceptional Optics, 8 HP
        "CommandPoints": 50,
        "availability": [0, 4, 0, 0],
        "UpgradeFromUnit": "Mi_2_reco_SOV",
    },

    "Mi_8PPA_SOV": { # VG optics, 8 HP, 30% ECM, Jammer
        "CommandPoints": 75,
        "availability": [0, 3, 0, 0],
        "UpgradeFromUnit": "Mi_8R_SOV",
    },
    
    "Mi_8TARK_reco_SOV": { # x64 S-5M 57mm rocket, VG Optics
        "CommandPoints": 80,
        "availability": [0, 6, 0, 0],
        "UpgradeFromUnit": "Mi_8PPA_SOV",
    },

    "Mi_8MTPI_SOV": { # VG optics, 8 HP, 40% ECM, Jammer, Sigint
        "CommandPoints": 105,
        "availability": [0, 3, 0, 0],
        "UpgradeFromUnit": "Mi_8TARK_reco_SOV",
    },
    
    "Mi_14PL_recon_SOV": {
        "CommandPoints": 50,
        "availability": [0, 4, 0, 0],
        "UpgradeFromUnit": "Mi_2_reco_SOV",
    },

    "Mi_24K_reco_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 150,
        "strength": "Mi_24P_SOV",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 2, 0],
    },

    "Pchela_1T_SOV": { # Recon Drone (Slow)
        "CommandPoints": 45,
    },
    
    "Pero_UAV_SOV": { # Recon Drone (Medium)
        "CommandPoints": 50,
        "availability": [0, 4, 0, 0],
        "UpgradeFromUnit": "Pchela_1T_SOV",
    },

    # SOV AA
    "BTR_ZD_Skrezhet_SOV": {
        "CommandPoints": 30,
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm": 29,
            },
        },
    },

    "GTMU_1D_ZU_SOV": {
        "CommandPoints": 30,
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm": 29,
            },
        },
    },

    "LuAZ_967M_AA_VDV_SOV": {
        "CommandPoints": 35,
        "Stealth": 2.0,
    },
    
    "DCA_ZU_23_2_nonPara_SOV": {
        "CommandPoints": 20,
        "Factory": "Factory/Logistic",
        "availability": [10, 7, 0, 0],
        "max_speed": 6,
        
        "UpgradeFromUnit": "FOB_SOV",
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm_TOWED": 31,
            },
        },
    },
    
    "DCA_ZU_23_2_Naval_SOV": {
        "CommandPoints": 20,
        "Factory": "Factory/Logistic",
        "availability": [10, 7, 0, 0],
        "max_speed": 6,
        
        "UpgradeFromUnit": "FOB_SOV",
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm_TOWED": 31,
            },
        },
    },

    "DCA_ZU_23_2_TTsko_SOV": {
        "CommandPoints": 20,
        "Factory": "Factory/Logistic",
        "Divisions": {
            "add": ["SOV_119IndTkBrig"],
            "is_transported": True,
            "needs_transport": True,
            "default": {
                "Transports": ["MTLB_transp_SOV"],
                "cards": 1,
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 6,
        
        "UpgradeFromUnit": "FOB_SOV",
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm_TOWED": 31,
            },
        },
    },

    "DCA_ZU_23_2_SOV": {  # Airborne (non-airborne is nonPara_SOV)
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "Factory": "Factory/Logistic",
        "availability": [0, 10, 7, 0],
        "max_speed": 6,
        
        "UpgradeFromUnit": "FOB_SOV",
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm_TOWED": 31,
            },
        },
    },

    "DCA_AZP_S60_SOV": {
        "CommandPoints": 70,
        "TagSet": {
            "add_tags": ['"AA_radar"'],
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 6,
        
        "WeaponDescriptor": {
            "Salves": {
                "DCA_1_canon_S60_57mm_radar": 1,
            },
            "equipmentchanges": {
                "replace": {
                    "DCA_1_canon_S60_57mm": {
                        "new_weapon": "DCA_1_canon_S60_57mm_radar",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    "DCA_KS30_130mm_SOV": {
        "CommandPoints": 85,
        "TagSet": {
            "add_tags": ['"AA_radar"'],
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 6,
        
        "WeaponDescriptor": {
            "Salves": {
                "DCA_1_canon_KS30_130mm_radar": 1,
                "Canon_HE_KS30_130mm": 1,
            },
            "equipmentchanges": {
                "replace": {
                    "DCA_1_canon_KS30_130mm": {
                        "new_weapon": "DCA_1_canon_KS30_130mm_radar",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    "MANPAD_Igla_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_119IndTkBrig": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle": {
                "cards": 4,
            },
            "SOV_6IndMSBrig": {
                "cards": 3,
            },
            "SOV_79_Gds_Tank": {
                "cards": 3,
            },
        },
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_AK_74": {
                        "new_weapon": "FM_AK_74_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
        "availability": [7, 5, 0, 0],
    },

    "MANPAD_Igla_TTsko_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [7, 5, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_AK_74": {
                        "new_weapon": "FM_AK_74_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },

    "MANPAD_Igla_Gvardeitsy_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [7, 5, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_AK_74": {
                        "new_weapon": "FM_AK_74_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },

    "MANPAD_Igla_VDV_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 7, 5, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_AKS_74": {
                        "new_weapon": "FM_AKS_74_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },
    
    "MANPAD_Igla_Naval_VDV_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 7, 5, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_AKS_74": {
                        "new_weapon": "FM_AKS_74_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },

    "MANPAD_Igla_DShV_SOV": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 7, 5, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_AKS_74": {
                        "new_weapon": "FM_AKS_74_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },

    "MANPAD_Strela_3_SOV": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_AK_74": {
                        "new_weapon": "FM_AK_74_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
        "availability": [12, 0, 0, 0],
    },

    "GAZ_66B_ZU_SOV": {
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 1,
            },
            "SOV_76_VDV": {
                "cards": 2,
            },
        },
        "availability": [0, 10, 7, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm": 39,
            },
        },
    },

    "Ural_4320_ZU_SOV": {
        "CommandPoints": 40,
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm": 39,
            },
        },
    },

    "Ural_4320_ZPU_SOV": {
        "CommandPoints": 30,
        "availability": [12, 9, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_4_canon_ZPU4_14_5mm": 80,
            },
        },
    },

    "BRDM_Strela_1_SOV": {
        "CommandPoints": 50,
        "availability": [6, 4, 0, 0],
        "strength": 8,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "WeaponDescriptor": {
            "Salves": {
                "SAM_Strela1_salvolength4": 2,
            },
        },
    },
    
    "ZSU_23_Shilka_Afghan_SOV": {
        "CommandPoints": 40,
        "availability": [8, 6, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_4_canons_AZP_23_Amur_23mm_Afghan": 53,
            },
        },
    },

    "ZSU_23_Shilka_early_SOV": {
        "CommandPoints": 85,
        "availability": [6, 4, 0, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 7800,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "DCA_4_canons_APZ23_23mm": 67,
            },
        },
    },

   "ZSU_23_Shilka_SOV": {
        "CommandPoints": 85,
        "availability": [6, 4, 0, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 7800,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "DCA_4_canons_AZP_23_Amur_23mm_late": 67,
            },
        },
    },
   
   "ZSU_23_Shilka_Naval_SOV": {
        "CommandPoints": 85,
        "availability": [6, 4, 0, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 7800,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "DCA_4_canons_AZP_23_Amur_23mm_late": 67,
            },
        },
    },

    "Tunguska_2K22_SOV": {
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "CommandPoints": 135,
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "SOV_6IndMSBrig": {
                "cards": 4,
            },
        },
        "availability": [0, 3, 2, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canons_2A38M_30mm": 21,
            },
        },
    },

    "Tor_SOV": {
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "CommandPoints": 150,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [0, 3, 2, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    "Osa_9K33M3_SOV": {
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "CommandPoints": 130,
        "availability": [0, 3, 2, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    "MTLB_Strela10_SOV": {
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 7800,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "CommandPoints": 65,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [6, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },
    
    "MTLB_Strela10_Naval_SOV": {
        "CommandPoints": 65,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 7800,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [6, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "MTLB_Strela10M3_SOV": {
        "CommandPoints": 100,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 7800,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 4, 3, 0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "2K12_KUB_SOV": { # 2K12 Kub
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "CommandPoints": 115,
        "availability": [4, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "UpgradeFromUnit": None,
    },
    
    "Buk_9K37M_SOV": { # 9K37M Buk
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 2, 0, 1],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    "2K11_KRUG_SOV": {  # 2K11 Krug
        "CommandPoints": 130,
        "availability": [3, 2, 0, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "UpgradeFromUnit": "2K12_KUB_SOV",
    },
    
    "DCA_S125_quad_Neva_SOV": {
        "CommandPoints": 90,
        "availability": [3, 2, 0, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "UpgradeFromUnit": "2K12_KUB_SOV",
    },

    # SOV HELI
    "Mi_2_trans_SOV": {
        "CommandPoints": 35,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Mi_8TV_non_arme_SOV": {
        "CommandPoints": 50,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Mi_8TV_SOV": {  # 32 S-5M x2
        "CommandPoints": 50,
    },
    
    "Mi_8MTV_SOV": { # 32 S-5m x2, 20% ECM
        "CommandPoints": 60,
    },

    "Mi_8TV_Gunship_SOV": {  # 4x Molniya, 2x S-24 (Vanilla) 40x S-8KOM, 2x S-24
        "CommandPoints": 110,
        "availability": [0, 4, 3, 0],
        "WeaponDescriptor": {
            "Salves": {
                "remove": ["RocketAir_B8_80mm_x20"],
                "AA_R60M_Vympel": 4,
            },
            "equipmentchanges": {
                "replace": {
                    "AA_R60M_Vympel": {
                        "new_weapon": "AA_R60M_Vympel_helo",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "turrets": {
                1: {
                    "MountedWeapons": {
                        "AA_R60M_Vympel": {
                            "HandheldEquipmentKey": "'WeaponAlternative_1'",
                            "AmmoBoxIndex": 0,
                            "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_1'",
                            "WeaponIgnoredPropertyName": "'WeaponIgnored_1'",
                            "WeaponShootDataPropertyName": ['WeaponShootData_0_1'],
                        },
                    },
                    "Tag": "'tourelle1'",
                    "YulBoneOrdinal": 1,
                },
                2: {
                    "MountedWeapons": {
                        "RocketAir_S24_240mm_salvolength2": {
                            "AmmoBoxIndex": 1,
                        },
                    },
                },
                "remove": [0],
            },
        },
    },

    "Mi_8TV_s57_16_SOV": {
        "GameName": {
            "display": "Mi-8MT [RKT]",
        },
        "CommandPoints": 70,
        "availability": [0, 6, 4, 0],
    },

    "Mi_8TV_s57_32_SOV": {
        "CommandPoints": 85,
        "availability": [0, 6, 4, 0],
        "GameName": {
            "display": "Mi-8MT [RKT2]",
        },
    },
    
    "Mi_8TV_PodGatling_PodAGL_SOV": {
        "CommandPoints": 85,
        "availability": [0, 6, 4, 0],
    },

    "Mi_8TV_s80_SOV": {
        "GameName": {
            "display": "Mi-8MT [RKT3]",
        },
        "CommandPoints": 85,
        "availability": [0, 0, 4, 3],
    },

    "Mi_8TB_SOV": {
        "CommandPoints": 95,
        "availability": [0, 4, 3, 0],
    },
    
    "Mi_24D_Desant_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 85,
        "strength": "Mi_24P_SOV",
    },
    
    "Mi_24A_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 100,
        "strength": "Mi_24P_SOV",
    },

    "Mi_24V_AA_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 160,
        "strength": "Mi_24P_SOV",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 2, 0],
    },

    "Mi_24V_RKT_SOV": {  # 4x Kokon, 20x S-13
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 160,
        "strength": "Mi_24P_SOV",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle": {
                "cards": 1,
            },
        },
        "availability": [0, 4, 3, 0],
    },

    "Mi_24V_RKT2_SOV": {  # 4x Kokon, 80x S-8KOM
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 160,
        "strength": "Mi_24P_SOV",
        "availability": [0, 4, 3, 0],
    },

    "Mi_24V_AT_SOV": {  # 8x Kokon, 40x S-80
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 160,
        "strength": "Mi_24P_SOV",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 1,
            },
            "SOV_79_Gds_Tank": {
                "cards": 1,
            },
        },
        "availability": [0, 4, 3, 0],
    },

    "Mi_24P_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "GameName": {
            "display": "Mi-24P [AT]",
        },
        "CommandPoints": 185,
        "strength": 10,
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_30mm_Bitube_Gsh30k": 5,
            },
            "turrets": {
                0: {
                    "MountedWeapons": {
                        "AutoCanon_AP_30mm_Bitube_Gsh30k": {
                            "Ammunition": "AutoCanon_AP_30mm_Bitube_Gsh30k_burst",
                            "EffectTag": "'FireEffect_GatlingAir_Gsh_30_2_30mm_x2'",
                        },
                        "AutoCanon_HE_30mm_Bitube_Gsh30k": {
                            "Ammunition": "AutoCanon_HE_30mm_Bitube_Gsh30k_burst",
                            "EffectTag": "'FireEffect_GatlingAir_Gsh_30_2_30mm_x2'",
                        },
                    },
                },
            },
        },
        "availability": [0, 0, 3, 2],
    },

    "Mi_24P_AA_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "GameName": {
            "display": "Mi-24P [AA]",
        },
        "CommandPoints": 185,
        "strength": "Mi_24P_SOV",
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_30mm_Bitube_Gsh30k": 5,
            },
            "turrets": {
                0: {
                    "MountedWeapons": {
                        "AutoCanon_AP_30mm_Bitube_Gsh30k": {
                            "Ammunition": "AutoCanon_AP_30mm_Bitube_Gsh30k_burst",
                            "EffectTag": "'FireEffect_GatlingAir_Gsh_30_2_30mm_x2'",
                        },
                        "AutoCanon_HE_30mm_Bitube_Gsh30k": {
                            "Ammunition": "AutoCanon_HE_30mm_Bitube_Gsh30k_burst",
                            "EffectTag": "'FireEffect_GatlingAir_Gsh_30_2_30mm_x2'",
                        },
                    },
                },
            },
        },
        "availability": [0, 0, 3, 2],
    },

    "Mi_24VP_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 200,
        "strength": "Mi_24P_SOV",
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_23mm_Bitube_Gsh23L": 28,
                "RocketAir_B8_80mm_salvolength10": 4,
                "AGM_9M114M_KokonM_salvolength16": 1,
            },
        },
        "availability": [0, 2, 0, 1],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
    },
    
    "Mi_24P_Atakax4_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 200,
        "strength": "Mi_24P_SOV",
        "availability": [0, 2, 0, 1],
    },
    
    "Mi_24P_Atakax8_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 230,
        "strength": "Mi_24P_SOV",
        "availability": [0, 2, 0, 1],
    },
    
    "Ka_29_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 230,
        "strength": 10,
        "availability": [0, 2, 0, 1],
    },
    
    "Ka_50_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 230,
        "availability": [0, 2, 0, 1],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
    },
    
    "Ka_50_AA_SOV": {
        "XP": {
            "pack": "helico_attack",
        },
        "availability": [0, 3, 2, 0],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
    },

    # SOV AIR
    "L39ZO_HE1_SOV": {  # 2x FAB-500
        "CommandPoints": 75,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 5, 0, 0],
    },

    "L39ZO_NPLM_SOV": {  # 2x ZB-500
        "CommandPoints": 60,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 6, 0, 0],
    },

    "L39ZO_SOV": {  # 2x 32x S-5M
        "CommandPoints": 60,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 5, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "RocketAir_S5_57mm_salvolength32": {
                        "new_weapon": "RocketAir_S5_57mm_avion_salvolength32",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },

    "MiG_21bis_CLU_SOV": {  # 2x RBK-500, 2x RBK-250
        "CommandPoints": 190,
        "ECM": -0.25,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "MiG_21bis_HE_SOV": {  # 2x RBK-500, 2x RBK-250
        "CommandPoints": 145,
        "ECM": -0.15,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 2, 0],
    },
    
    "MiG_21SMT_AA_SOV": {  # 2x R-3R, 2x R-13M1
        "CommandPoints": 120,
        "ECM": -0.15,
        "FuelModule": {
            "FuelCapacity": 3600,
            "FuelMoveDuration": 360,
        },
        "availability": [0, 4, 3, 2],
    },
    
    "MiG_23ML_SOV": { # 3x R-60M, 3x R-60M
        "CommandPoints": 130,
        "ECM": -0.15,
        "availability": [0, 4, 3, 2],
    },

    "MiG_23MLA_AA_SOV": {  # 2x R-24R, 4x R-60M
        "CommandPoints": 140,
        "ECM": -0.15,
        "availability": [0, 3, 2, 0],
    },

    "MiG_23MLD_AA1_SOV": {  # 2x R-24R, 4x R-60M
        "CommandPoints": 145,
        "ECM": -0.2,
        "availability": [0, 3, 2, 0],
    },

    "MiG_23MLD_SOV": {  # 2x R-24MR, 2x R-73
        "CommandPoints": 175,
        "ECM": -0.2,
        "Divisions": {
            "add": ["SOV_76_VDV"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 2, 0],
    },

    "MiG_23P_SOV": {  # 2x R-24MR, 2x R-13M1
        "CommandPoints": 160,
        "availability": [0, 3, 2, 0],
    },

     "MiG_25RBF_SOV": { # 8x FAB-500
        "CommandPoints": 175,
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1800,
            },
        },
        "availability": [0, 2, 0, 0],
    },
    
    "MiG_25BM_SOV": {  # Kh-58U 6300m
        "CommandPoints": 270,
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1800,
            },
        },
        "availability": [0, 2, 0, 1],
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
    },
    
    "MiG_25PD_SOV": {
        "CommandPoints": 220,
        "ECM": -0.15,
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1800,
            },
        },
        "availability": [0, 2, 0, 1],
    },
    
    "MiG_27K_AT1_SOV": { # GSh-6-30, 2x Kh-29L, 40x S-8KOM
        "CommandPoints": 170,
        "ECM": -0.2,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 4550.0,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMaxPitch": 1.047198, # 60 degrees
                    "AngleRotationMinPitch": -1.047198,
                },
            },
            "Salves": {
                "GatlingAir_AP_Gsh_30_6_30mm": (4, False),
                "AGM_Kh29L": (2, True),
                "RocketAir_B8_80mm_salvolength40": (1, True),
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "MiG_27K_AT2_SOV": { # GSh-6-30, 2x Kh-29T, 4x R-60M
        "CommandPoints": 195,
        "ECM": -0.2,
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_Kh29T": 1,
            },
        },
    },

    "MiG_27K_LGB_SOV": {
        "CommandPoints": 260,
        "ECM": -0.3,
        "GameName": {
            "display": "MiG-27K [PGB]",
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 0, 2],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "GatlingAir_Gsh_30_6_30mm": {
                        "new_weapon": "GatlingAir_Gsh_30_6_30mm_NoShootPos",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
            "SalvoIsMainSalvo": [False, True, False],
        },
    },

    "MiG_27K_SEAD_SOV": {  # MiG-27K [SEAD2] - Kh-25MP 5250m
        "CommandPoints": 180,
        "ECM": -0.4,
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
                1: {
                    "AngleRotationMax": 0.9599311,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "availability": [0, 2, 0, 0],
    },
    
    "MiG_27M_sead_SOV": {  # MiG-27K [SEAD] - Kh-28 5600m
        "CommandPoints": 195,
        "ECM": -0.4,
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
                1: {
                    "AngleRotationMax": 0.9599311,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "availability": [0, 2, 0, 0],
        "Divisions": {
            "add": ["SOV_27_Gds_Rifle"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 1,
            },
        },
    },

    "MiG_27M_bombe_SOV": {  # 4x FAB-500
        "CommandPoints": 175,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 0, 0],
    },
    
    "MiG_27M_CLU_SOV": {
        "CommandPoints": 195, # Vanilla price
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 2, 0, 0],
    },

    "MiG_27M_SOV": { # GSh-6-30, 2x Kh-29T
        "CommandPoints": 195,
        "ECM": -0.3,
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_Kh29T": 1,
            },
        },
    },

    "MiG_27M_napalm_SOV": {  # 4x ZB-500
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 0, 0],
    },
    
    "MiG_27M_rkt_SOV": {
        "CommandPoints": 140,
        "availability": [0, 3, 2, 0],
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "RocketAir_B8_80mm_salvolength40": 1,
        #     },
        #     "equipmentchanges": {
        #         "replace": {
        #             "RocketAir_B8_80mm_avion_salvolength10": [
        #                 {
        #                     "new_weapon": "RocketAir_B8_80mm_salvolength40",
        #                     "swap_fire_effect": False,
        #                     "depiction_baked_in": False,
        #                 },
        #                 {
        #                     "new_weapon": "RocketAir_B8_80mm_salvolength40",
        #                     "swap_fire_effect": False,
        #                     "depiction_baked_in": False,
        #                 },
        #             ],
        #         },
        #     },
        # },
    },
    
    "MiG_29S_SOV": {
        "CommandPoints": 285,
        "availability": [0, 2, 0, 1],
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "UpgradeFromUnit": "MiG_29_AA_SOV",
    },

    "MiG_29_9_13_SOV": {  # 2x R-27R, 4x R-73
        "CommandPoints": 230,
        "availability": [0, 2, 0, 1],
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "UpgradeFromUnit": "MiG_29_AA_SOV",
    },

    "MiG_29_AA2_SOV": {  # 2x R-60M, 2x R-27R
        "CommandPoints": 185,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 3,
            },
        },
        "availability": [0, 2, 0, 1],
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "UpgradeFromUnit": "MiG_29_AA_SOV",
    },

    "MiG_29_AA3_SOV": {  # 4x R-73, 2x R-27T
        "CommandPoints": 185,
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "UpgradeFromUnit": "MiG_29_AA_SOV",
        "ButtonTexture": "MiG_29_AA_SOV",  # match icon to model (regular icon has wrong camo)
    },

    "MiG_29_AA_SOV": {  # 4x R-73, 2x R-27R
        "GameName": {
            "display": "MiG-29 [AA]",
        },
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "availability": [0, 2, 0, 1],
        "UpgradeFromUnit": None,
    },

    "MiG_31M_SOV": {  # 4x R-33S
        "GameName": {
            "display": "MiG-31B [AA]",
        },
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1800,
            },
        },
        "ECM": -0.2,
        "CommandPoints": 270,
        "availability": [0, 2, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AA_R37_Vympel": 2,
            },
        },
    },

    "MiG_31_AA1_SOV": {  # 4x R-33, 2x R-40TD1
        "GameName": {
            "display": "MiG-31 [AA]",
        },
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1800,
            },
        },
        "ECM": -0.2,
        "CommandPoints": 270,
        "availability": [0, 2, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AA_R33_Vympel": 2,
            },
        },
    },

    "MiG_31_AA2_SOV": {  # 4x R-33, 4x R-60M
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1800,
            },
        },
        "ECM": -0.2,
        "CommandPoints": 240,
        "availability": [0, 2, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AA_R33_Vympel": 2,
            },
        },
    },

    "Su_15TM_AA_SOV": {  # 1x R-98MT, 1x R-98MR, 2x R-60M
        "CommandPoints": 125,
        "ECM": -0.05,
        "availability": [0, 3, 2, 0],
    },

    "Su_15TM_AA2_SOV": {  # 2x R-98MT, 2x R-60M, 2x UPK-23-250
        "CommandPoints": 135,
        "ECM": -0.05,
        "availability": [0, 3, 2, 0],
    },

    "Su_17M4_HE1_SOV": {  # 6x FAB-500, 2x R-60M
        "CommandPoints": 190,
        "ECM": -0.2,
        "availability": [0, 2, 0, 0],
    },

    "Su_17M4_HE2_SOV": {  # 4x FAB-500, 2x RBK-500, 2x R-60M
        "CommandPoints": 230,
        "ECM": -0.3,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "Su_17M4_CLU_SOV": {  # 4x FAB-500, 2x RBK-500, 2x R-60M
        "CommandPoints": 240,
        "ECM": -0.3,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "Su_17M4_SOV": {  # 20x S-13, 2x R-60M
        "CommandPoints": 120,
        "ECM": -0.2,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 2, 0],
    },

    "Su_17M4_RKT2_SOV": { # 2x 40x SK-80s, 2x R-60M
        "CommandPoints": 120,
        "ECM": -0.20,
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketAir_B8_80mm_salvolength40": 2,
            },
            "equipmentchanges": {
                "replace": {
                    "RocketAir_B8_80mm_salvolength80": {
                        "new_weapon": "RocketAir_B8_80mm_salvolength40",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },

    "Su_17M4_thermo_SOV": {  # 6x ODAB-500PM, 2x R-60M
        "CommandPoints": 220,
        "ECM": -0.3,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "Su_22_AT_SOV": {  # 2x Kh-29T, 2x R-60M
        "CommandPoints": 195,
        "ECM": -0.3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_Kh29T": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
    },

    "Su_17M4_AT2_SOV": {  # 4x S-25LD guided AT rockets, 2x R-60M
        "CommandPoints": 170,
        "ECM": -0.2,
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMaxPitch": 1.047198, # 60 degrees
                    "AngleRotationMinPitch": -1.047198,
                },
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "Su_17M4_SEAD_SOV": {  # KH-25
        "CommandPoints": 180,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "ECM": -0.4,
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
                1: {
                    "AngleRotationMax": 0.9599311,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 3, 0, 2],
    },

    "Su_24MP_EW_SOV": { # EW
        "CommandPoints": 135,
        "ECM": -0.45,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 2, 0],
    },

    "Su_24MP_SEAD2_SOV": {  # SEAD2
        "CommandPoints": 300,
        "ECM": -0.45,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
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
                1: {
                    "AngleRotationMax": 0.9599311,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 1],
    },

    "Su_24MP_SOV": {  # Kh-28 5425m
        "CommandPoints": 255,
        "ECM": -0.45,
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
                1: {
                    "AngleRotationMax": 0.9599311,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 1],
    },

    "Su_24M_AT1_SOV": {
        "GameName": {
            "display": "Su-24M [AT]",
        },
        "CommandPoints": 240,
        "ECM": -0.35,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "AGM_Kh29T": 1,
            },
        },
    },

    "Su_24M_AT2_SOV": {
        "CommandPoints": 210,
        "ECM": -0.35,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 4550.0,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMaxPitch": 1.047198, # 60 degrees
                    "AngleRotationMinPitch": -1.047198,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
    },

    "Su_24M_LGB_SOV": {
        "GameName": {
            "display": "Su-24M [PGB]",
        },
        "CommandPoints": 265,
        "ECM": -0.35,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 4550.0,
            },
        },
        "UpgradeFromUnit": None,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "Bomb_KAB_1500Kr": {
                        "new_weapon": "Bomb_KAB_1500L_salvolength2",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "Bomb_KAB_1500L_salvolength2": 1,
            },
        },
        "availability": [0, 0, 0, 1],
    },

    "Su_24M_LGB2_SOV": {
        "CommandPoints": 280,
        "ECM": -0.35,
        "GameName": {
            "display": "Su-24M [PGB2]",
        },
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 4550.0,
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "GatlingAir_Gsh_23_6_23mm": {
                        "new_weapon": "GatlingAir_Gsh_23_6_23mm_NoShootPos",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                    "Bomb_KAB_1500L": {
                        "new_weapon": "Bomb_KAB_1500Kr",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
        "availability": [0, 0, 0, 1],
    },

    "Su_24M_SOV": {
        "CommandPoints": 210,
        "ECM": -0.35,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "Su_24M_clu2_SOV": {
        "CommandPoints": 240,
        "ECM": -0.35,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "Su_24M_clu_SOV": {
        "CommandPoints": 240,
        "alternatives": {
            "mesh": "Su_24M_T2_SOV",
        },
        "ECM": -0.35,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "Bomb_CLU_RBK_250kg_salvolength8"),],
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "Tag": '"tourelle3"',
                            "YulBoneOrdinal": 3,
                        },
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": '"WeaponAlternative_3"',
                        "WeaponActiveAndCanShootPropertyName": '"WeaponActiveAndCanShoot_3"',
                        "WeaponIgnoredPropertyName": '"WeaponIgnored_3"',
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
            },
            "Salves": {
                "insert": [(2, 1)],
            },
            "SalvoIsMainSalvo": [False, True, True],
        },
    },
    
    "Su_24M_nplm_SOV": {
        "CommandPoints": 200,
        "ECM": -0.35,
        "availability": [0, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
    },

    "Su_24M_thermo_SOV": {
        "CommandPoints": 235,
        "ECM": -0.35,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
    },
    
    "Su_25T_SOV": {  # 16x Vikhr, 2x R-73
        "CommandPoints": 280,
        "ECM": -0.40,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 750,
            },
        },
        "max_speed": 750,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 1],
    },

    "Su_25_SOV": {  # 4x Kh-25ML, 2x R-60M
        "CommandPoints": 260,
        "ECM": -0.20,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 750,
            },
        },
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 4550.0,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMaxPitch": 1.047198, # 60 degrees
                    "AngleRotationMinPitch": -1.047198,
                },
            },
        },
        "max_speed": 750,
        "availability": [0, 2, 0, 1],
    },

    "Su_25_clu_SOV": {  # 6x RBK-250, 2x R-60M
        "CommandPoints": 220,
        "ECM": -0.20,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 750,
            },
        },
        "max_speed": 750,
        "availability": [0, 2, 0, 0],
    },

    "Su_25_he_SOV": {  # 6x FAB-500, 2x R-60M
        "CommandPoints": 220,
        "ECM": -0.20,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 750,
            },
        },
        "max_speed": 750,
        "availability": [0, 2, 0, 0],
    },

    "Su_25_nplm_SOV": {  # 4x ZB-500, 2x R-60M
        "CommandPoints": 180,
        "ECM": -0.20,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 750,
            },
        },
        "max_speed": 750,
        "availability": [0, 2, 0, 0],
    },
    
    "Su_25_RKT3_SOV": {
        "CommandPoints": 220,
        "ECM": -0.20,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 750,
            },
        },
        "max_speed": 750,
        "availability": [0, 2, 0, 0],
    },

    "Su_25_rkt2_SOV": {  # x10 S-13, x2 x40 S-8KOM
        "CommandPoints": 220,
        "ECM": -0.20,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 750,
            },
        },
        "max_speed": 750,
        "availability": [0, 2, 0, 0],
    },

     "Su_25_rkt_SOV": {  # x2 x40 S-8KOM
        "CommandPoints": 220,
        "ECM": -0.20,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 750,
            },
        },
        "max_speed": 750,
        "availability": [0, 2, 0, 0],
    },

    "Su_27K_SOV": {  # 2x R-73, 4x R-27R, 2x R-24T
        "CommandPoints": 235,
        "ECM": -0.20,
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "availability": [0, 2, 0, 1],
        "UpgradeFromUnit": "Su_27S_SOV",
    },

    "Su_27S_SOV": {  # 6x R-73, 4x R-27R
        "CommandPoints": 225,
        "ECM": -0.20,
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "availability": [0, 2, 0, 1],
    },

    "Su_27S_jammers_SOV": {  # 4x R-27ER, 2x R-27T, 40% ECM
        "CommandPoints": 270,
        "ECM": -0.30,
        "SpecialtiesList": {
            "add_specs": ["'_hmd'", "'_jammer_air'"],
        },
        "availability": [0, 2, 0, 1],
        "UpgradeFromUnit": "Su_27K_SOV",
    },
    
    "Tu_22_EW_SOV": {
        "CommandPoints": 145,
        "ECM": -0.55,
        "availability": [0, 2, 0, 1],
    },
    
    "Tu_22_HE_SOV": {
        "CommandPoints": 290,
        "ECM": -0.40,
        "availability": [0, 2, 0, 0],
    },
    
    "Yak28_PP_EW_SOV": {
        "CommandPoints": 145,
        "ECM": -0.55,
    },
}
