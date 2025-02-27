"""VAB_T20_FR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
vab_t20_fr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "VAB_T20_FR",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        ("DepictionOperator_AMX_10_PC_CMD_FR_Weapon1", "DepictionOperator_WeaponInstantFire"): {
            "copy": "DepictionOperator_VAB_T20_FR_Weapon3",
            "FireEffectTag": "'weapon_effet_tag3'",
            "WeaponShootDataPropertyName": ["'WeaponShootData_0_3'"],
        },
        
        ("Gfx_VAB_T20_FR", "TacticVehicleDepictionTemplate"): {
            "Operators": {
                7: ("add", (
                    "DepictionOperator_VAB_T20_FR_Weapon3"
                )),
            },
            "Actions": (
                'MAP['
                '            ( [ "weapon_effet_tag1" ], Weapon_AutoCanon_AP_M693_F1_20mm ),'
                '            ( [ "weapon_effet_tag2" ], Weapon_MMG_AANF1_7_62mm ),'
                '            ( [ "weapon_effet_tag3" ], Weapon_AutoCanon_HE_M693_F1_20mm ),'
                '            ( [ "weapon_effet_tag5" ], Weapon_SMOKE_Vehicle_Grenadex8 ),'
                '        ]'
                '        + DepictionAction_Stress_And_Wrecked'
                '        + DepictionAction_MovementFX_Wheeled'
                '        + DepictionAction_CriticalFX_Tank'
                '        + DepictionAction_FX_Amphibious_NoPropulsion'
            ),
        },
    },
}
# fmt: on
