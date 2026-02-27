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
            1: ("remove", [("MeshDescriptor", "MMG_PKM_7_62mm")]),
            1: ("edit", [("SelectorId", "WeaponAlternative_2")]),
        },

        ("AllWeaponSubDepiction_Engineers_Geb_RFA_RFA", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("remove", [("FireEffectTag", "MMG_PKM_7_62mm")]),
                1: ("edit", [("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
            },
        },

        ("TacticDepiction_Engineers_Geb_RFA_RFA_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": {
                0: ("remove", [("mmg", "WeaponAlternative_2")]),
                0: ("edit", [("grenade", "WeaponAlternative_2")]),
            },
        },
    }
}
# fmt: on