"""Engineers_Geb_RFA_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
engineers_geb_rfa_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Engineers_Geb_RFA_RFA",
    "valid_files": ["DepictionInfantry.ndf"],
    "DepictionInfantry_ndf": {
        # Vanilla: 0 G3A4/WA_1, 1 MG3/WA_2, 2 MainNue/WA_3, 3 meshless
        # Target:  Uzi/WA_1, satchel/WA_3 (MG3 removed; WA ids not renumbered)
        ("AllWeaponAlternatives_Engineers_Geb_RFA_RFA", None): {
            0: ("edit", [("MeshDescriptor", "Uzi")]),
            1: ("remove", []),
        },

        ("AllWeaponSubDepiction_Engineers_Geb_RFA_RFA", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                0: ("edit", [("FireEffectTag", "PM_uzi")]),
                1: ("remove", []),
            },
        },

        # Vanilla ConditionalTags: [mmg/WA_2, grenade/WA_3]
        # Target:                  [smg/WA_1, grenade/WA_3]
        ("TacticDepiction_Engineers_Geb_RFA_RFA_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("edit", [("smg", "WeaponAlternative_1")]),
            },
        },
    }
}
# fmt: on
