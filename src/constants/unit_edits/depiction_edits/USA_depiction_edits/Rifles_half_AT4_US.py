"""Rifles_half_AT4_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
rifles_half_at4_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Rifles_half_AT4_US",
    "valid_files": ["DepictionInfantry.ndf", "WeaponDescriptor.ndf"],
    "DepictionInfantry_ndf": {
        
        ("AllWeaponAlternatives_Rifles_half_AT4_US", None): { # (namespace, object type)
            # row: (edit type, [(property, value), (property, value), ...]) (edit types: "edit", "add", "remove", "replace")
            2: ("edit", [("MeshDescriptor", "M240B")]), # (selector_id or mesh)
        },
    }
}
# fmt: on
