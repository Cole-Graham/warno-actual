"""Miscellaneous game constant edits."""

from typing import Any, Dict

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def edit_gen_gp_gfx_orderavailabilitytactic(source_path, game_db: Dict[str, Any]):
    """GameData/Generated/Gameplay/Gfx/OrderAvailability_Tactic.ndf

    Args:
        source_path: The NDF file being edited
        game_db: Game database containing unit data
    """
    logger.info("Editing OrderAvailability_Tactic.ndf")

    unit_edits = load_unit_edits()

    for order_list in source_path:
        if not hasattr(order_list, "namespace"):
            continue

        # Get unit name from descriptor
        unit_name = order_list.namespace.replace("Descriptor_OrderAvailability_", "")

        # Handle existing unit edits
        if unit_name in unit_edits and "orders" in unit_edits[unit_name]:
            if "add_orders" in unit_edits[unit_name]["orders"]:
                for order in unit_edits[unit_name]["orders"]["add_orders"]:
                    if order == "EOrderType/Sell":
                        order_list.v.insert(1, "EOrderType/Sell")
                        logger.info(f"Added EOrderType/Sell order to {unit_name}")
                    else:
                        order_list.v.add(f"{order}")
                        logger.info(f"Added {order} order to {unit_name}")

            if "remove_orders" in unit_edits[unit_name]["orders"]:
                for order in order_list.v:
                    if order in unit_edits[unit_name]["orders"]["remove_orders"]:
                        order_list.v.remove(order.index)
                        logger.info(f"Removed {order} order from {unit_name}")

        # If unit has add_capacities, ensure UseCapacite order is present
        if unit_name in unit_edits:
            add_capacities = unit_edits[unit_name].get("capacities", {}).get("add_capacities", [])
            if add_capacities:
                has_use_capacite = any(
                    getattr(o, "v", o) == "EOrderType/UseCapacite" for o in order_list.v
                )
                if not has_use_capacite:
                    order_list.v.add("EOrderType/UseCapacite")
                    logger.info(f"Added EOrderType/UseCapacite order to {unit_name} (has add_capacities)")

        # Remove sell order from supply units
        if unit_name in game_db["unit_data"]:
            unit_data = game_db["unit_data"][unit_name]
            if unit_data.get("is_supply_unit", False):
                # Find and remove sell order
                for i, order in enumerate(order_list.v):
                    if order.v == "EOrderType/Sell":
                        order_list.v.remove(i)
                        logger.info(f"Removed EOrderType/Sell order from supply unit {unit_name}")
                        break

    # Create new order entries for new units
    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits or "orders" not in edits:
            logger.warning(f"No orders found for {donor}")
            continue

        unit_name = edits["NewName"]
        orders_str = str(edits["orders"]).replace("'", "")
        new_entry = f"Descriptor_OrderAvailability_{unit_name} is {orders_str}"
        source_path.add(new_entry)
        logger.info(f"Added new order entry for {unit_name}")