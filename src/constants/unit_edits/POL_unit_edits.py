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
        "max_speed": 6,
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
        "max_speed": 6,
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
        "max_speed": 6,
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
        "max_speed": 6,
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
        "CommandPoints": 170,
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
    
    "BRDM_2_CMD_R5_POL": {  # BRDM-2 R-5
        "CommandPoints": 175,
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
        "CommandPoints": 180,
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
        "remove_zone_capture": None,
    },

    
    "Commandos_CMD_POL": {  # Komandosi Dow. (sp only)
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
         "GameName": {
             "display": "#LDRSOV KOMANDOSI LDR.",
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
                "UNITE_Commandos_CMD_POL",
                "Unite",
                "noSIGINT",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry_sf", "Texture_sf"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_sf',
                '_choc',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry_sf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPG7VL": 6,
            },
        },
        "remove_zone_capture": None,
    },

    "Commandos_Para_CMD_POL": {  # Desant. Komandosi Dow. (sp only)
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
         "GameName": {
             "display": "#LDRSOV SPADO. KOMANDOSI LDR.",
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
                "UNITE_Commandos_Para_CMD_POL",
                "Unite",
                "noSIGINT",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry_sf", "Texture_sf"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_sf',
                '_choc',
                '_para',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry_sf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_PM63_RAK": 8,
                    "Grenade_Satchel_Charge": 1,
                },
                "replace": [("FM_Tantal", "PM_PM63_RAK"),
                        ("MMG_PKM_7_62mm", "Grenade_Satchel_Charge"),
                        ("RocketInf_RPG7", "RocketInf_RPG76_Komar")],
            },
            "Salves": {
                "Grenade_Satchel_Charge": 5,
                "RocketInf_RPG76_Komar": 8,
            },
        },
        "remove_zone_capture": None,
        "ButtonTexture": "Commandos_CMD_POL",
    },

    "Engineers_paras_CMD_POL": {  # Desant. Saperzy Dow.
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "strength": 8,
        "GameName": {
            "display": "#LDRSOV SPADO. SAPERZY LDR.",
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
                "UNITE_Engineers_paras_CMD_POL",
                "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
                "leader_sov",
                "_choc",
                "_para",
                "infantry_equip_medium",
            ],
        },
       "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_kbk_AK": 8,
                },
                "replace": [
                    ("FM_kbk_AKM", "FM_kbk_AK"),
                    ("RocketInf_RPG76_Komar", "RocketInf_RPG7", "RocketInf_RPG76_Komar", "RocketInf_RPG7"),
                ],
            },
            "Salves": {
                "RocketInf_RPG7": 6,
            },
        },
        "selector_tactic": "(2, 4)",
        "selector_tactic_obj": "02_04",
        "remove_zone_capture": None,
    },

     "Para_CMD_POL": {  # Dow. SPADOCHRONIARZE 
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "strength": 7,
        "GameName": {
            "display": "#LDRSOV SPADOCHRONIARZE LDR.",
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
                "UNITE_Para_CMD_POL",
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
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_kbk_AK": 7,
                },
                "replace": [
                    ("FM_kbk_AKM", "FM_kbk_AK"),
                ],
            },
            "Salves": {
                "RocketInf_RPG7": 6,
            },
        },
        "selector_tactic": "(2, 4)",
        "selector_tactic_obj": "02_04",
        "remove_zone_capture": None,
    },
    
    "Reserve_CMD_POL": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
         "GameName": {
            "display": "#CMD REZERWIŚCI DOW."
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
                "UNITE_Reserve_CMD_POL",
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
                "leader_sov",
                "_reservist",
                "infantry_equip_light",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 7, 5, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_kbk_AK": 5,
                },
                "insert": [(2, "RocketInf_RPG7")],
                "insert_edits": {
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "SalvoStockIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
                },
                "Salves": {
                    "insert": [(2, 6)],
                },
            },
        "selector_tactic": "(2, 4)",
        "selector_tactic_obj": "02_04",
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
        "availability": [8, 6, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "UpgradeFromUnit": "Engineers_CMD_POL",
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
            },
        },
        # 7x kbk AKM
        # 2x RPG-7VL x6 (panzerjager with VL instead of VR)
    },
    
    "Groupe_AT_Para_POL": {  # Desant. Druzyna Ppanc.
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SPADO. DRUŻYNA PPANC.",
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_kbk_AK": 9,
                "RocketInf_RPG7VL": 5,
            },
        },
        # 7x kbk AKM
        # 2x RPG-7VL x6 (panzerjager with VL instead of VR)
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
    
     "Para_POL": {  # Spadochroniarze
        "CommandPoints": 40,
        "availability": [0, 6, 4, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
         "WeaponDescriptor": {
             "equipmentchanges": {
                "replace": [("RocketInf_RPG7", "RocketInf_RPG7VL")],
            },
        },
        # 7x kbk AKM
        # 1x RPK
        # 1x SVD
        # RPG-7VL x6
    },
    
     "Para_Metis_POL": {  # Spadochroniarze [Metis]
        "CommandPoints": 45,
        "availability": [0, 6, 4, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        # 8x kbk AKM
        # 1x RPK
        # Metis x6
     },
    
     "Para_HMG_POL": {  # Spadochroniarze [PKM]
        "CommandPoints": 40,
        "availability": [0, 6, 4, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
         "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketInf_RPG76_Komar", "RocketInf_RPG7")],
            },
            "Salves": {
                "RocketInf_RPG7": 6,
            },
        },
        # 6x kbk AKM
        # 3x PKM
        # RPG-7VM x6
    },
    
    "Engineers_paras_POL": {  # Desant. Saperzy
        "CommandPoints": 40,
        "availability": [0, 6, 4, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                 "replace": [
                    ("FM_kbk_AKM", "FM_kbk_AK"),
                ],
                "insert": [(3, "RocketInf_RPG7")],
                "insert_edits": {
                    3: {
                        "turret_edits": {
                            "YulBoneOrdinal": 4,
                        },
                        "SalvoStockIndex": 3,
                        "HandheldEquipmentKey": "'WeaponAlternative_4'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_4'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_4'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_4"],
                    },
                },
            },
            "Salves": {
                "insert": [(3, 6)],
            },
        },
        "GameName": {
            "display": "SPADO. SAPERZY",
        },
    },
    
    "Engineers_paras_Flam_POL": {  # Desant. Saperzy (LPO-50)
        "CommandPoints": 50,
        "availability": [0, 6, 4, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "strength": 9,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "flamethrower_LPO": False,
                },
                "replace": [
                    ("FM_kbk_AKM", "FM_kbk_AK")
                ],
                "quantity": {
                    "FM_kbk_AK": 7,
                    "flamethrower_LPO": 2,
                },
            },
            "Salves": {
                "FM_kbk_AK": 9,
                "flamethrower_LPO": 120,
            },
        },
        "GameName": {
            "display": "SPADO. SAPERZY [FLAM]",
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
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "GameName": {
            "display": "SPADO. KOMANDOSI",
        },
        "UpgradeFromUnit": "Commandos_Para_CMD_POL",
    },
    
    
    
    "WSW_POL": {  # WSW
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 8, 6, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Para_Security_POL": {  # Desant. Ochrona
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [0, 6, 4, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "GameName": {
            "display": "SPADO. OCHRONA",
        },
    },
    
    "Reserve_POL": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [12, 0, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
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
        "UpgradeFromUnit": None,
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
        "UpgradeFromUnit": "HMGteam_PKM_POL",
    },
    
    "HMGteam_AGS17_POL": {
        "CommandPoints": "HMGteam_AGS17_SOV",
        "strength": "HMGteam_AGS17_SOV",
        "max_speed": "HMGteam_AGS17_SOV",
        "SpecialtiesList": {
            "add_specs": "HMGteam_AGS17_SOV",
        },
        "UpgradeFromUnit": "HMGteam_NSV_POL",
        "ButtonTexture": "HMGteam_PKM_POL",
    },
    
    "Atteam_Fagot_POL": {  # PPK Fagot
        "CommandPoints": 25,
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
        "UpgradeFromUnit": "ATteam_RCL_SPG9_POL",
    },
    
    "Atteam_Fagot_Para_POL": {  # Desant. PPK Faktoria
        "CommandPoints": 35,
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
        "CommandPoints": 45,
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
        "UpgradeFromUnit": "UAZ_469_SPG9_POL",
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
        "availability": [0, 3, 0, 0],
        "remove_zone_capture": None,
    },
    
    "Mortier_240mm_M240_POL": {  # M wz.1951 240mm
        "CommandPoints": 110,
        "availability": [3, 2, 0, 0],
         "GameName": {
            "display": "M wz.1951 240mm",
        },
    },

     "Mortier_M43_160mm_POL": {  # M wz.43 160mm
        "CommandPoints": 60,
        "availability": [4, 3, 0, 0],
         "GameName": {
            "display": "M wz.43 160mm",
        },
        "TagSet": {
            "overwrite_all": [
                 "AllUnits",
                "AllowedForMissileRoE",
                "Artillerie",
                "Artillerie_Courte_Portee",
                "CanBeAirlifted",
                "GroundUnits",
                "UNITE_Mortier_M43_160mm_POL",
                "Unite",
                "Unite_transportable"
            ],
        },
    },

    "Mortier_PM43_120mm_POL": {  # M wz.43 120mm
        "CommandPoints": 45,
        "availability": [5, 4, 3, 0],
    },
    
    "Mortier_2S12_120mm_Para_POL": {  # Desant. 2S12 120mm
        "CommandPoints": 45,
        "availability": [0, 5, 4, 3],
        "GameName": {
            "display": "SPADO. 2S12 120mm",
        },
    },
    
    "Mortier_M43_82mm_Para_POL": {  # Desant. M43 82mm
        "CommandPoints": 30,
        "availability": [0, 5, 4, 3],
        "GameName": {
            "display": "SPADO. M wz. 43 82mm",
        },
    },
    
    "Mortier_M43_82mm_POL": {  # Desant. M43 82mm
        "CommandPoints": 30,
        "availability": [5, 4, 3, 0],
        "GameName": {
            "display": "M wz. 43 82mm",
        },
        "SpecialtiesList": {
            "overwrite_all": [
                "_canBeAirlifted",
            ],
        },
        "DeploymentShift": 0,
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
                0: {
                    "MountedWeapons": {
                        "insert": {
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
    
    "Howz_M30_122mm_POL": {  # H wz. 1938/85 122mm
        "CommandPoints": 75,
        "availability": [5, 4, 3, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },

    "Howz_A19_122mm_POL": {  # AH wz. 1931/37/85 122mm (A-19 122mm)
        "CommandPoints": 90,
        "availability": [5, 4, 3, 0],
        "GameName": {
            "display": "AH wz. 1931/37/85 122mm",
        },
         "UpgradeFromUnit": "Howz_M30_122mm_POL",
    },

    "Howz_M46_130mm_POL": {  # AHP wz. 1954 130mm (M-46 132mm)
        "CommandPoints": 100,
        "availability": [4, 3, 2, 0],
        "GameName": {
            "display": "AHP wz. 1954 130mm",
        },
        "UpgradeFromUnit": "Howz_A19_122mm_POL",
        "ButtonTexture": "Howz_M46_130mm_TCH",
    },
    
    "Howz_ML20_152mm_POL": {  # AH wz. 1937/85 152mm
        "CommandPoints": 100,
        "availability": [3, 2, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "UpgradeFromUnit": "Howz_D1_152mm_POL",
    },

     "Howz_D1_152mm_POL": {  # H wz. 1943 152mm (D-1 152mm)
        "CommandPoints": 85,
        "availability": [3, 2, 0, 0],
        "UpgradeFromUnit": "Howz_M46_130mm_POL",
        "GameName": {
            "display": "H wz. 1943 152mm",
        },
        "ButtonTexture": "Howz_D1_152mm_SOV",
    },

     "MLRS_WP_8z_POL": {  # WP-8z
        "CommandPoints": 60,
        "GameName": {
            "display": "WP-8z 140mm",
        },
    },
    
    "BM14M_POL": {  # BM-14M
        "CommandPoints": 180,
        "availability": [3, 2, 0, 0],
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
        "UpgradeFromUnit": "2S1_POL",
    },

    "2S7_Pion_POL": {  # 2S7 Piwonia
        "CommandPoints": 230,
        "availability": [2, 0, 1, 0],
        "UpgradeFromUnit": "DANA_POL",
    },
    
    # POL TANK
    #    "T34_85M_CMD_POL": {  # T-34/85MD LDR
    #   "CommandPoints": 40,
    #   "GameName": {
    #        "display": "#LDRSOV T-34/85MD LDR.",
    #        "token": "POLTFFAD",
    #    },
    #    "TagSet": {
    #        "overwrite_all": [
    #            "AllUnits",
    #            "AllowedForMissileRoE",
    #            "Char",
    #            "GroundUnits",
    #            "UNITE_T34_85M_CMD_POL",
    #            "Unite",
    #        ],
    #    },
    #    "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
    #    "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
    #    "UnitRole": "armor",
    #    "SpecialtiesList": {
    #        "overwrite_all": [
    #            "_reservist",
    #            "leader_sov",
    #        ],
    #    },
    #    "MenuIconTexture": "Texture_RTS_H_Armor",
    #    "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
    #    "availability": [0, 0, 6, 0],
    #    "remove_zone_capture": None,
    #},

    # "T54B_CMD_POL": {  # T-54BD LDR (now a new unit for the model)
    #     "CommandPoints": 75,
    #     "GameName": {
    #         "display": "#LDRSOV T-54BD LDR.",
    #         "token": "POLTFFBD",
    #     },
    #     "TagSet": {
    #         "overwrite_all": [
    #             "AllUnits",
    #             "AllowedForMissileRoE",
    #             "Char",
    #             "GroundUnits",
    #             "UNITE_T54B_CMD_POL",
    #             "Unite",
    #         ],
    #     },
    #     "ButtonTexture": "T55A_CMD_POL",
    #     "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
    #     "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
    #     "UnitRole": "armor",
    #     "SpecialtiesList": {
    #         "overwrite_all": [
    #             "leader_sov",
    #         ],
    #     },
    #     "MenuIconTexture": "Texture_RTS_H_Armor",
    #     "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
    #     "availability": [0, 0, 6, 0],
    #     "remove_zone_capture": None,
    # },
    
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
                "_smoke_launcher",
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
        "CommandPoints": 165,
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
        "CommandPoints": 195,
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
    
    "ASU_85_CMD_POL": {  # ASU-85 LDR
        "CommandPoints": 70,
        "GameName": {
            "display": "#LDRSOV ASU-85D LDR.",
            "token": "POLASUEFD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_ASU_85_CMD_POL",
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
        "availability": [0, 0, 6, 0],
        "remove_zone_capture": None,
    },

    "PT76B_CMD_POL": {  # PT-76BD LDR
        "CommandPoints": 30,
        "GameName": {
            "display": "#LDRSOV PT-76BD LDR.",
            "token": "POLPTSSBD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_PT76B_CMD_POL",
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
        "availability": [0, 0, 8, 0],
        "remove_zone_capture": None,
    },

    "PT76B_CMD_Naval_POL": {  #  NIEB.BERETY PT-76BD LDR
        "CommandPoints": 30,
        "GameName": {
            "display": "#LDRSOV NIEB.BERETY PT-76BD LDR.",
            "token": "POLPTSSBDN",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_PT76B_CMD_Naval_POL",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                "_resolute",
                "leader_sov",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 8, 0, 0],
        "remove_zone_capture": None,
    },

    "T54B_POL": {  # T-54B
        "CommandPoints": 65,
        "availability": [10, 7, 0, 0],
         "SpecialtiesList": {
            "overwrite_all": [
            ],
        },
         "capacities": {
            "remove_capacities": [],
        },
        "ButtonTexture": "T55A_POL",
    },

    "T55A_POL": {  # T-55A
        "CommandPoints": 70,
        "availability": [10, 7, 0, 0],
        "UpgradeFromUnit": "T55A_CMD_POL",
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
        "availability": [8, 6, 0, 0],
    },
    
    "T72M1_POL": {  # T-72M1
        "CommandPoints": 175,
        "availability": [0, 6, 4, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },
    
    "T72M1_Wilk_POL": {  # T-72M2 Wilk
        "CommandPoints": 195,
        "availability": [0, 0, 4, 3],
        "SpecialtiesList": {
            "overwrite_all": ['_era', '_smoke_launcher', '_smoke_launcher'],
        },
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "WeaponDescriptor": {
            "Salves": {
                "SMOKE_Vehicle_Grenadex8": 2,
            },
        },
    },

    "ASU_85_POL": {  # ASU-85
        "CommandPoints": 60,
        "availability": [0, 8, 6, 0],
    },

    "PT76B_tank_POL": {  # PT-76B
        "CommandPoints": 25,
        "availability": [14, 11, 0, 0],
    },

     "PT76B_tank_Naval_POL": {  # NIEB.BERETY PT-76B
        "CommandPoints": 25,
        "availability": [0, 14, 11, 0],
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

    "AT_D44_85mm_POL": {  # D-44 AT 85mm
        "CommandPoints": 35,
        "availability": [9, 7, 5, 0],
        "ButtonTexture": "AT_D44_85mm_DDR",
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

    "OT_62_TOPAS_2AP_POL": {  # TOPAS-2AP
        "CommandPoints": 20,
        "capacities": {
            "add_capacities": ["IFV"],
        },
        "SpecialtiesList": {
            "overwrite_all": [
                "_transport1",
                "_ifv",
                "_amphibie",
            ],
        },
    },

    "OT_62_TOPAS_SPG9_POL": {  # TOPAS-2 SPG-9
        "CommandPoints": 25,
        "SpecialtiesList": {
            "overwrite_all": [
                "_transport1",
                "_amphibie",
            ],
        },
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
    },
    
    "Scout_para_POL": {  # Desant. Zwiadowcy
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "strength": 6,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "GameName": {
            "display": "#RECO2 SPADO. ZWIADOWCY",
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_kbk_AKM": 5,
                },
                "replace": [("FM_kbk_AKM", "FM_kbk_AK")],
                "insert": [(1, "Sniper_SVD_Dragunov")], # (turret, weapon)
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "SalvoStockIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                },
            },
        },
    },

     "Sniper_paras_POL": {  # Desant. Snajper
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "strength": 3,
        "GameName": {
            "display": "#RECO2 SPADO. SNAJPER",
        },
         "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "Sniper_SVD_Dragunov": 2,
                },
            },
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
        "GameName": {
            "display": "#RECO2 ROZP. SPECJALNE [GSR]",
        },
        "availability": [0, 0, 4, 3],
    },
    
    "Scout_LRRP_Para_POL": {  # Desant. Rozp. Specjalne [GSR]
        "CommandPoints": 65,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "GameName": {
            "display": "#RECO2 SPADO. ROZP. [GSR]",
        },
    },
    
    "Scout_SF_POL": {  # Rozp. Specjalne
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
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

    "PT76B_POL": {  # PT-76B
        "CommandPoints": 30,
        "availability": [8, 6, 0, 0],
    },
    
    "Mi_2_gunship_POL": {  # Mi-2US
        "availability": [0, 6, 4, 0],
    },
    
    "Mi_2Ro_reco_POL": {  # Mi-2Ro
        "CommandPoints": 50,
        "availability": [0, 6, 4, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_23mm_NS23": 25,
            },
        },
    },

    "W3RR_Procjon_POL": {  # W-3RR PROCJON
        "CommandPoints": 45,
        "availability": [0, 6, 0, 0],
    },
    
    #   recon tab transports
    "BMP_1_SP2_reco_POL": {  # Rozp. BWP-1
        "CommandPoints": 35,
    },
    
    "BRDM_1_POL": {  # BRDM-1
        "CommandPoints": 20,
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
        "CommandPoints": 20,
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
        "CommandPoints": 20,
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
            "display": "SPADO. STRZAŁA-2M",
        },
    },
    
    "DCA_AZP_S60_POL": {  # AZP S-60
        "CommandPoints": 35,
        "max_speed": 6,
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
        "UpgradeFromUnit": None,
    },

    "2K11_KRUG_POL": {  # 2K11 Krug
        "CommandPoints": "2K11_KRUG_SOV",
        "availability": "2K11_KRUG_SOV",
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 300,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "UpgradeFromUnit": "2K12_KUB_POL",
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
        "CommandPoints": 80,
        "GameName": {
            "display": "W-3 SOKÓŁ [RKT]"
        }
    },
    
    "W3W_Sokol_AA_POL": {  # W-3 Sokol [AA]
        "CommandPoints": 110,
        "GameName": {
            "display": "W-3 SOKÓŁ [AA]"
        }
    },
    
    "Mi_2_rocket_POL": {  # Mi-2URN Zmija
        "CommandPoints": 50,
        "availability": [8, 6, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_23mm_NS23": 25,
            },
        },
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
    
    "Mi_8MT_POL": {  # twin S-5 x32 - Mi-17 [RKT]
        "CommandPoints": 60,
        "ButtonTexture": "Mi_8T_DDR",
    },
    
    # POL AIR
    "MiG_17PF_POL": {  # Lim-6M [RKT]
        "CommandPoints": 80,
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
        "CommandPoints": "MiG_21bis_HE_DDR",
        "availability": "MiG_21bis_HE_DDR",
    },
    
    "MiG_21bis_RKT2_POL": {  # 4x S-24 [RKT2]
        "CommandPoints": "MiG_21bis_RKT2_DDR",
        "availability": "MiG_21bis_RKT2_DDR",
        "WeaponDescriptor": {
            "Salves": {
                "RocketAir_S24_240mm_avion_salvolength4": (1, True),
                # set salvo count to 1 and corresponding SalvoIsMainSalvo to True
            },
            "equipmentchanges": {
                "replace": [("RocketAir_S24_240mm_salvolength2", "RocketAir_S24_240mm_avion_salvolength4")],
            },
        },
        "GameName": {
            "display": "MiG-21bis [RKT]"
        },
    },
    
    "MiG_21bis_AT_POL": {  # 2x Kh-66, 2x R-13M
        "CommandPoints": 115,
        "availability": [0, 3, 0, 0],
    },
    
    "MiG_23MF_AA_POL": {  # MiG-23MF [AA], 2x R-23R, 4x R-60M
        "CommandPoints": "MiG_23MF_AA_DDR",
        "availability": "MiG_23MF_AA_DDR",
        "ECM": "MiG_23MF_AA_DDR",
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
            "display": "MiG-29A [AA1]",
        },
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 2, 0, 1],
    },

    "MiG_29_AA2_POL": {  # 6x R-73 [AA]
        "GameName": {
            "display": "MiG-29A [AA2]",
        },
        "CommandPoints": 170,
        "availability": [0, 3, 2, 0],
    },
    
    "Su_17_cluster_POL": { # Su-20 [CLU] - 6x RBK-500
        "CommandPoints": 180,
        "availability": [0, 2, 0, 0],
    },
    
    "Su_22_POL": {
        "CommandPoints": "Su_22_DDR",
        "availability": "Su_22_DDR",
    },

    "Su_22_nplm_POL": {  # 4x ZB-500, 2x R-60M
        "CommandPoints": 215,
        "availability": [0, 3, 0, 0],
    },
    
    "Su_22_clu_POL": {  # 4x RBK-250, 2x R-60M
        "CommandPoints": 205,
        "availability": [0, 2, 0, 0],
    },
    
    "Su_22_AT_POL": {  # Su-22M4 Seria 30
        "CommandPoints": "Su_22_AT_SOV",
        "availability": "Su_22_AT_SOV",
        "WeaponDescriptor": {
            "Salves": {
                "AGM_Kh29T": 1,
            },
        },
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
        "GameName": {
            "display": "SU-22M4 [RKT1]",
        },
    },

    "Su_22_RKT2_POL": {  # 80x S-8, 2x R-60M
        "CommandPoints": 125,
        "availability": [0, 3, 2, 0],
        "GameName": {
            "display": "SU-22M4 [RKT2]",
        },
    },
    
    "Su_22_SEAD_POL": {  # Su-22M4P [SEAD]
        "CommandPoints": 180,
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "availability": [0, 2, 0, 1],
        "Divisions": {
            "add": ["POL_20_Pancerna", "POL_4_Zmechanizowana"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 1,
            },
        },
    },
}
# fmt: off
