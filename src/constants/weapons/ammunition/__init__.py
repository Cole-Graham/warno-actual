"""Ammunition weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

from .autocanon import weapons as autocanon_weapons
from .autocanon_dca import weapons as autocanon_dca_weapons
from .bomb import weapons as bomb_weapons
from .canon import weapons as canon_weapons
from .howitzer import weapons as howitzer_weapons
from .mlrs import weapons as mlrs_weapons
from .mortier import weapons as mortier_weapons
from .rocket import weapons as rocket_weapons
from .rocketinf import weapons as rocketinf_weapons
from .small_arms import weapons as small_arms_weapons

WeaponData = Dict[str, Union[Dict, List, int, float, str]]
WeaponKey = Tuple[str, str, Optional[str], bool]  # (weapon, category, donor, is_new)

# fmt: off
ammunitions: Dict[WeaponKey, WeaponData] = {
    **autocanon_weapons,
    **autocanon_dca_weapons,
    **bomb_weapons,
    **canon_weapons,
    **howitzer_weapons,
    **mlrs_weapons,
    **mortier_weapons,
    **rocket_weapons,
    **rocketinf_weapons,
    **small_arms_weapons,
}
# fmt: on 