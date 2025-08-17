rfa_unit_edits = {
    # RFA LOG
    "Iltis_RFA": {
        "CommandPoints": 145,
        "availability": [0, 3, 0, 0],
        "Divisions": {
            "default": {
                "cards": 2,
            },
        },
    },
    "DCA_FK20_2_20mm_Zwillinge_RFA": {  # FK-20-2 Zwillinge
        "CommandPoints": 20,
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
        "max_speed": 4,
        "capacities": {
            "add_capacities": ["Deploy", "Deploy_ok"],
        },
        "UpgradeFromUnit": "FOB_RFA",
    },
    # RFA INF
    "Panzergrenadier_CMD_RFA": {  # #CMD Fs-JÄGER FÜH.
        "CommandPoints": 45,
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
        "WeaponAssignment": [(0, [1]), (1, [0]), (2, [0]), (3, [0]), (4, [0, 3]), (5, [0, 2])],
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
        "CommandPoints": 40,
        "GameName": {"display": "#LDR JÄGER LDR."},
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
    "Panzergrenadier_IFV_RFA": {  # PZ.GRENADIER
        "GameName": {"display": "PANZERGRENADIER"},
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 2,
            },
            "US_11ACR": {
                "cards": 1,
            },
        },
        "availability": [12, 9, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    "HeimatschutzJager_RFA": {  # HEIMAT-JAGER
        "GameName": {"display": "HEIMATJÄGER"},
        "CommandPoints": 30,
        "Divisions": {
            "default": {
                "cards": 1,  # or 2
            },
        },
        "availability": [10, 0, 0, 0],
        "max_speed": 26,
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_medium'"],
        },
    },
    "Engineers_AT_RFA": {  # PIONIER (CarlG)
        "GameName": {"display": "PIONIER [CG]"},
    },
    "Panzergrenadier_APC_RFA": {  # PZ.GRENADIER (M113)
        "GameName": {"display": "PANZERGRENADIER [M113]"},
    },
    "Fallschirm_RFA": {  # Fs-JÄGER
        "GameName": {"display": "FALLSCHIRMJÄGER"},
        "UpgradeFromUnit": "Fallschirmjager_CMD_RFA",
    },
    "Jager_RFA": {  # JÄGER (PzF)
        "GameName": {"display": "JÄGER [PzF]"},
    },
    "PzGrenadier_RFA": {  # PZ.GRENADIER (CarlG)
        "GameName": {"display": "PANZERGRENADIER [CG]"},
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
        "availability": [0, 2, 0, 0],
        "remove_zone_capture": None,
    },
    "M113_PzMorser_RFA": {
        "GameName": {"display": "PzMrs M113A1G"},
        "CommandPoints": 75,
        "availability": [4, 3, 0, 0],
    },
    "Mortier_Tampella_120mm_RFA": {
        "GameName": {"display": "TAMPELLA 120mm"},
    },
    "M109A3G_HOWZ_RFA": {
        "CommandPoints": 190,
        "availability": [3, 2, 0, 0],
    },
    # RFA TANK
    "Jaguar_2_RFA": {
        "CommandPoints": 75,
        "availability": [6, 4, 0, 0],
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
        "SpecialtiesList": {
            "add_specs": ["'refundable_unit'",],
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
    "BGS_RFA": {
        "GameName": {"display": "#RECO2 BGS STREIFE"},
        "CommandPoints": 15,
        "max_speed": 26,
        "availability": [10, 0, 0, 0],
        "SpecialtiesList": {
            "add_specs": ["'infantry_equip_light'", "'_swift'"],
        },
    },
    "Fallschirmjager_Scout_RFA": {  # Fs-Jager aufk
        "GameName": {"display": "#RECO2 FJ AUFKLÄRER"},
    },
    "Jager_Aufk_RFA": {  # JAGER AUFKL.
        "GameName": {"display": "#RECO2 JÄGER AUFKLÄRER"},
    },
    "M113A1G_reco_RFA": {  # M113A1G AUFKL.
        "GameName": {"display": "#RECO1 M113A1G AufKl"},
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
}
