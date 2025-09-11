"""New unit definitions for RDA."""

# fmt: off
RDA_NEW_UNITS = {
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
        "WeaponAssignment": [
            (0, [1]),
            (1, [0]),
            (2, [0]),
            (3, [0, 3]),
            (4, [0, 2]),
        ],
        "WeaponDescriptor": {
            "Salves": {
                "FM_Mpi_AK_74N": 7,
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
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "RDA_7_Panzer_multi": {
                "Transports": ["UAZ_469_trans_DDR", "BTR_70_DDR", "Mi_2_trans_DDR", "Mi_8T_non_arme_DDR", "Mi_8T_DDR"],
            },
        },
        "availability": [0, 0, 2, 0],
        "max_speed": 26,
        "Orders": ['Stop', 'Move', 'FollowFormation', 'SmartMove', 'Attack', 'SmartMoveAndAttack', 'MoveAndAttack',
                   'Shoot', 'ShootOnPosition', 'ShootOnPositionWithoutCorrection', 'ShootOnPositionSmoke',
                   'ShootOnPositionWithoutCorrectionSmoke', 'AskForSupply', 'EnterDistrict', 'LoadIntoTransport', 'Load',
                   'AIDefend', 'AIAttack', 'AIStop'],
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
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
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
            "RDA_KdA_Bezirk_Erfurt_multi": {
                "Transports": None,
                },
        },
        "availability": [0, 3, 0, 0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Reverse',
                   'AskForSupply', 'AIDefend', 'AIAttack', 'AIStop'],
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
        "CommandPoints": 40,
        "SpecialtiesList": [
            'AT',
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
        },
        "availability": [7, 5, 4, 0],
        "max_speed": 20,
        "Orders": ['Stop', 'Move', 'FollowFormation', 'Attack', 'MoveAndAttack', 'Spread',
                   'Shoot', 'AskForSupply', 'EnterDistrict', 'LoadIntoTransport', 'Load',
                   'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "DDR",
        "depiction_type": "Towed",
        "alternatives_count": 2,
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
        "CommandPoints": 190,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_resolute',
        ],
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
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
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Attack', 'FastMoveAndAttack',
                   'MoveAndAttack', 'Reverse', 'Shoot', 'ShootOnPosition',
                   'ShootOnPositionWithoutCorrection', 'AskForSupply',
                   'AIDefend', 'AIAttack', 'AIStop'],
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
        "CommandPoints": 265,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_resolute',
            '_smoke_launcher',
        ],
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
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
            "RDA_Rugen_Gruppierung": {
                "Transports": None,
            },
            "WP_Unternehmen_Zentrum_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 0, 2, 0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Attack', 'FastMoveAndAttack',
                   'MoveAndAttack', 'Reverse', 'Shoot', 'ShootOnPosition',
                   'ShootOnPositionWithoutCorrection', 'ShootDefensiveSmoke', 'AskForSupply',
                   'AIDefend', 'AIAttack', 'AIStop'],
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
        "CommandPoints": 285,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_resolute',
            '_smoke_launcher',
        ],
        # "Decks": {
        #     "packs": {
        #         "rename": True, 
        #     },
        # },
        # "Divisions": {
        #     "default": {
        #         "cards": 1,
        #     },
        #     "POL_20_Pancerna_multi": {
        #         "Transports": None,
        #     },
        # },
        "availability": [0, 0, 2, 0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Attack', 'FastMoveAndAttack',
                   'MoveAndAttack', 'Reverse', 'Shoot', 'ShootOnPosition',
                   'ShootOnPositionWithoutCorrection', 'ShootDefensiveSmoke', 'AskForSupply',
                   'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": False,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
        "UpgradeFromUnit": "T72M_CMD2_DDR",
    },
}
# fmt: on
