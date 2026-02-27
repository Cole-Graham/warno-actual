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
                   'EOrderType/ShootOnPositionWithoutCorrectionSmoke', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/UseCapacite',
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
                   'EOrderType/ShootOnPositionWithoutCorrectionSmoke', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/UseCapacite',
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
                   'EOrderType/AskForSupply', 'EOrderType/UseCapacite', 'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
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
                   'EOrderType/Shoot', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/UseCapacite',
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
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply', 'EOrderType/UseCapacite',
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
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply', 'EOrderType/UseCapacite',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
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
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply', 'EOrderType/UseCapacite',
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
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply', 'EOrderType/UseCapacite',
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
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply', 'EOrderType/UseCapacite',
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
}
# fmt: on
