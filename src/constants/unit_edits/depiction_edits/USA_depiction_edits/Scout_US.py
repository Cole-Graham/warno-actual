"""Scout_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
scout_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Scout_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Scout_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("edit", [("MeshDescriptor", "M249")]), # (selector_id or mesh)
        },

        ("AllWeaponSubDepiction_Scout_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "SAW_M249_5_56mm")]),
            },
        },
    }
}
# fmt: on
