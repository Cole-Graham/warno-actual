from typing import Dict, Any

# fmt: off
f15e_strikeeagle_pgb2_us: Dict[str, Dict[str, Any]] = {
    "unit_name": "F15E_StrikeEagle_PGB2_US",
    "valid_files": ["DepictionAerialUnits.ndf", "DepictionAerialUnitsShowRoom.ndf", "MissileCarriage.ndf",
                    "MissileCarriageDepiction.ndf"],
    "DepictionAerialUnits_ndf": {
        "weapon1":
            """Op_F15E_StrikeEagle_PGB2_US_Weapon1 is DepictionOperator_WeaponContinuousFire
            (
                Anchors = 
                [
                    "fx_tourelle1_tir_01",
                ]
                FireEffectTag = "weapon_effet_tag1"
                NbFX = 1
                WeaponActiveAndCanShootPropertyName = "WeaponActiveAndCanShoot_1"
                WeaponShootDataPropertyName = "WeaponShootData_0_1"
            )""",
        "weapon2": 
            """Op_F15E_StrikeEagle_PGB2_US_Weapon2 is DepictionOperator_WeaponMissileCarriageFire
            (
                Connoisseur = MissileCarriage_F15E_StrikeEagle_PGB2_US
                FireEffectTag = "weapon_effet_tag2"
                NbProj = 2
                WeaponIndex = 2
                WeaponShootDataPropertyName = 
                [
                    "WeaponShootData_0_2",
                    "WeaponShootData_1_2",
                ]
            )""",
        "weapon3": """
            Op_F15E_StrikeEagle_PGB2_US_Weapon3 is DepictionOperator_WeaponMissileCarriageFire
            (
                Connoisseur = MissileCarriage_F15E_StrikeEagle_PGB2_US
                FireEffectTag = "weapon_effet_tag3"
                NbProj = 1
                WeaponIndex = 2
                WeaponShootDataPropertyName = 
                [
                    "WeaponShootData_0_3",
                ]
            )""",
        "weapon4": """
            Op_F15E_StrikeEagle_PGB2_US_Weapon4 is DepictionOperator_WeaponMissileCarriageFire
            (
                Connoisseur = MissileCarriage_F15E_StrikeEagle_PGB2_US
                FireEffectTag = "weapon_effet_tag4"
                NbProj = 1
                WeaponIndex = 3
                WeaponShootDataPropertyName = 
                [
                    "WeaponShootData_0_4",
                ]
            )""",
        "TacticAerialDepictionRegistration": """
            unnamed TacticAerialDepictionRegistration
            (
                Deviator = DepictionDeviator_Airplane
                AdditionalTextures = $/M3D/Shader/AirplaneDestTextures
                Selector = SpecificAirplaneDepictionSelector
                CoatingName = 'F15E_StrikeEagle_PGB2_US'
                Alternatives = Alternatives_F15E_StrikeEagle_PGB2_US

                Operators = 
                    [
                        $/GFX/Sound/DepictionOperator_MovementSound_SM_SD_avion_multirole_F15,
                        DepictionOperator_SoundProbe,
                        DepictionOperator_Turret_1_Aim,
                        Op_F15E_StrikeEagle_PGB2_US_Weapon1,
                        Op_F15E_StrikeEagle_PGB2_US_Weapon2,
                        Op_F15E_StrikeEagle_PGB2_US_Weapon3,
                        Op_F15E_StrikeEagle_PGB2_US_Weapon4,
                        DepictionOperator_CriticalEffects,
                        DepictionOperator_AirplaneParts,
                        DepictionOperator_Airplane,
                        DepictionOperator_AirplaneShadow,
                        DepictionOperator_Feedback_Degat_Level1,
                        DepictionOperator_Feedback_Degat_Level2,
                        DepictionOperator_Heat,
                        DepictionOperator_EjectableProps_Plane,
                        DepictionOperator_Flares,
                    ]
                    Actions = MAP[
                                ( "weapon_effet_tag1", Weapon_GatlingAir_M61_Vulcan_20mm ),
                                ( "weapon_effet_tag2", Weapon_Bomb_GBU_10_x2 ),
                                ( "weapon_effet_tag3", Weapon_Bomb_Mk84_920kg_x4 ),
                                ( "weapon_effet_tag4", Weapon_AA_AIM9M_Sidewinder ),
                            ]
                            + DepictionAction_Stress_And_Wrecked_Avion
                            + DepictionAction_CriticalFX_Airplane
                            + DepictionAction_MovementFX_DoubleReactorAirplane
                            + DepictionAction_Flare_Double

                    SubDepictions = 

                    [
                        TSubDepiction
                        (
                            Anchors = 
                            [
                                "pilot",
                                "pilot2",
                            ]
                            Depiction = Pilot_Pilote_US
                        ),
                    ]        

                    SubDepictionGenerators = [ SubGenerators_F15E_StrikeEagle_PGB2_US ]
            )""",
    },
    
    "DepictionAerialUnitsShowroom_ndf": {
        "ShowroomAerialDepictionRegistration": """
            unnamed ShowroomAerialDepictionRegistration
            (
                MeshDescriptor = $/GFX/DepictionResources/Modele_F15E_StrikeEagle_US
                MimeticName = 'showroom_F15E_StrikeEagle_PGB2_US'
                SubDepictionGenerators = 
                [
                    SubGenerators_Showroom_F15E_StrikeEagle_PGB2_US,
                ]
                SubDepictions = 
                [
                    ShowroomLandingGear
                    (
                        MeshDescriptor = $/GFX/DepictionResources/Modele_F15E_StrikeEagle_US_train
                    ),
                ]
            )""",
    },
    
    "MissileCarriage_ndf": {
        "carriage": """
            export MissileCarriage_F15E_StrikeEagle_PGB2_US is TMissileCarriageConnoisseur
            (
                MeshDescriptor = $/GFX/DepictionResources/Modele_F15E_StrikeEagle_US
                PylonSet = ~/DepictionPylonSet_Airplane_Default
                WeaponInfos = 
                [
                    TMissileCarriageWeaponInfo( MissileCount=2 MissileType=eAGM WeaponIndex=2 ),
                    TMissileCarriageWeaponInfo( MissileCount=2 MissileType=eAGM MountingType=eMountingBomb WeaponIndex=2 ),
                    TMissileCarriageWeaponInfo( MissileCount=4 MissileType=eAAM WeaponIndex=3 ),
                ]
            )""",
        "carriage_showroom": """
            export MissileCarriage_F15E_StrikeEagle_PGB2_US_Showroom is TMissileCarriageConnoisseur
            (
                MeshDescriptor = $/GFX/DepictionResources/Modele_F15E_StrikeEagle_US
                PylonSet = ~/DepictionPylonSet_Airplane_Default_Showroom
                WeaponInfos = ~/MissileCarriage_F15E_StrikeEagle_PGB2_US.WeaponInfos
            )""",
    },
    
    "MissileCarriageDepiction_ndf": {
        "carriage_depiction": """
            SubGenerators_F15E_StrikeEagle_PGB2_US is TStaticMissileCarriageSubDepictionGenerator
            (
                MissileCarriageConnoisseur = MissileCarriage_F15E_StrikeEagle_PGB2_US
                Missiles = 
                [
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionStaticMissiles
                        (
                            PhysicalProperty = "Tourelle2_MissileCount"
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_GBU10
                        )
                        MissileCount = 2
                        WeaponIndex = 2
                    ),
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionStaticMissiles
                        (
                            PhysicalProperty = "Tourelle2_MissileCount"
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_Mk_83
                        )
                        MissileCount = 2
                        WeaponIndex = 2
                    ),
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionStaticMissiles
                        (
                            PhysicalProperty = "Tourelle4_MissileCount"
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_SideWinder
                        )
                        MissileCount = 4
                        WeaponIndex = 3
                    ),
                ]
                Pylons = ~/DepictionPylonSet_Airplane_Default
                ReferenceMesh = $/GFX/DepictionResources/Modele_F15E_StrikeEagle_US
            )""",
        "carriage_depiction_showroom": """
            SubGenerators_Showroom_F15E_StrikeEagle_PGB2_US is TShowroomMissileCarriageSubDepictionGenerator
            (
                MissileCarriageConnoisseur = MissileCarriage_F15E_StrikeEagle_PGB2_US_Showroom
                Missiles = 
                [
                    TShowroomMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionMissileShowroom
                        (
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_GBU10
                        )
                        MissileCount = 2
                        WeaponIndex = 2
                    ),
                    TShowroomMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionMissileShowroom
                        (
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_Mk_83
                        )
                        MissileCount = 2
                        WeaponIndex = 2
                    ),
                    TShowroomMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionMissileShowroom
                        (
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_SideWinder
                        )
                        MissileCount = 4
                        WeaponIndex = 3
                    ),
                ]
                Pylons = ~/DepictionPylonSet_Airplane_Default_Showroom
                ReferenceMesh = $/GFX/DepictionResources/Modele_F15E_StrikeEagle_US
            )""",
    },
}
# fmt: on
