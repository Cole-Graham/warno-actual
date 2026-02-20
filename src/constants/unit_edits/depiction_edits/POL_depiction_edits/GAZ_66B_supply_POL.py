"""GAZ_66B_supply_POL depiction edits."""

from typing import Dict, Tuple, Union

# fmt: off
gaz_66b_supply_pol: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {
    "unit_name": "GAZ_66B_supply_POL",
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
