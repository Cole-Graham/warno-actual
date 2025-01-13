"""Functions for modifying team properties."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_team_supply(source) -> None:
    """Edit team supply rates in Team.ndf."""
    logger.info("Modifying team supply rates")
    
    for descr_row in source:
        if descr_row.namespace != "Tactic_TeamUnitDescriptor":
            continue
            
        modules_list = descr_row.v.by_m("ModulesDescriptors").v
        for module in modules_list:
            if not hasattr(module.v, 'type'):
                continue
                
            if module.v.type != "TTeamAirportModuleDescriptor":
                continue
                
            module.v.by_m("AmmunitionSupplyAmountBySecond").v = "2"
            logger.info("Set airport ammunition supply rate to 2/second") 