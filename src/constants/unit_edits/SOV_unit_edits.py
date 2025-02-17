"""Soviet unit edits."""

# from typing import Any, Dict

# fmt: off
sov_unit_edits = {
    #SOV LOG
    "BMD_1_CMD_SOV": {
        "CommandPoints": 145,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "BMP_1_CMD_SOV": {
        "CommandPoints": 155,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "BMD_2_CMD_SOV": {
        "CommandPoints": 160,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "LUAZ_967M_CMD_VDV_SOV": {
        "CommandPoints": 145,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
        "SpecialtiesList": {
            "remove_specs": ["'_para'"],
        },
        "ButtonTexture": "LUAZ_967M_SOV",
        "DeploymentShift": 0,
    },

    "BMP_2_CMD_SOV": {
        "CommandPoints": 170,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },
    
    "BTR_60_CMD_SOV": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "BTR_80_CMD_SOV": {
        "CommandPoints": 170,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "Mi_8K_CMD_SOV": {
        "CommandPoints": 145,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
    },

    "Mi_8TZ_SOV": {  # Mi-8MT Gruzovoi
        "GameName": {
            "display": "Mi-8MT GRUZ.",
        },
    },

    "Mi_6_SOV": {  # Mi-6A Gruzovoi
        "GameName": {
            "display": "Mi-6A GRUZ.",
        },
    },

    "Mi_26_SOV": {  # Mi-26 Gruzovoi
        "GameName": {
            "display": "Mi-26 GRUZ.",
        },
    },

    # SOV INF
    "MotRifles_CMD_TTsko_SOV": {
        "CommandPoints": 35,
        "GameName": {
            "display": "#LDRSOV MOTOSTRELKI LDR.",
            # "token": "ZJRMUWLPVH",
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
                "UNITE_MotRifles_CMD_TTsko_SOV",
                "Unite",
            ],
        },
        "strength": 6,
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, 3]),
                (5, [0, 2]),
            ],
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
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
            "SOV_27_Gds_rifle": {
                "Transports": ['GAZ_66_SOV', 'BTR_80_SOV', 'BMP_1P_SOV', 'BMP_2_SOV'],
            },
        },
        "availability": 7,
        "XPMultiplier": [0.0, 0.0, 7/7, 5/7],
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
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "Engineers_CMD_TTsko_SOV": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDRSOV SAPERY LDR.",
            # "token": "QCNBGTPZWL",
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
                "UNITE_Engineers_CMD_TTsko_SOV",
                "Unite"
            ],
        },
        "strength": 8,
        "WeaponAssignment": [
                (0, [0, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, ]),
                (6, [0, ]),
                (7, [0, 1, ]),
            ],
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                'leader_sov',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "Divisions": {
            "SOV_27_Gds_rifle": {
                "Transports": ["GAZ_66_SOV", "MTLB_transp_SOV"],
            },
        },
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 5/5, 4/5],
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
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },
    
    "Engineers_CMD_SOV": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDRSOV SAPERY LDR.",
            # "token": "AGYMPGDUXA",
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
                "UNITE_Engineers_CMD_SOV",
                "Unite"
            ],
        },
        "strength": 8,
        "WeaponAssignment": [
                (0, [0, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, ]),
                (6, [0, ]),
                (7, [0, 1, ]),
            ],
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
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
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 5/5, 4/5],
        "max_speed": 26,
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },
    
    "Spetsnaz_CMD_SOV": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDRSOV SPETSNAZ LDR.",
            # "token": "CKLQCEBSOY",
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
                "UNITE_Spetsnaz_CMD_SOV",
                "Unite",
                "noSIGINT",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry_sf", "Texture_sf"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
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
                "Transports": ["GAZ_66_SOV", "BTR_60_SOV"],
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 4/4, 3/4],
        "max_speed": 26,
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "VDV_CMD_SOV": {
        "CommandPoints": 45,
        "GameName": {
            "display": "#LDRSOV DESANTNIKI LDR.",
            # "token": "JSBZIJKKJJ",
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
                "UNITE_VDV_CMD_SOV",
                "Unite",
            ],
        },
        "strength": 6,
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, 3, ]),
                (5, [0, 2, ]),
            ],
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                'leader_sov',
                '_ifv',
                '_choc',
                '_para',
                'infantry_equip_heavy',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 4/4, 3/4],
        "max_speed": 20,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 5,
                },
            },
            "Salves": {
                "PM_AKSU_74": 7,
                "SAW_RPK_74_5_56mm": 10,
                "MANPAD_igla": 4,
                "Grenade_SMOKE": 3,
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "Engineers_CMD_VDV_SOV": {
        "CommandPoints": 45,
        "GameName": {
            "display": "#LDRSOV DESANT. SAPERY LDR.",
            # "token": "SWFVKVIZVT",
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
                "UNITE_Engineers_CMD_TTsko_SOV",
                "Unite"
            ],
        },
        "strength": 8,
        "WeaponAssignment": [
                (0, [0, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, ]),
                (6, [0, ]),
                (7, [0, 1, ]),
            ],
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                'leader_sov',
                '_choc',
                '_para',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 5/5, 4/5],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AKS_74": 8,
                },
            },
            "Salves": {
                "FM_AKS_74": 9,
                "RocketInf_RPG7": 6,
            },
        },
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },
    
    "Engineers_SOV": {
        "GameName": {
            "display": "SAPERY",
        },
        "CommandPoints": 40,
        "availability": 7,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_119IndTkBrig": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 7/7, 5/7, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 30,
                "Grenade_Satchel_Charge": 5,
            },
        },
        "UpgradeFromUnit": "Engineers_CMD_SOV"
    },
        
    "Engineers_TTsko_SOV": {
        "GameName": {
            "display": "SAPERY",
        },
        "CommandPoints": 40,
        "availability": 7,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 7/7, 5/7, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 30,
                "Grenade_Satchel_Charge": 5,
            },
        },
    },

    "Engineers_VDV_SOV": {
        "GameName": {
            "display": "DESANT. SAPERY",
        },
        "CommandPoints": 30,
        "availability": 10,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 10/10, 7/10, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Engineers_Flam_SOV": {
        "GameName": {
            "display": "SAPERY [RPO]",
        },
        "CommandPoints": 50,
        "availability": 6,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_119IndTkBrig": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 6/6, 4/6, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 7,
                "MMG_PKM_7_62mm": 30,
                "RocketInf_RPO_A_93mm": 4,
            },
        },
    },

    "Engineers_Flam_TTsko_SOV": {
        "GameName": {
            "display": "SAPERY [RPO]",
        },
        "CommandPoints": 50,
        "availability": 6,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 6/6, 4/6, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 7,
                "MMG_PKM_7_62mm": 30,
                "RocketInf_RPO_A_93mm": 4,
            },
        },
    },

    "Engineers_Flam_VDV_SOV": {
        "GameName": {
            "display": "DESANT. SAPERY [RPO]",
        },
        "CommandPoints": 35,
        "availability": 10,
        "XPMultiplier": [0.0, 10/10, 7/10, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 7,
            },
        },
    },
    
    "MotRifles_SOV": {
        "GameName": {
            "display": "MOTOSTRELKI [RPG-7V]",
        },
        "CommandPoints": 30,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "SOV_119IndTkBrig": {
                "cards": 1,
            },
        },
        "XPMultiplier": [12/12, 9/12, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "MotRifles_TTsko_SOV": {  # RPG-27
        "GameName": {
            "display": "MOTOSTRELKI [RPG-27]",
        },
        "CommandPoints": 30,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 9,
                "SAW_RPK_74_5_56mm": 10,
                "RocketInf_RPG27_105mm": 4,
            },
        },
    },

    "MotRifles_BTR_TTsko_SOV": {  # RPG-26
        "GameName": {
            "display": "MOTOSTRELKI [RPG-26]",
        },
        "CommandPoints": 30,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "UpgradeFromUnit": "MotRifles_RPG7V_TTsko_SOV",
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "SAW_RPK_74_5_56mm": 10,
                "RocketInf_RPG26_72_5mm": 7,
            },
        },
    },

    "MotRifles_Metis_TTsko_SOV": {
        "GameName": {
            "display": "MOTOSTRELKI [METIS]",
        },
        "CommandPoints": 40,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 7,
                "SAW_RPK_74_5_56mm": 10,
                "ATGM_9K115_Metis": 6,
            },
        },
    },

    "VDV_Mech_SOV": {  # RPK, SVD, RPG-7VL
        "GameName": {
            "display": "DESANTNIKI [BMD]",
        },
        "CommandPoints": 40,
        "availability": 8,
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
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 9,
            },
        },
    },

    "VDV_SOV": {  # RPK, SVD, RPG-7VL
        "CommandPoints": 40,
        "availability": 8,
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
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 9,
            },
        },
    },

    "VDV_Combine_SOV": {  # RPK, SVD, RPG-7VL
        "CommandPoints": 50,
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 9,
                "RocketInf_RPG22_72_5mm": 4,
            },
        },
    },

    "VDV_Metis_SOV": {
        "GameName": {
            "display": "DESANTNIKI [METIS]",
        },
        "CommandPoints": 50,
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 7,
                "ATGM_9K115_Metis": 5,
            },
        },
    },

    "MP_SOV": {
        "CommandPoints": 15,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
            },
        },
    },

    "VDV_HMG_SOV": {  # VDV Pulemetchiki
        "CommandPoints": 35,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "MotRifles_HMG_SOV": {  # Pulmetchiki
        "CommandPoints": 35,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 30,
                "RocketInf_RPG22_72_5mm": 6,
            },
        },
    },

    "MotRifles_HMG_TTsko_SOV": {  # Pulmetchiki
        "CommandPoints": 35,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 30,
                "RocketInf_RPG22_72_5mm": 6,
            },
        },
    },

    "FireSupport_TTsko_SOV": {
        "CommandPoints": 25,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 7,
                "RocketInf_RPG29_105mm": 6,
            },
        },  
    },
    
    "Spetsnaz_SOV": {
        "CommandPoints": 70,
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPO_A_93mm": 6,
            },
        },
    },

    "Spetsnaz_Vympel_SOV": {  # Spetsgruppa Vympel
        "CommandPoints": 70,
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
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
        "CommandPoints": 35,
        "availability": 8,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
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

    "HMGteam_PKM_SOV": {
        "GameName": {
            "display": "PKM 7.62mm",
        },
    },

    "HMGteam_PKM_TTsko_SOV": {
        "GameName": {
            "display": "PKM 7.62mm",
        },
    },

    "HMGteam_PKM_VDV_SOV": {
        "GameName": {
            "display": "DESANT. PKM 7.62mm",
        },
    },

    "HMGteam_PKM_DShV_SOV": {
        "GameName": {
            "display": "DSh PKM 7.62mm",
        },
    },

    "HMGteam_NSV_SOV": {
        "GameName": {
            "display": "NSV 12.7mm",
        },
    },

    "HMGteam_NSV_TTsko_SOV": {
        "GameName": {
            "display": "NSV 12.7mm",
        },
    },

    "HMGteam_NSV_DShV_SOV": {
        "GameName": {
            "display": "DSh NSV 12.7mm",
        },
    },

    "HMGteam_NSV_VDV_SOV": {
        "GameName": {
            "display": "DESANT. NSV 12.7mm",
        },
    },

    "HMGteam_NSV_6U6_VDV_SOV": {
        "GameName": {
            "display": "DESANT. 6U6 12.7mm",
        },
    },

    "HMGteam_AGS17_SOV": {
        "strength": 5,
        "CommandPoints": 35,
        "availability": 9,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "UpgradeFromUnit": "HMGteam_NSV_SOV",
    },

    "HMGteam_AGS17_TTsko_SOV": {
        "strength": 5,
        "CommandPoints": 35,
        "availability": 9,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "HMGteam_AGS17_VDV_SOV": {
        "strength": 5,
        "CommandPoints": 35,
        "availability": 9,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "ATteam_RCL_SPG9_VDV_SOV": {
        "strength": 3,
        "CommandPoints": 30,
        "availability": 10,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },
    
    "ATteam_Fagot_SOV": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("ATGM_9K111M_Faktoriya", "ATGM_9K111_Fagot")],
            },
        },
    },
    
    "Atteam_Fagot_DShV_SOV": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("ATGM_9K111M_Faktoriya", "ATGM_9K111_Fagot")],
            },
        },
    },

    "Atteam_Fagot_VDV_SOV": {
        "CommandPoints": 30,
        "availability": 9,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.6],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("ATGM_9K111M_Faktoriya", "ATGM_9K111_Fagot")],
            },
        },
    },

    "Atteam_Konkurs_VDV_SOV": {
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "ATteam_Faktoriya_VDV_SOV",
    },

    "ATteam_Konkurs_TTsko_SOV": {
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "ATteam_KonkursM_TTsko_SOV": {
        "CommandPoints": 65,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("ATGM_9M113M_KonkursM", "ATGM_inf_9M113M_KonkursM")],
            },
        },
    },

    "UAZ_469_SPG9_VDV_SOV": {
        "CommandPoints": 25,
        # "availability": 12,
        # "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "LUAZ_967M_SPG9_SOV": {
        "CommandPoints": 25,
        # "availability": 12,
        # "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "LUAZ_967M_SPG9_VDV_SOV": {
        "CommandPoints": 25,
        "availability": 12,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "LUAZ_967M_Fagot_SOV": {
        "CommandPoints": 35,
        "GameName": {
            "display": "LuAZ-967M FAKTORIYA",
            "token": "KYODTOGRYC",
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": 6,
            },
        },
    },

    "LUAZ_967M_VDV_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "UAZ_469_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "UAZ_469_MP_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "Ural_4320_trans_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    "GAZ_66_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "GAZ_66B_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "KrAZ_255B_SOV": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    # SOV ARTILLERY
    "MTLB_CMD_SOV": {
        "CommandPoints": 60,
        "GameName": {
            "display": "#LDRSOV MT-LBu MASHINA",
            "token": "PUEZYZBZLF",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_MTLB_CMD_SOV",
                "Unite",
                "Vehicule",
            ],
        },
        "Factory": "EDefaultFactories/Art",
        "IdentifiedTextures": ["Texture_RTS_H_appui", "Texture_appui"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
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
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
        "remove_zone_capture": None,
    },
    
    "Mortier_2B14_82mm_VDV_SOV": {
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 5,
        "XPMultiplier": [0.0, 1.0, 0.8, 0.6],
    },
    
    "Mortier_2B9_Vasilek_nonPara_SOV": {
        "CommandPoints": 45,
        "availability": 4,
        "orders": {
            "add_orders": ["ShootOnPositionSmoke", "ShootOnPositionWithoutCorrectionSmoke"],
        },
        "XPMultiplier": [1.0, 0.75, 0.5, 0.0],
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "MountedWeapons": {
                        "add": {
                            "Mortier_Vasilek_indirect_82mm_towed": {
                                "Ammunition": "$/GFX/Weapon/Ammo_Mortier_Vasilek_indirect_82mm_SMOKE_towed",
                                "DispersionRadiusOffColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOffThickness": -0.1,
                                "DispersionRadiusOnColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOnThickness": -0.1,
                                "EffectTag": "'FireEffect_Mortier_Vasilek_indirect_82mm_towed'",
                                "HandheldEquipmentKey": "'MeshAlternative_3'",
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
        "CommandPoints": 45,
        "availability": 4,
        "orders": {
            "add_orders": ["ShootOnPositionSmoke", "ShootOnPositionWithoutCorrectionSmoke"],
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.5],
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "MountedWeapons": {
                        "add": {
                            "Mortier_Vasilek_indirect_82mm_towed": {  # donor
                                "Ammunition": "$/GFX/Weapon/Ammo_Mortier_Vasilek_indirect_82mm_SMOKE_towed",
                                "DispersionRadiusOffColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOffThickness": -0.1,
                                "DispersionRadiusOnColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOnThickness": -0.1,
                                "EffectTag": "'FireEffect_Mortier_Vasilek_indirect_82mm_towed'",
                                "HandheldEquipmentKey": "'MeshAlternative_3'",
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
    
    "MTLB_Vasilek_SOV": {
        "CommandPoints": 60,
        "availability": 4,
        "orders": {
            "add_orders": ["ShootOnPositionSmoke", "ShootOnPositionWithoutCorrectionSmoke"],
        },
        "XPMultiplier": [1.0, 0.75, 0.5, 0.0],
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "MountedWeapons": {
                        "add": {
                            "Mortier_Vasilek_indirect_82mm": {  # donor
                                "Ammunition": "$/GFX/Weapon/Ammo_Mortier_Vasilek_indirect_82mm_SMOKE",
                                "DispersionRadiusOffColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOffThickness": -0.1,
                                "DispersionRadiusOnColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOnThickness": -0.1,
                                "EffectTag": "'FireEffect_Mortier_Vasilek_indirect_82mm'",
                                "HandheldEquipmentKey": "'MeshAlternative_4'",
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

    "Howz_D30_122mm_SOV": {
        "CommandPoints": 85,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 5,
        "XPMultiplier": [1.0, 0.8, 0.6, 0.0],
    },

    "2S9_Nona_SOV": {
        "GameName": {
            "display": "2S9 NONA-S",
        },
        "CommandPoints": 85,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "2S23_Nona_SVK_SOV": {
        "GameName": {
            "display": "2S23 NONA-SVK",
        },
        "CommandPoints": 95,
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
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
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "UpgradeFromUnit": None,
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
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
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
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "2S3M_Akatsiya_SOV": {
        "CommandPoints": 180,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
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
        "availability": 2,
        "XPMultiplier": [1.0, 0.0, 0.5, 0.0],
    },

    "BM21V_GradV_SOV": {
        "CommandPoints": 95,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "BM21_Grad_SOV": {
        "CommandPoints": 195,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "TOS1_Buratino_SOV": {
        "CommandPoints": 250,
        "availability": 2,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    # SOV TANK
    "T80BV_CMD_SOV": {
        "CommandPoints": 225,
        "GameName": {
            "display": "#LDRSOV T-80BVK LDR.",
            "token": "YWAOJLFAFW",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T80BV_CMD_SOV",
                "Unite",
            ],
        },
        "armor": {
            "front": 18,
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'Armor_heavy',
                'leader_sov',
                '_smoke_launcher',
                '_era',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
        "remove_zone_capture": None,
    },
    
    "MTLB_transp_SOV": {
        "orders": {
            "add_orders": ["sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "BTR_D_SOV": {
        "CommandPoints": 20,
    },

    "BTR_D_Robot_SOV": {  # 10x Konkurs, 2x PKT
        "CommandPoints": 30,
    },
    
    "BTR_60_SOV": {
        "CommandPoints": 20,
    },

    "BTR_80_SOV": {
        "CommandPoints": 25,
    },

    "BMP_1P_SOV": {
        "CommandPoints": 35,
        "GameName": {
            "display": "BMP-1P [FAKTORIYA]",
            # "token": "CVRIKDQELZ",
        },
    },

    "BMD_2_SOV": {
        "CommandPoints": 35,
    },

    "BMP_2_SOV": {
        "CommandPoints": 50,
    },

    "BMP_2AG_SOV": {
        "CommandPoints": 60,
    },

    "BMP_3_SOV": {
        "CommandPoints": 80,
    },

    "BMD_3_SOV": {
        "CommandPoints": 80,
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "UpgradeFromUnit": "BMD_2_SOV",
    },

    "LUAZ_967M_Fagot_VDV_SOV": {
        "CommandPoints": 35,
        "GameName": {
            "display": "DESANT. LuAZ FAKTORIYA",
            "token": "SXGTONCUAP",
        },
        "availability": 10,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "BRDM_2_Konkurs_SOV": {
        "strength": 8,
        "CommandPoints": 50,
        "stealth": 1.5,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "BRDM_2_Konkurs_M_SOV": {
        "strength": 8,
        "CommandPoints": 65,
        "stealth": 1.5,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "AT_T12_Rapira_SOV": {
        "GameName": {
            "display": "MT-12 RAPIRA 100mm",
        },
        "CommandPoints": 55,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "AT_2A45_SprutB_SOV": {
        "GameName": {
            # "display": "2A45M SPRUT-B",
            "display": "2A45 SPRUT-A",
        },
        "CommandPoints": 55,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "TO_55_SOV": {
        "CommandPoints": 60,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "T80BV_SOV": {
        "armor": {
            "front": 18,
        },
        "availability": 6,
        "CommandPoints": 215,
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
                "replace": [("ATGM_9M112_Kobra", "ATGM_9M112M2_Kobra")],
            },
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "T80U_SOV": {
        "CommandPoints": 260,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },
    
    "T80UD_SOV": {
      "CommandPoints": 290, 
      "Divisions": {
            "default": {
                "cards": 4,
            },
        },
      "availability": 3,
      "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
    },
    
    # SOV RECON
    "UAZ_469_Reco_SOV": {
        "CommandPoints": 25,
    },

    "LUAZ_967M_AGL_VDV_SOV": {
        "CommandPoints": 30,
    },

    "BTR_D_reco_SOV": {
        "CommandPoints": 25,
    },

    "BMP_2_reco_SOV": {
        "CommandPoints": 75,
    },

    "BRM_1_SOV": {
        "CommandPoints": 55,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_6IndMSBrig": {
                "cards": 3,
            },
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "BMD_1_Reostat_SOV": {
        "CommandPoints": 30,
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "BMD_3_reco_SOV": {
        "CommandPoints": 105,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "BRDM_2_SOV": {
        "strength": 8,
        "CommandPoints": 35,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_6IndMSBrig": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "Pchela_1T_SOV": {
        "CommandPoints": 45,
    },

    "Scout_TTsko_SOV": {
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },

    "Scout_VDV_SOV": {
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },

    "Scout_SIGINT_SOV": {
        "CommandPoints": 30,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },
    
    "Engineers_Scout_SOV": {
        "GameName": {
            # "display": "#RECO2 RAZVEDKA SAPERY",
            "display": "#RECO2 RAZV. SAPERY",
        },
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "DeploymentShift": 0,
    },

    "Engineers_Scout_TTsko_SOV": {
        "GameName": {
            # "display": "#RECO2 RAZVEDKA SAPERY",
            "display": "#RECO2 RAZV. SAPERY",
        },
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "HvyScout_SOV": {
        "CommandPoints": 40,
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "DeploymentShift": 0,
    },

    "HvyScout_TTsko_SOV": {
        "CommandPoints": 40,
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "DeploymentShift": 0,
    },

    "Scout_LRRP_SOV": {  # Spetsnaz GRU
        "CommandPoints": 55,
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Scout_Spetsnaz_SOV": {
        "CommandPoints": 65,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "DeploymentShift": 0,
    },

    "Scout_Spetsnaz_VDV_SOV": {
        "CommandPoints": 70,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Mi_24K_reco_SOV": {
        "CommandPoints": 150,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    # SOV AA
    "BTR_ZD_Skrezhet_SOV": {
        "CommandPoints": 30,
    },

    "LuAZ_967M_AA_VDV_SOV": {
        "CommandPoints": 30,
        "Stealth": 2.0,
    },

    "DCA_ZU_23_2_TTsko_SOV": {
        "CommandPoints": 20,
        "Factory": "EDefaultFactories/Logistic",
        "Divisions": {
            "add": ["SOV_119IndTkBrig"],
            "is_transported": True,
            "needs_transport": True,
            "default": {
                "cards": 1,
                "Transports": ["GAZ_66_SOV"],
            },
        },
        "availability": 9,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 4,
        "UpgradeFromUnit": "FOB_SOV",
    },

    "DCA_ZU_23_2_SOV": {  # Airborne
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "Factory": "EDefaultFactories/Logistic",
        "availability": 9,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 4,
        "UpgradeFromUnit": "FOB_SOV",
    },
    
    "MANPAD_Igla_SOV": {
        "CommandPoints": 35,
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_AK_74", "FM_AK_74_noreflex")],
            },
        },
    },

    "MANPAD_Igla_TTsko_SOV": {
        "CommandPoints": 35,
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_AK_74", "FM_AK_74_noreflex")],
            },
        },
    },

    "MANPAD_Igla_VDV_SOV": {
        "CommandPoints": 35,
        "availability": 7,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_AKS_74", "FM_AKS_74_noreflex")],
            },
        },
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
        "availability": 10,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "BRDM_Strela_1_SOV": {
        "strength": 8,
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 6,
        "WeaponDescriptor": {
            "Salves": {
                "SAM_Strela1_salvolength4": 2,
            },
        },
        "XPMultiplier": [6/6, 4/6, 0.0, 0.0],
    },

    "Tunguska_2K22_SOV": {
        "optics": {
            "OpticalStrengthAltitude": 300,
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
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    "Tor_SOV": {
        "optics": {
            "OpticalStrengthAltitude": 300,
        },
        "CommandPoints": 150,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },
    
    "MTLB_Strela10_SOV": {
        "optics": {
            "OpticalStrengthAltitude": 220,
        },
        "CommandPoints": 65,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 6,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "MTLB_Strela10M3_SOV": {
        "optics": {
            "OpticalStrengthAltitude": 220,
        },
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "2K12_KUB_SOV": {
        "optics": {
            "OpticalStrengthAltitude": 300,
        },
        "CommandPoints": 90,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    # SOV HELI
    "Mi_2_trans_SOV": {
        "CommandPoints": 35,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "Mi_8TV_non_arme_SOV": {
        "CommandPoints": 50,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "Mi_8TV_SOV": {  # 32 S-5M x2
        "CommandPoints": 50,
    },
    
    "Mi_8TV_Gunship_SOV": {  # 4x Molniya, 2x S-24
        "CommandPoints": 110,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "WeaponDescriptor": {
            "Salves": {
                "remove": ["RocketAir_B8_80mm_x20"],
                "AA_R60M_Vympel": 4,
            },
            "turrets": {
                2: {
                    "MountedWeapons": {
                        "AA_R60M_Vympel": {
                            "HandheldEquipmentKey": "'MeshAlternative_1'",
                            "SalvoStockIndex": 0,
                            "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_1'",
                            "WeaponIgnoredPropertyName": "'WeaponIgnored_1'",
                            "WeaponShootDataPropertyName": ['WeaponShootData_0_1'],
                        },
                    },
                    "Tag": "'tourelle1'",
                    "YulBoneOrdinal": 1,
                },
                3: {
                    "MountedWeapons": {
                        "RocketAir_S24_240mm_salvolength2": {
                            "SalvoStockIndex": 1,
                        },
                    },
                },
                "remove": [1],
            },
        },
    },

    "Mi_8TV_s57_16_SOV": {
        "GameName": {
            "display": "Mi-8MT [RKT]",
        },
    },
    
    "Mi_8TV_s57_32_SOV": {
        "GameName": {
            "display": "Mi-8MT [RKT2]",
        },
    },

    "Mi_8TV_s80_SOV": {
        "GameName": {
            "display": "Mi-8MT [RKT3]",
        },
        "CommandPoints": 95,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "Mi_24V_AA_SOV": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Mi_24V_RKT_SOV": {  # 4x Kokon, 20x S-13
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Mi_24V_AT_SOV": {  # 8x Kokon, 40x S-80
        "CommandPoints": 160,
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
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },
    
    "Mi_24P_SOV": {
        "GameName": {
            "display": "Mi-24P [AT]",
        },
        "CommandPoints": 160,
        "availability": 2,
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_30mm_Bitube_Gsh30k": 5,
            },
            "turrets": {
                1: {
                    "MountedWeapons": {
                        "AutoCanon_AP_30mm_Bitube_Gsh30k": {
                            "add_members": [("TirContinu", True), ],
                            "Ammunition": "AutoCanon_AP_30mm_Bitube_Gsh30k_burst",
                            "EffectTag": "'FireEffect_GatlingAir_Gsh_30_2_30mm_x2'",
                        },
                        "AutoCanon_HE_30mm_Bitube_Gsh30k": {
                            "add_members": [("TirContinu", True), ],
                            "Ammunition": "AutoCanon_HE_30mm_Bitube_Gsh30k_burst",
                            "EffectTag": "'FireEffect_GatlingAir_Gsh_30_2_30mm_x2'",
                        },
                    },
                },
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },
    
    "Mi_24VP_SOV": {
        "CommandPoints": 200,
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_23mm_Bitube_Gsh23L": 28,
                "RocketAir_B8_80mm_salvolength10": 4,
                "AGM_9M114M_KokonM_salvolength16": 1,
            },
        },
    },

    # SOV AIR
    "Su_17M4_SOV": {  # 20x S-13, 2x R-60M
        "CommandPoints": 125,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Su_22_AT_SOV": {  # 2x Kh-29T, 2x R-60M
        "CommandPoints": 195,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },

    "Su_24MP_EW_SOV": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },
    
    "Su_24MP_SOV": {  # SEAD
        "CommandPoints": 270,
        "WeaponDescriptor": {
            "turrets": {
                2: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },

    "Su_24MP_SEAD2_SOV": {  # SEAD2
        "CommandPoints": 300,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,       
        "WeaponDescriptor": {
            "turrets": {
                2: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },
    
    "Su_24M_LGB_SOV": {
        "GameName": {
            "display": "Su-24M [LGB]",
        },
        "CommandPoints": 245,
        "UpgradeFromUnit": None,
    },

    "Su_24M_LGB2_SOV": {
        "CommandPoints": 260,
    },

    "Su_24M_AT1_SOV": {
        "GameName": {
            "display": "Su-24M [AT]",
        },
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
    },

    "Su_24M_AT2_SOV": {
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
    },

    "Su_24M_SOV": {
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "Su_24M_thermo_SOV": {
        "CommandPoints": 225,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "MiG_27M_bombe_SOV": {  # 4x FAB-500
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "MiG_27M_napalm_SOV": {  # 4x ZB-500
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "MiG_23MLD_SOV": {  # 2x R-24MR, 2x R-73
        "CommandPoints": 175,
        "Divisions": {
            "add": ["SOV_76_VDV"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Su_25T_SOV": {  # 16x Vikhr, 2x R-73
        "CommandPoints": 260,
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
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
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
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
        "UpgradeFromUnit": None,
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
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
        "UpgradeFromUnit": "MiG_29_AA_SOV",
    },

    "MiG_29_AA3_SOV": {  # 4x R-73, 2x R-27T
        "UpgradeFromUnit": "MiG_29_AA2_SOV",
        "ButtonTexture": "MiG_29_AA_SOV",  # match icon to model (regular icon has wrong camo)
    },
    
    "Su_27S_SOV": {  # 6x R-73, 4x R-27R
        "CommandPoints": 240,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },

    "MiG_31_AA1_SOV": {  # 4x R-33, 2x R-40TD1
        "GameName": {
            "display": "MiG-31 [AA]",
        },
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1650,
            },
        },
        "CommandPoints": 310,
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
        "WeaponDescriptor": {
            "Salves": {
                "AA_R33_Vympel": 2,
            },
        },
    },

    "MiG_31_AA2_SOV": {  # 4x R-33, 4x R-60M
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1650,
            },
        },
        "CommandPoints": 290,
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
        "WeaponDescriptor": {
            "Salves": {
                "AA_R33_Vympel": 2,
            },
        },
    },
}
