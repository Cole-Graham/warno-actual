"""Pattern standard: WA infantry Blindage for squads (not HMG/AT weapon teams)."""

from typing import Sequence, TypedDict

INFANTRY_WA_ARMOR_FAMILY = "ResistanceFamily_infanterieWA"
VANILLA_INFANTRY_ARMOR_FAMILY = "ResistanceFamily_infanterie"

# Dedicated AT teams: exclude via live TagSet (covers RCL_* / AT_* names without ATteam_).
EXCLUDED_AT_TEAM_TAG = "Infanterie_AT"

# Dedicated HMG / MMG teams stay on vanilla infantry Blindage (no unique Infanterie_* tag).
EXCLUDED_WEAPON_TEAM_PREFIXES: tuple[str, ...] = (
    "HMGteam_",
    "MMGteam_",
)

# Live Blindage Family values that may be rewritten to WA.
REWRITABLE_INFANTRY_ARMOR_FAMILIES: frozenset[str] = frozenset({
    VANILLA_INFANTRY_ARMOR_FAMILY,
    INFANTRY_WA_ARMOR_FAMILY,
})


class InfantryArmorPatternStandard(TypedDict):
    """WA family + strength-scaled Index for Infanterie squads."""

    armor_family: str
    strength_index_base: int
    excluded_at_team_tag: str
    excluded_prefixes: Sequence[str]
    rewritable_families: frozenset[str]


INFANTRY_ARMOR_PATTERN_STANDARD: InfantryArmorPatternStandard = {
    "armor_family": INFANTRY_WA_ARMOR_FAMILY,
    "strength_index_base": 15,
    "excluded_at_team_tag": EXCLUDED_AT_TEAM_TAG,
    "excluded_prefixes": EXCLUDED_WEAPON_TEAM_PREFIXES,
    "rewritable_families": REWRITABLE_INFANTRY_ARMOR_FAMILIES,
}


def infantry_wa_armor_index(strength: int, base: int = 15) -> int:
    """Index = max(base - strength, 1)."""
    return max(base - strength, 1)


def is_excluded_hmg_team_unit(
    unit_name: str,
    excluded_prefixes: Sequence[str] = EXCLUDED_WEAPON_TEAM_PREFIXES,
) -> bool:
    """True for dedicated HMG/MMG teams by name prefix."""
    lower = unit_name.lower()
    for prefix in excluded_prefixes:
        if unit_name.startswith(prefix) or lower.startswith(prefix.lower()):
            return True
    return False


# Back-compat alias used by tests / callers that still import the old name.
def is_excluded_weapon_team_unit(
    unit_name: str,
    excluded_prefixes: Sequence[str] = EXCLUDED_WEAPON_TEAM_PREFIXES,
) -> bool:
    return is_excluded_hmg_team_unit(unit_name, excluded_prefixes)
