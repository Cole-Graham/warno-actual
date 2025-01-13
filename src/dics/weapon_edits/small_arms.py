"""Small arms weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
weapons: Dict[WeaponKey, WeaponData] = {
    ("Sniper_SVD_Dragunov", "small_arms", None, False): {
        "Ammunition": {
            "Arme": {
                "Family": "DamageFamily_sniper",
            },
            "hit_roll": {
                "BaseCriticModifier": 0,
                "Idling": 65,
            },
            "parent_membr": {
                "TempsEntreDeuxTirs": 6.0,
                "TempsEntreDeuxFx": 6.0,
                "PhysicalDamages": 1.0,
                "SuppressDamages": 100.0,
                "PorteeMaximaleGRU": 1050,
                "PorteeMaximaleTBAGRU": 875,
                "DisplaySalveAccuracy": False,
                "TempsDeVisee": 6.0,
                "NbTirParSalves": 10,
                "AffichageMunitionParSalve": 10
            },
        },
        "BaseSupplyCost": 2,
        "NbWeapons": [1],
        "WeaponDescriptor": {
            "Salves": 10,
        },
    },
    # Continue with other small arms...
}
# fmt: on 