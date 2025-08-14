"""Missile weapon definitions."""

from typing import Dict, List, Optional, Tuple, Union

from .a2a import missiles as a2a_missiles
from .aa import missiles as aa_missiles
from .agm import missiles as agm_missiles
from .atgm import missiles as atgm_missiles
from .sead import missiles as sead_missiles

MissileData = Dict[str, Union[Dict, List, int, float, str]]
MissileKey = Tuple[str, str, Optional[str], bool]  # (missile, category, donor, is_new)

# fmt: off
raw_missiles: Dict[MissileKey, MissileData] = {
    **a2a_missiles,
    **aa_missiles,
    **agm_missiles,
    **atgm_missiles,
    **sead_missiles,
}
# fmt: on
