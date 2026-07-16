"""Pattern standard: strength for dedicated ATGM infantry teams."""

from typing import TypedDict

# TypeCategoryName token for ANTI-TANK MISSILE (ammunition.json Value).
ATGM_TYPE_CATEGORY_TOKEN = "JTOYRAARTS"

VERYHEAVY_EQUIP_SPECIALTY = "infantry_equip_veryheavy"


class AtgmInfantryTeamStrengthPatternStandard(TypedDict):
    """Soldier count / HP for dedicated ATGM infantry teams by equip specialty."""

    veryheavy_strength: int
    default_strength: int
    type_category_token: str
    veryheavy_specialty: str


ATGM_INFANTRY_TEAM_STRENGTH_PATTERN_STANDARD: AtgmInfantryTeamStrengthPatternStandard = {
    "veryheavy_strength": 4,
    "default_strength": 3,
    "type_category_token": ATGM_TYPE_CATEGORY_TOKEN,
    "veryheavy_specialty": VERYHEAVY_EQUIP_SPECIALTY,
}
