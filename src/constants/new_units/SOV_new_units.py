"""New unit definitions for Soviet Union."""

# fmt: off
SOV_NEW_UNITS = {
    ("MotRifles_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "ae9979f0-0bb1-47f3-b4f6-c4e820ad2a06",
        "GroupeCombatGUID": "e9462050-a89d-456b-915d-a68d7edafd17",
        "ShowroomGUID": "c7b5a9d8-e4f2-4c16-9d3b-8a2e4f7c6b5d",
        "CadavreGUID": "4a793ae9-5f90-41e1-b8a2-b9203e527de5",
        "NewName": "MotRifles_CMD2_SOV",
        "GameName": {
            # "display": "#CMD KOMANDNOE OTDELENIE",
            "display": "#CMD KOM. OTDELENIE",
            "token": "FFFKSMMRGR",
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
                "UNITE_MotRifles_CMD2_SOV",
                "Unite",
            ],
        },
        "strength": 5,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        "Dangerousness": 12,
        "WeaponAssignment": [
            (0, [1]),
            (1, [0]),
            (2, [0]),
            (3, [0, 3]),
            (4, [0, 2]),
        ],
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 7,
                "Sniper_SVD_Dragunov": 100,
                "RocketInf_RPG22_72_5mm": 5
            },
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 4,
                },
            },
        },
        # "weapon1": "FM_AK_74",
        # "weapon1_quantity": 4,
        "Salves": [7, 100, 5, 3],
        "TransportedTexture": "UseInGame_Transport_COMMAND",

        "TransportedSoldier": "MotRifles_SOV",
        "Factory": "EFactory/Logistic",

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
            "SOV_119IndTkBrig_multi": {
                "Transports": ["UAZ_469_SOV", "BTR_80_SOV", "Mi_2_trans_SOV", "Mi_8TV_non_arme_SOV", "Mi_8TV_SOV"],
            },
            "SOV_76_VDV_multi": {
                "Transports": ["LUAZ_967M_SOV", "BTR_D_SOV"],
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
        "Faction": "PACT",
        "Nation": "SOV",
        "alternatives_count": 4,
        "selector_tactic": "02_04",
    },

    ("MotRifles_CMD_TTsko_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "e3e48926-a5ee-492a-b6f9-c772b8a90924",
        "GroupeCombatGUID": "9a2f1fad-0e56-4f46-8345-b125fda7314a",
        "ShowroomGUID": "b1c2d3e4-f5g6-4h7i-8j9k-l0m1n2o3p4q5",
        "CadavreGUID": "b852d941-cba8-42e6-867a-7ecf24be522b",
        "NewName": "MotRifles_CMD2_TTsko_SOV",
        "GameName": {
            # "display": "#CMD KOMANDNOE OTDELENIE",
            "display": "#CMD KOM. OTDELENIE",
            "token": "PKHNVEPCJL",
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
                "UNITE_MotRifles_CMD2_TTsko_SOV",
                "Unite",
            ],
        },
        "strength": 5,
        # "BoundingBoxSize": str(determine_BoundingBox(5)) + " * Metre",
        "Dangerousness": 12,
        "WeaponAssignment": [
            (0, [1]),
            (1, [0]),
            (2, [0]),
            (3, [0, 3]),
            (4, [0, 2]),
        ],
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 7,
                "Sniper_SVD_Dragunov": 100,
                "RocketInf_RPG22_72_5mm": 5
            },
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 4,
                },
            },
        },
        "TransportedTexture": "UseInGame_Transport_COMMAND",
        "TransportedSoldier": "MotRifles_TTsko_SOV",
        "Factory": "EFactory/Logistic",
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
            "SOV_27_Gds_Rifle_multi": {
                "Transports": ["UAZ_469_SOV", "BTR_80_SOV", "Mi_2_trans_SOV", "Mi_8TV_non_arme_SOV", "Mi_8TV_SOV"],
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
        "Faction": "PACT",
        "Nation": "SOV",
        "alternatives_count": 4,
        "selector_tactic": "02_04",
    },

    ("T80BV_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "7885fe97-44c5-4ec9-92ea-dea7d1335a23",
        "GroupeCombatGUID": "993eaf28-65c8-4c9d-bbf0-37c296fe5466",
        "ShowroomGUID": "e6f7g8h9-i0j1-4k2l-3m4n-5o6p7q8r9s0t",
        "CadavreGUID": "ac22fe6a-7e23-49b8-823d-4f68ad83cf7c",
        "NewName": "T80BV_CMD2_SOV",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_T80BV_CMD2_SOV",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "armor": {
            "front": 18,
        },
        "CommandPoints": 335,
        "SpecialitiesList": [
                'hq_tank',
                'leader_sov',
                '_smoke_launcher',
            ],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle_multi": {
                "Transports": None,
            },
            "SOV_39_Gds_Rifle_multi": {
                "Transports": None,
            },
            "SOV_79_Gds_Tank_multi": {
                "Transports": None,
            },
            "SOV_119IndTkBrig_multi": {
                "cards": 2,
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
        "Faction": "PACT",
        "Nation": "SOV",
    },

    ("MTLB_CMD_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "ddc1a5b9-cc08-494a-a9dc-7d8b35591505",
        "GroupeCombatGUID": "41959c7e-e732-453f-91d5-000729d068e5",
        "ShowroomGUID": "847a7325-445a-44ba-bfcb-24c03dfaad07",
        "CadavreGUID": "fe1ea57b-0847-4688-9618-d0f814126711",
        "NewName": "MTLB_CMD2_SOV",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_MTLB_CMD2_SOV",
                "Unite",
                "Vehicule",
                "Vehicule_CMD",
            ],
        },
        "Factory": "EFactory/Logistic",
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
            "SOV_27_Gds_Rifle_multi": {
                "Transports": None,
            },
            "SOV_39_Gds_Rifle_multi": {
                "Transports": None,
            },
            "SOV_79_Gds_Tank_multi": {
                "Transports": None,
            },
            "SOV_119IndTkBrig_multi": {
                "Transports": None,
            },
            "SOV_6IndMSBrig_multi": {
                "Transports": None,
            },
        },
        "availability": [0, 3, 0, 0],
        "Orders": ['Stop', 'Move', 'FollowFormation', 'QuickMove', 'Reverse',
                   'AskForSupply', 'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": False, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": True,
        "Faction": "PACT",
        "Nation": "SOV",
    },

    ("MotRifles_TTsko_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "21a5481c-bf7f-45b8-9c22-bb6885850521",
        "GroupeCombatGUID": "f41497ec-862f-4321-b628-0b6fb0b80b27",
        "ShowroomGUID": "a4ac9eac-d74d-4da1-91d6-f2c08dd11ad3",
        "CadavreGUID": "9d790fe8-5668-4757-b532-6d70f411d232",
        "NewName": "MotRifles_RPG7V_TTsko_SOV",
        "GameName": {
            "display": "MOTOSTRELKI [RPG-7]",
            "token": "UQYYVBRKGT",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_IFV",
                "Infanterie_Standard",
                "Steelman_infanterie_autoresolve",
                "UNITE_MotRifles_RPG7_TTsko_SOV",
                "Unite",
            ],
        },
        "strength": 7,
        "WeaponAssignment": [
                (0, [1]),
                (1, [0]),
                (2, [0]),
                (3, [0]),
                (4, [0]),
                (5, [0]),
                (6, [0, 2]),
            ],
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 9,
                "SAW_RPK_74_5_56mm": 10,
                "RocketInf_RPG7VL": 6,
            },
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 6,
                },
                "replace": [
                    ("RocketInf_RPG27_105mm", "RocketInf_RPG7VL", "RocketInf_RPG27_105mm", "RocketInf_RPG7VL"),
                ],
            },
        },
        "TransportedSoldier": "MotRifles_RPG7V_TTsko_SOV",
        "CommandPoints": 30,
        "SpecialitiesList": [
                'infantry',
                '_ifv',
                'infantry_equip_medium',
            ],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle_multi": {
                "Transports": ["GAZ_66_SOV", "BTR_80_SOV", "BMP_1P_SOV", "BMP_2AG_SOV", "BMP_3_SOV"],
            },
        },
        "availability": [10, 7, 0, 0],
        "max_speed": 26,
        "Orders": ['Stop', 'Move', 'FollowFormation', 'SmartMove', 'Attack', 'SmartMoveAndAttack', 'MoveAndAttack',
                   'Shoot', 'ShootOnPosition', 'ShootOnPositionWithoutCorrection', 'AskForSupply',
                   'EnterDistrict', 'LoadIntoTransport', 'Load', 'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "SOV",
        "UpgradeFromUnit": "MotRifles_TTsko_SOV",
        "alternatives_count": 6,
        "selector_tactic": "00_06",
    },

    ("ATteam_Fagot_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "22caa472-c587-4816-b3b4-913e7c2316f4",
        "GroupeCombatGUID": "674ce341-9c4a-4da2-9f3e-4b4e6f6c2358",
        "ShowroomGUID": "c419b0c4-6f4e-435b-8e1f-fb74b33cf884",
        "CadavreGUID": "d0a2edad-e8c8-4073-8b90-cdfadcd3a78e",
        "NewName": "ATteam_Faktoriya_SOV",
        "GameName": {
            "display": "FAKTORIYA",
            "token": "ZADIQTXXXX",
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
                "UNITE_ATteam_Faktoriya_SOV",
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
        "ButtonTexture": "Atteam_Konkurs_DShV_SOV",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_39_Gds_Rifle_multi": {
                "Transports": ["UAZ_469_SOV", "BTR_60_SOV", "BMP_1P_SOV"],
            },
            "SOV_79_Gds_Tank_multi": {
                "Transports": ["UAZ_469_SOV", "BMP_1P_SOV"],
            },
        },
        "availability": [7, 5, 4, 0],
        "max_speed": 20,
        "Orders": ['Stop', 'Move', 'FollowFormation', 'Attack', 'MoveAndAttack', 'Spread',
                   'Shoot', 'AskForSupply', 'EnterDistrict', 'LoadIntoTransport', 'Load',
                   'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "SOV",
        "depiction_type": "Towed",
        "alternatives_count": 2,
    },

    ("Atteam_Fagot_VDV_SOV", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "60fff50e-03da-402c-bbec-15424522f06d",
        "GroupeCombatGUID": "bcd261dd-e99e-4f6c-9f0e-4ffa0e470bb4",
        "ShowroomGUID": "d2e3f4g5-h6i7-4j8k-9l0m-n1o2p3q4r5s6",
        "CadavreGUID": "24612725-41c9-4d25-821b-d0e6e9377a11",
        "NewName": "ATteam_Faktoriya_VDV_SOV",
        "GameName": {
            "display": "DESANT. FAKTORIYA",
            "token": "YDMQOTJZVZ",
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
                "UNITE_ATteam_Faktoriya_VDV_SOV",
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
                '_para',
                'infantry_equip_heavy'
            ],
        "UpgradeFromUnit": "Atteam_Fagot_VDV_SOV",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_76_VDV_multi": {
                "Transports": ["LUAZ_967M_SOV", "BTR_D_Robot_SOV"],
            },
        },
        "availability": [0, 7, 5, 4],
        "max_speed": 20,
        "Orders": ['Stop', 'Move', 'FollowFormation', 'Attack', 'MoveAndAttack', 'Spread', 
                   'Shoot', 'AskForSupply', 'EnterDistrict', 'LoadIntoTransport', 'Load', 
                   'AIDefend', 'AIAttack', 'AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "PACT",
        "Nation": "SOV",
        "depiction_type": "Towed",
        "alternatives_count": 2,
    },
} 
# fmt: on
