"""M812_supply_US depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
m812_supply_us: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "M812_supply_US",
    "valid_files": ["DepictionVehicles.ndf"],
    "DepictionVehicles_ndf": {
        (None, "TacticVehicleDepictionRegistration"): {
            "SubDepictionGenerators": {
                "TowedUnitSubDepictionGenerator": {
                    "add": None,
                },
            },
        },
    },
}
# fmt: on
