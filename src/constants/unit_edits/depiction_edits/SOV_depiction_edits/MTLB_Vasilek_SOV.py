"""MTLB_Vasilek_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
mtlb_vasilek_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MTLB_Vasilek_SOV",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        ("DepictionOperator_MTLB_Vasilek_SOV_Weapon1", "DepictionOperator_WeaponInstantFire"): { # (Namespace (can be None), Object type)
            "copy": "DepictionOperator_MTLB_Vasilek_SOV_Weapon4", # new namespace, this entry is a donor for a new entry
            "FireEffectTag": "'weapon_effet_tag4'",
            "WeaponShootDataPropertyName": ["'WeaponShootData_0_4'"]
        },
        
        ("TacticDepiction_MTLB_Vasilek_SOV", "TacticVehicleDepictionDesc"): {
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
