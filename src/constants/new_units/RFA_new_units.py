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
        "Factory": "EDefaultFactories/Logistic",
        "CommandPoints": 145,
        "SpecialitiesList": [
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
            "US_11ACR_multi": {
                "Transports": ["Iltis_trans_RFA", "Marder_1A3_RFA", "Marder_1A3_MILAN_RFA"],
                "cards": 1,  # + 1 card TACOM
            },
        },
        "availability": [0, 0, 2, 0],
        "max_speed": 26,
        "Orders": ['Stop', 'Move', 'FollowFormation', 'SmartMove', 'Attack', 'SmartMoveAndAttack', 'MoveAndAttack',
                   'Spread', 'Shoot', 'ShootOnPosition', 'ShootOnPositionWithoutCorrection', 'ShootOnPositionSmoke',
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
}
# fmt: on
