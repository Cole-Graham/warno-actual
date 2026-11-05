"""New unit definitions for Denmark."""

# fmt: off
DK_NEW_UNITS = {
    ("Leopard_1A3_DK", 0): {
        "GUID": "fd182bf0-9af7-435f-8181-b7d448337d95",
        "InfantrySquadModuleGUID": "a692ae40-5225-4470-81ec-112244e1a084",
        "ShowroomGUID": "73ec9301-b606-42ee-a08e-d458b80904eb",
        "CadavreGUID": "994ae32e-0129-43a0-b7e9-4399138dcf9b",
        "UnitId": 50118,
        "NewName": "Otomatic_DK",
        "CommandPoints": 130,  # WA Gepard_1A2_RFA is 95; 76mm outranges it (AA 3000 m) and also fires AP
        "GameName": {
            "display": "OTOMATIC",
            "token": "DKOTOMATIC",
        },
        "TypeUnit": {
            "MotherCountry": "DK",
            # AA tab / AA card, same as vanilla Gepard_1A2_RFA.
            "AcknowUnitTypes": ["CanonAA"],
            "TypeUnitFormation": "Artillerie",
        },
        "Factory": "Factory/DCA",
        "UnitRole": "AA",
        "IdentifiedTextures": ["Texture_RTS_H_AA_veh", "Texture_AA_veh"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "MenuIconTexture": "Texture_RTS_H_AA_veh",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/AA_Veh",
        "TagSet": {
            # Copied from vanilla Gepard_1A2_RFA (another Leopard-1-chassis SPAAG) and
            # renamed. Check this is still the right tag set once the real depiction exists.
            "overwrite_all": [
                "AA_radar",
                "AllUnits",
                "AllowedForMissileRoE",
                "Canon_AA",
                "Canon_AA_Porte",
                "GroundUnits",
                "UNITE_Otomatic_DK",
                "Unite",
            ],
        },
        "depictions": {
            # Own mesh: assets/gameplaymod/3d/units/dk/otomatic_dk/Otomatic_DK.fbx + _MID/_LOW
            # LOD files, registered in new_depictions/DK_new_depictions/Otomatic_DK.py.
            "new_mesh": True,
            # Donor's turret-2 SubDepiction draws the Leopard's coax MG mesh on
            # base_tourelle_02, which the Otomatic model doesn't have.
            "remove": {
                "DepictionVehicles_ndf": {
                    "remove_members": ["SubDepictions"],
                },
                "DepictionVehiclesShowroom_ndf": {
                    "remove_members": ["SubDepictions"],
                },
            },
        },
        "armor": {
            "front": (9, None),
            "sides": (4, None),
            "rear": (3, None),
            "top": (1, None),
        },
        "max_speed": 50,
        # SPAAG kill-XP standard (DCA_STANDARDS["experience_unit"]). Set by hand because the
        # automatic pass looks at the donor's (Leopard's) weapons and doesn't see the AA gun.
        "XP": {"multiplier": 0.001},
        "WeaponDescriptor": {
            # Donor Leopard_1A3_DK turrets: 0 = tourelle1 105mm AP+HE (box 0), 1 = tourelle2
            # coax MG3 (box 1), 2 = tourelle4 loader MG3 (box 2), 3 = tourelle5 smoke (box 3).
            # The 105mm pair becomes the 76mm AA/AT pair; both MG3 turrets are removed (the real
            # OTOMATIC has no machine guns).
            "equipmentchanges": {
                "replace": {
                    # Fire effects borrowed from existing guns (no OTO 76mm effect exists):
                    # Danish M41 Walker's 76mm for AT, 57mm Bofors for AA. Must match the
                    # Actions map in DK_new_depictions/Otomatic_DK.py.
                    "Canon_AP_105mm_L7A3_Leo1A1A2": {
                        "new_weapon": "Canon_AP_Otomatic_76mm_DK",
                        "swap_fire_effect": True,
                        "depiction_baked_in": True,
                        "old_new_effect": ("Canon_AP_105mm_L7A3_Leo1A1A2", "Canon_AP_76mm_M32A1_Walker"),
                    },
                    "Canon_HE_105mm_L7A3": {
                        "new_weapon": "DCA_Otomatic_76mm_DK",
                        "swap_fire_effect": True,
                        "depiction_baked_in": True,
                        "old_new_effect": ("Canon_HE_105mm_L7A3", "DCA_1_canon_Bofors_57mm"),
                    },
                },
            },
            # Final ammo boxes: 0 = AA round, 1 = AP round, 2 = smoke.
            # The AA round (ShotsCountPerSalvo 13) and AP round (ShotsCountPerSalvo 1)
            # can't share a box - the engine requires every ammo on one box to agree on
            # ShotsCountPerSalvo - so the AP round gets box 1 (freed by the coax MG3).
            #
            # NEW_UNITS turret edits only support "insert"/"remove" on MountedWeapons, and
            # "equipmentchanges" runs before "turrets", so a box change = clone the mount with the
            # new AmmoBoxIndex ("insert", appended) then drop the original ("remove": [0]).
            # Turret 3 (smoke) is listed first: the turret-level "remove": [1, 2] on turret 0
            # shifts it to index 1 once it runs.
            "turrets": {
                3: {
                    "MountedWeapons": {
                        "insert": {
                            "SMOKE_Vehicle_Grenadex8": {
                                "AmmoBoxIndex": 2,
                            },
                        },
                        "remove": [0],
                    },
                },
                0: {
                    "MountedWeapons": {
                        "insert": {
                            "Canon_AP_Otomatic_76mm_DK": {
                                "AmmoBoxIndex": 1,
                            },
                        },
                        "remove": [0],
                    },
                    "remove": [1, 2],
                },
            },
            # Salves = number of salvos per ammo box. Donor list [60, 75, 75, 1]; drop the two
            # MG3 boxes -> [60, 1], insert the AP box -> [60, 12, 1], AA box -> [4, 12, 1].
            # AA 52 rounds (4 bursts of 13), AP 12 single shots, smoke 1.
            "Salves": {
                "remove": [1, 2],
                "insert": [
                    (1, 12),
                ],
                "DCA_Otomatic_76mm_DK": 4,  # 4 bursts x 13 = 52 rounds
            },
        },
        # Placeholder icon - reuses the donor's so the card isn't blank. Needs a real
        # Otomatic icon (WACE's otomatic.png, under GameData/Assets/2D/Interface/Common/
        # UnitsIcons/NATO/otomatic.png, could be a starting point).
        "ButtonTexture": "Leopard_1A3_DK",
        "UpgradeFromUnit": None,
        "orders": [
            "EOrderType/Stop",
            "EOrderType/Move",
            "EOrderType/FollowFormation",
            "EOrderType/FollowUnit",
            "EOrderType/QuickMove",
            "EOrderType/Attack",
            "EOrderType/FastMoveAndAttack",
            "EOrderType/MoveAndAttack",
            "EOrderType/Reverse",
            "EOrderType/Shoot",
            "EOrderType/ShootOnPosition",
            "EOrderType/ShootOnPositionWithoutCorrection",
            "EOrderType/ShootDefensiveSmoke",
            "EOrderType/AskForSupply",
            "EOrderType/AIDefend",
            "EOrderType/AIAttack",
            "EOrderType/AIStop",
        ],
        "is_infantry": False,
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "DK",
    },

    # Real tank command unit. The vanilla Leopard_1A3_CMD_DK is turned into a leader tank in
    # DK_unit_edits.py, so this clone keeps the commander module - same split as
    # Leopard_1A5_CMD2_RFA (240) / Leopard_1A1_CMD2_RFA (205).
    ("Leopard_1A3_CMD_DK", 0): {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
        "GUID": "165d3f25-7664-4280-8d22-e7daabf64992",
        "InfantrySquadModuleGUID": "07da1035-a354-42a5-9560-bc180ab6bad0",
        "ShowroomGUID": "ae1df1ec-db7b-4e3e-a74f-94bb9539bd5e",
        "CadavreGUID": "5ec89cf5-9a90-4fd5-8de8-82dede65911a",
        "UnitId": 50119,
        "NewName": "Leopard_1A3_CMD2_DK",
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "CMD_Unit",
                "AllowedForMissileRoE",
                "Char",
                "Char_CMD",
                "Commandant",
                "GroundUnits",
                "InfmapCommander",
                "UNITE_Leopard_1A3_CMD2_DK",
                "Unite",
            ],
        },
        "Factory": "Factory/Logistic",
        "CommandPoints": 215,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False,
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "DK",
    },

    # Real infantry command squad, same idea as Engineers_CMD2_RFA (145). The vanilla
    # Rifles_CMD_DK becomes a leader squad in DK_unit_edits.py.
    ("Rifles_CMD_DK", 0): {
        "GUID": "6d77d1e0-a9cd-46c2-8bb5-82384f335135",
        "InfantrySquadModuleGUID": "cf9ae569-0e59-4f9c-b9f8-bc735b293b4f",
        "ShowroomGUID": "477d2b2c-86ee-4efc-a9fb-d6fdcd0c6a63",
        "CadavreGUID": "512c1605-5c65-4f25-8d5a-7e0c54c0ebba",
        "UnitId": 50120,
        "NewName": "Rifles_CMD2_DK",
        "GameName": {
            "display": "KOMMANDOGRUPPE",
            "token": "NEATMMKIFQ",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "CMD_Unit",
                "AllowedForMissileRoE",
                "Commandant",
                "Crew",
                "GroundUnits",
                "Inf_quartier_ok",
                "Infanterie",
                "Infanterie_CMD",
                "InfmapCommander",
                "UNITE_Rifles_CMD2_DK",
                "Unite",
            ],
        },
        "strength": 4,  # donor's; the weapon handler skips new infantry without it
        "TransportedTexture": "UseInGame_Transport_COMMAND",
        "TransportedSoldier": "Rifles_CMD_DK",
        "Factory": "Factory/Logistic",
        "CommandPoints": 145,
        "SpecialtiesList": [
            '_leader',
            'infantry_equip_light',
        ],
        "MenuIconTexture": "Texture_RTS_H_CMD_inf",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/CMD_Inf",
        "max_speed": 26,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/SmartMove', 'EOrderType/Attack', 'EOrderType/SmartMoveAndAttack', 'EOrderType/MoveAndAttack',
                   'EOrderType/Shoot', 'EOrderType/ShootOnPosition', 'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootOnPositionSmoke',
                   'EOrderType/ShootOnPositionWithoutCorrectionSmoke', 'EOrderType/AskForSupply', 'EOrderType/EnterDistrict', 'EOrderType/Load',
                   'EOrderType/Load', 'EOrderType/UseCapacite', 'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": True,
        "is_heavy_equipment": False,
        "is_ground_vehicle": False,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "DK",
        # Donor's own depiction values (DepictionInfantry.ndf: Count 5, UniqueCount 2,
        # InfantrySelectorTactic_02_05).
        "alternatives_count": 5,
        "unique_count": 2,
        "selector_tactic": "02_05",
    },
    # Recon Leopard 1A5, cloned from the Danish Leopard_1A5_DK (Danish mesh/icon) and given
    # the recon setup of vanilla Leopard_1A5_reco_RFA: recon tab/role/tags, optics
    # 5300/5300/1413, forward deploy (750 m, as WA). WA balance as Leopard_1A5_reco_RFA: 115 pts,
    # Reload_Penalty, identify 1.0 / 3 s (= vanilla recon 0.5 / 6 s after WA's x2 pass).
    ("Leopard_1A5_DK", 0): {
        "capacities": {
            "add_capacities": ["Reload_Penalty"],
        },
        "GUID": "2b251aee-b5f4-4777-9ab6-0a692e5eaecd",
        "InfantrySquadModuleGUID": "a0f1945b-d7dd-45d9-83e6-8cbe8661a859",
        "ShowroomGUID": "572c0979-2a70-4b64-833f-09b2219ebec3",
        "CadavreGUID": "186a5ab5-f20a-4fed-bc54-78df0ab6aed4",
        "UnitId": 50121,
        "NewName": "Leopard_1A5_reco_DK",
        "CommandPoints": 115,
        "TypeUnit": {
            "MotherCountry": "DK",
            "AcknowUnitTypes": ["Recon_Vehicle"],
            "TypeUnitFormation": "Reconnaissance",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_Reco",
                "GroundUnits",
                "Radio",
                "Reco",
                "UNITE_Leopard_1A5_reco_DK",
                "Unite",
            ],
        },
        "Factory": "Factory/Recons",
        "UnitRole": "reco",
        "IdentifiedTextures": ["Texture_RTS_H_reco", "Texture_reco"],
        "UnidentifiedTextures": ["Texture_RTS_H_veh_nonIdentifie", "Texture_veh_nonIdentifie"],
        "MenuIconTexture": "Texture_RTS_H_reco",
        "TypeStrategicCount": "ETypeStrategicDetailedCount/Reco",
        "optics": {
            "OpticalStrengths": {
                "EOpticalStrength/Standard": 5300.0,
                "EOpticalStrength/LowAltitude": 5300.0,
                "EOpticalStrength/HighAltitude": 1413.0,
            },
            "IdentifyBaseProbability": 1.0,
            "TimeBetweenEachIdentifyRoll": 3.0,
        },
        "DeploymentShift": 750,  # WA forward deploy of Leopard_1A5_reco_RFA (vanilla 2473)
        "ButtonTexture": "Leopard_1A5_DK",  # no own icon yet - reuse the Danish Leopard 1A5's
        "UpgradeFromUnit": None,
        "orders": ['EOrderType/Stop', 'EOrderType/Move', 'EOrderType/FollowFormation', 'EOrderType/FollowUnit', 'EOrderType/QuickMove', 'EOrderType/Attack', 'EOrderType/FastMoveAndAttack',
                   'EOrderType/MoveAndAttack', 'EOrderType/Reverse', 'EOrderType/Shoot', 'EOrderType/ShootOnPosition',
                   'EOrderType/ShootOnPositionWithoutCorrection', 'EOrderType/ShootDefensiveSmoke', 'EOrderType/AskForSupply',
                   'EOrderType/AIDefend', 'EOrderType/AIAttack', 'EOrderType/AIStop'],
        "is_infantry": False,
        "is_heavy_equipment": False,
        "is_ground_vehicle": True,
        "is_aerial": False,
        "is_unarmed": False,
        "Faction": "NATO",
        "Nation": "DK",
    },
}
# fmt: on
