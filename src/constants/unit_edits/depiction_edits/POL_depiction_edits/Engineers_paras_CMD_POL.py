"""Engineers_paras_CMD_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
engineers_paras_cmd_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Engineers_paras_CMD_POL",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Engineers_paras_CMD_POL", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("edit", [("MeshDescriptor", "RPG7V")]), # (selector_id or mesh)
            2: ("edit", [("ReferenceMeshForSkeleton", "RPG7V")]),
        },

        ("AllWeaponSubDepiction_Engineers_paras_CMD_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "FireEffect_RocketInf_RPG7")]),
            },
        },
    }
}
# fmt: on