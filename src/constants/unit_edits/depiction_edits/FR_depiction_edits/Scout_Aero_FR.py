"""Scout_Aero_FR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
scout_aero_fr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Scout_Aero_FR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Scout_Aero_FR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "LRAC_F1")]),
            2: ("edit", [("ReferenceMeshForSkeleton", "LRAC_F1")]),
        },

        ("AllWeaponSubDepiction_Scout_Aero_FR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "RocketInf_LRAC_F1"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
            },
        },

        ("TacticDepiction_Scout_Aero_FR_Soldier", "TemplateInfantryDepictionFactoryTactic"): {
            "Operators": { # usually (always?) editing conditional tags submember
                0: ("insert", [("bazooka", "WeaponAlternative_2")]),
            }
        },
    }
}
# fmt: on
