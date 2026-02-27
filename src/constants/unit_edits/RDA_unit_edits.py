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
    
    "MTLB_CMD_DDR": {
        "CommandPoints": 145,
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
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

    "Mi_2_CMD_DDR": {  # Mi-2D
        "GameName": {"display": "#CMD Mi-2D"},
        "CommandPoints": 115,
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 3, 0, 0],
    },

    "Mi_9_DDR": {  # Mi-19D
        "GameName": {"display": "#CMD Mi-19"},
        "CommandPoints": 145,
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 3, 0, 0],
    },

    # RDA INF
    "MotRifles_CMD_DDR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV MOT.-SCHUTZEN FÜR. LDR.",
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

    "Engineers_Naval_CMD_DDR": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV MARINEPIONIER FÜR. LDR.",
            "token": "UPIUDWZHAI",
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
                "UNITE_Engineers_Naval_CMD_DDR",
                "Unite"
            ],
        },
        "strength": 12,
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_choc',
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
                    "FM_KMS_72": 12,
                },
            },
            "Salves": {
                "FM_KMS_72": 11,
                "RocketInf_RPG7": 6,
            },
        },
        "selector_tactic": "(0, 1)",
        "selector_tactic_obj": "00_01",
        "remove_zone_capture": None,
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
                        "AmmoBoxIndex": 1,
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
    
    "Fallschirmjager_CMD_DDR": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV FALLSCHIRM FÜR. LDR.",
            "token": "BFPSSUUCFZ",
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
                "UNITE_Fallschirmjager_CMD_DDR",
                "Unite",
                "noSIGINT",
            ],
        },
        "strength": 9,
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
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_lMG_K_7_62mm": False,
                },
                "quantity": {
                    "FM_Mpi_AKS_74NK": 7,
                    "SAW_lMG_K_7_62mm": 2,
                },
                "insert": [(1, "SAW_lMG_K_7_62mm")],
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
            "Salves": {
                "insert": [(3, 4)],
                "RocketInf_RPG18_64mm": 7,
                "FM_Mpi_AKS_74NK": 11,
                "SAW_lMG_K_7_62mm": 92,
            },
        },
        "selector_tactic": "(2, 4)",
        "selector_tactic_obj": "02_04",
        "remove_zone_capture": None,
    },

    "Luftsturmjager_CMD_DDR": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV LUFTSTURM-JÄGER FÜR. LDR.",
            "token": "IBYSOQOQYU",
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
                "UNITE_Luftsturmjager_CMD_DDR",
                "Unite",
                "noSIGINT",
            ],
        },
        "strength": 9,
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
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "SAW_lMG_K_7_62mm": False,
                },
                "quantity": {
                    "FM_Mpi_AKS_74NK": 7,
                    "SAW_lMG_K_7_62mm": 2,
                },
                "insert": [(1, "SAW_lMG_K_7_62mm")],
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
            "Salves": {
                "insert": [(3, 4)],
                "RocketInf_RPG18_64mm": 7,
                "FM_Mpi_AKS_74NK": 11,
                "SAW_lMG_K_7_62mm": 92,
            },
        },
        "selector_tactic": "(2, 4)",
        "selector_tactic_obj": "02_04",
        "remove_zone_capture": None,
    },

    "Wachregiment_CMD_DDR": {
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV WACHSCHÜTZEN FÜH. LDR.",
            "token": "ZMOICNFUWP",
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
                "UNITE_Wachregiment_CMD_DDR",
                "Unite"
            ],
        },
        "strength": 10,
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_choc',
                '_resolute',
                '_security',
                'infantry_equip_heavy',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 4, 3],
        "max_speed": 20,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_Skorpion": 5,
                    "FM_StG_941": 5,
                },
            },
        },
        "selector_tactic": "(1, 3)",
        "selector_tactic_obj": "01_03",
        "remove_zone_capture": None,
    },

    "Fallschirmjager_FalseFlag_CMD_DDR": {
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV FALLSCHIRM FÜR. FF LDR.",
            "token": "AKEYFQLRBG",
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
                "UNITE_Fallschirmjager_FalseFlag_CMD_DDR",
                "Unite",
                "noSIGINT",
            ],
        },
        "strength": 8,
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
                '_falseflag'
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry_sf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 0, 3],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "SAW_M249_5_56mm"), (3, "Grenade_SMOKE")],
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
                "quantity": {
                    "FM_M16": 6,
                    "SAW_M249_5_56mm": 2,
                },
            },
            "Salves": {
                "insert": [(1, 23), (3, 3)],
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "remove_zone_capture": None,
    },

    "Volkspolizei_CMD_DDR": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDRSOV VOPOS FÜH. LDR.",
            "token": "VXWUPWYFCP",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Volkspolizei_CMD_DDR",
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
                '_security',
                '_militia',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 7, 0, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "RocketInf_RPG18_64mm"), (2, "Grenade_SMOKE")],
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AnimateOnlyOneSoldier": True,
                        "NbWeapons": 1,
                        "SalvoStockIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
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
                "quantity": {
                    "PM_Skorpion": 6,
                },
            },
            "Salves": {
                "insert": [(1, 7), (2, 3)],
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "remove_zone_capture": None,
    },

    "Reserve_DDR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_medium'"],
        },
    },

    "Reserve_DDR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_medium'"],
        },
    },
    
    "Reserve_HMG_DDR": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_light'"],
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

     "Volkspolizei_DDR": {
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "RocketInf_RPG18_64mm")],
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AnimateOnlyOneSoldier": True,
                        "NbWeapons": 1,
                        "SalvoStockIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                },
            },
            "Salves": {
                "insert": [(1, 7)],
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
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
                "RocketInf_RPG7VL": 6,
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

    "MotRifles_HMG_DDR": {
        "GameName": {
            "display": "MOT.-SCHÜTZEN [s.MG]",
        },
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPG18_64mm": 7,
            },
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

    "MotRifles_Metis_DDR": {
        "GameName": {
            "display": "MOT.-SCHÜTZEN [METIS]",
        },
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
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

    "MotRifles_Strela_DDR": {
        "GameName": {
            "display": "MOT.-SCHÜTZEN [STRELA]",
        },
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_Mpi_AK_74N": 11,
                "RocketInf_RPG18_64mm": 7,
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

    "Fallschirmjager_DDR": {
        "GameName": {
            "display": "FALLSCHIRMJÄGER",
        },
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "strength": 9,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
             "equipmentchanges": {
                "animate": {
                    "SAW_lMG_K_7_62mm": False,
                },
                "quantity": {
                    "FM_Mpi_AKS_74NK": 7,
                    "SAW_lMG_K_7_62mm": 2,
                },
                "replace": [("FM_Mpi_AKS_74NK", "PM_MPi_AKSU_74NK")],
            },
            "Salves": {
                "FM_Mpi_AKS_74NK": 11,
                "RocketInf_RPG7VL": 6,
            },
        },
    },

    "Fallschirmjager_HMG_DDR": {
        "GameName": {
            "display": "FALLSCHIRMJÄGER (s.MG)",
        },
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "strength": 9,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
             "equipmentchanges": {
                "quantity": {
                    "FM_Mpi_AKS_74NK": 6,
                },
            },
            "Salves": {
                "FM_Mpi_AKS_74NK": 11,
                "RocketInf_RPG18_64mm": 7,
            },
        },
    },

    "Fallschirmjager_Metys_DDR": {
        "GameName": {
            "display": "FALLSCHIRMJÄGER (Metis)",
        },
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "strength": 9,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
             "equipmentchanges": {
                "animate": {
                    "SAW_lMG_K_7_62mm": False,
                },
                "quantity": {
                    "FM_Mpi_AKS_74NK": 7,
                    "SAW_lMG_K_7_62mm": 2,
                },
                "replace": [("FM_Mpi_AKS_74NK", "PM_MPi_AKSU_74NK")],
            },
            "Salves": {
                "FM_Mpi_AKS_74NK": 11,
            },
        },
    },

    "Luftsturmjager_DDR": {
        "GameName": {
            "display": "LUFTSTURM-JÄGER",
        },
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "strength": 9,
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
             "equipmentchanges": {
                "quantity": {
                    "FM_Mpi_AKS_74NK": 7,
                    "MMG_PKM_7_62mm": 1,
                },
            "insert": [(2, "MMG_PKM_7_62mm")],
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
                "FM_Mpi_AKS_74NK": 11,
                "MMG_PKM_7_62mm": 135,
            },
        },
    },

    "Luftsturmjager_Metis_DDR": {
        "GameName": {
            "display": "LUFTSTURM-JÄGER (Metis)",
        },
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "strength": 9,
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "Luftsturmjager_DDR",
        "WeaponDescriptor": {
             "equipmentchanges": {
                "quantity": {
                    "FM_Mpi_AKS_74NK": 7,
                    "MMG_PKM_7_62mm": 1,
                },
            "insert": [(2, "MMG_PKM_7_62mm")],
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
                "FM_Mpi_AKS_74NK": 11,
                "MMG_PKM_7_62mm": 135,
            },
        },
    },

    "Wachregiment_RPG_DDR": {
        "GameName": {
            "display": "WACHSCHÜTZEN",
        },
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Wachregiment_DDR": {
        "GameName": {
            "display": "WACHSCHÜTZEN [RPO]",
        },
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Wachregiment_SMG_DDR": {
        "GameName": {
            "display": "WACHSCHÜTZEN [STOSS]",
        },
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Groupe_AT_Wach_DDR": {
        "GameName": {
            "display": "WACH. PANZERJÄGER",
        },
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "strength": 8,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
         "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_Skorpion": 8,
                },
            },
            "Salves": {
                "RocketInf_RPG7VR_64mm": 4,
            },
        },
    },

    "Engineers_DDR": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [8, 6, 0, 0],
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
                    "FM_Mpi_AK_74N": 6,
                    "MMG_PKM_7_62mm": 2,
                },
            },
            "Salves": {
                "Grenade_Satchel_Charge": 6,
            },
        },
    },

    "Engineers_Naval_DDR": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [8, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_KMS_72": 9,
                    "SAW_lMG_K_7_62mm": 3,
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

     "Engineers_Naval_Flam_DDR": {
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "availability": [8, 0, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Engineers_AGI_DDR": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
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

    "UAZ_469_SPG9_DDR": {
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [12, 9, 0, 0],
    },

    "UAZ_469_SPG9_FJ_DDR": {
        "CommandPoints": 25,
        "availability": [0, 0, 12, 9],
        "SpecialtiesList": {
            "add_specs": ["'_para'"],
        },
        "DeploymentShift": 1750,
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

    "ATteam_RCL_SPG9_FJ_DDR": {
        "strength": 5,
        "CommandPoints": 30,
        "availability": [0, 0, 10, 7],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "DeploymentShift": 1750,
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

    "ATteam_Fagot_FJ_DDR": {
        "CommandPoints": 25,
        "availability": [0, 0, 9, 7],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("ATGM_9K111M_Faktoriya", "ATGM_9K111_Fagot")],
            },
        },
        "DeploymentShift": 1750,
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

    "Mortier_M43_82mm_FJ_DDR": {
        "CommandPoints": 30,
        "availability": [0, 0, 5, 4],
    },

    "Mortier_PM43_120mm_DDR": {
        "CommandPoints": 45,
        "availability": [5, 4, 3, 0],
    },
    
    "Mortier_2S12_120mm_DDR": {
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

    "Howz_ZiS3_76mm_DDR": {
        "CommandPoints": 55,
        "availability": [5, 4, 3, 0],
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

    "MFRW_RM70_cluster_DDR": { # [CLU] 
        "CommandPoints": 280,
        "GameName": {
            "display": "MFRW RM-70M [CLU]",
        },
        "availability": [2, 0, 1, 0],
        # "WeaponDescriptor": {
        #     "equipmentchanges": {
        #         "replace": [("RocketArt_M21OF_122mm_cluster", "RocketArt_M21OF_122mm_RM70_cluster")],
        #     },
        # },
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

    "BTR_50_MRF_DDR": {
        "CommandPoints": 50,
        "availability": [3, 2, 0, 0],
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

    "T55AM2_CMD_DDR": {  # T-55AM2 LDR
        "CommandPoints": 125,
        "GameName": {
            "display": "#LDRSOV FüPz T-55AM2K3 LDR.",
            "token": "POLT55AMLD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T55AM_CMD_DDR",
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
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },

    "T72_CMD_DDR": {
        "CommandPoints": 115,
        "GameName": {
            "display": "#LDRSOV FüPz. T-72K LDR.",
            "token": "NYCDIWGOQO",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T72_CMD_DDR",
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
        "availability": [0, 0, 4, 0],
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
        "CommandPoints": 195,
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
    
    "AT_ZiS2_57mm_DDR": {  # Zis-2 AT 57mm (This may be way to cheap, but man is this thing bad, and has no HE)
        "CommandPoints": 15,
        "availability": [14, 0, 0, 0],
    },
    
    "AT_vz52_85mm_DDR": {  # vz-52 AT 85mm
        "CommandPoints": 35,
        "availability": [9, 0, 0, 0],
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
        "CommandPoints": 55,
    },

    "BTR_60_DDR": {
        "CommandPoints": 20,
        "strength": 10,
    },

    "BTR_70_DDR": {
        "CommandPoints": 25,
        "strength": 10,
    },

    "BTR_152A_DDR": {
        "CommandPoints": 25,
        "strength": 10,
    },

    "PSzH_IV_DDR": {
        "CommandPoints": 20,
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
    
    "TO_55_DDR": {
        "GameName": {
            "display": "FlamPz. TO-55",
        },
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

    "T55AM2_DDR": {  # T-55AM2
        "CommandPoints": 110,
        "availability": [0, 8, 6, 0],
    },

    "T55AM2B_DDR": {  # T-55AM2B
        "CommandPoints": 140,
        "availability": [0, 6, 4, 0],
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
        "availability": [0, 6, 4, 0],
    },

    "T72M1_DDR": {
        "GameName": {
            "display": "KPz T-72M1",
        },
        "CommandPoints": 175,
        "Divisions": {
            "remove": ["RDA_7_Panzer"],
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 5, 3, 0],
    },
    
    "T72S_DDR": {
        "CommandPoints": 210,
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

    "UAZ_469_AGL_Grenzer_DDR": {
        "CommandPoints": 30,
    },

    "OT_65_DDR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "BRDM_1_DDR": {
        "CommandPoints": 20,
    },

    "BTR_60_reco_DDR": {
        "CommandPoints": 30,
        "strength": 10,
    },

     "BMP_1P_reco_DDR": { # is named BMP-1P in descriptor but lacks the smoke and fagot missle, so its basically a BMP-1 basic
        "GameName": {
            "display": "#RECO1 AufKl BMP-1",
        },
        "CommandPoints": 35,
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

    "Mi_8TB_reco_Marine_DDR": { # #RECO2 AUFKL. Mi-8TB
        "CommandPoints": 110,
        "availability": [0, 4, 3, 0],
    },

    "Mi_14PL_recon_DDR": {  # #RECO3 AUFKL. Mi-14PL
        "CommandPoints": 50,
        "availability": [0, 4, 0, 0],
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
        "max_speed": 26,
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

    "Grenzer_Mot_DDR": {
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "availability": [8, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(1, "SAW_lMG_K_7_62mm")], # (turret, weapon)
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
                "quantity": {
                    "FM_KMS_72": 3,
                    "SAW_lMG_K_7_62mm": 1,
                },
            },
            "Salves": {
                "insert": [(1, 18)],
            },
        },
    },

    "Grenzer_DDR": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [8, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },

    "Grenzer_Flam_DDR": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [6, 0, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(2, "SAW_lMG_K_7_62mm")], # (turret, weapon)
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
                "quantity": {
                    "FM_KMS_72": 5,
                    "SAW_lMG_K_7_62mm": 1,
                },
            },
            "Salves": {
                "insert": [(2, 18)],
            },
        },
    },

    "Scout_Wach_DDR": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "strength": 7,
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_StG_942": 6,
                },
            },
        },
    },

    "Engineers_Naval_Scout_DDR": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "availability": [0, 4, 3, 0],
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
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "KSK18_DDR": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "strength": 8,
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_MPi_AKSU_74NK": 6,
                },
            },
            "Salves": {
                "RocketInf_RPG18_64mm": 7,
                "Grenade_Satchel_Charge": 6,
            },
        },
    },

    "Fallschirmjager_FalseFlag_DDR": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Fallschirmjager_FlaseFlag_Demo_DDR": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketInf_M72_LAW_66mm", "RocketInf_M72A3_LAW_66mm")],
            },
            "Salves": {
                "RocketInf_M72A3_LAW_66mm": 7,
            },
        },
    },

    "Scout_FJ_DDR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 8, 6],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPG18_64mm": 4,
            },
        },
    },

    "Sniper_FJ_DDR": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "strength": 3,
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(2, "RocketInf_RPG18_64mm")], # (turret, weapon)
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
                "quantity": {
                    "PM_Skorpion": 2,
                },
            },
            "Salves": {
                "insert": [(2, 3)],
            },
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

     "MANPAD_Strela_2M_FJ_DDR": {
        "GameName": {
            "display": "Fs-FLA-RAK. STRELA-2M",
        },
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 12, 9],
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

    "Bofors_40mm_capture_DDR": {
        "GameName": {
            "display": "BEUTE BOFORS 40mm",
        },
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },
    
    "DCA_AZP_S60_DDR": {
        "GameName": {
            "display": "FLAK S-60 57mm",
        },
        "CommandPoints": 35,
        "availability": [9, 7, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },

    "DCA_KS19_100mm_DDR": {
        "GameName": {
            "display": "FLAK KS-19M2 100mm",
        },
        "CommandPoints": 55,
        "availability": [9, 7, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },

    "DCA_FASTA_4_DDR": {
        "CommandPoints": 25,
        "max_speed": 6,
        "stealth": 2,
        "availability": [10, 7, 0, 0],
    },

    "LO_1800_FASTA_4_DDR": {
        "CommandPoints": 35,
        "availability": [8, 6, 0, 0],
    },

    "W50_LA_A_25mm_DDR": {
        "CommandPoints": 40,
        "availability": [7, 5, 0, 0],
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
        "CommandPoints": 130,
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

    "2K11_KRUG_DDR": {  # 2K11 Krug
        "CommandPoints": 130,
        "availability": [3, 2, 0, 0],
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
        "UpgradeFromUnit": "2K12_KUB_DDR",
    },

     "DCA_I_Hawk_capture_DDR": {
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
        "UpgradeFromUnit": "2K11_KRUG_DDR",
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
        "CommandPoints": 85,
        "availability": [0, 6, 4, 0],
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

    "Mi_24D_AA_DDR": {
        "CommandPoints": 130,
        "availability": [0, 3, 2, 0],
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
        "CommandPoints": 160,
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

    "Mi_14PL_AT_DDR": {
        "CommandPoints": 100,
        "availability": [0, 2, 0, 1],
    },

    # RDA AIR
    "L39ZO_CLU_DDR": {
        "CommandPoints": 90,
        "availability": [0, 4, 0, 0],
    },

    "L39ZO_DDR": {
        "CommandPoints": 60,
        "availability": [0, 5, 0, 0],
    },

    "L39ZO_HE1_DDR": {
        "CommandPoints": 90,
        "availability": [0, 5, 0, 0],
    },

    "MiG_21PFM_AA_DDR": {
        "CommandPoints": 95,
        "availability": [0, 4, 3, 2],
    },

    "MiG_21bis_AA2_DDR": {
        "CommandPoints": 110,
        "availability": [0, 4, 3, 2],
    },

    "MiG_21bis_AA3_DDR": {
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

    "MiG_21bis_NPLM_DDR": {
        "CommandPoints": 135,
        "availability": [0, 4, 0, 0],
    },

    "MiG_21bis_HE_DDR": {
        "CommandPoints": 135,
        "availability": [0, 4, 0, 0],
    },

    "MiG_21bis_CLU_DDR": {
        "CommandPoints": 180,
        "availability": [0, 2, 0, 0],
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

    "MiG_23BN_AT_DDR": {  # MiG-23BN [AT]
        "CommandPoints": 135,
        "availability": [0, 3, 2, 0],
    },

    "MiG_23BN_CLU_DDR": {  # MiG-23BN [CLU]
        "CommandPoints": 185,
        "availability": [0, 3, 0, 0],
    },

    "MiG_23BN_DDR": {  # MiG-23BN [HE]
        "CommandPoints": 140,
        "availability": [0, 3, 0, 0],
    },

    "MiG_23BN_nplm_DDR": {  # MiG-23BN [HE]
        "CommandPoints": 145,
        "availability": [0, 3, 0, 0],
    },

    "MiG_23BN_RKT_DDR": {  # MiG-23BN 240mm rocket
        "CommandPoints": 140,
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

    "MiG_23BN_KMGU_DDR": {  # MiG-23BN HE cluster bomblets thing?
        "CommandPoints": 200,
        "availability": [0, 2, 0, 0],
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
        "CommandPoints": 195,
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_Kh29T": 1,
            },
        },
    },

    "Su_22_AT2_DDR": {
        "CommandPoints": 160,
        "availability": [0, 2, 0, 1],
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

    "Su_22_HE2_DDR": {  # [HE2]
        "CommandPoints": 230,
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

    "Su_22_UPK_DDR": {  # [HE2]
        "CommandPoints": 125,
        "availability": [0, 3, 2, 0],
    },
}