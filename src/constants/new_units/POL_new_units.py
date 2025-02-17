"""New unit definitions for POL."""

# fmt: off
POL_NEW_UNITS = {
    ("Rifles_CMD_POL", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
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
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
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
                "cards": 1,
                "Transports": [
                    "UAZ_469_trans_POL",
                    "MTLB_trans_POL",
                    "BMP_1_SP2_POL",
                    "BMP_2_POL",
                    "Mi_2_trans_POL",
                    "Mi_24D_POL",
                ],
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
        "alternatives_count": 4,
        "selector_tactic": "2, 4",
    },

    ("T55A_CMD_POL", 0): {  # T-55AD CV
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

    ("T72M_CMD_POL", 0): {  # T-72MD CV
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

    ("T72M1_CMD_POL", 0): {  # T-72M1D CV
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
    
    ("OT_64_SKOT_2_POL", 0): {  # SKOT R-2AM LDR
        "GUID": "35b514f1-55d8-4c63-86c0-ff0604547fb4",
        "GroupeCombatGUID": "fb1db3c4-ed80-4a3a-b8f8-1eab529da04e",
        "ShowroomGUID": "6211126c-6458-4edc-8e7e-a7d17338c60a",
        "CadavreGUID": "8f3685da-a277-41c1-8870-3d60c6acc84f",
        "modules_add": ["TCommanderModuleDescriptor()"],
        "modules_remove": ["WeaponDescriptor", "WeaponManager", "Transporter"],
        "depictions": {
            "custom": {
                "DepictionVehicles.ndf": ["TacticVehicleDepictionTemplate"],
            },
            "cadavre": {
                "remove_modules": ["WeaponManager", "Transporter"],
            },
        },
        "NewName": "OT_64_SKOT_2_CMD_POL",
        "GameName": {
            "display": "#LDRSOV SKOT R-2AM",
            "token": "RTBIJFPDGK",
        },
        "TypeUnit": {
            "AcknowUnitType": "~/TAcknowUnitType_Command",
            "TypeUnitFormation": "'Supply'",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_OT_64_SKOT_2_CMD_POL",
                "Unite",
                "Vehicule",
                "Vehicule_CMD",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_CMD_veh", "Texture_CMD_veh"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "Factory": "EDefaultFactories/Art",
        "CommandPoints": 60,
        "SpecialitiesList": [
            'leader_sov',
        ],
        "InfoPanelConfig": "Default",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "POL_20_Pancerna_multi": {
                "Transports": None,
            },
            "POL_4_Zmechanizowana_multi": {
                "Transports": None,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 2/2, 0.0, 0.0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Spread', 'Reverse', 
                   'AskForSupply', 'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": True,
        "Faction": "PACT",
        "Nation": "POL",
    },

    ("Atteam_Fagot_POL", 0): {  # PPK Faktoria
        "GUID": "a4f73e0b-8b70-4c8d-bcee-440a4c79fb6e",
        "GroupeCombatGUID": "37d0eb0b-25b4-4351-bd94-db17bfccfce5",
        "ShowroomGUID": "24fd6fc3-aaff-4f8b-b46e-63a5188edcab",
        "CadavreGUID": "2a3d92a7-1ab7-4bc1-94be-916ac8b06ab4",
        "NewName": "ATteam_FagotM_POL",
        "GameName": {
            "display": "PPK FAKTORIA",
            "token": "FAKTORIAPL",
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
        "SpecialitiesList": [
            'AT',
            'infantry_equip_heavy',
        ],
        "UpgradeFromUnit": "Atteam_Fagot_POL",
        "ButtonTexture": "Atteam_Fagot_POL",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "POL_20_Pancerna_multi": {
                "Transports": ['UAZ_469_trans_POL', 'MTLB_trans_POL', 'BMP_1_SP2_POL'],
            },
        },
        "availability": 7,
        "XPMultiplier": [7/7, 5/7, 4/7, 0.0],
        "max_speed": 20,
        "Orders": ['Stop', 'Move', 'FollowFormation', 'Attack', 'MoveAndAttack', 'Spread',
                   'Shoot', 'AskForSupply', 'EnterDistrict', 'LoadIntoTransport', 'Load',
                   'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": True,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
        "depiction_type": "Towed",
        "alternatives_count": 2,
    },

    ("OT_62_TOPAS_R3M_CMD_POL", 0): {  # NIEB. BERETY TOPAS R-3M
        "GameName": {
            "display": "#CMD TOPAS R-3M",
            "token": "MUGMPUTSYS",
        },
        "GUID": "a40a0809-44e9-4f2d-a85b-c2927c736712",
        "GroupeCombatGUID": "5b78e35d-682b-47a4-b0e0-5d5059825b57",
        "ShowroomGUID": "871cf1cb-8457-4f8e-a3db-115ad7a2f8e9",
        "CadavreGUID": "aa84aa16-69c0-4145-9b88-fd27dbfc94a6",
        "NewName": "OT_62_TOPAS_R3M_CMD2_POL",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_OT_62_TOPAS_R3M_CMD2_POL",
                "Unite",
                "Vehicule",
                "Vehicule_CMD",
            ],
        },
        "Factory": "EDefaultFactories/Logistic",
        "CommandPoints": 145,
        "SpecialitiesList": [
            'hq_veh',
            'leader_sov',
            '_amphibie',
        ],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "POL_Korpus_Desantowy_multi": {
                "Transports": None,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 3/3, 0.0, 0.0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Spread', 'Reverse',
                   'AskForSupply', 'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": True,
        "Faction": "PACT",
        "Nation": "POL",
    },

    # ("MiG_23MF_AA_POL", 0): {  # MiG-23MF [AA3]
    #     "GameName": {
    #         "display": "MiG-23MF [AA3]",
    #         "token": "MIG23MFAA3",
    #     },
    #     "GUID": "1b34c5cf-ed1f-48ce-9db3-f227dfa3cce7",
    #     "GroupeCombatGUID": "701c25c0-7522-46b3-b2bf-d3614701d7c5",
    #     "ShowroomGUID": "ec350db0-6b05-428c-8659-5fc40fff3820",
    #     "CadavreGUID": "d7249c56-d85b-41b6-8bc1-f1d8e2ba6fd8",
    #     "NewName": "MiG_23MF_AA3_POL",
    #     # "TagSet": {
    #     #     "overwrite_all": [
    #     #         "AllUnits",
    #     #         "AllowedForMissileRoE",
    #     #         "Commandant",
    #     #         "GroundUnits",
    #     #         "InfmapCommander",
    #     #         "UNITE_OT_62_TOPAS_R3M_CMD2_POL",
    #     #         "Unite",
    #     #         "Vehicule",
    #     #         "Vehicule_CMD",
    #     #     ],
    #     # },
    #     # "Factory": "EDefaultFactories/Logistic",
    #     # "CommandPoints": 145,
    #     "Divisions": {
    #         "default": {
    #             "cards": 2,
    #         },
    #         "POL_4_Zmechanizowana_multi": {
    #             "Transports": None,
    #         },
    #     },
    #     "WeaponDescriptor": {
    #         "equipmentchanges": {
    #             "replace": [("AA_R23R_Vympel", "AA_R60M_Vympel")],
    #         },
    #     },
    #     "Orders": ['Stop', 'Move', 'FollowFormation', 'Shoot', 'ShootOnPosition', 'ShootOnPositionWithoutCorrection',
    #                'AirplanePatrol', 'AirplaneAttack', 'AirplaneMoveAndEngage', 'AirplaneEvacuate', 'AirplaneShoot',
    #                'AIAirplaneAutoManage', 'AIStop'],
    #     "availability": 3,
    #     "XPMultiplier": [0.0, 3/3, 0.0, 0.0],
    #     "is_infantry": False, # False for Javelin LML (unique exception), towed units.
    #     "is_heavy_equipment": False,
    #     "is_ground_vehicle": False,
    #     "is_aerial": True,
    #     "is_unarmed": False,
    #     "Faction": "PACT",
    #     "Nation": "POL",
    # },
}
# fmt: on
