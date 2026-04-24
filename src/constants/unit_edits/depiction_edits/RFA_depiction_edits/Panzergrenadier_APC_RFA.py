"""Panzergrenadier_APC_RFA depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
panzergrenadier_apc_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Panzergrenadier_APC_RFA",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Panzergrenadier_APC_RFA", None): {
            2: ("edit", [("MeshDescriptor", "Panzerfaust_3")]),
        },
        
        ("AllWeaponSubDepiction_Panzergrenadier_APC_RFA", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("edit", [("FireEffectTag", "RocketInf_PzF_3")]),
            },
        },
        
        ("TacticDepiction_Panzergrenadier_APC_RFA_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                1: ("insert", [("bazooka", "WeaponAlternative_3")]),
            },
        },
    },
}
# fmt: on
