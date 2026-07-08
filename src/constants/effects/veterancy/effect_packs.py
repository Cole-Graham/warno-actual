"""Effect-pack namespace wiring and derived-pack metadata."""

from __future__ import annotations

from src.constants.effects.veterancy._schema import PostPatchOverride
from src.constants.effects.veterancy.levels import AVION_VET_REBALANCE_ENABLED

LEVEL_SUFFIXES: tuple[str, ...] = ("rookie", "trained", "veteran", "elite")

# Pack types that keep vanilla HintBodyToken / ingame dictionary text (not mod-overwritten).
PACK_TYPES_VANILLA_LOCALIZATION = frozenset({"SF_v2"})

EFFECT_PACK_SUFFIX_BY_LEVEL: dict[int, str] = {
    0: "rookie",
    1: "trained",
    2: "veteran",
    3: "elite",
}

EFFECT_PACK_BY_PACK_TYPE: dict[str, tuple[str, ...]] = {
    "simple_v3": (
        "UnitEffect_xp_rookie",
        "UnitEffect_xp_trained",
        "UnitEffect_xp_veteran",
        "UnitEffect_xp_elite",
    ),
    "simple_v3_multiplicative": (
        "UnitEffect_xp_rookie_multiplicative",
        "UnitEffect_xp_trained_multiplicative",
        "UnitEffect_xp_veteran_multiplicative",
        "UnitEffect_xp_elite_multiplicative",
    ),
    "SF_v2": (
        "UnitEffect_xp_rookie",
        "UnitEffect_xp_trained_SF",
        "UnitEffect_xp_veteran_SF",
        "UnitEffect_xp_elite_SF",
    ),
    "SF_v2_multiplicative": (
        "UnitEffect_xp_rookie_multiplicative",
        "UnitEffect_xp_trained_SF_multiplicative",
        "UnitEffect_xp_veteran_SF_multiplicative",
        "UnitEffect_xp_elite_SF_multiplicative",
    ),
    "artillery": (
        "UnitEffect_xp_rookie_arty",
        "UnitEffect_xp_trained_arty",
        "UnitEffect_xp_veteran_arty",
        "UnitEffect_xp_elite_arty",
    ),
    "helico": (
        "UnitEffect_xp_rookie_helo",
        "UnitEffect_xp_trained_helo",
        "UnitEffect_xp_veteran_helo",
        "UnitEffect_xp_elite_helo",
    ),
    "helico_attack": (
        "UnitEffect_xp_rookie_helo_attack",
        "UnitEffect_xp_trained_helo_attack",
        "UnitEffect_xp_veteran_helo_attack",
        "UnitEffect_xp_elite_helo_attack",
    ),
    "avion": (
        "UnitEffect_xp_rookie_avion",
        "UnitEffect_xp_trained_avion",
        "UnitEffect_xp_veteran_avion",
        "UnitEffect_xp_elite_avion",
    ),
}

HELO_ATTACK_EFFECT_GUIDS: dict[str, str] = {
    "UnitEffect_xp_rookie_helo_attack": "30d8a0dd-0f87-429b-98e2-098aeb1a0b1e",
    "UnitEffect_xp_trained_helo_attack": "0c48af36-5a1d-401c-9952-ae4351b5f2ac",
    "UnitEffect_xp_veteran_helo_attack": "96e82bfe-107a-44fc-a76d-94a293e4a769",
    "UnitEffect_xp_elite_helo_attack": "fac2b968-dcf7-4e8d-baa1-ac3b79d13976",
}

MULTIPLICATIVE_INFANTRY_GUIDS: dict[str, str] = {
    "xp_rookie": "93c3832b-179f-4f71-9c3e-0aaa51ad6563",
    "xp_trained": "38b2a348-2385-463c-8edb-722a5d9b37f3",
    "xp_trained_SF": "2b3b11d5-f08d-4428-82a2-7307ab6055d9",
    "xp_veteran": "d1b6e97c-24f3-4aec-a457-79c3262cc830",
    "xp_veteran_SF": "f125886e-e9d2-4f30-92d9-700303ccd8c6",
    "xp_elite": "b80fe588-b3b5-4f63-9587-75b254a2361e",
    "xp_elite_SF": "7b707579-3230-4884-a91f-b10dc4df0ddb",
}

ELITE_HELO_SF_GUID = "2967b45d-5b50-48ab-87f7-7ddeeb17f5f4"

# Created at NDF edit time (not present in vanilla EffetsSurUnite.ndf).
RUNTIME_CREATED_EFFECT_PACKS: frozenset[str] = frozenset({
    "UnitEffect_xp_elite_helo_SF",
})

_AVION_REMOVE_EVASION_OVERRIDES: tuple[PostPatchOverride, ...] = (
    PostPatchOverride(
        effect_pack="UnitEffect_xp_veteran_avion",
        remove_evasion_descriptor=True,
    ),
    PostPatchOverride(
        effect_pack="UnitEffect_xp_elite_avion",
        remove_evasion_descriptor=True,
    ),
) if AVION_VET_REBALANCE_ENABLED else ()

POST_PATCH_OVERRIDES: tuple[PostPatchOverride, ...] = (
    PostPatchOverride(
        effect_pack="UnitEffect_xp_veteran_helo",
        precision_stationary=5,
        precision_moving=5,
    ),
    PostPatchOverride(
        effect_pack="UnitEffect_xp_elite_helo",
        precision_stationary=10,
        precision_moving=10,
    ),
    PostPatchOverride(
        effect_pack="UnitEffect_xp_elite_helo_SF",
        suppress_resist_bonus_damage=-40,
        evasion_bonus_precision_when_targeted=-5,
    ),
) + _AVION_REMOVE_EVASION_OVERRIDES
