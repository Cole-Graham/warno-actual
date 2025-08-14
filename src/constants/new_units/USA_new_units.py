"""New unit definitions for US."""

# fmt: off
USA_NEW_UNITS = {
    ("Rifles_half_CMD_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "b022b55d-ed0f-4a4f-ba79-79ab8d7f21b4",
        "GroupeCombatGUID": "70931c7c-04ef-4d92-bf10-137416584504",
        "ShowroomGUID": "d4f8e3a2-b6c1-4d95-8e7a-f2c9d1b3e5a7",
        "CadavreGUID": "2b771f4e-f0e0-464e-bafb-caee6bb82079",
        "NewName": "Rifles_half_CMD2_US",
        "GameName": {
            "display": "#CMD TACOM",
            "token": "ZVQUJZFLND",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits", "AllowedForMissileRoE", "Commandant", "Crew", "GroundUnits", "Inf_quartier_ok", 
                "Infanterie", "Infanterie_CMD", "InfmapCommander", "UNITE_Rifles_half_CMD2_US", "Unite"
            ],
        },
        "strength": 5,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        # "Dangerousness": 12,
        "WeaponAssignment": [
            (0, [1, ]),
            (1, [1, ]),
            (2, [1, ]),
            (3, [0, 3]),
            (4, [0, 2, ]),
        ],
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "Commando_733": 7,
                "M72A3_LAW_66mm": 5,
            },
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 2,
                    "Commando_733": 3,
                },
            },
        },
        "TransportedTexture": "UseInGame_Transport_COMMAND",
        "TransportedSoldier": "Rifles_half_LAW_US",
        "Factory": "EFactory/Logistic",
        "CommandPoints": 145,
        "UnitAttackValue": 1,
        "UnitDefenseValue": 16,
        "SpecialitiesList": [
            'hq_inf',
            '_leader',
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
            "US_101st_Airmobile_multi": {  # all M1038 changed to M998 - revert if u want
                "Transports": ["M998_Humvee_US", "UH60A_Black_Hawk_US"],
            },
            "US_11ACR_multi": {
                "Transports": ["M998_Humvee_US", "UH60A_Black_Hawk_US"],
                "cards": 1,  # + 1 card RFA cmd inf
            },
            "US_24th_Inf_multi": {
                "Transports": ["M998_Humvee_US", "UH60A_Black_Hawk_US"],
            },
            "US_35th_Inf_multi": {
                "Transports": ["M998_Humvee_US", "UH60A_Black_Hawk_US"],
            },
            "US_3rd_Arm_multi": {
                "Transports": ["M998_Humvee_US", "UH60A_Black_Hawk_US"],
            },
            "US_82nd_Airborne_multi": {
                "Transports": ["M998_Humvee_US", "UH60A_Black_Hawk_US"],
            },
            "US_8th_Inf_multi": {
                "Transports": ["M998_Humvee_US", "UH60A_Black_Hawk_US"],
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
        "Nation": "US",
        "alternatives_count": 10,
        "selector_tactic": "00_10",
    },
    
    ("M1038_Humvee_US", 0): {
        "GUID": "e1db01b4-f48e-4c46-a9b3-284668573864",
        "GroupeCombatGUID": "7941cf9e-4bb2-4fe2-a9f4-d301c3a14000",
        "ShowroomGUID": "c6fc6686-20f2-4a61-8873-c5fd90ad23d1",
        "CadavreGUID": "cd105858-c974-493d-b327-5c68849f3833",
        "modules_add": [
                """TSupplyModuleDescriptor
                (
                    SupplyDescriptor = $/GFX/Weapon/SquadSupply
                    SupplyCapacity = 675.0
                    SupplyPriority = -1
                )""",
            ],
        "modules_remove": ["TTransporterModuleDescriptor"],
        "TypeUnit": {
            "AcknowUnitType": "~/TAcknowUnitType_Logistic",
        },
        "depictions": {
            "remove": {
                "DepictionVehicles_ndf": {
                    "remove_members": ["SubDepictionGenerators"]
                },
            },
            "cadavre": {
                "remove_modules": ["Transporter"],
            },
        },
        "NewName": "M1038_Humvee_supply_US",
        "GameName": {
            "display": "M1038 HUMVEE CARGO",
            "token": "LKQDXAWXPE",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_M1038_Humvee_supply_US",
                "Unite",
                "Vehicule",
                "Vehicule_Logistique",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_supply", "Texture_supply"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "MenuIconTexture": "Texture_RTS_H_supply",
        "CubeActionDescriptor": "vehiculeSol_supply",
        "Factory": "EFactory/Logistic",
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "US_82nd_Airborne_multi": {
                "Transports": None,
            },
        },
        "availability": [4, 0, 0, 0],
        "SpecialitiesList": [
            'supply',
            '_supply_squad',
        ],
        "InfoPanelConfig": "VehiculeSupplier",
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Reverse',
                   'SupplyUnit', 'AskForSupply', 'AIStop', 'AISupply'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": True,
        "Faction": "NATO",
        "Nation": "US",
    },

    ("Scout_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "6f07c62b-c344-4c79-a72b-c1a80ce3375b",
        "GroupeCombatGUID": "375817f4-441d-4030-a902-b22f0103552d",
        "ShowroomGUID": "7c0ba2f2-804f-4550-8161-e687c1305a10",
        "CadavreGUID": "eab4f242-c8fd-4868-b009-a6a86f934dd8",
        "NewName": "Cav_Scout_Dragon_M3A1_US",
        "GameName": {
            "display": "#RECO2 CAVALRY SCOUTS [M3A1]",
            "token": "VKPPUUNVBK",
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
                "UNITE_Cav_Scout_Dragon_M3A1_US",
                "Unite"
            ],
        },
        "strength": 2,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        # "Dangerousness": 12,
        "WeaponAssignment": [
            (0, [2, ]),
            (1, [0, 1]),
        ],
        "WeaponDescriptor": {
            "Salves": {
                "add": [(1, 10), ],
                "FM_M16": 7,
                "MMG_inf_M240B_7_62mm": 30,
                "M47_DRAGON_II": 2,
            },
            "equipmentchanges": {
                "add": [(1, "Sniper_M21", "Sniper_M14")],
                "update": [2],
                "replace": [
                    ("MMG_inf_M240B_7_62mm", "M47_DRAGON_II", "MMG_inf_M240B_7_62mm", "M47_DRAGON_II"),
                ],
                "quantity": {
                    "FM_M16": 1,
                    "Sniper_M21": 1,
                    "M47_DRAGON_II": 1,
                },
            },
        },
        "TransportedSoldier": "Cav_Scout_Dragon_M3A1_US",
        "CommandPoints": 20,
        "SpecialitiesList": [
            'reco',
            'infantry_equip_heavy',
        ],
        "ButtonTexture": "Scout_Aero_US",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_3rd_Arm_multi": {
                "Transports": ["M3A1_Bradley_CFV_US"],
            },
            "US_8th_Inf_multi": {
                "Transports": ["M3A1_Bradley_CFV_US"],
            },
            "US_11ACR_multi": {
                "Transports": ["M3A1_Bradley_CFV_US"],
            },
        },
        "availability": [4, 3, 0, 0],
        "max_speed": 20,
        "Orders": ['Stop', 'Move', 'FollowFormation', 'SmartMove', 'Attack', 'SmartMoveAndAttack', 'MoveAndAttack',
                   'Shoot', 'ShootOnPosition', 'ShootOnPositionWithoutCorrection', 'AskForSupply',
                   'EnterDistrict', 'LoadIntoTransport', 'Load', 'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "US",
        "alternatives_count": 2,
        "selector_tactic": "02_02",
        "unique_count": 2,
    },

    ("Scout_US", 1): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "f1cd2505-5d6a-436f-b678-c82be2e65918",
        "GroupeCombatGUID": "0e948acc-c379-4498-946b-21b5b3b13314",
        "ShowroomGUID": "87b3d52f-1703-494c-a3ee-b25dc6095136",
        "CadavreGUID": "b47e0795-709b-4377-9f5c-f42df25e7aac",
        "NewName": "Cav_Scout_Dragon_M3A2_US",
        "GameName": {
            "display": "#RECO2 CAVALRY SCOUTS [M3A2]",
            "token": "VKPPUUNVBJ",
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
                "UNITE_Cav_Scout_Dragon_M3A2_US",
                "Unite"
            ],
        },
        "strength": 2,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        # "Dangerousness": 12,
        "WeaponAssignment": [
            (0, [2, ]),
            (1, [0, 1]),
        ],
        "WeaponDescriptor": {
            "Salves": {
                "add": [(1, 10), ],
                "FM_M16": 7,
                "MMG_inf_M240B_7_62mm": 30,
                "M47_DRAGON_II": 2,
            },
            "equipmentchanges": {
                "add": [(1, "Sniper_M21", "Sniper_M14")],
                "update": [2],
                "replace": [
                    ("MMG_inf_M240B_7_62mm", "M47_DRAGON_II", "MMG_inf_M240B_7_62mm", "M47_DRAGON_II"),
                ],
                "quantity": {
                    "FM_M16": 1,
                    "Sniper_M21": 1,
                    "M47_DRAGON_II": 1,
                },
            },
        },
        "TransportedSoldier": "Cav_Scout_Dragon_M3A2_US",
        "CommandPoints": 20,
        "SpecialitiesList": [
            'reco',
            'infantry_equip_heavy',
        ],
        "ButtonTexture": "Scout_Aero_US",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_11ACR_multi": {
                "Transports": ["M3A2_Bradley_CFV_US"],
            },
        },
        "availability": [3, 2, 0, 0],
        "max_speed": 20,
        "Orders": ['Stop', 'Move', 'FollowFormation', 'SmartMove', 'Attack', 'SmartMoveAndAttack', 'MoveAndAttack',
                   'Shoot', 'ShootOnPosition', 'ShootOnPositionWithoutCorrection', 'AskForSupply',
                   'EnterDistrict', 'LoadIntoTransport', 'Load', 'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "US",
        "alternatives_count": 2,
        "selector_tactic": "02_02",
        "unique_count": 2,
    },

    # ("M3A1_Bradley_CFV_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
    #     "GUID": "e34ee9a5-9090-4b17-b917-430adc1b6ca9",
    #     "GroupeCombatGUID": "4e620fd4-7d88-4cee-9a21-c3f0f03203cd",
    #     "ShowroomGUID": "9a773c3f-110b-48b0-9c03-e490e3e3fd6a",
    #     "CadavreGUID": "77650abe-7421-4feb-b52b-7aa4342966ea",
    #     "modules_add": ["TTransporterModuleDescriptor"],
    #     "NewName": "M3A1_Bradley_CFV_trans_US",
    #     "TagSet": {
    #         "overwrite_all": [
    #             "AllUnits",
    #             "AllowedForMissileRoE",
    #             "Char",
    #             "Char_Reco",
    #             "ChasseurDeChar",
    #             "GroundUnits",
    #             "Radio",
    #             "Reco",
    #             "UNITE_M3A1_Bradley_CFV_trans_US",
    #             "Unite",
    #             "Vehicule_Transport_Arme"
    #         ],
    #     },
    #     "CommandPoints": 100,
    #     "SpecialitiesList": [
    #             'reco',
    #             '_transport1',
    #             '_ifv',
    #             '_smoke_launcher',
    #         ],
    #     "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Attack', 'FastMoveAndAttack', 'MoveAndAttack',
    #                'Reverse', 'Shoot', 'ShootOnPosition', 'ShootOnPositionWithoutCorrection', 'ShootDefensiveSmoke',
    #                'AskForSupply', 'UnloadFromTransport', 'UnloadAtPosition', 'LoadUnit', 'AIDefend', 'AIAttack', 'AIStop'],
    #     "is_infantry": False, # False for Javelin LML (unique exception), towed units.
    #     "is_heavy_equipment": False,
    #     "is_ground_vehicle": True,
    #     "is_aerial": False,
    #     "is_unarmed": False,
    #     "Faction": "NATO",
    #     "Nation": "US",
    # },

    ("MANPAD_Stinger_C_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "569c934b-4a8e-4f2e-83e5-06640fa620a4",
        "GroupeCombatGUID": "90c692ce-e3c6-45aa-8567-3baba4eb5b18",
        "ShowroomGUID": "234345e1-ef60-4fc4-ba7c-9643521ed1dc",
        "CadavreGUID": "7e6528ba-b0b7-4276-9f62-3c7ac39c4aba",
        "NewName": "MANPAD_Stinger_C_Rifles_US",
        "GameName": {
            "display": "FIRE TEAM [STINGER]",
            "token": "CZWRLXUPXA",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits", "AllowedForMissileRoE", "Crew", "GroundUnits", "Inf_quartier_ok",
                "Infanterie", "Infanterie_AA", "Infanterie_Spec_Defense", "MANPAD_Stinger_C_Rifles_US", "Unite"
            ],
        },
        "strength": 6,
        "Stealth": 2.0,
        # "Dangerousness": 12,
        "WeaponDescriptor": {
            "Salves": {
                "add": [(1, 10), ],
                "FM_M16": 7,
                "MANPAD_FIM92": 8,
            },
            "equipmentchanges": {
                "HAGRU_MANPADS": [(2, 0, "MANPAD_FIM92_HAGRU")], # turret_index, donor_weapon_index, ammo_name
                "add": [(1, "Sniper_M21", "Sniper_M14")],
                "update": [2],
                "replace": [("FM_M16_noreflex", "FM_M16_x5")],
                "quantity": {
                    "FM_M16": 4,
                    "Sniper_M21": 1,
                },
            },
        },
        "TransportedTexture": "UseInGame_Transport_LAAD",
        "TransportedSoldier": "MANPAD_Stinger_C_US",
        "Factory": "EFactory/DCA",
        "CommandPoints": 60,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "SpecialitiesList": [
                'AA',
                'infantry_equip_heavy',
            ],
        "MenuIconTexture": "Texture_RTS_H_manpad",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Manpad",
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "US_82nd_Airborne_multi": {
                "Transports": ["UH60A_Black_Hawk_US"],
            },
        },
        "availability": [0, 7, 5, 0],
        "max_speed": 20,
        "UpgradeFromUnit": "MANPAD_Stinger_C_para_US",
        "Orders": ['Stop', 'Move', 'FollowFormation', 'SmartMove', 'Attack', 'SmartMoveAndAttack', 'MoveAndAttack',
                   'Shoot', 'ShootOnPosition', 'ShootOnPositionWithoutCorrection', 'AskForSupply',
                   'EnterDistrict', 'LoadIntoTransport', 'Load', 'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "US",
        "alternatives_count": 1,
        "selector_tactic": "00_01",
    },

    ("M1A1HA_Abrams_CMD_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "74eb3b04-5b62-406d-9350-6b1765555505",
        "GroupeCombatGUID": "f3b3b3b4-5b62-406d-9350-6b1765555505",
        "ShowroomGUID": "b059b7ca-be63-4407-9e15-283899bd0a51",
        "CadavreGUID": "5b05cbe1-282e-41fd-b696-18b3112f733a",
        "NewName": "M1A1HA_Abrams_CMD2_US",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_M1A1HA_Abrams_CMD2_US",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 350,
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "US_3rd_Arm_multi": {
                "cards": 2,
                "Transports": None,
            },
        },
        "availability": [0, 0, 0, 1],
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
        "Nation": "US",
        "UpgradeFromUnit": "M1A1_Abrams_CMD2_US",
    },

    ("M1A1_Abrams_CMD_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "2b1fcb11-8a07-401e-b7a8-bbaa38a4881e",
        "GroupeCombatGUID": "e9f5c7ac-6dd0-45f3-af98-2f0e148b660e",
        "ShowroomGUID": "l1m2n3o4-p5q6-4r7s-8t9u-0v1w2x3y4z5b",
        "CadavreGUID": "c5697d12-0538-41e3-9087-f6a3c0a3f302",
        "NewName": "M1A1_Abrams_CMD2_US",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_M1A1_Abrams_CMD2_US",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 325,
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_11ACR_multi": {
                "Transports": None,
            },
            "US_8th_Inf_multi": {
                "Transports": None,
            },
            "US_3rd_Arm_multi": {
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
        "Nation": "US",
        "UpgradeFromUnit": "M1IP_Abrams_CMD2_US",
    },

    ("M1A1_Abrams_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "d2ec00df-1542-4e0c-b00b-6a406453c071",
        "GroupeCombatGUID": "52e5dadb-f6cf-422a-b3d6-253f78572641",
        "ShowroomGUID": "822614ec-98c7-4078-a82d-8f1bb675920a",
        "CadavreGUID": "d00475c4-04a1-45b5-8eb5-56c7338b74cd",
        "NewName": "8th_M1A1_Abrams_US",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_Standard",
                "GroundUnits",
                "SM_charLourd",
                "UNITE_8th_M1A1_Abrams_US",
                "Unite",
            ],
        },
        "GameName": {
            "display": "#8THINF M1A1 ABRAMS",
            "token": "JNEJSZOAGF",
        },
        "CommandPoints": 235,
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "US_8th_Inf_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 4, 3, 0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Attack', 'FastMoveAndAttack',
                   'MoveAndAttack', 'Reverse', 'Shoot', 'ShootOnPosition',
                   'ShootOnPositionWithoutCorrection', 'ShootDefensiveSmoke', 'AskForSupply',
                   'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "is_replacement": True,
        "Faction": "NATO",
        "Nation": "US",
    },

    ("M1IP_Abrams_CMD_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "cc7fc0a1-1e81-4b68-b25f-51dfbbb09f85",
        "GroupeCombatGUID": "5a929931-ed80-48a5-815f-db963cdee0c0",
        "ShowroomGUID": "976dd926-5c33-4c26-836d-77107a0c4fcb",
        "CadavreGUID": "8f2e58ba-c88f-4e86-82e3-149bad45e7e7",
        "NewName": "M1IP_Abrams_CMD2_US",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_M1IP_Abrams_CMD2_US",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 295,
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_24th_Inf_multi": {
                "Transports": None,
            },
            "US_101st_Airmobile_multi": {
                "Transports": None,
            },
            "NATO_Garnison_Berlin_multi": {
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
        "Nation": "US",
        "UpgradeFromUnit": "M1_Abrams_CMD2_US",
    },

    ("M1_Abrams_CMD_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "0a337b4d-3fe2-4b88-9bdf-a73bc6733296",
        "GroupeCombatGUID": "c200a4e1-1ca5-4c19-aa5a-885ed917b114",
        "ShowroomGUID": "12f471a0-e473-40f3-b23c-534b44864771",
        "CadavreGUID": "5a57b6f3-4978-499d-9291-4817452df13d",
        "NewName": "M1_Abrams_CMD2_US",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_M1_Abrams_CMD2_US",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 280,
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_8th_Inf_multi": {
                "Transports": None,
            },
            "US_24th_Inf_multi": {
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
        "Nation": "US",
    },

    ("M60A3_CMD_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "31082f44-67be-4428-8df2-13d9159a911c",
        "GroupeCombatGUID": "f1902a7c-9a79-4df0-aff1-28c8f0d1451c",
        "ShowroomGUID": "785b5ffe-97af-4a1f-834f-3d45c249618c",
        "CadavreGUID": "32f23257-7290-45a6-be73-7eccf571a367",
        "NewName": "M60A3_CMD2_US",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_M60A3_CMD2_US",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 225,
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_8th_Inf_multi": {
                "Transports": None,
            },
            "US_35th_Inf_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 2, 0, 0],
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
        "Nation": "US",
    },

    ("M60A1_RISE_Passive_CMD_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "d8a1ca26-594b-4ec9-962c-b3403b4ab8e3",
        "GroupeCombatGUID": "bdf4c41e-1be4-4a30-b742-0391f4829599",
        "ShowroomGUID": "c11f7f2b-2de6-4ccd-b688-0364ca95422c",
        "CadavreGUID": "ff5fa067-210e-4e7f-8352-08e3b5bfed68",
        "NewName": "M60A1_RISE_Passive_CMD2_US",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "M60A1_RISE_Passive_CMD2_US",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 220,
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_35th_Inf_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 3, 0, 0],
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
        "Nation": "US",
    },

    ("M551A1_TTS_Sheridan_CMD_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "7df5c2e6-7313-4de6-bc0c-3f98df60ad0b",
        "GroupeCombatGUID": "c841f8d3-9015-41d8-b072-5ce130a20f24",
        "ShowroomGUID": "4d9c0ca3-0791-4c83-ab22-98ba9a8bd480",
        "CadavreGUID": "66211e93-310a-4356-8eab-f97acfabc06b",
        "NewName": "M551A1_TTS_Sheridan_CMD2_US",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "M551A1_TTS_Sheridan_CMD2_US",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 150,
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_82nd_Airborne_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 0, 0, 3],
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
        "Nation": "US",
    },

    ("M577_US", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "40a7809c-a6c1-4af0-ad2c-b17c9250732f",
        "GroupeCombatGUID": "d2b58f7f-12a7-437c-83c1-dd18aaf9ff9e",
        "ShowroomGUID": "n4o5p6q7-r8s9-4t0u-1v2w-3x4y5z6a7b81",
        "CadavreGUID": "a88c4ec3-d343-411e-823b-0e57d3e6e63a",
        "NewName": "M577_CMD2_US",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_M577_CMD2_US",
                "Unite",
                "Vehicule",
                "Vehicule_CMD",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 145,
        "Decks": {
            "packs": {
                "rename": True, 
            },
        },
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "US_11ACR_multi": {
                "Transports": None,
            },
            "US_8th_Inf_multi": {
                "Transports": None,
            },
            "US_24th_Inf_multi": {
                "Transports": None,
            },
            "US_35th_Inf_multi": {
                "Transports": None,
            },
            "US_3rd_Arm_multi": {
                "Transports": None,
            },
            "NATO_Garnison_Berlin_multi": {
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
        "Nation": "US",
    },
} 
# fmt: on
