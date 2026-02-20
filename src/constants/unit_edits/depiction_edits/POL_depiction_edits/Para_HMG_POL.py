"""Para_HMG_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
para_hmg_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Para_HMG_POL",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Para_HMG_POL", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            2: ("edit", [("MeshDescriptor", "RPG7V")]), # (selector_id or mesh)
        },

        ("AllWeaponSubDepiction_Para_HMG_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("edit", [("FireEffectTag", "FireEffect_RocketInf_RPG7")]),
            },
        },
    }
}
# fmt: on