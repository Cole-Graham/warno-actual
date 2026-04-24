"""HvyScout_RPG7VL_DDR depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
hvyscout_rpg7vl_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "HvyScout_RPG7VL_DDR",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_HvyScout_RPG7VL_DDR", None): {
            2: ("edit", [("MeshDescriptor", "RPG7V")]),
        },
        
        ("AllWeaponSubDepiction_HvyScout_RPG7VL_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("edit", [("FireEffectTag", "RocketInf_RPG7VL")]),
            },
        },
    },
}
# fmt: on
