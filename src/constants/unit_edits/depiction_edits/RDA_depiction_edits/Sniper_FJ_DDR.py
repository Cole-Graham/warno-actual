"""Sniper_FJ_DDR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
sniper_fj_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Sniper_FJ_DDR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Sniper_FJ_DDR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "RPG18")]),
            3: ("edit", [("ReferenceMeshForSkeleton", "RPG18")]),
        },

        ("AllWeaponSubDepiction_Sniper_FJ_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("insert", [("FireEffectTag", "RocketInf_RPG18_64mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },
    }
}
# fmt: on
