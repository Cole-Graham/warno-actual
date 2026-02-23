"""New unit definitions for Soviet Union."""

# fmt: off
SOV_NEW_UNITS = {
    ("MotRifles_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "ae9979f0-0bb1-47f3-b4f6-c4e820ad2a06",
        "GroupeCombatGUID": "e9462050-a89d-456b-915d-a68d7edafd17",
        "ShowroomGUID": "c7b5a9d8-e4f2-4c16-9d3b-8a2e4f7c6b5d",
        "CadavreGUID": "4a793ae9-5f90-41e1-b8a2-b9203e527de5",
        "NewName": "MotRifles_CMD2_SOV",
        "GameName": {
            # "display": "#CMD KOMANDNOE OTDELENIE",
            "display": "#CMD KOM. OTDELENIE",
            "token": "FFFKSMMRGR",
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
                "UNITE_MotRifles_CMD2_SOV",
                "Unite",
            ],
        },
        "strength": 5,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        "Dangerousness": 12,
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "Sniper_SVD_Dragunov": 100,
                "RocketInf_RPG22_72_5mm": 5
            },
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 4,
                },
            },
        },
        "Salves": [7, 100, 5, 3],
        "TransportedTexture": "UseInGame_Transport_COMMAND",
        "TransportedSoldier": "MotRifles_SOV",
        "armor": "Infantry_armor_reference",
        "Factory": "EFactory/Logistic",
        "CommandPoints": 145,
        "UnitAttackValue": 1,
        "UnitDefenseValue": 16,
        "UnitRole": 'hq_inf',
        "SpecialtiesList": [
            'leader_sov',
            'infantry_equip_light',
        ],
        "MenuIconTexture": "Texture_RTS_H_CMD_inf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/CMD_Inf",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_119IndTkBrig_multi": {
                "Transports": ["UAZ_469_SOV", "BTR_80_SOV", "Mi_2_trans_SOV", "Mi_8TV_non_arme_SOV", "Mi_8TV_SOV"],
            },
            "SOV_35_AirAslt_Brig_multi": {
                "Transports": ["LUAZ_967M_SOV", "Mi_8TV_non_arme_SOV", "Mi_8MTV_SOV", "Mi_24D_Desant_SOV"],
            },
            "SOV_76_VDV_multi": {
                "Transports": ["LUAZ_967M_SOV", "BTR_D_SOV"],
            },
            "SOV_79_Gds_Tank_multi": {
                "Transports": ["UAZ_469_SOV", "BTR_60_SOV", "Mi_2_trans_SOV", "Mi_8TV_non_arme_SOV", "Mi_8TV_SOV"],
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
        "Faction": "PACT",
        "Nation": "SOV",
        "alternatives_count": 4,
        "selector_tactic": "02_04",
    },

    ("MotRifles_CMD_TTsko_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "e3e48926-a5ee-492a-b6f9-c772b8a90924",
        "GroupeCombatGUID": "9a2f1fad-0e56-4f46-8345-b125fda7314a",
        "ShowroomGUID": "b1c2d3e4-f5g6-4h7i-8j9k-l0m1n2o3p4q5",
        "CadavreGUID": "b852d941-cba8-42e6-867a-7ecf24be522b",
        "NewName": "MotRifles_CMD2_TTsko_SOV",
        "GameName": {
            # "display": "#CMD KOMANDNOE OTDELENIE",
            "display": "#CMD KOM. OTDELENIE",
            "token": "PKHNVEPCJL",
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
                "UNITE_MotRifles_CMD2_TTsko_SOV",
                "Unite",
            ],
        },
        "strength": 5,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        "Dangerousness": 12,
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "Sniper_SVD_Dragunov": 100,
                "RocketInf_RPG22_72_5mm": 5
            },
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 4,
                },
            },
        },
        "TransportedTexture": "UseInGame_Transport_COMMAND",
        "TransportedSoldier": "MotRifles_TTsko_SOV",
        "armor": "Infantry_armor_reference",
        "Factory": "EFactory/Logistic",
        "CommandPoints": 145,
        "UnitAttackValue": 1,
        "UnitDefenseValue": 16,
        "UnitRole": 'hq_inf',
        "SpecialtiesList": [
            'leader_sov',
            'infantry_equip_light',
        ],
        "MenuIconTexture": "Texture_RTS_H_CMD_inf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/CMD_Inf",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle_multi": {
                "Transports": ["UAZ_469_SOV", "BTR_80_SOV", "Mi_2_trans_SOV", "Mi_8TV_non_arme_SOV", "Mi_8TV_SOV"],
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
        "Faction": "PACT",
        "Nation": "SOV",
        "model": "Engineers_CMD_TTsko_SOV",
        "alternatives_count": 4,
        "selector_tactic": "02_04",
    },
    
    ("T55A_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "ce816c42-84bd-4dd1-bdb1-2ac7ef346eed",
        "GroupeCombatGUID": "d504f8c8-c90b-4e7a-a5d9-5409cc08fab9",
        "ShowroomGUID": "24505a1a-f485-46f5-b232-4c473533e889",
        "CadavreGUID": "f19ca0de-4193-499e-8467-0b5418bb9bc4",
        "NewName": "T55A_CMD2_SOV",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T55A_CMD2_SOV",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 205,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
        ],
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
        "Nation": "SOV",
    },

    ("T62M_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "c2ac3a2f-1057-4ec9-9899-7f393b33ac82",
        "GroupeCombatGUID": "0dc2bcb7-29cc-4d6c-9f71-f6db00824499",
        "ShowroomGUID": "e6094770-c5e4-425c-971e-cc579665e64d",
        "CadavreGUID": "5c2534eb-fcc8-4737-8f6f-b57d720d1313",
        "NewName": "T62M_CMD2_SOV",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T62M_CMD2_SOV",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 265,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_smoke_launcher',
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
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "SOV",
    },

    ("T62MD_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "81f3dffc-6d6b-4ae8-bd1d-71a93e7da2d6",
        "GroupeCombatGUID": "39f721e9-7bc3-4d42-ba9b-1830253380e2",
        "ShowroomGUID": "cf476f51-97c1-4944-9dcd-2df24a002933",
        "CadavreGUID": "8eb9e440-a1c8-44ae-b739-75245f48d11c",
        "NewName": "T62MD_CMD2_SOV",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T62MD_CMD2_SOV",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 265,
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
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "SOV",
    },

    ("T64B_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "9bf644a7-043e-4d01-9731-901c51a5e574",
        "GroupeCombatGUID": "f42eacb6-8364-45fd-b58f-19c3be63b7b6",
        "ShowroomGUID": "4be95367-4a61-49e5-b23f-d871f128db58",
        "CadavreGUID": "affcaa18-b675-4261-8188-2016a025127c",
        "NewName": "T64B_CMD2_SOV",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T64B_CMD2_SOV",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 320,
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
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "SOV",
    },

    ("T72M1_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "47d21a4b-c990-4ca9-a357-e7cbfb49fe28",
        "GroupeCombatGUID": "88605290-8a7f-4a1b-943b-9a25b761bb97",
        "ShowroomGUID": "2760c8bd-e31a-4620-8550-cc5d8b001d06",
        "CadavreGUID": "91efeb67-8d2d-4e1d-bbad-01c9f8d01a8d",
        "NewName": "T72M1_CMD2_SOV",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T72M1_CMD2_SOV",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 310,
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
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "SOV",
    },

    ("T72B_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "139d6b80-8f85-4789-96dd-34c5f8ddf42f",
        "GroupeCombatGUID": "77ff57b2-800b-4e39-8870-6f03868c53d8",
        "ShowroomGUID": "04f8b0aa-63f7-4989-8407-5ce7716ccecc",
        "CadavreGUID": "6133b463-f467-4eb7-86b2-1fd887bc1c1a",
        "NewName": "T72B_CMD2_SOV",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T72B_CMD2_SOV",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 355,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_smoke_launcher',
            '_era',
        ],
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
        "Nation": "SOV",
    },

    ("T80BV_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "7885fe97-44c5-4ec9-92ea-dea7d1335a23",
        "GroupeCombatGUID": "993eaf28-65c8-4c9d-bbf0-37c296fe5466",
        "ShowroomGUID": "e6f7g8h9-i0j1-4k2l-3m4n-5o6p7q8r9s0t",
        "CadavreGUID": "ac22fe6a-7e23-49b8-823d-4f68ad83cf7c",
        "NewName": "T80BV_CMD2_SOV",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T80BV_CMD2_SOV",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "armor": {
            "front": (18, None),
        },
        "CommandPoints": 355,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_smoke_launcher',
            '_era',
        ],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle_multi": {
                "Transports": None,
            },
            "SOV_39_Gds_Rifle_multi": {
                "Transports": None,
            },
            "SOV_79_Gds_Tank_multi": {
                "Transports": None,
            },
            "SOV_119IndTkBrig_multi": {
                "cards": 2,
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
        "Nation": "SOV",
    },
    # MT-LBu
    ("MTLB_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "ddc1a5b9-cc08-494a-a9dc-7d8b35591505",
        "GroupeCombatGUID": "41959c7e-e732-453f-91d5-000729d068e5",
        "ShowroomGUID": "847a7325-445a-44ba-bfcb-24c03dfaad07",
        "CadavreGUID": "fe1ea57b-0847-4688-9618-d0f814126711",
        "NewName": "MTLB_CMD2_SOV",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_MTLB_CMD2_SOV",
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
        ],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle_multi": {
                "Transports": None,
            },
            "SOV_39_Gds_Rifle_multi": {
                "Transports": None,
            },
            "SOV_79_Gds_Tank_multi": {
                "Transports": None,
            },
            "SOV_119IndTkBrig_multi": {
                "Transports": None,
            },
            "SOV_6IndMSBrig_multi": {
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
        "Nation": "SOV",
    },

    ("MotRifles_TTsko_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "21a5481c-bf7f-45b8-9c22-bb6885850521",
        "GroupeCombatGUID": "f41497ec-862f-4321-b628-0b6fb0b80b27",
        "ShowroomGUID": "a4ac9eac-d74d-4da1-91d6-f2c08dd11ad3",
        "CadavreGUID": "9d790fe8-5668-4757-b532-6d70f411d232",
        "NewName": "MotRifles_RPG7V_TTsko_SOV",
        "GameName": {
            "display": "MOTOSTRELKI",
            "token": "UQYYVBRKGT",
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
                "Infanterie_Standard",
                "Steelman_infanterie_autoresolve",
                "UNITE_MotRifles_RPG7_TTsko_SOV",
                "Unite",
            ],
        },
        "strength": 8,
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "SAW_RPK_74_5_56mm": 18,
                "RocketInf_RPG7VL": 6,
            },
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 7,
                },
                "replace": [
                    ("RocketInf_RPG27_105mm", "RocketInf_RPG7VL", "RocketInf_RPG27_105mm", "RocketInf_RPG7VL"),
                ],
            },
        },
        "TransportedSoldier": "MotRifles_RPG7V_TTsko_SOV",
        "armor": "Infantry_armor_reference",
        "CommandPoints": 30,
        "UnitRole": 'infantry',
        "SpecialtiesList": [
                '_ifv',
                'infantry_equip_medium',
            ],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle_multi": {
                "Transports": ["GAZ_66_SOV", "BTR_80_SOV", "BMP_1P_SOV", "BMP_2AG_SOV", "BMP_3_SOV"],
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/SmartMove', 'EOrderType/Attack', 'EOrderType/SmartMoveAndAttack', 'EOrderType/MoveAndAttack',
                   'EOrderType/Shoot', 'EOrderType/ShootOnPosition', 'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load', 'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "SOV",
        "UpgradeFromUnit": "MotRifles_BTR_TTsko_SOV",
        "alternatives_count": 4,
        "selector_tactic": "00_04",
    },

    ("ATteam_Fagot_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "22caa472-c587-4816-b3b4-913e7c2316f4",
        "GroupeCombatGUID": "674ce341-9c4a-4da2-9f3e-4b4e6f6c2358",
        "ShowroomGUID": "c419b0c4-6f4e-435b-8e1f-fb74b33cf884",
        "CadavreGUID": "d0a2edad-e8c8-4073-8b90-cdfadcd3a78e",
        "NewName": "ATteam_Faktoriya_SOV",
        "GameName": {
            "display": "FAKTORIYA",
            "token": "ZADIQTXXXX",
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
                "UNITE_ATteam_Faktoriya_SOV",
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
        "CommandPoints": 40,
        "SpecialtiesList": [
                'infantry_equip_heavy',
            ],
        "ButtonTexture": "Atteam_Konkurs_DShV_SOV",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_39_Gds_Rifle_multi": {
                "Transports": ["UAZ_469_SOV", "BTR_60_SOV", "BMP_1P_SOV"],
            },
            "SOV_35_AirAslt_Brig_multi": {
                "Transports": ["UAZ_469_SOV", "BTR_D_Robot_SOV"],
            },
            "SOV_79_Gds_Tank_multi": {
                "Transports": ["UAZ_469_SOV", "BMP_1P_SOV"],
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
        "Nation": "SOV",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_SOV", "D_SOV"),
        "servant_types": {
            "showroom": {
                "G_SOV": ["ATGMServantLeft"],
                "D_SOV": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_SOV": ["ATGMServantLeft"],
                "D_SOV": ["ATGMServantRight"]
            },
        }
    },

    ("Atteam_Fagot_VDV_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "60fff50e-03da-402c-bbec-15424522f06d",
        "GroupeCombatGUID": "bcd261dd-e99e-4f6c-9f0e-4ffa0e470bb4",
        "ShowroomGUID": "d2e3f4g5-h6i7-4j8k-9l0m-n1o2p3q4r5s6",
        "CadavreGUID": "24612725-41c9-4d25-821b-d0e6e9377a11",
        "NewName": "ATteam_Faktoriya_VDV_SOV",
        "GameName": {
            "display": "DESANT. FAKTORIYA",
            "token": "YDMQOTJZVZ",
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
                "UNITE_ATteam_Faktoriya_VDV_SOV",
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
        "CommandPoints": 40,
        "SpecialtiesList": [
                '_para',
                'infantry_equip_heavy'
            ],
        "UpgradeFromUnit": "Atteam_Fagot_VDV_SOV",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_76_VDV_multi": {
                "Transports": ["LUAZ_967M_SOV", "BTR_D_Robot_SOV"],
            },
        },
        "availability": [0, 7, 5, 4],
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
        "Nation": "SOV",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_VDV", "Spe_D_VDV"),
        "servant_types": {
            "showroom": {
                "G_VDV": ["ATGMServantLeft"],
                "Spe_D_VDV": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_VDV": ["ATGMServantLeft"],
                "Spe_D_VDV": ["ATGMServantRight"]
            },
        }
    },
} 
# fmt: on
