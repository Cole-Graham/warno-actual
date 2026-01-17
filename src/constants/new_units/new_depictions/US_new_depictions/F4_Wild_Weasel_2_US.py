from typing import Dict, Any

# fmt: off
f4_wild_weasel_2_us: Dict[str, Dict[str, Any]] = {
    "unit_name": "F4_Wild_Weasel_2_US",
    "valid_files": ["DepictionAerialUnits.ndf", "DepictionAerialUnitsShowRoom.ndf", "MissileCarriage.ndf",
                    "MissileCarriageDepiction.ndf"],
    "DepictionAerialUnits_ndf": {
        "weapon2": 
            """Op_F4_Wild_Weasel_2_US_Weapon2 is DepictionOperator_WeaponMissileCarriageFire
            (
                Connoisseur = MissileCarriage_F4_Wild_Weasel_2_US
                FireEffectTag = "weapon_effet_tag2"
                NbProj = 1
                WeaponIndex = 2
                WeaponShootDataPropertyName = 
                [
                    "WeaponShootData_0_2",
                ]
            )""",
        "weapon3": """
            Op_F4_Wild_Weasel_2_US_Weapon3 is DepictionOperator_WeaponMissileCarriageFire
            (
                Connoisseur = MissileCarriage_F4_Wild_Weasel_2_US
                FireEffectTag = "weapon_effet_tag3"
                NbProj = 1
                WeaponIndex = 3
                WeaponShootDataPropertyName = 
                [
                    "WeaponShootData_0_3",
                ]
            )""",
        "weapon4": """
            Op_F4_Wild_Weasel_2_US_Weapon4 is DepictionOperator_WeaponMissileCarriageFire
            (
                Connoisseur = MissileCarriage_F4_Wild_Weasel_2_US
                FireEffectTag = "weapon_effet_tag4"
                NbProj = 1
                WeaponIndex = 4
                WeaponShootDataPropertyName = 
                [
                    "WeaponShootData_0_4",
                ]
            )""",
        "weapon5": """
            Op_F4_Wild_Weasel_2_US_Weapon5 is DepictionOperator_WeaponMissileCarriageFire
            (
                Connoisseur = MissileCarriage_F4_Wild_Weasel_2_US
                FireEffectTag = "weapon_effet_tag5"
                NbProj = 1
                WeaponIndex = 5
                WeaponShootDataPropertyName = 
                [
                    "WeaponShootData_0_5",
                ]
            )""",
        "TacticAerialDepictionRegistration": """
            unnamed TacticAerialDepictionRegistration
            (
                Deviator = DepictionDeviator_Airplane
                AdditionalTextures = $/M3D/Shader/AirplaneDestTextures
                Selector = SpecificAirplaneDepictionSelector
                CoatingName = 'F4_Wild_Weasel_2_US'
                Alternatives = Alternatives_F4_Wild_Weasel_2_US

                Operators = 
                    [
                        $/GFX/Sound/DepictionOperator_MovementSound_SM_SD_avion_multirole_F4,
                        DepictionOperator_SoundProbe,
                        Op_F4_Wild_Weasel_2_US_Weapon2,
                        Op_F4_Wild_Weasel_2_US_Weapon3,
                        Op_F4_Wild_Weasel_2_US_Weapon4,
                        Op_F4_Wild_Weasel_2_US_Weapon5,
                        DepictionOperator_CriticalEffects,
                        DepictionOperator_AirplaneParts,
                        DepictionOperator_Airplane,
                        DepictionOperator_AirplaneShadow,
                        DepictionOperator_Feedback_Degat_Level1,
                        DepictionOperator_Feedback_Degat_Level2,
                        DepictionOperator_EjectableProps_Plane,
                        DepictionOperator_Flares,
                    ]
                    Actions = MAP[
                                ( "weapon_effet_tag2", Weapon_AGM_AGM88_HARM ),
                                ( "weapon_effet_tag3", Weapon_AA_AIM9M_Sidewinder ),
                                ( "weapon_effet_tag4", Weapon_AGM_AGM65D_Maverick ),
                                ( "weapon_effet_tag5", Weapon_AA_AIM7M_Sparrow ),
                            ]
                            + DepictionAction_Stress_And_Wrecked_Avion
                            + DepictionAction_CriticalFX_Airplane
                            + DepictionAction_MovementFX_DoubleReactorAirplane_VerySmoky
                            + DepictionAction_Flare_Simple

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
                    SubDepictionGenerators = [ SubGenerators_F4_Wild_Weasel_2_US ]
            )""",
    },
    
    "DepictionAerialUnitsShowroom_ndf": {
        "ShowroomAerialDepictionRegistration": """
            unnamed ShowroomAerialDepictionRegistration
            (
                MeshDescriptor = $/GFX/DepictionResources/Modele_F4_Wild_Weasel_2_US
                MimeticName = 'showroom_F4_Wild_Weasel_2_US'
                SubDepictionGenerators = 
                [
                    SubGenerators_Showroom_F4_Wild_Weasel_2_US,
                ]
                SubDepictions = 
                [
                    ShowroomLandingGear
                    (
                        MeshDescriptor = $/GFX/DepictionResources/Modele_F4_Wild_Weasel_2_US_train
                    ),
                ]
            )""",
    },
    
    "MissileCarriage_ndf": {
        "carriage": """
            export MissileCarriage_F4_Wild_Weasel_2_US is TMissileCarriageConnoisseur
            (
                MeshDescriptor = $/GFX/DepictionResources/Modele_F4_Wild_Weasel_2_US
                PylonSet = ~/DepictionPylonSet_Airplane_Default
                WeaponInfos = 
                [
                    TMissileCarriageWeaponInfo( MissileCount=3 MissileType=eAGM WeaponIndex=2 ),
                    TMissileCarriageWeaponInfo( MissileCount=2 MissileType=eAAM WeaponIndex=3 ),
                    TMissileCarriageWeaponInfo( MissileCount=3 MissileType=eAGM WeaponIndex=4 ),
                    TMissileCarriageWeaponInfo( MissileCount=2 MissileType=eAAM WeaponIndex=5 ),
                ]
            )""",
        "carriage_showroom": """
            export MissileCarriage_F4_Wild_Weasel_2_US_Showroom is TMissileCarriageConnoisseur
            (
                MeshDescriptor = $/GFX/DepictionResources/Modele_F4_Wild_Weasel_2_US
                PylonSet = ~/DepictionPylonSet_Airplane_Default_Showroom
                WeaponInfos = ~/MissileCarriage_F4_Wild_Weasel_2_US.WeaponInfos
            )""",
    },
    
    "MissileCarriageDepiction_ndf": {
        "carriage_depiction": """
            SubGenerators_F4_Wild_Weasel_2_US is TStaticMissileCarriageSubDepictionGenerator
            (
                MissileCarriageConnoisseur = MissileCarriage_F4_Wild_Weasel_2_US
                Missiles = 
                [
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionStaticMissiles
                        (
                            PhysicalProperty = "Tourelle2_MissileCount"
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_AGM88_Harm
                        )
                        MissileCount = 3
                        WeaponIndex = 2
                    ),
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionStaticMissiles
                        (
                            PhysicalProperty = "Tourelle3_MissileCount"
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_SideWinder
                        )
                        MissileCount = 2
                        WeaponIndex = 3
                    ),
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionStaticMissiles
                        (
                            PhysicalProperty = "Tourelle4_MissileCount"
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_Maverick_AGM65D
                        )
                        MissileCount = 2
                        WeaponIndex = 4
                    ),
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionStaticMissiles
                        (
                            PhysicalProperty = "Tourelle5_MissileCount"
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_AIM7
                        )
                        MissileCount = 2
                        WeaponIndex = 5
                    ),
                ]
                Pylons = ~/DepictionPylonSet_Airplane_Default
                ReferenceMesh = $/GFX/DepictionResources/Modele_F4_Wild_Weasel_2_US
            )""",
        "carriage_depiction_showroom": """
            SubGenerators_Showroom_F4_Wild_Weasel_2_US is TStaticMissileCarriageSubDepictionGenerator
            (
                MissileCarriageConnoisseur = MissileCarriage_F4_Wild_Weasel_2_US_Showroom
                Missiles = 
                [
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionMissileShowroom
                        (
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_AGM88_Harm
                        )
                        MissileCount = 3
                        WeaponIndex = 2
                    ),
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionMissileShowroom
                        (
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_SideWinder
                        )
                        MissileCount = 2
                        WeaponIndex = 3
                    ),
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionMissileShowroom
                        (
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_Maverick_AGM65D
                        )
                        MissileCount = 2
                        WeaponIndex = 4
                    ),
                    TStaticMissileCarriageSubDepictionMissileInfo
                    (
                        Depiction = TemplateDepictionMissileShowroom
                        (
                            ProjectileModelResource = $/GFX/DepictionResources/Modele_Missile_AIM7
                        )
                        MissileCount = 2
                        WeaponIndex = 5
                    ),
                ]
                Pylons = ~/DepictionPylonSet_Airplane_Default_Showroom
                ReferenceMesh = $/GFX/DepictionResources/Modele_F4_Wild_Weasel_2_US
            )""",
    },
    "F4_Wild_Weasel_2_US_ndf": {
        "directory": "Avion",
        "ndf_code": """
            export Modele_F4_Wild_Weasel_2_US is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/F4G/F4G/F4G.fbx"
            )

            export Modele_F4_Wild_Weasel_2_US_MID is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/F4G/F4G_MID/F4G_MID.fbx"
            )

            export Modele_F4_Wild_Weasel_2_US_LOW is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/F4G/F4G_LOW/F4G_LOW.fbx"
            )

            export Modele_F4_Wild_Weasel_2_US_train is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/US/Avion/F4G/F4G/F4G_train.fbx"
            )""",
    },
}
# fmt: on
