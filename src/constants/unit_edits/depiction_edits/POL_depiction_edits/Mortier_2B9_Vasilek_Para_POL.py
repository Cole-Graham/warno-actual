"""Mortier_2B9_Vasilek_Para_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
mortier_2b9_vasilek_para_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Mortier_2B9_Vasilek_Para_POL",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        "new_objects": {
            "weapon3": """
                DepictionOperator_Mortier_2B9_Vasilek_Para_POL_Weapon3 is DepictionOperator_WeaponInstantFire
                (
                    FireEffectTag = 'weapon_effet_tag3'
                    Anchors = ["fx_tourelle1_tir_01"]
                    WeaponShootDataPropertyName = ['WeaponShootData_0_3']
                    NbProj = 1
                )
            """,
        },
        
        (None, "TacticVehicleDepictionRegistration"): {
            "Operators": {
                7: ("add", (
                    "DepictionOperator_Mortier_2B9_Vasilek_Para_POL_Weapon3"
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
