"""M2_Bradley_BSV_US depiction edits.

Adds AP autocannon support to match the unit descriptor's weapon layout.
Uses the M2A2 Bradley pattern: AP at weapon_effet_tag1, HE at weapon_effet_tag2,
with ATGM and MMG shifted to tag3 and tag4.
"""

from typing import Dict, Tuple, Union

# fmt: off
m2_bradley_bsv_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "M2_Bradley_BSV_US",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        "new_objects": {
            "weapon1_ap": """
                DepictionOperator_M2_Bradley_BSV_US_Weapon1_AP is DepictionOperator_WeaponInstantFire
                (
                    FireEffectTag = 'weapon_effet_tag1'
                    Anchors = ["fx_tourelle1_tir_01"]
                    WeaponShootDataPropertyName = ['WeaponShootData_0_1']
                    NbProj = 1
                )
            """,
        },
        # Shift original Weapon1 (HE) to slot 2
        ("DepictionOperator_M2_Bradley_BSV_US_Weapon1", "DepictionOperator_WeaponInstantFire"): {
            "FireEffectTag": "'weapon_effet_tag2'",
            "Anchors": ["fx_tourelle1_tir_01"],
            "WeaponShootDataPropertyName": ["'WeaponShootData_0_2'"],
            "NbProj": 1,
        },
        # Modify Weapon2 (ATGM) to use slot 3
        ("DepictionOperator_M2_Bradley_BSV_US_Weapon2", "DepictionOperator_WeaponMissileCarriageFire"): {
            "FireEffectTag": "'weapon_effet_tag3'",
            "WeaponShootDataPropertyName": ["'WeaponShootData_0_3'"],
        },
        # Modify Weapon3 (MMG) to use slot 4
        ("DepictionOperator_M2_Bradley_BSV_US_Weapon3", "DepictionOperator_WeaponContinuousFire"): {
            "FireEffectTag": "'weapon_effet_tag4'",
            "WeaponActiveAndCanShootPropertyName": "'WeaponActiveAndCanShoot_4'",
            "WeaponShootDataPropertyName": ["'WeaponShootData_0_4'"],
        },
        # Add AP operator to list and replace Actions MAP
        (None, "TacticVehicleDepictionRegistration"): {
            "Operators": {
                12: ("add", (
                    "DepictionOperator_M2_Bradley_BSV_US_Weapon1_AP",
                )),
            },
            "Actions": (
                'MAP['
                '            ( "weapon_effet_tag1", Weapon_AutoCanon_AP_25mm_M242_Bushmaster_Late ),'
                '            ( "weapon_effet_tag2", Weapon_AutoCanon_HE_25mm_M242_Bushmaster_Late_BSV ),'
                '            ( "weapon_effet_tag3", Weapon_ATGM_BGM71C_ITOW_x2_IFV ),'
                '            ( "weapon_effet_tag4", Weapon_MMG_M240_7_62mm ),'
                '            ( "weapon_effet_tag5", Weapon_SMOKE_Vehicle_Grenadex8 ),'
                '        ]'
                '        + DepictionAction_Stress_And_Wrecked'
                '        + DepictionAction_MovementFX_Tracked'
                '        + DepictionAction_CriticalFX_Tank'
            ),
        },
    },
}
# fmt: on
