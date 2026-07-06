"""Veterancy balance constants — single source of truth for UI hints and NDF patches."""

from src.constants.effects.veterancy.build import (
    SEMANTIC_FIELD_TO_PATCH_KEYS,
    build_helo_attack_effect_changes,
    build_runtime_effect_changes,
    build_veterancy_bonuses,
    build_veterancy_effect_changes,
)
from src.constants.effects.veterancy.effect_packs import (
    EFFECT_PACK_BY_PACK_TYPE,
    ELITE_HELO_SF_GUID,
    HELO_ATTACK_EFFECT_GUIDS,
    MULTIPLICATIVE_INFANTRY_GUIDS,
    POST_PATCH_OVERRIDES,
    RUNTIME_CREATED_EFFECT_PACKS,
)
from src.constants.effects.veterancy.levels import AVION_VET_REBALANCE_ENABLED, PACK_CONFIGS, PACK_LEVELS

VETERANCY_BONUSES = build_veterancy_bonuses()
VETERANCY_EFFECT_CHANGES = build_veterancy_effect_changes()
VETERANCY_HELO_ATTACK_EFFECT_CHANGES = build_helo_attack_effect_changes()
VETERANCY_RUNTIME_EFFECT_CHANGES = build_runtime_effect_changes()

__all__ = [
    "AVION_VET_REBALANCE_ENABLED",
    "EFFECT_PACK_BY_PACK_TYPE",
    "ELITE_HELO_SF_GUID",
    "HELO_ATTACK_EFFECT_GUIDS",
    "MULTIPLICATIVE_INFANTRY_GUIDS",
    "PACK_CONFIGS",
    "PACK_LEVELS",
    "POST_PATCH_OVERRIDES",
    "RUNTIME_CREATED_EFFECT_PACKS",
    "SEMANTIC_FIELD_TO_PATCH_KEYS",
    "VETERANCY_BONUSES",
    "VETERANCY_EFFECT_CHANGES",
    "VETERANCY_HELO_ATTACK_EFFECT_CHANGES",
    "VETERANCY_RUNTIME_EFFECT_CHANGES",
]
