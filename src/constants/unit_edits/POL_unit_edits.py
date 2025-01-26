"""Polish unit edits."""

# from typing import Any, Dict

# fmt: off
pol_unit_edits = {
    #POL LOG
    "DCA_ZU_23_2_POL": {  # ZU-23-2
        "CommandPoints": 20,
        "Factory": "EDefaultFactories/Logistic",
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
        "availability": 9,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 4,
    },

    "DCA_ZUR_23_2S_JOD_POL": {  # ZUR-23-2S Jod
        "CommandPoints": 30,
        "Factory": "EDefaultFactories/Logistic",
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
        "availability": 6,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
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
        "strength": 8,
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "BRDM_2_CMD_R5_POL": {  # BRDM-2 R-5
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
    "Engineers_CMD_POL": {  # Saperzy Ldr.
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDRSOV SAPERZY LDR.",
            "token": "SAPERZYLDR",
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
                "UNITE_Engineers_CMD_POL",
                "Unite"
            ],
        },
        "strength": 9,
        "WeaponAssignment": [
                (0, [0, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, ]),
                (6, [0, ]),
                (7, [0, ]),
                (8, [0, 1, ]),
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
            "POL_20_Pancerna": {
                "Transports": ["Star_266_POL", "OT_64_SKOT_2_POL"],
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_Kbk_AK", "FM_Kbk_AKM")],
                "quantity": {
                    "FM_Kbk_AKM": 8,
                },
            },
        },
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "selector_tactic": "(0, 9)",
        "selector_tactic_obj": "00_09",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "MotRifles_CMD_POL": {  # Piechota Zmech. Ldr.
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDRSOV PIECHOTA ZMECH. LDR.",
            "token": "PCZMECHLDR",
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
                "UNITE_MotRifles_CMD_POL",
                "Unite",
            ],
        },
        "strength": 7,
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, ]),
                (4, [0, ]),
                (5, [0, 3]),
                (6, [0, 2]),
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
            "POL_20_Pancerna": {
                "Transports": ['Star_266_POL', 'BMP_1_SP2_POL', 'BMP_2_POL'],
            },
        },
        "availability": 7,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPG76_Komar": 7,
            },
        },
        "selector_tactic": "(0, 7)",
        "selector_tactic_obj": "00_07",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "Engineers_POL": {  # Saperzy
        "CommandPoints": 40,
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
        #         "MMG_PKM_7_62mm": 30,
        #         "Grenade_Satchel_Charge": 5,
        #     },
        # },
        # 8x Kbk AKM
        # 1x PKM
        # Satchel
        # RPG-76 Komar x4
    },


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
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "FM_Kbk_AKM": 7,
        #         "MMG_PKM_7_62mm": 30,
        #         "RocketInf_RPO_A_93mm": 4,
        #     },
        # },
        # 8x Kbk AKM
        # 1x PKM
        # RPO Rys x6
    },

    "Groupe_AT_POL": {  # Druzyna PPanc
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
                "cards": 4,
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
                "cards": 2,
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

    "WSW_POL": {  # WSW
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

    "ATteam_RCL_SPG9_Para_POL": {  # Desant. SPG-9
        "Strength": 3,
        "CommandPoints": 30,
        "availability": 10,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "ATteam_RCL_SPG9_POL": {  # SPG-9
        "Strength": 3,
        "CommandPoints": 30,
        "availability": 10,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Atteam_Fagot_POL": {  # PPK Fagot
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

    #  infantry tab transports
    "Star_266_POL": {  # Star 266
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "UAZ_469_trans_POL": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "Honker_4011_POL": {  # Honker 4011
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "GAZ_66_POL": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "GAZ_66B_POL": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "BAV_485_POL": {  # BAW-485
        "CommandPoints": 15,
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
        "strength": 8,
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

    # "OT_64_SKOT_2_POL": {  # SKOT-2
    #     "CommandPoints": 20,
    #     "SpecialtiesList": {
    #         "add_specs": ["'refundable_unit'"],
    #     },
    # },

    # "OT_64_SKOT_2A_POL": {  # SKOT-2A
    #     "CommandPoints": 25,
    # },

    "BMP_1_SP2_POL": {  # BWP-1
        "CommandPoints": 20,
    },

    "BMP_2_POL": {  # BWP-2
        "CommandPoints": 50,
    },

    # POL RECON
    "HvyScout_POL": {  # Zmot. Zwiad. -> Zwiadowcy Zmot.
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

    "Scout_POL": {  # Zwiadowcy
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "POL_20_Pancerna": {
                "Transports": ['UAZ_469_trans_POL', 'OT_65_POL', 'Mi_2_trans_POL'],
            },
            "POL_4_Zmechanizowana": {
                "Transports": ['UAZ_469_trans_POL', 'BRDM_1_POL', 'Mi_2_trans_POL'],
            },
        },
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Scout_LRRP_POL": {  # Rozp. Specjalne [GSR]
        "Divisions": {
            "POL_20_Pancerna": {
                "Transports": ['Honker_4011_POL', 'Honker_RYS_POL', 'OT_65_POL', 'Mi_2_trans_POL'],
            },
        },
    },

    "Scout_LRRP_Para_POL": {  # Desant. Rozp. Specjalne [GSR]
    },

    "Scout_SF_POL": {  # Rozp. Specjalne
    },

    "BRM_1_POL": {  # BWR-1D
        "CommandPoints": 60,
        # "cards": {
        #     "default": 2,
        # },
        # "Divisions": {
        #     "default": {
        #         "cards": 2,
        #     },
        # },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "BRDM_2_POL": {
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

    "Mi_2_gunship_POL": {  # Mi-2US
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "ECM:": -0.1,
    },

    #   recon tab transports

    "BMP_1_SP2_reco_POL": {  # Rozp. BWP-1
        "CommandPoints": 35,
    },

    # "BRDM_1_POL": {  # BRDM-1
    #     "CommandPoints": 25,
    # },
    #
    # "OT_65_POL": {  # OT-65
    #     "CommandPoints": 25,
    # },

    "MTLB_TRI_Hors_POL": {  # Tri Hors
        "CommandPoints": 25,
    },

    "Honker_RYS_POL": {  # Honker Rys
        "CommandPoints": 25,
    },

    # POL AA
    "MANPAD_Strela_2M_POL": {  # Strzala-2M
        "CommandPoints": 20,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_kbk_AK", "FM_kbk_AK_noreflex")],
            },
        },
    },
    
    "MANPAD_Strela_2M_Para_POL": {  # Desant. Strzala-2M
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_kbk_AKM", "FM_kbk_AK_noreflex")],
            },
        },
    },

    "MTLB_Strela10_POL": {  # Strzala-10
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

    "ZSU_23_Shilka_POL": {  # ZSU-23-4 Szylka
        "optics": {
            "OpticalStrengthAltitude": 220,
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
            "OpticalStrengthAltitude": 300,
        },
        "CommandPoints": 90,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    # POL HELI


    # heli tab transports
    "Mi_2_trans_POL": {
        "CommandPoints": 35,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

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
        "WeaponDescriptor": {
            "turrets": {
                2: {
                    "AngleRotationMax": 2.094395,
                    "AngleRotationMaxPitch": 1.570796,
                    "AngleRotationMinPitch": -1.570796,
                },
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },

}
