uk_unit_edits = {
    #UK LOG
    "LandRover_CMD_UK": {
        "CommandPoints": 145,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
    
    "Saxon_CMD_UK": {
        "CommandPoints": 155,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
    
    "Gazelle_CMD_UK": {
        "CommandPoints": 115,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
    #UK INF
    "LandRover_UK": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    
    "Bedford_MJ_4t_trans_UK": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    
    "Gun_Group_TA_UK": {
        "CommandPoints": 15,
        "availability": 12,
        "Strength": 5,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "WeaponAssignment": [
                (0,[1,]),
                (1,[1,]),
                (2,[0,]),
                (3,[0,]),
                (4,[0,]),
            ],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_L1A1_SLR": (1, 2, 3), # weapon index, current quanity, new quantity
                },
            },
        },
    },
    
    "RMP_UK": {
        "CommandPoints": 20,
        "availability": 12,
        "Strength": 5,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "WeaponAssignment": [
                (0,[2,]),
                (1,[1,]),
                (2,[1,]),
                (3,[0,]),
                (4,[0,]),
            ],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_Sterling": (1, 1, 2),
                },
            },
        },
    },
    
    "Security_UK": {
        "CommandPoints": 25,
    },
    
    "Territorial_UK": {
        "CommandPoints": 30,
        "availability": 12,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "AT_Group_TA_UK": {
        "CommandPoints": 25,
        "availability": 12,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_Carl_Gustav": 6,
            },
        },
    },
    
    "Airmobile_UK": { # 3x FN Mag
        "CommandPoints": 40,
        "availability": 12,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },
    
    "Airmobile_MILAN_UK": {
        "CommandPoints": 50,
        "availability": 12,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "XPMultiplier": [1.0, 0.75, 0.6, 0.0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_LAW_80": 6,
            },
        },
    },
    
    "Engineers_Airmobile_UK": {
        "CommandPoints": 45,
        "availability": 8,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_Carl_Gustav": 8,
            },
        },
    },
    
    "Engineers_TA_UK": {
        "CommandPoints": 35,
        "availability": 10,
        "max_speed": 26,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "NATO_Garnison_Berlin": {
                "cards": 1,
            },
            "UK_2nd_Infantry": {
                "cards": 2,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Airmobile_Mot_UK": {
        "CommandPoints": 35,
        "availability": 12,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_Carl_Gustav": 8,
            },
        },
    },
    
    "Rifles_UK": {
        "CommandPoints": 25,
        "availability": 12,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },
    
    "RCL_L6_Wombat_UK": {
        "CommandPoints": 35,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "max_speed": 9,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        }, 
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },
    
    "ATteam_Milan_1_UK": {
        "CommandPoints": 30,
        "availability": 9,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "XPMultiplier": [1.0, 0.8, 0.6, 0.0],
    },
    
    "ATteam_Milan_2_UK": {
        "CommandPoints": 45,
        "availability": 6,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "SAS_UK": {
        "CommandPoints": 70,
        "availability": 4,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
    },
    #UK ARTILLERY
    "81mm_mortar_UK": {
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "UK_2nd_Infantry": {
                "cards": 2,
            },
        },
        "availability": 5,
        "XPMultiplier": [0.0, 1.0, 0.8, 0.6],
    },
    
    "Howz_L118_105mm_UK": {
        "CommandPoints": 55,
        "availability": 4,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },
    
    "FH70_155mm_UK": {
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "M107A2_175mm_UK": {
        "CommandPoints": 170,
        "availability": 2,
        "XPMultiplier": [1.0, 0.0, 0.5, 0.0],
    },
    
    "M270_MLRS_cluster_UK": {
        "CommandPoints": 280,
        "availability": 1,
        "Divisions": {
            # "add": ["US_8th_Inf"],
            # "is_transported": False,
            # "needs_transport": False,
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
    #UK TANK
    "Rover_101FC_UK": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "Saxon_UK": {
        "CommandPoints": 15,
        "orders": {
            "remove_orders": ["'sell'"],
        },
    },
    
    "FV603_Saracen_UK": {
        "CommandPoints": 15,
        "orders": {
            "remove_orders": ["'sell'"],
        },
    },
    
    "LandRover_MILAN_UK": {
        "CommandPoints": 40,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "NATO_Garnison_Berlin": {
                "cards": 1,
            },
            "UK_2nd_Infantry": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },
    
    "MCV_80_Warrior_UK": {
        "CommandPoints": 30,
    },
    
    "MCV_80_Warrior_MILAN_UK": {
        "CommandPoints": 40,
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN": 6,
            },
        },
    },
    
    "Challenger_1_Mk1_UK": {
        "CommandPoints": 185,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "UK_1st_Armoured": {
                "cards": 4,
            },
            "UK_2nd_Infantry": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },
    #UK RECON
    "Ferret_Mk2_UK": {
        "CommandPoints": 20,
        "availability": 10,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "FV601_Saladin_UK": {
        "CommandPoints": 35,
        "availability": 8,
    },
    
    "FV721_Fox_UK": {
        "CommandPoints": 35,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },
    
    "Scout_TA_UK": {
        "CommandPoints": 15,
        "availability": 10,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Scout_UK": {
        "CommandPoints": 20,
        "availability": 8,
        "DeploymentShift": 0,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "UK_2nd_Infantry": {
                "cards": 2,
            },
        },
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },
    
    "Scout_Airmobile_UK": {
        "CommandPoints": 35,
        "availability": 6,
        "DeploymentShift": 0,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "Sniper_UK": {
        "CommandPoints": 30,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Gazelle_UK": {
        "CommandPoints": 30,
        "availability": 4,
    },
    #UK DCA
    "MANPAD_Blowpipe_UK": {
        "CommandPoints": 15,
        "availability": 12,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },
    
    "MANPAD_Javelin_UK": {
        "CommandPoints": 35,
        "availability": 9,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "UK_1st_Armoured": {
                "cards": 2,
            },
            "UK_2nd_Infantry": {
                "cards": 3,
            },
            "UK_4th_Armoured": {
                "cards": 2,
            },
        },
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },
    
    "DCA_Javelin_LML_UK": {
        "CommandPoints": 35,
        "availability": 6,
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "stealth": 2.5,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "DCA_Rapier_UK": {
        "CommandPoints": 65,
        "availability": 6,
        "OpticalStrengthAltitude": 225,
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "Tracked_Rapier_UK": {
        "CommandPoints": 85,
        "availability": 4,
        "OpticalStrengthAltitude": 225,
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },
    
    "DCA_Rapier_FSA_UK": { # towed FSB1
        "CommandPoints": 85,
        "availability": 6,
        "OpticalStrengthAltitude": 285,
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    #UK HELI
    "CH47_Chinook_UK": {
        "CommandPoints": 60,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    
    "Lynx_AH_Mk1_UK": {
        "CommandPoints": 50,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    
    "Lynx_AH_Mk1_LBH_UK": {
        "CommandPoints": 70,
    },
    
    "Gazelle_SNEB_UK": {
        "CommandPoints": 40,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },
    
    "Lynx_AH_Mk1_TOW_UK": {
        "CommandPoints": 90,
        "availability": 6,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },
    
    "Lynx_AH_Mk7_I_TOW_UK": { # 8x ITOW
        "CommandPoints": 100,
        "availability": 5,
        "XPMultiplier": [0.0, 1.0, 0.8, 0.0],
    },
    
    "Lynx_AH_Mk7_I_TOW2_UK": { # 8x FITOW
        "CommandPoints": 130,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },
    #UK AIR
    "Harrier_RKT1_UK": { # 36x SNEB, 2x AIM-9L
        "CommandPoints": 110,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace_fixedsalvo": [("RocketAir_SNEB_68mm_x18", "RocketAir_SNEB_68mm_x36")],
            },
            "Salves": {
                "RocketAir_SNEB_68mm": 1,
            },
        },
    },
    
    "Harrier_RKT2_UK": { # 36x SNEB, 36x SNEB
        "CommandPoints": 100,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace_fixedsalvo": [("RocketAir_SNEB_68mm_x18", "RocketAir_SNEB_68mm_x36")],
            },
            "Salves": {
                "RocketAir_SNEB_68mm": 1,
            },
        },
    },
    
    "Harrier_HE1_UK": { # 2x mk83 450kg
        "CommandPoints": 130,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
    
    "Jaguar_CLU_UK": { # 4x BL755 CLU
        "CommandPoints": 205,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
    
    "Jaguar_HE1_UK": { # 8x mk82 227kg
        "CommandPoints": 190,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
    
    "Jaguar_HE2_UK": { # 4x Mk18 513kg
        "CommandPoints": 190,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
    
    "Tornado_ADV_HE_UK": {
        "CommandPoints": 220,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
    
    "Harrier_UK": { # 4x AIM-9L
        "CommandPoints": 100,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },
    
    "F4_Phantom_AA_F3_UK": { # 4x Skyflash, 4x AIM-9L
        "CommandPoints": 145,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },
}