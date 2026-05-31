"""TRM_2000_supply_FR depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
trm_2000_supply_fr: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "TRM_2000_supply_FR",
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
