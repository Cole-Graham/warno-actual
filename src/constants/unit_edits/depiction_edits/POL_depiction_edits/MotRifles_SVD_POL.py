"""MotRifles_SVD_POL depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
motrifles_svd_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "MotRifles_SVD_POL",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_MotRifles_SVD_POL", None): {
            3: ("edit", [("MeshDescriptor", "RPG7V")]),
        },
        
        ("AllWeaponSubDepiction_MotRifles_SVD_POL", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                3: ("edit", [("FireEffectTag", "RocketInf_RPG7VL")]),
            },
        },
    },
}
# fmt: on
