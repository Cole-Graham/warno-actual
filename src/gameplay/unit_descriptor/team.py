"""Functions for modifying team properties."""

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_team_supply(source_path) -> None:
    """GameData/Gameplay/Unit/Tactic/Team.ndf"""
    logger.info("Modifying team supply rates")

    for descr_row in source_path:
        if descr_row.namespace != "Tactic_TeamUnitDescriptor":
            continue

        modules_list = descr_row.v.by_m("ModulesDescriptors").v
        for module in modules_list:
            if not hasattr(module.v, "type"):
                continue

            if module.v.type != "TTeamAirportModuleDescriptor":
                continue

            """ Vanilla WARNO rates are too low, but we don't want to use Wargame's rates 
            because aircraft are less expensive and more numerous in WARNO.
            
            Wargame = 2.5 seconds of TOT per second of refueling (Based on Canadian CF-188)
            Vanilla WARNO = 1 second of TOT per second of refueling
            WARNO ACTUAL = 1.91 seconds of TOT per second of refueling """

            # 76.5% of Wargame's fuel rate
            new_fuel_rate = "19.125"  # Vanilla rate = 10
            module.v.by_m("FuelSupplyAmountBySecond").v = new_fuel_rate
            logger.info(f"Set airport fuel supply rate to {new_fuel_rate}/second")

            # 76.5% of Wargame's repair rate
            new_health_rate = "0.023"  # Vanilla rate = 0.0198
            module.v.by_m("HealthSupplyAmountBySecond").v = new_health_rate
            logger.info(f"Set airport health supply rate to {new_health_rate}/second")

            """ For ammo we just use 1:1 with wargame, because I feel like fighters or 
            bombers that are undamaged after a mission are often so because they are
            being used conservatively and/or defensively. """

            # Roughly equivalent to 1:1 ammo supply rate, comparing the time to resupply 4 AMRAAMs
            new_ammo_rate = "2"
            module.v.by_m("AmmunitionSupplyAmountBySecond").v = new_ammo_rate
            logger.info(f"Set airport ammunition supply rate to {new_ammo_rate}/second")
