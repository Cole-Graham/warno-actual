"""Airmobile_Mot_UK depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
airmobile_mot_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Airmobile_Mot_UK",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Airmobile_Mot_UK", None): {
            # Vanilla: [0]=L85, [1]=L86A1_LSW, [2]=Carl_Gustav
            1: ("edit", [("MeshDescriptor", "L7A2")]),
        },

        ("AllWeaponSubDepiction_Airmobile_Mot_UK", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("edit", [("FireEffectTag", "MMG_inf_L7A2_7_62mm")]),
            },
        },

        ("TacticDepiction_Airmobile_Mot_UK_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("insert", [("mmg", "WeaponAlternative_2")]),
            },
        },
    },
}
# fmt: on
