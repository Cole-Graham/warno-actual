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
        # "Dangerousness": 12,
        "WeaponDescriptor": {
            "Salves": {
                "FM_kbk_AK": 11,
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
        "armor": "Infantry_armor_reference",
        "Factory": "EFactory/Logistic",
        "CommandPoints": 145,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
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
            "POL_20_Pancerna_multi": {
                "cards": 1,
                "Transports": [
                    "UAZ_469_trans_POL",
                    "BMP_1_SP2_POL",
                    "OT_64_SKOT_2A_POL",
                    "Mi_2_trans_POL",
                    "Mi_24D_POL",
                ],
            },
            "POL_4_Zmechanizowana_multi": {
                "cards": 1,
                "Transports": [
                    "UAZ_469_trans_POL",
                    "BMP_1_SP2_POL",
                    "OT_64_SKOT_2A_POL",
                    "Mi_2_trans_POL",
                    "Mi_24D_POL",
                ],
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
        "Nation": "POL",
        "alternatives_count": 4,
        "selector_tactic": "02_04",
    },

    ("ASU_85_CMD_POL", 0): {  # ASU-85 CMD
        "GUID": "c0194429-3a64-4e52-a9a7-67cec54592e2",
        "GroupeCombatGUID": "6575d3ea-db2a-42bf-aff3-5bdcf3b50373",
        "ShowroomGUID": "c1ebe660-2108-429c-bf7f-24d8224510e5",
        "CadavreGUID": "8470bf3d-e203-4841-a528-ae547622908a",
        "NewName": "ASU_85_CMD2_POL",
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
        "Factory": "EFactory/Logistic",
        "CommandPoints": 190,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
        ],
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
        "GameName": {
            "display": "#CMD ASU-85D",
            "token": "POLTASUEFC",
        },
    },

    ("T55A_CMD_POL", 2): {  # T-54B CMD
        "GUID": "23dd9821-54ed-4320-bd58-dce59331d9fc",
        "GroupeCombatGUID": "15f04b2f-f19f-433d-a659-3801250e5ffc",
        "ShowroomGUID": "bf3555f0-d3af-4024-a8f9-980967b84cfd",
        "CadavreGUID": "8a4d7cd6-3a6b-453b-9e11-342982ac2bc3",
        "NewName": "T54B_CMD2_POL",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T54B_CMD2_POL",
                "Unite",
            ],
        },
        "GameName": {
            "display": "#CMD T-54BD",
            "token": "POLTFFBC",
        },
        "Factory": "EFactory/Tanks",
        "CommandPoints": 200,
        "UnitRole": 'armor',
        "SpecialtiesList": [
            'leader_sov',
        ],
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
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
        "Factory": "EFactory/Logistic",
        "CommandPoints": 205,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
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
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
    },

    ("T55AM_Merida_CMD_POL", 0): {  # T-55AM Merida CV
        "GUID": "0ed06908-888a-4535-881f-5e714b21a1e4",
        "GroupeCombatGUID": "7c76c4fe-53a0-4508-ad01-2683a195fc34",
        "ShowroomGUID": "a9ce6acc-5f50-4994-8518-e1aa378f200b",
        "CadavreGUID": "24ee87a1-9b71-4e72-aa2d-66e5b720ea91",
        "NewName": "T55AM_Merida_CMD2_POL",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "T55AM_Merida_CMD2_POL",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 255,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            'leader_sov',
            '_smoke_launcher',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "POL_4_Zmechanizowana_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
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
        "Factory": "EFactory/Logistic",
        "CommandPoints": 275,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
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
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
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
        "Factory": "EFactory/Logistic",
        "CommandPoints": 310,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
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
        "availability": [0, 0, 2, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
        "UpgradeFromUnit": "T72M_CMD2_POL",
    },

    ("T55A_CMD_POL", 1): {  # T-54B Ldr.
        "GUID": "ce7aac18-0994-4f41-b5dd-35b8c9b8d434",
        "GroupeCombatGUID": "9ab3d76b-e841-4944-96e8-b6be76bdde98",
        "ShowroomGUID": "e07a7e81-164b-43b1-98a6-5ecf33509420",
        "CadavreGUID": "cbd9c1a8-134c-4521-b84e-605ed4d7af99",
        "NewName": "T54B_CMDactual_POL",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T54B_CMDactual_POL",
                "Unite",
            ],
        },
        "GameName": {
            "display": "#LDRSOV T-54BD LDR.",
            "token": "POLTFFBD",
        },
        "Factory": "EFactory/Tanks",
        "CommandPoints": 75,
        "UnitRole": 'armor',
        "SpecialtiesList": [
            'leader_sov',
        ],
        "availability": [0, 0, 6, 0],
        "remove_zone_capture": None,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
    },

    ("OT_64_SKOT_2_POL", 0): {  # SKOT R-2AM LDR
        "GUID": "35b514f1-55d8-4c63-86c0-ff0604547fb4",
        "GroupeCombatGUID": "fb1db3c4-ed80-4a3a-b8f8-1eab529da04e",
        "ShowroomGUID": "6211126c-6458-4edc-8e7e-a7d17338c60a",
        "CadavreGUID": "8f3685da-a277-41c1-8870-3d60c6acc84f",
        "modules_add": ["TCommanderModuleDescriptor()"],
        "modules_remove": ["WeaponDescriptor", "WeaponManager", "Transporter", "~/TargetManagerModuleDescriptor"],
        "depictions": {
            "custom": {
                "DepictionVehicles.ndf": ["TacticVehicleDepictionRegistration"],
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
            "AcknowUnitTypes": ["Command"],
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
        "Factory": "EFactory/Art",
        "CommandPoints": 60,
        "UnitRole": 'leader_sov',
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
        "availability": [0, 2, 0, 0],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Reverse',
                   'EOrderType/AskForSupply', 'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
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
        "CommandPoints": 35,
        "SpecialtiesList": [
            'infantry_equip_heavy',
        ],
        "UpgradeFromUnit": "Atteam_Fagot_POL",
        "ButtonTexture": "Atteam_Fagot_POL",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "POL_4_Zmechanizowana_multi": {
                "Transports": ['UAZ_469_trans_POL', 'OT_64_SKOT_2AM_POL'],
            },
            "POL_20_Pancerna_multi": {
                "Transports": ['UAZ_469_trans_POL', 'MTLB_trans_POL', 'BMP_1_SP2_POL', 'BMP_2_POL'],
            },
        },
        "availability": [7, 5, 4, 0],
        "max_speed": 20,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/Attack', 'EOrderType/MoveAndAttack',
                   'EOrderType/Shoot', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True,  # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "needs_transport": True,
        "Faction": "PACT",
        "Nation": "POL",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_POL", "D_POL"),
        "servant_types": {
            "showroom": {
                "G_POL": ["ATGMServantLeft"],
                "D_POL": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_POL": ["ATGMServantLeft"],
                "D_POL": ["ATGMServantRight"]
            },
        }
    },

    ("Atteam_Fagot_Para_POL", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "24abfd2b-f4c6-4377-a1dc-29719cc9c2ad",
        "GroupeCombatGUID": "3ec286bd-3931-4d6a-8354-89d2e1360197",
        "ShowroomGUID": "f5e0ff9b-e75d-45b7-9106-9852e53ead09",
        "CadavreGUID": "b9e1df75-08a7-4ee7-9e9a-a272763652ac",
        "NewName": "Atteam_Konkurs_Para_POL",
        "GameName": {
            "display": "SPADO. PPK KONKURS",
            "token": "WODNYOJNVF",
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
                "UNITE_Atteam_Konkurs_Para_POL",
                "Unite"
            ],
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9M113_Konkurs": 6,
            },
            "equipmentchanges": {
                "replace": [("ATGM_9K111_Fagot", "ATGM_9M113_Konkurs")]
            },
        },
        "CommandPoints": 45,
        "SpecialtiesList": [
                '_para',
                'infantry_equip_heavy'
            ],
        "UpgradeFromUnit": "Atteam_Fagot_Para_POL",
        "availability": [0, 6, 4, 0],
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
        "Nation": "POL",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_Para_POL", "D_Para_POL"),
        "servant_types": {
            "showroom": {
                "G_Para_POL": ["ATGMServantLeft"],
                "D_Para_POL": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_Para_POL": ["ATGMServantLeft"],
                "D_Para_POL": ["ATGMServantRight"]
            },
        },
        "UpgradeFromUnit": "Atteam_Fagot_Para_POL",
    },

    ("HMGteam_PKM_para_POL", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "02f68c8d-483d-4787-927a-9db855de0e5f",
        "GroupeCombatGUID": "7a140754-7160-44fb-8233-ac9b1096abd1",
        "ShowroomGUID": "aead18dd-0321-4534-a292-e7a2b52a81f3",
        "CadavreGUID": "e1fa2afd-f15e-4d24-9981-5c482fe4cbf7",
        "NewName": "HMGteam_NSV_para_POL",
        "depictions": {
            "custom": {
                "DepictionVehicles.ndf": ["TacticVehicleDepictionRegistration", "DepictionOperator_WeaponContinuousFire"],
            },
            "alternatives": "HMGteam_NSV_POL",
        },
        "GameName": {
            "display": "SPADO. NSV 12,7mm",
            "token": "JNBWVSQPZV",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Defense",
                "UNITE_HMGteam_NSV_para_POL",
                "Unite"
            ],
        },
        "TransportedSoldier": "HMGteam_NSV_para_POL",
        "WeaponDescriptor": {
            "Salves": {
                "HMG_12_7_mm_NSVT": 48,
            },
            "equipmentchanges": {
                "replace": [("MMG_team_7_62mm_PKM", "HMG_team_12_7_mm_NSV", "MMG_team_7_62mm_PKM", "HMG_team_12_7_mm_NSV")]
            },
        },
        "CommandPoints": 25,
        "SpecialtiesList": [
                '_para',
                'infantry_equip_veryheavy'
            ],
        "UpgradeFromUnit": "HMGteam_PKM_para_POL",
        "availability": [0, 10, 7, 0],
        "max_speed": 14,
        "strength": 5,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/Attack', 'EOrderType/MoveAndAttack', 
                   'EOrderType/Shoot','EOrderType/AskForSupply', 'EOrderType/ShootOnPosition', 'EOrderType/UnloadFromTransport', 'EOrderType/UnloadAtPosition', 'EOrderType/Load',
                   'EOrderType/ShootOnPositionWithoutCorrection','EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_Para_POL", "D_Para_POL"),
        "servant_types": {
            "showroom": {
                "G_Para_POL": ["ATGMServantLeft"],
                "D_Para_POL": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_Para_POL": ["ATGMServantLeft"],
                "D_Para_POL": ["ATGMServantRight"]
            },
        },
    },

    ("HMGteam_PKM_para_POL", 1): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "4734c29a-2afe-4c03-baca-964c750825fc",
        "GroupeCombatGUID": "dda90888-7c16-410b-bb1b-6c7576df5def",
        "ShowroomGUID": "c3a0e94a-4d8b-403b-9e69-316f977990a1",
        "CadavreGUID": "4a5322be-f90f-418d-8d20-87768d1faa05",
        "NewName": "HMGteam_AGS17_para_POL",
        "GameName": {
            "display": "SPADO. AGS-17 30mm",
            "token": "LEAGOMIHPJ",
        },
        "depictions": {
            "custom": {
                "DepictionVehicles.ndf": ["TacticVehicleDepictionRegistration", "DepictionOperator_WeaponInstantFire"],
            },
            "alternatives": "HMGteam_AGS17_POL",
        },
        "TagSet": {
            "overwrite_all": [    
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Defense",
                "UNITE_HMGteam_AGS17_para_POL",
                "Unite"
            ],
        },
        "TransportedSoldier": "HMGteam_AGS17_para_POL",
        "WeaponDescriptor": {
            "Salves": {
                "Lance_grenade_AGS17": 30,
            },
            "equipmentchanges": {
                "replace": [("MMG_team_7_62mm_PKM", "Lance_grenade_AGS17", "MMG_team_7_62mm_PKM", "Lance_grenade_AGS17")]
            },
        },
        "CommandPoints": 30,
        "SpecialtiesList": [
                '_para',
                'infantry_equip_veryheavy'
            ],
        "UpgradeFromUnit": "HMGteam_NSV_para_POL",
        "availability": [0, 8, 6, 0],
        "max_speed": 14,
        "strength": 5,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/Attack', 'EOrderType/MoveAndAttack', 
                   'EOrderType/Shoot', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection','EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_Para_POL", "D_Para_POL"),
        "servant_types": {
            "showroom": {
                "G_Para_POL": ["ATGMServantLeft"],
                "D_Para_POL": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_Para_POL": ["ATGMServantLeft"],
                "D_Para_POL": ["ATGMServantRight"]
            },
        },
    },

    ("Honker_RYS_POL", 0): {  # HONKERS RYS (Transport)
        "GameName": {
            "display": "HONKERS RYS",
            "token": "ZMUZVMFCMK",
        },
        "GUID": "2419def0-6823-40f0-8e64-c646f6ad2d8e",
        "GroupeCombatGUID": "da37a488-aae5-44e2-8c88-2ff19c8639e8",
        "ShowroomGUID": "faae217b-5941-4d12-a0f4-f28628527291",
        "CadavreGUID": "cc4b63e5-182c-4393-9310-7053270a2c96",
        "NewName": "Honker_RYS_trans_POL",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_Honker_RYS_POL",
                "Unite",
                "Vehicule",
                "Vehicule_Transport_Arme",
                "noSIGINT",
            ],
        },
        "Factory": "EFactory/Tanks",
        "CommandPoints": 20,
        "UnitRole": 'transport',
        "SpecialtiesList": [
            '_transport1',
            '_sf',
        ],
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 3500.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/Standard": 45.0,
                "EOpticalStrength/LowAltitude": 45.0,
                "EOpticalStrength/HighAltitude": 10.0,
            },
        },
        "stealth": 1.5,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply', 'EOrderType/UnloadFromTransport', 'EOrderType/UnloadAtPosition', 'EOrderType/Load',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
    },

    ("OT_62_TOPAS_JOD_POL", 0): {  # TOPAS JOD (Transport)
        "GameName": {
            "display": "TOPAS JOD",
            "token": "USEVPJZMYG",
        },
        "GUID": "fe208523-a9ca-4ef2-860e-bf6a12b905ca",
        "GroupeCombatGUID": "058703d8-1efc-4836-89ce-fdf7a195c2d7",
        "ShowroomGUID": "b4e59d7c-5465-4c1b-bb43-217899193ab5",
        "CadavreGUID": "c24a9ca7-b29f-47d0-a041-b1e786809548",
        "NewName": "OT_62_TOPAS_JOD2_POL",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_OT_62_TOPAS_JOD2_POL",
                "Unite",
                "Vehicule",
                "Vehicule_Transport_Arme",
            ],
        },
        "Factory": "EFactory/Tanks",
        "CommandPoints": 40,
        "UnitRole": 'transport',
        "SpecialtiesList": [
            '_transport1',
            '_ifv',
            '_amphibie',
        ],
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply', 'EOrderType/UnloadFromTransport', 'EOrderType/UnloadAtPosition', 'EOrderType/Load',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
    },

    ("UAZ_469_SPG9_Para_POL", 0): {  # UAZ-469 SPG-9 (Non Para)
        "GameName": {
            "display": "UAZ-469 SPG-9",
            "token": "NZMIMFLCIU",
        },
        "GUID": "a6ad7568-566b-44c9-9ecd-cab435c3571d",
        "GroupeCombatGUID": "33190296-883c-4962-8029-c6b2c117d294",
        "ShowroomGUID": "befd547b-c68c-4519-bf87-df910c2f0a85",
        "CadavreGUID": "a48e1365-8229-4df2-a700-a3ce718cfdda",
        "NewName": "UAZ_469_SPG9_POL",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_UAZ_469_SPG9_POL",
                "Unite",
                "Vehicule",
                "Vehicule_faible"
            ],
        },
        "Factory": "EFactory/Infantry",
        "CommandPoints": 25,
        "UnitRole": 'appui',
        "SpecialtiesList": [],
        "DeploymentShift": 0,
        "ButtonTexture": "UAZ_469_SPG9_DDR",
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
    },

    ("AT_D48_85mm_POL", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "0de44fc4-1a87-4146-8e24-0dd8ee7c2d52",
        "GroupeCombatGUID": "ec9269ff-531e-4d45-8bd0-9c3a0b0548cc",
        "ShowroomGUID": "116fa176-1fea-4d10-9782-794c7ba2fa30",
        "CadavreGUID": "04dc2d6f-591d-4c24-9e1e-8f6c032b2e99",
        "NewName": "AT_D48_85mm_Para_POL",
        "GameName": {
            "display": "SPADO. D-48 85mm",
            "token": "GYKTENGDYF",
        },
        "depictions": {
            "custom": {
                "DepictionVehicles.ndf": ["TacticVehicleDepictionRegistration", "DepictionOperator_WeaponInstantFire"],
            },
        },
        "TagSet": {
            "overwrite_all": [    
                "AllUnits",
                "AllowedForMissileRoE",
                "ChasseurDeChar",
                "ChasseurDeChar_canon_AT",
                "GroundUnits",
                "UNITE_AT_D48_85mm_Para_POL",
                "Unite",
                "Unite_transportable",
            ],
        },
        "TransportedSoldier": "AT_D48_85mm_Para_POL",
        "SpecialtiesList": [
                '_para',
            ],
        "UpgradeFromUnit": None,
        "availability": [0, 9, 7, 5],
        "DeploymentShift": 1750,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/Attack', 'EOrderType/MoveAndAttack', 
                   'EOrderType/Shoot', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection','EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "POL",
        "depiction_type": "Towed",
        "alternatives_count": 2,
        "servants": ("G_Para_POL", "D_Para_POL"),
        "servant_types": {
            "showroom": {
                "G_Para_POL": ["ServantLeft"],
                "D_Para_POL": ["ServantRight"]
            },
            "subdepictions": {
                "G_Para_POL": ["ServantLeft"],
                "D_Para_POL": ["ServantRight"]
            },
        },
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
            "POL_Korpus_Desantowy_multi": {
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
        "Nation": "POL",
    },

    ("Engineers_Scout_POL", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "a8123a99-091d-4e7e-9b09-e366848d1907",
        "GroupeCombatGUID": "139beeba-bf5b-48d4-bef1-09780c53f9fc",
        "ShowroomGUID": "3c945163-0eb1-46c0-b9ea-83e4fc58efed",
        "CadavreGUID": "8283ce2a-bf6a-40ea-9af8-81c0565226c0",
        "NewName": "Engineers_Scout_Para_POL",
        "GameName": {
            "display": "#RECO2 SPADO. ZWIAD. SAPERZY",
            "token": "YPBVPYJQXC",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Reco",
                "Radio",
                "Reco",
                "UNITE_Engineers_Scout_Para_POL",
                "Unite"
            ],
        },
        "SpecialtiesList": [
            '_choc',
            '_para',
            'infantry_equip_light',
        ],
        "DeploymentShift": 1750,
        "strength": 8,
        "TransportedSoldier": "Engineers_Scout_Para_POL",
        "armor": "Infantry_armor_reference",
        "ButtonTexture": "Scout_para_POL",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "FM_kbk_AK": 11,
                "MMG_PKM_7_62mm": 36,
            },
        },
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/SmartMove', 'EOrderType/Attack', 'EOrderType/SmartMoveAndAttack', 'EOrderType/MoveAndAttack',
                   'EOrderType/Shoot', 'EOrderType/ShootOnPosition', 'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load', 'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "POL",
        "alternatives_count": 4,
        "selector_tactic": "02_04",
        "unique_count": 2,
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
    #     # "Factory": "EFactory/Logistic",
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
    #     "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition', 'EOrderType/ShootOnPositionWithoutCorrection',
    #                'EOrderType/AirplanePatrol', 'EOrderType/AirplaneAttack', 'EOrderType/AirplaneMoveAndEngage', 'EOrderType/AirplaneEvacuate', 'EOrderType/AirplaneShoot',
    #                'EOrderType/AIAirplaneAutoManage', 'EOrderType/AIStop'],
    #     "availability": [0, 3, 0, 0],
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
