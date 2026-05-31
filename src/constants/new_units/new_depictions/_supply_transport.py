"""Shared depiction edits for supply-transport clone units."""

from typing import Dict, Tuple, Union


def towed_supply_vehicle_depiction(unit_name: str) -> Dict[str, Dict[Union[str, Tuple[str, str]], dict]]:
    return {
        "unit_name": unit_name,
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
