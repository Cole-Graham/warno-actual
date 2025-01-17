"""Miscellaneous game constant edits."""

from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_orders(source_path):
    """Edit unit order availability.
    
    Args:
        source_path: The NDF file being edited
    """
    logger.info("Editing OrderAvailability_Tactic.ndf")
    
    unit_edits = load_unit_edits()
    
    for unit, edits in unit_edits.items():
        if "orders" not in edits:
            continue
            
        for order_list in source_path:
            if order_list.namespace != f"Descriptor_OrderAvailability_{unit}":
                continue
                
            if "add_orders" in edits["orders"]:
                for order in edits["orders"]["add_orders"]:
                    if order == "sell":
                        order_list.v.insert(1, "'Sell'")
                        logger.info(f"Added 'Sell' order to {unit}")
                    else:
                        order_list.v.add(f"'{order}'")
                        logger.info(f"Added '{order}' order to {unit}")
                        
            if "remove_orders" in edits["orders"]:
                for order in order_list.v:
                    if order in edits["orders"]["remove_orders"]:
                        order_list.v.remove(order.index)
                        logger.info(f"Removed {order} order from {unit}")
