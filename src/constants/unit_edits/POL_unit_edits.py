"""Polish unit edits."""

# from typing import Any, Dict

pol_unit_edits = {
    # POL LOG
    "DCA_ZU_23_2_POL": {  # ZU-23-2
        "CommandPoints": 20,
        "Factory": "EFactory/Logistic",
        "Divisions": {
            "default": {
                "Transports": ["MTLB_trans_POL"],
                "cards": 69,
            },
            "POL_4_Zmechanizowana": {
                "cards": 2,
            },
            "POL_20_Pancerna": {
                "cards": 1,
            },
        },
        "availability": [9, 7, 0, 0],
        "max_speed": 4,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "FOB_POL",
    },
    "DCA_ZU_23_2_Para_POL": {  # Desant. ZU-23-2
        "CommandPoints": 20,
        "GameName": {
            "display": "SPADO. ZU-23-2",
        },
        "Factory": "EFactory/Logistic",
        "Divisions": {
            "default": {
                "Transports": ["MTLB_trans_POL"],
                "cards": 69,
            },
            "POL_4_Zmechanizowana": {
                "cards": 2,
            },
            "POL_20_Pancerna": {
                "cards": 1,
            },
        },
        "availability": [9, 7, 0, 0],
        "max_speed": 4,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        # "UpgradeFromUnit": "FOB_POL",  # no fob in korpus
    },
    "DCA_ZUR_23_2S_JOD_POL": {  # ZUR-23-2S Jod
        "CommandPoints": 30,
        # "Factory": "EFactory/Logistic",  # keep in AA tab
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
        "max_speed": 4,
        "availability": [9, 7, 0, 0],
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },
    "DCA_ZUR_23_2S_JOD_Para_POL": {  # Desant. ZUR-23-2S Jod
        "CommandPoints": 30,
        "GameName": {
            "display": "SPADO. ZUR-23-2S JOD",
        },
        "Factory": "EFactory/Logistic",
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
        "availability": [6, 4, 0, 0],
        "max_speed": 4,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "DCA_ZU_23_2_Para_POL",
    },
    "UAZ_469_CMD_POL": {  # WD-43
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "GameName": {
            "display": "#CMD WD-43",
        },
        "availability": [0, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
    },
    "UAZ_469_CMD_Para_POL": {  # Desant. WD-43
        "GameName": {
            "display": "#CMD SPADO. WD-43",
        },
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
    },
    "BMP_1_CMD_POL": {  # BWP-1K3
        "CommandPoints": 155,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 3, 0],
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "UpgradeFromUnit": None,
    },
    "BRDM_2_CMD_POL": {  # BRDM-2U
        "strength": 8,
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
        "availability": [0, 3, 0, 0],
    },
    "BRDM_2_CMD_R5_POL": {  # BRDM-2 R-5
        "CommandPoints": 160,
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
    "OT_64_SKOT_CMD_POL": {  # SKOT R-2M
        "CommandPoints": 165,
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
    "Mi_2_CMD_POL": {  # Mi-2D PRZETACZNIK
        "GameName": {"display": "#CMD Mi-2D PRZEŁĄCZNIK"},
        "CommandPoints": 115,
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
    "BAV_485_Supply_POL": {  # BAW-485
        "UpgradeFromUnit": None,
    },
    "PTS_M_supply_POL": {  # PTS-M Zaop.
        "UpgradeFromUnit": "BAV_485_Supply_POL",
    },
    # POL INFANTRY
    "Engineers_CMD_POL": {  # Saperzy Ldr.
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV SAPERZY LDR.",
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
                "Unite",
            ],
        },
        "strength": 9,
        "WeaponAssignment": [
            (0, [0,]),
            (1, [0,]),
            (2, [0,]),
            (3, [0,]),
            (4, [0,]),
            (5, [0,]),
            (6, [0,]),
            (7, [0,]),
            (8, [1,]),
        ],
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
                "leader_sov",
                "_choc",
                "infantry_equip_light",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "Divisions": {
            "POL_20_Pancerna": {
                "Transports": ["Star_266_POL", "MTLB_trans_POL", "OT_64_SKOT_2_POL"],
            },
        },
        "WeaponDescriptor": {
            "Salves": {
                "MMG_PKM_7_62mm": 36,
            },
            "equipmentchanges": {
                "replace": [("RocketInf_RPG76_Komar", "MMG_PKM_7_62mm", "RocketInf_RPG76_Komar", "MMG_PKM_7_62mm")],
                "quantity": {
                    "FM_kbk_AK": 8,
                },
            },
        },
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "selector_tactic": "(2, 4)",
        "selector_tactic_obj": "02_04",
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },
    "Rifles_CMD_POL": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV PIECHOTA LDR.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Rifles_CMD_POL",
                "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                "leader_sov",
                "infantry_equip_light",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "POL_4_Zmechanizowana": {
                "Transports": ["Star_266_POL", "OT_64_SKOT_2A_POL"],
            },
        },
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "FM_kbk_AK": 9,
                "RocketInf_RPG76_Komar": 7,
            },
        },
        "selector_tactic": "(2, 4)",
        "selector_tactic_obj": "02_04",
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },
    "MotRifles_CMD_POL": {  # Piechota Zmech. Ldr.
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV PIECHOTA ZMECH. LDR.",
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
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                "leader_sov",
                "_ifv",
                "infantry_equip_light",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "POL_20_Pancerna": {
                "Transports": ["Star_266_POL", "BMP_1_SP2_POL", "BMP_2_POL"],
            },
        },
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "FM_kbk_AK": 9,
                "RocketInf_RPG76_Komar": 7,
            },
        },
        "selector_tactic": "(2, 4)",
        "selector_tactic_obj": "02_04",
        "is_infantry": True,
        "is_ground_vehicle": False,
        "remove_zone_capture": None,
    },
    "Engineers_POL": {  # Saperzy
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "POL_20_Pancerna": {
                "Transports": ["Star_266_POL", "MTLB_trans_POL", "OT_64_SKOT_2_POL", "OT_64_SKOT_2A_POL"],
            },
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "FM_AK_74": 11,
        #         "MMG_PKM_7_62mm": 36,
        #         "Grenade_Satchel_Charge": 5,
        #     },
        # },
        # 8x kbk AKM
        # 1x PKM
        # Satchel
        # RPG-76 Komar x4
    },
    "Engineers_Flam_POL": {  # Saperzy Szturmowi
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "POL_20_Pancerna": {
                "Transports": ["Star_266_POL", "MTLB_trans_POL", "OT_64_SKOT_2_POL", "OT_64_SKOT_2A_POL"],
            },
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_kbk_AK": 11,  # 7 mags per soldier bc heavy
                "MMG_PKM_7_62mm": 36,
            },
        },
        # 8x kbk AKM
        # 1x PKM
        # RPO Rys x6
    },
    "Groupe_AT_POL": {  # Druzyna PPanc
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "DRUŻYNA PPANC.",
        },
        "Divisions": {
            "add": ["POL_20_Pancerna"],
            "is_transported": True,
            "needs_transport": True,
            "POL_20_Pancerna": {
                "Transports": ["Star_266_POL", "MTLB_trans_POL", "BMP_1_SP2_POL"],
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
                "FM_kbk_AK": 9,
                "RocketInf_RPG7VL": 5,
                "special": {
                    "RocketInf_RPG7VL": (1, 5),
                },
            },
        },
        # 7x kbk AKM
        # 2x RPG-7VL x6 (panzerjager with VL instead of VR)
    },
    "Groupe_AT_Para_POL": {  # Desant. Druzyna Ppanc.
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SPADO. DRUŻYNA PPANC.",
        },
    },
    "Rifles_POL": {  # Piechota
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
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
                "FM_kbk_AK": 9,
            },
        },
    },
    "Rifles_HMG_POL": {  # Piechota (SVD)
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "PIECHOTA [SVD]",
        },
        "availability": [7, 5, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_kbk_AK": 9,
            },
        },
    },
    "MotRifles_POL": {  # Piechota Zmech
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "strength": 8,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_kbk_AK": 7,
                },
            },
            "Salves": {
                "FM_kbk_AK": 9,
            },
        },
        # 6x kbk AK(M?)
        # 1x PKM
        # RPG-7VM x6
    },
    "MotRifles_SVD_POL": {  # Piechota Zmech (SVD)
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "PIECHOTA ZMECH [SVD]",
        },
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 1, # Limit BWP-2 since we added BWP-2 to ATGMs and Leaders
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_kbk_AK": 9,
            },
        },
        # 4x kbk AKM
        # 2x PKM
        # 1x SVD
        # RPG-7VM x6
    },
    # "Para_POL": {  # Spadochroniarze
    #     "WeaponDescriptor": {
    #         "equipmentchanges": {
    #             "replace": [("FM_kbk_AKM", "FM_kbk_AKMS")],
    #         },
    #     },
    # },
    #
    # "Para_Metis_POL": {  # Spadochroniarze [Metis]
    #     "WeaponDescriptor": {
    #         "equipmentchanges": {
    #             "replace": [("FM_kbk_AKM", "FM_kbk_AKMS")],
    #         },
    #     },
    # },
    #
    # "Para_HMG_POL": {  # Spadochroniarze [PKM]
    #     "WeaponDescriptor": {
    #         "equipmentchanges": {
    #             "replace": [("FM_kbk_AKM", "FM_kbk_AKMS")],
    #         },
    #     },
    # },
    #
    "Engineers_paras_POL": {  # Desant. Saperzy
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SPADO. SAPERZY",
        },
    },
    "Engineers_paras_Flam_POL": {  # Desant. Saperzy (LPO-50)
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SPADO. SAPERZY [FLAM]",
        },
    },
    "Engineers_paras_CMD_POL": {  # Desant. Saperzy Dow.
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SPADO. SAPERZY LDR.",
        },
    },
    "Commandos_POL": {  # Komandosi
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 8, 6],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    "Commandos_Para_POL": {  # Desant. Komandosi
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SPADO. KOMANDOSI",
        },
    },
    # "Commandos_Para_CMD_POL": {  # Desant. Komandosi Dow. (sp only)
    #     "GameName": {
    #         "display": "SPADO. KOMANDOSI DOW.",
    #     },
    # },
    "WSW_POL": {  # WSW
        "CommandPoints": 25,
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
    },
    "Para_Security_POL": {  # Desant. Ochrona
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SPADO. OCHRONA",
        },
    },
    "Reserve_CMD_POL": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#CMD REZERWIŚCI DOW."
        }
    },
    "Reserve_POL": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "REZERWIŚCI"
        },
    },
    "ATteam_RCL_SPG9_POL": {  # SPG-9
        "strength": 5,
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },
    "ATteam_RCL_SPG9_Para_POL": {  # Desant. SPG-9(D)
        "strength": 5,
        "CommandPoints": 30,
        "availability": [0, 10, 7, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "GameName": {
            "display": "SPADO. SPG-9D",
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Ammo_Canon_HEAT_73_mm_SPG9_TOWED", "Ammo_Canon_HEAT_73_mm_SPG9D_TOWED")],
            },
        },
    },
    "HMGteam_PKM_POL": {
        "CommandPoints": "HMGteam_M60_US",
        "GameName": {
            "display": "PKM 7.62mm",
        },
        "strength": "HMGteam_M60_US",
        "max_speed": "HMGteam_M60_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_US",
        },
        "Divisions": {
            "POL_20_Pancerna": {
                "Transports": ["UAZ_469_trans_POL", "MTLB_trans_POL"],
            },
        },
    },
    "HMGteam_PKM_Naval_POL": {
        "CommandPoints": "HMGteam_M60_US",
        "strength": "HMGteam_M60_US",
        "max_speed": "HMGteam_M60_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_US",
        },
    },
    "HMGteam_PKM_para_POL": {
        "CommandPoints": "HMGteam_M60_AB_US",
        "GameName": {
            "display": "SPADO. PKM 7.62mm",
        },
        "strength": "HMGteam_M60_AB_US",
        "max_speed": "HMGteam_M60_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_AB_US",
        },
    },
    "HMGteam_NSV_POL": {  # NSW 12,7mm
        "CommandPoints": "HMGteam_M2HB_US",
        "GameName": {
            "display": "NSW 12.7mm",
            "token": "NSVAKANSW",
        },
        "strength": "HMGteam_M2HB_US",
        "max_speed": "HMGteam_M2HB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M2HB_US",
        },
        "availability": [8, 5, 0, 0],
        "Divisions": {
            "add": ["POL_20_Pancerna", "POL_4_Zmechanizowana"],
            "is_transported": True,
            "needs_transport": True,
            "POL_20_Pancerna": {
                "Transports": ["UAZ_469_trans_POL", "MTLB_trans_POL"],
                "cards": 1,
            },
            "POL_4_Zmechanizowana": {
                "Transports": ["UAZ_469_trans_POL"],
                "cards": 1,
            },
        },
    },
    
    "HMGteam_AGS17_POL": {
        "CommandPoints": "HMGteam_AGS17_SOV",
        "strength": "HMGteam_AGS17_SOV",
        "max_speed": "HMGteam_AGS17_SOV",
        "SpecialtiesList": {
            "add_specs": "HMGteam_AGS17_SOV",
        },
    },
    
    "Atteam_Fagot_POL": {  # PPK Fagot
        "CommandPoints": 30,
        "max_speed": 20,
        "availability": [9, 7, 5, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "Divisions": {
            "POL_20_Pancerna": {
                "Transports": ["UAZ_469_trans_POL", "MTLB_trans_POL", "BMP_1_SP2_POL", "BMP_2_POL"],
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("ATGM_9K111M_Faktoriya", "ATGM_9K111_Fagot")],
            },
        },
    },
    "Atteam_Fagot_Para_POL": {  # Desant. PPK Faktoria
        "CommandPoints": 40,
        "availability": [7, 5, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "GameName": {
            "display": "SPADO. PPK FAKTORIA",
        },
    },
    "Atteam_Konkurs_POL": {  # PPK Konkurs (campaign only)
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            # "add": ['POL_20_Pancerna'],
            # "is_transported": True,
            # "needs_transport": True,
        },
        "availability": [6, 4, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "Atteam_Fagot_POL",
    },
    "UAZ_469_SPG9_Para_POL": {  # Desant. UAZ-469 SPG-9
        "GameName": {
            "display": "SPADO. UAZ-469 SPG-9",
        },
        "CommandPoints": 25,
        "availability": [0, 12, 9, 0],
    },
    # infantry tab transports
    "Star_266_POL": {  # Star 266
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    "KrAZ_255B_POL": {  # KraZ-255 trsp
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
        "UpgradeFromUnit": "Star_266_POL",
    },
    "UAZ_469_trans_POL": {  # UAZ-469
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    "Honker_4011_POL": {  # Honker 4011
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
        "UpgradeFromUnit": "UAZ_469_trans_POL",
    },
    "GAZ_66B_POL": {  # GAZ-66B (para)
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    "BAV_485_POL": {  # BAW-485
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
        "UpgradeFromUnit": "GAZ_46_POL",
    },
    "GAZ_46_POL": {  # MAW
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
        "UpgradeFromUnit": None,
    },
    # POL ARTILLERY
    "OT_62_TOPAS_R3M_CMD_POL": {  # TOPAS R-2M
        "CommandPoints": 60,
        "GameName": {
            "display": "#LDRSOV TOPAS R-2M",
            "token": "TOPASARTLD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_OT_62_TOPAS_R3M_CMD_POL",
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
                "_amphibie",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_appui",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Transport",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 2, 0, 0],
        "remove_zone_capture": None,
    },
    "Mortier_PM43_120mm_POL": {  # M wz.43 120mm
        "CommandPoints": 40,
        "availability": [5, 4, 3, 0],
    },
    "Mortier_2S12_120mm_Para_POL": {  # Desant. 2S12 120mm
        # "CommandPoints": 40,
        "availability": [5, 4, 3, 0],
        "GameName": {
            "display": "SPADO. 2S12 120mm",
        },
    },
    "Mortier_M43_82mm_Para_POL": {  # Desant. M43 82mm
        "GameName": {
            "display": "SPADO. M wz. 43 82mm",
        },
    },
    "Mortier_M43_82mm_POL": {  # Desant. M43 82mm
        "GameName": {
            "display": "M wz. 43 82mm",
        },
    },
    "Mortier_2B9_Vasilek_Para_POL": {  # Desant. 2B9 Wasilok
        "CommandPoints": 45,
        "orders": {
            "add_orders": ["EOrderType/ShootOnPositionSmoke", "EOrderType/ShootOnPositionWithoutCorrectionSmoke"],
        },
        "GameName": {
            "display": "SPADO. 2B9 WASILOK",
        },
        "availability": [0, 4, 3, 2],
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
                                "HandheldEquipmentKey": "'WeaponAlternative_3'",
                                "ShowDispersion": False,
                                "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                                "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                                "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                            },
                        },
                    },
                },
            },
        },
    },
    "MLRS_WP_8z_POL": {  # Desant. M43 82mm
        "GameName": {
            "display": "WP-8z 140mm",
        },
    },
    "Howz_M30_122mm_POL": {  # H wz. 1938/85 122mm
        "CommandPoints": 75,
        "availability": [5, 4, 3, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },
    "Howz_ML20_152mm_POL": {  # AH wz. 1937/85 152mm
        "CommandPoints": 100,
        "availability": [3, 2, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "UpgradeFromUnit": "Howz_M30_122mm_POL",
    },
    "BM21_Grad_POL": {  # BM-21 Grad
        "CommandPoints": "BM21_Grad_SOV",
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": "BM21_Grad_SOV",
    },
    "RM70_85_POL": {
        "CommandPoints": "MFRW_RM70_DDR",
        "GameName": {
            "display": "RM wz. 70/85"
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketArt_M21OF_122mm", "RocketArt_M21OF_122mm_RM70")],
            },
        },
        "availability": "MFRW_RM70_DDR",
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },
    "2S1_POL": {  # 2S1 Gozdzik
        "CommandPoints": "2S1_Gvozdika_SOV",
        "availability": "2S1_Gvozdika_SOV",
        # "CommandPoints": 110,
        # "availability": [3, 2, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },
    "2S1M_POL": {  # 2S1M Morski Gozdzik
        "CommandPoints": "2S1_Gvozdika_SOV",
        "availability": "2S1_Gvozdika_SOV",
        # "CommandPoints": 110,
        # "availability": [3, 2, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },
    "DANA_POL": {  # AHS wz. 77 DANA
        "GameName": {
            "display": "AHS wz. 77 DANA",
        },
        "CommandPoints": 210,
        "availability": [2, 0, 1, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        # "max_speed": 65,
        # # speed corrected in vanilla - keeping this here for reference
        # "road_speed": {
        #     # requires either factor, or base_speed & road_speed
        #     # factor computed from road_speed / base_speed if factor not defined
        #     # visual (UI) road_speed unchanged if unspecified
        #     "base_speed": 65,
        #     "factor": 1.92,
        #     "road_speed": 100,
        # },
    },
    # POL TANK
    "T55A_CMD_POL": {  # T-55AD LDR
        "CommandPoints": 80,
        "GameName": {
            "display": "#LDRSOV T-55AD LDR.",
            "token": "POLTFFAD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T55A_CMD_POL",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                "leader_sov",
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
    "T55AM_Merida_CMD_POL": {  # T-55AM Merida LDR
        "CommandPoints": 125,
        "GameName": {
            "display": "#LDRSOV T-55AD-1M Merida LDR.",
            "token": "POLT55AMLD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T55AM_Merida_CMD_POL",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                "leader_sov",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },
    "T72M_CMD_POL": {  # T-72MD LDR
        "CommandPoints": 160,
        "GameName": {
            "display": "#LDRSOV T-72MD LDR.",
            "token": "POLTSTMLDR",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T72M_CMD_POL",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                "leader_sov",
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
    "T72M1_CMD_POL": {  # T-72M1D LDR
        "CommandPoints": 190,
        "GameName": {
            "display": "#LDRSOV T-72M1D LDR.",
            "token": "POLTSTMOLD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T72M1_CMD_POL",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                "leader_sov",
                "_smoke_launcher",
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
    "T55A_POL": {  # T-55A
        "CommandPoints": 70,
        "availability": [10, 7, 0, 0],
    },
    "T55AS_POL": {  # T-55AS coffin launcher
        "CommandPoints": 85,
        "availability": [0, 4, 3, 0],
    },
    "T55AM_Merida_POL": {  # T-55AM Merida
        "CommandPoints": 110,
        "availability": [0, 8, 6, 0],
    },
    "T55AMS_Merida_POL": {  # T-55AMS Merida coffin launcher
        "CommandPoints": 140,
        "availability": [0, 3, 2, 0],
    },
    "T72M_POL": {  # T-72M
        "CommandPoints": 140,
        "availability": [0, 8, 6, 0],
    },
    "T72M1_POL": {  # T-72M1
        "CommandPoints": 170,
        "availability": [0, 6, 4, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },
    "T72M1_Wilk_POL": {  # T-72M2 Wilk
        "CommandPoints": 190,
        "availability": [0, 0, 4, 3],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },
    "UAZ_469_Fagot_POL": {  # UAZ-469 Fagot/Faktoria
        "CommandPoints": 35,
        "GameName": {
            "display": "UAZ-469 FAKTORIA",
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": 6,
            },
        },
        "availability": [10, 7, 0, 0],
    },
    "UAZ_469_Fagot_Para_POL": {  # Desant./Spado. UAZ-469 Fagot/Faktoria
        "CommandPoints": 35,
        "GameName": {
            "display": "SPADO. UAZ-469 FAKTORIA",
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": 6,
            },
        },
    },
    "AT_D48_85mm_POL": {  # D-48 AT 85mm
        "CommandPoints": 40,
        "availability": [9, 7, 5, 0],
    },
    "BRDM_2_Konkurs_POL": {  # BRDM-2 Konkurs
        "CommandPoints": "BRDM_2_Konkurs_SOV",
        "strength": "BRDM_2_Konkurs_SOV",
        "stealth": "BRDM_2_Konkurs_SOV",
        "availability": "BRDM_2_Konkurs_SOV",
    },
    "BRDM_2_Malyu_P_POL": {  # BRDM-2 Malutka-P
        "CommandPoints": 40,
        "strength": 8,
        "stealth": 1.5,
        "availability": [10, 7, 0, 0],
    },
    #   tank tab transports
    "OT_64_SKOT_2_POL": {  # SKOT-2
        "CommandPoints": 20,
        "strength": 10,
    },
    "OT_64_SKOT_2A_POL": {  # SKOT-2A
        "CommandPoints": 25,
        "strength": 10,
        "SpecialtiesList": {
            "overwrite_all": [
                "_transport2",
                "_amphibie",
            ],
        },
        "is_prime_mover": True,
    },
    "OT_64_SKOT_2AM_POL": {  # SKOT-2AM
        "CommandPoints": 30,
        "strength": 10,
        "SpecialtiesList": {
            "overwrite_all": [
                "_transport2",
                "_amphibie",
            ],
        },
        "is_prime_mover": True,
    },
    "OT_64_SKOT_2P_POL": {  # SKOT-2AP
        "CommandPoints": 30,
        "strength": 10,
        "SpecialtiesList": {
            "overwrite_all": [
                "_transport2",
                "_amphibie",
            ],
        },
        "is_prime_mover": True,
    },
    "MTLB_trans_POL": {  # MT-LB
        "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    "BMP_1_SP2_POL": {  # BWP-1
        "CommandPoints": 20,
        "UpgradeFromUnit": "MTLB_trans_POL",
    },
    "BMP_2_POL": {  # BWP-2
        "CommandPoints": "BMP_2_SOV",
    },
    # POL RECON
    "HvyScout_POL": {  # Zmot. Zwiad.
        "GameName": {
            "display": "#RECO2 ZWIADOWCY ZMOT.",
        },
        "armor": "Infantry_armor_reference",
        "CommandPoints": 35,
        "availability": [6, 4, 0, 0],
        "max_speed": 26,
        "strength": 8,
        "WeaponAssignment": [
            (0, [1,]),
            (1, [0,]),
            (2, [0,]),
            (3, [0,]),
            (4, [0,]),
            (5, [0,]),
            (6, [0,]),
            (7, [0, 2,]),
        ],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_kbk_AK": 7,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    "Engineers_Scout_POL": {  # Saperzy Zwiadowcy
        "GameName": {
            "display": "#RECO2 SAPERZY ZWIAD.",
        },
        "armor": "Infantry_armor_reference",
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 4, 3, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "DeploymentShift": 0,
    },
    "Scout_POL": {  # Zwiadowcy
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "POL_20_Pancerna": {
                "Transports": ["UAZ_469_trans_POL", "OT_65_POL", "Mi_2_trans_POL"],
            },
            "POL_4_Zmechanizowana": {
                "Transports": ["UAZ_469_trans_POL", "BRDM_1_POL", "Mi_2_trans_POL"],
            },
        },
        "availability": [8, 6, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_kbk_AK": 9,
                "PM_PM63_RAK": 9,
                "RocketInf_RPG7": 4,
            },
        },
        "DeploymentShift": 0,
    },
    "Scout_para_POL": {  # Desant. Zwiadowcy
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#RECO2 SPADO. ZWIADOWCY",
        },
    },
    "Scout_LRRP_POL": {  # Rozp. Specjalne [GSR]
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "strength": 4,
        "WeaponAssignment": [
            (0, [0,]),
            (1, [0,]),
            (2, [0,]),
            (3, [0, 1,]),
        ],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_PM63_RAK": 4,
                },
            },
            "Salves": {
                "RocketInf_RPG76_Komar": 4,
            },
        },
        "Divisions": {
            "POL_20_Pancerna": {
                "Transports": ["Honker_4011_POL", "Honker_RYS_POL", "OT_65_POL", "Mi_2_trans_POL", "Mi_24D_POL"],
            },
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "DeploymentShift": 0,
        "GameName": {
            "display": "#RECO2 ROZP. SPECJALNE [GSR]",
        },
        "availability": [0, 0, 4, 3],
    },
    "Scout_LRRP_Para_POL": {  # Desant. Rozp. Specjalne [GSR]
        # "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "GameName": {
            "display": "#RECO2 SPADO. ROZP. [GSR]",
        },
    },
    "Sniper_paras_POL": {  # Desant. Snajper
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#RECO2 SPADO. SNAJPER",
        },
    },
    "Scout_SF_POL": {  # Rozp. Specjalne
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        # "strength": 5,
        "max_speed": 26,
        "availability": [0, 0, 4, 3],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_Tantal": 9,
                "PM_PM63_RAK": 9,
                "RocketInf_RPG7VL": 4,
            },
        },
        "DeploymentShift": 0,
    },
    # TODO: Find out what happened to this unit
    # "Scout_SF_Para_POL": {  # Desant. Rozp. Specjalne
    #     "GameName": {
    #         "display": "#RECO2 SPADO. ROZP. SPECJALNE",
    #     },
    # },
    "BRDM_1_PSNR1_POL": {  # BRDM-1 PSNR-1
        "CommandPoints": 30,
        "availability": [8, 0, 0, 0],
    },
    "BRM_1_POL": {  # BWR-1D
        "CommandPoints": "BRM_1_SOV",
        "availability": "BRM_1_SOV",
        # "CommandPoints": 55,
        # "availability": [6, 4, 0, 0],
    },
    "BRDM_2_POL": {  # BRDM-2
        "CommandPoints": "BRDM_2_SOV",
        "availability": "BRDM_2_SOV",
        # "CommandPoints": 35,
        # "availability": [8, 6, 0, 0],
        "strength": 8,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "UpgradeFromUnit": "OT_65_POL",
    },
    "Mi_2_gunship_POL": {  # Mi-2US
        "availability": [0, 4, 3, 0],
    },
    "Mi_2Ro_reco_POL": {  # Mi-2Ro
        "CommandPoints": 50,
        "availability": [0, 4, 3, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_23mm_NS23": 25,
            },
        },
    },
    #   recon tab transports
    "BMP_1_SP2_reco_POL": {  # Rozp. BWP-1
        "CommandPoints": 35,
    },
    "BRDM_1_POL": {  # BRDM-1
        "CommandPoints": 25,
        "UpgradeFromUnit": None,
    },
    "OT_65_POL": {  # OT-65
        "CommandPoints": 15,
        "GameName": {
            "display": "#RECO1 OT-65",
        },
        "UpgradeFromUnit": "BRDM_1_POL",
    },
    "MTLB_TRI_Hors_POL": {  # TRI Hors
        "CommandPoints": 20,
        "UpgradeFromUnit": None,
    },
    "Honker_RYS_POL": {  # Honker Rys
        "CommandPoints": 25,
        "UpgradeFromUnit": "Honker_4011_POL",
    },
    # POL AA
    "MANPAD_Strela_2M_POL": {  # Strzala-2M
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [12, 9, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_kbk_AK", "FM_kbk_AK_noreflex")],
            },
            "Salves": {
                "FM_kbk_AK": 11,
            },
        },
    },
    "MANPAD_Strela_2M_Naval_POL": {  # Desant. Strzala-2M
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_kbk_AK", "FM_kbk_AK_noreflex")],
            },
            "Salves": {
                "FM_kbk_AK": 11,
            },
        },
        "GameName": {
            "display": "NIEB. BERETY STRZAŁA-2M",
        },
    },
    "MANPAD_Strela_2M_Para_POL": {  # Desant. Strzala-2M
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_kbk_AKM", "FM_kbk_AK_noreflex")],
            },
            "Salves": {
                "FM_kbk_AK": 11,
            },
        },
        "GameName": {
            "display": "SPADO. STRZAŁA-2M",
        },
    },
    "DCA_AZP_S60_POL": {  # AZP S-60
        "CommandPoints": 35,
        "max_speed": 4,
        "availability": [9, 7, 0, 0],
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },
    "Hibneryt_POL": {  # Hibneryt
        "CommandPoints": 40,
        "availability": [7, 5, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm": 18,
            },
        },
    },
    "Hibneryt_KG_POL": {  # Hibneryt KG
        "CommandPoints": 50,
        "availability": [6, 4, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_Jod_SP_23mm": 18,
            },
        },
    },
    "BRDM_Strela_1_POL": {  # (BRDM-2) Strzala-1
        "CommandPoints": "BRDM_Strela_1_SOV",
        "availability": "BRDM_Strela_1_SOV",
        # "CommandPoints": 50,
        # "availability": [6, 4, 0, 0],
        "strength": 8,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 220,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "SAM_Strela1_salvolength4": 2,
            },
        },
    },
    "MTLB_Strela10_POL": {  # (MT-LB) Strzala-10
        "CommandPoints": "MTLB_Strela10_SOV",
        "availability": "MTLB_Strela10_SOV",
        # "CommandPoints": 65,
        # "availability": [6, 4, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
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
    "ZSU_23_Shilka_POL": {  # ZSU-23-4 Szylka
        "CommandPoints": 85,
        "availability": [6, 4, 0, 0],
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
    "Osa_9K33M3_POL": {  # PWRB Osa-AKM
        "CommandPoints": 130,
        "GameName": {
            "display": "9K33M3 ROMB",  # wargame reference
        },
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
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },

    },
    "2K12_KUB_POL": {  # 2K12 Kub
        "CommandPoints": "2K12_KUB_SOV",
        "availability": "2K12_KUB_SOV",
        # "CommandPoints": 90,
        # "availability": [4, 3, 0, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 300,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },
    # POL HELI
    "Mi_24D_POL": {  # 64x S-5, 4x Falanga - Mi-24D [AT] -> transport
        "CommandPoints": 145,
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Helo",
                "Helo_Gunship",
                "Helo_Transport",
                "UNITE_Mi_24D_POL",
                "Unite",
            ],
        },
        "SpecialtiesList": {
            "overwrite_all": [
                "_transport1",
            ],
        },
        "orders": {
            "add_orders": ["EOrderType/UnloadFromTransport", "EOrderType/UnloadAtPosition", "EOrderType/Load"]},
        "Divisions": {
            "remove": ["POL_20_Pancerna"],
        },
        "availability": [0, 4, 3, 0],
        "GameName": {
            "display": "Mi-24D DESANT"
        },
    },
    "Mi_24D_s8_AT_POL": {  # 80x S-8, 4x Falanga - Mi-24D [AT2]
        "CommandPoints": 150,
        "availability": [0, 4, 3, 0],
        "GameName": {
            "display": "Mi-24D [AT]"
        },
    },
    "Mi_24V_POL": {
        "CommandPoints": "Mi_24V_AT_SOV",
        "availability": "Mi_24V_AT_SOV",
    },
    "W3W_Sokol_RKT_POL": {  # W-3 Sokol [RKT]
        "GameName": {
            "display": "W-3 SOKÓŁ [RKT]"
        }
    },
    "W3W_Sokol_AA_POL": {  # W-3 Sokol [AA]
        "GameName": {
            "display": "W-3 SOKÓŁ [AA]"
        }
    },
    "Mi_2_rocket_POL": {  # Mi-2URN Zmija
        "CommandPoints": 50,
        "availability": [8, 6, 0, 0],
    },
    "Mi_2_ATGM_POL": {  # Mi-2URP Salamandra
        "CommandPoints": 60,
        "availability": [7, 5, 0, 0],
        "Divisions": {
            "POL_20_Pancerna": {
                "cards": 2,
            },
        },
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_23mm_NS23": 25,
            },
        },
    },
    "Mi_2_AA_POL": {  # Mi-2URPG GNIEWOSZ
        "CommandPoints": 80,
        "availability": [0, 4, 3, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_23mm_NS23": 25,
            },
        },
    },
    # heli tab transports
    "Mi_2_trans_POL": {  # Mi-2P
        "CommandPoints": 35,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    "W3_Sokol_POL": {  # W-3 Sokol
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
        "GameName": {
            "display": "W-3 SOKÓŁ"
        },
    },
    "Mi_8T_non_arme_POL": {  # Mi-8T
        "CommandPoints": 50,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
        "UpgradeFromUnit": "W3_Sokol_POL",
    },
    "Mi_8T_POL": {  # twin S-5 x32 - Mi-8T [RKT]
        "CommandPoints": 50,
    },
    # POL AIR
    "MiG_17PF_POL": {  # Lim-6M [RKT]
        "GameName": {
            "display": "Lim-6M [RKT]"
        },
    },
    "MiG_21bis_AA_POL": {  # 4x R-60M, 2x R-3R MiG-21bis [AA1]
        # effectively deleted - replaced with mig23 AA2
        "Divisions": {
            "remove": ["POL_20_Pancerna"],
        },
        "CommandPoints": 120,
        "availability": [0, 4, 3, 2],
        "GameName": {
            "display": "MiG-21bis [AA2]"
        },
    },
    "MiG_21bis_POL": {  # 4x R-60M, 2x R-13M - MiG-21bis [AA2]
        "CommandPoints": "MiG_21bis_AA2_DDR",
        "availability": "MiG_21bis_AA2_DDR",
        "GameName": {
            "display": "MiG-21bis [AA]"
        },
    },
    "MiG_21bis_HE_POL": {  # MiG-21bis [HE]
        "CommandPoints": 135,
        "availability": [0, 3, 0, 0],
    },
    "MiG_21bis_RKT2_POL": {  # 4x S-24 [RKT2]
        "CommandPoints": 100,
        "availability": [0, 4, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketAir_S24_240mm_avion_salvolength4": (1, True),
                # set salvo count to 1 and corresponding SalvoIsMainSalvo to True
            },
            "equipmentchanges": {
                "replace": [("RocketAir_S24_240mm_salvolength2", "RocketAir_S24_240mm_avion_salvolength4")],
            },
        },
    },
    "MiG_21bis_AT_POL": {  # 2x Kh-66, 2x R-13M
        "CommandPoints": 115,
        "availability": [0, 3, 0, 0],
    },
    "MiG_23MF_AA_POL": {  # MiG-23MF [AA], 2x R-23R, 4x R-60M
        "CommandPoints": 125,
        "availability": [0, 4, 3, 2],
    },
    "MiG_23MF_AA2_POL": {  # MiG-23MF [AA2], 2x R-3R, 2x R-13M
        "CommandPoints": 110,
        "availability": [0, 4, 3, 2],
        "Divisions": {
            "add": ["POL_20_Pancerna"],
            "POL_20_Pancerna": {
                "cards": 1,
            },
        },
    },
    "MiG_29_AA_POL": {  # 4x R-73, 2x R-27R [AA]
        "GameName": {
            "display": "MiG-29A [AA]",
        },
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 2, 0, 1],
    },
    "Su_17_cluster_POL": { # Su-20 [CLU] - 6x RBK-500
        "CommandPoints": 180,
        "availability": [0, 2, 0, 0],
    },
    "Su_22_POL": {
        "CommandPoints": "Su_22_DDR",
        "availability": "Su_22_DDR",
    },
    "Su_22_clu_POL": {  # 4x RBK-250, 2x R-60M
        "CommandPoints": 205,
        "availability": [0, 2, 0, 0],
    },
    "Su_22_AT_POL": {  # Su-22M4 Seria 30
        "CommandPoints": "Su_22_AT_SOV",
        "availability": "Su_22_AT_SOV",
    },
    "Su_22_RKT_POL": {  # 4x S-24, 2x R-60M
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
    "Su_22_SEAD_POL": {  # Su-22M4P [SEAD]
        "CommandPoints": 180,
        "WeaponDescriptor": {
            "turrets": {
                2: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "availability": [0, 2, 0, 1],
        "Divisions": {
            "add": ["POL_20_Pancerna"],
            "POL_20_Pancerna": {
                "cards": 1,
            },
        },
    },
}
# fmt: off
