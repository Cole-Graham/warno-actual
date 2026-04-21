"""MTLB_Vasilek_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
mtlb_vasilek_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MTLB_Vasilek_SOV",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        "new_objects": {
            "weapon4": """
                DepictionOperator_MTLB_Vasilek_SOV_Weapon4 is DepictionOperator_WeaponInstantFire
                (
                    FireEffectTag = 'weapon_effet_tag4'
                    Anchors = ["fx_tourelle1_tir_01"]
                    WeaponShootDataPropertyName = ['WeaponShootData_0_4']
                    NbProj = 1
                )
            """,
        },
        
        (None, "TacticVehicleDepictionRegistration"): {
            "SubDepictions": {
                0: {
                    "Depiction": {
                        "Operators": { 
                            4: ("add", (
                                "DepictionOperator_MTLB_Vasilek_SOV_Weapon4"
                            )),
                        },
                        "Actions": {
                            3: ("add", (
                                '('
                                '    "weapon_effet_tag4",'
                                '    Weapon_Mortier_Vasilek_indirect_82mm'
                                ')'
                            )),
                        },
                    },
                },
            },
        },
    },
}
# fmt: on
