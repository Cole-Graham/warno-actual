from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gameplay_constantes_weaponconstantes(source_path) -> None:
    """GameData/Gameplay/Constantes/WeaponConstantes.ndf"""
    logger.info("Editing WeaponConstantes.ndf")

    weapon_constantes_obj = source_path.by_n("WeaponConstantes").v

    # Add infantry WA to mimetic resistance map
    mimetic_res_map = weapon_constantes_obj.by_m("ResistanceToMimeticImpact").v
    mimetic_res_map.add(f"(ResistanceFamily_infanterieWA, EImpactSurface/Ground)")

    # Add full ball damage to blindages to ignore
    blindages_to_ignore = weapon_constantes_obj.by_m("BlindagesToIgnoreForDamageFamilies").v
    blindages_to_ignore.add(f"(DamageFamily_sa_full, [ResistanceFamily_blindage])")
    blindages_to_ignore.add(f"(DamageFamily_sa_intermediate, [ResistanceFamily_blindage])")
    blindages_to_ignore.add(f"(DamageFamily_thermobarique, [ResistanceFamily_blindage])")

    # Add manpad_hagru damage to blindages to ignore
    blindages_to_ignore.add("(DamageFamily_manpad_hagru, [ResistanceFamily_helico])")
    logger.info("Added manpad_hagru to blindages to ignore")

    # Add manpad_tbagru damage to blindages to ignore
    blindages_to_ignore.add("(DamageFamily_manpad_tbagru, [ResistanceFamily_avion])")
    logger.info("Added manpad_tbagru to blindages to ignore")