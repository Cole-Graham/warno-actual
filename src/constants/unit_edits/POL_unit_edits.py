"""Polish unit edits."""

# from typing import Any, Dict

pol_unit_edits = {
    # POL LOG
    "DCA_ZU_23_2_POL": {  # ZU-23-2
        "CommandPoints": 20,
        "Factory": "Factory/Logistic",
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
        
        "UpgradeFromUnit": "FOB_POL",
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm_TOWED": 20,
            },
        },
    },
    
    "DCA_ZU_23_2_Para_POL": {  # Desant. ZU-23-2
        "CommandPoints": 20,
        "GameName": {
            "display": "SPADO. ZU-23-2",
        },
        "Factory": "Factory/Logistic",
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
        "max_speed": 9,
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm_TOWED": 20,
            },
        },
        "UpgradeFromUnit": "DCA_ZU_23_2_POL",
    },
    
    "DCA_ZUR_23_2S_JOD_POL": {  # ZUR-23-2S Jod
        "CommandPoints": 30,
        "max_speed": 9,
        "availability": [9, 7, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_Jod_towed_23mm": 20,
            },
        },
        "UpgradeFromUnit": "DCA_ZPU4_POL",
    },
    
    "DCA_ZUR_23_2S_JOD_Para_POL": {  # Desant. ZUR-23-2S Jod
        "CommandPoints": 30,
        "GameName": {
            "display": "SPADO. ZUR-23-2S JOD",
        },
        "max_speed": 9,
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_Jod_towed_23mm": 20,
            },
        },
        "UpgradeFromUnit": "DCA_ZUR_23_2S_JOD_POL",
    },
    
    "UAZ_469_CMD_POL": {  # WD-43
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "GameName": {
            "display": "WD-43",
        },
        "availability": [0, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    
    "UAZ_469_CMD_Para_POL": {  # Desant. WD-43
        "CommandPoints": 145,
        "GameName": {
            "display": "SPADO. WD-43",
        },
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "TagSet": {"add_tags": ['"CMD_Unit"']},
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
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    
    "BRDM_2_CMD_POL": {  # BRDM-2U
        "CommandPoints": 155,
        "strength": 8,
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
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    
    "BRDM_2_CMD_R5_POL": {  # BRDM-2 R-5
        "CommandPoints": 170,
        "strength": 8,
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
        "TagSet": {"add_tags": ['"CMD_Unit"']},
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
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    
    "Mi_2_CMD_POL": {  # Mi-2D PRZETACZNIK
        "GameName": {"display": "Mi-2D PRZEŁĄCZNIK"},
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
        "TagSet": {"add_tags": ['"CMD_Unit"']},
    },
    
    # POL INFANTRY
    "Engineers_CMD_POL": {  # Saperzy Ldr.
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "SAPERZY",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
                "replace": {
                    "RocketInf_RPG76_Komar": {
                        "new_weapon": "MMG_PKM_7_62mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
                "quantity": {
                    "FM_kbk_AK": 8,
                },
            },
        },
        "availability": [0, 0, 5, 4],
        "max_speed": 26,
        "remove_zone_capture": None,
    },
    
    "Rifles_CMD_POL": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "PIECHOTA",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
                "RocketInf_RPG76_Komar_salvolength7": 1,
            },
        },
        "remove_zone_capture": None,
    },
    
    "MotRifles_CMD_POL": {  # Piechota Zmech. Ldr.
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "PIECHOTA ZMECH.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
                "RocketInf_RPG76_Komar_salvolength7": 1,
            },
        },
        "remove_zone_capture": None,
    },

    
    "Commandos_CMD_POL": {  # Komandosi Dow. (sp only)
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
         "GameName": {
             "display": "KOMANDOSI",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
                'leader_sov',
                '_sf',
                '_choc',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry_sf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "WeaponDescriptor": {
            "Salves": {
                "PM_PM63_RAK": 22,
                "RocketInf_RPG7VL_salvolength6": 1,
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
             "display": "SPADO. KOMANDOSI",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
                'leader_sov',
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
                "replace": {
                    "FM_Tantal": {
                        "new_weapon": "PM_PM63_RAK",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                    "MMG_PKM_7_62mm": {
                        "new_weapon": "Grenade_Satchel_Charge",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                    "RocketInf_RPG7": {
                        "new_weapon": "RocketInf_RPG76_Komar_salvolength8",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "PM_PM63_RAK": 22,
                "Grenade_Satchel_Charge": 6,
                "RocketInf_RPG76_Komar_salvolength8": 1,
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
            "display": "SPADO. SAPERZY",
        },
         "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
                "replace": {
                    "FM_kbk_AKM": {
                        "new_weapon": "FM_kbk_AK",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                    "RocketInf_RPG76_Komar": {
                        "new_weapon": "RocketInf_RPG7_salvolength6",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "RocketInf_RPG7_salvolength6": 1,
            },
        },
        "remove_zone_capture": None,
    },

    "Para_CMD_POL": {  # Dow. SPADOCHRONIARZE 
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "strength": 7,
        "GameName": {
            "display": "SPADOCHRONIARZE",
        },
         "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
                'leader_sov',
                '_choc',
                '_para',
                'infantry_equip_medium',
            ],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_Tantal": 7,
                },
                "replace": {
                    "FM_kbk_AKM": {
                        "new_weapon": "FM_Tantal",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "RocketInf_RPG7_salvolength6": 1,
            },
        },
        "remove_zone_capture": None,
    },
    
    "Reserve_CMD_POL": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
         "GameName": {
            "display": "REZERWIŚCI DOW."
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
            },
        },
        "remove_zone_capture": None,
    },

    "Naval_Rifle_CMD_POL": {  # Dow. Nieb Berety
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "strength": 12,
         "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Standard",
                "UNITE_Naval_Rifle_CMD_POL",
                "Unite",
            ],
        },
        "GameName": {
            "display": "NIEBIESKIE BERETY",
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "capacities": {
            "remove_capacities": [
                "Choc",
                "Choc_feedback",
            ],
        },
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_resolute',
                'infantry_equip_medium',
            ],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_kbk_AK": 12,
                },
                "replace": {
                    "RocketInf_RPG76_Komar": {
                        "new_weapon": "RocketInf_RPG7VL_salvolength9",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "RocketInf_RPG76_Komar": 9,
            },
        },
        "DeploymentShift": 1750,
        "remove_zone_capture": None,
    },

    "Naval_Engineers_CMD_POL": {  # NIEB. BERETY SAPERZY Dow.
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "strength": 6,
        "GameName": {
            "display": "NIEB. BERETY SAPERZY",
        },
         "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Naval_Engineers_CMD_POL",
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
                "_resolute",
                "infantry_equip_light",
            ],
        },
       "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_kbk_AK": 6,
                },
            },
        },
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
        "WeaponDescriptor": {
            "Salves": {
                "Grenade_Satchel_Charge": 6,
            },
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
    
    "Engineers_Reserve_POL": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
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
                "MMG_PKM_7_62mm": 36,
            },
        },
        # 8x kbk AKM
        # 1x PKM
        # RPO Rys x6
    },

    "Engineers_paras_POL": {  # Desant. Saperzy
        "CommandPoints": 50,
        "GameName": {
            "display": "SPADO. SAPERZY",
        },
        "availability": [0, 6, 4, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_kbk_AKM": {
                        "new_weapon": "FM_kbk_AK",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "insert": [(3, "RocketInf_RPG7")],
                "insert_edits": {
                    3: {
                        "turret_edits": {
                            "YulBoneOrdinal": 4,
                        },
                        "AmmoBoxIndex": 3,
                        "HandheldEquipmentKey": "'WeaponAlternative_4'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_4'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_4'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_4"],
                    },
                },
            },
            "Salves": {
                "insert": [(3, 6)],
                "Grenade_Satchel_Charge": 6,
            },
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
                "replace": {
                    "FM_kbk_AKM": {
                        "new_weapon": "FM_kbk_AK",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
                "quantity": {
                    "FM_kbk_AK": 7,
                    "flamethrower_LPO": 2,
                },
            },
            "Salves": {
                "flamethrower_LPO": 30,
            },
        },
        "GameName": {
            "display": "SPADO. SAPERZY [FLAM]",
        },
    },

    "Naval_Engineers_POL": {  # Nieb. Berety Saperzy
        "CommandPoints": 50,
        "availability": [0, 6, 4, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Naval_Engineers_Flam_POL": {  # Nieb. Berety Saperzy (LPO-50)
        "CommandPoints": 55,
        "availability": [0, 6, 4, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "flamethrower_LPO": 30,
            },
        },
        "UpgradeFromUnit": "Naval_Engineers_POL",
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
                "RocketInf_RPG7VL_salvolength5": 1,
            },
        },
        "UpgradeFromUnit": "MotRifles_SVD_POL",
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
                "RocketInf_RPG7VL_salvolength5": 1,
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
    },
    
    "Rifles_HMG_POL": {  # Piechota (SVD)
        "CommandPoints": 40,
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
            "equipmentchanges": {
                "replace": {
                    "RocketInf_RPG7": {
                        "new_weapon": "RocketInf_RPG7VL",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
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
        "CommandPoints": 35,
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
            "equipmentchanges": {
                "replace": {
                    "RocketInf_RPG7": {
                        "new_weapon": "RocketInf_RPG7VL",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
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
                "replace": {
                    "FM_kbk_AKM": {
                        "new_weapon": "FM_Tantal",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                    "SAW_RPK_7_62mm": {
                        "new_weapon": "SAW_RPK_74_5_56mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                    "RocketInf_RPG7": {
                        "new_weapon": "RocketInf_RPG7VL",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "FM_kbk_AKM": 11,
                "SAW_RPK_7_62mm": 24,
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
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_kbk_AKM": {
                        "new_weapon": "FM_Tantal",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                    "SAW_RPK_7_62mm": {
                        "new_weapon": "SAW_RPK_74_5_56mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "FM_Tantal": 11,
                "SAW_RPK_74_5_56mm": 24,
            },
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
                "replace": {
                    "FM_kbk_AKM": {
                        "new_weapon": "FM_Tantal",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                    "RocketInf_RPG76_Komar": {
                        "new_weapon": "RocketInf_RPG7_salvolength6",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "RocketInf_RPG7_salvolength6": 1,
            },
        },
        # 6x kbk AKM
        # 3x PKM
        # RPG-7VM x6
    },
    
    "Naval_Rifle_POL": {  # Niebeskie Berety
        "CommandPoints": 40,
        "availability": [10, 7, 0, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "overwrite_all": [
                "_resolute",
                "infantry_equip_medium",
            ],
        },
        "capacities": {
            "remove_capacities": [
                "Choc",
                "Choc_feedback",
            ],
        },
        "DeploymentShift": 1750,
        # 10x kbk AKM
        # 2x PKM
        # RPG-7VM x6
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
        "WeaponDescriptor": {
            "Salves": {
                "PM_PM63_RAK": 22,
            },
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
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_kbk_AKM": {
                        "new_weapon": "FM_kbk_AK",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                    "SAW_RPK_74_5_56mm": {
                        "new_weapon": "SAW_RPK_7_62mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "RocketInf_RPG76_Komar_salvolength7": 1,
            },
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
            "add_specs": ["'infantry_equip_medium'"],
        },
        "GameName": {
            "display": "REZERWIŚCI"
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_PKM_7_62mm": False,
                },
                "quantity": {
                    "FM_kbk_AK": 10,
                    "MMG_PKM_7_62mm": 2,
                },
            },
        },
    },
    
    "Reserve_SVD_POL": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [12, 0, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "GameName": {
            "display": "REZERWIŚCI [SVD]"
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
                "replace": {
                    "Canon_HEAT_73_mm_SPG9_TOWED": {
                        "new_weapon": "Canon_HEAT_73_mm_SPG9D_TOWED",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
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
                "replace": {
                    "ATGM_9K111M_Faktoriya": {
                        "new_weapon": "ATGM_9K111_Fagot",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
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
    
    "UAZ_452_MP_POL": {
        "CommandPoints": 20,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "LO_1800_trans_POL": {
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 60,
        "GameName": {
            "display": "TOPAS R-2M",
            "token": "TOPASARTLD", # Don't remove or logistic tab version will get renamed as well
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_OT_62_TOPAS_R3M_CMD_POL",
                "Unite",
                "Vehicule",
            ],
        },
        "Factory": "Factory/Art",
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
    
    "BM24M_POL": {
        "CommandPoints": "BM24M_SOV",
    },
    
    "RM70_85_POL": {
        "CommandPoints": 240,
        "GameName": {
            "display": "RM wz. 70/85"
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "RocketArt_M21OF_122mm": {
                        "new_weapon": "RocketArt_M21OF_122mm_RM70",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
        "availability": [0, 2, 0, 1],
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
    #        "display": "#LDRSOV T-34/85MD",
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
    #         "display": "#LDRSOV T-54BD",
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
        "capacities": {
            "add_capacities": ["LDR_TNK", "Reload_Penalty"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 70,
        "GameName": {
            "display": "T-55AD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
        "capacities": {
            "add_capacities": ["LDR_TNK", "Reload_Penalty"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 110,
        "GameName": {
            "display": "T-55AD-1M Merida",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 140,
        "armor": {
            "top": (2, None),
        },
        "GameName": {
            "display": "T-72MD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 185,
        "armor": {
            "top": (3, None),
        },
        "GameName": {
            "display": "T-72M1D",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
        "capacities": {
            "add_capacities": ["LDR_TNK", "Reload_Penalty"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 60,
        "GameName": {
            "display": "ASU-85D",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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

    "PT76B_CMD_POL": {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
  # Turned into reco PT-76
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 30,
        "GameName": {
            "display": "PT-76B",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_Reco",
                "GroundUnits",
                "Radio",
                "Reco",
                "UNITE_PT76B_CMD_POL",
                "Unite",
            ],
        },
        "stealth": 1.5,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 3500,
                "EVisionRange/LowAltitude": 4947,
                "EVisionRange/HighAltitude": 5654,
            },
            "OpticalStrengths": {
                "EOpticalStrength/Standard": 5300,
                "EOpticalStrength/LowAltitude": 5300,
                "EOpticalStrength/HighAltitude": 1413,
            },
        },
        "Factory": "Factory/Recons",
        "IdentifiedTextures": ["Texture_RTS_H_reco", "Texture_reco"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "MenuIconTexture": "Texture_RTS_H_reco",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Reco",
        "ButtonTexture": "PT76B_POL",
        "UnitRole": "reco",
        "SpecialtiesList": {
            "overwrite_all": [
                "_amphibie",
            ],
        },
        "availability": [0, 8, 6, 0],
        "remove_zone_capture": None,
        "DeploymentShift": 750,
        "UpgradeFromUnit": None,
    },

    "PT76B_CMD_Naval_POL": {  #  NIEB.BERETY PT-76BD LDR
        "capacities": {
            "add_capacities": ["LDR_TNK", "Reload_Penalty"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 30,
        "GameName": {
            "display": "NIEB.BERETY PT-76BD",
            "token": "POLPTSSBDN",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
        "CommandPoints": 70,
        "availability": [10, 7, 0, 0],
        "SpecialtiesList": {
            "overwrite_all": [
            ],
        },
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
            "remove_capacities": ["resolute"],
        },
        "ButtonTexture": "T55A_POL", 
        "UpgradeFromUnit": "T54B_CMDactual_POL",
    },

    "T55U_POL": {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
  # T-55A
        "CommandPoints": 65,
        "availability": [10, 7, 0, 0],
        "UpgradeFromUnit": "T55A_CMD_POL",
    },

    "T55A_POL": {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
  # T-55A
        "CommandPoints": 70,
        "availability": [10, 7, 0, 0],
        "UpgradeFromUnit": "T55A_CMD_POL",
    },
    
    "T55AS_POL": {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
  # T-55AS coffin launcher
        "CommandPoints": 85,
        "availability": [0, 4, 3, 0],
    },
    
    "T55AM_Merida_POL": {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
  # T-55AM Merida
        "CommandPoints": 110,
        "availability": [0, 8, 6, 0],
    },
    
    "T55AMS_Merida_POL": {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
  # T-55AMS Merida coffin launcher
        "CommandPoints": 140,
        "availability": [0, 3, 2, 0],
    },
    
    "T72M_POL": {  # T-72M
        "CommandPoints": 140,
        "armor": {
            "top": (2, None),
        },
        "availability": [8, 6, 0, 0],
    },
    
    "T72M1_POL": {  # T-72M1
        "CommandPoints": 175,
        "armor": {
            "top": (3, None),
        },
        "availability": [0, 6, 4, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },
    
    "T72M1_Wilk_POL": {  # T-72M2 Wilk
        "CommandPoints": 210,
        "armor": {
            "top": (4, None),
        },
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

    "ASU_85_POL": {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
  # ASU-85
        "CommandPoints": 60,
        "availability": [0, 8, 6, 0],
    },

    "PT76B_tank_POL": {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
  # PT-76B
        "CommandPoints": 25,
        "availability": [14, 11, 0, 0],
    },

    "PT76B_tank_Naval_POL": {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
  # NIEB.BERETY PT-76B
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
                "ATGM_9K111M_Faktoriya": "LUAZ_967M_Fagot_SOV",
            },
        },
        "availability": [10, 7, 0, 0],
    },
    
    "UAZ_469_Fagot_Para_POL": {  # Desant./Spado. UAZ-469 Fagot/Faktoria
        "CommandPoints": 35,
        "availability": [0, 10, 7, 0],
        "GameName": {
            "display": "SPADO. UAZ-469 FAKTORIA",
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": "LUAZ_967M_Fagot_SOV",
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
        "CommandPoints": 15,
        "strength": 10,
    },
    
    "OT_64_SKOT_2A_POL": {  # SKOT-2A
        "CommandPoints": 20,
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
    
    "OT_64_SKOT_2P_POL": {  # SKOT-2AP
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

    "OT_62_TOPAS_POL": {  # TOPAS-2
        "CommandPoints": 15,
        "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
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
    
    "BMP_1_SP2_POL": {  # BWP-1 (Malyutka, no smoke)
        "CommandPoints": "BMP_1_SP2_SOV",
        "UpgradeFromUnit": "MTLB_trans_POL",
    },
    
    "BMP_2_POL": {  # BWP-2
        "CommandPoints": "BMP_2_SOV",
    },
    
    # POL RECON
    "HvyScout_POL": {  # Zmot. Zwiad.
        "GameName": {
            "display": "ZWIADOWCY ZMOT.",
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
        "UpgradeFromUnit": "Scout_POL",
    },
    
    "Engineers_Scout_POL": {  # Saperzy Zwiadowcy
        "GameName": {
            "display": "SAPERZY ZWIAD.",
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
        "UpgradeFromUnit": "HvyScout_POL",
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
                "PM_PM63_RAK": 22,
                "RocketInf_RPG7_salvolength4": 1,
            },
        },
        "UpgradeFromUnit": "Scout_Reserve_POL",
    },
    
     "Scout_Reserve_POL": {  # Rez. Zwiadowcy
        "armor": "Infantry_armor_reference",
        "CommandPoints": 20,
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
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
            "display": "SPADO. ZWIADOWCY",
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_Tantal": 5,
                },
                "replace": {
                    "FM_kbk_AKM": {
                        "new_weapon": "FM_Tantal",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                        "old_new_effect": ("FM_kbk_AKM", "FM_Tantal"),
                    },
                    "RocketInf_RPG76_Komar": {
                        "new_weapon": "Sniper_SVD_Dragunov",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                        "old_new_effect": ("RocketInf_RPG76_Komar", "Sniper_SVD_Dragunov"),
                    },
                },
                "insert": [(2, "RocketInf_RPG76_Komar")], # (turret, weapon)
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
                "Sniper_SVD_Dragunov": 10,
                "insert": [(2, 6)],
            },
        },
    },

    "Sniper_POL": {  # Snajper
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "WeaponDescriptor": {
            "Salves": {
                "PM_PM63_RAK": 22,
            },
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },

    "Sniper_paras_POL": {  # Spado. Snajper
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "strength": 3,
        "GameName": {
            "display": "SPADO. SNAJPER",
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "Sniper_SVD_Dragunov_double": False,
                },
                "quantity": {
                    "Sniper_SVD_Dragunov_double": 2,
                },
                "replace": {
                    "Sniper_SVD_Dragunov": {
                        "new_weapon": "Sniper_SVD_Dragunov_double",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "PM_PM63_RAK": 22,
            },
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "UpgradeFromUnit": "Sniper_POL",
    },
    
    "Scout_LRRP_POL": {  # Rozp. Specjalne [GSR]
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "strength": 4,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_PM63_RAK": 4,
                },
            },
            "Salves": {
                "PM_PM63_RAK": 22,
                "RocketInf_RPG76_Komar_salvolength4": 1,
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
            "display": "ROZP. SPECJALNE [GSR]",
        },
        "availability": [0, 0, 4, 3],
        "UpgradeFromUnit": "Scout_SF_POL",
    },
    
    "Scout_LRRP_Para_POL": {  # Desant. Rozp. Specjalne [GSR]
        "CommandPoints": 65,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "GameName": {
            "display": "SPADO. ROZP. [GSR]",
        },
        "WeaponDescriptor": {
            "Salves": {
                "PM_PM63_RAK": 22,
            },
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
                "PM_PM63_RAK": 22,
                "RocketInf_RPG7VL_salvolength4": 1,
            },
        },
    },

    "Commandos_Marine_POL": {  # Formoza, this maybe should be 70? Based the Price off of the Spetz Gru Stinger. Formza is better in CQC, and has worse ATGM
        "CommandPoints": 65,
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "availability": [0, 0, 0, 3],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "Scout_LRRP_Para_POL",
    },

    # TODO: Find out what happened to this unit
    # "Scout_SF_Para_POL": {  # Desant. Rozp. Specjalne
    #     "GameName": {
    #         "display": "SPADO. ROZP. SPECJALNE",
    #     },
    # },
    
    "UAZ_469_Reco_POL": {
        "CommandPoints": 25,
        "UpgradeFromUnit": "Honker_RYS_POL",
    },
    
    "BRDM_1_DShK_POL": {
        "CommandPoints": 30,
        "availability": [12, 9, 0, 0],
        "UpgradeFromUnit": None,
    },
    
    "BRDM_1_PSNR1_POL": {  # BRDM-1 PSNR-1
        "CommandPoints": 35,
        "availability": [8, 0, 0, 0],
        "UpgradeFromUnit": "MTLB_Taran_SIGINT_POL",
    },
    
    "BRM_1_POL": {  # BWR-1D
        "CommandPoints": "BRM_1_SOV",
        "availability": "BRM_1_SOV",
    },
    
    "BRDM_2_POL": {  # BRDM-2
        "CommandPoints": "BRDM_2_SOV",
        "availability": "BRDM_2_SOV",
        "strength": 8,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "UpgradeFromUnit": "BRDM_1_DShK_POL",
    },

    "MTLB_Taran_SIGINT_POL": {  # R-330T Taran
        "CommandPoints": "MTLB_Taran_SIGINT_SOV",
        "availability": "MTLB_Taran_SIGINT_SOV",
    },

    "SNAR_10_POL": {  # SNAR-10 (Counter Battery Radar)
        "CommandPoints": "SNAR_10_SOV",
        "availability": "SNAR_10_SOV",
    },

    "PT76B_POL": {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
  # PT-76B
        "CommandPoints": "PT76B_Naval_SOV",
        "availability": [8, 6, 0, 0],
    },
    
    "Mi_2_gunship_POL": {  # Mi-2US 4x PKT
        "CommandPoints": "Mi_2_gunship_DDR",
        "availability": [0, 6, 4, 0],
        "UpgradeFromUnit": None,
    },
    
    "Mi_2Ro_reco_POL": {  # Mi-2Ro
        "CommandPoints": 50,
        "availability": [0, 6, 4, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_23mm_NS23": 25,
            },
        },
        "UpgradeFromUnit": "Mi_2_gunship_POL",
    },

    "W3RR_Procjon_POL": {  # W-3RR PROCJON
        "CommandPoints": 50,
        "availability": [0, 6, 0, 0],
        "UpgradeFromUnit": "Mi_2Ro_reco_POL",
    },
    
    "W3W_Sokol_RKT_POL": {  # W-3 Sokol
        "CommandPoints": 80,
        "GameName": {
            "display": "W-3 SOKÓŁ"
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Helo",
                "Helo_Reco",
                "Radio",
                "Reco",
                "UNITE_W3W_Sokol_RKT_POL",
                "Unite",
            ],
        },
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 3500,
                "EVisionRange/LowAltitude": 4947,
                "EVisionRange/HighAltitude": 8481,
            },
            "OpticalStrengths": {
                "EOpticalStrength/Standard": 5300,
                "EOpticalStrength/LowAltitude": 5300,
                "EOpticalStrength/HighAltitude": 2826,
            },
        },
        "IdentifiedTextures": ["Texture_RTS_H_RECO_hel", "Texture_RECO_hel"],
        "UnidentifiedTextures": ["Texture_RTS_H_hel_nonIdentifie", "Texture_hel_nonIdentifie"],
        "Factory": "Factory/Recons",
        "UpgradeFromUnit": "W3RR_Procjon_POL",
        "UnitRole": "reco",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Reco_Hel",
        "DeploymentShift": 750,
    },
    
    #   recon tab transports
    "BMP_1_SP2_reco_POL": {  # Rozp. BWP-1
        "CommandPoints": "BMP_1P_reco_DDR",
        "UpgradeFromUnit": "MTLB_TRI_Hors_POL", # PT76B_CMD is reco PT76 now
    },
    
    "BRDM_1_POL": {  # BRDM-1
        "CommandPoints": 20,
        "UpgradeFromUnit": "OT_65_POL",
    },
    
    "OT_65_POL": {  # OT-65
        "CommandPoints": 15,
        "GameName": {
            "display": "OT-65",
        },
        "UpgradeFromUnit": None,
    },
    
    "MTLB_TRI_Hors_POL": {  # TRI Hors
        "CommandPoints": 20,
        "UpgradeFromUnit": None,
    },
    
    "Honker_RYS_POL": {  # Honker Rys
        "CommandPoints": 25,
    },
    
    # POL AA
    "MANPAD_Strela_2M_POL": {  # Strzala-2M
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [12, 9, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_kbk_AK": {
                        "new_weapon": "FM_kbk_AK_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "FM_kbk_AK_noreflex": 9,
            },
        },
    },
    
    "MANPAD_Strela_2M_Naval_POL": {  # Desant. Strzala-2M
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_kbk_AK": {
                        "new_weapon": "FM_kbk_AK_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "FM_kbk_AK": 9,
            },
        },
        "GameName": {
            "display": "NIEB. BERETY STRZAŁA-2M",
        },
    },
    
    "MANPAD_Strela_2M_Para_POL": {  # Desant. Strzala-2M
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_kbk_AKM": {
                        "new_weapon": "FM_kbk_AK",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "FM_kbk_AK": 9,
            },
        },
        "GameName": {
            "display": "SPADO. STRZAŁA-2M",
        },
    },

    "DCA_ZPU4_POL": {
        "CommandPoints": 20,
        "availability": [12, 9, 0, 0],
        "max_speed": 6,
        
        "WeaponDescriptor": {
            "Salves": {
                "DCA_4_canon_ZPU4_towed_14_5mm": 160,
            },
        },
    },
    
    "DCA_AZP_S60_POL": {  # AZP S-60
        "CommandPoints": "DCA_AZP_S60_SOV",
        "max_speed": "DCA_AZP_S60_SOV",
        "availability": "DCA_AZP_S60_SOV",
        "TagSet": {
            "add_tags": ['"AA_radar"'],
        },
        
        "WeaponDescriptor": {
            "Salves": {
                "DCA_1_canon_S60_57mm_radar": 1,
            },
            "equipmentchanges": {
                "replace": {
                    "DCA_1_canon_S60_57mm": {
                        "new_weapon": "DCA_1_canon_S60_57mm_radar",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "UpgradeFromUnit": "DCA_ZUR_23_2S_JOD_Para_POL",
    },
    
    "LO_1800_ZPU_2_POL": {  # Lo-1800 ZPU-2
        "CommandPoints": 30,
        "availability": [12, 9, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZPU4_14_5mm": 192,
            },
        },
    },
    
    "OT_62_TOPAS_JOD_POL": { # TOPAS JOD (Transport)
        "CommandPoints": 40,
    },

    "Hibneryt_POL": {  # Hibneryt
        "CommandPoints": 40,
        "availability": [7, 5, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm": 25,
            },
        },
    },
    
    "Hibneryt_KG_POL": {  # Hibneryt KG
        "CommandPoints": 50,
        "availability": [6, 4, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_Jod_SP_23mm": 25,
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
                "EOpticalStrength/HighAltitude": 7800,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
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
                "EOpticalStrength/HighAltitude": 7800,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
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
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "DCA_4_canons_APZ23_23mm": {
                        "new_weapon": "DCA_4_canons_AZP_23_Amur_23mm_late",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
            "Salves": {
                "DCA_4_canons_AZP_23_Amur_23mm_late": 67,
            },
        },
    },
    
    "Osa_9K33M3_POL": {  # PWRB Osa-AKM
        "CommandPoints": 130,
        "GameName": {
            "display": "9K33M3 ROMB",  # wargame reference
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "strength": 10,
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
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "strength": 10,
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
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "strength": 10,
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "UpgradeFromUnit": "2K12_KUB_POL",
    },
    
    # POL HELI
    "Mi_24D_POL": {  # 64x S-5, 4x Falanga - Mi-24D [AT] -> transport
        "XP": {
            "pack": "helico_attack",
        },
        "GameName": {
            "display": "Mi-24D SPADO."
        },
        "CommandPoints": 130,
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
        "strength": "Mi_24P_SOV",
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
    },
    
    "Mi_24D_s8_AT_POL": {  # 80x S-8, 4x Falanga - Mi-24D [AT2]
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 150,
        "strength": "Mi_24P_SOV",
        "availability": [0, 4, 3, 0],
        "GameName": {
            "display": "Mi-24D [AT]"
        },
    },
    
    "Mi_24V_POL": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": "Mi_24V_AT_SOV",
        "strength": "Mi_24P_SOV",
        "availability": "Mi_24V_AT_SOV",
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
    
    "Mi_8T_POL": {  # 32 S-5M x2 (introduced with 15. Zmech)
        "CommandPoints": "Mi_8TV_SOV",
    },
    
    "Mi_8MT_POL": {  # THIS IS A EAST GERMAN MODEL... POL might not even have procured the Mi-17
        "CommandPoints": 50,
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
        "CommandPoints": 130,
        "ECM": -0.15,
        "availability": [0, 4, 3, 2],
        "GameName": {
            "display": "MiG-21bis [AA2]"
        },
    },
    
    "MiG_21bis_POL": {  # 4x R-60M, 2x R-13M - MiG-21bis [AA2]
        "CommandPoints": 120,
        "ECM": -0.15,
        "availability": [0, 4, 3, 2],
        "GameName": {
            "display": "MiG-21bis [AA]"
        },
    },
    
    "MiG_21bis_HE_POL": {  # MiG-21bis [HE]
        "CommandPoints": 145,
        "ECM": -0.15,
        "availability": [0, 4, 0, 0],
    },
    
    "MiG_21bis_RKT2_POL": {  # 4x S-24 [RKT2]
        "CommandPoints": 110,
        "ECM": -0.15,
        "availability": [0, 4, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketAir_S24_240mm_avion_salvolength4": (1, True),
                # set salvo count to 1 and corresponding SalvoIsMainSalvo to True
            },
            "equipmentchanges": {
                "replace": {
                    "RocketAir_S24_240mm_salvolength2": {
                        "new_weapon": "RocketAir_S24_240mm_avion_salvolength4",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
        "GameName": {
            "display": "MiG-21bis [RKT]"
        },
    },
    
    "MiG_21bis_AT_POL": {  # 2x Kh-66, 2x R-13M
        "CommandPoints": 160,
        "ECM": -0.25,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 4550.0,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMaxPitch": 1.047198, # 60 degrees
                    "AngleRotationMinPitch": -1.047198,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 3, 0, 0],
        "UpgradeFromUnit": "MiG_21bis_HE_POL",
    },
    
    "MiG_23MF_AA_POL": {  # MiG-23MF [AA], 2x R-23R, 4x R-60M
        "CommandPoints": 115,
        "availability": [0, 4, 3, 2],
        "ECM": -0.15,
    },
    
    "MiG_23MF_AA2_POL": {  # MiG-23MF [AA2], 2x R-3R, 2x R-13M
        "CommandPoints": 110,
        "ECM": -0.15,
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
        "CommandPoints": "MiG_29_AA_DDR",
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "availability": [0, 3, 2, 0],
    },

    "MiG_29_AA2_POL": {  # 6x R-73 [AA]
        "GameName": {
            "display": "MiG-29A [AA2]",
        },
        "CommandPoints": 165,
        "SpecialtiesList": {
            "add_specs": ["'_hmd'"],
        },
        "availability": [0, 3, 2, 0],
    },
    
    "Su_7BKL_RKT_POL": {
        "CommandPoints": 110,
        "ECM": -0.05,
        "availability": [0, 3, 0, 0],
    },

    "Su_7BKL_EW_POL": {
        "CommandPoints": 130,
        "ECM": -0.25,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 3, 0, 0],
    },

    "Su_7BKL_HE_POL": {
        "CommandPoints": 185,
        "ECM": -0.15,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 3, 0, 0],
    },

    "Su_7BKL_NPLM_POL": {
        "CommandPoints": 175,
        "ECM": -0.05,
        "availability": [0, 4, 0, 0],
    },
    
    "Su_17_cluster_POL": { # Su-20 [CLU] - 6x RBK-500
        "CommandPoints": 190,
        "ECM": -0.15,
        "availability": [0, 2, 0, 0],
    },
    
    "Su_22_POL": { # Su-22M4 [HE]
        "CommandPoints": "Su_22_DDR",
        "ECM": -0.30,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "Su_22_nplm_POL": {  # 4x ZB-500, 2x R-60M
        "CommandPoints": 190,
        "ECM": -0.20,
        "availability": [0, 3, 0, 0],
    },
    
    "Su_22_clu_POL": {  # 4x RBK-250, 2x R-60M
        "CommandPoints": "Su_22_nplm_DDR",
        "ECM": -0.20,
        "availability": [0, 2, 0, 0],
    },
    
    "Su_22_AT_POL": {  # Su-22M4 Seria 30
        "CommandPoints": "Su_22_AT_SOV",
        "ECM": "Su_22_AT_SOV",
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": "Su_22_AT_SOV",
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
    },
    
    "Su_22_RKT_POL": {  # 4x S-24, 2x R-60M
        "CommandPoints": 115,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "ECM": -0.20,
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketAir_S24_240mm_avion_salvolength4": 1,
            },
            "equipmentchanges": {
                "replace": {
                    "RocketAir_S24_240mm_salvolength2": {
                        "new_weapon": "RocketAir_S24_240mm_avion_salvolength4",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
        "GameName": {
            "display": "SU-22M4 [RKT1]",
        },
    },

    "Su_22_RKT2_POL": {  # 80x S-8, 2x R-60M
        "CommandPoints": 115,
        "GameName": {
            "display": "SU-22M4 [RKT2]",
        },
        "ECM": -0.20,
        "availability": [0, 3, 2, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketAir_B8_80mm_salvolength40": 2,
            },
            "equipmentchanges": {
                "replace": {
                    "RocketAir_B8_80mm_salvolength80": {
                        "new_weapon": "RocketAir_B8_80mm_salvolength40",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },
    
    "Su_22_RKT3_POL": {  # 4x S-25O
        "CommandPoints": 140,
        "ECM": -0.30,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
    },
    
    "Su_22_SEAD_POL": {  # Su-22M4P [SEAD]
        "CommandPoints": 180,
        "ECM": -0.40,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 175000.0,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "AngleRotationMax": 0.9599311,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 3, 0, 2],
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
