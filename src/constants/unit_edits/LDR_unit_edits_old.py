"""Leader unit edits"""

from typing import Any, Dict

#fmt: off
ldr_unit_edits = {
    
    "Rifles_half_CMD_US": {
        "CommandPoints": 40,
        "GameName": {
            "token": "CPCIJQLHML",
            "display": "#LDR FIRE TEAM LDR.",
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
                "UNITE_Rifles_half_CMD_US",
                "Unite",
            ],
        },
        "strength": 6,
        "WeaponAssignment": [
                (0,[0,]),
                (1,[0,]),
                (2,[1,]),
                (3,[1,]),
                (4,[1,3]),
                (5,[1,2]),
            ],
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                '_ifv',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 7,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_M16": 2,
                    "Commando_733": 3,
                },
            },
            "Salves": {
                "RocketInf_M72A3_LAW_66mm": 6,
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "Rifles_CMD_US": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDR MECH. RIFLES LDR.",
            "token": "CPCIJQLHML",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Rifles_CMD_US",
                "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 7,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_M72A3_LAW_66mm": 6,
            },
        },
        "is_infantry": True,
        "is_ground_vehicle": False,
    },
    
    "NatGuard_CMD_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "Engineer_CMD_US": {
        "CommandPoints": 50,
        "GameName": {
            "display": "#LDR ENGINEERS LDR.",
            "token": "DBEBRUEYSP",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Engineer_CMD_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        # "SortingOrder": 20040,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                '_leader',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "Rangers_CMD_US": {
        "CommandPoints": 70,
        "GameName": {
            "display": "#LDR RANGERS LDR.",
            "token": "WPUCULQQND",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Rangers_CMD_US",
                "Unite",
                "noSIGINT",
            ],
        },
        "strength": 9,
        "WeaponAssignment": [
                (0,[1,]),
                (1,[0,]),
                (2,[0,]),
                (3,[0,]),
                (4,[0,]),
                (5,[0,]),
                (6,[0,]),
                (7,[0,3]),
                (8,[0,2]),
            ],
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry_sf", "Texture_sf"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                '_sf',
                '_choc',
                'infantry_equip_heavy',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry_sf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "US_8th_Inf": {
                "Transports": ["M1038_Humvee_US", "UH60A_Black_Hawk_US"]
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
        "max_speed": 20,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Commando_733", "M16A1_Carbine")],
                "quantity": {
                    "M16A1_Carbine": 8,
                },
            },
            "Salves": {
                "RocketInf_M67_RCL_90mm": 10,
            },
        },
        "unique_count": 2,
        "surrogates": 9,
        "selector_tactic": "(2, 9)",
        "selector_tactic_obj": "02_09",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "Airborne_Engineer_CMD_US": {
        "CommandPoints": 60,
        "GameName": {
            "display": "#LDR AB ENGINEERS LDR.",
            "token": "LRTQFDCCCB",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Airborne_Engineer_CMD_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        # "SortingOrder": 20040,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                '_leader',
                '_choc',
                '_para',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "Airborne_CMD_US": {
        "CommandPoints": 70,
        "GameName": {
            "display": "#LDR AIRBORNE LDR.",
            "token": "ADLDSRBBFX",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Standard",
                "UNITE_Airborne_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20060,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                '_choc',
                '_para',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 5,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 26,
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "RocketInf_AT4_83mm": 6,
            },
        },
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "AeroRifles_CMD_US": {
        "CommandPoints": 50,
        "GameName": {
            "display": "#LDR AERO-RIFLES LDR.",
            "token": "TVWIKAOSVP",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Standard",
                "UNITE_AeroRifles_CMD_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20060,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "Aero_half_CMD_US": {
        "CommandPoints": 35,
        "GameName": {
            "display": "#LDR AERO-FIRE TEAM LDR.",
            "token": "MHGSSCNBFO",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Standard",
                "UNITE_AeroRifles_CMD_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20045,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 41,
        # "UnitDefenseValue": 41,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 7,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "AeroEngineer_CMD_US": {
        "CommandPoints": 60,
        "GameName": {
            "display": "#LDR AERO-ENGINEERS LDR.",
            "token": "OWQFQTLBJN",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_AeroEngineer_CMD_US",
                "Unite"
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        # "SortingOrder": 20085,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 31,
        # "UnitDefenseValue": 31,
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                '_leader',
                '_choc',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "GreenBerets_CMD_US": {
        "CommandPoints": 75,
        "GameName": {
            "display": "#LDR GREEN BERETS LDR.",
            "token": "KFNXNJOXZS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Standard",
                "UNITE_GreenBerets_CMD_US",
                "Unite",
                "noSIGINT",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20100,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 41,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_sf',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 0.0, 1.0],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "M577_US": {
        "CommandPoints": 60,
        "GameName": {
            "display": "#LDR M577 TACFIRE FCV",
            "token": "ZTSGIUUUVJ",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_M577_US",
                "Unite",
                "Vehicule",
            ],
        },
        "Factory": "EDefaultFactories/Art",
        "IdentifiedTextures": ["Texture_RTS_H_appui", "Texture_appui"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_appui",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Transport",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "M1A1HA_Abrams_CMD_US": {
        "CommandPoints": 335,
        "GameName": {
            "display": "#LDR M1A1(HA) ABRAMS LDR.",
            "token": "CIOEKZVEAY",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1A1HA_Abrams_CMD_US",
                "Unite",
            ],
        },
        # "SortingOrder": 20340,
        # "UnitAttackValue": 561,
        # "UnitDefenseValue": 561,
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'Armor_heavy',
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": 2,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 0.0, 1.0],
    },

    "M1A1_Abrams_CMD_US": {
        "CommandPoints": 260,
        "GameName": {
            "display": "#LDR M1A1 ABRAMS LDR.",
            "token": "JARUASHKDH",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1A1_Abrams_CMD_US",
                "Unite",
            ],
        },
        # "SortingOrder": 20290,
        # "UnitAttackValue": 461,
        # "UnitDefenseValue": 461,
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'Armor_heavy',
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "M1IP_Abrams_CMD_US": {
        "CommandPoints": 210,
        "GameName": {
            "display": "#LDR M1IP ABRAMS LDR.",
            "token": "TSLINICZXV",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1IP_Abrams_CMD_US",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'Armor_heavy',
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "M1_Abrams_CMD_US": {
        "CommandPoints": 185,
        "GameName": {
            "display": "#LDR M1 ABRAMS LDR.",
            "token": "JMIRJBBLPW",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M1_Abrams_CMD_US",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'Armor_heavy',
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": 3,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "M60A3_CMD_US": {
        "CommandPoints": 120,
        "GameName": {
            "display": "#LDR M60A3 (TTS) LDR.",
            "token": "OZPDFIGTWN",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M60A3_CMD_US",
                "Unite"
            ],
        },  
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'armor',
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "M551A1_TTS_Sheridan_CMD_US": {
        "CommandPoints": 65,
        "GameName": {
            "display": "#LDR M551 TTS SHERIDAN LDR.",
            "token": "NBZRAJWZXD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "M551A1_TTS_Sheridan_CMD_US",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_amphibie',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 0.0, 1.0],
    },

    "MotRifles_CMD_TTsko_SOV": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDRSOV MOTOSTRELKI LDR.",
            "token": "ZJRMUWLPVH",
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
                "UNITE_MotRifles_CMD_TTsko_SOV",
                "Unite",
            ],
        },
        "strength": 6,
        "WeaponAssignment": [
                (0,[1,]),
                (1,[0,]),
                (2,[0,]),
                (3,[0,]),
                (4,[0,3]),
                (5,[0,2]),
            ],
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                'leader_sov',
                '_ifv',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "SOV_27_Gds_Rifle": {
                "Transports": ['GAZ_66_SOV', 'BTR_80_SOV', 'BMP_1P_SOV', 'BMP_2_SOV'],
            },
        },
        "availability": 7,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 5,
                },
            },
            "Salves": {
                "RocketInf_RPG22_72_5mm": 6,
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "Engineers_CMD_TTsko_SOV": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDRSOV SAPERI LDR.",
            "token": "QCNBGTPZWL",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Engineers_CMD_TTsko_SOV",
                "Unite"
            ],
        },
        "strength": 8,
        "WeaponAssignment": [
                (0,[0,]),
                (1,[0,]),
                (2,[0,]),
                (3,[0,]),
                (4,[0,]),
                (5,[0,]),
                (6,[0,]),
                (7,[0,1,]),
            ],
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                'leader_sov',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "Divisions": {
            "SOV_27_Gds_Rifle": {
                "Transports": ["GAZ_66_SOV", "MTLB_transp_SOV"],
            },
        },
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 8,
                },
            },
            "Salves": {
                "RocketInf_RPG18_64mm": 7,
            },
        },
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },
    
    "Engineers_CMD_SOV": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDRSOV SAPERI LDR.",
            "token": "AGYMPGDUXA",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Engineers_CMD_SOV",
                "Unite"
            ],
        },
        "strength": 8,
        "WeaponAssignment": [
                (0,[0,]),
                (1,[0,]),
                (2,[0,]),
                (3,[0,]),
                (4,[0,]),
                (5,[0,]),
                (6,[0,]),
                (7,[0,1,]),
            ],
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                'leader_sov',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "Divisions": {
            "SOV_119IndTkBrig": {
                "Transports": ["GAZ_66_SOV", "BTR_60_SOV"],
            },
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 8,
                },
            },
        },
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },
    
    "Spetsnaz_CMD_SOV": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDRSOV SPETSNAZ LDR.",
            "token": "CKLQCEBSOY",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Spetsnaz_CMD_SOV",
                "Unite",
                "noSIGINT",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry_sf", "Texture_sf"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                'leader_sov',
                '_sf',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry_sf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "SOV_119IndTkBrig": {
                "Transports": ["GAZ_66_SOV", "BTR_60_SOV"],
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
        "max_speed": 26,
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "VDV_CMD_SOV": {
        "CommandPoints": 50,
        "GameName": {
            "display": "#LDRSOV DESANTNIKI LDR.",
            "token": "JSBZIJKKJJ",
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
                "UNITE_VDV_CMD_SOV",
                "Unite",
            ],
        },
        "strength": 6,
        "WeaponAssignment": [
                (0,[1,]),
                (1,[0,]),
                (2,[0,]),
                (3,[0,]),
                (4,[0,3]),
                (5,[0,2,]),
            ],
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                'leader_sov',
                '_ifv',
                '_choc',
                '_para',
                'infantry_equip_heavy',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 5,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 20,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AK_74": 5,
                },
            },
            "Salves": {
                "PM_AKSU_74": 7,
                "SAW_RPK_74_5_56mm": 10,
                "MANPAD_igla": 4,
                "Grenade_SMOKE": 3,
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "Engineers_CMD_VDV_SOV": {
        "CommandPoints": 50,
        "GameName": {
            "display": "#LDRSOV DESANT. SAPERI LDR.",
            "token": "SWFVKVIZVT",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Engineers_CMD_TTsko_SOV",
                "Unite"
            ],
        },
        "strength": 8,
        "WeaponAssignment": [
                (0,[0,]),
                (1,[0,]),
                (2,[0,]),
                (3,[0,]),
                (4,[0,]),
                (5,[0,]),
                (6,[0,]),
                (7,[0,1,]),
            ],
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                'leader_sov',
                '_choc',
                '_para',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_AKS_74": 8,
                },
            },
            "Salves": {
                "FM_AKS_74": 9,
                "RocketInf_RPG7": 6,
            },
        },
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "MTLB_CMD_SOV": {
        "CommandPoints": 60,
        "GameName": {
            "display": "#LDRSOV MT-LBu MASHINA",
            "token": "PUEZYZBZLF",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_MTLB_CMD_SOV",
                "Unite",
                "Vehicule",
            ],
        },
        "Factory": "EDefaultFactories/Art",
        "IdentifiedTextures": ["Texture_RTS_H_appui", "Texture_appui"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_amphibie',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_appui",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Transport",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "T80BV_CMD_SOV": {
        "CommandPoints": 225,
        "GameName": {
            "display": "#LDRSOV T-80BVK LDR.",
            "token": "YWAOJLFAFW",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T80BV_CMD_SOV",
                "Unite",
            ],
        },
        "armor": {
            "front": 18,
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'Armor_heavy',
                'leader_sov',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "MotRifles_CMD_DDR": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDRSOV MOT.-SCHUTZEN LDR.",
            "token": "LJDWEYDMZI",
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
                "UNITE_MotRifles_CMD_DDR",
                "Unite",
            ],
        },
        "strength": 6,
        "WeaponAssignment": [
                (0,[1,]),
                (1,[0,]),
                (2,[0,]),
                (3,[0,]),
                (4,[0,3]),
                (5,[0,2]),
            ],
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                'leader_sov',
                '_ifv',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 7,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_Mpi_AK_74N": 5,
                },
            },
            "Salves": {
                "RocketInf_RPG18_64mm": 6,
            },
        },
        "selector_tactic": "(0, 6)",
        "selector_tactic_obj": "00_06",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "Engineers_CMD_DDR": {
        "CommandPoints": 50,
        "GameName": {
            "display": "#LDRSOV PIONIER LDR.",
            "token": "KYSSUXXTDG",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Engineers_CMD_DDR",
                "Unite"
            ],
        },
        "strength": 8,
        "WeaponAssignment": [
                (0,[0,]),
                (1,[0,]),
                (2,[0,]),
                (3,[0,]),
                (4,[0,]),
                (5,[0,]),
                (6,[0,]),
                (7,[0,1,]),
            ],
        "TransportedTexture": "UseInGame_Transport_assault",
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                'leader_sov',
                '_choc',
                '_resolute',
                'infantry_equip_medium',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": 7,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_Mpi_AK_74N": 8,
                },
            },
            "Salves": {
                "FM_Mpi_AK_74N": 9,
                "RocketInf_RPG7VL": 6,
            },
        },
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },

    "BTR_50_CMD_DDR": {
        "CommandPoints": 60,
        "GameName": {
            "display": "#LDRSOV SPW-50PU(A)",
            "token": "MXTHDKLGFB",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_BTR_50_CMD_DDR",
                "Unite",
                "Vehicule",
            ],
        },
        "Factory": "EDefaultFactories/Art",
        "IdentifiedTextures": ["Texture_RTS_H_appui", "Texture_appui"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'leader_sov',
                '_amphibie',
                '_resolute',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_appui",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Transport",
        "availability": 2,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "T55A_CMD_DDR": {
        "CommandPoints": 85,
        "GameName": {
            "display": "#LDRSOV FUPZ. T-55AK LDR.",
            "token": "VKLRXNSTQE",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T55A_CMD_DDR",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'armor',
                'leader_sov',
                '_resolute',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": 6,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "T72M_CMD_DDR": {
        "CommandPoints": 170,
        "GameName": {
            "display": "#LDRSOV FUPZ. T-72M LDR.",
            "token": "XVEZUMJKLL",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_T72M_CMD_DDR",
                "Unite",
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'Armor_heavy',
                'leader_sov',
                '_resolute',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },
    
    "Territorial_CMD_UK": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDR TERRIERS LDR.",
            "token": "QMPRIAZFYF",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Territorial_CMD_UK",
                "Unite",
            ],
        },
        "strength": 7,
        "WeaponAssignment": [
                (0,[1,]),
                (1,[1,]),
                (2,[1,]),
                (3,[1,]),
                (4,[0,]),
                (5,[0,]),
                (6,[0,2,]),
            ],
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 7,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_Sterling": 3,
                },
            },
            "Salves": {
                "PM_Sterling": 12,
            },
        },
        "selector_tactic": "(0, 2)",
        "selector_tactic_obj": "00_02",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },
    
    "Engineers_CMD_UK": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDR ASSAULT PIONEERS LDR.",
            "token": "VZOODKAGWE",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Engineers_CMD_UK",
                "Unite",
            ],
        },
        "strength": 8,
        "WeaponAssignment": [
                (0,[0,]),
                (1,[0,]),
                (2,[0,]),
                (3,[0,]),
                (4,[0,]),
                (5,[0,]),
                (6,[0,]),
                (7,[0,]),
            ],
        "TransportedTexture": "UseInGame_Transport_assault",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'engineer',
                '_leader',
                '_choc',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": 7,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_Sterling": 8,
                },
            },
            "Salves": {
                "PM_Sterling": 12,
            },
        },
        "selector_tactic": "(0, 8)",
        "selector_tactic_obj": "00_08",
        "is_infantry": True,
        "is_ground_vehicle": False,
    },
    
    "Rifles_CMD_UK": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDR RIFLES LDR.",
            "token": "YGMKZKXXEV",
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
                "UNITE_Rifles_CMD_UK",
                "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                '_ifv',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 7,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
    },
    
    "Airmobile_CMD_UK": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDR AIRMOBILE LDR.",
            "token": "CFLNZATSET",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Airmobile_CMD_UK",
                "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 7,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
    },
    
    "Airmobile_Mot_CMD_UK": {
        "CommandPoints": 40,
        "GameName": {
            "display": "#LDR MOT. AIRMOBILE LDR.",
            "token": "DPDYRJPOBS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Mot_Airmobile_CMD_UK",
                "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'infantry',
                '_leader',
                'infantry_equip_light',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": 7,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
    },
    
    "Challenger_1_Mk1_CMD_UK": {
        "CommandPoints": 205,
        "GameName": {
            "display": "#LDR CHALLENGER MK.2 LDR.",
            "token": "LDRSOVCHAL",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_Challenger_1_Mk1_CMD_UK",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor_heavy", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "SpecialtiesList": {
            "overwrite_all": [
                'Armor_heavy',
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor_heavy",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor_Heavy",
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },
}
#fmt: on
