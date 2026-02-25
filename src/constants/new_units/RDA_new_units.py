"""New unit definitions for RDA."""

# fmt: off
RDA_NEW_UNITS = {
    ("KdA_DDR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "5f4a66c6-9baa-48b0-8276-20557fb1cf41",
        "GroupeCombatGUID": "ce0f6edf-7dbb-4654-a28a-5babfffc1678",
        "ShowroomGUID": "e460caeb-435d-44a8-b6e6-fcec671f4628",
        "CadavreGUID": "1416dac9-0b07-4a67-8455-fea6055d2254",
        "NewName": "KdA_DDR_TargetDummy",
        "GameName": {
            "display": "KdA 100",
            # "display": "#CMD MOT.-SCHÜTZEN FÜH.",
            "token": "VQYWUZFQCE",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_KdA_DDR_TargetDummy",
                "Unite",
            ],
        },
        "strength": 40,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        "Dangerousness": 12,
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "TransportedSoldier": "KdA_DDR_TargetDummy",
        "armor": "Infantry_armor_reference",
        "Factory": "EFactory/Logistic",
        "CommandPoints": 5,
        "UnitAttackValue": 1,
        "UnitDefenseValue": 16,
        "UnitRole": 'infantry',
        "SpecialtiesList": [
            '_reservist',
            '_militia',
            'infantry_equip_light',
        ],
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/CMD_Inf",
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [99, 0, 0, 0],
        "max_speed": 200,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/SmartMove', 'EOrderType/Attack', 'EOrderType/SmartMoveAndAttack', 'EOrderType/MoveAndAttack',
                   'EOrderType/Shoot', 'EOrderType/ShootOnPosition', 'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootOnPositionSmoke',
                   'EOrderType/ShootOnPositionWithoutCorrectionSmoke', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "is_transport": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "alternatives_count": 3,
        "selector_tactic": "01_03",
    },
    
    ("MotRifles_CMD_DDR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "847f8c3c-52c8-4a5b-8955-6dc3334ac281",
        "GroupeCombatGUID": "5bed0d57-83b0-46d7-99e6-f69138e38a84",
        "ShowroomGUID": "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d",
        "CadavreGUID": "79abc88c-d5be-4615-9ed2-4cb87bde9f4b",
        "NewName": "MotRifles_CMD2_DDR",
        "GameName": {
            "display": "#CMD FÜHRUNGSTRUPP",
            # "display": "#CMD MOT.-SCHÜTZEN FÜH.",
            "token": "DGZBQXLAYD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Commandant",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_CMD",
                "InfmapCommander",
                "UNITE_MotRifles_CMD2_DDR",
                "Unite",
            ],
        },
        "strength": 5,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        "Dangerousness": 12,
        "WeaponDescriptor": {
            "Salves": {
                "FM_Mpi_AK_74N": 11,
                "RocketInf_RPG18_64mm": 5,
            },
            "equipmentchanges": {
                "quantity": {
                    "FM_Mpi_AK_74N": 4,
                },
            },
        },
        "TransportedTexture": "UseInGame_Transport_COMMAND",
        "TransportedSoldier": "MotRifles_CMD_DDR",
        "armor": "Infantry_armor_reference",
        "Factory": "EFactory/Logistic",
        "CommandPoints": 145,
        "UnitAttackValue": 1,
        "UnitDefenseValue": 16,
        "UnitRole": 'hq_inf',
        "SpecialtiesList": [
            'leader_sov',
            '_resolute',
            'infantry_equip_light',
        ],
        "MenuIconTexture": "Texture_RTS_H_CMD_inf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/CMD_Inf",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "RDA_4_MSD_multi": {
                "Transports": ["W50_LA_A_DDR", "BTR_70_DDR", "Mi_2_trans_DDR", "Mi_8T_non_arme_DDR", "Mi_8T_DDR"],
            },
            "RDA_7_Panzer_multi": {
                "Transports": ["W50_LA_A_DDR", "BTR_70_DDR", "Mi_2_trans_DDR", "Mi_8T_non_arme_DDR", "Mi_8T_DDR"],
            },
            "RDA_9_Panzer_multi": {
                "Transports": ["W50_LA_A_DDR", "BTR_70_DDR", "Mi_2_trans_DDR", "Mi_8T_non_arme_DDR", "Mi_8T_DDR"],
            },
            "RDA_KdA_Bezirk_Erfurt_multi": {
                "Transports": ["UAZ_469_trans_DDR", "SPW_152K_DDR", "BTR_60_DDR","Mi_2_trans_DDR"],
            },
        },
        "availability": [0, 0, 2, 0],
        "max_speed": 26,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/SmartMove', 'EOrderType/Attack', 'EOrderType/SmartMoveAndAttack', 'EOrderType/MoveAndAttack',
                   'EOrderType/Shoot', 'EOrderType/ShootOnPosition', 'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootOnPositionSmoke',
                   'EOrderType/ShootOnPositionWithoutCorrectionSmoke', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "is_transport": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "alternatives_count": 5,
        "selector_tactic": "02_05",
    },

    ("BTR_50_CMD_DDR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "eb482c98-ddae-45cb-b62e-f50ad4c79d99",
        "GroupeCombatGUID": "1d1735b6-a0e6-49be-994e-f1bf7480872b",
        "ShowroomGUID": "e5f6a7b8-c9d0-4e1f-2a3b-4c5d6e7f8a9b",
        "CadavreGUID": "94711356-5cd2-4d35-b3e6-a25ca820237b",
        "NewName": "BTR_50_CMD2_DDR",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_BTR_50_CMD2_DDR",
                "Unite",
                "Vehicule",
                "Vehicule_CMD",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 145,
        "UnitRole": 'hq_veh',
        "SpecialtiesList": [
            'leader_sov',
            '_amphibie',
            '_resolute',
        ],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "RDA_4_MSD_multi": {
                "Transports": None,
            },
            "RDA_7_Panzer_multi": {
                "Transports": None,
            },
            "RDA_9_Panzer_multi": {
                "Transports": None,
            },
            "RDA_KdA_Bezirk_Erfurt_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 3, 0, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Reverse',
                   'EOrderType/AskForSupply', 'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": True,
        "Faction": "PACT",
        "Nation": "DDR",
    },

    ("ATteam_Fagot_DDR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "87782b09-1378-4507-8e87-45139ae746eb",
        "GroupeCombatGUID": "1def4c80-26b9-47d0-b601-cfb485394ff9",
        "ShowroomGUID": "d7e8f9a0-b1c2-4d3e-4f5g-6h7i8j9k0l1m",
        "CadavreGUID": "a89772b8-0b7f-40bd-8760-edc249b9f5da",
        "NewName": "ATteam_FagotM_DDR",
        "GameName": {
            "display": "PALR FAGOT-M",
            "token": "AUVIBEMJSD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_AT",
                "Infanterie_Spec_Defense",
                "UNITE_ATteam_FagotM_DDR",
                "Unite"
            ],
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": 6,
            },
            "equipmentchanges": {
                "replace": [("ATGM_9K111_Fagot", "ATGM_9K111M_Faktoriya")]
            },
        },
        "CommandPoints": 35,
        "SpecialtiesList": [
            '_resolute',
            'infantry_equip_heavy',
        ],
        "UpgradeFromUnit": "ATteam_Fagot_DDR",
        "ButtonTexture": "ATteam_Fagot_DDR",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "RDA_7_Panzer_multi": {
                "Transports": ["UAZ_469_trans_DDR", "BTR_50_DDR", "BMP_1_SP1_DDR", "BMP_1_SP2_DDR", "BMP_1P_DDR"],
            },
            "RDA_9_Panzer_multi": {
                "Transports": ["UAZ_469_trans_DDR", "BMP_1_SP1_DDR", "BMP_1_SP2_DDR", "BMP_1P_DDR"],
            },
            "RDA_KdA_Bezirk_Erfurt_multi": {
                "Transports": ["UAZ_469_trans_DDR"],
            },
        },
        "availability": [7, 5, 4, 0],
        "max_speed": 20,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/Attack', 'EOrderType/MoveAndAttack',
                   'EOrderType/Shoot', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_DDR", "D_DDR"),
        "servant_types": {
            "showroom": {
                "G_DDR": ["ATGMServantLeft"],
                "D_DDR": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_DDR": ["ATGMServantLeft"],
                "D_DDR": ["ATGMServantRight"]
            },
        }
    },
    
    ("T54B_CMD_DDR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "f7652424-a88a-41c5-837d-a0e25713c036",
        "GroupeCombatGUID": "c0304787-17d4-4277-bc87-7bb405aa4876",
        "ShowroomGUID": "04f02987-77e8-40de-a214-b0f6abf047b2",
        "CadavreGUID": "2eb3afbb-2015-4f06-a410-a0d2e29f90eb",
        "NewName": "T54B_CMD2_DDR",
        "GameName": {
            "token": "CRMEBWSIWS",
            "display": "#CMD FüPz T-54AMK",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T54B_CMD2_DDR",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 200,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_resolute',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "RDA_KdA_Bezirk_Erfurt_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
    },

    ("T55A_CMD_DDR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "257bde27-dc1e-4899-ab2f-c6edf9c4af76",
        "GroupeCombatGUID": "e7a7acba-d937-427a-9035-7e4f957cf778",
        "ShowroomGUID": "376f5cd3-f3ef-4bd0-80c9-61ffe40e38a6",
        "CadavreGUID": "96ae475b-77da-4775-bb65-6cc436c23015",
        "NewName": "T55A_CMD2_DDR",
        "GameName": {
            "display": "#CMD FüPz T-55AK",
            "token": "LSXHWRLFEM",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T55A_CMD2_DDR",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 205,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_resolute',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "RDA_4_MSD_multi": {
                "Transports": None,
            },
            "RDA_7_Panzer_multi": {
                "cards": 2,
                "Transports": None,
            },
            "RDA_Rugen_Gruppierung": {
                "Transports": None,
            },
            "WP_Unternehmen_Zentrum_multi": {
                "cards": 2,
                "Transports": None,
            },
        },
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
    },

    ("T55AM2_CMD_DDR", 0): {  # T-55AM Merida CV
        "GUID": "45a64f6d-3512-4d15-9307-10022d6ad4e4",
        "GroupeCombatGUID": "f16d2db0-0ac0-4929-bdcb-cf574be8da4f",
        "ShowroomGUID": "f29b94d3-7dd9-4c05-a31b-53fd5a9c76df",
        "CadavreGUID": "372beca7-a92e-4df4-bbe2-da4ebd0b95fa",
        "NewName": "T55AM2_CMD2_DDR",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "T55AM2_CMD2_DDR",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 255,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_smoke_launcher',
        ],
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
    },

    ("T72M_CMD_DDR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "983055d0-fd20-4e45-bd7c-aa49fa29ca02",
        "GroupeCombatGUID": "da74e4f0-2b89-4ddf-8dc7-e866bf171845",
        "ShowroomGUID": "f8a9b0c1-d2e3-4f5g-6h7i-8j9k0l1m2n3o",
        "CadavreGUID": "3f275f69-0fdf-4e49-9f14-a3bfc4e0b471",
        "NewName": "T72M_CMD2_DDR",
        "GameName": {
            "display": "#CMD FüPz T-72MK",
            "token": "DBXQVRQECV",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T72M_CMD2_DDR",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 290,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_resolute',
            '_smoke_launcher',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "RDA_4_MSD_multi": {
                "Transports": None,
            },
            "RDA_7_Panzer_multi": {
                "Transports": None,
            },
            "RDA_9_Panzer_multi": {
                "Transports": None,
            },
            "RDA_Rugen_Gruppierung": {
                "Transports": None,
            },
            "WP_Unternehmen_Zentrum_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "UpgradeFromUnit": "T55A_CMD2_DDR",
    },

    ("T72M1_CMD_DDR", 0): {  # T-72M1K CV - stats copied from T-72M1D POL
        "GUID": "1f959432-d175-45bd-8016-e97a918227e0",
        "GroupeCombatGUID": "3253ab9a-0c2d-4d3a-b0b8-92bfc824b381",
        "ShowroomGUID": "6ff34493-d566-430c-a501-2b1fb7c980fd",
        "CadavreGUID": "63454739-09a9-4377-bddd-4125e18c2425",
        "GameName": {
            "display": "#CMD FüPz T-72M1K",
            "token": "FUPZTSTMOK",
        },
        "NewName": "T72M1_CMD2_DDR",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T72M1_CMD2_DDR",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 310,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_resolute',
            '_smoke_launcher',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "RDA_9_Panzer_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "UpgradeFromUnit": "T72M_CMD2_DDR",
    },
    
    ("T72M1_DDR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "199faa87-81d3-48bf-8fca-b331756a8a8c",
        "GroupeCombatGUID": "98f2a222-2df1-44be-b552-8c94960f4578",
        "ShowroomGUID": "e42dc1dc-4d1e-4526-bb56-15f32c1eee8a",
        "CadavreGUID": "60d5682a-895b-42b0-9ee7-0600fa8917ab",
        "NewName": "9_Panzer_T72M1_DDR",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_Standard",
                "GroundUnits",
                "SM_charLourd",
                "UNITE_9_Panzer_T72M1_DDR",
                "Unite",
            ],
        },
        "GameName": {
            "display": "#7PANZER KPzT-72M1",
            "token": "ZXTTDHOZUI",
        },
        "CommandPoints": 180,
        "Divisions": {
            "default": {
                "cards": 2, 
            },
            "RDA_7_Panzer_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 0, 4, 3],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "is_replacement": True,
        "Faction": "PACT",
        "Nation": "DDR",
        "UpgradeFromUnit": "T72M_DDR",
    },

    # Infantry

    ("ATteam_Fagot_FJ_DDR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "b24fbc1d-e1cd-4bd2-bd71-7bd9926f58b5",
        "GroupeCombatGUID": "81fac455-2f48-49da-9e81-e2409d6f73fb",
        "ShowroomGUID": "61bb438f-1039-4e0c-9931-82750f1e5eec",
        "CadavreGUID": "1e24d282-7acd-48eb-8968-940e2d20409b",
        "NewName": "ATteam_FagotM_FJ_DDR",
        "GameName": {
            "display": "Fs-PALR FAGOT-M",
            "token": "UILHHWRPGD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_AT",
                "Infanterie_Spec_Defense",
                "UNITE_ATteam_FagotM_FJ_DDR",
                "Unite"
            ],
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": 6,
            },
            "equipmentchanges": {
                "replace": [("ATGM_9K111M_Faktoriya", "ATGM_9K111M_Faktoriya")]
            },
        },
        "CommandPoints": 35,
        "SpecialtiesList": [
                '_para',
                '_resolute',
                'infantry_equip_heavy'
            ],
        "UpgradeFromUnit": "ATteam_Fagot_FJ_DDR",
        "availability": [0, 0, 7, 5],
        "max_speed": 20,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/Attack', 'EOrderType/MoveAndAttack', 
                   'EOrderType/Shoot', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load', 
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_FJ_DDRL", "D_FJ_DDR"),
        "servant_types": {
            "showroom": {
                "G_FJ_DDR": ["ATGMServantLeft"],
                "D_FJ_DDR": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_FJ_DDR": ["ATGMServantLeft"],
                "D_FJ_DDR": ["ATGMServantRight"]
            },
        },
    },

    ("ATteam_Fagot_FJ_DDR", 1): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "297c834b-9f52-4b2f-a467-f88dbf4244f3",
        "GroupeCombatGUID": "ff7745cb-ea97-4e1d-ac7a-42df52791e08",
        "ShowroomGUID": "51182ac7-2b39-4f89-a694-168f023c8fd3",
        "CadavreGUID": "39eecf61-55ca-49a0-ad56-04afe0fcb541",
        "NewName": "ATteam_Konkurs_FJ_DDR",
        "GameName": {
            "display": "Fs-PALR KONKURS",
            "token": "XTXNXPQTZH",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_AT",
                "Infanterie_Spec_Defense",
                "UNITE_ATteam_Konkurs_FJ_DDR",
                "Unite"
            ],
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9M113_Konkurs": 6,
            },
            "equipmentchanges": {
                "replace": [("ATGM_9K111M_Faktoriya", "ATGM_9M113_Konkurs")]
            },
        },
        "CommandPoints": 45,
        "SpecialtiesList": [
                '_para',
                '_resolute',
                'infantry_equip_heavy'
            ],
        "UpgradeFromUnit": "ATteam_FagotM_FJ_DDR",
        "availability": [0, 0, 7, 5],
        "max_speed": 20,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/Attack', 'EOrderType/MoveAndAttack', 
                   'EOrderType/Shoot', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load', 
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_FJ_DDRL", "D_FJ_DDR"),
        "servant_types": {
            "showroom": {
                "G_FJ_DDR": ["ATGMServantLeft"],
                "D_FJ_DDR": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_FJ_DDR": ["ATGMServantLeft"],
                "D_FJ_DDR": ["ATGMServantRight"]
            },
        },
    },

    ("HMGteam_PKM_FJ_DDR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "46a1e2d7-2210-4e4e-b6ed-bcaa85525265",
        "GroupeCombatGUID": "6ed53486-dcf5-4ca8-8368-0fc0c05d0dfd",
        "ShowroomGUID": "8f674126-c7c2-4067-ab28-36bf3429409e",
        "CadavreGUID": "da989fc0-b192-4730-9da4-dfd9d5541b3c",
        "NewName": "HMGteam_NSV_FJ_DDR",
        "depictions": {
            "custom": {
                "DepictionVehicles.ndf": ["TacticVehicleDepictionRegistration", "DepictionOperator_WeaponContinuousFire"],
            },
            "alternatives": "HMGteam_NSV_DDR",
        },
        "GameName": {
            "display": "Fs-NSV 12,7mm",
            "token": "FPGTXESVLM",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Defense",
                "UNITE_HMGteam_NSV_FJ_DDR",
                "Unite"
            ],
        },
        "TransportedSoldier": "HMGteam_NSV_FJ_DDR",
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_NSVT": 48,
            },
            "equipmentchanges": {
                "replace": [("MMG_team_7_62mm_PKM", "HMG_team_12_7_mm_NSV", "MMG_team_7_62mm_PKM", "HMG_team_12_7_mm_NSV")]
            },
        },
        "CommandPoints": 25,
        "SpecialtiesList": [
                '_para',
                '_resolute',
                'infantry_equip_veryheavy'
            ],
        "UpgradeFromUnit": "HMGteam_PKM_FJ_DDR",
        "availability": [0, 0, 10, 7],
        "max_speed": 14,
        "strength": 5,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/Attack', 'EOrderType/MoveAndAttack', 
                   'EOrderType/Shoot','EOrderType/AskForSupply', 'EOrderType/ShootOnPosition', 'EOrderType/UnloadFromTransport', 'EOrderType/UnloadAtPosition', 'EOrderType/Load',
                   'EOrderType/ShootOnPositionWithoutCorrection','EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_FJ_DDRL", "D_FJ_DDR"),
        "servant_types": {
            "showroom": {
                "G_FJ_DDR": ["ATGMServantLeft"],
                "D_FJ_DDR": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_FJ_DDR": ["ATGMServantLeft"],
                "D_FJ_DDR": ["ATGMServantRight"]
            },
        },
    },

    ("HMGteam_PKM_FJ_DDR", 1): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "83beab40-d237-4840-af85-5351834e7a37",
        "GroupeCombatGUID": "dac3c31c-5882-4bba-9cb9-53435e7d36f5",
        "ShowroomGUID": "fb2d887f-b0dc-47b6-89c7-53a10f355364",
        "CadavreGUID": "cd269c11-feb5-4ea1-8ef9-e3845f58cc89",
        "NewName": "HMGteam_AGS17_FJ_DDR",
        "GameName": {
            "display": "Fs-GR.-MG 30mm",
            "token": "QHOSQDALMW",
        },
        "depictions": {
            "custom": {
                "DepictionVehicles.ndf": ["TacticVehicleDepictionRegistration", "DepictionOperator_WeaponInstantFire"],
            },
            "alternatives": "HMGteam_AGS17_DDR",
        },
        "TagSet": {
            "overwrite_all": [    
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Defense",
                "UNITE_HMGteam_AGS17_FJ_DDR",
                "Unite"
            ],
        },
        "TransportedSoldier": "HMGteam_AGS17_FJ_DDR",
        "WeaponDescriptor": {
            "Salves": {
                "Lance_grenade_AGS17": 30,
            },
            "equipmentchanges": {
                "replace": [("MMG_team_7_62mm_PKM", "Lance_grenade_AGS17", "MMG_team_7_62mm_PKM", "Lance_grenade_AGS17")]
            },
        },
        "CommandPoints": 30,
        "SpecialtiesList": [
                '_para',
                '_resolute',
                'infantry_equip_veryheavy'
            ],
        "UpgradeFromUnit": "HMGteam_NSV_FJ_DDR",
        "availability": [0, 0, 8, 6],
        "max_speed": 14,
        "strength": 5,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/Attack', 'EOrderType/MoveAndAttack', 
                   'EOrderType/Shoot', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection','EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_FJ_DDRL", "D_FJ_DDR"),
        "servant_types": {
            "showroom": {
                "G_FJ_DDR": ["ATGMServantLeft"],
                "D_FJ_DDR": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_FJ_DDR": ["ATGMServantLeft"],
                "D_FJ_DDR": ["ATGMServantRight"]
            },
        },
    },

    # Tank

    ("PT76B_CMD_DDR", 0): {  # PT-76B LDR
        "GUID": "11f92429-0da5-4c32-a5fc-95292c277fda",
        "GroupeCombatGUID": "507aa56d-6875-4b05-8aa5-21464360b536",
        "ShowroomGUID": "e65bd9bb-fd99-4316-9146-f5ec494ad462",
        "CadavreGUID": "957a042c-fe88-4a9d-9aa3-2c4e789f03e4",
        "NewName": "PT76B2_CMD_DDR",
        "GameName": {
            "display": "#LDRSOV FüPz PT-76B",
            "token": "WTDVRSZIAP",
        },
        "TagSet": {
            "overwrite_all": [    
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T54B_CMDactual_POL",
                "Unite",
            ],
        },
        "Factory": "EFactory/Tanks",
        "UnitRole": 'armor',
        "CommandPoints": 30,
        "SpecialtiesList": [
                'leader_sov',
            ],
        "UpgradeFromUnit": None,
        "availability": [0, 0, 8, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "remove_zone_capture": None,
    },

    ("AT_D44_85mm_DDR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "edf2ccc0-cd21-41f3-b360-00bd6a2b535a",
        "GroupeCombatGUID": "de11395f-bb79-4c1f-94da-3ac8fe8180c0",
        "ShowroomGUID": "84e76070-8997-4044-8d3d-cfc36a8bbf2d",
        "CadavreGUID": "a808cbb3-cc0b-44e4-a240-8f424bdd89c7",
        "NewName": "AT_D44_85mm_FJ_DDR",
        "GameName": {
            "display": "Fs-PaK D-44 85mm",
            "token": "YGDUAPVTPS",
        },
        "depictions": {
            "custom": {
                "DepictionVehicles.ndf": ["TacticVehicleDepictionRegistration", "DepictionOperator_WeaponInstantFire"],
            },
        },
        "TagSet": {
            "overwrite_all": [    
                "AllUnits",
                "AllowedForMissileRoE",
                "ChasseurDeChar",
                "ChasseurDeChar_canon_AT",
                "GroundUnits",
                "UNITE_AT_D44_85mm_FJ_DDR",
                "Unite",
                "Unite_transportable",
            ],
        },
        "TransportedSoldier": "AT_D44_85mm_FJ_DDR",
        "SpecialtiesList": [
                '_resolute',
                '_para',
            ],
        "UpgradeFromUnit": None,
        "availability": [0, 0, 9, 7],
        "DeploymentShift": 1750,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/Attack', 'EOrderType/MoveAndAttack', 
                   'EOrderType/Shoot', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection','EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_FJ_DDRL", "D_FJ_DDR"),
        "servant_types": {
            "showroom": {
                "G_FJ_DDR": ["ATGMServantLeft"],
                "D_FJ_DDR": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_FJ_DDR": ["ATGMServantLeft"],
                "D_FJ_DDR": ["ATGMServantRight"]
            },
        },
    },

    ("UAZ_469_Fagot_DDR", 0): {  # Fs-UAZ-469 FAGOT-M
        "GameName": {
            "display": "Fs-UAZ-469 FAGOT-M",
            "token": "NBMMUMLTJE",
        },
        "GUID": "6cea194d-2284-444b-abbb-b3a51b07ff5c",
        "GroupeCombatGUID": "0139d60a-20c3-42de-934d-443a17adb815",
        "ShowroomGUID": "94ff8fc9-e3cd-4b01-bfbe-507525503b9a",
        "CadavreGUID": "38f2aa67-4230-48a5-ae23-d00cad44d7eb",
        "NewName": "UAZ_469_Fagot_FJ_DDR",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_UAZ_469_Fagot_FJ_DDR",
                "Unite",
                "Vehicule",
                "Vehicule_faible"
            ],
        },
        "Factory": "EFactory/Tanks",
        "CommandPoints": 35,
        "UnitRole": 'AT',
        "SpecialtiesList": [
            '_resolute',
            '_para',
        ],
        "DeploymentShift": 1750,
        "ButtonTexture": "UAZ_469_Fagot_DDR",
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
    },
}
# fmt: on
