"""Engineers_CMD_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
engineers_cmd_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Engineers_CMD_POL",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Engineers_CMD_POL", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("edit", [("MeshDescriptor", "PKM")]), # (selector_id or mesh)
            2: ("edit", [("ReferenceMeshForSkeleton", "PKM")]),
        },

        ("AllWeaponSubDepiction_Engineers_CMD_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "MMG_PKM_7_62mm")]),
            },
        },

        ("TacticDepiction_Engineers_CMD_POL_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": { # usually (always?) editing conditional tags submember
                0: ("replace", [("mmg", "MeshAlternative_2")]),
            }
        },
    }
}
# fmt: on
