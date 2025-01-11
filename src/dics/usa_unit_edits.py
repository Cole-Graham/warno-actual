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
        #     "game_n": "AIRBORNE ASSAULT ENG.",
        #     "nametoken": "TXOZWRNEVU",
        # },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("MMG_M60E1_7_62mm", "MMG_WA_M60E3_7_62mm")],
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
        "CommandPoints": 30,
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
        "CommandPoints": 30,
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
    },

    "Ranger_Dragon_US": {
        "CommandPoints": 65,
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
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

    "Rifles_half_Dragon_NG_US": {
        "CommandPoints": 30,
        "availability": 15,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_M16A1": 10,
                "MMG_M60E1_7_62mm": 30,
                "M47_DRAGON": 4,
            },
        }
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
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M35_trans_US": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M998_Humvee_US": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M1038_Humvee_US": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    #US ARTILLERY
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
            "game_n": "M270 MLRS",
            "nametoken": "MYQQNJCCAK",
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
    "M113A3_US": {
        "orders": {
            "add_orders": ["sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M113A1_NG_US": {
        "orders": {
            "add_orders": ["sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "M113_Dragon_US": {
        "CommandPoints": 20,
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
            "game_n": "#3RDARM M1A1 ABRAMS",
            "nametoken": "YEMPBPBTNZ",
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
            "game_n": "#RECO3 M981 FISTV",
            "nametoken": "JKFBZFRBYZ",
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
                (0,[1,]),
                (1,[0,]),
                (2,[0,]),
                (3,[0,2,]),
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
                "replace": [("RocketInf_M72A1_LAW_66mm", "RocketInf_M72A3_LAW_66mm")],
            },
        },
        "DeploymentShift": 0,
    },
    #US AA
    "MANPAD_Stinger_C_US": {
        "GameName": {
            "game_n": "STINGER C",
            "nametoken": "XQYDBWCBAP",
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
            "Salves": {
                "FM_M16": 7,
                "MANPAD_FIM92": 6,
            },
        },
    },

    "MANPAD_Stinger_C_para_US": {
        "GameName": {
            "game_n": "AB STINGER C",
            "nametoken": "VVEXCPXVQB",
        },
        "CommandPoints": 45,
        "availability": 7,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
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
        "category": "Logistic",
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
        "category": "Logistic",
        "Divisions": {
            "add": ["US_3rd_Arm", "US_8th_Inf"],
            "is_transported": True,
            "needs_transport": True,
            "default": {
                "cards": 1,
                "Transports": ["M998_Humvee_US"],
            },
        },
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 4,
    },

    "M998_Avenger_US": {
        "CommandPoints": 100,
        "availability": 5,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "M48_Chaparral_MIM72F_US": {
        "optics": {
            "OpticalStrengthAltitude": 225,
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
            "OpticalStrengthAltitude": 285,
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
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111F_Aardvark_US": { # 12x mk82, 3rd Armored
        "CommandPoints": 190,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111F_Aardvark_LGB_US": { # 4x GBU-12
        "CommandPoints": 210,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111E_Aardvark_CBU_US": { # 8x Mk-20 Rockeye, 3rd Armored
        "CommandPoints": 190,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111F_Aardvark_CBU_US": { # 8x Mk-20 Rockeye, 82nd Airborne
        "CommandPoints": 190,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111E_Aardvark_napalm_US": { # 4x Mk-77 napalm, 3rd Armored
        "CommandPoints": 190,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "F111F_Aardvark_napalm_US": { # 4x Mk-77 napalm, 82nd Airborne
        "CommandPoints": 190,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "EF111_Raven_US": {
        "CommandPoints": 140,
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
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "F16E_CBU_US": {
        "CommandPoints": 180,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "F16E_AA_US": {
        "CommandPoints": 200,
        "cards": {
            "default": 1,
            "US_8th_Inf": 2,
        },
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
