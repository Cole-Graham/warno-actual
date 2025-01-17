"""Polish unit edits."""

from typing import Any, Dict

# fmt: off
pol_unit_edits = {
    #POL LOG
    "DCA_ZU_23_2_POL": {
        "CommandPoints": 20,
        "category": "Logistic",
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "POL_4_Zmechanizowana": {
                "cards": 2,
            },
            "POL_20_Pancerna": {
                "cards": 1,
            },
        },
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 4,
    },

    "DCA_ZUR_23_2S_JOD_POL": {
        "CommandPoints": 30,
        "category": "Logistic",
        # "Divisions": {
        #     "default": {
        #         "cards": 69,
        #     },
        #     "POL_4_Zmechanizowana": {
        #         "cards": 2,
        #     },
        #     "POL_20_Pancerna": {
        #         "cards": 1,
        #     },
        # },
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 4,
    },

    "BMP_1_CMD_POL": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "BRDM_2_CMD_POL": {
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

    "BRDM_2_CMD_R5_POL": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },


    #POL INFANTRY
    "Engineers_Flam_POL": {  # Saperzy Szturmowi
        "CommandPoints": 50,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        # 8x Kbk AKM
        # 1x PKM
        # RPO Rys x6
    },

    "Engineers_POL": {
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        # 8x Kbk AKM
        # 1x PKM
        # Satchel
        # RPG-76 Komar x4
    },

    "Groupe_AT_POL": {  # Druzyna PPanc 2x RPG-7VL
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        # 7x Kbk AKM
        # 2x RPG-7VL x6 (panzerjager with VL instead of VR)
    },

    "MotRifles_POL": {  # Piechota Zmech
        "CommandPoints": 30,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        # 6x Kbk AK(M?)
        # 1x PKM
        # RPG-7VM x6
    },

    "MotRifles_SVD_POL": {  # Piechota Zmech (SVD)
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
            "add_specs": ["'infantry_equip_medium'"],
        },
        # 4x Kbk AKM
        # 2x PKM
        # 1x SVD
        # RPG-7VM x6
    },

    "WSW_POL": {
        "CommandPoints": 35,
        "availability": 8,
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
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "FM_AK_74": 11,
        #     },
        # },
    },

    #  infantry tab transports
    "Star_266_POL": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "UAZ_469_trans_POL": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "Honker_4011_POL": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "GAZ_66_POL": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "GAZ_66B_POL": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "BAV_485_POL": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    #POL ARTILLERY
    "Mortier_PM43_120mm_POL": {
        "CommandPoints": 40,
        "availability": 5,
        "XPMultiplier": [1.0, 0.8, 0.6, 0.0],
    },

    "Mortier_2B9_Vasilek_Para_POL": {  # Desant. 2B9 Wasilok
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

    "BM21_Grad_POL": {
        "CommandPoints": 175,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "2S1_POL": {
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    # POL TANK
    "BRDM_2_Konkurs_POL": {
        "Strength": 8,
        "CommandPoints": 50,
        "stealth": 1.5,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "T55A_POL": {
        "CommandPoints": 70,
        "availability": 10,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "T55AS_POL": {  # coffin launcher
        "CommandPoints": 420,
        # FUCK this guy in particular
    },

    "T72M_POL": {
        "CommandPoints": 145,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "T72M1_POL": {
        "CommandPoints": 170,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
    },

    "T72M1_Wilk_POL": {
        "CommandPoints": 170,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
    },

    #   tank tab transports

    "OT_64_SKOT_2_POL": {
        "CommandPoints": 20,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "OT_64_SKOT_2A_POL": {
        "CommandPoints": 25,
    },

    "BMP_1_SP2_POL": {  # BWP-1
        "CommandPoints": 20,
    },

    "BMP_2_POL": {  # BWP-2
        "CommandPoints": 50,
    },

    # POL RECON

    "HvyScout_POL": {  # Zmot Zwiad -> Zwiadowcy Zmot
        "CommandPoints": 40,
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "DeploymentShift": 0,
    },

    "Engineers_Scout_POL": {  # Saperzy Zwiadowcy
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

    "BRM_1_POL": {
        "CommandPoints": 60,
        "cards": {
            "default": 2,
        },
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    #   recon tab transports

    "BMP_1_SP2_reco_POL": {
        "CommandPoints": 25,
    },

    "Honker_RYS_POL": {
        "CommandPoints": 25,
    },

    # POL AA
    "MANPAD_Strela_2M_POL": {
        "CommandPoints": 20,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "MTLB_Strela10_POL": {
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

    "ZSU_23_Shilka_POL": {
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

    "2K12_KUB_POL": {
        "optics": {
            "OpticalStrengthAltitude": 285,
        },
        "CommandPoints": 90,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    # POL HELI

    # POL AIR

    "MiG_21bis_POL": {  # MiG-21bis AA2
        "CommandPoints": 120,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.5],
    },

    "MiG_21bis_HE_POL": {
        "CommandPoints": 135,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "Su_22_AT_POL": {  # Su-22M4 Seria 30
        "CommandPoints": 180,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "Su_22_SEAD_POL": {
        "CommandPoints": 195,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },

}
