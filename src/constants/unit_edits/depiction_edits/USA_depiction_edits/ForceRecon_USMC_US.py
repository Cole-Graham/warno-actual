"""ForceRecon_USMC_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
forcerecon_usmc_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "ForceRecon_USMC_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_ForceRecon_USMC_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "insert", "remove", "replace")
            3: ("edit", [("MeshDescriptor", "AT_4")]), # (selector_id or mesh)
        },

        ("AllWeaponSubDepiction_ForceRecon_USMC_US", "TemplateAllSubWeaponDepiction"): {
            "Operators": {
                3: ("edit", [("FireEffectTag", "RocketInf_AT4_83mm")]),
            },
        },
    }
}
# fmt: on
