"""Unit edit constants."""

import importlib
import os
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple, Set

from src.utils.logging_utils import setup_logger

logger = setup_logger('dics')


def _flatten_dict(data: Any, path: str = "") -> List[Tuple[str, Any]]:
    """Flatten a nested dictionary structure, returning (path, value) pairs."""
    result = []
    if isinstance(data, dict):
        for key, value in data.items():
            current_path = f"{path}.{key}" if path else key
            result.extend(_flatten_dict(value, current_path))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            current_path = f"{path}[{i}]" if path else f"[{i}]"
            result.extend(_flatten_dict(item, current_path))
    else:
        result.append((path, data))
    return result


def _extract_field_value(data: Any, field_path: str) -> Any:
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


def precompute_dependency_graph(unit_edits_dict: Dict) -> Dict[str, Set[str]]:
    """Precompute which units depend on which other units."""
    dependencies = {}
    unit_names = set()
    
    # First pass: collect all unit names (excluding reference entries)
    for unit_name in unit_edits_dict:
        if not unit_name.endswith("_reference"):
            unit_names.add(unit_name)
            dependencies[unit_name] = set()
    
    # Second pass: find dependencies
    for unit_name, unit_data in unit_edits_dict.items():
        # Skip reference entries
        if unit_name.endswith("_reference"):
            continue
            
        # Find all unit references in this unit's data
        for field_path, field_value in _flatten_dict(unit_data):
            if isinstance(field_value, str) and field_value in unit_names:
                dependencies[unit_name].add(field_value)
    
    return dependencies


def precompute_circular_references(dependencies: Dict[str, Set[str]]) -> Set[str]:
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


def precompute_resolution_order(dependencies: Dict[str, Set[str]]) -> List[str]:
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


def precompute_field_resolution_cache(unit_edits_dict: Dict) -> Dict[str, Dict[str, Any]]:
    """Precompute resolved field values for each unit to avoid repeated lookups."""
    # Precompute resolved field values for each unit
    field_cache = {}
    for unit_name, unit_data in unit_edits_dict.items():
        # Skip reference entries
        if unit_name.endswith("_reference"):
            continue
            
        field_cache[unit_name] = {}
        # Pre-resolve all potential field references
        for field_path, field_value in _flatten_dict(unit_data):
            if isinstance(field_value, str) and field_value in unit_edits_dict:
                donor_unit = unit_edits_dict[field_value]
                # Extract the specific field value from donor unit
                resolved_value = _extract_field_value(donor_unit, field_path)
                if resolved_value is not None:
                    field_cache[unit_name][field_path] = resolved_value
    
    return field_cache


def _resolve_unit_with_cache(unit_data: Any, unit_name: str, field_cache: Dict[str, Dict[str, Any]], unit_edits_dict: Dict[str, Any]) -> Any:
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
            
            # Special exception: if we're inside a list (like Transports), these are unit names, not references
            if "[" in current_path:
                return value
            
            # Check if this string references a unit name
            if value in unit_edits_dict:
                # Check if we have a precomputed field value
                if unit_name in field_cache and current_path in field_cache[unit_name]:
                    logger.debug(f"Using cached field reference '{value}.{current_path.split('.')[-1]}' for path '{current_path}'")
                    return field_cache[unit_name][current_path]
                
                referenced_value = unit_edits_dict[value]
                
                # Strict field resolution: extract the specific field from the referenced unit
                if isinstance(referenced_value, dict):
                    # Extract the field using the current path
                    extracted_value = _extract_field_value(referenced_value, current_path)
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





def resolve_unit_edit_references_optimized(unit_edits_dict: Dict) -> Dict:
    """
    Optimized version of resolve_unit_edit_references with precomputation.
    
    This version precomputes dependency graphs, field resolution caches, and optimal
    resolution order to improve performance, especially for large datasets with many
    shared references.
    """
    logger.info("Precomputing dependency graph and resolution caches for unit edits...")
    
    # Precompute all the caches and graphs
    dependencies = precompute_dependency_graph(unit_edits_dict)
    circular_refs = precompute_circular_references(dependencies)
    resolution_order = precompute_resolution_order(dependencies)
    field_cache = precompute_field_resolution_cache(unit_edits_dict)
    
    if circular_refs:
        logger.warning(f"Detected circular references in units: {circular_refs}")
    
    logger.info(f"Resolving {len(resolution_order)} units in optimal order...")
    
    # Resolve in optimal order using precomputed caches
    resolved_dict = {}
    for unit_name in resolution_order:
        if unit_name in unit_edits_dict:
            unit_data = unit_edits_dict[unit_name]
            resolved_data = _resolve_unit_with_cache(
                unit_data, unit_name, field_cache, unit_edits_dict
            )
            resolved_dict[unit_name] = resolved_data
    
    logger.info(f"Successfully resolved {len(resolved_dict)} units with optimizations")
    return resolved_dict


def load_unit_edits() -> Dict:
    """Load and merge all unit edit dictionaries."""
    merged_edits = {}
    
    logger.info("Loading unit edit dictionaries...")
    
    # Dictionary name mapping
    dict_names = {
        'BEL_unit_edits': 'bel_unit_edits',
        'FR_unit_edits': 'fr_unit_edits',
        'POL_unit_edits': 'pol_unit_edits',
        'RDA_unit_edits': 'rda_unit_edits',
        'RFA_unit_edits': 'rfa_unit_edits',
        'SOV_unit_edits': 'sov_unit_edits',
        'SUPPLY_unit_edits': 'supply_unit_edits',
        'UK_unit_edits': 'uk_unit_edits',
        'USA_unit_edits': 'usa_unit_edits'
    }
    
    # Load dictionaries
    dics_path = Path(__file__).parent
    for file in dics_path.glob("*unit_edits.py"):
        module_name = f"src.constants.unit_edits.{file.stem}"
        logger.debug(f"Processing {file.stem}")
        
        try:
            module = importlib.import_module(module_name)
            dict_name = dict_names.get(file.stem)
            if dict_name and hasattr(module, dict_name):
                merged_edits.update(getattr(module, dict_name))
                logger.info(f"Loaded unit edits from {file.stem}")
        except Exception as e:
            logger.error(f"Failed to load {file.stem}: {str(e)}")
    
    logger.info(f"Loaded edits for {len(merged_edits)} units total")

    # Resolve shared/borrowed values in unit edits dictionary
    logger.info("Resolving shared values in unit edits dictionaries...")
    merged_edits = resolve_unit_edit_references_optimized(merged_edits)
    logger.info("Successfully resolved unit edit references")
    with open("merged_edits.json", "w") as f:
        json.dump(merged_edits, f, indent=4)

    return merged_edits


def load_depiction_edits() -> Dict:
    """Load and merge all depiction edit dictionaries."""
    merged_edits = {}
    
    logger.info("Loading depiction edit dictionaries...")

    # Dictionary of faction modules to import
    faction_modules = {
        'POL': 'src.constants.unit_edits.depiction_edits.POL_depiction_edits',
        'SOV': 'src.constants.unit_edits.depiction_edits.SOV_depiction_edits',
        'UK': 'src.constants.unit_edits.depiction_edits.UK_depiction_edits',
        'USA': 'src.constants.unit_edits.depiction_edits.USA_depiction_edits',
        'FR': 'src.constants.unit_edits.depiction_edits.FR_depiction_edits',
        'RDA': 'src.constants.unit_edits.depiction_edits.RDA_depiction_edits',
        'RFA': 'src.constants.unit_edits.depiction_edits.RFA_depiction_edits',
    }
    
    # Import each faction's edits
    for faction, module_path in faction_modules.items():
        try:
            module = importlib.import_module(module_path)
            
            # Get all exported variables from __all__
            if hasattr(module, '__all__'):
                for var_name in module.__all__:
                    if hasattr(module, var_name):
                        unit_edits = getattr(module, var_name)
                        if "unit_name" in unit_edits:
                            unit_name = unit_edits["unit_name"]
                            merged_edits[unit_name] = unit_edits
                            logger.debug(f"Loaded depiction edits for {unit_name}")
                        else:
                            logger.warning(f"No unit_name found in {var_name} from {faction}")
            else:
                logger.debug(f"No __all__ defined in {faction} depiction edits")
                
        except ImportError:
            # Skip if faction module doesn't exist yet
            logger.debug(f"No depiction edits found for {faction}")
        except Exception as e:
            logger.error(f"Failed to load {faction} depiction edits: {str(e)}")
    
    logger.info(f"Loaded depiction edits for {len(merged_edits)} units total")
    return merged_edits

# # parse dictionary for shared/borrowed values in specific fields
#     for unit in merged_edits:
#         # if "import_base" in unit:
#         #     src_unit = merged_edits[merged_edits[unit].get("import_base")]
#         #     src_unit = {i: src_unit[i] for i in src_unit if i not in ("Divisions", "UpgradeFromUnit", "GameName")}
#         #     merged_edits[unit] = src_unit | merged_edits[unit]
#         for field in ("CommandPoints", "availability"):
#             ref_unit = merged_edits[unit].get(field, False)
#             if type(ref_unit) == str:
#                 # if field in merged_edits[unit] and type(merged_edits[unit][field]) == str:
#                 if ref_unit in merged_edits and field in merged_edits[ref_unit]:
#                     merged_edits[unit][field] = merged_edits[ref_unit][field]
#                     logger.info(f"Retrieved referenced \"{field}\" value for unit {unit} from unit {ref_unit}")
#                 else:
#                     merged_edits[unit].pop(field)