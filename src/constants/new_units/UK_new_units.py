"""New unit definitions for UK."""

# fmt: off
UK_NEW_UNITS = {
    ("DCA_M167A2_Vulcan_20mm_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "016266d7-5576-4c95-8885-a9cd0277079a",
        "GroupeCombatGUID": "852cb4c1-67fd-4039-89d9-df1c2ba6c46c",
        "ShowroomGUID": "967df281-0e6b-40af-8c42-65ccb81ca47d",
        "CadavreGUID": "e1eeca97-647d-4296-a631-9ea45800fae9",
        "depictions": {
            "custom": {
                "DepictionVehicles.ndf": ["TacticVehicleDepictionRegistration", "DepictionOperator_WeaponContinuousFire"],
            },
        },
        "NewName": "DCA_M167A2_Vulcan_20mm_UK",
        "GameName": {
            "display": "M167A2 VADS (UK)",
            "token": "XWWJJTOTON",
        },
        "TypeUnit": {
            "MotherCountry": "'UK'",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Canon_AA",
                "Canon_AA_Porte",
                "GroundUnits",
                "UNITE_DCA_M167A2_Vulcan_20mm_UK",
                "Unite",
                "Unite_transportable",
            ],
        },
        "TransportedSoldier": "DCA_M167A2_Vulcan_20mm_UK",
        "Factory": "EFactory/Logistic",
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "UK_2nd_Infantry_multi": {
                "Transports": ["Bedford_MJ_4t_trans_UK"],
            },
        },
        "availability": [6, 4, 0, 0],
        "max_speed": 4,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "FOB_UK",
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack', 'EOrderType/MoveAndAttack',
                   'EOrderType/Shoot', 'EOrderType/ShootOnPosition', 'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/Load', 'EOrderType/Load', 'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "UK",
        "alternatives_count": 2,
        "servants": ("G_UK", "D_UK")
    },

    ("Rifles_CMD_UK", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
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
            (0, [1, ]),
            (1, [0, ]),
            (2, [0, ]),
            (3, [0, 3]),
            (4, [0, 2, ]),
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
        "Factory": "EFactory/Logistic",
        "armor": "Infantry_armor_reference",
        "CommandPoints": 145,
        "UnitAttackValue": 1,
        "UnitDefenseValue": 16,
        "UnitRole": 'hq_inf',
        "SpecialtiesList": [
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
        "availability": [0, 0, 2, 0],
        "max_speed": 26,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/SmartMove', 'EOrderType/Attack', 'EOrderType/SmartMoveAndAttack', 'EOrderType/MoveAndAttack',
                   'EOrderType/Shoot', 'EOrderType/ShootOnPosition', 'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootOnPositionSmoke',
                   'EOrderType/ShootOnPositionWithoutCorrectionSmoke', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "UK",
        "alternatives_count": 5,
        "selector_tactic": "02_05",
    },

    ("Challenger_1_Mk1_CMD_UK", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "d8a0de03-ee46-49c5-ba51-24320c053d55",
        "GroupeCombatGUID": "5d21c985-c92a-4975-b0f3-74ed1a7920b8",
        "ShowroomGUID": "c4d5e6f7-8a9b-4c5d-6e7f-8a9b0c1d2e3f",
        "CadavreGUID": "e8f48e53-2ad0-4d41-ac9f-f6d24a3f2e77",
        "NewName": "Challenger_1_Mk1_CMD2_UK",
        "GameName": {
            "display": "#CMD CHALLENGER Mk.2",
            "token": "RLYOMURBXH",
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
                "UNITE_Challenger_1_Mk1_CMD2_UK",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 315,
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
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack', 
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition', 
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply', 
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
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
