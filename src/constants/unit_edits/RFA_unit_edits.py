rfa_unit_edits = {
    # RFA LOG
    "Iltis_RFA": {
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
    },

    "Iltis_para_CMD_RFA": {
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
        "SpecialtiesList": {
            "remove_specs": ["'_para'"],
        },
        "DeploymentShift": 0,
    },

    "Faun_Kraka_CMD_RFA": {
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
    },

    "TPZ_Fuchs_CMD_RFA": {
        "CommandPoints": 155,
        "availability": [0, 3, 0, 0],
    },

    "Bo_105_CMD_RFA": {
        "CommandPoints": 115,
        "availability": [0, 3, 0, 0],
    },

    "Alouette_II_CMD_RFA": {
        "CommandPoints": 115,
        "availability": [0, 3, 0, 0],
    },
    
    "DCA_FK20_2_20mm_RFA": {
        "CommandPoints": 20,
        "Factory": "EFactory/Logistic",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [9, 7, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "FOB_RFA",
    },
    
    "DCA_FK20_2_20mm_Zwillinge_RFA": {  # FK-20-2 Zwillinge
        "CommandPoints": 25,
        "Factory": "EFactory/Logistic",
        "Divisions": {
            "default": {
                "Transports": ["Iltis_trans_RFA"],
                "cards": 69,
            },
            "RFA_2_PzGrenadier": {
                "cards": 2,
            },
        },
        "availability": [9, 7, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "FOB_RFA",
    },
    
    # RFA INF
    "Panzergrenadier_CMD_RFA": {  # #CMD Fs-JÄGER FÜH.
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR PZ.GRENADIER LDR.",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Panzergrenadier_CMD_RFA",
                "Unite",
            ],
        },
        "strength": 6,
        "TransportedTexture": "UseInGame_Transport_REGINF",
        # "SortingOrder": 20075,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 16,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                "_leader",
                "_ifv",
                "infantry_equip_heavy",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "Divisions": {
            "default": {
                "cards": 1,
            },
            "US_11ACR": {
                "Transports": ["Marder_1A3_RFA", "Marder_1A3_MILAN_RFA"],
            },
        },
        "availability": [0, 0, 5, 4],
        "max_speed": 20,
        "remove_zone_capture": None,
    },
    
    "Fallschirmjager_CMD_RFA": {  # #CMD Fs-JÄGER FÜH.
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "GameName": {"display": "#LDR FALLSCHIRMJÄGER LDR."},
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_Spec_Attaque",
                "UNITE_Fallschirmjager_CMD_RFA",
                "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        # "SortingOrder": 20085,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 31,
        # "UnitDefenseValue": 31,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                "_leader",
                "_choc",
                "infantry_equip_light",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "remove_zone_capture": None,
    },
    
    "Jager_CMD_RFA": {  # #CMD JÄGER FÜH.
        "CommandPoints": 35,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR JÄGER LDR."
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Jager_CMD_RFA",
                "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        # "SortingOrder": 20085,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 31,
        # "UnitDefenseValue": 31,
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                "_leader",
                "infantry_equip_light",
            ],
        },
         "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "remove_zone_capture": None,
    },
    
    "Engineers_CMD_RFA": {  # #CMD PIONIER FÜH.
        "CommandPoints": 40,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR PIONIER LDR."
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
                "UNITE_Engineers_CMD_RFA",
                "Unite",
            ],
        },
        "TransportedTexture": "UseInGame_Transport_assault",
        # "SortingOrder": 20085,
        # "UnitAttackValue": 1,
        # "UnitDefenseValue": 31,
        # "UnitDefenseValue": 31,
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "engineer",
        "SpecialtiesList": {
            "overwrite_all": [
                "_leader",
                "_choc",
                "infantry_equip_medium",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "remove_zone_capture": None,
    },

    "Gebirgsjager_CMD_RFA": {  # #LDR GEBIRGSJÄGER FÜH.
        "CommandPoints": 60,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#LDR GEBIRGSJÄGER LDR."
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "UNITE_Gebirgsjager_CMD_RFA",
                "Unite",
            ],
        },
        "strength": 8,
        "TransportedTexture": "UseInGame_Transport_REGINF",
        "IdentifiedTextures": ["Texture_RTS_H_Infantry", "Texture_Infantry"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                "_leader",
                "_mountaineer",
                "infantry_equip_heavy",
            ],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_G3KA4": 8,
                },
            },
        },
        "MenuIconTexture": "Texture_RTS_H_Infantry",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Infantry",
        "availability": [0, 0, 4, 3],
        "max_speed": 20,
        "remove_zone_capture": None,
    },
    
    "HeimatschutzJager_RFA": {  # HEIMAT-JAGER
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "HEIMATJÄGER"
        },
        "CommandPoints": 35,
        "Divisions": {
            "default": {
                "cards": 1,  # or 2
            },
            "RFA_TerrKdo_Sud": {
                "cards": 2,
            },
        },
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_inf__MG3_7_62mm": False,
                },
                "quantity": {
                    "FM_G3KA4": 8,
                    "MMG_inf__MG3_7_62mm": 2,
                },
            },
        },
    },
    
    "Engineers_RFA": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_G3KA4": 8,
                    "MMG_inf__MG3_7_62mm": 2,
                },
            },
            "Salves": {
                "Grenade_Satchel_Charge": 6,
            },
        },
    },

    "Fallschirm_Engineers_RFA": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_G3KA4": 8,
                    "MMG_inf__MG3_7_62mm": 2,
                },
            },
            "Salves": {
                "Grenade_Satchel_Charge": 6,
            },
        },
    },

    "Engineers_Geb_RFA_RFA": {  # GEBIRGSPIONERE
        "CommandPoints": 50,
        "GameName": {
            "display": "GEBIRGSPIONERE"
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [8, 6, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "remove": [(1, "MMG_PKM_7_62mm")],
                "insert_edits": {
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                },
                "quantity": {
                    "FM_G3KA4": 10,
                },
                "replace": [
                    ("FM_G3KA4", "PM_uzi", "FM_G3KA4", "PM_uzi"),
                ],
            },
        },
    },
    
    "Engineers_Reserve_RFA": {
        "CommandPoints": 25,
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "armor": "Infantry_armor_reference",
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "Grenade_Satchel_Charge": 4,
            },
        },
    },
    
    "Engineers_Flam_RFA": {
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_Handflammpatrone": 6,
            },
        },
    },
    
    "Engineers_AT_RFA": {  # PIONIER (CarlG)
        "CommandPoints": 50,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "PIONIER [CG]"
        },
        "availability": [0, 6, 4, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_inf__MG3_7_62mm": False,
                },
                "quantity": {
                    "FM_G3KA4": 8,
                    "MMG_inf__MG3_7_62mm": 2,
                },
            },
        },
    },
    
    "Feldgendarmerie_RFA": {
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "availability": [0, 12, 9, 0],
        "max_speed": 26,
        "strength": 5,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "PM_MP_5A3": 5,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'"],
        },
    },
    
    "Security_RFA": {
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_inf__MG3_7_62mm": False,
                },
                "quantity": {
                    "FM_G3KA4": 9,
                    "MMG_inf__MG3_7_62mm": 2,
                },
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Reserve_Polizei_RFA": {
        "CommandPoints": 25,
        "armor": "Infantry_armor_reference",
        "availability": [12, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Hochgebirgjager_RFA": {  # HOCHGEBIRGSJÄGER
        "CommandPoints": 65,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [0, 0, 4, 3],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "Grenade_Satchel_Charge": 6,
            },
        },
    },

    "Fallschirm_RFA": {  # Fs-JÄGER
        "CommandPoints": 45,
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "FALLSCHIRMJÄGER"
        },
        "max_speed": 20,
        "availability": [0, 6, 4, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_inf__MG3_7_62mm": False,
                },
                "quantity": {
                    "FM_G3KA4": 6,
                    "MMG_inf__MG3_7_62mm": 2,
                },
            },
        },
        "UpgradeFromUnit": "Fallschirmjager_CMD_RFA",
    },

    "Fallschirm_Reserve_RFA": {  # JÄGER (PzF)
        "CommandPoints": 35,
        "GameName": {
            "display": "FALLSCHIRM.-RESERVISTEN"
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [8, 0, 0, 0],
        "capacities": {
            "add_capacities": ["reserviste", "Choc", "Choc_feedback"],
        },
        "SpecialtiesList": {
            "add_specs": ["'_reservist'", "'_choc'", "'infantry_equip_medium'"],
        },
    },
    
    "Gebirgsjager_RFA": {  # GEBIRGSJÄGER
        "CommandPoints": 40,
        "GameName": {
            "display": "GEBIRGSJÄGER"
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [10, 7, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Gebirgsjager_PzF3_RFA": {  # GEBIRGSJÄGER [PzF3]
        "CommandPoints": 50,
        "GameName": {
            "display": "GEBIRGSJÄGER [PzF3]"
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "availability": [10, 7, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "remove": [(2, "Sniper_G3A3ZF")],
                "insert_edits": {
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                    3: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
                "quantity": {
                    "FM_G3KA4": 9,
                },
            },
        },
    },

    "Gebirgsjager_Hvy_RFA": {  # GEBIRGSJÄGER
        "CommandPoints": 65,
        "GameName": {
            "display": "LUFT.-GEBIRGSJÄGER"
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [6, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Jager_RFA": {  # JÄGER (PzF44)
        "CommandPoints": 30,
        "GameName": {
            "display": "JÄGER [PzF44]"
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [10, 7, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Jager_noAT_RFA": { # JÄGER (G3A3ZF)
        "CommandPoints": 30,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [10, 7, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Jager_Carl_RFA": {  # JÄGER (Carl Gustav)
        "CommandPoints": 40,
        "GameName": {
            "display": "JÄGER [CarlG]"
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [10, 7, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "animate": {
                    "MMG_inf__MG3_7_62mm": False,
                },
                "quantity": {
                    "FM_G3KA4": 7,
                    "MMG_inf__MG3_7_62mm": 2,
                },
            },
        },
    },
    
    "PzGrenadier_RFA": {  # PZ.GRENADIER (CarlG)
        "armor": "Infantry_armor_reference",
        "CommandPoints": 25,
        "GameName": {
            "display": "PZ.GRENADIER [CG]"
        },
        "max_speed": 26,
        "availability": [12, 9, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Panzergrenadier_APC_RFA": { # PZ.GRENADIER (M113)
        "CommandPoints": 35,
        "GameName": {
            "display": "PZ.GRENADIER [M113]"
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "availability": [10, 7, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    (
                        "RocketInf_PzF_44", "RocketInf_PzF_3",
                    ),
                ],
            },
            "Salves": {
                "RocketInf_PzF_3": 4,
            },
        },
    },

    "Panzergrenadier_PzF3_RFA": { # PZ.GRENADIER [PzF3]
        "CommandPoints": 30,
        "GameName": {
            "display": "PZ.GRENADIER [PzF3]"
        },
        "armor": "Infantry_armor_reference",
        "strength": 6,
        "max_speed": 20,
        "availability": [12, 9, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "quantity": {
                    "FM_G3KA4": 5,
                },
            },
            "Salves": {
                "RocketInf_PzF_3": 4,
            },
        },
    },
    
    "Panzergrenadier_IFV_RFA": { # PZ.GRENADIER (G3A3ZF)
        "CommandPoints": 25,
        "GameName": {
            "display": "PZ.GRENADIER"
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [12, 9, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "ATteam_RCL_M40A1_RFA": {
        "CommandPoints": 35,
        "strength": 5,
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
        "max_speed": 9,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_veryheavy'"],
        },
        "availability": [10, 7, 0, 0],
    },
    
    "ATteam_Milan_1_RFA": {
        "CommandPoints": 25,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [10, 7, 5, 0],
    },
    
    "ATteam_Milan_2_RFA": {
        "CommandPoints": 40,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [6, 4, 0, 0],
    },
    
    "ATteam_Milan_2_para_RFA": {
        "CommandPoints": 40,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [6, 4, 0, 0],
    },
    
    "HMGteam_MG3_RFA": {  # MG-3 7,62mm
        "CommandPoints": "HMGteam_M60_US",
        "GameName": {
            "display": "MG3 7.62mm",
        },
        "strength": "HMGteam_M60_US",
        "max_speed": "HMGteam_M60_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_US",
        },
    },
    
    "HMGteam_MG3_FJ_RFA": {  # Fs-MG-3 7,62mm
        "CommandPoints": "HMGteam_M60_AB_US",
        "GameName": {
            "display": "FJ MG3 7.62mm",
        },
        "strength": "HMGteam_M60_AB_US",
        "max_speed": "HMGteam_M60_AB_US",
        "SpecialtiesList": {
            "add_specs": "HMGteam_M60_AB_US",
        },
    },
    
    "Faun_Kraka_M40A1_RFA": {
        "CommandPoints": 30,
        "availability": [0, 12, 9, 0],
    },    

    # trsp
    "Unimog_trans_RFA": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "Iltis_trans_RFA": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "MAN_Kat_6x6_trans_RFA": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "Faun_kraka_RFA": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "DaimlerBenz_Typ1017_trans_RFA": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "VW_T2b_MP_RFA": { # MP
        "CommandPoints": 20,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    # RFA ARTY
    "M577_RFA": {
        "CommandPoints": 60,
        "GameName": {
            "display": "#LDR M577GA2 TACFIRE",
            "token": "M577GA2LDR",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "GroundUnits",
                "UNITE_M577_RFA",
                "Unite",
                "Vehicule",
            ],
        },
        "Factory": "EFactory/Art",
        "IdentifiedTextures": ["Texture_RTS_H_appui", "Texture_appui"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "_leader",
        "SpecialtiesList": {
            "overwrite_all": [],
        },
        "MenuIconTexture": "Texture_RTS_H_appui",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Transport",
        "Divisions": {
            "default": {
                "cards": 1,
            },
        },
        "availability": [0, 3, 0, 0],
        "remove_zone_capture": None,
    },
    
    "HS30_Panzermorser_120mm_RFA": {
        "CommandPoints": 60,
        "availability": [4, 3, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_MG3_7_62mm": 48,
            },
        },
    },
    
    "M113_PzMorser_RFA": {
        "GameName": {
            "display": "PzMrs M113A1G"
        },
        "CommandPoints": 60,
        "availability": [4, 3, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "MMG_MG3_7_62mm": 48,
            },
        },
    },
    
    "Mortier_Tampella_120mm_RFA": {
        "CommandPoints": 45,
        "availability": [5, 4, 3, 0],
        "GameName": {
            "display": "MRS. 120mm TAMPELLA"
        },
    },

    "Mortier_Tampella_120mm_para_RFA": {
        "CommandPoints": 45,
        "availability": [0, 5, 4, 3],
        "GameName": {
            "display": "Fs-MRS. 120mm TAMPELLA"
        },
    },
    
    "Howz_M101_105mm_RFA": {
        "CommandPoints": 55,
        "availability": [4, 3, 0, 0],
    },

    "Howz_M56_Pack_FJ_RFA": {
        "CommandPoints": 55,
        "availability": [0, 4, 3, 0],
    },

    "Howz_M56_Pack_Geb_RFA": {
        "CommandPoints": 55,
        "availability": [4, 3, 0, 0],
    },
    
    "FH70_155mm_RFA": {
        "CommandPoints": 110,
        "availability": [3, 2, 0, 0],
    },
    
    "M109G_RFA": {
        "CommandPoints": 170,
        "availability": [3, 2, 0, 0],
    },

    "M109A3G_HOWZ_RFA": {
        "CommandPoints": 190,
        "availability": [3, 2, 0, 0],
    },

    "M110A2_Howz_RFA": {
        "CommandPoints": 220,
        "availability": [2, 0, 1, 0]
    },

    "Lars_2_RFA": {
        "CommandPoints": 180,
        "availability": [3, 2, 0, 0],
    },

    "M270_MLRS_RFA": {
        "CommandPoints": 300,
        "WeaponDescriptor": {
            "turrets": {
                0: {
                    "AngleRotationMaxPitch": 1.0,
                },
            },
        },
        "availability": [0, 1, 0, 0],
    },
    
    # RFA TANK
    "M48A2GA2_CMD_RFA": {
        "CommandPoints": 75,
        "GameName": {
            "display": "#LDR PZ.BEF. M48A2GA2",
            "token": "VLNKYMRDNH",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_M48A2GA2_CMD_RFA",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_reservist',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 6, 0],
        "remove_zone_capture": None,
    },

    "Leopard_1A1_CMD_RFA": {
        "CommandPoints": 80,
        "GameName": {
            "display": "#LDR PZ.BEF. LEOPARD 1A1A1",
            "token": "XCPWTQSWXH",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_Leopard_1A1_CMD_RFA",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 6, 0],
        "remove_zone_capture": None,
    },

    "Leopard_1A4_CMD_RFA": {
        "CommandPoints": 85,
        "GameName": {
            "display": "#LDR PZ.BEF. LEOPARD 1A4",
            "token": "ELPLTKBAYX",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_Leopard_1A4_CMD_RFA",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },

    "Leopard_1A5_CMD_RFA": {
        "CommandPoints": 110,
        "GameName": {
            "display": "#LDR PZ.BEF. LEOPARD 1A5",
            "token": "GLAVEMFHKO",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_Leopard_1A5_CMD_RFA",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 4, 0],
        "remove_zone_capture": None,
    },

    "Leopard_2A3_CMD_RFA": {
        "CommandPoints": 205,
        "GameName": {
            "display": "#LDR PZ.BEF. LEOPARD 2A3",
            "token": "IKKNOBNJOQ",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_Leopard_2A3_CMD_RFA",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 3, 0],
        "remove_zone_capture": None,
    },

    "Leopard_2A1_CMD_RFA": {
        "CommandPoints": 180,
        "GameName": {
            "display": "#LDR PZ.BEF. LEOPARD 2A1",
            "token": "LWSMADUUPS",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_Leopard_2A1_CMD_RFA",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 3, 0],
        "remove_zone_capture": None,
    },

        "Leopard_2A4_CMD_RFA": {
        "CommandPoints": 270,
        "GameName": {
            "display": "#LDR PZ.BEF. LEOPARD 2A4(C)",
            "token": "PBLIFBOOCD",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "GroundUnits",
                "UNITE_Leopard_2A4_CMD_RFA",
                "Unite"
            ],
        },
        "IdentifiedTextures": ["Texture_RTS_H_Armor", "Texture_Armor"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "UnitRole": "armor",
        "SpecialtiesList": {
            "overwrite_all": [
                '_leader',
                '_smoke_launcher',
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_Armor",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Armor",
        "availability": [0, 0, 0, 2],
        "remove_zone_capture": None,
    },
    
    "Iltis_MILAN_RFA": {
        "CommandPoints": 30,
        "availability": [12, 9, 0, 0],
    },
    
    "Iltis_MILAN_2_RFA": {
        "CommandPoints": 45,
        "availability": [8, 6, 0, 0],
    },

    "Faun_Kraka_MILAN_RFA": {
        "CommandPoints": 45,
        "availability": [8, 6, 0, 0],
    },

    "Faun_Kraka_TOW_RFA": {
        "CommandPoints": 55,
        "availability": [8, 6, 0, 0],
    },

    "Wiesel_20mm_RFA": {
        "CommandPoints": 25,
        "availability": [0, 12, 9, 0],
    },

    "Wiesel_TOW_RFA": {
        "CommandPoints": 60,
        "availability": [0, 6, 4, 0],
    },

    "Jaguar_1_RFA": {
        "CommandPoints": 75,
        "availability": [6, 4, 0, 0],
    },

    "Jaguar_2_RFA": {
        "CommandPoints": 85,
        "availability": [6, 4, 0, 0],
    },
    
    "KanJagdPanzer_RFA": {
        "CommandPoints": 35,
        "availability": [14, 0, 0, 0],
        "armor": {
            "front": (4, None),
        },
    },
    
    "M48A2C_RFA": {
        "CommandPoints": 55,
        "availability": [12, 0, 0, 0],
    },
    
    "M48A2GA2_RFA": {
        "CommandPoints": 65,
        "availability": [10, 0, 0, 0],
    },

    "M48A2GA2_nonHeimat_RFA": {
        "CommandPoints": 70,
        "availability": [10, 7, 0, 0],
    },
    
    "Leopard_1A1_RFA": {
        "CommandPoints": 70,
        "availability": [10, 7, 0, 0],
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "MMG_AANF1_7_62mm": 44,
        #     },
        # },
    },

    "Leopard_1A1A2_RFA": {
        "CommandPoints": 70,
        "availability": [10, 7, 0, 0],
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "MMG_AANF1_7_62mm": 44,
        #     },
        # },
    },

    "Leopard_1A4_RFA": {
        "CommandPoints": 75,
        "availability": [10, 7, 0, 0],
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "MMG_AANF1_7_62mm": 44,
        #     },
        # },
    },
    
    "Leopard_1A5_RFA": {
        "CommandPoints": 95,
        "availability": [0, 8, 6, 0],
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "MMG_AANF1_7_62mm": 44,
        #     },
        # },
    },

    "Leopard_2A1_RFA": { # Could be swapped to a Recon Unit
        "CommandPoints": 165,
        "availability": [6, 4, 0, 0],
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "MMG_AANF1_7_62mm": 44,
        #     },
        # },
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
    },

    "Leopard_2A3_RFA": {
        "CommandPoints": 185,
        "availability": [0, 4, 3, 0],
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "MMG_AANF1_7_62mm": 44,
        #     },
        # },
    },

    "Leopard_2A4_RFA": {
        "CommandPoints": 235,
        "availability": [0, 4, 3, 0],
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "MMG_AANF1_7_62mm": 44,
        #     },
        # },
    },
    
    # trsp
    "TPZ_Fuchs_1_RFA": {
        "CommandPoints": 15,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_MG3_7_62mm": 48,
            },
        },
    },
    
    "TPZ_Fuchs_MILAN_RFA": {
        "CommandPoints": 30,
        "WeaponDescriptor": {
            "Salves": {
                "MMG_MG3_7_62mm": 48,
            },
        },
    },
    
    "M113A1G_RFA": {
        "CommandPoints": 15,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    "M113A1G_MILAN_RFA": {
        "CommandPoints": 25,
        "WeaponDescriptor": {
            "Salves": {
                "ATGM_MILAN": 5,
            },
        },
    },
    
    "Marder_1A1_RFA": {
        "CommandPoints": 45,
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_20mm_MK_20_Rh_202": 48,
            },
        },
    },
    
    "Marder_1A1_MILAN_RFA": {
        "CommandPoints": 50,
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_20mm_MK_20_Rh_202": 48,
            },
        },
    },

    "Marder_1A2_RFA": {
        "CommandPoints": 45,
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_20mm_MK_20_Rh_202": 48,
            },
        },
    },
    
    "Marder_1A2_MILAN_RFA": {
        "CommandPoints": 50,
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_20mm_MK_20_Rh_202": 48,
            },
        },
    },

    "Marder_1A3_RFA": {
        "CommandPoints": 50,
        "WeaponDescriptor": {
            "Salves": {
                "AutoCanon_AP_20mm_MK_20_Rh_202": 48,
            },
        },
    },
    
    "Marder_1A3_MILAN_RFA": {
        "CommandPoints": 60,
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    (
                        "ATGM_MILAN_IFV", "ATGM_MILAN_2_IFV",
                        "ATGM_MILAN_2_IFV", "ATGM_MILAN_2_IFV"
                    ),
                ],
            },
            "Salves": {
                "AutoCanon_AP_20mm_MK_20_Rh_202": 48,
                "ATGM_MILAN_2_IFV": 6,
            },
        },
    },
    
    # RFA REC
    "Sonderwagen_4_RFA": {
        "CommandPoints": 25,
    },
    
    "Iltis_reco_RFA": {
        "CommandPoints": 25,
    },

    "Faun_Kraka_MG3_RFA": {
        "CommandPoints": 20,
    },

    "M113A1G_reco_RFA": {  # M113A1G AUFKL.
        "GameName": {
            "display": "#RECO1 M113A1G AufKl"
        },
        "CommandPoints": 20,
    },

    "TPZ_Fuchs_1_reco_RFA": {
        "CommandPoints": 25,
    },

    "Scout_RFA": {
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [8, 6, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "BGS_RFA": {
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#RECO2 BGS STREIFE"
        },
        "CommandPoints": 15,
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [10, 0, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },
    
    "BGS_hvy_RFA": {
        "CommandPoints": 35,
        "availability": [8, 0, 0, 0],
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Fernspaher_RFA": {
        "CommandPoints": 70,
        "armor": "Infantry_armor_reference",
        "availability": [0, 0, 4, 3],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "RocketInf_M72A4_LAW_66mm": 6,
            },
        },
    },
    
    "Fallschirm_B1_RFA": { # Fallschirmjäger B1 (Satchel, Panzerfaust 3T)
        "CommandPoints": 65,
        "availability": [0, 0, 4, 3],
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    (
                        "RocketInf_PzF_3", "RocketInf_PzF_3T",
                    ),
                ],
            },
            "Salves": {
                "RocketInf_PzF_3T": 6,
            },
        },
    },
    
    "Fallschirmjager_Scout_RFA": {  # Fs-Jager aufk
        "armor": "Infantry_armor_reference",
        "CommandPoints": 25,
        "availability": [0, 7, 5, 0],
        "GameName": {
            "display": "#RECO2 FJ AUFKLÄRER"
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
    },

    "Gebirgsjager_JagdKdo_RFA": {  # Geb JagKdo
        "armor": "Infantry_armor_reference",
        "CommandPoints": 55,
        "availability": [0, 4, 3, 0],
        "GameName": {
            "display": "#RECO2 GEB. JAGDKOMMANDO"
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "remove": [(2, "Sniper_G3A3ZF")],
                "insert_edits": {
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 2,
                        },
                        "AmmoBoxIndex": 1,
                        "HandheldEquipmentKey": "'WeaponAlternative_2'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_2'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_2'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_2"],
                    },
                    3: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
                "quantity": {
                    "FM_G3KA4": 10,
                },
            },
        },
    },
    
    "Gebirgsjager_Scout_RFA": {  # GEB AUFKL.
        "armor": "Infantry_armor_reference",
        "CommandPoints": 55,
        "availability": [0, 7, 5, 0],
        "GameName": {
            "display": "#RECO2 GEB. AUFKLÄRER"
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Jager_Aufk_RFA": {  # JAGER AUFKL.
        "armor": "Infantry_armor_reference",
        "CommandPoints": 40,
        "availability": [6, 4, 0, 0],
        "GameName": {
            "display": "#RECO2 JÄGER AUFKLÄRER"
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },

    "Sniper_Fern_RFA": {  # #RECO2 FERN. SCHARFSCHÜTZE.
        "armor": "Infantry_armor_reference",
        "CommandPoints": 35,
        "availability": [0, 0, 4, 3],
        "strength": 3,
        "GameName": {
            "display": "#RECO2 FERN. SCHARFSCHÜTZE"
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "insert": [(2, "RocketInf_M72A4_LAW_66mm")],
                "insert_edits": {
                    2: {
                        "turret_edits": {
                            "YulBoneOrdinal": 3,
                        },
                        "AmmoBoxIndex": 2,
                        "HandheldEquipmentKey": "'WeaponAlternative_3'",
                        "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_3'",
                        "WeaponIgnoredPropertyName": "'WeaponIgnored_3'",
                        "WeaponShootDataPropertyName": ["WeaponShootData_0_3"],
                    },
                },
                "quantity": {
                    "PM_MP_5SD": 2,
                },
            },
        },
    },

    "Sniper_Geb_RFA": {  # GEB. SCHARFSCHÜTZE
        "armor": "Infantry_armor_reference",
        "CommandPoints": 30,
        "availability": [0, 4, 3, 0],
        "GameName": {
            "display": "#RECO2 GEB. SCHARFSCHÜTZE"
        },
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },

    "SEK_RFA": {  # #RECO2 SEK
        "armor": "Infantry_armor_reference",
        "CommandPoints": 25,
        "availability": [0, 0, 8, 6],
        "GameName": {
            "display": "#RECO2 SEK"
        },
        "SpecialtiesList": {
            "add_specs": ["'_choc'", "'infantry_equip_light'", "'_swift'"],
        },
        "capacities": {
            "add_capacities": ["Choc", "Choc_feedback"],
        },
    },
    
    "M113_GreenArcher_RFA": {
        "CommandPoints": 30,
        # "optics": {
        #     "OpticalStrength": 233.475
        # },
        "availability": [8, 0, 0, 0],
    },

    "TPZ_Fuchs_RASIT_RFA": {
        "CommandPoints": 30,
        "availability": [8, 0, 0, 0],
    },

    "Luchs_A1_RFA": {
        "CommandPoints": 50,
        "availability": [0, 6, 4, 0],
    },

    "Leopard_1A5_reco_RFA": {
        "CommandPoints": 115,
        "availability": [0, 6, 4, 0],
    },
    
    "Bo_105_reco_RFA": {
        "CommandPoints": 30,
        "availability": [0, 6, 0, 0],
    },

    "Alouette_II_reco_RFA": {
        "CommandPoints": 30,
        "availability": [0, 6, 0, 0],
    },

    "CL_289_RFA": {
        "CommandPoints": 60,
        "availability": [0, 3, 0, 0],
    },
    
    # RFA AA
    "MANPAD_Redeye_RFA": {  # Fliegerfaust
        "CommandPoints": 20,
        "armor": "Infantry_armor_reference",
        "availability": [12, 9, 0, 0],
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("PM_uzi", "PM_uzi_noreflex")],
            },
        },
    },
    
    "Bofors_40mm_RFA": {
        "CommandPoints": 30,
        "availability": [10, 7, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "WeaponDescriptor": {
            "Salves": {
                "DCA_1_canon_Bofors_40mm": 18,
            },
        },
    },

    "DCA_FK20_2_20mm_FJ_RFA": {
        "CommandPoints": 20,
        "availability": [0, 9, 7, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },

    "DCA_FK20_2_20mm_FJ_RFA": {
        "CommandPoints": 25,
        "availability": [9, 7, 0, 0],
        "max_speed": 6,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
    },

    "Faun_Kraka_20mm_RFA": {
        "CommandPoints": 35,
        "availability": [9, 7, 0, 0],
    },

    "Unimog_S_404_FK20_RFA": {
        "CommandPoints": 35,
        "availability": [9, 7, 0, 0],
    },
    
    "Gepard_1A2_RFA": { # Gepard 1A1
        "CommandPoints": 90,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 220,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "availability": [6, 4, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },

    "Marder_Roland_2_RFA": { # Roland 2
        "CommandPoints": 120,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 220,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "availability": [4, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'good_airoptics'"],
        },
    },
    
    "Marder_Roland_RFA": { # Roland 3
        "CommandPoints": 150,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 300,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "availability": [0, 3, 2, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "FR_5e_Blindee": {
                "cards": 2,
            },
        },
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
    },
    
    "DCA_I_Hawk_RFA": {
        "CommandPoints": 90,
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 300,
            },
            "TimeBetweenEachIdentifyRoll": 1.0,
        },
        "availability": [4, 3, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'verygood_airoptics'"],
        },
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "RFA_TerrKdo_Sud": {
                "Transports": ["Unimog_S_404_RFA"],
            },
        },
    },
    
    # RFA HELICOPTER

    "Bo_105_PAH_1_RFA": {
        "CommandPoints": 80,
        "availability": [0, 6, 0, 0],
    },

    "Bo_105_PAH_1A1_RFA": {
        "CommandPoints": 100,
        "availability": [0, 0, 4, 3],
    },

    # Helo Transports

    "UH1D_RFA": {
        "CommandPoints": 45,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    "CH53G_trans_RFA": {
        "CommandPoints": 60,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },

    # RFA AIR
    "Alpha_Jet_A_he_RFA": {
        "CommandPoints": 75,
        "availability": [0, 4, 0, 0],
    },
    
    "Alpha_Jet_A_clu_RFA": {
        "CommandPoints": 75,
        "availability": [0, 4, 0, 0],
    },
    
    "Alpha_Jet_A_nplm_RFA": {
        "CommandPoints": 75,
        "availability": [0, 6, 0, 0],
    },
    
    "Alpha_Jet_A_rkt_RFA": {
        "CommandPoints": 70,
        "availability": [0, 5, 0, 0],
    },

    "Alpha_Jet_A_KWS_RFA": { # 30% ECM, 2 Mavericks
        "CommandPoints": 100,
        "availability": [0, 3, 2, 0],
    },

    "F104G_Starfighter_RFA": { # F-104G [AA]
        "CommandPoints": 95,
        "availability": [0, 4, 3, 0],
    },
    
    "F104G_Starfighter_HE_RFA": { # F-104G [HE]
        "CommandPoints": 145,
        "availability": [0, 4, 0, 0],
    },
    
    "F104G_Starfighter_AT_RFA": { # F-104G [AT]
        "CommandPoints": 95,
        "availability": [0, 4, 0, 0],
    },
    
    "F4F_Phantom_II_AA2_RFA": { # 2x 2x AIM-9L(Improved)
        "CommandPoints": 165,
        "availability": [0, 3, 2, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
    },

    "F4F_Phantom_II_AA_RFA": { # 2x 2x AIM-9L
        "CommandPoints": 155,
        "availability": [0, 3, 2, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
    },

    "F4F_Phantom_II_AT_RFA": { # 4x Maverick
        "CommandPoints": 220,
        "availability": [0, 2, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_AGM65B_Maverick": 2,
            },
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
    },

    "F4F_Phantom_II_HE1_RFA": { # 12x Mk82
        "CommandPoints": 205,
        "availability": [0, 2, 0, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
    },

    "F4F_Phantom_II_HE2_RFA": { # 5x Mk83
        "CommandPoints": 210,
        "availability": [0, 2, 0, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
    },

    "F4F_Phantom_II_LGB_RFA": { # 2x GBU-16
        "CommandPoints": 190,
        "GameName": {
            "display": "F-4F [PGB]",
        },
        "availability": [0, 1, 0, 0],
        "WeaponDescriptor": {
            "Salves": {
                "Bomb_GBU_12_salvolength2": 1,
            },
            "equipmentchanges": {
                "replace": [("Bomb_GBU_12", "Bomb_GBU_12_salvolength2")],
            },
        },
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
    },

    "F4F_Phantom_II_RKT1_RFA": { # 76x Hydra 70mm Rockets (RKT2)
        "CommandPoints": 125,
        "availability": [0, 3, 2, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
    },

    "F4F_Phantom_II_RKT2_RFA": { # 2x 8x Zuni 127mm Rockets (RKT)
        "CommandPoints": 125,
        "availability": [0, 3, 2, 0],
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/HighAltitude": 375,
            },
        },
    },

    "HFB_320_ECM_RFA": { # EW
        "CommandPoints": 180,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 12500.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
            },
        },
        "availability": [0, 0, 2, 0],
    },
    
    "G91_R3_Gina_HE_RFA": {
        "CommandPoints": 65,
        "availability": [0, 5, 0, 0],
    },

    "G91_R3_Gina_NPL_RFA": {
        "CommandPoints": 65,
        "availability": [0, 6, 0, 0],
    },
    
    "G91_R3_Gina_RKT_RFA": {
        "CommandPoints": 70,
        "availability": [0, 5, 0, 0],
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [("RocketAir_SNEB_68mm_salvolength18", "RocketAir_SNEB_68mm_avion_salvolength18")],
            },
            "Salves": {
                "RocketAir_SNEB_68mm_avion_salvolength18": (2, True),
            },
        },
    },
    
    "Tornado_IDS_AT1_RFA": { # 4x AGM-65B, 2x AIM-9L
        "CommandPoints": 245,
        "availability": [0, 2, 0, 1],
        "WeaponDescriptor": {
            "Salves": {
                "AGM_AGM65B_Maverick": 2,
            },
        },
    },

    "Tornado_IDS_HE1_RFA": { # 3x Mk 83, 2x AIM-9L
        "CommandPoints": 220,
        "availability": [0, 2, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
    },

    "Tornado_IDS_SEAD_RFA": { # AGM-88 5950m
        "CommandPoints": 250,
        "optics": {
            "VisionRangesGRU": {
                "EVisionRange/Standard": 10000.0,
            },
            "OpticalStrengths": {
                "EOpticalStrength/AntiRadar": 5000.0,
                "EOpticalStrength/HighAltitude": 375,
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
        "availability": [0, 2, 0, 1],
    },

    "Tornado_IDS_MW1_RFA": { # MW-1 KB44 (Anti Airfield HE Cluster Munitions), 2x AIM-9L
        "CommandPoints": 240,
        "availability": [0, 2, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'terrain_radar'"],
        },
    },

    "Tornado_IDS_RFA": { # 4x GBU-24 -> 4x GBU-10
        "CommandPoints": 270,
        "GameName": {
            "display": "TORNADO IDS [PGB]",
        },
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "Bomb_GBU_24_salvolength2": 1,
        #     },
        #     "equipmentchanges": {
        #         "replace": [("Bomb_GBU_24_salvolength2", "Bomb_GBU_10_salvolength4")],
        #     },
        # },
    }
}
