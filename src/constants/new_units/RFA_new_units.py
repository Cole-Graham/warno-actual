"""New unit definitions for RDA."""

# fmt: off
RFA_NEW_UNITS = {
    ("Engineers_CMD_RFA", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "588f60ff-9ec8-4b7a-8120-420261a07249",
        "GroupeCombatGUID": "578b6227-7369-4cd9-9bbc-278e7723f972",
        "ShowroomGUID": "5130c30c-9bf2-4cdd-8b72-cd4cef0dd6b2",
        "CadavreGUID": "f224d57e-a53f-40bc-88dd-c96ecb026e64",
        "NewName": "InfCV_CMD_RFA",
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
                "UNITE_InfCV_CMD_RFA",
                "Unite",
            ],
        },
        "strength": 5,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        "Dangerousness": 12,
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
        "TransportedSoldier": "MotRifles_CMD_DDR",
        "Factory": "EDefaultFactories/Logistic",
        "CommandPoints": 145,
        "UnitAttackValue": 1,
        "UnitDefenseValue": 16,
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
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 2/2, 0.0],
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
        "alternatives_count": 5,
        "selector_tactic": "2, 5",
    },
}
# fmt: on
