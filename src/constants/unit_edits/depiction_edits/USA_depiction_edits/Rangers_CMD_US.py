"""Rangers_CMD_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
rangers_cmd_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Rangers_CMD_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Rangers_CMD_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove", "replace")
            2: ("edit", [("MeshDescriptor", "Carl_Gustav_M2")]), # (selector_id or mesh)
            3: ("remove", []),
        },

        ("AllWeaponSubDepiction_Rangers_CMD_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("edit", [("FireEffectTag", "RocketInf_Carl_Gustav")]),
                3: ("remove", []),
            },
        },
        
        ("TacticDepiction_Rangers_CMD_US_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                1: ("insert", [("bazooka", "WeaponAlternative_3")]),
            },
        },
    }
}
# fmt: on
