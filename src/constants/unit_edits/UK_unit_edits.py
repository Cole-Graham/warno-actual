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

    "Saxon_CMD_UK": {
        "CommandPoints": 155,
        "availability": [0, 3, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 56,
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
        "is_infantry": True,
        "is_ground_vehicle": False,
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
                "add": [(1, "RocketInf_M72A3_LAW_66mm")],
                "add_edits": {
                    1: {
                        "SalvoStockIndex": 1,
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
                "add": [(1, 7)], # (salve_index, salves)
                "PM_Sterling": 22,
            },
        },
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "is_infantry": True,
        "is_ground_vehicle": False,
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
        "is_infantry": True,
        "is_ground_vehicle": False,
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
        "is_infantry": True,
        "is_ground_vehicle": False,
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
        "WeaponAssignment": [
                (0, [0, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, ]),
                (6, [0, 1]),
                (7, [0, 2]),
            ],
        "WeaponDescriptor": {
            "Salves": {
                "add": [(2, 7)], # (turret, salves)
            },
            "equipmentchanges": {
                "add": [(2, "RocketInf_M72A3_LAW_66mm")],
            },
        },
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
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

    "Bedford_MJ_4t_trans_UK": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Gun_Group_TA_UK": {
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "strength": 5,
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_L1A1_SLR": 3,
                },
            },
        },
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
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
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

    "AT_Group_TA_UK": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "strength": 5,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
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

    "Engineers_TA_UK": {
        "CommandPoints": 40,
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
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
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

    "Rifles_UK": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "availability": [10, 7, 0, 0],
    },
    
    "HMGteam_MAG_UK": {
        "CommandPoints": "HMGteam_M60_US",
        "GameName": {
            "display": "MAG 7.62mm"
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
            "display": "MAG 7.62mm"
        },
        "strength": "HMGteam_M60_AB_US",
        "max_speed": "HMGteam_M60_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_AB_US",
        },
    },
    
    "HMGteam_M2HB_para_UK": {
        "CommandPoints": "HMGteam_M2HB_AB_US",
        "strength": "HMGteam_M2HB_AB_US",
        "max_speed": "HMGteam_M2HB_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_AB_US",
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
        "availability": [8, 6, 0, 0],
    },

    "ATteam_Milan_1_UK": {
        "CommandPoints": 30,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [9, 7, 5, 0],
    },

    "ATteam_Milan_2_UK": {
        "CommandPoints": 45,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [6, 4, 0, 0],
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
        "availability": [0, 5, 4, 3],
    },

    "Howz_L118_105mm_UK": {
        "CommandPoints": 60,
        "availability": [4, 3, 0, 0],
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
                1: {
                    "AngleRotationMaxPitch": 1.0,
                },
            },
        },
        "availability": [0, 1, 0, 0],
    },

    # UK TANK
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
    "Ferret_Mk2_UK": {
        "CommandPoints": 15,
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M1919": 40,
            },
        },
    },

    "FV601_Saladin_UK": {
        "CommandPoints": 35,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M1919": 40,
            },
        },
    },

    "FV721_Fox_UK": {
        "CommandPoints": 35,
        "availability": [8, 6, 0, 0],
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
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
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

    "Scout_Airmobile_UK": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "DeploymentShift": 0,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "availability": [6, 4, 0, 0],
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
                "replace": [("PM_Sterling", "PM_Sterling_noreflex")],
            },
        },
        "availability": [9, 7, 0, 0],
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
    
    "Tornado_ADV_SEAD_UK" : { # ALARM 5600m
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
            },
        },
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

    "Harrier_HE1_UK": {  # 2x mk83 450kg
        "GameName": {
            "display": "HARRIER GR.3 [HE]",
        },
        "CommandPoints": 130,
        "availability": [0, 4, 0, 0],
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

    "Tornado_ADV_HE_UK": {
        "CommandPoints": 220,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "Harrier_UK": {  # 4x AIM-9L
        "CommandPoints": 95,
        "availability": [0, 4, 3, 0],
    },

    "F4_Phantom_AA_F3_UK": { # 4x Skyflash, 4x AIM-9L
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
}
