"""New unit definitions for FR."""

# fmt: off
FR_NEW_UNITS = {
    ("Chasseurs_CMD_FR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "416dd19d-49b3-4a23-bd49-9e890f2a1efd",
        "GroupeCombatGUID": "5910ff01-80de-4b1f-a203-629d3fe3cb3b",
        "ShowroomGUID": "8119e3f8-17df-4a7b-a215-5a465642f343",
        "CadavreGUID": "578e09f3-9959-410e-8615-1f90103762c3",
        "NewName": "Chasseurs_CMD2_FR",
        "GameName": {
            "display": "#CMD GROUPE DE CMDT",
            "token": "HLYMDCAYOT",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits", "AllowedForMissileRoE", "Commandant", "Crew", "GroundUnits", "Inf_quartier_ok", 
                "Infanterie", "Infanterie_CMD", "InfmapCommander", "UNITE_Chasseurs_CMD2_FR", "Unite"
            ],
        },
        "strength": 5,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        # "Dangerousness": 12,
        "WeaponAssignment": [
            (0, [0, ]),
            (1, [0, ]),
            (2, [0, ]),
            (3, [0, 1]),
            (4, [0, 2]),
        ],
        "WeaponDescriptor": {
            "Salves": {
                "add": [(2, 4),],
                "FM_FAMAS": 9,
            },
            "equipmentchanges": {
                "add": [(2, "RocketInf_LRAC_F1", "RocketInf_LRAC_F1")],
                "quantity": {
                    "RocketInf_LRAC_F1": 1,
                },
            },
        },
        "TransportedTexture": "UseInGame_Transport_COMMAND",
        "TransportedSoldier": "Chasseurs_CMD2_FR",
        "Factory": "EFactory/Logistic",
        "CommandPoints": 145,
        "SpecialitiesList": [
            'hq_inf',
            '_leader',
            '_ifv',
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
            "FR_5e_Blindee_multi": {
                "Transports": ["TRM_2000_FR", "AMX_10_P_FR", "Super_Puma_FR"],
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
        "Faction": "NATO",
        "Nation": "FR",
        "alternatives_count": 4,
        "selector_tactic": "04_05",
        "unique_count": 4,
    },
    
    ("AMX_30_B2_CMD_FR", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "e1b9b77e-ed05-4415-951f-cbc291d8e3df",
        "GroupeCombatGUID": "21eaa0d7-8acd-4431-a7fd-47329780bb11",
        "ShowroomGUID": "dccaeb21-3a70-4fea-9f4d-bc05f53fd011",
        "CadavreGUID": "86fa429c-aa00-4a30-95e0-9deb1ab09e43",
        "NewName": "AMX_30_B2_CMD2_FR",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_AMX_30_B2_CMD2_US",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 245,
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "FR_5e_Blindee_multi": {
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
        "Faction": "NATO",
        "Nation": "FR",
    },
}
# fmt: on
