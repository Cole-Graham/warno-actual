"""M3A1 Bradley CFV depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
m3a1_bradley_cfv_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "M3A1_Bradley_CFV_US",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        
        (None, "TacticVehicleDepictionRegistration"): {
            "SubDepictionGenerators": {
                "TransportedInfantrySubGenerator": {
                    "add": None,
                },
            },
        },
    },
}
# fmt: on
