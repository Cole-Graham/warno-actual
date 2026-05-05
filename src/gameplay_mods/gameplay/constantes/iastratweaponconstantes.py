from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gameplay_constantes_iastratweaponconstantes(source_path) -> None:
    """GameData/Gameplay/Constantes/IAStratWeaponConstantes.ndf"""
    logger.info("Editing IAStratWeaponConstantes.ndf")

    ia_strat = source_path.by_n("IAStratWeaponConstantes").v
    
    damage_menace = ia_strat.by_m("DamageWithMenaceForDangerounessArmor").v
    damage_menace.add("DamageFamily_sead_missile_wa")
    damage_menace.add("DamageFamily_missile_he_bigly")
    damage_menace.add("DamageFamily_sa_intermediate")
    damage_menace.add("DamageFamily_sa_full")
    damage_menace.add("DamageFamily_12_7")
    damage_menace.add("DamageFamily_14_5")
    
    always_threaten = ia_strat.by_m("AlwaysThreateningDamageFamily").v
    always_threaten.add("DamageFamily_nplm_bomb_flamme")
    
    attack_threats = ia_strat.by_m("AttackDamageTypeThreat").v
    attack_threats.add("DamageFamily_sa_intermediate")
    attack_threats.add("DamageFamily_sa_full")
    attack_threats.add("DamageFamily_12_7")
    attack_threats.add("DamageFamily_14_5")
