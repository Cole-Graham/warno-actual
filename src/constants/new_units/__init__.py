"""New unit definitions."""

import json
from pathlib import Path
from typing import Dict, Any, List, Tuple, Set

from .FR_new_units import FR_NEW_UNITS
from .new_depictions import NEW_DEPICTIONS
from .POL_new_units import POL_NEW_UNITS
from .RDA_new_units import RDA_NEW_UNITS
from .RFA_new_units import RFA_NEW_UNITS
from .SOV_new_units import SOV_NEW_UNITS
from .UK_new_units import UK_NEW_UNITS
from .USA_new_units import USA_NEW_UNITS
from src.utils.logging_utils import setup_logger

logger = setup_logger('new_units')


def _flatten_dict_new_units(data: Any, path: str = "") -> List[Tuple[str, Any]]:
    """Flatten a nested dictionary structure, returning (path, value) pairs."""
    result = []
    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}.{key}" if path else key
            result.extend(_flatten_dict_new_units(value, current_path))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            current_path = f"{path}[{i}]" if path else f"[{i}]"
            result.extend(_flatten_dict_new_units(item, current_path))
    else:
        result.append((path, data))
    return result


def _extract_field_value_new_units(data: Any, field_path: str) -> Any:
    """Extract a field value from nested data structure using dot notation."""
    if not field_path:
        return data
    
    parts = field_path.split(".")
    current = data
    
    for part in parts:
        if isinstance(current, dict) and part in current:
            current = current[part]
        elif isinstance(current, list) and part.startswith("[") and part.endswith("]"):
            try:
                index = int(part[1:-1])
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    return None
            except (ValueError, IndexError):
                return None
        else:
            return None
    
    return current


def _get_unit_name_from_key(key: Any) -> str:
    """Extract unit name from tuple key (unit_name, index) or return string key as-is."""
    if isinstance(key, tuple):
        return key[0]
    return str(key)


def precompute_dependency_graph_new_units(new_units_dict: Dict) -> Dict[str, Set[str]]:
    """Precompute which units depend on which other units."""
    dependencies = {}
    unit_names = set()
    
    # First pass: collect all unit names (excluding reference entries)
    for key in new_units_dict:
        unit_name = _get_unit_name_from_key(key)
        if not unit_name.endswith("_reference"):
            unit_names.add(unit_name)
            dependencies[unit_name] = set()
    
    # Second pass: find dependencies
    for key, unit_data in new_units_dict.items():
        unit_name = _get_unit_name_from_key(key)
        # Skip reference entries
        if unit_name.endswith("_reference"):
            continue
            
        # Find all unit references in this unit's data
        for field_path, field_value in _flatten_dict_new_units(unit_data):
            if isinstance(field_value, str) and field_value in unit_names:
                # Skip fields that should not be treated as references
                if (field_path.endswith("UpgradeFromUnit") or 
                    field_path.endswith("ButtonTexture") or 
                    field_path.endswith("TransportedSoldier") or
                    "[" in field_path):
                    continue
                dependencies[unit_name].add(field_value)
    
    return dependencies


def precompute_circular_references_new_units(dependencies: Dict[str, Set[str]]) -> Set[str]:
    """Precompute which units have circular references."""
    circular_units = set()
    
    def has_cycle(unit: str, visited: Set[str], rec_stack: Set[str]) -> bool:
        visited.add(unit)
        rec_stack.add(unit)
        
        for dep in dependencies.get(unit, set()):
            if dep not in visited:
                if has_cycle(dep, visited, rec_stack):
                    return True
            elif dep in rec_stack:
                circular_units.add(unit)
                return True
        
        rec_stack.remove(unit)
        return False
    
    for unit in dependencies:
        if unit not in circular_units:
            has_cycle(unit, set(), set())
    
    return circular_units


def precompute_resolution_order_new_units(dependencies: Dict[str, Set[str]]) -> List[str]:
    """Precompute optimal order to resolve units (topological sort)."""
    # Count incoming dependencies for each unit
    in_degree = {unit: 0 for unit in dependencies}
    for unit, deps in dependencies.items():
        for dep in deps:
            if dep in in_degree:
                in_degree[dep] += 1
    
    # Start with units that have no dependencies
    queue = [unit for unit, degree in in_degree.items() if degree == 0]
    resolution_order = []
    
    while queue:
        unit = queue.pop(0)
        resolution_order.append(unit)
        
        # Reduce in-degree for all units that depend on this one
        for dep in dependencies.get(unit, set()):
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                queue.append(dep)
    
    # Add any remaining units (those with circular references)
    for unit in dependencies:
        if unit not in resolution_order:
            resolution_order.append(unit)
    
    return resolution_order


def precompute_field_resolution_cache_new_units(new_units_dict: Dict) -> Dict[str, Dict[str, Any]]:
    """Precompute resolved field values for each unit to avoid repeated lookups."""
    # Precompute resolved field values for each unit
    field_cache = {}
    for key, unit_data in new_units_dict.items():
        unit_name = _get_unit_name_from_key(key)
        # Skip reference entries
        if unit_name.endswith("_reference"):
            continue
            
        field_cache[unit_name] = {}
        # Pre-resolve all potential field references
        for field_path, field_value in _flatten_dict_new_units(unit_data):
            if isinstance(field_value, str) and field_value in [_get_unit_name_from_key(k) for k in new_units_dict]:
                # Skip fields that should not be treated as references
                if (field_path.endswith("UpgradeFromUnit") or 
                    field_path.endswith("ButtonTexture") or 
                    field_path.endswith("TransportedSoldier") or
                    "[" in field_path):
                    continue
                # Find the actual key for this unit name
                donor_key = None
                for k in new_units_dict:
                    if _get_unit_name_from_key(k) == field_value:
                        donor_key = k
                        break
                
                if donor_key:
                    donor_unit = new_units_dict[donor_key]
                    # Extract the specific field value from donor unit
                    resolved_value = _extract_field_value_new_units(donor_unit, field_path)
                    if resolved_value is not None:
                        field_cache[unit_name][field_path] = resolved_value
    
    return field_cache


def _resolve_unit_with_cache_new_units(unit_data: Any, unit_name: str, field_cache: Dict[str, Dict[str, Any]], new_units_dict: Dict[Any, Any]) -> Any:
    """Resolve a single unit using precomputed field cache."""
    
    def resolve_value(value: Any, current_path: str = "") -> Any:
        """Recursively resolve a value, handling nested dictionaries and lists."""
        if isinstance(value, dict):
            # Recursively resolve nested dictionaries
            resolved = {}
            for k, v in value.items():
                resolved[k] = resolve_value(v, f"{current_path}.{k}" if current_path else k)
            return resolved
        elif isinstance(value, list):
            # Recursively resolve lists
            return [resolve_value(item, f"{current_path}[{i}]") for i, item in enumerate(value)]
        elif isinstance(value, str):
            # Special exception: UpgradeFromUnit field should not be resolved as references
            if current_path.endswith("UpgradeFromUnit") or current_path.endswith("ButtonTexture"):
                return value
            
            # Special exception: TransportedSoldier field should not be resolved as references
            if current_path.endswith("TransportedSoldier"):
                return value
            
            # Special exception: if we're inside a list (like Transports), these are unit names, not references
            if "[" in current_path:
                return value
            
            # Check if this string references a unit name
            unit_names = [_get_unit_name_from_key(k) for k in new_units_dict]
            if value in unit_names:
                # Check if we have a precomputed field value
                if unit_name in field_cache and current_path in field_cache[unit_name]:
                    logger.debug(f"Using cached field reference '{value}.{current_path.split('.')[-1]}' for path '{current_path}'")
                    return field_cache[unit_name][current_path]
                
                # Find the actual key for this unit name
                referenced_key = None
                for k in new_units_dict:
                    if _get_unit_name_from_key(k) == value:
                        referenced_key = k
                        break
                
                if referenced_key:
                    referenced_value = new_units_dict[referenced_key]
                    
                    # Strict field resolution: extract the specific field from the referenced unit
                    if isinstance(referenced_value, dict):
                        # Extract the field using the current path
                        extracted_value = _extract_field_value_new_units(referenced_value, current_path)
                        if extracted_value is not None:
                            logger.debug(f"Resolving field reference '{value}.{current_path}' for path '{current_path}'")
                            return extracted_value
                    
                    # No fallback - if we can't find the field, raise an error
                    logger.error(f"Failed to resolve field reference '{value}' for path '{current_path}' - field not found in referenced unit")
                    raise ValueError(f"Field '{current_path}' not found in referenced unit '{value}'")
            else:
                # String doesn't reference a unit, return as-is
                return value
        else:
            # Non-string value, return as-is
            return value
    
    return resolve_value(unit_data, "")


def resolve_new_unit_references_optimized(new_units_dict: Dict) -> Dict:
    """
    Optimized version of resolve_new_unit_references with precomputation.
    
    This version precomputes dependency graphs, field resolution caches, and optimal
    resolution order to improve performance, especially for large datasets with many
    shared references.
    """
    logger.info("Precomputing dependency graph and resolution caches for new units...")
    
    # Precompute all the caches and graphs
    dependencies = precompute_dependency_graph_new_units(new_units_dict)
    circular_refs = precompute_circular_references_new_units(dependencies)
    resolution_order = precompute_resolution_order_new_units(dependencies)
    field_cache = precompute_field_resolution_cache_new_units(new_units_dict)
    
    if circular_refs:
        logger.warning(f"Detected circular references in new units: {circular_refs}")
    
    logger.info(f"Resolving {len(resolution_order)} new units in optimal order...")
    
    # Resolve in optimal order using precomputed caches
    resolved_dict = {}
    for unit_name in resolution_order:
        # Find the actual key for this unit name
        unit_key = None
        for k in new_units_dict:
            if _get_unit_name_from_key(k) == unit_name:
                unit_key = k
                break
        
        if unit_key and unit_key in new_units_dict:
            unit_data = new_units_dict[unit_key]
            resolved_data = _resolve_unit_with_cache_new_units(
                unit_data, unit_name, field_cache, new_units_dict
            )
            resolved_dict[unit_key] = resolved_data
    
    # Include any non-reference units that weren't in the resolution order
    for key, unit_data in new_units_dict.items():
        if key not in resolved_dict:
            unit_name = _get_unit_name_from_key(key)
            # Skip reference entries (like Infantry_armor_reference)
            if unit_name.endswith("_reference"):
                continue
            resolved_data = _resolve_unit_with_cache_new_units(
                unit_data, unit_name, field_cache, new_units_dict
            )
            resolved_dict[key] = resolved_data
    
    logger.info(f"Successfully resolved {len(resolved_dict)} new units with optimizations")
    return resolved_dict


def load_new_units() -> Dict:
    """Load and merge all new unit dictionaries with reference resolution."""
    merged_units = {}
    
    logger.info("Loading new unit dictionaries...")
    
    # Combine all new unit definitions
    merged_units = {
        **SOV_NEW_UNITS, 
        **RDA_NEW_UNITS,
        **RFA_NEW_UNITS,
        **POL_NEW_UNITS,
        **UK_NEW_UNITS,
        **USA_NEW_UNITS,
        **FR_NEW_UNITS,
    }
    
    logger.info(f"Loaded {len(merged_units)} new units total")

    # Resolve shared/borrowed values in new units dictionary
    logger.info("Resolving shared values in new units dictionaries...")
    merged_units = resolve_new_unit_references_optimized(merged_units)
    logger.info("Successfully resolved new unit references")
    
    # Save resolved units for debugging (convert tuple keys to strings for JSON serialization)
    logs_dir = Path(__file__).parents[3] / "logs"
    logs_dir.mkdir(exist_ok=True)
    
    # Convert tuple keys to strings for JSON serialization
    json_safe_units = {}
    for key, value in merged_units.items():
        json_key = str(key) if isinstance(key, tuple) else key
        json_safe_units[json_key] = value
    
    with open(logs_dir / "merged_new_units.json", "w") as f:
        json.dump(json_safe_units, f, indent=4)

    return merged_units


# Load new units with reference resolution
NEW_UNITS = load_new_units()

__all__ = [
    "NEW_UNITS",
    "NEW_DEPICTIONS",
    "load_new_units",
]
