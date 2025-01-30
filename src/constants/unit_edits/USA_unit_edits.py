"""USA unit edits."""

from typing import Any, Dict

# fmt: off
usa_unit_edits = {
    #US LOG
    "OH58C_CMD_US": {
        "CommandPoints": 115,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "UH60A_CO_US": {
        "CommandPoints": 145,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "M151_MUTT_CMD_US": {
        "CommandPoints": 145,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
  
    "M1025_Humvee_CMD_para_US": {
        "CommandPoints": 145,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
        "SpecialtiesList": {
            "remove_specs": ["'_para'"],
        },
        "ButtonTexture": "M1038_Humvee_US",
        "DeploymentShift": 0,
    },

    "M2A1_Bradley_Leader_US": {
        "CommandPoints": 180,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "M2A2_Bradley_Leader_US": {
        "CommandPoints": 180,
        "availability": 2,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 0.0, 1.0],
    },
    #US INF
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
                    "Commando_733": 4,
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
        "remove_zone_capture": None,
    },

    "Rifles_CMD_US": {
        "CommandPoints": 40,
        "GameName": {
            "token": "SVWNZUYPNE",
            "display": "#LDR MECH. RIFLES LDR.",
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
    },

    "Airborne_CMD_US": {
        "CommandPoints": 70,
        "GameName": {
            "display": "#LDR AIRBORNE LDR.",
            "token": "BHVJUDTEVR",
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
    },
    
    "Engineers_US": {
        "CommandPoints": 45,
        "availability": 7,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "NatGuard_Engineers_US": {
        "CommandPoints": 35,
        "availability": 7,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "AeroEngineers_US": {
        "CommandPoints": 45,
        "availability": 7,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Airborne_Engineers_US": {
        "CommandPoints": 50,
        "availability": 7,
        # "GameName": {
        #     "display": "AIRBORNE ASSAULT ENG.",
        #     "token": "TXOZWRNEVU",
        # },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_inf_M240B_7_62mm", "MMG_WA_M60E3_7_62mm")],
            },
        },
    },

    "Engineers_Flash_US": {
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 2,
            },
        },
        "availability": 10,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "RocketInf_M202_Flash_66mm": 2,
            },
        },
    },

    "Airborne_Engineers_Flash_US": {
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 10,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_inf_M240B_7_62mm", "MMG_WA_M60E3_7_62mm")],
            },
            "Salves": {
                "FM_M16": 9,
                "MMG_WA_M60E3_7_62mm": 30,
                "RocketInf_M202_Flash_66mm": 2,
            },
        },
    },

    "NatGuard_Engineers_Flam_US": {
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 7,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
            "Salves": {
                "PM_GreaseGun": 40,
                "FM_M16A1": 7,
                "MMG_M60E1_7_62mm": 30,
                "flamethrower_M2": 15,
            },
        },
    },

    "NatGuard_Engineers_M67_US": {
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 7,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16A1": 10,
                "RocketInf_M67_RCL_90mm": 8,
            },
        },
    },

    "Engineers_Dragon_US": {
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 2,
            },
        },
        "availability": 7,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "M47_DRAGON": 6,
            },
            "equipmentchanges": {
                "replace": [("M47_DRAGON", "M47_DRAGON_II")],
            },
        },
    },

    "Airborne_Dragon_US": {
        "CommandPoints": 45,
        "availability": 7,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },
    
    "Airborne_MP_US": {
        "CommandPoints": 20,
        "availability": 12,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "MP_US": {
        "CommandPoints": 20,
        "availability": 12,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Airborne_MP_RCL_US": {
        "CommandPoints": 25,
        "availability": 9,
        "XPMultiplier": [0.0, 1.0, 0.8, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
            },
        },
    },

    "MP_RCL_US": {
        "CommandPoints": 25,
        "availability": 9,
        "XPMultiplier": [0.0, 1.0, 0.8, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "RocketInf_M67_RCL_90mm": 6,
            },
        },
    },

    "Rifles_HMG_US": {
        "CommandPoints": 35,
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Airborne_HMG_US": { # AIRBORNE GUNNERS
        "CommandPoints": 35,
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "AeroRifles_US": { # AIR CAV TROOPERS
        "CommandPoints": 40,
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Rifles_US": { # MECH. RIFLES (DRAGON)
        "CommandPoints": 45,
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Rifles_LAW_US": { # MECH. RIFLES (LAW)
        "CommandPoints": 35,
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Rifles_half_LAW_US": {
        "CommandPoints": 25,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "US_24th_Inf": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 3,
            },
            "US_8th_Inf": {
                "cards": 2,
            },
        },
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Rifles_half_AT4_US": {
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 2,
            },
        },
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "SAW_M249_5_56mm": 30,
                "MMG_WA_M60E3_7_62mm": 30,
                "RocketInf_AT4_83mm": 4,
            },
        },
    },

    "Ranger_US": {
        "CommandPoints": 55,
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Commando_733", "M16A1_Carbine")],
            },
        },
    },

    "Ranger_Dragon_US": {
        "CommandPoints": 65,
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Commando_733", "M16A1_Carbine")],
            },
        },
    },
    
    "DeltaForce_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("Commando_733", "M16A1_Carbine")],
            },
        },
    },

    "Airborne_US": {
        "CommandPoints": 55,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 7,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "MMG_inf_M240B_7_62mm": 30,
                "RocketInf_AT4_83mm": 6,
            },
        },
    },

    "Airborne_half_LAW_US": { # AB FIRE TEAM (AT-4)
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "SAW_M249_5_56mm": 30,
                "RocketInf_AT4_83mm": 4,
            },
        },
    },

    "Airborne_half_Dragon_US": {
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "SAW_M249_5_56mm": 30,
                "M47_DRAGON_II": 4,
            },
        },
    },

    "AeroRifles_AB_US": {
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 6,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "AeroRifles_Dragon_US": {
        "CommandPoints": 40,
        "availability": 6,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "SAW_M249_5_56mm": 30,
                "M47_DRAGON_II": 4,
            },
        },
    },

    "Aero_half_AT4_US": {
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "SAW_M249_5_56mm": 30,
                "RocketInf_AT4_83mm": 4,
            },
        },
    },

    "AeroRifles_AT4_US": {
        "CommandPoints": 65,
        "availability": 5,
        "XPMultiplier": [0.0, 1.0, 0.8, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
                "SAW_M249_5_56mm": 30,
                "RocketInf_AT4_83mm": 9,
            },
        },
    },

    "Rifles_half_Dragon_US": {
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "US_24th_Inf": {
                "cards": 2,
            },
            "US_3rd_Arm": {
                "cards": 3,
            },
        },
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "SAW_M249_5_56mm": 30,
                "MMG_WA_M60E3_7_62mm": 30,
                "M47_DRAGON_II": 4,
            },
        }
    },
    
    "Rifles_half_LAW_NG_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "Rifles_half_Dragon_NG_US": {
        "CommandPoints": 30,
        "availability": 15,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
            "Salves": {
                "FM_M16A1": 10,
                "MMG_M60E1_7_62mm": 30,
                "M47_DRAGON": 4,
            },
        }
    },
    
    "NatGuard_M67_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },
    
    "NatGuard_LAW_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },
    
    "NatGuard_Dragon_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "Aero_half_Dragon_US": {
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 7,
                "SAW_M249_5_56mm": 30,
                "M47_DRAGON_II": 4,
            },
        }
    },

    "GreenBerets_ODA_US": {
        "CommandPoints": 85,
        "availability": 3,
        "XPMultiplier": [0.0, 0.0, 0.0, 1.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16", "M16A1_Carbine")],
            },
            "Salves": {
                "M16A1_Carbine": 9,
                "SAW_M249_5_56mm": 30,
                "Sniper_M21": 10,
                "RocketInf_AT4_83mm": 9,
            },
        }
    },

    "ATteam_ITOW_US": {
        "CommandPoints": 60,
        "availability": 6,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "ATteam_TOW2_US": {
        "CommandPoints": 75,
        "availability": 4,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "ATteam_TOW2_Aero_US": {
        "CommandPoints": 75,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "ATteam_TOW2_para_US": {
        "CommandPoints": 75,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "M274_Mule_RCL_US": {
        "CommandPoints": 30,
        "availability": 9,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "M151_MUTT_trans_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M35_trans_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M998_Humvee_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M1038_Humvee_US": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    #US ARTILLERY
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
        "remove_zone_capture": None,
    },
    
    "Mortier_107mm_US": {
        "CommandPoints": 40,
        "availability": 5,
        "XPMultiplier": [1.0, 0.8, 0.6, 0.0],
    },

    "Mortier_107mm_Airborne_US": {
        "CommandPoints": 40,
        "availability": 5,
        "XPMultiplier": [0.0, 1.0, 0.8, 0.6],
    },

    "M125_HOWZ_US": { # M125 mortar carrier, M29A1 81mm Mortar
        "CommandPoints": 45,
        "availability": 4,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },
    "Howz_M102_105mm_US": {
        "CommandPoints": 55,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "M106A2_HOWZ_US": {
        "CommandPoints": 60,
        "availability": 4,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "M109A2_HOWZ_US": {
        "CommandPoints": 165,
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "M110A2_HOWZ_US": {
        "CommandPoints": 200,
        "availability": 2,
        "XPMultiplier": [1.0, 0.0, 0.5, 0.0],
    },

    "M270_MLRS_US": {
        "CommandPoints": 240,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
        "Divisions": {
            "remove": ["US_8th_Inf"]
        },
    },

    "M270_MLRS_cluster_US": {
        "GameName": {
            "display": "M270 MLRS",
            "token": "MYQQNJCCAK",
        },
        "CommandPoints": 280,
        "availability": 1,
        "Divisions": {
            "add": ["US_8th_Inf"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 2,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "AngleRotationMaxPitch": 1.0,
                },
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
    #US TANK/VEHICLE
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
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
        "remove_zone_capture": None,
    },
    
    "M113A3_US": {
        "CommandPoints": 15,
        "orders": {
            "add_orders": ["sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M113A1_NG_US": {
        "CommandPoints": 15,
        "orders": {
            "add_orders": ["sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M113_Dragon_US": {
        "CommandPoints": 15,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("M47_DRAGON", "M47_DRAGON_II")],
            },
        },
    },

    "M1025_Humvee_TOW_para_US": {
        "CommandPoints": 65,
        "stealth": 1.5,
        "availability": 6,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "M901A1_ITW_US": { # TOW 2
        "CommandPoints": 65,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "M901_TOW_US": { # ITOW
        "CommandPoints": 50,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "M728_CEV_US": {
        "CommandPoints": 65,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "M2A1_Bradley_IFV_US": {
        "CommandPoints": 65,
    },

    "M2A2_Bradley_IFV_US": {
        "CommandPoints": 80,
    },

    "M1A1HA_Abrams_US": {
        "CommandPoints": 310,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
    },

    "M1A1_Abrams_US": {
        "GameName": {
            "display": "#3RDARM M1A1 ABRAMS",
            "token": "YEMPBPBTNZ",
        },
        "CommandPoints": 225,
        "Divisions": {
            "remove": ["US_8th_Inf"],
            "default": {
                "cards": 5,
            },
        },
        "availability": 5,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "M1IP_Abrams_US": {
        "CommandPoints": 190,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "US_24th_Inf": {
                "cards": 3,
            },
            "US_101st_Airmobile": {
                "cards": 2,
            },
            "NATO_Garnison_Berlin": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],   
    },

    "M1_Abrams_US": {
        "CommandPoints": 160,
        "availability": 6,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],   
    },

    "M1_Abrams_NG_US": {
        "CommandPoints": 150,
        "availability": 6,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.0, 0.0, 0.0],   
    },

    "M60A3_Patton_US": {
        "CommandPoints": 105,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],   
    },

    "M60A3_ERA_Patton_US": {
        "CommandPoints": 110,
        "availability": 6,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],   
    },

    "M60A3_Patton_NG_US": {
        "CommandPoints": 110,
        "availability": 10,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],   
    },

    "M60A1_RISE_Passive_US": {
        "CommandPoints": 80,
        "availability": 10,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],   
    },

    "M551A1_TTS_Sheridan_US": {
        "CommandPoints": 50,
        "availability": 10,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],   
    },
    #US RECON
    "M151A2_scout_US": {
        "CommandPoints": 25,
    },

    "M113_ACAV_US": {
        "CommandPoints": 35,
    },

    "M1025_Humvee_scout_US": {
        "CommandPoints": 25,
    },

    "M1025_Humvee_AGL_US": {
        "CommandPoints": 30,
    },

    "M1025_Humvee_AGL_nonPara_US": {
        "CommandPoints": 30,
    },

    "M981_FISTV_US": {
        "availability": 8,
        "GameName": {
            "display": "#RECO3 M981 FISTV",
            "token": "JKFBZFRBYZ",
        },
        "TagSet": {
            "add_tags": ['"reco_radar"'],
        },
        "optics": {
            "OpticalStrength": 233.475
        },
        "XPMultiplier": [1.0, 0.0, 0.0, 0.0],  
    },

    "M113A1_TOW_US": {
        "CommandPoints": 55,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "LAV_25_M1047_US_US": {
        "CommandPoints": 70,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_team_7_62mm_M60", "MMG_turret_7_62mm_M60")],
            },
        },

    },

    "M3A1_Bradley_CFV_US": {
        "CommandPoints": 105,
        "availability": 4,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "M3A2_Bradley_CFV_US": {
        "CommandPoints": 135,
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "M551A1_ACAV_Sheridan_US": {
        "CommandPoints": 55,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "OH58C_Scout_US": {
        "CommandPoints": 40,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "OH58D_Combat_Scout_US": {
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "ECM:": -0.1,
    },

    "OH58D_Kiowa_Warrior_US": {
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "ECM": -0.1,
    },

    "EH60A_EW_US": {
        "availability": 3,
        "Divisions": {
            "add": ["US_3rd_Arm"],
            "is_transported": False,
            "needs_transport": False,
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "Airborne_Scout_US": {
        "CommandPoints": 25,
        "availability": 7,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 9,
            },
        },
    },

    "Scout_US": {
        "WeaponAssignment": [
                (0, [1, ]),
                (1, [0, ]),
                (2, [0, ]),
                (3, [0, 2, ]),
            ],
        "CommandPoints": 20,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "Divisions": {
            "is_transported": True,
            "needs_transport": False,
            "default": {
                "Transports": [
                    "M151_MUTT_trans_US",
                    "M151A2_scout_US",
                    "M113_ACAV_US",
                    "M113A3_US",
                ],
            },
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16": 11,
                "MMG_inf_M240B_7_62mm": 30,
                "add": [(2, 4)],
            },
            "equipmentchanges": {
                "add": [(2, "RocketInf_M72A3_LAW_66mm")] # (turret, salves, weapon)
            },
        },
    },
    
    "HvyScout_NG_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },
    
    "HvyScout_NG_Dragon_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_WA_M60E3_7_62mm", "MMG_M60E1_7_62mm")],
            },
        },
    },

    "LRRP_US": {
        "CommandPoints": 60,
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
        "Divisions": {
            "default": {
                "Transports": ["M998_Humvee_US", "UH60A_Black_Hawk_US"],
            },
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    ("Commando_733", "M16A1_Carbine"),
                    ("RocketInf_M72A1_LAW_66mm", "RocketInf_M72A3_LAW_66mm"),
                ],
            },
        },
        "DeploymentShift": 0,
    },
    #US AA
    "MANPAD_Stinger_C_US": {
        "GameName": {
            "display": "STINGER C",
            "token": "XQYDBWCBAP",
        },
        "CommandPoints": 45,
        "Divisions": {
            "remove": ["US_82nd_Airborne"],
            "default": {
                "cards": 2,
            },
            "NATO_Garnison_Berlin": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 3,
            },
            "US_8th_Inf": {
                "cards": 3,
            },
        },
        "availability": 7,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16", "FM_M16_noreflex")],
            },
            "Salves": {
                "FM_M16": 7,
                "MANPAD_FIM92": 6,
            },
        },
    },
    
    "MANPAD_Stinger_C_Aero_US": {
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16", "FM_M16_noreflex")],
            },
        },
    },

    "MANPAD_Stinger_C_para_US": {
        "GameName": {
            "display": "AB STINGER C",
            "token": "VVEXCPXVQB",
        },
        "CommandPoints": 45,
        "availability": 7,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("FM_M16", "FM_M16_noreflex")],
            },
            "Salves": {
                "FM_M16": 7,
                "MANPAD_FIM92": 6,
            },
        },
    },

    "M163_CS_US": {
        "CommandPoints": 40,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "M163_PIVADS_US": {
        "CommandPoints": 65,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        # "SpecialtiesList": {
        #     "add_specs": ["'normal_airoptics'"],
        # },
    },

    "DCA_M167_Vulcan_20mm_US": {
        "CommandPoints": 25,
        "Factory": "EDefaultFactories/Logistic",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 4,
    },
    
    "DCA_M167A2_Vulcan_20mm_US": {
        "CommandPoints": 25,
        "Factory": "EDefaultFactories/Logistic",
        "Divisions": {
            "add": ["US_3rd_Arm", "US_8th_Inf", "UK_2nd_Infantry"],
            "is_transported": True,
            "needs_transport": True,
            "default": {
                "cards": 1,
                "Transports": ["M998_Humvee_US"],
            },
            "UK_2nd_Infantry": {
                "cards": 1,
                "Transports": ["LandRover_UK"],
            },
        },
        "availability": 6,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "max_speed": 4,
    },

    "M998_Avenger_US": {
        "CommandPoints": 100,
        "availability": 5,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "M48_Chaparral_MIM72F_US": {
        "optics": {
            "OpticalStrengthAltitude": 220,
        },
        "CommandPoints": 130,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "DCA_I_Hawk_US": {
        "CommandPoints": 90,
        "optics": {
            "OpticalStrengthAltitude": 300,
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },
    #US HELI
    "UH60A_Black_Hawk_US": {
        "CommandPoints": 60,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "MMG_M240d_7_62mm": 60,
            },
        },
    },

    "CH47_Chinook_US": {
        "CommandPoints": 60,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "AH6C_Little_Bird_US": {
        "CommandPoints": 45,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 6,
        "XPMultiplier": [0.0, 0.0, 0.0, 1.0],
    },

    "AH6G_Little_Bird_US": {
        "CommandPoints": 60,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 0.0, 1.0],
    },

    "OH58_CS_US": {
        "CommandPoints": 75,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "MH_60A_DAP_US": {
        "CommandPoints": 120,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 0.0, 0.0, 1.0],
    },

    "AH1F_ATAS_US": {
        "CommandPoints": 130,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "AH1F_Cobra_US": {
        "CommandPoints": 120,
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "US_101st_Airmobile": {
                "cards": 1,
            },
            "US_11ACR": {
                "cards": 1,
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "AH1S_Cobra_US": {
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "US_3rd_Arm": {
                "cards": 2,
            },
            "US_82nd_Airborne": {
                "cards": 1,
            },
            "US_101st_Airmobile": {
                "cards": 1,
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "AH1F_Hog_US": {
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 2,
            },
            "US_8th_Inf": {
                "cards": 2,
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "AH1F_HeavyHog_US": {
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "AH64_Apache_US": { # 8x Hellfire / Hydra
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.49],
    },

    "AH64_Apache_emp1_US": { # 16x Hellfire
        "CommandPoints": 215,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 3,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.49],
    },

    "AH64_Apache_emp2_US": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_3rd_Arm": {
                "cards": 3,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.49],
    },

    "AH64_Apache_ATAS_US": {
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.49],
    },
    #US Air
    "F4E_Phantom_II_AA_US": {
        "CommandPoints": 165,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "F15C_Eagle_AA_US": {
        "CommandPoints": 280,
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1375,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.49],
    },

    "F4_Wild_Weasel_US": {
        "CommandPoints": 190,
        "optics": {
            "SpecializedOpticalStrengths": {
                "EVisionUnitType/AntiRadar": 1850.0,
            },
        },
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.49],
    },

    "F4E_Phantom_II_HE_US": {
        "CommandPoints": 165,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F4E_Phantom_II_CBU_US": {
        "CommandPoints": 165,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F4E_Phantom_II_napalm_US": {
        "CommandPoints": 150,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111E_Aardvark_US": { # 12x mk82, 3rd Armored
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111F_Aardvark_US": { # 12x mk82, 3rd Armored
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111F_Aardvark_LGB_US": { # 4x GBU-12
        "CommandPoints": 210,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111E_Aardvark_CBU_US": { # 8x Mk-20 Rockeye, 3rd Armored
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111F_Aardvark_CBU_US": { # 8x Mk-20 Rockeye, 82nd Airborne
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111E_Aardvark_napalm_US": { # 4x Mk-77 napalm, 3rd Armored
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111F_Aardvark_napalm_US": { # 4x Mk-77 napalm, 82nd Airborne
        "CommandPoints": 190,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "EF111_Raven_US": {
        "CommandPoints": 180,
        "max_speed": 1400,
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0]
    },

    "F16C_LGB_US": {
        "CommandPoints": 220,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F16E_AGM_US": { # 4x AGM-65D, 2x AIM-9M
        "CommandPoints": 195,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F16E_HE_US": {
        "CommandPoints": 195,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F16E_napalm_US": {
        "CommandPoints": 195,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "F16E_SEAD_US": {
        "CommandPoints": 215,
        "availability": 3,
        "WeaponDescriptor": {
            "turrets": {
                2: {
                    "AngleRotationMax": 1.745329,
                    "AngleRotationMaxPitch": 0.8726646,
                    "AngleRotationMinPitch": -0.8726646,
                },
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "F16E_CBU_US": {
        "CommandPoints": 180,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "F16E_AA_US": {
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_8th_Inf": {
                "cards": 2,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "A10_Thunderbolt_II_US": { # 8x mk.82, 2x AIM-9M
        "CommandPoints": 220,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 500,
            },
        },
        "max_speed": 500,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "A10_Thunderbolt_II_Rkt_US": { # 76x Hydra, 2x AIM-9M
        "CommandPoints": 220,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 500,
            },
        },
        "max_speed": 500,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "A10_Thunderbolt_II_ATGM_US": { # 76x Hydra, 2x AIM-9M
        "CommandPoints": 240,
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 500,
            },
        },
        "max_speed": 500,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
    
}
