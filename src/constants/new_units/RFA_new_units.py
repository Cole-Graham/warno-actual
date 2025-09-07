"""New unit definitions for RDA."""

# fmt: off
RFA_NEW_UNITS = {
    ("Engineers_CMD_RFA", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "8c7f95ed-4fce-491e-9151-29ed2a49fc6a",
        "GroupeCombatGUID": "64e00b37-e760-4493-89ab-28caa9c825d2",
        "ShowroomGUID": "410ea2b1-7671-4061-ad6d-0228d39c973c",
        "CadavreGUID": "c95f3f05-66f0-4a2a-b66f-1396d103d186",
        "NewName": "Engineers_CMD2_RFA",
        "GameName": {
            "display": "#CMD FÜHRUNGSGRUPPE",
            "token": "WGERCMDINF",
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
                "UNITE_Engineers_CMD2_RFA",
                "Unite",
            ],
        },
        "strength": 5,
        "WeaponAssignment": [
            (0, [0]),
            (1, [0]),
            (2, [0]),
            (3, [0]),
            (4, [0, 1]),
        ],
        "WeaponDescriptor": {
            "Salves": {
                "PM_uzi": 7,
                "RocketInf_Carl_Gustav": 5,
            },
        },
        "TransportedTexture": "UseInGame_Transport_COMMAND",
        "TransportedSoldier": "Engineers_CMD_RFA",
        "armor": "Infantry_armor_reference",
        "Factory": "EFactory/Logistic",
        "CommandPoints": 145,
        "SpecialtiesList": [
            'hq_inf',
            '_leader',
            'infantry_equip_medium',
        ],
        "MenuIconTexture": "Texture_RTS_H_CMD_inf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/CMD_Inf",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "RFA_2_PzGrenadier_multi": {
                "Transports": ["Iltis_trans_RFA", "TPZ_Fuchs_1_RFA", "TPZ_Fuchs_MILAN_RFA"],
            },
            "RFA_5_Panzer_multi": {
                "Transports": ["Iltis_trans_RFA", "TPZ_Fuchs_1_RFA", "TPZ_Fuchs_MILAN_RFA"],
            },
            "RFA_TerrKdo_Sud_multi": {
                "Transports": ["Iltis_trans_RFA"],
            },
            "US_11ACR_multi": {
                "Transports": ["Iltis_trans_RFA", "Marder_1A3_RFA", "Marder_1A3_MILAN_RFA"],
                "cards": 1,  # + 1 card TACOM
            },
        },
        "availability": [0, 0, 2, 0],
        "max_speed": 26,
        "Orders": ['Stop', 'Move', 'FollowFormation', 'SmartMove', 'Attack', 'SmartMoveAndAttack', 'MoveAndAttack',
                   'Shoot', 'ShootOnPosition', 'ShootOnPositionWithoutCorrection', 'ShootOnPositionSmoke',
                   'ShootOnPositionWithoutCorrectionSmoke', 'AskForSupply', 'EnterDistrict', 'LoadIntoTransport',
                   'Load', 'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": True,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "RFA",
        "alternatives_count": 1,
        "selector_tactic": "00_01",
    },

    ("M577_RFA", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "712fd59c-3baa-434d-b904-b07c5e9c4003",
        "GroupeCombatGUID": "d1157c11-5816-4ff9-897b-fd49e0fad863",
        "ShowroomGUID": "432efe92-ddce-40da-af72-6508b094186b",
        "CadavreGUID": "ade35527-8206-4c07-a8b3-38da179b3629",
        "NewName": "M577_CMD2_RFA",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_M577_CMD2_RFA",
                "Unite",
                "Vehicule",
                "Vehicule_CMD",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "RFA_2_PzGrenadier_multi": {
                "Transports": None,
            },
            "RFA_5_Panzer_multi": {
                "Transports": None,
            },
            "RFA_TerrKdo_Sud_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 3, 0, 0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Spread',
                   'Reverse', 'AskForSupply', 'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": True,
        "Faction": "NATO",
        "Nation": "RFA",
    },
}
# fmt: on
