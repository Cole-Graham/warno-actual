"""French unit edits."""

# from typing import Any, Dict

# fmt: off
fr_unit_edits = {
    # FR LOG
    "TRM_10000_supply_FR": {
        "GameName": {
            "display": "TRM-10000 LOG.",
        },
    },
    
    "VLTT_P4_PC_FR": { # CMD P4 PC
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
    },
    
    "VAB_CMD_FR": {
        "CommandPoints": 155,
        "strength": 10,
        "availability": [0, 0, 3, 0],
    },
    
    "AMX_10_PC_CMD_FR": {
        "CommandPoints": 160,
        "availability": [0, 0, 3, 0],
    },
    
    "Puma_PC_FR": {
        "CommandPoints": 125,
        "availability": [0, 3, 0, 0],
    },
    # FR INF
    "Chasseurs_CMD_FR": {
        "CommandPoints": 45,
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
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
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
                "add": [(2, "RocketInf_LRAC_F1")],
                "add_edits": {
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "SalvoStockIndex": 2,
                        "HandheldEquipmentKey": "'MeshAlternative_3'",
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
                "add": [(2, 6)],
                "FM_FAMAS": 9,
            },
        },
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },
    
    "Rifles_CMD_FR": {
        "CommandPoints": 30,
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
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, 2]),
            ],
        "TransportedTexture": "UseInGame_Transport_REGINF",
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
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },
    
    "Sapeurs_CMD_FR": {
        "CommandPoints": 50,
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
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, ]),
                (6, [0, ]),
                (7, [0, 2]),
            ],
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
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
                "add": [(2, "RocketInf_LRAC_F1")],
                "add_edits": {
                    2: {
                        "SalvoStockIndex": 2,
                        "HandheldEquipmentKey": "'MeshAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
            },
            "Salves": {
                "add": [(2, 6)],
                "FM_FAMAS": 9,
            },
        },
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },
    
    "VLTT_P4_FR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    
    "TRM_2000_FR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    
    "VLRA_trans_FR": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "TRM_10000_FR": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    
    "Gendarmerie_FR": { # security
        "CommandPoints": 15,
        "availability": [0, 12, 9, 0],
        "strength": 5,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "max_speed": 26,
        "WeaponAssignment": [
                (0, [0, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
            ],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_MAT_49": 5,
                },
            },
        },
    },
    
    "Rifles_FR": {
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "FM_FAMAS": 9,
                "RocketInf_LRAC_F1": 7,
            },
        },
    },
    
    "Rifles_DMR_FR": {
        "CommandPoints": 40,
        "availability": [8, 6, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "FM_FAMAS": 9,
                "RocketInf_LRAC_F1": 7,
            },
        },
    },
    
    "Rifles_APILAS_FR": {   
        "CommandPoints": 45,
        "availability": [8, 6, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_FAMAS": 7,
                "RocketInf_APILAS": 6,
            },
        },
    },
    
    "Escorte_FR": {
        "CommandPoints": 25,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Chasseurs_FR": {
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Reserviste_FR": {
        "CommandPoints": 30,
        "availability": [14, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Sapeurs_FR": {
        "CommandPoints": 35,
        "availability": [0, 7, 5, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "max_speed": 26,
        "UpgradeFromUnit": "Sapeurs_CMD_FR",
    },
    
    "Sapeurs_Flam_FR": {
        "CommandPoints": 50,
        "availability": [0, 7, 5, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "max_speed": 20,
        "UpgradeFromUnit": "Sapeurs_FR",
    },
    
    "Groupe_AT_FR": {
        "CommandPoints": 35,
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_FAMAS": 7,
            },
        },
    },
    
    "Commandos_FR": {
        "CommandPoints": 65,
        "availability": [0, 0, 4, 3],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_FAMAS": 7,
            },
        },
    },
    
    "ATteam_Milan_1_FR": {
        "CommandPoints": 30,
        "availability": [9, 7, 5, 0],
    },
    
    "ATteam_Milan_2_FR": {
        "CommandPoints": 45,
        "availability": [6, 4, 0, 0],
    },
    
    # FR ARTILLERY
    "Mortier_MORT61_120mm_FR": {
        "CommandPoints": 40,
        "availability": [5, 4, 3, 0]
    },
    "VAB_Mortar_81_FR": {
        "CommandPoints": 50,
        "availability": [4, 3, 0, 0],
    },
    "AMX_30_AuF1_FR": {
        "CommandPoints": 210,
        "availability": [3, 2, 0, 0],
    },
    # FR TANK
    "AMX_30_B2_CMD_FR": {
        "CommandPoints": 145,
        "GameName": {
            "display": "#LDR AMX-30 B2 PC LDR.",
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
        "SpecialtiesList": {
            "overwrite_all": [
                'armor',
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
    
    "VAB_FR": {
        "CommandPoints": 20,
        "strength": 10,
    },

    "VAB_Reserve_FR": {
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
    
    "VAB_T20_FR": {
        "CommandPoints": 50,
        "strength": 10,
        # "modules_remove": ["Transporter"],
        # "SpecialtiesList": {
        #     "remove_specs": ["'_transport1'"],
        # },
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
    
    "AMX_10_P_FR": {
        "CommandPoints": 40,
    },
    
    "AMX_10_P_MILAN_FR": {
        "CommandPoints": 45,
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN": 4,
            }
        },
    },
    
    "AMX_13_VCI_12_7mm_FR": {
        "CommandPoints": 15,
        "armor": {
            "front": 2,
            "sides": 1,
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    
    "AMX_13_VCI_20mm_FR": {
        "CommandPoints": 30,
        "armor": {
            "front": 2,
            "sides": 1,
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
    
    "VAB_HOT_FR": {
        "CommandPoints": 75,
        "availability": [6, 4, 0, 0]
    },
    
    "AMX_10_HOT_FR": {
        "availability": [6, 4, 0 ,0],
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
    
    "AMX_30_B_FR": {
        "CommandPoints": 70,
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },
    
    "AMX_30_B2_FR": {
        "CommandPoints": 120,
        "availability": [0, 7, 5, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_AANF1_7_62mm": 44,
            },
        },
    },
    
    "AMX_30_B2_Brennus_FR": {
        "CommandPoints": 150,
        "availability": [0, 0, 4, 3],
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
        "CommandPoints": 25,
    },
    
    "Scout_FR": {
        "CommandPoints": 25,
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
    
    "LRRP_FR": {
        "CommandPoints": 60,
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
    
    "VBL_Reco_FR": {
        "CommandPoints": 15,
        "availability": [10, 7, 0, 0],
    },
    
    "VBL_MILAN_FR": {
        "CommandPoints": 65,
        "availability": [0, 4, 3, 0],
    },
    
    "Alouette_III_FR": {
        "CommandPoints": 35,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    
    "AMX_10_RC_FR": {
        "CommandPoints": 135,
        "availability": [0, 4, 3, 0],
    },
    
    "AMX_10_RCR_FR": {
        "CommandPoints": 165,
        "availability": [0, 0, 3, 2],
    },
    # FR AA
    "TRM_2000_20mm_FR": {
        "CommandPoints": 35,
        "availability": [9, 7, 0, 0],
    },
    
    "MANPAD_Mistral_FR": {
        "CommandPoints": 55,
        "availability": [6, 4, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_FAMAS", "FM_FAMAS_noreflex")],
            },
        },
    },
    
    "AMX_13_DCA_FR": {
        "CommandPoints": 60,
        "availability": [6, 4, 0, 0],
    },
    
    "Roland_2_FR": {
        "CommandPoints": 120,
        "optics": {
            "OpticalStrengthAltitude": 220,
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
            "OpticalStrengthAltitude": 300,
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
    # FR HELICOPTER
    "Super_Puma_FR": {
        "CommandPoints": 50,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    
    "Gazelle_20mm_FR": {
        "availability": [0, 8, 6, 0],
    },
    
    "Gazelle_HOT_FR": {
        "CommandPoints": 70,   
        "availability": [0, 6, 4, 0],
    },
    
    "Gazelle_HOT_2_FR": {
        "CommandPoints": 85,
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
    
    "Jaguar_HE_FR": {
        "CommandPoints": 200,
        "availability": [0, 2, 0, 1],
    },
    
    "Jaguar_ATGM_FR": {
        "CommandPoints": 150,
        "availability": [0, 3, 2, 0],
    },
    
    "Jaguar_SEAD_FR": {
        "CommandPoints": 150,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "FR_5e_Blindee": {
                "cards": 2,
            },
        },
        "availability": [0, 2, 0, 1],
    },
    
    "Mirage_III_E_FR": {
        "CommandPoints": 115,
        "strength": 10,
        "availability": [0, 4, 3, 2],
    },
    
    "Mirage_F1_C_FR": {
        "CommandPoints": 150,
        "availability": [0, 3, 2, 0],
    },
}
