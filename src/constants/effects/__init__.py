"""Re-exports for unit effect descriptor fragments."""

from .medium_equip_penalty_effects import (
    MEDIUM_EQUIP_PENALTY_EFFECT,
)
from .deploy_effects import DEPLOY_EFFECT, DEPLOY_OK_EFFECT
from .sprint_effects import NO_SPRINT_MORALE_EFFECT, SPRINT_EFFECT
from .swift_effects import NO_SWIFT_EFFECT, SWIFT_EFFECT, SWIFT_OK_EFFECT

CHOC_CQC_BONUSES = {
    "aim_time_multiplier": 0.70,
    "salvo_reload_multiplier": 0.70,
    "shot_reload_percentage": -30,
}

CHOC_SPRINT_BONUSES = {
    "suppress_damage_multiplier": 0.75,
    "speed_bonus_percentage": 70,
}

__all__ = [
    "CHOC_CQC_BONUSES",
    "NO_SPRINT_MORALE_EFFECT",
    "SPRINT_EFFECT",
    "MEDIUM_EQUIP_PENALTY_EFFECT",
    "DEPLOY_EFFECT",
    "DEPLOY_OK_EFFECT",
    "NO_SWIFT_EFFECT",
    "SWIFT_EFFECT",
    "SWIFT_OK_EFFECT",
]
