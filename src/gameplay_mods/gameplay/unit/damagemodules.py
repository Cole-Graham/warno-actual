"""Functions for modifying damage modules."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gameplay_unit_damagemodules(source_path) -> None:
    """GameData/Gameplay/Unit/DamageModules.ndf"""
    logger.info("Modifying damage modules")
    
    # Airplane
    source_path.by_n("Airplane_StunDamagesRegen").v = "1" # vanilla is 9999
    # Mt = 255 (stun threshold = r * Mt = 178.5) is paired with the bumped
    # AA_SUPPRESS_BY_PHYSICAL_DAMAGE table so every "must stun" case clears the
    # threshold by >= 11 written suppress -- enough headroom for the 1 stun/sec
    # regen between non-salvo missile hits. "Must NOT stun" cases stay >= 18
    # under the threshold. SPAAGs use a separate he_dca_airtargets ammo with a
    # 2/3 W ratio to avoid over-stunning at this Mt.
    source_path.by_n("Airplane_MaxStunDamages").v = "255" # vanilla is 9999
    
    # Helico
    source_path.by_n("Helico_MaxStunDamages").v = "250" # vanilla is 450
    