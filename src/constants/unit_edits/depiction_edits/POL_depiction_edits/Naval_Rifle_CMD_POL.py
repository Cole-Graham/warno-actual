"""Naval_Rifle_CMD_POL depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
naval_rifle_cmd_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Naval_Rifle_CMD_POL",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Naval_Rifle_CMD_POL", None): {
            1: ("edit", [("MeshDescriptor", "RPG7V")]),
        },
        
        ("AllWeaponSubDepiction_Naval_Rifle_CMD_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "RocketInf_RPG7VL")]),
            },
        },
    },
}
# fmt: on
