"""Rifles_HMG_POL depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
rifles_hmg_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Rifles_HMG_POL",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Rifles_HMG_POL", None): {
            3: ("edit", [("MeshDescriptor", "RPG7V")]),
        },
        
        ("AllWeaponSubDepiction_Rifles_HMG_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                3: ("edit", [("FireEffectTag", "RocketInf_RPG7VL")]),
            },
        },
    },
}
# fmt: on
