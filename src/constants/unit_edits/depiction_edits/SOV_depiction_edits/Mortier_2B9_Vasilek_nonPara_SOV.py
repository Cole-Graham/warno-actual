"""Mortier_2B9_Vasilek_nonPara_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
mortier_2b9_vasilek_nonpara_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Mortier_2B9_Vasilek_nonPara_SOV",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        ("DepictionOperator_Mortier_2B9_Vasilek_nonPara_SOV_Weapon1", "DepictionOperator_WeaponInstantFire"): {
            "copy": "DepictionOperator_Mortier_2B9_Vasilek_nonPara_SOV_Weapon3",
            "FireEffectTag": "'weapon_effet_tag3'",
            "WeaponShootDataPropertyName": ["'WeaponShootData_0_3'"],
        },
        
        (None, "TacticVehicleDepictionRegistration"): {
            "Operators": {
                7: ("add", (
                    "DepictionOperator_Mortier_2B9_Vasilek_nonPara_SOV_Weapon3"
                )),
            },
            "Actions": (
                'MAP['
                '            ( "weapon_effet_tag1", Weapon_Mortier_Vasilek_82mm_towed ),'
                '            ( "weapon_effet_tag2", Weapon_Mortier_Vasilek_indirect_82mm_towed ),'
                '            ( "weapon_effet_tag3", Weapon_Mortier_Vasilek_indirect_82mm_towed )'
                '        ]'
                '        + DepictionAction_CriticalFX_Towed'
            ),
        },
    },
}
# fmt: on
