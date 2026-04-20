from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gameplay_constantes_weaponconstantes(source_path) -> None:
    """GameData/Gameplay/Constantes/WeaponConstantes.ndf"""
    logger.info("Editing WeaponConstantes.ndf")

    weapon_constantes_obj = source_path.by_n("WeaponConstantes").v
    
    # Add sead_missile_wa to SuppressDamagePerFamily
    suppress_damage_per_family = weapon_constantes_obj.by_m("SuppressDamagePerFamily").v
    suppress_damage_per_family.add(
        '(\n'
        '      DamageFamily_sead_missile_wa,\n'
        '      TDamageTypeRTTI\n'
        '      (\n'
        '          Family = DamageFamily_suppressap\n'
        '          Index = 1\n'
        '      )\n'
        ')\n'
    )
    
    # Add sead_missile_wa to PierceBonusForDamageFamilies
    pierce_bonus_for_damage_families = weapon_constantes_obj.by_m("PierceBonusForDamageFamilies").v
    pierce_bonus_for_damage_families.add(f"(DamageFamily_sead_missile_wa, 31)")

    # Add infantry WA to mimetic resistance map
    mimetic_res_map = weapon_constantes_obj.by_m("ResistanceToMimeticImpact").v
    mimetic_res_map.add(f"(ResistanceFamily_infanterieWA, EImpactSurface/Ground)")
    
    # Add sead_missile_wa to DamageTypeToMimeticProjectile
    damage_type_to_mimetic_projectile = weapon_constantes_obj.by_m("DamageTypeToMimeticProjectile").v
    damage_type_to_mimetic_projectile.add(f"(DamageFamily_sead_missile_wa, EImpactProjectile/APShell)")

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

    # SAM and A2A hagru/tbagru variants follow the same plane/helo split as MANPADs
    blindages_to_ignore.add("(DamageFamily_sam_hagru, [ResistanceFamily_helico])")
    blindages_to_ignore.add("(DamageFamily_sam_tbagru, [ResistanceFamily_avion])")
    blindages_to_ignore.add("(DamageFamily_a2a_hagru, [ResistanceFamily_helico])")
    blindages_to_ignore.add("(DamageFamily_a2a_tbagru, [ResistanceFamily_avion])")
    logger.info("Added sam/a2a hagru and tbagru to blindages to ignore")