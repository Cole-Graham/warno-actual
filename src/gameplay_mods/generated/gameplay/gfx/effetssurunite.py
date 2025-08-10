"""Functions for modifying EffetsSurUnite.ndf"""

from src.constants.effects.capacities import (
    CHOC_MOVE_EFFECT,
    CHOC_MOVE_OK_EFFECT,
    NO_CHOC_MOVE_EFFECT,
    NO_CHOC_MOVE_MORALE_EFFECT,
    NO_SWIFT_EFFECT,
    SWIFT_EFFECT,
    SWIFT_OK_EFFECT,
    DEPLOY_EFFECT,
    DEPLOY_OK_EFFECT,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_effetssurunite(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/EffetsSurUnite.ndf"""
    logger.info("Modifying unit effects")

    # Add new shock effects
    for i, row in enumerate(source_path, start=1):
        if row.namespace == "UnitEffect_Choc":
            source_path.insert(i, CHOC_MOVE_EFFECT)
            source_path.insert(i, NO_CHOC_MOVE_EFFECT)
            source_path.insert(i, NO_CHOC_MOVE_MORALE_EFFECT)
            source_path.insert(i, SWIFT_EFFECT)
            source_path.insert(i, NO_SWIFT_EFFECT)
            source_path.insert(i, CHOC_MOVE_OK_EFFECT)
            source_path.insert(i, SWIFT_OK_EFFECT)
            source_path.insert(i, DEPLOY_OK_EFFECT)
            source_path.insert(i, DEPLOY_EFFECT)
            logger.info("Added shock movement effects")
            break

    # Modify sniper effects
    sniper_obj = source_path.by_n("UnitEffect_sniper")
    effects_list = sniper_obj.v.by_m("EffectsDescriptors")

    for effect in effects_list.v:
        if not hasattr(effect.v, "type"):
            continue

        if effect.v.type == "TUnitEffectIncreaseWeaponPhysicalDamagesDescriptor":
            effects_list.v.remove(effect.index)
            logger.info(f"Removed sniper damage bonus from {sniper_obj.v.parent_row.namespace}")
            break

    # Modify stress on miss
    stress_on_miss_objects = [
        ("UnitEffect_stressOnMiss_high", 140),
        ("UnitEffect_stressOnMiss_low", 80),
        ("UnitEffect_stressOnMiss_mid", 110),
    ]

    # Edit stress on miss effects
    for effect_name, suppress_damage in stress_on_miss_objects:
        stress_on_miss_obj = source_path.by_n(effect_name)
        effects_list = stress_on_miss_obj.v.by_m("EffectsDescriptors")
        for effect in effects_list.v:
            if not hasattr(effect.v, "type"):
                continue

            if effect.v.type == "TEffectInflictSuppressDamageDescriptor":
                effect.v.by_m("SuppressDamageValue").v = str(suppress_damage)
                logger.info(f"Updated {effect_name.replace('UnitEffect_', '')} effect to "
                            f"{suppress_damage}")
                break