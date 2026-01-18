"""Functions for modifying team properties."""

from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_type, find_obj_by_namespace

logger = setup_logger(__name__)


def edit_gameplay_unit_team(source_path) -> None:
    """GameData/Gameplay/Unit/Tactic/Team.ndf

    Edit Airport supply rates.
    """
    logger.info("Modifying Team.ndf")
    
    # TacticProductionQueue (Controls time between unit spawns)
    tactic_production_queue = find_obj_by_namespace(source_path, "TacticProductionQueue")
    _handle_tactic_production_queue(tactic_production_queue)
    
    # Main descriptor
    tactict_teamunit_descr = find_obj_by_namespace(source_path, "Tactic_TeamUnitDescriptor")
    modules_list = tactict_teamunit_descr.v.by_m("ModulesDescriptors")
    
    # Airport module
    team_airport_module = find_obj_by_type(modules_list.v, "TTeamAirportModuleDescriptor")
    _handle_team_airport_module(team_airport_module)


# TacticProductionQueue
def _handle_tactic_production_queue(tactic_production_queue) -> None:
    """GameData/Gameplay/Unit/Tactic/Team.ndf

    Edit time between unit spawns.
    """
    pass


# TTeamAirportModuleDescriptor
def _handle_team_airport_module(team_airport_module) -> None:
    """GameData/Gameplay/Unit/Tactic/Team.ndf

    Edit fuel, repair, and ammo airport supply rates.
    """
    
    """ Vanilla WARNO rates are too low, but we don't want to use Wargame's rates 
    because aircraft are less expensive and more numerous in WARNO.
    
    Wargame = 2.5 seconds of TOT per second of refueling (Based on Canadian CF-188)
    Vanilla WARNO = 1 second of TOT per second of refueling
    WARNO ACTUAL = 1.91 seconds of TOT per second of refueling """

    # 76.5% of Wargame's fuel rate
    new_fuel_rate = "19.125"  # Vanilla rate = 10
    team_airport_module.v.by_m("FuelSupplyAmountBySecond").v = new_fuel_rate
    logger.info(f"Set airport fuel supply rate to {new_fuel_rate}/second")

    # 76.5% of Wargame's repair rate
    new_health_rate = "0.023"  # Vanilla rate = 0.0198
    team_airport_module.v.by_m("HealthSupplyAmountBySecond").v = new_health_rate
    logger.info(f"Set airport health supply rate to {new_health_rate}/second")

    """ For ammo we just use 1:1 with wargame, because I feel like fighters or 
    bombers that are undamaged after a mission are often so because they are
    being used conservatively and/or defensively. """
    
    """ Wargame's airport ammo resupply rate is 35 per second, but the supply costs
    are also much higher. e.g. 1 Kh-58U SEAD missile costs 3250 supply in Wargame. """

    # Roughly equivalent to 1:1 ammo supply rate, comparing the time to resupply 4 AMRAAMs
    # in wargame and warno actual.
    new_ammo_rate = "2"
    team_airport_module.v.by_m("AmmunitionSupplyAmountBySecond").v = new_ammo_rate
    logger.info(f"Set airport ammunition supply rate to {new_ammo_rate}/second")
    
    