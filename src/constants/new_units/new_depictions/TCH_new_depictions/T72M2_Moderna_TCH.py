from typing import Any, Dict

# fmt: off
t72m2_moderna_tch: Dict[str, Any] = {
    "unit_name": "T72M2_Moderna_TCH",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        # Donor operators cover weapons 1-5. Weapon 4 (PKT) already uses
        # fx_tourelle4_tir_01. The 30mm pair uses the BMP-2 instant-fire shape
        # on the tourelle 2 muzzle, fx_tourelle2_tir_01 (parent canon_02).
        # Operator index 15 is the cloned NSVT (Weapon3), which also anchors
        # that muzzle. Adds at 18 and 19 run before the remove, and 15 sits
        # below them, so the remove still hits Weapon3.
        "new_objects": {
            "weapon6": """
                DepictionOperator_T72M2_Moderna_TCH_Weapon6 is DepictionOperator_WeaponInstantFire
                (
                    FireEffectTag = "weapon_effet_tag6"
                    Anchors = ["fx_tourelle2_tir_01"]
                    WeaponShootDataPropertyName = ['WeaponShootData_0_6']
                    NbProj = 1
                )
            """,
            "weapon7": """
                DepictionOperator_T72M2_Moderna_TCH_Weapon7 is DepictionOperator_WeaponInstantFire
                (
                    FireEffectTag = "weapon_effet_tag7"
                    Anchors = ["fx_tourelle2_tir_01"]
                    WeaponShootDataPropertyName = ['WeaponShootData_0_7']
                    NbProj = 1
                )
            """,
        },
        (None, "TacticVehicleDepictionRegistration"): {
            "Operators": {
                15: ("remove", None),
                18: ("add", "DepictionOperator_T72M2_Moderna_TCH_Weapon6"),
                19: ("add", "DepictionOperator_T72M2_Moderna_TCH_Weapon7"),
            },
            "Actions": (
                'MAP['
                '            ( "weapon_effet_tag1", Weapon_Canon_AP_125_mm_2A46M ),'
                '            ( "weapon_effet_tag2", Weapon_Canon_HE_125_mm_2A46M ),'
                '            ( "weapon_effet_tag4", Weapon_MMG_PKT_7_62mm ),'
                '            ( "weapon_effet_tag5", Weapon_SMOKE_Vehicle_Grenadex8 ),'
                '            ( "weapon_effet_tag6", Weapon_AutoCanon_AP_30mm_24A2_BMP2 ),'
                '            ( "weapon_effet_tag7", Weapon_AutoCanon_HE_30mm_24A2_BMP2 ),'
                '        ]'
                '        + DepictionAction_Stress_And_Wrecked'
                '        + DepictionAction_MovementFX_Tracked'
                '        + DepictionAction_CriticalFX_Tank'
            ),
        },
    },
    # Only moderna.fbx exists. Mid and low use that mesh; there is no mid fbx
    # and low/ is a blend, not an fbx.
    "T72M2_Moderna_TCH_ndf": {
        "directory": "Char",
        "ndf_code": """
            export Modele_T72M2_Moderna_TCH is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/tch/char/moderna/moderna.fbx"
            )

            export Modele_T72M2_Moderna_TCH_MID is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/tch/char/moderna/moderna.fbx"
            )

            export Modele_T72M2_Moderna_TCH_LOW is TResourceMesh
            (
                Mesh="GameData:/Assets/3D/Units/tch/char/moderna/moderna.fbx"
            )""",
    },
}
# fmt: on
