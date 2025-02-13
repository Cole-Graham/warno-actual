"""Miscellaneous game constant edits."""

from typing import Any, Dict

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

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
    
    # Edit standard supply
    standard_supply_descr = source_path.by_n("StandardSupply").v
    standard_supply_descr.by_m("FuelSupplyCostBySecond").v = "0.5"
    standard_supply_descr.by_m("HealthSupplyBySecond").v = "0.20"
    standard_supply_descr.by_m("HealthSupplyCostBySecond").v = "3"
    standard_supply_descr.by_m("AmmunitionSupplyBySecond").v = "120"
    standard_supply_descr.by_m("CriticsSupplyBySecond").v = "20"
    
    logger.info("Updated standard supply values")
    
    # Create and add specialized supply descriptors
    supply_variants = {
        "FOBSupply": {"range": "1000"},
        "HeloSupply": {"range": "700"},
        "SmallHeloSupply": {"range": "550"}
    }
    
    for variant_name, settings in supply_variants.items():
        variant_descr = source_path.by_n("StandardSupply").copy()
        variant_descr.namespace = variant_name
        
        # Set common values
        variant_descr.v.by_m("DefaultSupplyRangeGRU").v = settings["range"]
        variant_descr.v.by_m("FuelSupplyCostBySecond").v = "0.5"
        variant_descr.v.by_m("HealthSupplyBySecond").v = "0.20"
        variant_descr.v.by_m("HealthSupplyCostBySecond").v = "6"
        variant_descr.v.by_m("AmmunitionSupplyBySecond").v = "120"
        variant_descr.v.by_m("CriticsSupplyBySecond").v = "20"
        
        source_path.add(variant_descr)
        logger.info(f"Added {variant_name} descriptor")
