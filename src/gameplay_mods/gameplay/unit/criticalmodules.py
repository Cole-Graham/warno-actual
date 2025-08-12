"""Functions for modifying critical effect modules."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_unit_template_critical(source) -> None:
    """GameData/Gameplay/Unit/CriticalModules/TemplateCriticalEffectModules.ndf"""
    logger.info("Modifying critical effect template")

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


def edit_unit_airplane_critical(source) -> None:
    """ ______________________________PLACEHOLDER_______________________________
    GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Airplane.ndf"""
    # logger.info("Modifying airplane critical effect modules")
    pass


def edit_unit_groundunit_critical(source) -> None:
    """ ______________________________PLACEHOLDER_______________________________
    GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_GroundUnit.ndf"""
    # logger.info("Modifying ground unit critical effect modules")
    pass


def edit_unit_helico_critical(source) -> None:
    """ ______________________________PLACEHOLDER_______________________________
    GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Helico.ndf"""
    # logger.info("Modifying helicopter critical effect modules")
    pass


def edit_unit_infanterie_critical(source) -> None:
    """ ______________________________PLACEHOLDER_______________________________
    GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_Infanterie.ndf"""
    # logger.info("Modifying infantry critical effect modules")
    pass


def edit_unit_testunits_critical(source) -> None:
    """ ______________________________PLACEHOLDER_______________________________
    GameData/Gameplay/Unit/CriticalModules/CriticalEffectModule_TestUnits.ndf"""
    # logger.info("Modifying critical effect test units")
    pass