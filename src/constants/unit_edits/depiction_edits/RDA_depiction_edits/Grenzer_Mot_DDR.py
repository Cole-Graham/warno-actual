"""Grenzer_Mot_DDR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
grenzer_mot_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Grenzer_Mot_DDR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Grenzer_Mot_DDR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            1: ("insert", [("SelectorId", "WeaponAlternative_2"), ("MeshDescriptor", "RPK")]),
            2: ("edit", [("ReferenceMeshForSkeleton", "RPK")]),
        },

        ("AllWeaponSubDepiction_Grenzer_Mot_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                1: ("insert", [("FireEffectTag", "SAW_lMG_K_7_62mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_2")]),
            },
        },
    }
}
# fmt: on
