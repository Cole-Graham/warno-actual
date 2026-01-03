"""Airborne_half_Dragon_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
airborne_half_dragon_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Airborne_half_Dragon_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Airborne_half_Dragon_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            1: ("edit", [("MeshDescriptor", "M240B")]), # (selector_id or mesh)
        },
    }
}
# fmt: on
