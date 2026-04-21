"""TOS1_Buratino_SOV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
tos1_buratino_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "TOS1_Buratino_SOV",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        "new_objects": {
            "weapon2": """
                DepictionOperator_TOS1_Buratino_SOV_Weapon5 is DepictionOperator_WeaponInstantFire
                (
                    FireEffectTag = 'weapon_effet_tag2'
                    WeaponShootDataPropertyName = ['WeaponShootData_0_2', 'WeaponShootData_1_2', 'WeaponShootData_2_2', 'WeaponShootData_3_2']
                    NbProj = 4
                )
            """,
        },
        
        (None, "TacticVehicleDepictionRegistration"): {
            "SubDepictions": {
                0: {
                    "Depiction": {
                        "Operators": { 
                            11: ("add", (
                                "DepictionOperator_TOS1_Buratino_SOV_Weapon2"
                            )),
                        },
                        "Actions": {
                            3: ("add", (
                                '('
                                '    "weapon_effet_tag2",'
                                '    Weapon_SMOKE_Vehicle_Grenadex8'
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
