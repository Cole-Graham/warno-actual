"""Miscellaneous game constant edits."""

from typing import Any, Dict

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger
from src.constants import NEW_SUPPLY_CONSTANTS as new_supply_constants

logger = setup_logger(__name__)

def edit_orders(source_path, game_db: Dict[str, Any]):
    """Edit OrderAvailability_Tactic.ndf.
    
    Args:
        source_path: The NDF file being edited
        game_db: Game database containing unit data
    """
    logger.info("Editing OrderAvailability_Tactic.ndf")
    
    unit_edits = load_unit_edits()
    
    for order_list in source_path:
        if not hasattr(order_list, 'namespace'):
            continue
            
        # Get unit name from descriptor
        unit_name = order_list.namespace.replace("Descriptor_OrderAvailability_", "")
        
        # Handle existing unit edits
        if unit_name in unit_edits and "orders" in unit_edits[unit_name]:
            if "add_orders" in unit_edits[unit_name]["orders"]:
                for order in unit_edits[unit_name]["orders"]["add_orders"]:
                    if order == "sell":
                        order_list.v.insert(1, "'Sell'")
                        logger.info(f"Added 'Sell' order to {unit_name}")
                    else:
                        order_list.v.add(f"'{order}'")
                        logger.info(f"Added '{order}' order to {unit_name}")
                        
            if "remove_orders" in unit_edits[unit_name]["orders"]:
                for order in order_list.v:
                    if order in unit_edits[unit_name]["orders"]["remove_orders"]:
                        order_list.v.remove(order.index)
                        logger.info(f"Removed {order} order from {unit_name}")
        
        # Remove sell order from supply units
        if unit_name in game_db["unit_data"]:
            unit_data = game_db["unit_data"][unit_name]
            if unit_data.get("is_supply_unit", False):
                # Find and remove sell order
                for i, order in enumerate(order_list.v):
                    if order.v == "'Sell'":
                        order_list.v.remove(i)
                        logger.info(f"Removed 'Sell' order from supply unit {unit_name}")
                        break
        
    # Create new order entries for new units
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits or "Orders" not in edits:
            logger.warning(f"No orders found for {donor}")
            continue
            
        unit_name = edits["NewName"]
        orders_str = str(edits["Orders"])
        new_entry = f"Descriptor_OrderAvailability_{unit_name} is {orders_str}"
        source_path.add(new_entry)
        logger.info(f"Added new order entry for {unit_name}")

def edit_ravitaillement(source_path) -> None:
    """Edit supply values in Ravitaillement.ndf."""
    logger.info("Editing Ravitaillement.ndf")
    
    source_path.by_n("SpecificDefaultSupplyRangeGRU").v = "450" # vanilla = 442
    
    # Edit standard supply
    standard_supply_descr = source_path.by_n("StandardSupply")
    # standard_supply_descr.v.by_m("FuelSupplyCostBySecond").v = "0.5"
    # standard_supply_descr.v.by_m("HealthSupplyBySecond").v = "0.20"
    # standard_supply_descr.v.by_m("HealthSupplyCostBySecond").v = "3"
    # standard_supply_descr.v.by_m("AmmunitionSupplyBySecond").v = "120"
    # standard_supply_descr.v.by_m("CriticsSupplyBySecond").v = "20"
    vanilla_supply_by_second = float(standard_supply_descr.v.by_m("FuelSupplyBySecond").v)
    vanilla_supply_cost_by_second = float(standard_supply_descr.v.by_m("FuelSupplyCostBySecond").v)
    vanilla_health_supply_by_second = float(standard_supply_descr.v.by_m("HealthSupplyBySecond").v)
    vanilla_health_supply_cost_by_second = float(standard_supply_descr.v.by_m("HealthSupplyCostBySecond").v)
    vanilla_ammo_supply_by_second = float(standard_supply_descr.v.by_m("AmmunitionSupplyBySecond").v)
    vanilla_critics_supply_by_second = float(standard_supply_descr.v.by_m("CriticsSupplyBySecond").v)
    vanilla_critics_supply_cost_by_second = float(standard_supply_descr.v.by_m("CriticsSupplyCostBySecond").v)
    
    vanilla_values_to_compare = [
        30.0, # FuelSupplyBySecond
        1.5,  # FuelSupplyCostBySecond
        0.10, # HealthSupplyBySecond
        3.0,  # HealthSupplyCostBySecond
        60,   # AmmunitionSupplyBySecond
        10,   # CriticsSupplyBySecond
        20,   # CriticsSupplyCostBySecond
    ]
    
    vanilla_values = {
        'vanilla_supply_by_second': vanilla_supply_by_second,
        'vanilla_supply_cost_by_second': vanilla_supply_cost_by_second,
        'vanilla_health_supply_by_second': vanilla_health_supply_by_second,
        'vanilla_health_supply_cost_by_second': vanilla_health_supply_cost_by_second,
        'vanilla_ammo_supply_by_second': vanilla_ammo_supply_by_second,
        'vanilla_critics_supply_by_second': vanilla_critics_supply_by_second,
        'vanilla_critics_supply_cost_by_second': vanilla_critics_supply_cost_by_second
    }
    
    for var_name, vanilla_value in vanilla_values.items():
        for value in vanilla_values_to_compare:
            if vanilla_value == value:
                continue
            else:
                logger.warning(f"{var_name} value {vanilla_value} is not expected value ({value}), "
                               f"Eugen has likely changed this value")
    
    # create and add new supply descriptors
    for variant_name, settings in new_supply_constants.items():
        variant_descriptor = source_path.by_n("StandardSupply").copy()
        variant_descriptor.namespace = variant_name
        logger.info(f"Adding {variant_name} descriptor")
        # Set common values
        descr_membr = variant_descriptor.v.by_m
        descr_membr("DefaultSupplyRangeGRU").v = str(settings["DefaultSupplyRangeGRU"])
        
        descr_membr("FuelSupplyBySecond").v = str(
            vanilla_supply_by_second * settings["FuelSupplyBySecond"])
        logger.info(f"FuelSupplyBySecond: {descr_membr('FuelSupplyBySecond').v}")
        
        descr_membr("FuelSupplyCostBySecond").v = str(float(
            vanilla_supply_cost_by_second * settings["FuelSupplyCostBySecond"]))
        logger.info(f"FuelSupplyCostBySecond: {descr_membr('FuelSupplyCostBySecond').v}")
        
        descr_membr("HealthSupplyBySecond").v = str(
            vanilla_health_supply_by_second * settings["HealthSupplyBySecond"])
        logger.info(f"HealthSupplyBySecond: {descr_membr('HealthSupplyBySecond').v}")
        
        descr_membr("HealthSupplyCostBySecond").v = str(
            vanilla_health_supply_cost_by_second * settings["HealthSupplyCostBySecond"])
        logger.info(f"HealthSupplyCostBySecond: {descr_membr('HealthSupplyCostBySecond').v}")
        
        descr_membr("AmmunitionSupplyBySecond").v = str(int( # must be int
            vanilla_ammo_supply_by_second * settings["AmmunitionSupplyBySecond"]))
        logger.info(f"AmmunitionSupplyBySecond: {descr_membr('AmmunitionSupplyBySecond').v}")
        
        descr_membr("CriticsSupplyBySecond").v = str(
            vanilla_critics_supply_by_second * settings["CriticsSupplyBySecond"])
        logger.info(f"CriticsSupplyBySecond: {descr_membr('CriticsSupplyBySecond').v}")
        
        descr_membr("CriticsSupplyCostBySecond").v = str(
            vanilla_critics_supply_cost_by_second * settings["CriticsSupplyCostBySecond"])
        logger.info(f"CriticsSupplyCostBySecond: {descr_membr('CriticsSupplyCostBySecond').v}")

        source_path.add(variant_descriptor)

