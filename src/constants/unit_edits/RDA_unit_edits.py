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
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
    },
    
    "PT76B_CMD_DDR": { # Too inexpensive to make a LDR., just changing to a CV
        "CommandPoints": 170,
        "Factory": "Factory/Logistic",
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
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
    },
    
    "MTLB_CMD_DDR": {
        "CommandPoints": 145,
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 0, 3, 0],
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
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
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
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
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
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
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
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
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
    },

    "Mi_2_CMD_DDR": {  # Mi-2D
        "GameName": {"display": "Mi-2D"},
        "CommandPoints": 115,
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "availability": [0, 3, 0, 0],
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
    },

    "Mi_9_DDR": {  # Mi-19D
        "GameName": {
            "display": "Mi-19"
        },
        "CommandPoints": 145,
        "SpecialtiesList": {
            "add_specs": ["'leader_sov'",],
            "remove_specs": ["'_leader'"],
        },
        "TagSet": {
            "add_tags": ['"CMD_Unit"'],
        },
        "availability": [0, 3, 0, 0],
    },

    # RDA INF
    "MotRifles_CMD_DDR": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MOT.-SCHUTZEN FÜR.",
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
        "remove_zone_capture": None,
    },

    "Engineers_CMD_DDR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "PIONIER",
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
        "remove_zone_capture": None,
    },

    "Engineers_Naval_CMD_DDR": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "MARINEPIONIER FÜR.",
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
                "RocketInf_RPG7": 9,
            },
        },
        "remove_zone_capture": None,
    },
    
    "KdA_CMD_DDR": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "K.d.A. FÜH.",
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
                "FM_KMS_72": 9,
                "SAW_lMG_K_7_62mm": 24,
            },
        },
        "remove_zone_capture": None,
    },
    
    "Reserve_CMD_DDR": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "RESERVISTEN FÜH.",
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
        "WeaponDescriptor": {
            "Salves": {
                "FM_KMS_72": 9,
            },
        },
        "availability": [0, 7, 5, 0],
        "max_speed": 20,
        "remove_zone_capture": None,
    },
    
    "Fallschirmjager_CMD_DDR": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "FALLSCHIRM FÜR.",
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
                'leader_sov',
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
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
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
                "insert": [(1, 18)],
                "RocketInf_RPG18_64mm": 7,
                "FM_Mpi_AKS_74NK": 11,
            },
        },
        "remove_zone_capture": None,
    },

    "Luftsturmjager_CMD_DDR": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "LUFTSTURM-JÄGER FÜR.",
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
                'leader_sov',
                '_sf',
                '_choc',
                '_para',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry_sf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_PKM_7_62mm": False,
                },
                "quantity": {
                    "FM_Mpi_AKS_74NK": 7,
                    "MMG_PKM_7_62mm": 2,
                },
                "replace": {
                    "RocketInf_RPG18_64mm": {
                        "new_weapon": "RocketInf_RPG27_105mm",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
                "insert": [(1, "MMG_PKM_7_62mm")],
                "insert_edits": {
                    1: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
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
                "insert": [(1, 36)],
                "RocketInf_RPG27_105mm": 6,
                "FM_Mpi_AKS_74NK": 11,
            },
        },
        "remove_zone_capture": None,
    },

    "Wachregiment_CMD_DDR": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "WACHSCHÜTZEN FÜH.",
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
        "remove_zone_capture": None,
    },

    "Fallschirmjager_FalseFlag_CMD_DDR": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "FALLSCHIRM FÜR. FF",
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
                "UNITE_Fallschirmjager_FalseFlag_CMD_DDR",
                "Unite",
                "noSIGINT",
            ],
        },
        "strength": 8,
        "orders": {
            "add_orders": ['EOrderType/ShootOnPositionSmoke', 'EOrderType/ShootOnPositionWithoutCorrectionSmoke'],
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
                '_falseflag',
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
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
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
                "quantity": {
                    "FM_M16": 6,
                    "SAW_M249_5_56mm": 2,
                },
            },
            "Salves": {
                "insert": [(1, 23), (3, 3)],
                "RocketInf_M72A3_LAW_66mm": 7,
            },
        },
        "remove_zone_capture": None,
    },

    "Volkspolizei_CMD_DDR": { # Not used, DLC slop
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "VOPOS FÜH.",
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
        "orders": {
            "add_orders": ["EOrderType/ShootOnPositionSmoke",
                "EOrderType/ShootOnPositionWithoutCorrectionSmoke"],
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
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
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
                "quantity": {
                    "PM_Skorpion": 6,
                },
            },
            "Salves": {
                "insert": [(1, 4), (2, 3)],
            },
        },
        "remove_zone_capture": None,
    },

    # Not sure if we will ever need these
    "MotRifles_Naval_CMD_DDR": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_MotRifles_Naval_CMD_DDR",
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
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_Mpi_AK_74N": 6,
                },
            },
        },
        "remove_zone_capture": None,
    },

    "Reserve_DDR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_KMS_72": 9,
            },
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
        "WeaponDescriptor": {
            "Salves": {
                "FM_KMS_72": 9,
            },
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
        "UpgradeFromUnit": "MP_mech_DDR",
    },

    "Security_VPB_DDR": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "MP_DDR": {
        "GameName": {
            "display": "MILITÄRSTREIFEIN (K.d.A.)",
        },
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [0, 12, 9, 0],
        "max_speed": 26,
        "strength": 5,
        "WeaponDescriptor": {
            # Mixed-model strength-5 squad: 4 MP_DDR + 1 KdA_DDR (RPG-2 gunner).
            # Vanilla turrets: T0=PM_Skorpion (qty=4)
            # Target turrets:  T0=PM_Skorpion(x4), T1=RocketInf_RPG2(x1 animate=True)
            "equipmentchanges": {
                "quantity": {
                    "PM_Skorpion": 5,
                },
                "insert": [
                    (1, "RocketInf_RPG2"),
                ],
                "insert_edits": {
                    1: {  # RocketInf_RPG2 (newly inserted, donor KdA_DDR)
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                },
            },
            # Vanilla Salves: [PM_Skorpion=80]. Target: [22, 6].
            "Salves": {
                "PM_Skorpion": 22,
                "insert": [
                    (1, 6),
                ],
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "MP_Combat_DDR": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [0, 8, 6, 0],
        "max_speed": 26,
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
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                },
            },
            "Salves": {
                "insert": [(1, 4)],
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
            "Salves": {
                "FM_KMS_72": 9,
                "SAW_lMG_K_7_62mm": 24,
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
        "CommandPoints": 30,
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
        "availability": [0, 0, 4, 4],
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
                "replace": {
                    "FM_Mpi_AKS_74NK": {
                        "new_weapon": "PM_MPi_AKSU_74NK",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
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
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "strength": 9,
        "availability": [0, 0, 4, 3],
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
            "display": "FALLSCHIRMJÄGER [METIS]",
        },
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "strength": 9,
        "availability": [0, 0, 4, 3],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
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
                "replace": {
                    "FM_Mpi_AKS_74NK": {
                        "new_weapon": "PM_MPi_AKSU_74NK",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
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
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "MMG_PKM_7_62mm": 1,
                },
                "insert": [(2, "MMG_PKM_7_62mm")],
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
                "insert": [(2, 36)],
            },
        },
    },

    "Luftsturmjager_Metis_DDR": {
        "GameName": {
            "display": "LUFTSTURM-JÄGER (Metis)",
        },
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "strength": 9,
        "availability": [0, 0, 4, 3],
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
                    "SAW_lMG_K_7_62mm": 1,
                },
                "insert": [(2, "MMG_PKM_7_62mm")],
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
                "insert": [(2, 36)],
            },
        },
    },

    "Wachregiment_RPG_DDR": {
        "GameName": {
            "display": "WACHSCHÜTZEN",
        },
        "CommandPoints": 50,
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
        "CommandPoints": 65,
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
        "CommandPoints": 55,
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

    "MotRifles_Naval_DDR": {
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
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
                "FM_KMS_72": 9,
                "Grenade_Satchel_Charge": 7,
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
        "WeaponDescriptor": {
            "Salves": {
                "FM_KMS_72": 9,
            },
            
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
        "UpgradeFromUnit": "HMGteam_NSV_DDR",
    },

    "HMGteam_AGS17_VPB_DDR": {
        "CommandPoints": "HMGteam_AGS17_SOV",
        "GameName": {
            "display": "VPB Gr-MG 30mm",
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
        "UpgradeFromUnit": "HMGteam_AGS17_DDR",
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
        "DeploymentShift": 1750,
        "ButtonTexture": "UAZ_469_SPG9_Para_POL",
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
                "replace": {
                    "ATGM_9K111M_Faktoriya": {
                        "new_weapon": "ATGM_9K111_Fagot",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
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
                "replace": {
                    "ATGM_9K111M_Faktoriya": {
                        "new_weapon": "ATGM_9K111_Fagot",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
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

    "LO_1800_trans_DDR": {
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
    
    "Trabant_601_MP_DDR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "Barkas_B1000_MP_DDR": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    # RDA ARTILLERY
    "BTR_50_CMD_DDR": {
        "capacities": {
            "add_capacities": ["LDR_ARTY"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 60,
        "GameName": {
            "display": "SPW-50PU(A)",
            "token": "MXTHDKLGFB", # Don't remove or logistic tab version will get renamed as well
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_BTR_50_CMD_DDR",
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
    
    "Howz_M30_122mm_DDR": { # not using, who the hell cares about slightly less range D-30
        "CommandPoints": 85, # vanilla 85
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
                "replace": {
                    "RocketArt_M21OF_122mm": {
                        "new_weapon": "RocketArt_M21OF_122mm_RM70",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
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
                "replace": {
                    "RocketArt_M21OF_122mm_napalm": {
                        "new_weapon": "RocketArt_M21OF_122mm_RM70_napalm",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
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
    
    "BM21_Grad_HE_DDR": { # BM-21 [HE]
        "CommandPoints": "BM21_Grad_SOV",
        "GameName": {
            "display": "MFRW BM-21 [HE]",
        },
        "availability": "BM21_Grad_SOV",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 70,
        "GameName": {
            "display": "FüPz T-54AMK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 70,
        "GameName": {
            "display": "FüPz T-55AK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 110,
        "GameName": {
            "display": "FüPz T-55AM2K3",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 110,
        "armor": {
            "top": (2, None),
        },
        "GameName": {
            "display": "FüPz. T-72K",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 160,
        "armor": {
            "top": (2, None),
        },
        "GameName": {
            "display": "FüPz T-72M",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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
        "capacities": {
            "add_capacities": ["LDR_TNK"],
        },
        "modules_remove": ["TCommanderModuleDescriptor"],
        "CommandPoints": 185,
        "armor": {
            "top": (3, None),
        },
        "GameName": {
            "display": "FüPz T-72M1K",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "LDR_SOV_Unit",
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

    "AT_T12_100mm_DDR": {  # T-12 AT 100mm
        "CommandPoints": 45,
        "availability": [8, 6, 0, 0],
    },
    
    "AT_T12_Rapira_DDR": { 
        "CommandPoints": "AT_T12_Rapira_SOV",
        "availability": "AT_T12_Rapira_SOV",
        "UpgradeFromUnit": "AT_T12_100mm_DDR",
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
        "CommandPoints": 15,
    },

    "BMP_1_SP1_DDR": { # (Resolute, smoke)
        "CommandPoints": 20,
    },

    "BMP_1_SP2_DDR": { # (Malyutka, resolute, smoke)
        "CommandPoints": 25,
    },

    "BMP_1P_DDR": { # BMP-1P(C) (Faktoriya, resolute, smoke)
        "CommandPoints": "BMP_1P_SOV",
        "WeaponDescriptor": {
            "Salves": "BMP_1P_SOV",
        },
    },
    
    "BMP_1P_Konkurs_DDR": { # BMP-1P(D) (Konkurs, resolute, smoke)
        "CommandPoints": "BMP_1P_Konkurs_SOV",
        "WeaponDescriptor": {
            "Salves": "BMP_1P_Konkurs_SOV"
        },      
    },
    
    "BMP_2_DDR": {
        "CommandPoints": "BMP_2_SOV",
    },

    "BTR_60PA_Reserve_DDR": {
        "CommandPoints": 20,
        "strength": 10,
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
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZPU4_14_5mm": 192,
            },
        },
    },

    "PSzH_IV_DDR": {
        "CommandPoints": 20,
        "strength": 10,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/Standard": 3180.0,
                "EOpticalStrength/LowAltitude": 3180.0,
                "EOpticalStrength/HighAltitude": 706.0,
            },
        },
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
                "ATGM_9K111M_Faktoriya": "LUAZ_967M_Fagot_SOV",
            },
        },
    },
    
    "BRDM_Malyu_P_DDR": {  # BRDM-2 Malutka-P
        "CommandPoints": "BRDM_2_Malyu_P_POL",
        "strength": "BRDM_2_Malyu_P_POL",
        "stealth": "BRDM_2_Malyu_P_POL",
        "availability": "BRDM_2_Malyu_P_POL",
        "UpgradeFromUnit": "UAZ_469_Fagot_FJ_DDR",
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
                "replace": {
                    "Canon_AP_85mm_S53": {
                        "new_weapon": "Canon_HEAT2_85mm_S53",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
    },
    
    "T54B_DDR": {
        "CommandPoints": 70,
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
        "CommandPoints": 125,
        "availability": [0, 4, 3, 0],
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_Reco",
                "GroundUnits",
                "Radio",
                "Reco",
                "UNITE_T55AM2_DDR",
                "Unite",
            ],
        },
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
        "UnitRole": 'reco',
        "UpgradeFromUnit": "T54B_reco_DDR",
    },

    "T55AM2B_DDR": {  # T-55AM2B
        "CommandPoints": 140,
        "availability": [0, 6, 4, 0],
    },

    "T72_DDR": {
        "GameName": {
            "display": "KPz T-72",
        },
        "CommandPoints": 110,
        "armor": {
            "top": (2, None),
        },
        "availability": [8, 6, 0, 0],
    },

    "T72M_DDR": {
        "GameName": {
            "display": "KPz T-72M",
        },
        "CommandPoints": 150,
        "armor": {
            "top": (2, None),
        },
        "availability": [6, 4, 0, 0],
    },
    
    "T72MUV2_DDR": {
        "CommandPoints": 155,
        "armor": {
            "top": (2, None),
        },
        "availability": [6, 4, 0, 0],
    },

    "T72M1_DDR": {
        "GameName": {
            "display": "KPz T-72M1",
        },
        "CommandPoints": 175,
        "armor": {
            "top": (3, None),
        },
        "Divisions": {
            "remove": ["RDA_7_Panzer"],
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 6, 4, 0],
    },
    
    "T72S_DDR": {
        "CommandPoints": 230,
        "armor": {
            "top": (4, None),
        },
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
        "CommandPoints": 20,
         "orders": {
            "add_orders": ["EOrderType/Sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
        "UpgradeFromUnit": None,
    },

    "BRDM_1_DDR": {
        "CommandPoints": 20,
    },

    "BTR_60_reco_DDR": {
        "CommandPoints": 30,
        "strength": 10,
        "UpgradeFromUnit": "UAZ_469_AGL_Grenzer_DDR",
    },

    "BMP_1P_reco_DDR": { # is named BMP-1P in descriptor but lacks the smoke and fagot missle, so its basically a BMP-1 basic
        "GameName": {
            "display": "AufKl BMP-1",
        },
        "CommandPoints": 40,
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
        "UpgradeFromUnit": "PT76B_DDR",
    },

    "BRM_1_DDR": {
        "GameName": {
            "display": "AufKl BRM-1K",
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
        "UpgradeFromUnit": "BRDM_2_DDR",
    },
    
    "PT76B_DDR": {
        "CommandPoints": "PT76B_Naval_SOV",
        "availability": [8, 6, 0, 0],
    },

    "Mi_2_reco_DDR": {
        "CommandPoints": 30,
        "availability": [0, 6, 0, 0],
    },
    
    "Mi_2_gunship_DDR": {
        "CommandPoints": 35,
        "availability": [0, 6, 4, 0],
    },

    "Mi_8TB_reco_Marine_DDR": { # #RECO2 AUFKL. Mi-8TB
        "CommandPoints": 110,
        "availability": [0, 4, 3, 0],
        "UpgradeFromUnit": "Mi_14PL_recon_DDR",
    },

    "Mi_24D_s5_AT_reco_DDR": { # #RECO2 DHS Mi-24D Transport
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 135,
        "strength": "Mi_24P_SOV",
    },

    "Mi_14PL_recon_DDR": {  # #RECO3 AUFKL. Mi-14PL
        "CommandPoints": "Mi_14PL_recon_SOV",
        "availability": [0, 4, 0, 0],
        "UpgradeFromUnit": "Mi_2_gunship_DDR",
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
        "UpgradeFromUnit": "Scout_KdA_DDR",
    },

    "Scout_Reserve_DDR": {
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "strength": 4,
        "capacities": {
            "add_capacities": ["reserviste"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_KMS_72": 3,
                },
            },
            "Salves": {
                "FM_KMS_72": 9,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'infantry_equip_light'", "'_swift'"],
        },
        "UpgradeFromUnit": None,
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
            "Salves": {
                "FM_KMS_72": 9,
                "SAW_lMG_K_7_62mm": 24,
            },
        },
        "UpgradeFromUnit": "Scout_Reserve_DDR",
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

    "Scout_SIGINT_DDR": {
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "availability": [6, 4, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
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
                        "AmmoBoxIndex": 1,
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
                "FM_KMS_72": 9,
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
        "WeaponDescriptor": {
            "Salves": {
                "FM_KMS_72": 9,
            },
        },
    },

    "Grenzer_Flam_DDR": {
        "CommandPoints": 45,
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
                        "AmmoBoxIndex": 2,
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
                "FM_KMS_72": 9,
            },
        },
        "UpgradeFromUnit": "Engineers_Naval_Scout_DDR",
    },

    "Scout_Wach_DDR": {
        "CommandPoints": 40,
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
        "UpgradeFromUnit": None,
    },

    "Engineers_Naval_Scout_DDR": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 4, 3, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "UpgradeFromUnit": "Grenzer_DDR",
    },

    "Scout_LRRP_DDR": {
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "UpgradeFromUnit": "KSK18_DDR",
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
        "UpgradeFromUnit": "Scout_FJ_DDR",
    },

    "Fallschirmjager_FalseFlag_DDR": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "UpgradeFromUnit": "Scout_Wach_DDR",
    },

    "Fallschirmjager_FlaseFlag_Demo_DDR": {
        "CommandPoints": 55,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        # This unit doesn't have a LAW???
        # "WeaponDescriptor": {
        #     "equipmentchanges": {
        #         "replace": [("RocketInf_M72_LAW_66mm", "RocketInf_M72A3_LAW_66mm")],
        #     },
        #     "Salves": {
        #         "RocketInf_M72A3_LAW_66mm": 7,
        #     },
        # },
    },

    "Scout_FJ_DDR": {
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 8, 6],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "RocketInf_RPG18_64mm": {
                        "new_weapon": "RocketInf_RPG7VL",
                        "swap_fire_effect": True,
                        "depiction_baked_in": False,
                    },
                },
            },
            "Salves": {
                "RocketInf_RPG7VL": 4,
            },
        },
    },

    "Sniper_FJ_DDR": {
        "CommandPoints": 40,
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
                        "AmmoBoxIndex": 2,
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
                    "FM_Mpi_AK_74N": {
                        "new_weapon": "FM_Mpi_AK_74N_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
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
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 12, 9],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_Mpi_AKS_74NK": {
                        "new_weapon": "FM_Mpi_AKS_74NK_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
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
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "availability": [7, 5, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "FM_Mpi_AK_74N": {
                        "new_weapon": "FM_Mpi_AK_74N_noreflex",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },
    
    "DCA_ZPU4_DDR": {
        "CommandPoints": 20,
        "availability": [12, 9, 0, 0],
        "max_speed": 6,
        
        "WeaponDescriptor": {
            "Salves": {
                "DCA_4_canon_ZPU4_towed_14_5mm": 160,
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
                "Transports": ["MTLB_trans_DDR"],
                "cards": 1,
            },
        },
        "Factory": "Factory/Logistic",
        "availability": [9, 7, 0, 0],
        "max_speed": 6,
        
        "UpgradeFromUnit": "FOB_DDR",
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZU23_2_23mm_TOWED": 31,
            },
        },
    },

    "Bofors_40mm_capture_DDR": {
        "GameName": {
            "display": "BEUTE BOFORS 40mm",
        },
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 6,
        
        "WeaponDescriptor": {
            "Salves": {
                "DCA_1_canon_Bofors_40mm": 1,
            },
        },
    },
    
    "DCA_AZP_S60_DDR": {
        "GameName": {
            "display": "FLAK S-60 57mm",
        },
        "CommandPoints": "DCA_AZP_S60_SOV",
        "TagSet": {
            "add_tags": ['"AA_radar"'],
        },
        "availability": [9, 7, 0, 0],
        "max_speed": 6,
        
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
    },

    "DCA_KS19_100mm_DDR": {
        "GameName": {
            "display": "FLAK KS-19M2 100mm",
        },
        "CommandPoints": 75,
        "TagSet": {
            "add_tags": ['"AA_radar"'],
        },
        "availability": [9, 7, 0, 0],
        "max_speed": 6,
        "strength": 6,
        "WeaponDescriptor": {
            "Salves": {
                "DCA_1_canon_KS19_100mm_radar": 1,
            },
            "equipmentchanges": {
                "replace": {
                    "DCA_1_canon_KS19_100mm": {
                        "new_weapon": "DCA_1_canon_KS19_100mm_radar",
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

    "LO_1800_ZPU_2_DDR": {
        "CommandPoints": "LO_1800_ZPU_2_POL",
        "availability": "LO_1800_ZPU_2_POL",
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_ZPU4_14_5mm": 192,
            },
        },
    },

    "W50_LA_A_25mm_DDR": {
        "CommandPoints": 40,
        "availability": [7, 5, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canon_2M3_25mm": 107,
            },
        },
    },

    "ZSU_57_2_DDR": {
        "CommandPoints": 70,
        "availability": [7, 0, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "DCA_2_canons_S60_57mm": 25,
            },
        },
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
                "EOpticalStrength/HighAltitude": 7800,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
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
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "CommandPoints": 85,
        "availability": [6, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "DCA_4_canons_AZP_23_Amur_23mm_late": 67,
            },
            "equipmentchanges": {
                "replace": {
                    "DCA_4_canons_APZ23_23mm": {
                        "new_weapon": "DCA_4_canons_AZP_23_Amur_23mm_late",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
        },
    },
    
    "Osa_9K33M3_DDR": {
        "CommandPoints": 130,
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

    "2K12_KUB_M1_DDR": {
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "CommandPoints": 85,
        "strength": 10,
        "availability": [4, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    "2K12_KUB_DDR": {
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "CommandPoints": "2K12_KUB_SOV",
        "strength": 10,
        "availability": [4, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    "2K11_KRUG_DDR": {  # 2K11 Krug
        "CommandPoints": 130,
        "strength": 10,
        "availability": [3, 2, 0, 0],
        # "CommandPoints": 90,
        # "availability": [4, 3, 0, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "UpgradeFromUnit": "2K12_KUB_DDR",
    },

    "DCA_I_Hawk_capture_DDR": {
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 10600.0,
            },
            "TimeBetweenEachIdentifyRoll": 0.5,
        },
        "CommandPoints": 90,
        "strength": 6,
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
                "RocketAir_S5_57mm_salvolength16": 2,
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
        "WeaponDescriptor": {
            "Salves": {
                "Pod_UPK_23_250_AP_23mm_x2": 15,
            },
        },
    },
    
    "Mi_8TV_PodGatling_DDR": {
        "CommandPoints": 85, # vanilla 110
        "WeaponDescriptor": {
            "Salves": {
                "Pod_GUV_Gatling_7_62mm_12_7mm_x2": 8,
                "Pod_GUV_Gatling_7_62mm_12_7mm_x2": 8,
            },
        },
    },
    
    "Mi_8TB_DDR": { # 12.7mm Afanasyev, 2x 64x S-5m, 6x Malyutka-M
        "CommandPoints": 85,
        "availability": [0, 6, 4, 0],
    },

    "Mi_24D_s5_AT_DDR": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 130,
        "strength": "Mi_24P_SOV",
        "availability": [0, 4, 3, 0],
    },
    
    "Mi_24D_s8_AT_DDR": { # Mi-24D [AT2]
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 145, # vanilla 130
        "strength": "Mi_24P_SOV",
    },

    "Mi_24D_AA_DDR": {
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 130,
        "strength": "Mi_24P_SOV",
        "availability": [0, 3, 2, 0],
    },

    "Mi_24P_s8_AT_DDR": {
        "XP": {
            "pack": "helico_attack",
        },
        "GameName": {
            "display": "Mi-24P [AT]",
        },
        "CommandPoints": 160,
        "strength": "Mi_24P_SOV",
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
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 160,
        "strength": "Mi_24P_SOV",
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
        "XP": {
            "pack": "helico_attack",
        },
        "CommandPoints": 100,
        "availability": [0, 2, 0, 1],
    },

    # RDA AIR
    "L39ZO_CLU_DDR": {
        "CommandPoints": 75,
        "availability": [0, 4, 0, 0],
        "UpgradeFromUnit": "L39ZO_HE1_DDR",
    },

    "L39ZO_DDR": {
        "CommandPoints": 60,
        "availability": [0, 5, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "RocketAir_S5_57mm_salvolength32": [
                        {
                            "new_weapon": "RocketAir_S5_57mm_avion_salvolength32",
                            "swap_fire_effect": False,
                            "depiction_baked_in": False,
                        },
                        {
                            "new_weapon": "RocketAir_S5_57mm_avion_salvolength32",
                            "swap_fire_effect": False,
                            "depiction_baked_in": False,
                        },
                    ],
                },
            },
        },
    },

    "L39ZO_HE1_DDR": {
        "CommandPoints": "L39ZO_HE1_SOV",
        "availability": [0, 5, 0, 0],
    },

    "MiG_21PFM_AA_DDR": {
        "CommandPoints": 105,
        "ECM": -0.15,
        "availability": [0, 4, 3, 2],
    },

    "MiG_21bis_AA2_DDR": {
        "CommandPoints": 125,
        "ECM": -0.15,
        "availability": [0, 4, 3, 2],
    },

    "MiG_21bis_AA3_DDR": {
        "CommandPoints": 125,
        "ECM": -0.15,
        "availability": [0, 4, 3, 2],
    },

    "MiG_21PFM_DDR": {  # [RKT1]
        "GameName": {
            "display": "MiG-21bis [RKT]",
        },
        "CommandPoints": 110,
        "ECM": -0.15,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": {
                    "RocketAir_S5_57mm_salvolength32": {
                        "new_weapon": "RocketAir_S5_57mm_avion_salvolength32",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
        "availability": [0, 4, 0, 0],
    },

    "MiG_21bis_NPLM_DDR": {
        "CommandPoints": 145,
        "ECM": -0.15,
        "availability": [0, 4, 0, 0],
    },

    "MiG_21bis_HE_DDR": {
        "CommandPoints": 145,
        "ECM": -0.15,
        "availability": [0, 4, 0, 0],
    },

    "MiG_21bis_CLU_DDR": {
        "CommandPoints": 190,
        "ECM": -0.15,
        "availability": [0, 2, 0, 0],
    },

    "MiG_21bis_RKT2_DDR": {  # 4x S-24 [RKT2]
        "CommandPoints": 110,
        "ECM": -0.15,
        "availability": [0, 4, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketAir_S24_240mm_avion_salvolength4": (1, True),
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
    },

    "MiG_23BN_AT2_DDR": {  # MiG-23BN [AT2]
        "CommandPoints": 145,
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
        "ECM": -0.15,
        "availability": [0, 3, 2, 0],
    },

    "MiG_23BN_CLU_DDR": {  # MiG-23BN [CLU]
        "CommandPoints": 195,
        "ECM": -0.15,
        "availability": [0, 3, 0, 0],
    },

    "MiG_23BN_DDR": {  # MiG-23BN [HE]
        "CommandPoints": 150,
        "ECM": -0.15,
        "availability": [0, 3, 0, 0],
    },

    "MiG_23BN_nplm_DDR": {  # MiG-23BN [HE]
        "CommandPoints": 155,
        "ECM": -0.15,
        "availability": [0, 3, 0, 0],
    },

    "MiG_23BN_RKT_DDR": {  # MiG-23BN 240mm rocket
        "CommandPoints": 150,
        "ECM": -0.15,
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
    },

    "MiG_23BN_KMGU_DDR": {  # MiG-23BN HE cluster bomblets thing?
        "CommandPoints": 210,
        "ECM": -0.15,
        "availability": [0, 2, 0, 0],
    },

    "MiG_23MF_DDR": {  # [HE]
        "CommandPoints": 230,
        "ECM": -0.15,
        "availability": [0, 3, 0, 0],
    },
    
    "MiG_23BN_AT_DDR": {  # MiG-23MF [AT]
        "CommandPoints": 120,
        "ECM": -0.15,
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
        "availability": [0, 3, 0, 0],
    },
    
    "MiG_23MF_AA_DDR": {
        "CommandPoints": 125,
        "availability": [0, 4, 3, 2],
        "ECM": -0.15,
    },

    "MiG_23ML_DDR": {  # [AA]
        "CommandPoints": 135,
        "ECM": -0.15,
        "availability": [0, 3, 2, 0],
    },

    "MiG_29_AA_DDR": {  # 4x R-73, 2x R-27R [AA1]
        "CommandPoints": 215, # Availability taxed
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

    "Su_22_AT_DDR": {
        "CommandPoints": 195,
        "ECM": -0.30,
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_Kh29T": 1,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
    },

    "Su_22_AT2_DDR": {
        "CommandPoints": 210,
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
        "ECM": -0.30,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 1],
    },

    "Su_22_SEAD_DDR": { # Kh-28 5425m
        "CommandPoints": 195,
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
        "ECM": -0.40,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 3, 0, 2],
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
        "CommandPoints": 200,
        "ECM": -0.20,
        "availability": [0, 2, 0, 0],
    },

    "Su_22_nplm_DDR": {
        "CommandPoints": 190,
        "ECM": -0.20,
        "availability": [0, 3, 0, 0],
    },

    "Su_22_DDR": {  # [HE]
        "CommandPoints": 190,
        "ECM": -0.30,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "Su_22_HE2_DDR": {  # [HE2]
        "CommandPoints": 210,
        "ECM": -0.30,
        "SpecialtiesList": {
            "add_specs": ["'_jammer_air'"],
        },
        "availability": [0, 2, 0, 0],
    },

    "Su_22_RKT_DDR": {  # 4x S-24
        "CommandPoints": 105,
        "ECM": -0.20,
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
                "replace": {
                    "RocketAir_S24_240mm_salvolength2": {
                        "new_weapon": "RocketAir_S24_240mm_avion_salvolength4",
                        "swap_fire_effect": False,
                        "depiction_baked_in": False,
                    },
                },
            },
        },
    },

    "Su_22_UPK_DDR": {  # [HE2]
        "CommandPoints": 115,
        "ECM": -0.20,
        "availability": [0, 3, 2, 0],
    },
}