"""Engineers_Geb_RFA_RFA depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
engineers_geb_rfa_rfa: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Engineers_Geb_RFA_RFA",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Engineers_Geb_RFA_RFA", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            1: ("remove", [("MeshDescriptor", "MG3")]),
            1: ("edit", [("SelectorId", "WeaponAlternative_2")]),
        },

        ("AllWeaponSubDepiction_Engineers_Geb_RFA_RFA", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("remove", [("FireEffectTag", "Grenade_Satchel_Charge")]),
                1: ("edit", [("FireEffectTag", "Grenade_Satchel_Charge"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
            },
        },

        ("TacticDepiction_Engineers_Geb_RFA_RFA_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("edit", [("smg", "WeaponAlternative_1")]),
                1: ("edit", [("grenade", "WeaponAlternative_2")]),
            },
        },
    }
}
# fmt: on