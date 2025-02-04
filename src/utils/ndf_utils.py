import re
from typing import Any, Dict, List, Optional, Pattern, Union
from uuid import uuid4

from src import ndf
from src.utils.logging_utils import setup_logger

# Set up logger
logger = setup_logger('ndf_utils')


def find_namespace(row: Any, edits: Dict, prefix: str = "", suffix: str = "",
                   pattern: Optional[Union[str, Pattern]] = None) -> Optional[Dict]:
    """Find edits for a given namespace.
    
    Args:
        row: The row to check namespace of
        edits: Dictionary of edits to search in
        prefix: Optional prefix to remove from namespace
        suffix: Optional suffix to remove from namespace
        pattern: Optional regex pattern to extract name
        
    Returns:
        Dict of edits if found, None otherwise
    """
    try:
        if not hasattr(row, 'namespace'):
            return None
            
        namespace = row.namespace
        
        # If pattern provided, use regex matching
        if pattern:
            if isinstance(pattern, str):
                pattern = re.compile(pattern)
            match = pattern.search(namespace)
            if match:
                name = match.group(1)
            else:
                return None
        else:
            # Otherwise use prefix/suffix removal
            name = namespace
            if prefix and name.startswith(prefix):
                name = name[len(prefix):]
            if suffix and name.endswith(suffix):
                name = name[:-len(suffix)]
        
        # Debug logging
        logger.debug(f"Looking for edits for unit: {name}")
        logger.debug(f"Available edit keys: {list(edits.keys())}")
        
        # Return edits if they exist
        if name in edits:
            logger.debug(f"Found edits for {name}")
            return edits[name]
        else:
            logger.debug(f"No edits found for {name}")
            return None
            
    except Exception as e:
        logger.error(f"Error in find_namespace: {str(e)}")
        return None


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
    except Exception:  # noqa
        return None


def get_modules_list(obj: Any, module_name: str) -> List[Any]:
    """Get a list from a module.
    
    Args:
        obj: NDF object containing the module
        module_name: Name of the module containing the list
        
    Returns:
        The module list if found, empty list otherwise
        
    Example:
        module_list = get_modules_list(unit_descr, "ModulesDescriptors")
        for module in module_list.v:
            # module.v contains the actual module object
    """
    try:
        # Only access .v once to get the module list
        return obj.by_m(module_name)
    except Exception as e:
        logger.error(f"Error getting module list for {obj.namespace}: {e}")
        return []


def get_key_value(obj: Any, resource_key: str) -> Any:
    """Get a value from a resource dictionary."""
    try:
        return obj.by_k(resource_key).v
    except Exception as e:
        logger.error(f"Error getting key value for {obj.namespace}: {e}")
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


def generate_guid():
    """Generate a new GUID."""
    return str(uuid4())
