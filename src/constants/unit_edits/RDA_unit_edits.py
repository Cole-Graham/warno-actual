"""RDA unit edits."""

from typing import Any, Dict

# fmt: off
rda_unit_edits = {
    # RDA LOG
    "BMP_1_CMD_DDR": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 2/2, 0.0],
    },

    "BRDM_2_CMD_DDR": {
        "strength": 8,
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 3/3, 0.0, 0.0],
    },

    "BTR_60_CMD_DDR": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 0.0, 3/3, 0.0],
    },

    "MTLB_supply_DDR": {
        "GameName": {
            "display": "MT-LB MUN.",
        },
    },

    # RDA INF
    "MotRifles_CMD_DDR": {
        "CommandPoints": 40,
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
        "availability": 7,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 7/7, 5/7],
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
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },

    "Engineers_CMD_DDR": {
        "CommandPoints": 50,
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
                '_resolute',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": 7,
        "XPMultiplier": [0.0, 0.0, 7/7, 5/7],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_Mpi_AK_74N": 8,
                },
            },
            "Salves": {
                "FM_Mpi_AK_74N": 9,
                "RocketInf_RPG7VL": 6,
            },
        },
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },
    
    "MP_DDR": {
        "CommandPoints": 15,
        "availability": 12,
        "XPMultiplier": [0.0, 12/12, 9/12, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Security_DDR": {
        "CommandPoints": 30,
        "availability": 12,
        "XPMultiplier": [12/12, 9/12, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "HMGteam_AGS17_DDR": {
        "strength": 5,
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "RDA_KdA_Bezirk_Erfurt": {
                "cards": 1,
            },
        },
        "availability": 9,
        "XPMultiplier": [0.0, 9/9, 7/9, 0.0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "MotRifles_DDR": {
        "CommandPoints": 40,
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
            "SOV_6IndMSBrig": {
                "cards": 1,
            },
        },
        "availability": 12,
        "XPMultiplier": [12/12, 9/12, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_Mpi_AK_74N": 9,
                "RocketInf_RPG7VL": 4,
            },
        },
    },

    "MotRifles_SVD_DDR": {
        "GameName": {
            "display": "MOT.-SCHÜTZEN [SVD]",
        },
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 12,
        "XPMultiplier": [12/12, 9/12, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "MotRifles_BTR_DDR": {
        "GameName": {
            "display": "MOT.-SCHÜTZEN [BTR]",
        },
        "CommandPoints": 45,
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
        "availability": 12,
        "XPMultiplier": [12/12, 9/12, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_Mpi_AK_74N": 9,
                "RocketInf_RPG7VL": 6,
            },
        },
    },

    "MotSchutzen_DDR": {  # Panzerjager 2x RPG-7VR
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 12,
        "XPMultiplier": [12/12, 9/12, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_Mpi_AK_74N": 9,
                "RocketInf_RPG7VR_64mm": 4,
            },
        },
    },

    "Engineers_DDR": {
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 8,
        "XPMultiplier": [0.0, 8/8, 6/8, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Engineers_Flam_DDR": {
        "GameName": {
            "display": "PIONIER [FLAM]",
        },
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 8,
        "XPMultiplier": [0.0, 8/8, 6/8, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_Mpi_AK_74N": 7,
            },
        },
    },

    "HMGteam_PKM_DDR": {
        "GameName": {
            "display": "PKM 7.62mm",
        },
    },

    "HMGteam_PKM_FJ_DDR": {
        "GameName": {
            "display": "Fs-PKM 7.62mm",
        },
    },

    "UAZ_469_SPG9_DDR": {
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 12,
        "XPMultiplier": [12/12, 9/12, 0.0, 0.0],
    },

    "ATteam_Fagot_DDR": {
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 9,
        "XPMultiplier": [9/9, 7/9, 5/9, 0.0],
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
        "CommandPoints": 50,
        "availability": 6,
        "XPMultiplier": [6/6, 4/6, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "ATteam_FagotM_DDR",
    },

    "UAZ_469_trans_DDR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "W50_LA_A_DDR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M35_trans_DDR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "T813_trans_DDR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
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
        "Factory": "EDefaultFactories/Art",
        "IdentifiedTextures": ["Texture_RTS_H_appui", "Texture_appui"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_amphibie',
                '_resolute',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_appui",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Transport",
        "availability": 2,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 2/2, 0.0, 0.0],
        "remove_zone_capture": None,
    },
    
    "Mortier_PM43_120mm_DDR": {
        "CommandPoints": 40,
        "availability": 5,
        "XPMultiplier": [5/5, 4/5, 3/5, 0.0],
    },

    "2S1_DDR": {
        "GameName": {
            "display": "SFL-H 2S1",
        },
        "CommandPoints": 100,
        "availability": 3,
        "XPMultiplier": [3/3, 2/3, 0.0, 0.0],
    },

    "2S3_DDR": {
        "GameName": {
            "display": "SFL-H 2S3M",
        },
        "CommandPoints": 165,
        "availability": 3,
        "XPMultiplier": [3/3, 2/3, 0.0, 0.0],
    },

    "MFRW_RM70_DDR": {
        "CommandPoints": 220,
        "XPMultiplier": [2/2, 0.0, 1/2, 0.0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketArt_M21OF_122mm", "RocketArt_M21OF_122mm_RM70")],
            },
        },
    },

    # RDA TANK
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
        "SpecialtiesList": {
            "overwrite_all": [
                'armor',
                'leader_sov',
                '_resolute',
                # '_smoke_launcher',  # do not smoke
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": 6,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 6/6, 0.0],
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
        "SpecialtiesList": {
            "overwrite_all": [
                'Armor_heavy',
                'leader_sov',
                '_resolute',
                '_smoke_launcher',
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
        "XPMultiplier": [0.0, 0.0, 4/4, 0.0],
        "remove_zone_capture": None,
    },
    
    "MTLB_trans_DDR": {
        "orders": {
            "add_orders": ["sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "BTR_50_DDR": {
        "orders": {
            "add_orders": ["sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "SPW_152K_DDR": {
        "orders": {
            "add_orders": ["sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
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

    "BTR_60_DDR": {
        "CommandPoints": 20,
    },

    "BTR_70_DDR": {
        "CommandPoints": 25,
    },

    "UAZ_469_Fagot_DDR": {
        "CommandPoints": 35,
        "GameName": {
            "display": "UAZ-469 FAKTORIYA",
            "token": "KBMDYNGBOG",
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": 6,
            },
        },
    },

    "BRDM_Konkurs_DDR": {
        "strength": 8,
        "CommandPoints": 50,
        "stealth": 1.5,
        "availability": 8,
        "XPMultiplier": [8/8, 6/8, 0.0, 0.0],
    },

    "T55A_DDR": {
        "GameName": {
            "display": "KPz T-55A",
        },
        "CommandPoints": 70,
        "availability": 10,
        "XPMultiplier": [10/10, 7/10, 0.0, 0.0],
    },

    "T72_DDR": {
        "GameName": {
            "display": "KPz T-72",
        },
        "CommandPoints": 100,
        "XPMultiplier": [8/8, 6/8, 0.0, 0.0],
    },

    "T72M_DDR": {
        "GameName": {
            "display": "KPz T-72M",
        },
        "CommandPoints": 145,
        "XPMultiplier": [0.0, 7/7, 5/7, 0.0],
    },

    "T72M1_DDR": {
        "GameName": {
            "display": "KPz T-72M1",
        },
        "CommandPoints": 170,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 0.0, 4/4, 3/4],
    },

    # RDA RECON
    "UAZ_469_Reco_DDR": {
        "CommandPoints": 25,
    },

    "BRDM_2_DDR": {
        "strength": 8,
        "CommandPoints": 35,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [8/8, 6/8, 0.0, 0.0],
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
        "availability": 6,
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
        "XPMultiplier": [6/6, 4/6, 0.0, 0.0],
    },

    "Mi_2_reco_DDR": {
        "XPMultiplier": [0.0, 4/4, 0.0, 0.0],
    },

    "Scout_DDR": {
        "CommandPoints": 20,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "RDA_Rugen_Gruppierung": {
                "cards": 1,
            },
        },
        "XPMultiplier": [8/8, 6/8, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },

    "HvyScout_DDR": {
        "CommandPoints": 30,
        "XPMultiplier": [6/6, 4/6, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "DeploymentShift": 0,
    },

    "Scout_LRRP_DDR": {
        "CommandPoints": 70,
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 4/4, 3/4],
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
        "XPMultiplier": [12/12, 9/12, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_Mpi_AK_74N", "FM_Mpi_AK_74N_noreflex")],
            },
        },
    },

    "MANPAD_Igla_DDR": {
        "GameName": {
            "display": "Fla-RAK IGLA",
        },
        "CommandPoints": 35,
        "availability": 7,
        "XPMultiplier": [7/7, 5/7, 0.0, 0.0],
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

    "DCA_ZU_23_2_DDR": {
        "GameName": {
            "display": "FlaK ZU-23-2 23mm",
        },
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "Factory": "EDefaultFactories/Logistic",
        "availability": 9,
        "XPMultiplier": [9/9, 7/9, 0.0, 0.0],
        "max_speed": 4,
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
        "availability": 6,
        "WeaponDescriptor": {
            "Salves": {
                "SAM_Strela1": 2,
            },
        },
        "XPMultiplier": [6/6, 4/6, 0.0, 0.0],
    },

    "MTLB_Strela10_DDR": {
        "GameName": {
            "display": "Fla-RAK STRELA-10M",
        },
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
        "XPMultiplier": [6/6, 4/6, 0.0, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "ZSU_23_Shilka_DDR": {
        "optics": {
            "OpticalStrengthAltitude": 220,
        },
        "CommandPoints": 75,
        "availability": 6,
        "XPMultiplier": [6/6, 4/6, 0.0, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "2K12_KUB_DDR": {
        "optics": {
            "OpticalStrengthAltitude": 300,
        },
        "CommandPoints": 90,
        "XPMultiplier": [4/4, 3/4, 0.0, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    # RDA HELI
    "Mi_2_trans_DDR": {
        "CommandPoints": 35,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    
    "Mi_2_rocket_DDR": {
        "CommandPoints": 50,
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_23mm_NS23": 20,
                "RocketAir_S5_57mm": 1,
            },
        },
    },
    
    "Mi_8T_non_arme_DDR": {
        "CommandPoints": 50,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
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
        "availability": 6,
        "XPMultiplier": [0.0, 6/6, 4/6, 0.0],
    },

    "Mi_8TV_s57_32_DDR": {  # [RKT 2]
        "GameName": {
            "display": "Mi-8TV [RKT2]",
        },
        "CommandPoints": 85,
        "availability": 6,
        "XPMultiplier": [0.0, 6/6, 4/6, 0.0],
    },

    "Mi_8TV_UPK_DDR": {
        "CommandPoints": 85,
        "availability": 6,
        "XPMultiplier": [0.0, 6/6, 4/6, 0.0],
    },

    "Mi_24D_s5_AT_DDR": {
        "CommandPoints": 135,
        "availability": 4,
        "XPMultiplier": [0.0, 4/4, 3/4, 0.0],
    },

    "Mi_24P_s8_AT_DDR": {
        "GameName": {
            "display": "Mi-24P [AT]",
        },
        "CommandPoints": 160,
        "availability": 3,
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
                1: {
                    "MountedWeapons": {
                        "AutoCanon_AP_30mm_Bitube_Gsh30k": {
                            "add_members": [("TirContinu", True),],
                            "Ammunition": "AutoCanon_AP_30mm_Bitube_Gsh30k_burst",
                            "EffectTag": "'FireEffect_GatlingAir_Gsh_30_2_30mm_x2'",
                        },
                        "AutoCanon_HE_30mm_Bitube_Gsh30k": {
                            "add_members": [("TirContinu", True),],
                            "Ammunition": "AutoCanon_HE_30mm_Bitube_Gsh30k_burst",
                            "EffectTag": "'FireEffect_GatlingAir_Gsh_30_2_30mm_x2'",
                        },
                    },
                },
            },
        },
        "XPMultiplier": [0.0, 3/3, 2/3, 0.0],
    },

    # RDA AIR
    "MiG_21PFM_AA_DDR": {
        "CommandPoints": 100,
        "XPMultiplier": [0.0, 4/4, 3/4, 2/4],
    },

    "MiG_21bis_AA2_DDR": {
        "CommandPoints": 120,
        "XPMultiplier": [0.0, 4/4, 3/4, 2/4],
    },

    "MiG_21PFM_DDR": {  # [RKT1]
        "GameName": {
            "display": "MiG-21bis [RKT]",
        },
        "CommandPoints": 100,
        "availability": 4,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketAir_S5_57mm_salvolength32", "RocketAir_S5_57mm_avion_salvolength32")],
            },
        },
        "XPMultiplier": [0.0, 4/4, 0.0, 0.0],
    },

    "MiG_21bis_HE_DDR": {
        "CommandPoints": 135,
        "XPMultiplier": [0.0, 3/3, 0.0, 0.0],
    },

    "MiG_21bis_RKT2_DDR": {  # 4x S-24 [RKT2]
        "CommandPoints": 100,
        "availability": 4,
        "XPMultiplier": [0.0, 4/4, 0.0, 0.0],
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
        "XPMultiplier": [0.0, 3/3, 0.0, 0.0],
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
        "availability": 3,
        "XPMultiplier": [0.0, 3/3, 0.0, 0.0],
    },

    "MiG_23ML_DDR": {  # [AA]
        "CommandPoints": 135,
        "XPMultiplier": [0.0, 3/3, 2/3, 0.0],
    },

    "MiG_29_AA_DDR": {  # 4x R-73, 2x R-27R [AA1]
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 2/2, 0.0, 1/2],
    },

    "Su_22_AT_DDR": {
        "CommandPoints": 180,
        "XPMultiplier": [0.0, 2/2, 0.0, 0.0],
    },

    "Su_22_SEAD_DDR": {
        "CommandPoints": 195,
        "WeaponDescriptor": {
            "turrets": {
                2: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "XPMultiplier": [0.0, 2/2, 0.0, 1/2],
    },

    "Su_22_clu_DDR": {
        "CommandPoints": 215,
        "XPMultiplier": [0.0, 2/2, 0.0, 0.0],
    },

    "Su_22_nplm_DDR": {
        "CommandPoints": 215,
        "availability": 3,
        "XPMultiplier": [0.0, 3/3, 0.0, 0.0],
    },

    "Su_22_DDR": {  # [HE]
        "CommandPoints": 215,
        "availability": 2,
        "XPMultiplier": [0.0, 2/2, 0.0, 0.0],
    },

    "Su_22_RKT_DDR": {  # 4x S-24
        "CommandPoints": 125,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 3/3, 2/3, 0.0],
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
