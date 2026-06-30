"""grenade weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Grenade_Satchel_Charge", "grenade", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TraitsToken": ['STAT', 'HE', 'CAC'],
                "PhysicalDamages": 1.5,
            },
        },
    },
}
# fmt: on
