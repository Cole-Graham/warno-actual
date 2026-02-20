"""Scout_para_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
scout_para_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Scout_para_POL",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Scout_para_POL", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "Dragunov")]),
        },

        ("AllWeaponSubDepiction_Scout_para_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "FireEffect_Sniper_SVD_Dragunov"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
            },
        },
    }
}
# fmt: on