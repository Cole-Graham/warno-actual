"""RDA unit edits."""

# from typing import Any, Dict

# fmt: off
rda_unit_edits = {
    # RDA LOG
    "UAZ_469_CMD_DDR": {
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
        "availability": [0, 4, 0, 0],
    },
    
    "PT76B_CMD_DDR": { # Too inexpensive to make a LDR., just changing to a CV
        "CommandPoints": 170,
        "Factory": "EFactory/Logistic",
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 3, 0],
    },
    
    "BMP_1_CMD_DDR": {
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
    },

    "BRDM_2_CMD_DDR": {
        "strength": 8,
        "CommandPoints": 155,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 3, 0, 0],
    },

    "BTR_60_CMD_DDR": {
        "CommandPoints": 175,
        "strength": 10,
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
    },
    
    "BTR_60_CHAIKA_CMD_DDR": {
        "CommandPoints": 155,
        "strength": 10,
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
    },

    # RDA INF
    "MotRifles_CMD_DDR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV MOT.-SCHUTZEN LDR.",
            "token": "LJDWEYDMZI",
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
                "UNITE_MotRifles_CMD_DDR",
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
            "RDA_7_Panzer": {
                "Transports": [
                    "W50_LA_A_DDR",
                    "BTR_70_DDR",
                    "BMP_1_SP1_DDR",
                    "BMP_1_SP2_DDR",
                    "BMP_1P_DDR",
                ],
            },
        },
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_Mpi_AK_74N": 5,
                },
            },
            "Salves": {
                "RocketInf_RPG18_64mm": 6,
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "remove_zone_capture": None,
    },

    "Engineers_CMD_DDR": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV PIONIER LDR.",
            "token": "KYSSUXXTDG",
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
                "UNITE_Engineers_CMD_DDR",
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
                '_resolute',
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
                    "FM_Mpi_AK_74N": 8,
                },
            },
            "Salves": {
                "FM_Mpi_AK_74N": 11,
                "RocketInf_RPG7VL": 6,
            },
        },
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "remove_zone_capture": None,
    },

    "MP_DDR": {
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "availability": [0, 12, 9, 0],
        "max_speed": 26,
        "strength": 5,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_Skorpion": 5,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "KdA_CMD_DDR": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV K.d.A. FÜH. LDR.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_KdA_CMD_DDR",
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
                '_reservist',
                '_militia',
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
        "availability": [0, 7, 0, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_KMS_72": 5,
                },
                "insert": [(1, "SAW_lMG_K_7_62mm")],
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "SalvoStockIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "NbWeapons": 1,
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                },
            },
            "Salves": {
                "insert": [(1, 15)],
            },
        },
        "remove_zone_capture": None,
    },
    
    "Reserve_CMD_DDR": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV RESERVISTEN FÜH. LDR.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Reserve_CMD_DDR",
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
        "availability": [0, 7, 5, 0],
        "max_speed": 20,
        "remove_zone_capture": None,
    },
    
    "Reserve_DDR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Reserve_HMG_DDR": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Security_DDR": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "HMGteam_AGS17_DDR": {
        "CommandPoints": "HMGteam_AGS17_SOV",
        "GameName": {
            "display": "Gr-MG 30mm",
        },
        "strength": "HMGteam_AGS17_SOV",
        "max_speed": "HMGteam_AGS17_SOV",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "RDA_KdA_Bezirk_Erfurt": {
                "cards": 1,
            },
        },
        "availability": [0, 9, 7, 0],
        "SpecialtiesList": {
            "add_specs": "HMGteam_AGS17_SOV",
        },
    },
    
    "KdA_DDR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "max_speed": 26,
        "availability": [12, 0, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_lMG_K_7_62mm": False,
                },
                "quantity": {
                    "FM_KMS_72": 12,
                    "SAW_lMG_K_7_62mm": 2,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "MotRifles_DDR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "RDA_4_MSD": {
                "cards": 2,
            },
            "RDA_7_Panzer": {
                "cards": 4,
            },
            "RDA_9_Panzer": {
                "cards": 4,
            },
            "SOV_6IndMSBrig": {
                "cards": 1,
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_Mpi_AK_74N": 11,
                "RocketInf_RPG7VL": 4,
            },
        },
    },

    "MotRifles_SVD_DDR": {
        "GameName": {
            "display": "MOT.-SCHÜTZEN [SVD]",
        },
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
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
    },

    "MotRifles_BTR_DDR": {
        "GameName": {
            "display": "MOT.-SCHÜTZEN [BTR]",
        },
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "RDA_4_MSD": {
                "cards": 3,
            },
            "RDA_Rugen_Gruppierung": {
                "cards": 3,
            },
            "WP_Unternehmen_Zentrum": {
                "cards": 3,
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_Mpi_AK_74N": 11,
                "RocketInf_RPG7VL": 6,
            },
        },
    },

    "MotSchutzen_DDR": {  # Panzerjager 2x RPG-7VR
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_Mpi_AK_74N": 11,
                "RocketInf_RPG7VR_64mm": 4,
            },
        },
    },
    
    "MotRifles_RPG27_DDR": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_Mpi_AK_74N": 11,
                "RocketInf_RPG27_105mm": 4,
            },
        },
    },

    "Engineers_DDR": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
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
            "equipmentchanges": {
                "animate": {
                    "MMG_PKM_7_62mm": False,
                },
                "quantity": {
                    "MMG_PKM_7_62mm": 2,
                },
            },
            "Salves": {
                "Grenade_Satchel_Charge": 6,
            },
        },
    },

    "Engineers_Flam_DDR": {
        "GameName": {
            "display": "PIONIER [FLAM]",
        },
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
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
                "FM_Mpi_AK_74N": 11,
            },
        },
    },

    "HMGteam_PKM_DDR": {
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

    "HMGteam_PKM_FJ_DDR": {
        "CommandPoints": "HMGteam_M60_AB_US",
        "GameName": {
            "display": "Fs-PKM 7.62mm",
        },
        "strength": "HMGteam_M60_AB_US",
        "max_speed": "HMGteam_M60_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_AB_US",
        },
    },
    
    "HMGteam_NSV_DDR": {
        "CommandPoints": "HMGteam_M2HB_US",
        "strength": "HMGteam_M2HB_US",
        "max_speed": "HMGteam_M2HB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_US",
        },
    },

    "UAZ_469_SPG9_DDR": {
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [12, 9, 0, 0],
    },
    
    "ATteam_RCL_SPG9_DDR": {
        "strength": 5,
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "ATteam_Fagot_DDR": {
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [9, 7, 5, 0],
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

    "ATteam_Konkurs_DDR": {
        "CommandPoints": 45,
        "availability": [6, 4, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "ATteam_FagotM_DDR",
    },

    "UAZ_469_trans_DDR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "GAZ_46_DDR": { # Advanced Schwimming Technologia
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "W50_LA_A_DDR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "M35_trans_DDR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "T813_trans_DDR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    # RDA ARTILLERY
    "BTR_50_CMD_DDR": {
        "CommandPoints": 60,
        "GameName": {
            "display": "#LDRSOV SPW-50PU(A)",
            "token": "MXTHDKLGFB",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_BTR_50_CMD_DDR",
                "Unite",
                "Vehicule",
            ],
        },
        "Factory": "EFactory/Art",
        "IdentifiedTextures": ["Texture_RTS_H_appui", "Texture_appui"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "leader_sov",
        "SpecialtiesList": {
            "overwrite_all": [
                '_amphibie',
                '_resolute',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_appui",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Transport",
        "Divisions": {
            "add": ["RDA_9_Panzer"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 0, 0],
        "remove_zone_capture": None,
    },
    
    "Mortier_M43_82mm_DDR": {
        "CommandPoints": 30,
        "availability": [5, 4, 3, 0],
    },

    "Mortier_PM43_120mm_DDR": {
        "CommandPoints": 45,
        "availability": [5, 4, 3, 0],
    },
    
    "Howz_M46_130mm_DDR": {
        "CommandPoints": 100,
        "availability": [4, 3, 2, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },
    
    "Howz_D20_152mm_DDR": {
        "CommandPoints": 95,
        "availability": [3, 2, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },
    
    "Howz_D30_122mm_DDR": {
        "CommandPoints": "Howz_D30_122mm_SOV",
        "availability": "Howz_D30_122mm_SOV",
        "Divisions": {
            "default": "Howz_D30_122mm_SOV"
        },
    },

    "2S1_DDR": {
        "GameName": {
            "display": "SFL-H 2S1",
        },
        "CommandPoints": 110,
        "availability": [3, 2, 0, 0],
    },

    "2S3_DDR": {
        "GameName": {
            "display": "SFL-H 2S3M",
        },
        "CommandPoints": 180,
        "availability": [3, 2, 0, 0],
    },

    "MFRW_RM70_DDR": {
        "CommandPoints": 240,
        "availability": [2, 0, 1, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketArt_M21OF_122mm", "RocketArt_M21OF_122mm_RM70")],
            },
        },
    },
    
    "RM70_85_DDR": { # [NPLM] 80 Salvo Length
        "CommandPoints": 155,
        "GameName": {
            "display": "MFRW RM-70M [INCD]",
        },
        "availability": [2, 0, 1, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketArt_M21OF_122mm_napalm", "RocketArt_M21OF_122mm_RM70_napalm")],
            },
        },
    },
    
    "BM21_Grad_DDR": { # BM-21 [NPLM]
        "CommandPoints": 110,
        "GameName": {
            "display": "MFRW BM-21 [INCD]",
        },
        "availability": [3, 2, 0, 0],
    },
    
    "BM24M_DDR": {
        "CommandPoints": 240,
        "availability": [2, 0, 1, 0],
    },

    # RDA TANK
    
    "T54B_CMD_DDR": {
        "CommandPoints": 75,
        "GameName": {
            "display": "#LDRSOV FüPz T-54AMK LDR.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_Standard",
                "GroundUnits",
                "UNITE_T54B_CMD_DDR",
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
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 6, 0],
        "remove_zone_capture": None,
    },
    
    "T55A_CMD_DDR": {
        "CommandPoints": 80,
        "GameName": {
            "display": "#LDRSOV FüPz T-55AK LDR.",
            "token": "VKLRXNSTQE",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T55A_CMD_DDR",
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
                # '_smoke_launcher',  # do not smoke
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 6, 0],
        "remove_zone_capture": None,
    },

    "T72M_CMD_DDR": {
        "CommandPoints": 170,
        "GameName": {
            "display": "#LDRSOV FüPz T-72M LDR.",
            "token": "XVEZUMJKLL",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T72M_CMD_DDR",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_resolute',
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
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },

    "T72M1_CMD_DDR": {  # FüPz T-72M1K LDR
        "CommandPoints": 190,
        "GameName": {
            "display": "#LDRSOV FüPz T-72M1K LDR.",
            "token": "FUPZTSTMOL",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T72M1_CMD_DDR",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_resolute',
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
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },
    
    "AT_D44_85mm_DDR": {  # D-44 AT 85mm
        "CommandPoints": 35,
        "availability": [9, 7, 5, 0],
    },
    
    "AT_T12_Rapira_DDR": { 
        "CommandPoints": "AT_T12_Rapira_SOV",
        "availability": "AT_T12_Rapira_SOV",
    },

    "MTLB_trans_DDR": {
        "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "BTR_50_DDR": {
        "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "SPW_152K_DDR": {
        "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "BMP_1_SP1_DDR": {
        "CommandPoints": 20,
    },

    "BMP_1_SP2_DDR": {
        "CommandPoints": 25,
    },

    "BMP_1P_DDR": {
        "CommandPoints": 35,
    },
    
    "BMP_1P_Konkurs_DDR": {
        "CommandPoints": 45,
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9M113_Konkurs_BMP2": 6,
            },
        },      
    },
    
    "BMP_2_DDR": {
        "CommandPoints": 65, # Vanilla price
    },

    "BTR_60_DDR": {
        "CommandPoints": 20,
        "strength": 10,
    },

    "BTR_70_DDR": {
        "CommandPoints": 25,
        "strength": 10,
    },

    "UAZ_469_Fagot_DDR": {
        "CommandPoints": 35,
        "GameName": {
            "display": "UAZ-469 FAGOT-M",
            "token": "KBMDYNGBOG",
        },
        "availability": [10, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": 6,
            },
        },
    },
    
    "BRDM_Malyu_P_DDR": {  # BRDM-2 Malutka-P
        "CommandPoints": "BRDM_2_Malyu_P_POL",
        "strength": "BRDM_2_Malyu_P_POL",
        "stealth": "BRDM_2_Malyu_P_POL",
        "availability": "BRDM_2_Malyu_P_POL",
    },

    "BRDM_Konkurs_DDR": {
        "strength": 8,
        "CommandPoints": 50,
        "stealth": 1.5,
        "availability": [8, 6, 0, 0],
    },
    
    "MTLB_Shturm_DDR": {
        "CommandPoints": 60,
        "availability": [8, 6, 0, 0],
    },
    
    "PT76B_tank_DDR": {
        "CommandPoints": 20,
        "availability": [14, 0, 0, 0],
    },
    
    "T34_85M_DDR": {
        "armor": {
            "front": (4, None),
            "sides": (2, None),
            "rear": (1, None),
        },
        "availability": [12, 0, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Canon_AP_85mm_S53", "Canon_HEAT2_85mm_S53")],
            },
        },
    },
    
    "T54B_DDR": {
        "CommandPoints": 65,
        "availability": [10, 7, 0, 0],
    },

    "T55A_DDR": {
        "GameName": {
            "display": "KPz T-55A",
        },
        "CommandPoints": 70,
        "availability": [10, 7, 0, 0],
    },

    "T72_DDR": {
        "GameName": {
            "display": "KPz T-72",
        },
        "CommandPoints": 100,
        "availability": [8, 6, 0, 0],
    },

    "T72M_DDR": {
        "GameName": {
            "display": "KPz T-72M",
        },
        "CommandPoints": 150,
        "availability": [0, 6, 4, 0],
    },
    
    "T72MUV2_DDR": {
        "CommandPoints": 155,
        "availability": [6, 4, 0, 0],
    },

    "T72M1_DDR": {
        "GameName": {
            "display": "KPz T-72M1",
        },
        "CommandPoints": 170,
        "Divisions": {
            "remove": ["RDA_7_Panzer"],
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 5, 3, 0],
    },
    
    "T72S_DDR": {
        "CommandPoints": 235,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 0, 4, 3],
    },

    # RDA RECON
    "UAZ_469_Reco_DDR": {
        "CommandPoints": 25,
    },

    "BRDM_2_DDR": {
        "strength": 8,
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [8, 6, 0, 0],
    },

    "BMP_1P_reco_DDR": {
        "GameName": {
            "display": "#RECO1 AufKl BMP-1P",
        },
        "CommandPoints": 35,
    },

    "BRM_1_DDR": {
        "GameName": {
            "display": "#RECO3 AufKl BRM-1K",
        },
        "CommandPoints": 55,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "RDA_4_MSD": {
                "cards": 1,
            },
            "WP_Unternehmen_Zentrum": {
                "cards": 1,
            },
        },
        "availability": [6, 4, 0, 0],
    },
    
    "PT76B_DDR": {
        "CommandPoints": 30,
        "availability": [8, 6, 0, 0],
    },

    "Mi_2_reco_DDR": {
        "availability": [0, 6, 0, 0],
    },
    
    "Mi_2_gunship_DDR": {
        "CommandPoints": 35,
        "availability": [0, 6, 4, 0],
    },
    
    "Mi_8PPA_SOV": {
        "availability": [0, 3, 0, 0],
    },

    "Scout_DDR": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "RDA_Rugen_Gruppierung": {
                "cards": 1,
            },
        },
        "availability": [8, 6, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },
    
    "Scout_KdA_DDR": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [8, 0, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_lMG_K_7_62mm": False,
                },
                "quantity": {
                    "FM_KMS_72": 4,
                    "SAW_lMG_K_7_62mm": 2,
                },
            },
        },
    },

    "HvyScout_DDR": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "availability": [6, 4, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Scout_LRRP_DDR": {
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    # RDA AA
    "MANPAD_Strela_2M_DDR": {
        "GameName": {
            "display": "Fla-RAK STRELA-2M",
        },
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [12, 9, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_Mpi_AK_74N", "FM_Mpi_AK_74N_noreflex")],
            },
            "Salves": {
                "FM_Mpi_AK_74N_noreflex": 11,
            },
        },
    },

    "MANPAD_Igla_DDR": {
        "GameName": {
            "display": "Fla-RAK IGLA",
        },
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [7, 5, 0, 0],
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
    
    "DCA_ZPU4_DDR": {
        "CommandPoints": 20,
        "availability": [12, 9, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },

    "DCA_ZU_23_2_DDR": {
        "GameName": {
            "display": "FlaK ZU-23-2 23mm",
        },
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "Transports": ["MTLB_trans_DDR"],
                "cards": 1,
            },
        },
        "Factory": "EFactory/Logistic",
        "availability": [9, 7, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "FOB_DDR",
    },
    
    "ZSU_57_2_DDR": {
        "CommandPoints": 60,
        "availability": [7, 0, 0, 0],
    },

    "BRDM_Strela_1_DDR": {
        "GameName": {
            "display": "Fla-RAK STRELA-1",
        },
        "strength": 8,
        "CommandPoints": 50,
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
        "availability": [6, 4, 0, 0],
    },

    "MTLB_Strela10_DDR": {
        "GameName": {
            "display": "Fla-RAK STRELA-10M",
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 220,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
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

    "ZSU_23_Shilka_DDR": {
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 220,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "CommandPoints": 85,
        "availability": [6, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },
    
    "Osa_9K33M3_DDR": {
        "CommandPoints": "Osa_9K33M3_POL",
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 300,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "availability": "Osa_9K33M3_POL",
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    "2K12_KUB_DDR": {
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 300,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "CommandPoints": 90,
        "availability": [4, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    # RDA HELI
    "Mi_2_trans_DDR": {
        "CommandPoints": 35,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Mi_2_rocket_DDR": {
        "CommandPoints": 50,
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_23mm_NS23": 25,
                "RocketAir_S5_57mm_salvolength32": 1,
            },
        },
    },

    "Mi_8T_non_arme_DDR": {
        "CommandPoints": 50,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Mi_8T_DDR": {  # 32 S-5M x2
        "CommandPoints": 50,
    },

    "Mi_8TV_DDR": {  # [RKT 1]
        "GameName": {
            "display": "Mi-8TV [RKT]",
        },
        "CommandPoints": 70,
        "availability": [0, 6, 4, 0],
    },

    "Mi_8TV_s57_32_DDR": {  # [RKT 2]
        "GameName": {
            "display": "Mi-8TV [RKT2]",
        },
        "CommandPoints": "Mi_8TV_s57_32_SOV",
        "availability": "Mi_8TV_s57_32_SOV",
    },

    "Mi_8TV_UPK_DDR": {
        "CommandPoints": 85,
        "availability": [0, 6, 4, 0],
    },
    
    "Mi_8TB_DDR": { # 12.7mm Afanasyev, 2x 64x S-5m, 6x Malyutka-M
        "CommandPoints": 85,
        "availability": [0, 6, 4, 0],
    },

    "Mi_24D_s5_AT_DDR": {
        "CommandPoints": 135,
        "availability": [0, 4, 3, 0],
    },

    "Mi_24P_s8_AT_DDR": {
        "GameName": {
            "display": "Mi-24P [AT]",
        },
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "RDA_7_Panzer": {
                "cards": 2,
            },
        },
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
        "availability": [0, 3, 2, 0],
    },
    
    "Mi_24P_s8_AT2_DDR": {
        "CommandPoints": 175,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
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
        "availability": [0, 3, 2, 0],
    },

    # RDA AIR
    "MiG_21PFM_AA_DDR": {
        "CommandPoints": 95,
        "availability": [0, 4, 3, 2],
    },

    "MiG_21bis_AA2_DDR": {
        "CommandPoints": 110,
        "availability": [0, 4, 3, 2],
    },

    "MiG_21PFM_DDR": {  # [RKT1]
        "GameName": {
            "display": "MiG-21bis [RKT]",
        },
        "CommandPoints": 100,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketAir_S5_57mm_salvolength32", "RocketAir_S5_57mm_avion_salvolength32")],
            },
        },
        "availability": [0, 4, 0, 0],
    },

    "MiG_21bis_HE_DDR": {
        "CommandPoints": 135,
        "availability": [0, 4, 0, 0],
    },

    "MiG_21bis_RKT2_DDR": {  # 4x S-24 [RKT2]
        "CommandPoints": 100,
        "availability": [0, 4, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketAir_S24_240mm_avion_salvolength4": (1, True),
            },
            "equipmentchanges": {
                "replace": [("RocketAir_S24_240mm_salvolength2", "RocketAir_S24_240mm_avion_salvolength4")],
            },
        },
    },

    "MiG_23BN_AT_DDR": {  # MiG-23MF [AT]
        "CommandPoints": 125,
        "availability": [0, 3, 0, 0],
    },

    "MiG_23BN_RKT_DDR": {  # MiG-23MF [AT]
        "WeaponDescriptor": {
            "Salves": {
                "RocketAir_S24_240mm_avion_salvolength4": 1,
            },
            "equipmentchanges": {
                "replace": [("RocketAir_S24_240mm_salvolength2", "RocketAir_S24_240mm_avion_salvolength4")],
            },
        },
    },

    "MiG_23MF_DDR": {  # [HE]
        "CommandPoints": 220,
        "availability": [0, 3, 0, 0],
    },
    
    "MiG_23MF_AA_DDR": {
        "CommandPoints": 115,
        "availability": [0, 4, 3, 2],
        "ECM": -0.1,
    },

    "MiG_23ML_DDR": {  # [AA]
        "CommandPoints": 145,
        "availability": [0, 3, 2, 0],
        "ECM": -0.2,
    },

    "MiG_29_AA_DDR": {  # 4x R-73, 2x R-27R [AA1]
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "Su_22_AT_DDR": {
        "CommandPoints": "Su_22_AT_SOV",
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_Kh29T": 1,
            },
        },
    },

    "Su_22_SEAD_DDR": { # Kh-28 5425m
        "CommandPoints": 195,
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
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
        "Divisions": {
            "add": ["RDA_9_Panzer"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 1,
            },
        },
    },

    "Su_22_clu_DDR": {
        "CommandPoints": 215,
        "availability": [0, 2, 0, 0],
    },

    "Su_22_nplm_DDR": {
        "CommandPoints": 215,
        "availability": [0, 3, 0, 0],
    },

    "Su_22_DDR": {  # [HE]
        "CommandPoints": 215,
        "availability": [0, 2, 0, 0],
    },

    "Su_22_RKT_DDR": {  # 4x S-24
        "CommandPoints": 125,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketAir_S24_240mm_avion_salvolength4": 1,
            },
            "equipmentchanges": {
                "replace": [("RocketAir_S24_240mm_salvolength2", "RocketAir_S24_240mm_avion_salvolength4")],
            },
        },
    },
}
