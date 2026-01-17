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
            "display": "#LDR PANZERGRENADIER LDR.",
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
        "is_infantry": True,
        "is_ground_vehicle": False,
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
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                "_leader",
                "_choc",
                "infantry_equip_light",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
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
        "IdentifiedTextures": ["Texture_RTS_H_assault", "Texture_assault"],
        "UnidentifiedTextures": ["Texture_RTS_H_infantry_nonIdentifie", "Texture_infantry_nonIdentifie"],
        "UnitRole": "infantry",
        "SpecialtiesList": {
            "overwrite_all": [
                "_leader",
                "infantry_equip_light",
            ],
        },
        "MenuIconTexture": "Texture_RTS_H_assault",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Engineer",
        "availability": [0, 0, 7, 5],
        "max_speed": 26,
        "is_infantry": True,
        "is_ground_vehicle": False,
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
        "is_infantry": True,
        "is_ground_vehicle": False,
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
    
    "Fallschirm_RFA": {  # Fs-JÄGER
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "FALLSCHIRMJÄGER"
        },
        "UpgradeFromUnit": "Fallschirmjager_CMD_RFA",
    },
    
    "Jager_RFA": {  # JÄGER (PzF)
        "CommandPoints": 30,
        "GameName": {
            "display": "JÄGER [PzF]"
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
    
    "PzGrenadier_RFA": {  # PZ.GRENADIER (CarlG)
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "PANZERGRENADIER [CG]"
        },
        "max_speed": 26,
        "availability": [12, 9, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    
    "Panzergrenadier_APC_RFA": { # PZ.GRENADIER (M113)
        "CommandPoints": 30,
        "GameName": {
            "display": "PANZERGRENADIER [M113]"
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 26,
        "availability": [10, 7, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
        "WeaponDescriptor": {
            "equipmentchanges": {
                "replace": [
                    (
                        "RocketInf_PzF_44", "RocketInf_PzF_3",
                    ),
                ],
            },
        },
    },
    
    "Panzergrenadier_IFV_RFA": { # PZ.GRENADIER (G3A3ZF)
        "CommandPoints": 30,
        "GameName": {
            "display": "PANZERGRENADIER"
        },
        "armor": "Infantry_armor_reference",
        "max_speed": 20,
        "availability": [12, 9, 0, 0],
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
        "availability": [9, 7, 0, 0],
    },
    
    "ATteam_Milan_1_RFA": {
        "CommandPoints": 30,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [9, 7, 5, 0],
    },
    
    "ATteam_Milan_2_RFA": {
        "CommandPoints": 45,
        "max_speed": 20,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_heavy'"],
        },
        "availability": [6, 4, 0, 0],
    },
    
    "ATteam_Milan_2_para_RFA": {
        "CommandPoints": 45,
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
            "display": "TAMPELLA 120mm"
        },
    },
    
    "Howz_M101_105mm_RFA": {
        "CommandPoints": 55,
        "availability": [4, 3, 0, 0],
    },
    
    "FH70_155mm_RFA": {
        "CommandPoints": 110,
        "availability": [3, 2, 0, 0],
    },
    
    "M109A3G_HOWZ_RFA": {
        "CommandPoints": 190,
        "availability": [3, 2, 0, 0],
    },
    
    # RFA TANK
    "M48A2GA2_CMD_RFA": {
        "CommandPoints": 75,
        "GameName": {
            "display": "#LDR M48A2GA2 LDR.",
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
    
    "Iltis_MILAN_RFA": {
        "CommandPoints": 30,
        "availability": [12, 9, 0, 0],
    },
    
    "Jaguar_2_RFA": {
        "CommandPoints": 75,
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
    
    "Leopard_1A1_RFA": {
        "CommandPoints": 80,
        "availability": [10, 7, 0, 0],
        # "WeaponDescriptor": {
        #     "Salves": {
        #         "MMG_AANF1_7_62mm": 44,
        #     },
        # },
    },
    
    "Leopard_1A5_RFA": {
        "CommandPoints": 105,
        "availability": [10, 7, 0, 0],
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
    
    "UH1D_RFA": {
        "CommandPoints": 40,
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
        },
    },
    
    # RFA REC
    "Sonderwagen_4_RFA": {
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
        "GameName": {
            "display": "#RECO2 FJ AUFKLÄRER"
        },
    },
    
    "Jager_Aufk_RFA": {  # JAGER AUFKL.
        "armor": "Infantry_armor_reference",
        "GameName": {
            "display": "#RECO2 JÄGER AUFKLÄRER"
        },
    },
    
    "M113A1G_reco_RFA": {  # M113A1G AUFKL.
        "GameName": {
            "display": "#RECO1 M113A1G AufKl"
        },
    },
    
    "M113_GreenArcher_RFA": {
        "CommandPoints": 30,
        # "optics": {
        #     "OpticalStrength": 233.475
        # },
        "availability": [8, 0, 0, 0],
    },
    
    "Bo_105_reco_RFA": {
        "CommandPoints": 30,
        "availability": [0, 4, 0, 0],
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
                "Transports": ["Unimog_S_404_RFA", "MAN_Kat_6x6_trans_RFA"],
            },
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
    
    "G91_R3_Gina_HE_RFA": {
        "CommandPoints": 65,
        "availability": [0, 5, 0, 0],
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
        "WeaponDescriptor": {
            "Salves": {
                "AGM_AGM65B_Maverick": 2,
            },
        },
    }
}
