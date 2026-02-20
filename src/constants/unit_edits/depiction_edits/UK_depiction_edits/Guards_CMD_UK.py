"""Guards_CMD_UK depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
guards_cmd_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Guards_CMD_UK",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Guards_CMD_UK", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            2: ("edit", [("MeshDescriptor", "LAW_80")]),
        },

        ("AllWeaponSubDepiction_Guards_CMD_UK", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("edit", [("FireEffectTag", "RocketInf_LAW_80")]),
            },
        },
    }
}
# fmt: on
