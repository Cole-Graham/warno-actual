"""New unit definitions for POL."""

# fmt: off
POL_NEW_UNITS = {
    "Rifles_CMD_POL": { # donor unit
        "GUID": "420dc280-c718-45a3-8edd-a022767e7773",
        "GroupeCombatGUID": "ff07058f-392e-477f-8eea-ec8ef042d0c6",
        "ShowroomGUID": "3585f744-fa44-4b2c-99af-2a50f4220b11",
        "CadavreGUID": "39caafd5-cb26-4aaf-8d9c-d3a0db6c23ec",
        "NewName": "Rifles_CMD2_POL",
        "GameName": {
            "display": "#CMD SZTAB DOWODZENIA",
            "token": "SZTABDOWPL",
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
                "UNITE_Rifles_CMD2_POL",
                "Unite",
            ],
        },
        "strength": 5,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        # "Dangerousness": 12,
        "WeaponAssignment": [
                (0, [1]),
                (1, [0]),
                (2, [0]),
                (3, [0, 3]),
                (4, [0, 2]),
            ],
        "WeaponDescriptor": {
            "Salves": {
                "FM_kbk_AK": 7,
                "RocketInf_RPG76_Komar": 5,
            },
            "equipmentchanges": {
                "quantity": {
                    "FM_kbk_AK": 4,
                },
            },
        },
        "TransportedTexture": "UseInGame_Transport_COMMAND",
        "TransportedSoldier": "Rifles_CMD_POL",
        "Factory": "EDefaultFactories/Logistic",
        "CommandPoints": 145,
        "UnitAttackValue": 1,
        "UnitDefenseValue": 16,
        "SpecialitiesList": [
            'hq_inf',
            'leader_sov',
            'infantry_equip_light',
        ],
        "MenuIconTexture": "Texture_RTS_H_CMD_inf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/CMD_Inf",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "POL_20_Pancerna_multi": {
                "Transports": ["UAZ_469_trans_POL", "MTLB_trans_POL", "BMP_1_SP2_POL", "BMP_2_POL", "Mi_2_trans_POL"],
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 2/2, 0.0],
        "max_speed": 26,
        "Orders": ['Stop', 'Move', 'FollowFormation', 'SmartMove', 'Attack', 'SmartMoveAndAttack', 'MoveAndAttack', 
                   'Spread', 'Shoot', 'ShootOnPosition', 'ShootOnPositionWithoutCorrection', 'ShootOnPositionSmoke',
                   'ShootOnPositionWithoutCorrectionSmoke', 'AskForSupply', 'EnterDistrict', 'LoadIntoTransport', 'Load',
                   'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
        "alternatives_count": 5,
        "selector_tactic": "2, 5",
    },

    "T55A_CMD_POL": {  # donor unit
        "GUID": "f85c67f5-5738-43ff-bae2-a92bfa88d83d",
        "GroupeCombatGUID": "6773a9af-c9e6-4d3f-a41c-953be75f966e",
        "ShowroomGUID": "2cf23742-85b4-4b75-a280-133aff0a63b6",
        "CadavreGUID": "1b246f95-d334-4219-bbe2-630ed38b013b",
        "NewName": "T55A_CMD2_POL",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T55A_CMD2_POL",
                "Unite",
            ],
        },
        "Factory": "EDefaultFactories/Logistic",
        "CommandPoints": 190,
        "SpecialitiesList": [
            'hq_tank',
            'leader_sov',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "POL_20_Pancerna_multi": {
                "Transports": None,
            },
            "POL_4_Zmechanizowana_multi": {
                "Transports": None,
                "cards": 2,
            },
            "POL_Korpus_Desantowy_multi": {
                "Transports": None,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 2/2, 0.0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Attack', 'FastMoveAndAttack',
                   'MoveAndAttack', 'Spread', 'Reverse', 'Shoot', 'ShootOnPosition',
                   'ShootOnPositionWithoutCorrection', 'AskForSupply',
                   'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": False,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
    },

    "T72M_CMD_POL": {  # donor unit
        "GUID": "dd59b59a-5698-4a72-b16c-71ec2bdc9064",
        "GroupeCombatGUID": "56fecca1-ce12-4cfb-9675-2ef6bb48e033",
        "ShowroomGUID": "65e63a59-27d9-4978-b3ba-93e44f91379c",
        "CadavreGUID": "a3f4a792-bdd7-48c8-a70f-dfe28ec0b129",
        "NewName": "T72M_CMD2_POL",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T72M_CMD2_POL",
                "Unite",
            ],
        },
        "Factory": "EDefaultFactories/Logistic",
        "CommandPoints": 255,
        "SpecialitiesList": [
            'hq_tank',
            'leader_sov',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "POL_20_Pancerna_multi": {
                "Transports": None,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 2/2, 0.0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Attack', 'FastMoveAndAttack',
                   'MoveAndAttack', 'Spread', 'Reverse', 'Shoot', 'ShootOnPosition',
                   'ShootOnPositionWithoutCorrection', 'ShootDefensiveSmoke', 'AskForSupply',
                   'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": False,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
        "UpgradeFromUnit": "T55A_CMD2_POL",
    },

    "T72M1_CMD_POL": {  # donor unit
        "GUID": "c292163d-73b2-47dd-9f39-ad607bd75a14",
        "GroupeCombatGUID": "f71b3c68-eb90-46ec-8ac3-5c75273b0212",
        "ShowroomGUID": "217706ae-a44b-4d9a-9b89-a516bf04207b",
        "CadavreGUID": "1b9dae2d-80ce-4331-be82-311b2ed53b29",
        "NewName": "T72M1_CMD2_POL",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T72M1_CMD2_POL",
                "Unite",
            ],
        },
        "Factory": "EDefaultFactories/Logistic",
        "CommandPoints": 285,
        "SpecialitiesList": [
            'hq_tank',
            'leader_sov',
            '_smoke_launcher',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "POL_20_Pancerna_multi": {
                "Transports": None,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 2/2, 0.0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Attack', 'FastMoveAndAttack',
                   'MoveAndAttack', 'Spread', 'Reverse', 'Shoot', 'ShootOnPosition',
                   'ShootOnPositionWithoutCorrection', 'ShootDefensiveSmoke', 'AskForSupply',
                   'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": False,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
        "UpgradeFromUnit": "T72M_CMD2_POL",
    },
}
# fmt: on
