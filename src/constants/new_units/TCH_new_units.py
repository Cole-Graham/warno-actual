"""New unit definitions for Czechoslovakia."""

# fmt: off
TCH_NEW_UNITS = {
    ("T72B1_SOV", 0): {
        "GUID": "19f1e836-3b7b-409a-a8cc-a9ceaf0baa4e",
        "InfantrySquadModuleGUID": "7ea7a948-14bc-4d90-aaa4-593dcd23650f",
        "ShowroomGUID": "f85a301a-aef3-4d62-ab72-670e81b43106",
        "CadavreGUID": "4b9c54e3-3e8b-4708-b962-9396cb0398a6",
        "UnitId": 50117,
        "NewName": "T72M2_Moderna_TCH",
        "CommandPoints": 275,
        "GameName": {
            "display": "T-72M2 MODERNA",
            "token": "TCHMODERNA",
        },
        "TypeUnit": {
            "MotherCountry": "TCH",
        },
        "TagSet": {
            "overwrite_all": [
                "AllUnits",
                "AllowedForMissileRoE",
                "Char",
                "Char_Standard",
                "GroundUnits",
                "SM_charLourd",
                "UNITE_T72M2_Moderna_TCH",
                "Unite",
            ],
        },
        "depictions": {
            "new_mesh": True,
            # Donor SubDepictions parents Modele_T72B1_SOV_Tourelle_02 to
            # base_tourelle_02. The Moderna mesh has no base_tourelle_* bone.
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
            "front": (20, None),
            "sides": (8, None),
            "rear": (4, None),
            "top": (4, None),
        },
        "max_speed": 55,
        "SpecialtiesList": [
            "_smoke_launcher",
            "_era",
        ],
        "WeaponDescriptor": {
            # Donor T72B1 turrets (index is 0-based; Tag / YulBoneOrdinal is the
            # tourelle number): 0=tourelle1 125mm, 1=tourelle2 NSVT, 2=tourelle4
            # PKT, 3=tourelle5 smoke. On the Moderna, tourelle2 is the 30mm, so
            # the AP/HE pair is cloned onto turret 1 from the NSVT mount and the
            # NSVT itself is removed (index 0, before the appended clones). The
            # "N:" prefix disambiguates the two clones. PKT stays on turret 2.
            # Magazine 62 is the authored BMP-2 30mm salvo.
            # 125mm is the T-72B 2A46M pair, swapped to the Moderna 2A46MS clones.
            # Fire effects stay on the donor so the muzzle flash is unchanged.
            "equipmentchanges": {
                "replace": {
                    "Canon_AP_125_mm_2A46M": {
                        "new_weapon": "Canon_AP_125_mm_2A46MS_Moderna",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                    "Canon_HE_125_mm_2A46M": {
                        "new_weapon": "Canon_HE_125_mm_2A46MS_Moderna",
                        "swap_fire_effect": False,
                        "depiction_baked_in": True,
                    },
                },
            },
            "turrets": {
                1: {
                    # Parent is the main gun's YulBoneOrdinal (tourelle1), same
                    # link the donor PKT uses. A mastered turret must have
                    # AimingPriority > 0; the PKT uses 3.
                    "AimingPriority": 2,
                    "MasterTurretYulBoneOrdinal": 1,
                    "AngleRotationMax": 0.17453292519943295,  # 10 degrees
                    "AngleRotationMaxPitch": 0.7853981633974483,  # 45 degrees
                    "MountedWeapons": {
                        "remove": [0],
                        "insert": {
                            "0:HMG_12_7_mm_NSVT": {
                                "Ammunition": "$/GFX/Weapon/Ammo_AutoCanon_AP_30mm_24A2_BMP2",
                                "AnimateOnlyOneSoldier": False,
                                "EffectTag": "'FireEffect_AutoCanon_AP_30mm_24A2_BMP2'",
                                "HandheldEquipmentKey": "'WeaponAlternative_6'",
                                "AmmoBoxIndex": 4,
                                "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_6'",
                                "WeaponIgnoredPropertyName": "'WeaponIgnored_6'",
                                "WeaponShootDataPropertyName": ["WeaponShootData_0_6"],
                                "NbWeapons": 1,
                            },
                            "1:HMG_12_7_mm_NSVT": {
                                "Ammunition": "$/GFX/Weapon/Ammo_AutoCanon_HE_30mm_24A2_BMP2",
                                "AnimateOnlyOneSoldier": False,
                                "EffectTag": "'FireEffect_AutoCanon_HE_30mm_24A2_BMP2'",
                                "HandheldEquipmentKey": "'WeaponAlternative_7'",
                                "AmmoBoxIndex": 4,
                                "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_7'",
                                "WeaponIgnoredPropertyName": "'WeaponIgnored_7'",
                                "WeaponShootDataPropertyName": ["WeaponShootData_0_7"],
                                "NbWeapons": 1,
                            },
                        },
                    },
                },
            },
            "Salves": {
                "insert": [
                    (4, 40),
                ],
            },
        },
        "ButtonTexture": "T72B1_SOV",
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
        "Faction": "PACT",
        "Nation": "TCH",
    },
}
# fmt: on
