"""Miscellaneous game constant edits."""

from typing import Any, Dict

from src.utils.logging_utils import setup_logger
from src.constants import NEW_SUPPLY_CONSTANTS as new_supply_constants

logger = setup_logger(__name__)


def edit_constantes_ravitaillement(source_path) -> None:
    """GameData/Gameplay/Constantes/Ravitaillement.ndf"""
    logger.info("Editing Ravitaillement.ndf")

    # Edit standard supply
    standard_supply_descr = source_path.by_n("StandardSupply")
    # standard_supply_descr.v.by_m("FuelSupplyCostBySecond").v = "0.5"
    # standard_supply_descr.v.by_m("HealthSupplyBySecond").v = "0.20"
    # standard_supply_descr.v.by_m("HealthSupplyCostBySecond").v = "3"
    # standard_supply_descr.v.by_m("AmmunitionSupplyBySecond").v = "120"
    # standard_supply_descr.v.by_m("CriticsSupplyBySecond").v = "20"
    vanilla_fuel_supply_by_second = float(standard_supply_descr.v.by_m("FuelSupplyBySecond").v)
    vanilla_fuel_supply_cost_by_second = float(standard_supply_descr.v.by_m("FuelSupplyCostBySecond").v)
    vanilla_health_supply_by_second = float(standard_supply_descr.v.by_m("HealthSupplyBySecond").v)
    vanilla_health_supply_cost_by_second = float(standard_supply_descr.v.by_m("HealthSupplyCostBySecond").v)
    vanilla_ammo_supply_by_second = float(standard_supply_descr.v.by_m("AmmunitionSupplyBySecond").v)
    vanilla_critics_supply_by_second = float(standard_supply_descr.v.by_m("CriticsSupplyBySecond").v)
    vanilla_critics_supply_cost_by_second = float(standard_supply_descr.v.by_m("CriticsSupplyCostBySecond").v)

    expected_vanilla_values = {
        "vanilla_fuel_supply_by_second": 30.0,
        "vanilla_fuel_supply_cost_by_second": 1.5,
        "vanilla_health_supply_by_second": 0.10,
        "vanilla_health_supply_cost_by_second": 3.0,
        "vanilla_ammo_supply_by_second": 60,
        "vanilla_critics_supply_by_second": 10,
        "vanilla_critics_supply_cost_by_second": 20,
    }

    vanilla_values = {
        "vanilla_fuel_supply_by_second": vanilla_fuel_supply_by_second,
        "vanilla_fuel_supply_cost_by_second": vanilla_fuel_supply_cost_by_second,
        "vanilla_health_supply_by_second": vanilla_health_supply_by_second,
        "vanilla_health_supply_cost_by_second": vanilla_health_supply_cost_by_second,
        "vanilla_ammo_supply_by_second": vanilla_ammo_supply_by_second,
        "vanilla_critics_supply_by_second": vanilla_critics_supply_by_second,
        "vanilla_critics_supply_cost_by_second": vanilla_critics_supply_cost_by_second,
    }

    for var_name, vanilla_value in vanilla_values.items():
        value_match = False
        for expected_value_key, expected_value in expected_vanilla_values.items():
            if var_name == expected_value_key and vanilla_value == expected_value:
                value_match = True
                break
        if not value_match:
            logger.warning(
                f"{var_name} value {vanilla_value} is not expected value ({expected_value}), "
                f"Eugen has likely changed this value"
            )

    # create and add new supply descriptors
    for variant_name, settings in new_supply_constants.items():
        variant_descriptor = source_path.by_n("StandardSupply").copy()
        variant_descriptor.namespace = variant_name
        logger.info(f"Adding {variant_name} descriptor")
        # Set common values
        descr_membr = variant_descriptor.v.by_m
        descr_membr("DefaultSupplyRangeGRU").v = str(settings["DefaultSupplyRangeGRU"])

        descr_membr("FuelSupplyBySecond").v = str(vanilla_fuel_supply_by_second * settings["FuelSupplyBySecond"])
        logger.info(f"FuelSupplyBySecond: {descr_membr('FuelSupplyBySecond').v}")

        descr_membr("FuelSupplyCostBySecond").v = str(
            float(vanilla_fuel_supply_cost_by_second * settings["FuelSupplyCostBySecond"])
        )
        logger.info(f"FuelSupplyCostBySecond: {descr_membr('FuelSupplyCostBySecond').v}")

        descr_membr("HealthSupplyBySecond").v = str(vanilla_health_supply_by_second * settings["HealthSupplyBySecond"])
        logger.info(f"HealthSupplyBySecond: {descr_membr('HealthSupplyBySecond').v}")

        descr_membr("HealthSupplyCostBySecond").v = str(
            vanilla_health_supply_cost_by_second * settings["HealthSupplyCostBySecond"]
        )
        logger.info(f"HealthSupplyCostBySecond: {descr_membr('HealthSupplyCostBySecond').v}")

        descr_membr("AmmunitionSupplyBySecond").v = str(
            int(vanilla_ammo_supply_by_second * settings["AmmunitionSupplyBySecond"])  # must be int
        )
        logger.info(f"AmmunitionSupplyBySecond: {descr_membr('AmmunitionSupplyBySecond').v}")

        descr_membr("CriticsSupplyBySecond").v = str(
            vanilla_critics_supply_by_second * settings["CriticsSupplyBySecond"]
        )
        logger.info(f"CriticsSupplyBySecond: {descr_membr('CriticsSupplyBySecond').v}")

        descr_membr("CriticsSupplyCostBySecond").v = str(
            vanilla_critics_supply_cost_by_second * settings["CriticsSupplyCostBySecond"]
        )
        logger.info(f"CriticsSupplyCostBySecond: {descr_membr('CriticsSupplyCostBySecond').v}")

        source_path.add(variant_descriptor)
        logger.info(f"Added {variant_name} descriptor")