"""French unit edits."""

# from typing import Any, Dict

# fmt: off
fr_unit_edits = {
    # FR LOG
    
    "VLTT_P4_PC_FR": { # CMD P4 PC
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
    },

    "VLTT_P4_PC_para_FR": { # CMD Para P4 PC
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
        "DeploymentShift": 0,
    },

    "VLTT_P4_PC_Legion_FR": { # CMD Legion P4 PC
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
    },

    "M201_CMD_FR": { # CMD M201 PC
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
    },

    "Auverland_PC_FR": {
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
    },
    
    "VBL_PC_FR": {
        "CommandPoints": 155,
        "strength": 10,
        "availability": [0, 0, 3, 0],
    },

    "VAB_CMD_FR": {
        "CommandPoints": 155,
        "strength": 10,
        "availability": [0, 0, 3, 0],
    },

    "AMX_13_mod56_CMD_FR": {
        "CommandPoints": 145,
        "availability": [0, 0, 3, 0],
    },
    
    "AMX_10_PC_CMD_FR": {
        "CommandPoints": 175,
        "availability": [0, 0, 3, 0],
    },

    "Alouette_II_CMD_FR": {
        "CommandPoints": 115,
        "availability": [0, 3, 0, 0],
    },

    "Gazelle_CMD_FR": {
        "CommandPoints": 115,
        "availability": [0, 3, 0, 0],
    },
    
    "Puma_PC_FR": {
        "CommandPoints": 125,
        "availability": [0, 3, 0, 0],
    },
    
    # FR INF
    "Chasseurs_CMD_FR": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR CHASSEURS LDR.",
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
                "UNITE_Chasseurs_CMD_FR",
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
                '_leader',
                '_ifv',
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
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "RocketInf_LRAC_F1")],
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
                "quantity": {
                    "FM_FAMAS": 8,
                },
            },
            "Salves": {
                "insert": [(2, 6)],
                "FM_FAMAS": 11,
            },
        },
        "remove_zone_capture": None,
    },
    
    "Rifles_CMD_FR": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR GREN.-VOLTIGEURS LDR.",
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
                "UNITE_Rifles_CMD_FR",
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
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_FAMAS": 5,
                },
            },
            "Salves": {
                "FM_FAMAS": 11,
                "Sniper_FRF1": 10,
            },
        },
        "remove_zone_capture": None,
    },
    
    "Sapeurs_CMD_FR": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR SAPEURS LDR.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Sapeurs_CMD_FR",
                "Unite",
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
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(2, "RocketInf_LRAC_F1")],
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
                "insert": [(2, 6)],
                "FM_FAMAS": 11,
            },
        },
        "remove_zone_capture": None,
    },
    
    "Rifles_Aero_CMD_FR": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR AEROMOBILES LDR.",
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
                "Steelman_infanterie_autoresolve",
                "UNITE_Rifles_Aero_CMD_FR",
                "Unite",
            ],
        },
        "strength": 9,
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
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
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "MMG_inf_AANF1_7_62mm")],
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AnimateOnlyOneSoldier": False,
                        "NbWeapons": 3,
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
                    "FM_FAMAS": 6,
                },
            },
            "Salves": {
                "insert": [(1, 45)],
            },
        },
        "remove_zone_capture": None,
    },
    
    "Auverland_FR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "VLTT_P4_FR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "VLTT_P4_Gendarmerie_FR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "TRM_2000_FR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "VLRA_trans_FR": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "TRM_10000_FR": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "Gendarmerie_FR": { # Prevote
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "availability": [0, 12, 9, 0],
        "strength": 5,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_MAT_49": 5,
                },
            },
        },
    },
    
    "Rifles_FR": { # Gren.-Voltigeurs
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "FM_FAMAS": 11,
                "RocketInf_LRAC_F1": 7,
            },
        },
    },
    
    "Rifles_DMR_FR": { # Gren.-Voltigeurs [FR-F1]
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [8, 6, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "FM_FAMAS": 11,
                "RocketInf_LRAC_F1": 7,
            },
        },
    },
    
    "Rifles_APILAS_FR": { # Gren.-Voltigeurs [APILAS]
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "availability": [8, 6, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_FAMAS": 11,
                "RocketInf_APILAS": 6,
            },
        },
    },
    
    "Rifles_Aero_FR": { # AEROMOBILES
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "strength": 11,
        "availability": [8, 6, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_inf_AANF1_7_62mm": False,
                },
                "quantity": {
                    "MMG_inf_AANF1_7_62mm": 2,
                },
            },
            "Salves": {
                "RocketInf_APILAS": 7,
            },
        },
    },
    
    "Escorte_FR": { # Escorte PC
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Chasseurs_FR": { # Chasseurs
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Reserviste_FR": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "availability": [14, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Sapeurs_FR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [0, 7, 5, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "max_speed": 26,
        "UpgradeFromUnit": "Sapeurs_CMD_FR",
    },
    
    "Sapeurs_Flam_FR": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "availability": [0, 7, 5, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "max_speed": 20,
        "UpgradeFromUnit": "Sapeurs_FR",
    },
    
    "Groupe_AT_FR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_FAMAS": 11,
            },
        },
    },
    
    "Commandos_FR": {
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_SIG_543": 7,
            },
        },
    },
    
    "HMGteam_AANF1_FR": {
        "CommandPoints": "HMGteam_M60_US",
        "strength": "HMGteam_M60_US",
        "max_speed": "HMGteam_M60_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_US",
        },
    },
    
    "HMGteam_AANF1_Reserve_FR": {
        "CommandPoints": "HMGteam_M60_NG_US",
        "strength": "HMGteam_M60_NG_US",
        "max_speed": "HMGteam_M60_NG_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_NG_US",
        },
    },
    
    "HMGteam_AANF1_para_FR": {
        "CommandPoints": "HMGteam_M60_AB_US",
        "strength": "HMGteam_M60_AB_US",
        "max_speed": "HMGteam_M60_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_AB_US",
        },
    },
    
    "HMGteam_M2HB_RIMa_FR": {
        "CommandPoints": "HMGteam_M2HB_US",
        "strength": "HMGteam_M2HB_US",
        "max_speed": "HMGteam_M2HB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_US",
        },
    },
    
    "HMGteam_M2HB_para_FR": {
        "CommandPoints": "HMGteam_M2HB_AB_US",
        "strength": "HMGteam_M2HB_AB_US",
        "max_speed": "HMGteam_M2HB_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_AB_US",
        },
    },
    
    "ATteam_Milan_1_FR": {
        "CommandPoints": 25,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [9, 7, 5, 0],
    },
    
    "ATteam_Milan_2_FR": {
        "CommandPoints": 40,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [6, 4, 0, 0],
    },
    
    # FR ARTILLERY
    "Mortier_MORT61_120mm_FR": {
        "CommandPoints": 45,
        "availability": [5, 4, 3, 0]
    },
    
    "VAB_Mortar_81_FR": {
        "CommandPoints": 45,
        "availability": [4, 3, 0, 0],
    },
    
    "AMX_30_AuF1_FR": {
        "CommandPoints": 210,
        "availability": [3, 2, 0, 0],
    },
    
    # FR TANK
    "AMX_30_B2_CMD_FR": {
        "CommandPoints": 135,
        "GameName": {
            "display": "#LDR AMX-30 B2 LDR.",
            "token": "WFTGAGEENP",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_AMX_30_B2_CMD_FR",
                "Unite",
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
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 0, 4, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
        "remove_zone_capture": None,
    },

    "AMX_30_B_CMD_FR": {
        "CommandPoints": 85,
        "GameName": {
            "display": "#LDR AMX-30 B LDR.",
            "token": "ZYIAQBGAXY",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_AMX_30_B_CMD_FR",
                "Unite",
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
        "availability": [0, 0, 5, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
        "remove_zone_capture": None,
    },

    "AMX_13_75mm_CMD_FR": {
        "CommandPoints": 50,
        "GameName": {
            "display": "#LDR AMX-13 T75 LDR.",
            "token": "IMPLFERKOJ",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_AMX_13_75mm_CMD_FR",
                "Unite",
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
        "availability": [0, 0, 6, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
        "remove_zone_capture": None,
    },

    "AMX_10_RC_CMD_FR": {
        "CommandPoints": 120,
        "GameName": {
            "display": "#LDR AMX-10RC LDR.",
            "token": "QAQVLDFWWN",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_AMX_10_RC_CMD_FR",
                "Unite",
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
        "availability": [0, 0, 4, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
        "remove_zone_capture": None,
    },

    "AMX_10_RC_CMD_FR": {
        "CommandPoints": 120,
        "GameName": {
            "display": "#LDR AMX-10RC LDR.",
            "token": "QAQVLDFWWN",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_AMX_10_RC_CMD_FR",
                "Unite",
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
        "availability": [0, 0, 4, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
        "remove_zone_capture": None,
    },

    "ERC_90_Sagaie_CMD_FR": {
        "CommandPoints": 90,
        "GameName": {
            "display": "#LDR ERC-90 LDR.",
            "token": "UZQEPDQLUU",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_ERC_90_Sagaie_CMD_FR",
                "Unite",
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
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
        "remove_zone_capture": None,
    },

    "AML_90_CMD_FR": {
        "CommandPoints": 50,
        "GameName": {
            "display": "#LDR AML-90 LDR.",
            "token": "SPARKJMVEK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_AML_90_CMD_FR",
                "Unite",
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
        "availability": [0, 0, 6, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
        "remove_zone_capture": None,
    },
    
    "Auverland_MILAN_FR": {
        "CommandPoints": 45,
        "availability": [8, 6, 0, 0],
    },
    
    "VLRA_MILAN_FR": {
        "CommandPoints": 45,
        "availability": [0, 8, 6, 0],
    },
    
    "VAB_FR": {
        "CommandPoints": 15,
        "strength": 10,
    },

    "VAB_Reserve_FR": {
        "CommandPoints": 15,
        "strength": 10,
    },

    "VAB_Legion_FR": {
        "CommandPoints": 15,
        "strength": 10,
    },
    
    "VAB_MILAN_FR": {
        "CommandPoints": 30,
        "strength": 10,
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN": 6,
            }
        },
    },

    "VAB_MILAN_Legion_FR": {
        "CommandPoints": 30,
        "strength": 10,
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN": 6,
            }
        },
    },
    
    "VAB_T20_FR": {
        "CommandPoints": 50,
        "strength": 10,
        "availability": [8, 6, 0, 0],
        "Divisions": {
            "add": ["FR_5e_Blindee"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 69,
            },
            "FR_5e_Blindee": {
                "cards": 1,
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "add_custom": [(0, 3, "AutoCanon_HE_T20_20mm")],
                "replace_custom": [(0, 0, 1, "AutoCanon_AP_T20_20mm")],
            },
            "Salves": {
                "DCA_1_canon_T20_20mm": 32,
            },
        },
    },

    "VIB_FR": {
        "CommandPoints": 50,
        "strength": 10,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "add_custom": [(0, 3, "AutoCanon_HE_T20_20mm")],
                "replace_custom": [(0, 0, 1, "AutoCanon_AP_T20_20mm")],
            },
            "Salves": {
                "DCA_1_canon_T20_20mm": 32,
            },
        },
    },

    "VBRG_FR": {
        "CommandPoints": 20,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "AMX_10_P_FR": {
        "CommandPoints": 40,
    },
    
    "AMX_10_P_MILAN_FR": {
        "CommandPoints": 45,
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN_IFV": 4,
            }
        },
    },
    
    "AMX_13_VCI_12_7mm_FR": {
        "CommandPoints": 15,
        "armor": {
            "front": (2, None),
            "sides": (1, None),
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "AMX_13_VCG_12_7mm_FR": {
        "CommandPoints": 15,
        "armor": {
            "sides": (1, None),
        },
    },
    
    "AMX_13_VCI_20mm_FR": {
        "CommandPoints": 30,
        "armor": {
            "front": (2, None),
            "sides": (1, None),
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    ("AutoCanon_AP_M693_F1_20mm", "AutoCanon_AP_M693_F1_20mm_15acc"),
                    ("AutoCanon_HE_M693_F1_20mm", "AutoCanon_HE_M693_F1_20mm_15acc"),
                ],
            },
        },
    },
    
    "VLTT_P4_MILAN_FR": {
        "CommandPoints": 45,
        "availability": [8, 6, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN_2": 6,
            },
        },
    },

    "VLTT_P4_MILAN_para_FR": {
        "CommandPoints": 45,
        "availability": [0, 8, 6, 0],
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN_2": 6,
            },
        },
    },

    "VLTT_P4_MILAN_Legion_FR": {
        "CommandPoints": 45,
        "availability": [0, 8, 6, 0],
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN_2": 6,
            },
        },
    },
    
    "VAB_HOT_FR": {
        "CommandPoints": 75,
        "availability": [6, 4, 0, 0]
    },

    "VAB_HOT_Legion_FR": {
        "CommandPoints": 75,
        "availability": [0, 6, 4, 0]
    },
    
    "AMX_10_HOT_FR": {
        "availability": [6, 4, 0, 0],
    },
    
    "AMX_30_EBG_FR": {
        "CommandPoints": 45,
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 88,
            },
        },
    },

    "AML_90_Reserve_FR": {
        "CommandPoints": 35,
        "availability": [12, 9, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },

    "ERC_90_Sagaie_FR": {
        "CommandPoints": 80,
        "availability": [0, 10, 7, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },

    "AMX_10_RC_tank_FR": {
        "CommandPoints": 105,
        "availability": [8, 6, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },

    "AMX_10_RCR_tank_FR": {
        "CommandPoints": 135,
        "availability": [0, 8, 6, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },
    
    "AMX_13_75mm_TCA_FR": {
        "CommandPoints": 45,
        "availability": [12, 9, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },

    "AMX_13_75mm_TCM_FR": {
        "CommandPoints": 45,
        "availability": [12, 9, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },

    "AMX_13_90mm_FR": {
        "CommandPoints": 50,
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },

    "M47_Patton_Dozer_FR": {
        "CommandPoints": 60,
        "availability": [10, 7, 0, 0],
    },

    "AMX_30_B_FR": {
        "CommandPoints": 75,
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },
    
    "AMX_30_B2_FR": {
        "CommandPoints": 120,
        "availability": [0, 8, 6, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
        "UpgradeFromUnit": "AMX_30_B2_CMD_FR",
    },
    
    "AMX_30_B2_Brennus_FR": {
        "CommandPoints": 140,
        "availability": [0, 0, 6, 4],
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "FR_5e_Blindee": {
                "cards": 2,
            },
        },
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },
    # FR RECON
    "VLRA_HMG_FR": {
        "CommandPoints": 20,
    },
    
    "VLTT_P4_MG_FR": {
        "CommandPoints": 20,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },

    "VLTT_P4_MG_Legion_FR": {
        "CommandPoints": 20,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },

    "Auverland_MG_FR": {
        "CommandPoints": 20,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },

    "M201_MG_FR": {
        "CommandPoints": 20,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },

    "VAB_reco_FR": {
        "CommandPoints": 25,
        "strength": 10,
    },
    
    "Scout_FR": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [8, 6, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_LRAC_F1": 4,
            },
        },
    },
    
    "Scout_Aero_FR": {
        "CommandPoints": 45,
        "max_speed": 26,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "RocketInf_LRAC_F1")],
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "NbWeapons": 1,
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                },
            },
            "Salves": {
                "insert": [(1, 4)],
            },
        },
    },
    
    "LRRP_FR": { # Dragon-Paras
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "AMX_10_P_VOA_FR": {
        "availability": [10, 7, 0, 0],
    },
    
    "VAB_RASIT_FR": {
        "CommandPoints": 30,
        "strength": 10,
        "availability": [8, 0, 0, 0],
    },

    "VAB_RASIT_Legion_FR": {
        "CommandPoints": 30,
        "strength": 10,
        "availability": [8, 0, 0, 0],
    },
    
    "VBL_Reco_FR": {
        "CommandPoints": 15,
        "availability": [10, 7, 0, 0],
    },
    
    "VBL_MILAN_FR": {
        "CommandPoints": 65,
        "availability": [0, 4, 3, 0],
    },

    "M201_RCL_FR": {
        "CommandPoints": 35,
        "availability": [8, 6, 0, 0],
    },

    "AML_60_FR": {
        "CommandPoints": 25,
        "availability": [0, 8, 6, 0],
    },
    
    "AML_60_Gendarmerie_FR": {
        "CommandPoints": 30,
        "availability": [0, 8, 6, 0],
    },

    "EBR_90mm_FR": {
        "CommandPoints": 60,
        "strength": 10,
        "availability": [6, 0, 0, 0],
    },

    "AML_90_FR": {
        "CommandPoints": 50,
        "availability": [6, 4, 0, 0],
    },

    "ERC_90_Sagaie_reco_FR": {
        "CommandPoints": 95,
        "availability": [0, 6, 4, 0],
    },

    "AMX_10_RC_FR": {
        "CommandPoints": 135,
        "availability": [0, 4, 3, 0],
    },

    "AMX_10_RC_Legion_FR": {
        "CommandPoints": 135,
        "availability": [0, 4, 3, 0],
    },
    
    "AMX_10_RCR_FR": {
        "CommandPoints": 165,
        "availability": [0, 0, 3, 2],
    },
    
    "Alouette_III_reco_FR": {
        "availability": [0, 6, 0, 0],
    },
    
    "Gazelle_reco_FR": {
        "CommandPoints": 30,
        "availability": [0, 6, 0, 0],
    },
    
    "Gazelle_20mm_reco_FR": {
        "CommandPoints": 50,
        "availability": [0, 6, 4, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_20mm_M621_GIAT": 10,
            },
        },
    },

    "Ecureuil_reco_FR": {
        "CommandPoints": 35,
        "availability": [0, 6, 0, 0],
    },

    "EH60A_EW_US": {
        "CommandPoints": 75,
        "availability": [0, 3, 0, 0],
    },

    "Puma_Orchidee_FR": { # Exceptional Optics, 6 HP
        "CommandPoints": 45,
        "availability": [0, 4, 0, 0],
    },

    "CM170_Magister_FR": {
        "CommandPoints": 65,
        "availability": [0, 3, 2, 0],
    },

    "CL_89_FR": {
        "CommandPoints": 60,
        "availability": [0, 3, 0, 0],
    },
    
    # FR AA
    "MANPAD_Mistral_FR": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [6, 4, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_FAMAS", "FM_FAMAS_noreflex")],
            },
        },
    },

    "MANPAD_Mistral_para_FR": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_FAMAS", "FM_FAMAS_noreflex")],
            },
        },
    },

    "MANPAD_Mistral_Legion_FR": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_FAMAS", "FM_FAMAS_noreflex")],
            },
        },
    },

    "DCA_M55_FR": { # Quad 50 Cal
        "CommandPoints": 15,
        "availability": [12, 9, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },

    "DCA_Bofors_L60_FR": { # L/60 40mm Bofors
        "CommandPoints": 15,
        "availability": [12, 0, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },

    "DCA_53T2_20mm_FR": { # 20mm AA gun for Logi Tab
        "CommandPoints": 20,
        "availability": [9, 7, 0, 0],
        "max_speed": 6,
        "Factory": "EFactory/Logistic",
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "FOB_FR",
    },

    "DCA_53T2_20mm_Para_FR": { # Para 20mm AA gun for Logi Tab
        "CommandPoints": 20,
        "availability": [0, 9, 7, 0],
        "max_speed": 6,
        "Factory": "EFactory/Logistic",
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },

    "DCA_53T2_20mm_Legion_FR": { # Leigon 20mm AA gun for Logi Tab
        "CommandPoints": 20,
        "availability": [0, 9, 7, 0],
        "max_speed": 6,
        "Factory": "EFactory/Logistic",
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "FOB_FR",
    },

    "DCA_HS831_30mm_FR": { # 30mm AA gun
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },

    "DCA_76T2_20mm_FR": { # CERBERE Duel 20mm
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },

    "DCA_76T2_20mm_CPA_FR": { # SF CERBERE Duel 20mm
        "CommandPoints": 30,
        "availability": [0, 0, 6, 4],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },

    "TRM_2000_20mm_FR": {
        "CommandPoints": 35,
        "availability": [9, 7, 0, 0],
    },
    
    "TRM_2000_20mm_Legion_FR": {
        "CommandPoints": 35,
        "availability": [0, 9, 7, 0],
    },

    "VLRA_20mm_FR": {
        "CommandPoints": 35,
        "availability": [0, 9, 7, 0],
    },

    "M16_MGMC_FR": {
        "CommandPoints": 25,
        "availability": [10, 7, 0, 0],
    },

    "AMX_13_DCA_FR": {
        "CommandPoints": 60,
        "availability": [6, 4, 0, 0],
    },

    "TRM_2000_Mistral_FR": {
        "CommandPoints": 60,
        "availability": [6, 4, 0, 0],
    },

    "VLRA_Mistral_FR": {
        "CommandPoints": 60,
        "availability": [0, 6, 4, 0],
    },
    
    "Crotale_FR": {
        "CommandPoints": 100,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 220,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "availability": [4, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "Roland_2_FR": {
        "CommandPoints": 120,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 220,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "availability": [4, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },
    
    "Roland_3_FR": {
        "CommandPoints": 150,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 300,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "availability": [0, 3, 2, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "FR_5e_Blindee": {
                "cards": 2,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },  

    "DCA_I_Hawk_FR": {
        "CommandPoints": 90,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 300,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "availability": [4, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },
    # FR HELICOPTER
    "Super_Puma_FR": {
        "CommandPoints": 50,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Alouette_II_trans_FR": { 
        "CommandPoints": 35,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Alouette_III_FR": {
        "CommandPoints": 35,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "Gazelle_20mm_FR": {
        "availability": [0, 8, 6, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_20mm_M621_GIAT": 10,
            },
        },
    },

    "Ecureuil_20mm_FR": {
        "CommandPoints": 60,
        "availability": [0, 8, 6, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_20mm_M621_GIAT": 12,
            },
        },
    },

    "Puma_Pirate_FR": {
        "CommandPoints": 65,
        "availability": [0, 7, 5, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_20mm_M621_GIAT": 15,
            },
        },
    },
    
    "Alouette_III_SS11_FR": {
        "CommandPoints": 55,   
        "availability": [7, 5, 0, 0],
    },

    "Gazelle_HOT_FR": {
        "CommandPoints": 70,   
        "availability": [0, 6, 0, 0],
    },
    
    "Gazelle_HOT_2_FR": {
        "CommandPoints": 90,
        "availability": [0, 0, 4, 3],
    },

    
    #FR AIR
    "Mirage_5_F_nplm_FR": {
        "CommandPoints": 160,
        "availability": [0, 3, 0, 0],
    },
    
    "Mirage_5_F_clu_FR": {
        "CommandPoints": 200,
        "availability": [0, 2, 0, 0],
    },
    
    "Mirage_2000_C_FR": {
        "CommandPoints": 175,
        "availability": [0, 3, 2, 0],
    },
    
    "Jaguar_HE_FR": {
        "CommandPoints": 200,
        "availability": [0, 2, 0, 1],
    },
    
    "Jaguar_ATGM_FR": {
        "CommandPoints": 150,
        "availability": [0, 3, 2, 0],
    },
    
    "Jaguar_SEAD_FR": { # Martel 5250m
        "CommandPoints": 150,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "FR_5e_Blindee": {
                "cards": 2,
            },
        },
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
            },
        },
        "availability": [0, 2, 0, 1],
    },
    
    "Jaguar_SEAD2_FR": { # Armat 5775mm
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
            },
        },
    },
    
    "Mirage_IV_SEAD_FR": { # Martel 5250m
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
            },
        },
    },
    "Mirage_III_E_FR": {
        "CommandPoints": 110,
        "strength": 10,
        "availability": [0, 4, 3, 2],
    },
    
    "Mirage_F1_C_FR": {
        "CommandPoints": 150,
        "availability": [0, 3, 2, 0],
    },
}
