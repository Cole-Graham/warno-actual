from typing import Any, List
from uuid import uuid4

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

def get_module_value(obj: Any, module_name: str, field_name: str) -> Any:
    """Get a value from a module's field."""
    try:
        return obj.v.by_m(module_name).v.by_m(field_name).v
    except Exception:
        return None

def get_module_list(obj: Any, module_name: str) -> List[Any]:
    """Get a list from a module."""
    try:
        return obj.v.by_m(module_name).v
    except Exception:
        return []

def get_resource_value(obj: Any, resource_key: str) -> Any:
    """Get a value from a resource dictionary."""
    try:
        return obj.by_k(resource_key).v
    except Exception:
        return None

def strip_quotes(value: str) -> str:
    """Strip both single and double quotes from a string value."""
    return value.strip("'").strip('"')

def is_valid_turret(turret: Any) -> bool:
    """Check if turret is a valid type."""
    return any([
        is_obj_type(turret, "TTurretBombardierDescriptor"),
        is_obj_type(turret, "TTurretInfanterieDescriptor"),
        is_obj_type(turret, "TTurretTwoAxisDescriptor"),
        is_obj_type(turret, "TTurretUnitDescriptor")
    ])
    
def _generate_guid():
    """Generate a new GUID."""
    return str(uuid4())