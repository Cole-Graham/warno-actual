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
            "MotherCountry": "UK",
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
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "UK_2nd_Infantry_multi": {
                "Transports": ["Bedford_MJ_4t_trans_UK"],
            },
        },
        "availability": [6, 4, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "Gatling_M61_Vulcan_20mm_late_TOWED": 13,
            },
        },
        "UpgradeFromUnit": "FOB_UK",
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack', 'EOrderType/MoveAndAttack',
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
        "servants": ("G_UK", "D_UK"),
        "servant_types": {
            "showroom": {
                "G_UK": ["GunnerLeft"],
                "D_UK": ["ServantRight"]
            },
            "subdepictions": {
                "G_UK": ["ServantWalkOnlyLeft", "GunnerIdleOnlyLeft"],
                "D_UK": ["ServantRight"]
            },
        }
    },
    
    ("MANPAD_Javelin_UK", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "7be6ab23-0cd0-48bb-8a21-cb4ae72bfaeb",
        "GroupeCombatGUID": "6654c8cb-38e3-41e9-bc29-d37e1a3fd862",
        "ShowroomGUID": "4f8f93db-5b47-4e3b-91f9-e7a63870c778",
        "CadavreGUID": "e9fecaf0-63ae-4181-beb7-a92c1e7d612a",
        "NewName": "MANPAD_Starstreak_UK",
        "GameName": {
            "display": "STARSTREAK",
            "token": "NFOWVDVULT",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_AA",
                "Infanterie_Spec_Defense",
                "UNITE_MANPAD_Starstreak_UK",
                "Unite",
            ],
        },
        "TransportedSoldier": "MANPAD_Starstreak_UK",
        "CommandPoints": 60,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [7, 5, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": [
            'infantry_equip_heavy',
        ],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "HAGRU_MANPADS": [(1, 0, "MANPAD_Starstreak_HAGRU")], # turret_index, donor_weapon_index, ammo_name
                "replace": [
                    ("FM_L85A1", "FM_L85A1_noreflex"),
                    ("MANPAD_FIM92", "MANPAD_Starstreak", "Javelin", "Starstreak_x3"),
                ],
            },
        },
        "UpgradeFromUnit": "DCA_Javelin_LML_UK",
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/SmartMove', 'EOrderType/Attack', 'EOrderType/SmartMoveAndAttack', 'EOrderType/MoveAndAttack',
                   'EOrderType/Shoot', 'EOrderType/ShootOnPosition', 'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply',
                   'EOrderType/EnterDistrict', 'EOrderType/Load', 'EOrderType/Load', 'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "UK",
        "alternatives_count": 6,
        "selector_tactic": "00_06",
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
            "UK_1st_Armoured_multi": {
                "Transports": ["Bedford_MJ_4t_trans_UK", "FV432_UK", "Lynx_AH_Mk1_UK"],
            },
            "UK_2nd_Infantry_multi": {
                "Transports": ["Bedford_MJ_4t_trans_UK", "MCV_80_Warrior_UK", "Lynx_AH_Mk1_UK"],
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
            "display": "#CMD CHALLENGER Mk.2 CMD",
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
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L8A2_7_62mm": 96,
            },
        },
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack', 
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
    
    ("FV4201_Chieftain_CMD_UK", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "c37302a6-8480-497d-8733-6e5d0e70ae3b",
        "GroupeCombatGUID": "e7b02c97-0130-4ac1-bf35-1c2f3065a4de",
        "ShowroomGUID": "451549aa-d69c-47e1-8824-30f60b236bb6",
        "CadavreGUID": "dcf2f600-fa63-4760-bb8a-334e57fccc84",
        "NewName": "FV4201_Chieftain_CMD2_UK",
        "GameName": {
            "display": "#CMD CHIEFTAIN Mk.10 CMD",
            "token": "VBMOZKDIQO",
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
                "UNITE_FV4201_Chieftain_CMD2_UK",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 265,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            '_leader',
            '_smoke_launcher',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 2, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 96,
                "MMG_L8A2_7_62mm": 96,
            },
        },
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack', 
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
    
    ("FV4201_Chieftain_Mk9_UK", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "42c8aa7b-7dec-406c-9806-876e01d5eff6",
        "GroupeCombatGUID": "2a3009a7-9dd4-4a3e-8f0d-f54471cbb1e2",
        "ShowroomGUID": "576ba527-ee4d-4078-b7aa-de7d5768e192",
        "CadavreGUID": "9758e636-88e4-4970-adba-ffb1b4a0813c",
        "NewName": "FV4201_Chieftain_Mk9_CMD2_UK",
        "GameName": {
            "display": "#CMD CHIEFTAIN Mk.9 CMD",
            "token": "ITZWHDGBHC",
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
                "UNITE_FV4201_Chieftain_Mk9_CMD2_UK",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 240,
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            '_leader',
            '_smoke_launcher',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 2, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 96,
                "MMG_L8A2_7_62mm": 96,
            },
        },
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack', 
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
    
    ("FV4201_Chieftain_Mk9_UK", 1): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "87f347d1-7532-4ac8-8856-cbf95fa29392",
        "GroupeCombatGUID": "c6bae323-a820-4eb3-b45f-c617e3162a3d",
        "ShowroomGUID": "f26a6c58-4680-4fb2-9540-179ac933400a",
        "CadavreGUID": "30a1f922-b453-4fbe-ac83-63be38aba866",
        "NewName": "FV4201_Chieftain_Mk9_CMD_UK",
        "GameName": {
            "display": "#LDR CHIEFTAIN Mk.9 LDR.",
            "token": "SHOVALSAYD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_FV4201_Chieftain_Mk9_CMD_UK",
                "Unite",
            ],
        },
        "CommandPoints": 130,
        "SpecialtiesList": [
            '_leader',
            '_smoke_launcher',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 4, 0],
        "UpgradeFromUnit": None,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L37A2_7_62mm": 96,
                "MMG_L8A2_7_62mm": 96,
            },
        },
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack', 
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
    
    ("Centurion_Mk13_CMD_UK", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "9bc04582-2e83-4b9f-bae7-7d367dc094f2",
        "GroupeCombatGUID": "f669e647-adbc-4414-99da-6f11eb06819f",
        "ShowroomGUID": "79a769f6-c8bc-4ec1-b6b6-697f2d024c72",
        "CadavreGUID": "f5920656-c32e-4094-9264-b4682fdfd05e",
        "NewName": "Centurion_Mk13_CMD2_UK",
        "GameName": {
            "display": "#CMD CENTURION Mk.13 CMD",
            "token": "BYGMCHPETR",
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
                "UNITE_Centurion_Mk13_CMD2_UK",
                "Unite",
            ],
        },
        "Factory": "EFactory/Logistic",
        "CommandPoints": 200,
        "capacities": {
            "remove_capacities": ["reserviste"],
        },
        "UnitRole": 'hq_tank',
        "SpecialtiesList": [
            '_leader',
            '_smoke_launcher',
        ],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 0, 2, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_FN_MAG_7_62mm": 96,
                "MMG_FN_MAG_7_62mm": 96,
            },
        },
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack', 
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
    
    ("FV101_Scorpion_UK", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "5892675b-4479-4d47-8cd6-c2e2d6a9c87b",
        "GroupeCombatGUID": "f9ebcac8-c741-47ca-8aac-db0b97fd4a59",
        "ShowroomGUID": "f9ebcac8-c741-47ca-8aac-db0b97fd4a59",
        "CadavreGUID": "712dc0c8-8a08-407a-86de-7966c49791e2",
        "NewName": "FV101_Scorpion_para_UK",
        "GameName": {
            "display": "PARA. FV101 SCORPION",
            "token": "VPPQSJIFIU",
        },
        "TypeUnit": {
            "AcknowUnitTypes": ["Tank"],
            "TypeUnitFormation": "Char",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_Standard",
                "GroundUnits",
                "UNITE_FV101_Scorpion_para_UK",
                "Unite",
            ],
        },
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "Factory": "EFactory/Tanks",
        "availability": [0, 12, 9, 0],
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 3500.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/Standard": 70.0,
                "EOpticalStrength/LowAltitude": 70.0,
                "EOpticalStrength/HighAltitude": 20.0,
            },
        },
        "stealth": 1.5,
        "UnitRole": "armor",
        "UpgradeFromUnit": "FV432_Rarden_UK",
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L43A1_7_62mm": 96,
            },
        },
        "DeploymentShift": 0,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack', 
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
    
    ("FV107_Scimitar_UK", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "9e1f563b-4429-4d95-a296-06c9e4be0305",
        "GroupeCombatGUID": "98ce59ad-4057-4d0c-b7d4-d837a9101758",
        "ShowroomGUID": "9ff607c6-2836-4b3c-90af-06e2a1194a1a",
        "CadavreGUID": "a8a1ac35-7624-4744-b802-18c4c100f364",
        "NewName": "FV107_Scimitar_para_UK",
        "GameName": {
            "display": "PARA. FV107 SCIMITAR",
            "token": "FYPVEURLLZ",
        },
        "TypeUnit": {
            "AcknowUnitTypes": ["Tank"],
            "TypeUnitFormation": "Char",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_Standard",
                "GroundUnits",
                "UNITE_FV107_Scimitar_para_UK",
                "Unite",
            ],
        },
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "Factory": "EFactory/Tanks",
        "availability": [0, 12, 9, 0],
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 3500.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/Standard": 70.0,
                "EOpticalStrength/LowAltitude": 70.0,
                "EOpticalStrength/HighAltitude": 20.0,
            },
        },
        "stealth": 1.5,
        "UnitRole": "armor",
        "UpgradeFromUnit": "FV101_Scorpion_para_UK",
        "WeaponDescriptor": {
            "Salves": {
                "MMG_L43A1_7_62mm": 96,
            },
        },
        "DeploymentShift": 0,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack', 
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
    
    ("RCL_L6_Wombat_UK", 0): {  # donor unit - increment integer as needed to avoid duplicate keys
        "GUID": "1a9bf3de-330b-4188-b4cf-a4bcf42571f1",
        "GroupeCombatGUID": "0c3c416b-12cd-42a8-bd2e-f343404a403d",
        "ShowroomGUID": "b33c7197-4360-4ebd-948e-70249481ec53",
        "CadavreGUID": "57a721f1-b874-4e45-bd51-9c5b90dd3afe",
        "NewName": "RCL_L6_Wombat_para_UK",
        "GameName": {
            "display": "PARA. L6 WOMBAT",
            "token": "UKZTRNJYMX",
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
                "UNITE_RCL_L6_Wombat_para_UK",
                "Unite"
            ],
        },
        "strength": 5,
        "CommandPoints": 30,
        "SpecialtiesList": [
            '_para',
            'infantry_equip_veryheavy',
        ],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": [0, 8, 6, 0],
        "max_speed": 9,
        "DeploymentShift": 1750,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack', 'EOrderType/MoveAndAttack',
                   'EOrderType/Shoot', 'EOrderType/ShootOnPosition', 'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/AssaultDistrict', 'EOrderType/Load',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True, # False for Javelin LML (unique exception), towed units.
        "is_heavy_equipment": True,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "UK",
        "alternatives_count": 2,
        "servants": ("G_UK", "D_UK"),
        "servant_types": {
            "showroom": {
                "G_UK": ["ATGMServantLeft"],
                "D_UK": ["ATGMServantRight"]
            },
            "subdepictions": {
                "G_UK": ["ATGMServantLeft"],
                "D_UK": ["ATGMServantRight"]
            },
        }
    },
}
# fmt: on
