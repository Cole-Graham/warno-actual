"""HvyScout_SOV depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
hvyscout_sov: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "HvyScout_SOV",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_HvyScout_SOV", None): {
            1: ("edit", [("MeshDescriptor", "PKM")]),
        },
        
        ("AllWeaponSubDepiction_HvyScout_SOV", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "MMG_PKM_7_62mm")]),
            },
        },
        
        ("TacticDepiction_HvyScout_SOV_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("insert", [("mmg", "WeaponAlternative_2")]),
            },
        },
    },
}
# fmt: on
