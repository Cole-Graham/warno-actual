"""RDA unit edits."""

from typing import Any, Dict

# fmt: off
rda_unit_edits = {
    #RDA LOG
    "BMP_1_CMD_DDR": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "BRDM_2_CMD_DDR": {
        "Strength": 8,
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "BTR_60_CMD_DDR": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },
    #RDA INF
    "MP_DDR": {
        "CommandPoints": 15,
        "availability": 12,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Security_DDR": {
        "CommandPoints": 30,
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "HMGteam_AGS17_DDR": {
        "Strength": 5,
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
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
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
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
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
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "MotRifles_BTR_DDR": {
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
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
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

    "MotSchutzen_DDR": { # Panzerjager 2x RPG-7VR
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
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
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Engineers_Flam_DDR": {
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
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

    "UAZ_469_SPG9_DDR": {
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "ATteam_Fagot_DDR": {
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 9,
        "XPMultiplier": [1.0, 0.8, 0.6, 0.0],
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
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "ATteam_FagotM_DDR",
    },

    "UAZ_469_trans_DDR": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "W50_LA_A_DDR": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M35_trans_DDR": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "T813_trans_DDR": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    #RDA ARTILLERY
    "Mortier_PM43_120mm_DDR": {
        "CommandPoints": 40,
        "availability": 5,
        "XPMultiplier": [1.0, 0.8, 0.6, 0.0],
    },

    "2S1_DDR": {
        "CommandPoints": 100,
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "2S3_DDR": {
        "CommandPoints": 165,
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "MFRW_RM70_DDR": {
        "CommandPoints": 220,
        "XPMultiplier": [1.0, 0.0, 0.5, 0.0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketArt_M21OF_122mm", "RocketArt_M21OF_122mm_RM70")],
            },
        },
    },
    #RDA TANK
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
        "CommandPoints": 55,
        "GameName": {
            "game_n": "UAZ-469 FAKTORIYA",
            "nametoken": "KBMDYNGBOG",
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": 6,
            },
        },
    },

    "BRDM_Konkurs_DDR": {
        "Strength": 8,
        "CommandPoints": 50,
        "stealth": 1.5,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "T55A_DDR": {
        "CommandPoints": 70,
        "availability": 10,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "T72_DDR": {
        "CommandPoints": 100,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "T72M_DDR": {
        "CommandPoints": 145,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "T72M1_DDR": {
        "CommandPoints": 170,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
    },
    #RDA RECON
    "UAZ_469_Reco_DDR": {
        "CommandPoints": 25,
    },

    "BRDM_2_DDR": {
        "Strength": 8,
        "CommandPoints": 35,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "BMP_1P_reco_DDR": {
        "CommandPoints": 25,
    },

    "BRM_1_DDR": {
        "CommandPoints": 60,
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
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "Mi_2_reco_DDR": {
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
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
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "HvyScout_DDR": {
        "CommandPoints": 30,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "DeploymentShift": 0,
    },

    "Scout_LRRP_DDR": {
        "CommandPoints": 60,
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    #RDA AA
    "MANPAD_Strela_2M_DDR": {
        "CommandPoints": 20,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "MANPAD_Igla_DDR": {
        "CommandPoints": 35,
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "DCA_ZU_23_2_DDR": {
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "category": "Logistic",
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 4,
    },

    "BRDM_Strela_1_DDR": {
        "Strength": 8,
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "MTLB_Strela10_DDR": {
        "optics": {
            "OpticalStrengthAltitude": 225,
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

    "ZSU_23_Shilka_DDR": {
        "optics": {
            "OpticalStrengthAltitude": 225,
        },
        "CommandPoints": 75,
        "availability": 6,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "2K12_KUB_DDR": {
        "optics": {
            "OpticalStrengthAltitude": 285,
        },
        "CommandPoints": 90,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },
    #RDA HELI
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
    
    "Mi_8T_DDR": { # 32 S-5M x2
        "CommandPoints": 50,
    },

    "Mi_8TV_DDR": { # [RKT 1]
        "CommandPoints": 70,
        "availability": 6,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Mi_8TV_s57_32_DDR": { # [RKT 2]
        "CommandPoints": 85,
        "availability": 6,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Mi_8TV_UPK_DDR": {
        "CommandPoints": 85,
        "availability": 6,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Mi_24D_s5_AT_DDR": {
        "CommandPoints": 135,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "Mi_24P_s8_AT_DDR": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "RDA_7_Panzer": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },
    #RDA AIR
    "MiG_21PFM_AA_DDR": {
        "CommandPoints": 100,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.5],
    },

    "MiG_21bis_AA2_DDR": {
        "CommandPoints": 120,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.5],
    },

    "MiG_21PFM_DDR": { # [RKT1]
        "CommandPoints": 100,
        "availability": 4,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace_fixedsalvo": [("RocketAir_S5_57mm_x32", "RocketAir_S5_57mm_salvolength32_avion")],
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "MiG_21bis_HE_DDR": {
        "CommandPoints": 135,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "MiG_23MF_DDR": { # [HE]
        "CommandPoints": 220,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "MiG_23BN_AT_DDR": { # MiG-23MF [AT]
        "CommandPoints": 125,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "MiG_23ML_DDR": { # [AA]
        "CommandPoints": 135,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Su_22_AT_DDR": {
        "CommandPoints": 180,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "Su_22_SEAD_DDR": {
        "CommandPoints": 195,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },

    "Su_22_clu_DDR": {
        "CommandPoints": 215,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "Su_22_nplm_DDR": {
        "CommandPoints": 215,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "Su_22_DDR": { # [HE]
        "CommandPoints": 215,
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

}
