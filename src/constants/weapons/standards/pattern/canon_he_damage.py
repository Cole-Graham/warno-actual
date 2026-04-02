"""Canon HE (PhysicalDamages) standards by caliber token and namespace exceptions."""

from typing import Dict, List

CANON_HE_DAMAGE_BY_CALIBER: Dict[str, float] = {
    "'BMQJOXODMC'": 1.25,  # 105mm
    "'PTAGBRTCDY'": 1.4,   # 115mm
    "'DYWXTLDKWR'": 1.5,   # 120mm
    "'GPFACVPVNW'": 1.6,   # 125mm
}

CANON_HE_DAMAGE_EXCEPTIONS: List[str] = [
    "Ammo_Canon_HE_73_mm_SPG9",
    "Ammo_Canon_HE_73_mm_SPG9_TOWED",
]
