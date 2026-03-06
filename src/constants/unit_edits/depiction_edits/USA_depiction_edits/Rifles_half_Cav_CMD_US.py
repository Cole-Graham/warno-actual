"""Rifles_half_Cav_CMD_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
rifles_half_cav_cmd_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Rifles_half_Cav_CMD_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Rifles_half_Cav_CMD_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("edit", [("MeshDescriptor", "AT_4")]), # (selector_id or mesh)
        },

        ("AllWeaponSubDepiction_Rifles_half_Cav_CMD_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "RocketInf_AT4_83mm")]),
            },
        },
    }
}
# fmt: on
