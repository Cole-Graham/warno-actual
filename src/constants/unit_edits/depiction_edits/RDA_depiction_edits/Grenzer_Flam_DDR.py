"""Grenzer_Flam_DDR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
grenzer_flam_ddr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Grenzer_Flam_DDR",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        ("AllWeaponAlternatives_Grenzer_Flam_DDR", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove")
            # always insert and/or remove first, then define the rest based on adjusted indices
            2: ("insert", [("SelectorId", "WeaponAlternative_3"), ("MeshDescriptor", "RPK")]),
        },

        ("AllWeaponSubDepiction_Grenzer_Flam_DDR", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                2: ("insert", [("FireEffectTag", "SAW_lMG_K_7_62mm"), ("WeaponShootDataPropertyName", "WeaponShootData_0_3")]),
            },
        },
    }
}
# fmt: on