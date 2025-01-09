# fmt: off
sov_unit_edits = {
    #SOV LOG
    "BMD_1_CMD_SOV": {
        "CommandPoints": 145,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "BMP_1_CMD_SOV": {
        "CommandPoints": 155,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "BMD_2_CMD_SOV": {
        "CommandPoints": 160,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "LUAZ_967M_CMD_VDV_SOV": {
        "CommandPoints": 145,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
        "SpecialtiesList": {
            "remove_specs": ["'_para'"],
        },
        "ButtonTexture": "LUAZ_967M_SOV",
        "DeploymentShift": 0,
    },

    "BMP_2_CMD_SOV": {
        "CommandPoints": 170,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },
    
    "BTR_60_CMD_SOV": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "BTR_80_CMD_SOV": {
        "CommandPoints": 170,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },

    "Mi_8K_CMD_SOV": {
        "CommandPoints": 145,
        "availability": 3,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
    },
    #SOV INF
    "Engineers_SOV": {
        "CommandPoints": 40,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_119IndTkBrig": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 30,
                "Grenade_Satchel_Charge": 5,
            },
        },
    },
        
    "Engineers_TTsko_SOV": {
        "CommandPoints": 40,
        "availability": 8,
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
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 30,
                "Grenade_Satchel_Charge": 5,
            },
        },
    },

    "Engineers_VDV_SOV": {
        "CommandPoints": 30,
        "availability": 10,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Engineers_Flam_SOV": {
        "CommandPoints": 50,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "SOV_119IndTkBrig": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 7,
                "MMG_PKM_7_62mm": 30,
                "RocketInf_RPO_A_93mm": 4,
            },
        },
    },

    "Engineers_Flam_TTsko_SOV": {
        "CommandPoints": 50,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 7,
                "MMG_PKM_7_62mm": 30,
                "RocketInf_RPO_A_93mm": 4,
            },
        },
    },

    "Engineers_Flam_VDV_SOV": {
        "CommandPoints": 35,
        "availability": 10,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 7,
            },
        },
    },
    
    "MotRifles_SOV": {
        "CommandPoints": 30,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "SOV_119IndTkBrig": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "MotRifles_TTsko_SOV": { # RPG-27
        "CommandPoints": 30,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 9,
                "SAW_RPK_74_5_56mm": 10,
                "RocketInf_RPG27_105mm": 4,
            },
        },
    },

    "MotRifles_BTR_TTsko_SOV": { # RPG-26
        "CommandPoints": 30,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "SAW_RPK_74_5_56mm": 10,
                "RocketInf_RPG26_72_5mm": 7,
            },
        },
    },

    "MotRifles_Metis_TTsko_SOV": {
        "CommandPoints": 40,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 7,
                "SAW_RPK_74_5_56mm": 10,
                "ATGM_9K115_Metis": 6,
            },
        },
    },

    "VDV_Mech_SOV": { # RPK, SVD, RPG-7VL
        "CommandPoints": 40,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 2,
            },
            "SOV_76_VDV": {
                "cards": 3,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 9,
            },
        },
    },

    "VDV_SOV": { # RPK, SVD, RPG-7VL
        "CommandPoints": 40,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 3,
            },
            "SOV_76_VDV": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 9,
            },
        },
    },

    "VDV_Combine_SOV": { # RPK, SVD, RPG-7VL
        "CommandPoints": 50,
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 9,
                "RocketInf_RPG22_72_5mm": 4,
            },
        },
    },

    "VDV_Metis_SOV": {
        "CommandPoints": 50,
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AKS_74": 7,
                "ATGM_9K115_Metis": 5,
            },
        },
    },

    "MP_SOV": {
        "CommandPoints": 15,
        "availability": 12,
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
            "Salves": {
                "FM_AK_74": 11,
            },
        },
    },

    "VDV_HMG_SOV": { # VDV Pulmetchiki
        "CommandPoints": 35,
        "availability": 12,
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
    
    "MotRifles_HMG_SOV": { # Pulmetchiki
        "CommandPoints": 35,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 30,
                "RocketInf_RPG22_72_5mm": 6,
            },
        },
    },

    "MotRifles_HMG_TTsko_SOV": { # Pulmetchiki
        "CommandPoints": 35,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 11,
                "MMG_PKM_7_62mm": 30,
                "RocketInf_RPG22_72_5mm": 6,
            },
        },
    },

    "FireSupport_TTsko_SOV": {
        "CommandPoints": 25,
        "availability": 12,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "FM_AK_74": 7,
                "RocketInf_RPG29_105mm": 6,
            },
        },  
    },
    
    "Spetsnaz_SOV": {
        "CommandPoints": 70,
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPO_A_93mm": 6,
            },
        },
    },

    "Spetsnaz_Vympel_SOV": { # Spetsgruppa Vympel
        "CommandPoints": 70,
        "availability": 5,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.8],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "PM_AKSU_74": 9,
                "RocketInf_RPG27_105mm": 6,
            },
        },
    },
    
    "Spetsnaz_FireSupport_SOV": {
        "CommandPoints": 30,
        "availability": 8,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_RPG29_105mm": 8,
            },
        },
    },

    "HMGteam_AGS17_TTsko_SOV": {
        "Strength": 5,
        "CommandPoints": 35,
        "availability": 9,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "HMGteam_AGS17_VDV_SOV": {
        "Strength": 5,
        "CommandPoints": 35,
        "availability": 9,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 14,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
    },

    "ATteam_RCL_SPG9_VDV_SOV": {
        "Strength": 3,
        "CommandPoints": 30,
        "availability": 10,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Atteam_Fagot_VDV_SOV": {
        "CommandPoints": 30,
        "availability": 9,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.6],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Atteam_Konkurs_VDV_SOV": {
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "UpgradeFromUnit": "ATteam_Faktoriya_VDV_SOV",
    },

    "ATteam_Konkurs_TTsko_SOV": {
        "CommandPoints": 50,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "ATteam_KonkursM_TTsko_SOV": {
        "CommandPoints": 65,
        "availability": 4,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("ATGM_9M113M_KonkursM", "ATGM_inf_9M113M_KonkursM")],
            },
        },
    },

    "LUAZ_967M_SPG9_VDV_SOV": {
        "CommandPoints": 25,
        "availability": 12,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "LUAZ_967M_Fagot_SOV": {
        "CommandPoints": 55,
        "GameName": {
            "game_n": "LuAZ-967M FAKTORIYA",
            "nametoken": "KYODTOGRYC",
        },
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_9K111M_Faktoriya": 6,
            },
        },
    },

    "LUAZ_967M_VDV_SOV": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "UAZ_469_SOV": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "UAZ_469_MP_SOV": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "Ural_4320_trans_SOV": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    "GAZ_66_SOV": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "GAZ_66B_SOV": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "KrAZ_255B_SOV": {
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },
    #SOV ARTILLERY
    "Mortier_2B14_82mm_VDV_SOV": {
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 5,
        "XPMultiplier": [0.0, 1.0, 0.8, 0.6],
    },

    "Mortier_2B14_82mm_VDV_SOV": {
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 5,
        "XPMultiplier": [0.0, 1.0, 0.8, 0.6],
    },
    
    "Mortier_2B9_Vasilek_nonPara_SOV": {
        "CommandPoints": 45,
        "availability": 4,
        "orders": {
            "add_orders": ["ShootOnPositionSmoke", "ShootOnPositionWithoutCorrectionSmoke"],
        },
        "XPMultiplier": [1.0, 0.75, 0.5, 0.0],
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "MountedWeapons": {
                        "add": {
                            "Mortier_Vasilek_indirect_82mm_towed": {
                                "Ammunition": "$/GFX/Weapon/Ammo_Mortier_Vasilek_indirect_82mm_SMOKE_towed",
                                "DispersionRadiusOffColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOffThickness": -0.1,
                                "DispersionRadiusOnColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOnThickness": -0.1,
                                "EffectTag": "'FireEffect_Mortier_Vasilek_indirect_82mm_towed'",
                                "HandheldEquipmentKey": "'MeshAlternative_3'",
                                "ShowDispersion": False,
                                "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                                "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                                "WeaponShootDataPropertyName": ['WeaponShootData_0_3'],
                            },
                        },
                    },
                },
            },
        },
    },

    "Mortier_2B9_Vasilek_SOV": {
        "CommandPoints": 45,
        "availability": 4,
        "orders": {
            "add_orders": ["ShootOnPositionSmoke", "ShootOnPositionWithoutCorrectionSmoke"],
        },
        "XPMultiplier": [0.0, 1.0, 0.75, 0.5],
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "MountedWeapons": {
                        "add": {
                            "Mortier_Vasilek_indirect_82mm_towed": {
                                "Ammunition": "$/GFX/Weapon/Ammo_Mortier_Vasilek_indirect_82mm_SMOKE_towed",
                                "DispersionRadiusOffColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOffThickness": -0.1,
                                "DispersionRadiusOnColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOnThickness": -0.1,
                                "EffectTag": "'FireEffect_Mortier_Vasilek_indirect_82mm_towed'",
                                "HandheldEquipmentKey": "'MeshAlternative_3'",
                                "ShowDispersion": False,
                                "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                                "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                                "WeaponShootDataPropertyName": ['WeaponShootData_0_3'],
                            },
                        },
                    },
                },
            },
        },
    },
    
    "MTLB_Vasilek_SOV": {
        "CommandPoints": 60,
        "availability": 4,
        "orders": {
            "add_orders": ["ShootOnPositionSmoke", "ShootOnPositionWithoutCorrectionSmoke"],
        },
        "XPMultiplier": [1.0, 0.75, 0.5, 0.0],
        "WeaponDescriptor": {
            "turrets": {
                1: {
                    "MountedWeapons": {
                        "add": {
                            "Mortier_Vasilek_indirect_82mm": {
                                "Ammunition": "$/GFX/Weapon/Ammo_Mortier_Vasilek_indirect_82mm_SMOKE",
                                "DispersionRadiusOffColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOffThickness": -0.1,
                                "DispersionRadiusOnColor": "RGBA[0,0,0,0]",
                                "DispersionRadiusOnThickness": -0.1,
                                "EffectTag": "'FireEffect_Mortier_Vasilek_indirect_82mm'",
                                "HandheldEquipmentKey": "'MeshAlternative_4'",
                                "ShowDispersion": False,
                                "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_4'",
                                "WeaponIgnoredPropertyName": "'WeaponIgnored_4'",
                                "WeaponShootDataPropertyName": ['WeaponShootData_0_4'],
                            },
                        },
                    },
                },
            },
        },
    },

    "Howz_D30_122mm_SOV": {
        "CommandPoints": 75,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 5,
        "XPMultiplier": [1.0, 0.8, 0.6, 0.0],
    },

    "2S9_Nona_SOV": {
        "CommandPoints": 85,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "2S23_Nona_SVK_SOV": {
        "CommandPoints": 95,
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "Howz_2A36_Giatsint_B_SOV": {
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "Howz_MstaB_150mm_SOV": {
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "2S1_Gvozdika_SOV": {
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_56_AirAslt_Brig": {
                "cards": 1,
            },
            "SOV_6IndMSBrig": {
                "cards": 3,
            },
        },
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "2S3M_Akatsiya_SOV": {
        "CommandPoints": 165,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "2S3M1_Akatsiya_SOV": {
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_56_AirAslt_Brig": {
                "cards": 1,
            },
            "SOV_6IndMSBrig": {
                "cards": 3,
            },
        },
        "availability": 2,
        "XPMultiplier": [1.0, 0.0, 0.5, 0.0],
    },

    "BM21V_GradV_SOV": {
        "CommandPoints": 85,
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "BM21_Grad_SOV": {
        "CommandPoints": 175,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 3,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "TOS1_Buratino_SOV": {
        "CommandPoints": 230,
        "availability": 2,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },
    #SOV TANK/VEHICLE
    "MTLB_transp_SOV": {
        "orders": {
            "add_orders": ["sell"],
        },
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "BTR_D_SOV": {
        "CommandPoints": 20,
    },

    "BTR_D_Robot_SOV": { # 10x Konkurs, 2x PKT
        "CommandPoints": 30,
    },
    
    "BTR_60_SOV": {
        "CommandPoints": 20,
    },

    "BTR_80_SOV": {
        "CommandPoints": 25,
    },

    "BMP_1P_SOV": {
        "CommandPoints": 35,
        "GameName": {
            "game_n": "BMP-1P (FAKTORIYA)",
            "nametoken": "CVRIKDQELZ",
        },
    },

    "BMD_2_SOV": {
        "CommandPoints": 35,
    },

    "BMP_2_SOV": {
        "CommandPoints": 50,
    },

    "BMP_2AG_SOV": {
        "CommandPoints": 60,
    },

    "BMP_3_SOV": {
        "CommandPoints": 80,
    },

    "BMD_3_SOV": {
        "CommandPoints": 80,
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "LUAZ_967M_Fagot_VDV_SOV": {
        "CommandPoints": 35,
        "GameName": {
            "game_n": "DESANT. LuAZ FAKTORIYA",
            "nametoken": "SXGTONCUAP",
        },
        "availability": 10,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "BRDM_2_Konkurs_SOV": {
        "Strength": 8,
        "CommandPoints": 50,
        "stealth": 1.5,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "BRDM_2_Konkurs_M_SOV": {
        "Strength": 8,
        "CommandPoints": 65,
        "stealth": 1.5,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "AT_T12_Rapira_SOV": {
        "CommandPoints": 55,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "AT_2A45_SprutB_SOV": {
        "CommandPoints": 55,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "TO_55_SOV": {
        "CommandPoints": 60,
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "T80BV_SOV": {
        "armor": {
            "front": 18,
        },
        "CommandPoints": 215,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_79_Gds_Tank": {
                "cards": 3,
            },
        },
        "availability": 6,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },
    
    "T80U_SOV": {
        "CommandPoints": 260,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },
    
    "T80UD_SOV": {
      "CommandPoints": 290, 
      "Divisions": {
            "default": {
                "cards": 4,
            },
        },
      "availability": 3,
      "XPMultiplier": [0.0, 0.0, 1.0, 0.68],
    },
    
    #SOV RECON
    "UAZ_469_Reco_SOV": {
        "CommandPoints": 25,
    },

    "LUAZ_967M_AGL_VDV_SOV": {
        "CommandPoints": 30,
    },

    "BTR_D_reco_SOV": {
        "CommandPoints": 25,
    },

    "BMP_2_reco_SOV": {
        "CommandPoints": 75,
    },

    "BRM_1_SOV": {
        "CommandPoints": 60,
        "cards": {
            "default": 2,
            "SOV_6IndMSBrig": 1,
        },
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_6IndMSBrig": {
                "cards": 3,
            },
        },
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
    },

    "BMD_1_Reostat_SOV": {
        "CommandPoints": 20,
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "BMD_3_reco_SOV": {
        "CommandPoints": 105,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "BRDM_2_SOV": {
        "Strength": 8,
        "CommandPoints": 35,
        "availability": 8,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_6IndMSBrig": {
                "cards": 1,
            },
        },
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "Pchela_1T_SOV": {
        "CommandPoints": 45,
    },

    "Scout_TTsko_SOV": {
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 8,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Scout_VDV_SOV": {
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 8,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Scout_SIGINT_SOV": {
        "CommandPoints": 30,
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Engineers_Scout_SOV": {
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "DeploymentShift": 0,
    },

    "Engineers_Scout_TTsko_SOV": {
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "HvyScout_SOV": {
        "CommandPoints": 40,
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "DeploymentShift": 0,
    },

    "HvyScout_TTsko_SOV": {
        "CommandPoints": 40,
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "DeploymentShift": 0,
    },

    "Scout_LRRP_SOV": { # Spetsnaz GRU
        "CommandPoints": 45,
        "availability": 4,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.75],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },

    "Scout_Spetsnaz_SOV": {
        "CommandPoints": 60,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "DeploymentShift": 0,
    },

    "Scout_Spetsnaz_VDV_SOV": {
        "CommandPoints": 70,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Mi_24K_reco_SOV": {
        "CommandPoints": 150,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },
    #SOV AA
    "BTR_ZD_Skrezhet_SOV": {
        "CommandPoints": 30,
    },

    "LuAZ_967M_AA_VDV_SOV": {
        "CommandPoints": 30,
        "Stealth": 2.0,
    },

    "DCA_ZU_23_2_TTsko_SOV": {
        "CommandPoints": 20,
        "category": "Logistic",
        "Divisions": {
            "add": ["SOV_119IndTkBrig"],
            "is_transported": True,
            "needs_transport": True,
            "default": {
                "cards": 1,
                "Transports": ["GAZ_66_SOV"],
            },
        },
        "availability": 12,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 4,
    },

    "DCA_ZU_23_2_SOV": { # Airborne
        "CommandPoints": 20,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "category": "Logistic",
        "availability": 12,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 4,
    },
    
    "MANPAD_Igla_SOV": {
        "CommandPoints": 35,
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "MANPAD_Igla_TTsko_SOV": {
        "CommandPoints": 35,
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "MANPAD_Igla_VDV_SOV": {
        "CommandPoints": 35,
        "availability": 7,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "GAZ_66B_ZU_SOV": {
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 69,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 1,
            },
            "SOV_76_VDV": {
                "cards": 2,
            },
        },
        "availability": 10,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "BRDM_Strela_1_SOV": {
        "Strength": 8,
        "CommandPoints": 40,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 7,
        "XPMultiplier": [1.0, 0.75, 0.0, 0.0],
    },

    "Tunguska_2K22_SOV": {
        "optics": {
            "OpticalStrengthAltitude": 285,
        },
        "CommandPoints": 135,
        "Divisions": {
            "default": {
                "cards": 3,
            },
            "SOV_6IndMSBrig": {
                "cards": 4,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },

    "Tor_SOV": {
        "optics": {
            "OpticalStrengthAltitude": 285,
        },
        "CommandPoints": 150,
        "Divisions": {
            "default": {
                "cards": 3,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },
    
    "MTLB_Strela10_SOV": {
        "optics": {
            "OpticalStrengthAltitude": 225,
        },
        "CommandPoints": 65,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 6,
        "XPMultiplier": [1.0, 0.68, 0.0, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "MTLB_Strela10M3_SOV": {
        "optics": {
            "OpticalStrengthAltitude": 225,
        },
        "CommandPoints": 100,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },
    #SOV HELI
    "Mi_2_trans_SOV": {
        "CommandPoints": 35,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "Mi_8TV_non_arme_SOV": {
        "CommandPoints": 50,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'"],
        },
    },

    "Mi_8TV_SOV": { # 32 S-5M x2
        "CommandPoints": 50,
    },
    
    "Mi_8TV_Gunship_SOV": { # 4x Molniya, 2x S-24
        "CommandPoints": 110,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
        "WeaponDescriptor": {
            "Salves": {
                "remove": ["RocketAir_B8_80mm_x20"],
                "AA_R60M_Vympel": 4,
            },
            "turrets": {
                2: {
                    "MountedWeapons": {
                        "AA_R60M_Vympel": {
                            "HandheldEquipmentKey": "'MeshAlternative_1'",
                            "SalvoStockIndex": 0,
                            "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_1'",
                            "WeaponIgnoredPropertyName": "'WeaponIgnored_1'",
                            "WeaponShootDataPropertyName": ['WeaponShootData_0_1'],
                        },
                    },
                    "Tag": "'tourelle1'",
                    "YulBoneOrdinal": 1,
                },
                3: {
                    "MountedWeapons": {
                        "RocketAir_S24_240mm_x2": {
                            "SalvoStockIndex": 1,
                        },
                    },
                },
                "remove": [1],
            },
        },
    },
    
    "Mi_8TV_s80_SOV": {
        "CommandPoints": 95,
        "availability": 4,
        "XPMultiplier": [0.0, 1.0, 0.75, 0.0],
    },

    "Mi_24V_AA_SOV": {
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Mi_24V_RKT_SOV": { # 4x Kokon, 20x S-13
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_27_Gds_Rifle": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Mi_24V_AT_SOV": { # 8x Kokon, 40x S-80
        "CommandPoints": 160,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 1,
            },
            "SOV_79_Gds_Tank": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },
    
    "Mi_24P_SOV": {
        "CommandPoints": 160,
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },
    
    "Mi_24VP_SOV": {
        "CommandPoints": 200,
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_23mm_Bitube_Gsh23L": 28,
                "RocketAir_B8_80mm": 4,
                "AGM_9M114M_KokonM": 1,
            },
        },
    },
    #SOV AIR
    "Su_17M4_SOV": { # 20x S-13, 2x R-60M
        "CommandPoints": 125,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Su_22_AT_SOV": { # 2x Kh-29T, 2x R-60M
        "CommandPoints": 195,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },

    "Su_24MP_EW_SOV": {
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 0.0, 1.0, 0.0],
    },
    
    "Su_24MP_SOV": {
        "CommandPoints": 270,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },

    "Su_24MP_SEAD2_SOV": {
        "CommandPoints": 300,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },
    
    "Su_24M_LGB_SOV": {
        "CommandPoints": 245,
    },

    "Su_24M_LGB2_SOV": {
        "CommandPoints": 260,
    },

    "Su_24M_AT1_SOV": {
        "CommandPoints": 190,
    },

    "Su_24M_AT2_SOV": {
        "CommandPoints": 190,
    },

    "Su_24M_SOV": {
        "CommandPoints": 190,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "Su_24M_thermo_SOV": {
        "CommandPoints": 225,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "MiG_27M_bombe_SOV": { # 4x FAB-500
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "MiG_27M_napalm_SOV": { # 4x ZB-500
        "CommandPoints": 145,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.0],
    },

    "MiG_23MLD_SOV": { # 2x R-24MR, 2x R-73
        "CommandPoints": 175,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": 3,
        "XPMultiplier": [0.0, 1.0, 0.68, 0.0],
    },

    "Su_25T_SOV": { # 16x Vikhr, 2x R-73
        "CommandPoints": 260,
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "AirplaneMovement": {
            "parent_membr": {
                "SpeedInKmph": 750,
            },
        },
        "max_speed": 750,
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },
    
    "MiG_29_AA_SOV": { # 4x R-73, 2x R-27R
        "CommandPoints": 200,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 1,
            },
        },
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },

    "MiG_29_AA2_SOV": { # 2x R-60M, 2x R-27R
        "CommandPoints": 185,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "SOV_35_AirAslt_Brig": {
                "cards": 3,
            },
        },
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },
    
    "Su_27S_SOV": { # 6x R-73, 4x R-27R
        "CommandPoints": 240,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
    },

    "MiG_31_AA1_SOV": { # 4x R-33, 2x R-40TD1
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1650,
            },
        },
        "CommandPoints": 310,
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
        "WeaponDescriptor": {
            "Salves": {
                "AA_R33_Vympel": 2,
            },
        },
    },

    "MiG_31_AA2_SOV": { # 4x R-33, 4x R-60M
        "AirplaneMovement": {
            "parent_membr": {
                "AgilityRadiusGRU": 1650,
            },
        },
        "CommandPoints": 290,
        "availability": 2,
        "XPMultiplier": [0.0, 1.0, 0.0, 0.5],
        "WeaponDescriptor": {
            "Salves": {
                "AA_R33_Vympel": 2,
            },
        },
    },
}
