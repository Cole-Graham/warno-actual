"""Fallschirmjager_Metys_DDR depiction edits (auto-generated draft)."""

from typing import Dict, Tuple, Union

# fmt: off
fallschirmjager_metys_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Fallschirmjager_Metys_DDR",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Fallschirmjager_Metys_DDR", None): {
            0: ("edit", [("MeshDescriptor", "AKs74U")]),
        },
        
        ("AllWeaponSubDepiction_Fallschirmjager_Metys_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                0: ("edit", [("FireEffectTag", "PM_MPi_AKSU_74NK")]),
            },
        },
        
        ("TacticDepiction_Fallschirmjager_Metys_DDR_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("insert", [("smg", "WeaponAlternative_1")]),
            },
        },
    },
}
# fmt: on
