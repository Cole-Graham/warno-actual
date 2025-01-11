from typing import Any

from src import ndf
from src.utils.logging_utils import setup_logger

# Set up logger
logger = setup_logger('ndf_utils')

def find_namespace(row: Any, prefix: str, edits: dict) -> dict:
    """Find edits for a given namespace."""
    if not hasattr(row, 'namespace'):
        return None
        
    # Get unit name without prefix
    unit_name = row.namespace.replace(prefix, "")
    
    # Return edits if they exist
    return edits.get(unit_name)


def is_obj_type(item: Any, item_type: str) -> bool:
    """Check if an NDF object is of a specific type.
    
    Args:
        item: The item to check
        item_type: The expected NDF object type
        
    Returns:
        bool: True if item is an NDF object of the specified type
    """
    return isinstance(item, ndf.model.Object) and item.type == item_type