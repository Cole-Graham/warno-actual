"""Functions for modifying critical effect modules."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_critical_effects(source) -> None:
    """GameData/Gameplay/Unit/CriticalModules/TemplateCriticalEffectModules.ndf

    Removes BailedOut critical effect from vehicle effect packs.
    """
    logger.info("Modifying critical effect modules")

    effect_packs = {
        "PackEffetCritique_VehiculeSansTourelle": "vehicles without turret",
        "PackEffetCritique_VehiculeStandard": "standard vehicles",
        "PackEffetCritique_VehiculeNonArme": "unarmed vehicles",
    }

    for pack_name, description in effect_packs.items():
        effects_list = source.by_n(pack_name).v

        for effect in effects_list:
            if effect.v.type == "CriticalEffect_BailedOut":
                effects_list.remove(effect.index)
                logger.info(f"Removed BailedOut effect from {description}")
                break
