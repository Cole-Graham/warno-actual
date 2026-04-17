"""Functions for modifying damage modules."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gameplay_unit_damagemodules(source_path) -> None:
    """GameData/Gameplay/Unit/DamageModules.ndf"""
    logger.info("Modifying damage modules")
    
    # Airplane
    source_path.by_n("Airplane_StunDamagesRegen").v = "1" # vanilla is 9999
    source_path.by_n("Airplane_MaxStunDamages").v = "350" # vanilla is 9999
    
    # Helico
    source_path.by_n("Helico_MaxStunDamages").v = "350" # vanilla is 450
    