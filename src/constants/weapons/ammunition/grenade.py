"""grenade weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Grenade_Satchel_Charge", "grenade", None, False): {
        "Ammunition": {
            "parent_membr": {
                "TraitsToken": ['STAT', 'CAC', 'HEAT'],
                "PhysicalDamages": 1.5,
                "RadiusSplashSuppressDamagesGRU": 235,
            },
        },
    },
    
    ("Grenade_Satchel_Charge_AT", "grenade", "Grenade_Satchel_Charge", True): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_ap_missile",
                "Index": 7,
            },
            "parent_membr": {
                "TraitsToken": ['STAT', 'CAC', 'HEAT'],
                "RadiusSplashPhysicalDamagesGRU": 25,
                "RadiusSplashSuppressDamagesGRU": 50,
                "PhysicalDamages": 1.0,
                "ShowDamageInUI": False,
            },
        },
    },
}
# fmt: on
