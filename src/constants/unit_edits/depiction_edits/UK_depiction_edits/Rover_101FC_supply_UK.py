"""Rover_101FC_supply_UK depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
rover_101fc_supply_uk: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "Rover_101FC_supply_UK",
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
