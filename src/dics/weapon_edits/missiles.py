"""Missile edit definitions."""

from typing import Dict, List, Optional, Tuple, Union

MissileData = Dict[str, Union[Dict, List, int, float, str]]
MissileKey = Tuple[str, str, Optional[str], bool]  # (missile, category, donor, is_new)

# fmt: off
missiles: Dict[MissileKey, MissileData] = {
    ("ATGM_TOW2", "atgm", None, False): {
        "MissileDescriptor": {
            "MaxSpeedGRU": 875,
            "MaxAccelerationGRU": 875,
        },
    },
    # ... more missiles ...
}
# fmt: on 