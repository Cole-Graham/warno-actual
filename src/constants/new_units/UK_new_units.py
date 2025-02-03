"""New unit definitions for UK."""

# fmt: off
UK_NEW_UNITS = {
    "Rifles_CMD_UK": { # donor unit
        "GUID": "1f764bcc-3c0f-4a39-90b3-43d97e749441",
        "GroupeCombatGUID": "f89e6ee3-40ac-4ef8-a6eb-5c1373cb51d7",
        "ShowroomGUID": "b2e1d9c4-a7f8-4b53-9c6e-d5f4e3a2c1b8",
        "CadavreGUID": "b1352738-64fe-4c41-8505-7fdb44402f6d",
        "NewName": "Rifles_CMD2_UK",
        "GameName": {
            "display": "#CMD HQ SECTION",
            "token": "UEBNKKQYYZ",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits", "AllowedForMissileRoE", "Commandant", "Crew", "GroundUnits", "Inf_quartier_ok", 
                "Infanterie", "Infanterie_CMD", "InfmapCommander", "UNITE_Rifles_CMD2_UK", "Unite",
            ],
        },
        "strength": 5,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        "Dangerousness": 12,
        "WeaponAssignment": [
                (0,[1,]),
                (1,[0,]),
                (2,[0,]),
                (3,[0,3]),
                (4,[0,2,]),
            ],
        "WeaponDescriptor": {
            "Salves": {
                "FM_L85A1": 11,
                "L7A2_7_62mm": 30,
                "RocketInf_M72A3_LAW_66mm": 5,
            },
            "equipmentchanges": {
                "quantity": {
                    "FM_L85A1": 4,
                },
            },
        },
        "TransportedTexture": "UseInGame_Transport_COMMAND",
        "TransportedSoldier": "Rifles_UK",
        "Factory": "EDefaultFactories/Logistic",

        "CommandPoints": 145,
        "UnitAttackValue": 1,
        "UnitDefenseValue": 16,
        "SpecialitiesList": [
                'hq_inf',
                '_leader',
                '_ifv',
                'infantry_equip_light',
            ],
        "MenuIconTexture": "Texture_RTS_H_CMD_inf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/CMD_Inf",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "UK_2nd_Infantry_multi": {
                "Transports": ["Bedford_MJ_4t_trans_UK", "MCV_80_Warrior_UK", "Lynx_AH_Mk1_UK"],
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
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
        "Faction": "NATO",
        "Nation": "UK",
        "alternatives_count": 5,
        "selector_tactic": "2, 5",
    },
    
    "Challenger_1_Mk1_CMD_UK": { # donor unit
        "GUID": "d8a0de03-ee46-49c5-ba51-24320c053d55",
        "GroupeCombatGUID": "5d21c985-c92a-4975-b0f3-74ed1a7920b8",
        "ShowroomGUID": "c4d5e6f7-8a9b-4c5d-6e7f-8a9b0c1d2e3f",
        "CadavreGUID": "e8f48e53-2ad0-4d41-ac9f-f6d24a3f2e77",
        "NewName": "Challenger_1_Mk1_CMD2_UK",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_Challenger_1_Mk1_CMD2_UK",
                "Unite",
            ],
        },
        "Factory": "EDefaultFactories/Logistic",
        "CommandPoints": 290,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "UK_1st_Armoured_multi": {
                "Transports": None,
            },
            "UK_2nd_Infantry_multi": {
                "Transports": None,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Attack', 'FastMoveAndAttack', 
                   'MoveAndAttack', 'Spread', 'Reverse', 'Shoot', 'ShootOnPosition', 
                   'ShootOnPositionWithoutCorrection', 'ShootDefensiveSmoke', 'AskForSupply', 
                   'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "UK",
    },
}
# fmt: on
