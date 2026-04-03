from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gameplay_constantes_iastratweaponconstantes(source_path) -> None:
    """GameData/Gameplay/Constantes/IAStratWeaponConstantes.ndf"""
    logger.info("Editing IAStratWeaponConstantes.ndf")

    ia_strat = source_path.by_n("IAStratWeaponConstantes").v
    damage_menace = ia_strat.by_m("DamageWithMenaceForDangerounessArmor").v
    damage_menace.add("DamageFamily_sead_missile_wa")
    damage_menace.add("DamageFamily_12_7")
    damage_menace.add("DamageFamily_14_5")
    
    attack_threats = ia_strat.by_m("AttackDamageTypeThreat").v
    attack_threats.add("DamageFamily_12_7")
    attack_threats.add("DamageFamily_14_5")
