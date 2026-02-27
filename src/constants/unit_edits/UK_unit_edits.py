"""UK unit edits."""

# from typing import Any, Dict

# fmt: off
uk_unit_edits = {
    # UK LOG
    "LandRover_CMD_UK": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 4, 0, 0],
    },
    
    "LandRover_CMD_nonBerlin_UK": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 4, 0, 0],
    },
    
    "LandRover_CMD_UK": {
        "CommandPoints": 145,
        "GameName": {
            "display": "#CMD ROVER CP"
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 4, 0, 0],
    },

    "Saxon_CMD_UK": {
        "CommandPoints": 155,
        "availability": [0, 0, 3, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 56,
            },
        },
    },
    
    "FV1612_Humber_CMD_UK": {
        "CommandPoints": 155,
        "availability": [0, 3, 0, 0],
    },
    
    "FV105_Sultan_UK": {
        "CommandPoints": 155,
        "availability": [0, 3, 0, 0],
    },
    
    "MCV_80_Warrior_CMD_UK": {
        "CommandPoints": 175,
        "availability": [0, 0, 3, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L94A1_7_62mm": 80,
            },
        },
    },

    "Gazelle_CMD_UK": {
        "CommandPoints": 115,
        "availability": [0, 3, 0, 0],
    },

    # UK INF
    "Territorial_CMD_UK": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR TERRIERS LDR.",
            "token": "QMPRIAZFYF",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Territorial_CMD_UK",
                "Unite",
            ],
        },
        "strength": 7,
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
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_Sterling": 3,
                },
            },
            "Salves": {
                "PM_Sterling": 22,
            },
        },
        "selector_tactic": "(0, 2)",
        "selector_tactic_obj": "00_02",
        "remove_zone_capture": None,
    },

    "Engineers_CMD_UK": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR ASSAULT PIONEERS LDR.",
            "token": "VZOODKAGWE",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Engineers_CMD_UK",
                "Unite",
            ],
        },
        "strength": 8,
        "TransportedTexture": "UseInGame_Transport_assault",
        # "SortingOrder": 20075,
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
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "RocketInf_M72A3_LAW_66mm")],
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
                },
                "quantity": {
                    "PM_Sterling": 8,
                },
            },
            "Salves": {
                "insert": [(1, 7)], # (salve_index, salves)
                "PM_Sterling": 22,
            },
        },
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "remove_zone_capture": None,
    },

    "Rifles_CMD_UK": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR RIFLES LDR.",
            "token": "YGMKZKXXEV",
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
                "UNITE_Rifles_CMD_UK",
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
                '_ifv',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "Divisions": {
            "UK_2nd_Infantry": {
                "Transports": [
                    "Bedford_MJ_4t_trans_UK",
                    "MCV_80_Warrior_UK",
                    "MCV_80_Warrior_MILAN_UK",
                ],
            },
        },
        "remove_zone_capture": None,
    },

    "Airmobile_CMD_UK": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR AIRMOBILE LDR.",
            "token": "CFLNZATSET",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Airmobile_CMD_UK",
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
        "availability": [0, 0, 6, 4],
        "max_speed": 26,
        "remove_zone_capture": None,
    },
    
    "Paratroopers_CMD_UK": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR PARA. LDR.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Paratroopers_CMD_UK",
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
                '_choc',
                '_para',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "strength": 8,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_inf_L7A2_7_62mm": False,
                },
                "quantity": {
                    "FM_L85A1": 6,
                    "MMG_inf_L7A2_7_62mm": 2,
                },
            },
        },
        "remove_zone_capture": None,
    },

    "Airmobile_Mot_CMD_UK": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR MOT. AIRMOBILE LDR.",
            "token": "DPDYRJPOBS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Mot_Airmobile_CMD_UK",
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
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "insert": [(1, 7)], # (salves_index, salves)
            },
            "equipmentchanges": {
                "insert": [(1, "RocketInf_M72A3_LAW_66mm")],
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
        },
        "remove_zone_capture": None,
    },
    
    "Rifles_Gurkhas_CMD_UK": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR GURKHA RIFLES LDR.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Rifles_Gurkhas_CMD_UK",
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
                '_resolute',
                '_choc',
                '_mountaineer',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "strength": 9,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_inf_L7A2_7_62mm", "SAW_L86A1_5_56mm", "MMG_inf_L7A2_7_62mm", "SAW_L86A1_5_56mm")],
                "skeleton_tags": [
                    ("bazooka", "WeaponAlternative_3"),
                    ("grenade", "WeaponAlternative_4")
                ],
                "quantity": {
                    "FM_L85A1": 6,
                    "SAW_L86A1_5_56mm": 3,
                },
                "Salves": {
                    "SAW_L86A1_5_56mm": 30,
                },
            },
        },
        "remove_zone_capture": None,
    },
    
    "Guards_CMD_UK": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR GUARDS LDR.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Guards_CMD_UK",
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
                '_resolute',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "strength": 7,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_L85A1": 6,
                },
                "replace": [("RocketInf_M72A3_LAW_66mm", "RocketInf_LAW_80", "RocketInf_M72_LAW_66mm", "RocketInf_LAW_80")],
            },
            "Salves": {
                "RocketInf_LAW_80": 4,
            },
        },
        "remove_zone_capture": None,
    },
    
    "Supacat_ATMP_UK": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Rover_101FC_UK": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "LandRover_UK": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "LandRover_MP_UK": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "FV1611_Humber_Pig_UK": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "FV1611a_Kremlin_Pig_UK": {
        "CommandPoints": 20,
    },
    
    "VW_T2b_MP_UK": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Bedford_MJ_4t_trans_UK": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Gun_Group_TA_UK": {
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "strength": 6,
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_L1A1_SLR": 4,
                },
            },
        },
    },
    
    "Gun_Group_UK": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [12, 9, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Gun_Group_Paras_UK": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 10, 7, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "RMP_UK": {
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "strength": 5,
        "availability": [0, 12, 9, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_Sterling": 2,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Security_UK": {
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [14, 0, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_Bren_L4A4": False,
                },
                "quantity": {
                    "FM_L1A1_SLR": 5,
                    "SAW_Bren_L4A4": 2,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Territorial_UK": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_Bren_L4A4": False,
                },
                "quantity": {
                    "FM_L1A1_SLR": 4,
                    "SAW_Bren_L4A4": 3,
                },
            },
        },
    },
    
    "Airmobile_TA_UK": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_Carl_Gustav": 8,
            },
            "equipmentchanges": {
                "animate": {
                    "SAW_Bren_L4A4": False,
                },
                "quantity": {
                    "FM_L1A1_SLR": 9,
                    "SAW_Bren_L4A4": 2,
                },
            },
        },
    },
    
    "Paratroopers_TA_UK": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [8, 0, 0, 0],
        "max_speed": 26,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_light'"],
        },
    },
    
    "Paratroopers_MILAN_TA_UK": {
        "CommandPoints": 45,
        "GameName": {
            "display": "TERRIERS PARAS [CG]",
        },
        "armor": "Infantry_armor_reference",
        "availability": [8, 0, 0, 0],
        "max_speed": 26,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_inf_L7A2_7_62mm": False,
                },
                "quantity": {
                    "FM_L1A1_SLR": 6,
                    "MMG_inf_L7A2_7_62mm": 2,
                },
            },
        },
    },
    
    "Paratroopers_UK": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "AT_Group_TA_UK": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "strength": 5,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_Sterling": 5,
                },
            },
            "Salves": {
                "RocketInf_Carl_Gustav": 6,
            },
        },
    },
    
    "AT_Group_Gurkhas_UK": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [0, 10, 7, 0],
    },
    
    "Rifles_Gurkhas_UK": {
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [0, 6, 4, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_LAW_80": 8,
            },
        },
    },

    "Airmobile_UK": {  # 3x FN Mag
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "strength": 10,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_L85A1": 7,
                },
            },
        },
    },

    "Airmobile_MILAN_UK": {  # 7x L85, 2x L86A1 lmg, 1x LAW 80
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_LAW_80": 6,
            },
        },
    },
    
    "Engineers_UK": { # ASSAULT PIONEERS
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "strength": 9,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "SAW_L86A1_5_56mm": 3,
                },
            },
            "Salves": {
                "Grenade_Satchel_Charge": 6,
            },
        },
    },
    
    "Engineers_AT_UK": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "strength": 9,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Engineers_Airmobile_UK": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "availability": [0, 6, 4, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_Carl_Gustav": 7,
            },
        },
    },
    
    "Paratroopers_Engineers_UK": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "availability": [0, 6, 4, 0],
    },
    
    "Paratroopers_Engineers_CarlG_UK": {
        "CommandPoints": 40,
        "GameName": {
            "display": "PARA. ENGINEERS [CG]",
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "availability": [0, 6, 4, 0],
    },

    "Engineers_TA_UK": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "NATO_Garnison_Berlin": {
                "cards": 1,
            },
            "UK_2nd_Infantry": {
                "cards": 2,
            },
        },
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_light'"],
        },
    },

    "Airmobile_Mot_UK": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_Carl_Gustav": 7,
            },
        },
    },

    "Rifles_UK": { # ARM. RIFLES
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "availability": [10, 7, 0, 0],
    },
    
    "Rifles_AT_UK": { # RIFLES
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "strength": 9,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "SAW_L86A1_5_56mm": 3,
                },
            },
            "Salves": {
                "RocketInf_LAW_80": 6,
            },
        },
    },
    
    "Rifles_Patrol_UK": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "availability": [10, 7, 0, 0],
    },
    
    "Rifles_Berlin_UK": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_L85A1": 7,
                },
                "insert": [(2, "MMG_inf_L7A2_7_62mm")],
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
            },
            "Salves": {
                "insert": [(2, 30)],
                "RocketInf_LAW_80": 7,
            },
        },
    },
    
    "Guards_UK": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_L85A1": 6,
                    "SAW_L86A1_5_56mm": 3,
                },
            },
        },
    },
    
    "Guards_CarlG_UK": {
        "CommandPoints": 40,
        "GameName": {
            "display": "GUARDS [CG]",
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_L85A1": 6,
                    "SAW_L86A1_5_56mm": 3,
                },
            },
            "Salves": {
                "RocketInf_Carl_Gustav": 6,
            },
        },
    },
    
    "HMGteam_MAG_UK": {
        "CommandPoints": "HMGteam_M60_US",
        "GameName": {
            "display": "L7A2 7.62mm"
        },
        "strength": "HMGteam_M60_US",
        "max_speed": "HMGteam_M60_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_US",
        },
    },
    
    "HMGteam_MAG_para_UK": {
        "CommandPoints": "HMGteam_M60_AB_US",
        "GameName": {
            "display": "PARA. L7A2 7.62mm"
        },
        "strength": "HMGteam_M60_AB_US",
        "max_speed": "HMGteam_M60_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_AB_US",
        },
    },
    
    "HMGteam_M2HB_UK": {
        "CommandPoints": "HMGteam_M2HB_US",
        "GameName": {
            "display": "L1A1 12.7mm",
        },
        "strength": "HMGteam_M2HB_US",
        "max_speed": "HMGteam_M2HB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_US",
        },
    },
    
    "HMGteam_M2HB_para_UK": {
        "CommandPoints": "HMGteam_M2HB_AB_US",
        "GameName": {
            "display": "PARA. L1A1 12.7mm",
        },
        "strength": "HMGteam_M2HB_AB_US",
        "max_speed": "HMGteam_M2HB_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_AB_US",
        },
    },
    
    "HMGteam_M2HB_M63_UK": {
        "is_standard": (True, "DCA_12_7_HMG_Team"),
        "CommandPoints": 25,
        "GameName": {
            "display": "L1A1 12.7mm M63",
        },
        "strength": 5,
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "RCL_L6_Wombat_UK": {
        "CommandPoints": 35,
        "strength": 5,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "max_speed": 9,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "availability": [10, 7, 0, 0],
    },

    "ATteam_Milan_1_UK": {
        "CommandPoints": 25,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [9, 7, 5, 0],
    },

    "ATteam_Milan_2_UK": {
        "CommandPoints": 40,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [6, 4, 0, 0],
    },
    
    "ATteam_Milan_2_para_UK": {
        "CommandPoints": 40,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [0, 6, 4, 0],
    },
    
    "ATteam_Milan_2_Guards_UK": {
        "UpgradeFromUnit": "ATteam_Milan_1_UK",
    },

    "SAS_UK": {
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [0, 0, 4, 3],
    },
    
    "SAS_G_UK": {
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "availability": [0, 0, 4, 3],
    },

    # UK ARTILLERY
    "FV432_CMD_UK": {
        "CommandPoints": 60,
        "GameName": {
            "display": "#LDR FV432 BATTERY CP",
            "token": "NUDZQLLWOD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_FV432_CMD_UK",
                "Unite",
                "Vehicule",
            ],
        },
        "Factory": "EFactory/Art",
        "IdentifiedTextures": ["Texture_RTS_H_appui", "Texture_appui"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "_leader",
        "SpecialtiesList": {
            "overwrite_all": [
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_appui",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Transport",
        "Divisions": {
            "add": ["UK_2nd_Infantry"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 0, 0],
        "remove_zone_capture": None,
    },

    "81mm_mortar_UK": {
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "UK_2nd_Infantry": {
                "cards": 2,
            },
        },
        "availability": [5, 4, 3, 0],
    },
    
    "81mm_mortar_Para_UK": {
        "CommandPoints": 35,
        "availability": [0, 5, 4, 3],
    },
    
    "81mm_mortar_CLU_UK": {
        "CommandPoints": 50,
        "availability": [0, 4, 3, 0],
    },
    
    "FV432_Mortar_UK": {
        "CommandPoints": 45,
        "availability": [4, 3, 0, 0],
    },
    
    "Howz_QF_25pdr_87mm_UK": {
        "CommandPoints": 55,
        "availability": [5, 4, 3, 0],
    },

    "Howz_L118_105mm_UK": {
        "CommandPoints": 60,
        "availability": [4, 3, 0, 0],
    },
    
    "FV433_Abbot_UK": {
        "CommandPoints": 95,
        "availability": [3, 2, 0, 0],
    },
    
    "Howz_BL_5_5in_140mm_UK": {
        "CommandPoints": 80,
        "availability": [3, 0, 0, 0],
    },

    "FH70_155mm_UK": {
        "CommandPoints": 110,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [3, 2, 0, 0],
    },

    "M107A2_175mm_UK": {
        "GameName": {
            "display": "M107A2",
        },
        "CommandPoints": 185,
        "availability": [2, 0, 1, 0],
    },
    
    "M109A2_UK": {
        "CommandPoints": 180,
        "availability": [3, 2, 0, 0],
    },
    
    "AS90_155mm_UK": {
        "CommandPoints": 230,
        "availability": [3, 2, 0, 0],
    },
    
    "M110A2_Howz_UK": {
        "CommandPoints": 220,
        "availability": [2, 0, 1, 0],
    },

    "M270_MLRS_cluster_UK": {
        "CommandPoints": 300,
        "Divisions": {
            # "add": ["US_8th_Inf"],
            # "is_transported": False,
            # "needs_transport": False,
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

    # UK TANK
    "Centurion_Mk13_CMD_UK": {
        "CommandPoints": 75,
        "GameName": {
            "display": "#LDR CENTURION Mk.13 LDR.",
            "token": "DBEDJIGRRN",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_Centurion_Mk13_CMD_UK",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_reservist',
                '_smoke_launcher',
            ],
        },
        "WeaponDescriptor": {
            "Salves": {
                "MMG_FN_MAG_7_62mm": 96,
            },
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 6, 0, 0],
        "remove_zone_capture": None,
    },
    
    "FV4201_Chieftain_CMD_UK": {
        "CommandPoints": 150,
        "GameName": {
            "display": "#LDR CHIEFTAIN Mk.10 LDR.",
            "token": "JMOQXJZCVT",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_FV4201_Chieftain_CMD_UK",
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
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 96,
                "MMG_L8A2_7_62mm": 96,
            },
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 2, 0],
        "remove_zone_capture": None,
    },
    
    "Challenger_1_Mk1_CMD_UK": {
        "CommandPoints": 205,
        "GameName": {
            "display": "#LDR CHALLENGER Mk.2 LDR.",
            "token": "LDRBLUCHAL",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_Challenger_1_Mk1_CMD_UK",
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
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L8A2_7_62mm": 96,
            },
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": [0, 0, 2, 0],
        "remove_zone_capture": None,
    },
    
    "FV432_UK": {
        "CommandPoints": 15,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 56,
            },
        },
    },
    
    "FV432_SCAT_UK": {
        "CommandPoints": 15,
    },

    "Saxon_UK": {
        "CommandPoints": 15,
        "orders": {
            "remove_orders": ["EOrderType/Sell"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 56,
            },
        },
    },

    "FV603_Saracen_UK": {
        "CommandPoints": 15,
        "orders": {
            "remove_orders": ["EOrderType/Sell"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 40,
            },
        },
    },
    
    "LandRover_WOMBAT_UK": {
        "CommandPoints": 35,
        "availability": [12, 9, 0, 0],
    },
    
    "LandRover_WOMBAT_Gurkhas_UK": {
        "CommandPoints": 35,
        "availability": [0, 12, 9, 0],
    },
    
    "LandRover_MILAN_nonBerlin_UK": {
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "UK_2nd_Infantry": {
                "cards": 2,
            },
        },
        "availability": [8, 6, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN_2": 6,
            },
        },
    },

    "LandRover_MILAN_UK": {
        "CommandPoints": 45,
        "GameName": {
            "display": "ROVER MILAN",
        },
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "NATO_Garnison_Berlin": {
                "cards": 1,
            },
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN_2": 6,
            },
        },
        "availability": [8, 6, 0, 0],
    },
    
    "LandRover_MILAN_Para_UK": {
        "CommandPoints": 45,
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN_2": 6,
            },
        },
        "availability": [0, 8, 6, 0],
    },
    
    "Supacat_ATMP_MILAN_UK": {
        "CommandPoints": 50,
        "availability": [0, 8, 6, 0],
    },
    
    "FV438_Swingfire_UK": {
        "CommandPoints": 55,
        "availability": [8, 6, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("ATGM_Swingfire_salvolength2", "ATGM_Swingfire_noisy_salvolength2")],
            },
        },
    },
    
    "FV102_Striker_UK": {
        "CommandPoints": 60,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_remote_controlled'"],
        },
        "availability": [8, 6, 0, 0],
    },
    
    "FV102_Striker_para_UK": {
        "CommandPoints": 60,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_remote_controlled'"],
        },
        "availability": [0, 8, 6, 0],
    },

    "MCV_80_Warrior_UK": {
        "CommandPoints": 35,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L94A1_7_62mm": 80,
            },
        },
    },

    "MCV_80_Warrior_MILAN_UK": {
        "CommandPoints": 45,
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN_IFV": 6,
                "MMG_L94A1_7_62mm": 80,
            },
        },
    },
    
    "MCV_80_Warrior_MILAN_ERA_UK": {
        "CommandPoints": 55,
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN_2_IFV": 6,
                "MMG_L94A1_7_62mm": 80,
            },
        },
    },
    
    "Centurion_AVRE_105_UK": {
        "CommandPoints": 65,
        "availability": [8, 6, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M1919": 96,
            },
        },
    },
    
    "FV4003_Centurion_AVRE_UK": {
        "CommandPoints": 65,
        "availability": [8, 6, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M1919": 96,
            },
        },
    },
    
    "FV4003_Centurion_AVRE_ROMOR_UK": {
        "CommandPoints": 75,
        "armor": {
            "top": (3, None),
        },
        "availability": [0, 8, 6, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M1919": 96,
            },
        },
    },
    
    "Centurion_Mk13_UK": {
        "CommandPoints": 65,
        "availability": [10, 0, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_FN_MAG_7_62mm": 96,
            },
        },
    },
    
    "FV4201_Chieftain_Mk1_4_UK": {
        "CommandPoints": 75,
        "availability": [0, 10, 7, 0],
        "capacities": {
            "remove_capacities": ["Instructor_TNK"],
        },
        "SpecialtiesList": {
            "remove_specs": ["'_instructor'"],
        },
        "UpgradeFromUnit": "FV4201_Chieftain_Mk9_CMD_UK",
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 96,
                "MMG_L8A2_7_62mm": 96,
                "HMG_12_7_mm_M2HB_CTRL": 55,
            },
        },
    },
    
    "FV4201_Chieftain_Mk6_UK": {
        "CommandPoints": 85,
        "availability": [10, 7, 0, 0],
        "UpgradeFromUnit": "FV4201_Chieftain_Mk1_4_UK",
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 96,
                "MMG_L8A2_7_62mm": 96,
            },
        },
    },
    
    "FV4201_Chieftain_Mk9_UK": {
        "CommandPoints": 115,
        "availability": [8, 6, 0, 0],
        "UpgradeFromUnit": "FV4201_Chieftain_Mk6_UK",
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 96,
                "MMG_L8A2_7_62mm": 96,
            },
        },
    },
    
    "FV4201_Chieftain_UK": { # Mk10 
        "CommandPoints": 135,
        "availability": [0, 6, 4, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 96,
                "MMG_L8A2_7_62mm": 96,
            },
        },
    },

    "Challenger_1_Mk1_UK": {
        "GameName": {
            "display": "CHALLENGER Mk.2",
        },
        "CommandPoints": 185,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "UK_1st_Armoured": {
                "cards": 4,
            },
            "UK_2nd_Infantry": {
                "cards": 2,
            },
        },
        "availability": [0, 4, 3, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L8A2_7_62mm": 96,
            },
        },
    },

    # UK RECON
    "LandRover_Yeoman_UK": {
        "CommandPoints": 25,
    },
    
    "FV103_Spartan_UK": {
        "CommandPoints": 25,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 96,
            },
        },
    },
    
    "LSV_M2HB_UK": {
        "CommandPoints": 35,
        "availability": [0, 0, 10, 7],
    },
    
    "LSV_MILAN_UK": {
        "CommandPoints": 65,
        "availability": [0, 0, 4, 3],
    },
    
    "Ferret_Mk2_UK": {
        "CommandPoints": 15,
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M1919": 40,
            },
        },
    },
    
    "FV103_Spartan_GSR_UK": {
        "CommandPoints": 30,
        "availability": [0, 8, 0, 0],
    },

    "FV601_Saladin_UK": {
        "CommandPoints": 35,
        "stealth": 1.5,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M1919": 40,
            },
        },
        "UpgradeFromUnit": "Ferret_Swingfire_UK",
    },

    "FV721_Fox_UK": {
        "CommandPoints": 45,
        "availability": [8, 6, 0, 0],
    },
    
    "FV721_Fox_ZB298_UK": {
        "CommandPoints": 60,
        "availability": [0, 6, 4, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 56,
            },
        },
        "UpgradeFromUnit": "FV103_Spartan_GSR_UK",
    },
    
    "Ferret_Swingfire_UK": {
        "CommandPoints": 75,
        "TypeUnit": {
            "AcknowUnitTypes": ["Reco"],
            "TypeUnitFormation": "Reconnaissance",
        },
        "GameName": {
            "display": "#RECO1 FERRET SWINGFIRE",
        },
        "Factory": "EFactory/Recons",
        "stealth": 1.5,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 3500.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/Standard": 150.0,
                "EOpticalStrength/LowAltitude": 150.0,
                "EOpticalStrength/HighAltitude": 40.0,
            },
        },
        "UpgradeFromUnit": "Ferret_Mk2_UK",
        "availability": [6, 4, 0, 0],
        "capacities": {
            "remove_capacities": ["reserviste"],
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UnitRole": "reco",
        "SpecialtiesList": {
            "overwrite_all": [
                '_remote_controlled',
                '_smoke_launcher',
            ],
        },
    },
    
    "FV4201_Chieftain_Mk11_UK": {
        "CommandPoints": 150,
        "TypeUnit": {
            "AcknowUnitTypes": ["Reco"],
            "TypeUnitFormation": "Reconnaissance",
        },
        "GameName": {
            "display": "#RECO1 CHIEFTAIN MK.11",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_Standard",
                "GroundUnits",
                "SM_charLourd",
                "UNITE_FV4201_Chieftain_Mk11_UK",
                "Unite",
            ],
        },
        "Factory": "EFactory/Recons",
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 3500.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/Standard": 150.0,
                "EOpticalStrength/LowAltitude": 150.0,
                "EOpticalStrength/HighAltitude": 40.0,
            },
        },
        "UnitRole": "reco",
        "availability": [0, 4, 3, 0],
        "UpgradeFromUnit": None,
    },
    
    "FV101_Scorpion_UK": {
        "CommandPoints": 45,
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L43A1_7_62mm": 96,
            },
        },
    },
    
    "FV107_Scimitar_UK": {
        "CommandPoints": 50,
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L43A1_7_62mm": 96,
            },
        },
    },
    
    "FV107_Scimitar_Spyglass_UK": {
        "CommandPoints": 55,
        "availability": [6, 4, 0, 0],
    },
    
    "Gazelle_SNEB_reco_UK": {
        "CommandPoints": 45,
        "availability": [0, 6, 4, 0],
    },
    
    "Westland_Scout_SS11_UK": {
        "CommandPoints": 60,
        "availability": [0, 4, 3, 0],
    },
    
    "Lynx_AH_Mk7_Chancellor_UK": {
        "CommandPoints": 55,
        "availability": [0, 4, 0, 0],
    },

    "Scout_TA_UK": {
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "max_speed": 26,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_light'", "'_swift'"],
        },
        "availability": [10, 0, 0, 0],
    },

    "Scout_UK": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "UK_2nd_Infantry": {
                "cards": 2,
            },
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "availability": [8, 6, 0, 0],
    },
    
    "Scout_AT_UK": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "strength": 5,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "availability": [8, 6, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_L86A1_5_56mm": False,
                },
                "quantity": {
                    "SAW_L86A1_5_56mm": 2,
                },
            },
        },
    },

    "Scout_Airmobile_UK": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "availability": [6, 4, 0, 0],
    },
    
    "Scout_Motorized_UK": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "availability": [6, 4, 0, 0],
    },
    
    "Scout_Para_UK": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "availability": [0, 4, 3, 0],
    },
    
    "Pathfinders_UK": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "availability": [0, 0, 4, 3],
    },
    
    "LRRP_UK": { # SAS PATROL
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "availability": [0, 0, 4, 3],
    },

    "Sniper_UK": {
        "GameName": {
            "display": "#RECO2 SNIPERS",
        },
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },
    
    "Sniper_Guards_UK": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(2, "RocketInf_M72A3_LAW_66mm")],
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
            "Salves": {
                "insert": [(2, 2)],
            },
        },
    },

    "Gazelle_UK": {
        "CommandPoints": 30,
        "availability": [0, 6, 0, 0],
    },

    # UK AA
    "MANPAD_Blowpipe_UK": {
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("PM_Sterling", "PM_Sterling_noreflex")],
            },
        },
        "availability": [12, 9, 0, 0],
    },

    "MANPAD_Javelin_UK": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "UK_1st_Armoured": {
                "cards": 2,
            },
            "UK_2nd_Infantry": {
                "cards": 3,
            },
            "UK_4th_Armoured": {
                "cards": 2,
            },
        },
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_L85A1", "FM_L85A1_noreflex")],
            },
        },
        "availability": [7, 5, 0, 0],
    },
    
    "MANPAD_Javelin_para_UK": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_L85A1", "FM_L85A1_noreflex")],
            },
        },
        "availability": [0, 7, 5, 0],
    },

    "DCA_Javelin_LML_UK": {
        "CommandPoints": 35,
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "stealth": 2.5,
        "availability": [6, 4, 0, 0],
    },
    
    "DCA_Starstreak_LML_UK": {
        "CommandPoints": 50,
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "stealth": 2.5,
        "availability": [0, 6, 4, 0],
        "UpgradeFromUnit": "MANPAD_Starstreak_UK",
    },
    
    "Supacat_ATMP_Javelin_LML_UK": {
        "CommandPoints": 35,
        "stealth": 2.0,
        "availability": [6, 4, 0, 0],
    },
    
    "DCA_Oerlikon_GDF_002_35mm_UK": { # Skyguard
        "CommandPoints": 65,
        "availability": [8, 6, 0, 0],
        "armor": {
            "front": (None, "ResistanceFamily_vehicule"),
            "sides": (None, "ResistanceFamily_vehicule"),
            "rear": (None, "ResistanceFamily_vehicule"),
            "top": (None, "ResistanceFamily_vehicule"),
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 220,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "DCA_Rapier_UK": {
        "CommandPoints": 65,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 220,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
        "availability": [6, 4, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "UK_2nd_Infantry": {
                "cards": 1,
                "Transports": ["Rover_101FC_supply_UK"],
            },
        },
    },

    "Tracked_Rapier_UK": {
        "CommandPoints": 85,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 220,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
        "availability": [4, 3, 0, 0],
    },

    "DCA_Rapier_FSA_UK": {  # towed FSB1
        "CommandPoints": 85,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 300,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "availability": [6, 4, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "UK_2nd_Infantry": {
                "cards": 2,
                "Transports": ["Rover_101FC_supply_UK"],
            },
        },
    },
    
    "DCA_Bloodhound_UK": {
        "CommandPoints": 90,
        "availability": [0, 2, 0, 0],
    },

    # UK HELI
    "CH47_Chinook_UK": {
        "CommandPoints": 60,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Lynx_AH_Mk1_UK": {
        "CommandPoints": 50,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Lynx_AH_Mk1_LBH_UK": {
        "CommandPoints": 65,
    },

    "Gazelle_trans_UK": {
        "CommandPoints": 35,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Gazelle_SNEB_UK": {
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 8, 6, 0],
    },
    
    "A109A_RKT_UK": {
        "CommandPoints": 75,
        "availability": [0, 0, 0, 4],
    },

    "Lynx_AH_Mk1_TOW_UK": {
        "CommandPoints": 75,
        "availability": [0, 6, 4, 0],
    },

    "Lynx_AH_Mk7_I_TOW_UK": {  # 8x ITOW
        "CommandPoints": 95,
        "availability": [0, 4, 3, 0],
    },

    "Lynx_AH_Mk7_I_TOW2_UK": {  # 8x FITOW
        "CommandPoints": 130,
        "availability": [0, 4, 3, 0],
    },

    # UK AIR
    "Canberra_T17A_UK": {
        "CommandPoints": 160,
        "availability": [0, 2, 0, 0],
    },
    
    "Canberra_B2_UK": { # [HE/CLU]
        "CommandPoints": 140,
        "availability": [0, 3, 0, 0],
    },
    
    "Buccaneer_S2B_HE_UK": {
        "CommandPoints": 190,
        "availability": [0, 2, 0, 0],
    },
    
    "Buccaneer_S2B_GBU_UK": { # 2x GBU-16
        "CommandPoints": 210,
        "GameName": {
            "display": "BUCCANEER S.2B [PGB]",
        },
        "availability": [0, 1, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Bomb_CPU_123", "Bomb_CPU_123_salvolength2")],
            },
            "Salves": {
                "Bomb_CPU_123_salvolength2": 1,
            },
        },
    },
    
    "Buccaneer_S2B_ATGM_UK": {
        "CommandPoints": 150,
        "availability": [0, 3, 0, 0],
    },
    
    "Buccaneer_S2B_SEAD_UK": { # Martel 5250m
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000,
            },
        },
    },
    
    "Hawk_T1_UK": {
        "CommandPoints": 55,
        "availability": [0, 6, 0, 0],
    },
    
    "Hawk_T1_AA_UK": {  # 2x AIM-9L
        "CommandPoints": 55,
        "availability": [0, 6, 4, 3],
    },

    "Harrier_RKT1_UK": {  # 36x SNEB, 2x AIM-9L
        "GameName": {
            "display": "HARRIER GR.3 [RKT]",
        },
        "CommandPoints": 110,
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketAir_SNEB_68mm_salvolength18", "RocketAir_SNEB_68mm_salvolength36")],
            },
            "Salves": {
                "RocketAir_SNEB_68mm": 1,
            },
        },
        "UpgradeFromUnit": None,
    },

    "Harrier_RKT2_UK": {  # 36x SNEB, 36x SNEB
        "CommandPoints": 100,
        "availability": [0, 4, 3, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketAir_SNEB_68mm_salvolength18", "RocketAir_SNEB_68mm_salvolength36")],
            },
            "Salves": {
                "RocketAir_SNEB_68mm": 1,
            },
        },
        "UpgradeFromUnit": "Harrier_RKT1_UK"
    },

    "Harrier_HE1_UK": {  # 2x mk83 450kg, 2x AIM-9L
        "GameName": {
            "display": "HARRIER GR.3 [HE]",
        },
        "CommandPoints": 130,
        "availability": [0, 4, 0, 0],
    },
    
    "Harrier_HE2_UK": {  # 4x mk18 513kg
        "CommandPoints": 130,
        "availability": [0, 4, 0, 0],
    },
    
    "Harrier_UK": {  # 4x AIM-9L
        "CommandPoints": 95,
        "availability": [0, 4, 3, 0],
    },
    
    "Harrier_GR5_UK": {
        "CommandPoints": 150,
        "availability": [0, 3, 0, 0],
    },
    
    "Harrier_GR5_CLU_UK": {
        "CommandPoints": 195,
        "availability": [0, 2, 0, 0],
    },
    
    "Jaguar_RKT_UK": {  # 36x SNEB, 2x AIM-9L
        "CommandPoints": 125,
        "availability": [0, 3, 2, 0],
    },

    "Jaguar_CLU_UK": {  # 4x BL755 CLU
        "CommandPoints": 205,
        "availability": [0, 2, 0, 0],
    },

    "Jaguar_HE1_UK": {  # 8x mk82 227kg
        "GameName": {
            "display": "JAGUAR GR.1 [HE]",
        },
        "CommandPoints": 190,
        "availability": [0, 2, 0, 0],
    },

    "Jaguar_HE2_UK": {  # 4x Mk18 513kg
        "CommandPoints": 190,
        "availability": [0, 2, 0, 0],
    },
    
    "Jaguar_overwing_UK": {  # 6x Mk18 513kg, 2x AIM-9L
        "CommandPoints": 215,
        "availability": [0, 0, 2, 0],
    },

    "Tornado_ADV_HE_UK": {
        "CommandPoints": 220,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
    },
    
    "Tornado_ADV_clu_UK": {
        "CommandPoints": 240,
        "availability": [0, 2, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
    },
    
    "Tornado_ADV_SEAD_UK" : { # ALARM 5600m
        "availability": [0, 2, 0, 1],
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
            },
        },
        "Divisions": {
            "add": ["UK_2nd_Infantry"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 1,
            },
        },
    },

    "Tornado_ADV_UK": { # 4x Skyflash SuperTEMP, 4x AIM-9L
        "CommandPoints": 250,
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("AA_AIM9L_Sidewinder", "AA_AIM9M_Sidewinder")],
            },
        },
    },
    
    "F4_Phantom_GR2_UK": {
        "CommandPoints": 245,
        "availability": [0, 0, 2, 0],
    },
    
    "F4_Phantom_GR2_HE_UK": { # 6x mk18 513kg, 2x Skyflash
        "CommandPoints": 230,
        "availability": [0, 0, 2, 0],
    },

    "F4_Phantom_AA_F3_UK": { # 4x Skyflash, 4x AIM-9M
        "CommandPoints": 175,
        "GameName": {
            "display": "F-4J(UK) PHANTOM II [AA]",
            "token": "BTFXWDBFCS",
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("AA_AIM9L_Sidewinder", "AA_AIM9M_Sidewinder")],
            },
        },
        "availability": [0, 3, 2, 0],
    },
    
    "F4_Phantom_AA_GR2_UK": { 
        "CommandPoints": 210,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("AA_AIM9L_Sidewinder", "AA_AIM9M_Sidewinder")],
            },
        },
        "availability": [0, 2, 0, 1],
    },
}
