"""Typed structures for veterancy level definitions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

ModifierMode = Literal["flat", "multiplicative"]


@dataclass(frozen=True)
class LevelBonuses:
    """Semantic veterancy stats for one experience level."""

    body_token: str
    level_key: str
    effect_pack: str | None = None
    stress_recovery: float | None = None
    aim_time_reduction_pct: int | None = None
    salvo_reload_reduction_pct: int | None = None
    shot_reload_reduction_pct: int | None = None
    accuracy_pct: int | None = None
    precision_moving_pct: int | None = None
    stress_resistance_pct: int | None = None
    physical_damage_reduction_pct: int | None = None
    movement_speed_pct: int | None = None
    evasion_pct: int | None = None
    add_evasion_descriptor: bool = False
    uses_dispersion_for_accuracy: bool = False


@dataclass(frozen=True)
class PackConfig:
    """Per experience-pack metadata for NDF effect mapping."""

    pack_type: str
    level_format: str
    modifier_mode: ModifierMode = "flat"
    uses_dispersion_for_accuracy: bool = False


@dataclass(frozen=True)
class PostPatchOverride:
    """Values applied after the main veterancy patch pass."""

    effect_pack: str
    precision_stationary: int | None = None
    precision_moving: int | None = None
    suppress_resist_bonus_damage: int | None = None
    evasion_bonus_precision_when_targeted: int | None = None
    remove_evasion_descriptor: bool = False
