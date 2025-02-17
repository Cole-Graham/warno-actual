"""Ranger_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
ranger_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Ranger_US",
    "valid_files": ["GeneratedDepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "GeneratedDepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Ranger_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            2: ("edit", [("MeshDescriptor", "AT_4")]), # (selector_id or mesh)
        },

        ("AllWeaponSubDepiction_Ranger_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("edit", [("FireEffectTag", "RocketInf_AT4_83mm")]),
            },
        },
    }
}
# fmt: on
