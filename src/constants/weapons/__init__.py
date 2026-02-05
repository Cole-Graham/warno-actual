"""Weapon edit definitions."""

from pathlib import Path
from typing import Dict, Any, Union, List, Tuple, Set
from src.utils.logging_utils import setup_logger
import json, os
from .ammunition import raw_ammunitions
from .damage_values import (
    HEAT_ROW_COUNT,
    KINETIC_ROW_COUNT,
    KE_AND_HEAT_ROW_COUNT,
    VANILLA_LAST_ROW,
    VANILLA_LAST_COLUMN,
    DAMAGE_EDITS,
    DPICM_DAMAGES,
    FMBALLE_INFANTRY_EDITS,
    FMBALLE_ROWS,
    SA_FULL_DAMAGE_RATIOS,
    SA_INTERMEDIATE_DAMAGE_RATIOS,
    SA_INF_ARMOR_DAMAGE_RATIOS,
    INFANTRY_ARMOR_EDITS,
    SNIPER_DAMAGE,
    NPLM_BOMB_DAMAGE,
    NPLM_BOMB_FLAMME_DAMAGE,
    PGB_BOMB_DAMAGE,
    MANPAD_HAGRU_DAMAGE,
    MANPAD_TBAGRU_DAMAGE,
    TWELVE_SEVEN_MM_DAMAGE,
    FOURTEEN_FIVE_MM_DAMAGE,
)
from .missiles import raw_missiles
from .mounted_weapons import mounted_weapons
from .salvo_standards import LIGHT_AT_AMMO
from .weapon_descriptions import WEAPON_DESCRIPTIONS, WEAPON_TRAIT_EDITS, WEAPON_DESCRIPTION_EDITS
from .vanilla_inst_modifications import (
    AMMUNITION_MISSILES_REMOVALS,
    AMMUNITION_MISSILES_RENAMES,
    AMMUNITION_REMOVALS,
    AMMUNITION_RENAMES
)

__all__ = [
    'HEAT_ROW_COUNT',
    'KINETIC_ROW_COUNT',
    'KE_AND_HEAT_ROW_COUNT',
    'VANILLA_LAST_ROW',
    'VANILLA_LAST_COLUMN',
    'AMMUNITION_MISSILES_REMOVALS',
    'AMMUNITION_MISSILES_RENAMES', 
    'AMMUNITION_REMOVALS',
    'AMMUNITION_RENAMES',
    'DAMAGE_EDITS',
    'DPICM_DAMAGES',
    'FMBALLE_INFANTRY_EDITS',
    'FMBALLE_ROWS',
    'SA_FULL_DAMAGE_RATIOS',
    'SA_INTERMEDIATE_DAMAGE_RATIOS',
    'SA_INF_ARMOR_DAMAGE_RATIOS',
    'INFANTRY_ARMOR_EDITS',
    'NPLM_BOMB_DAMAGE',
    'NPLM_BOMB_FLAMME_DAMAGE',
    'missiles',
    'mounted_weapons',
    'SNIPER_DAMAGE',
    'LIGHT_AT_AMMO',
    'WEAPON_DESCRIPTIONS',
    'WEAPON_DESCRIPTION_EDITS',
    'WEAPON_TRAIT_EDITS',
    'ammunitions',
    'PGB_BOMB_DAMAGE',
    'MANPAD_HAGRU_DAMAGE',
    'MANPAD_TBAGRU_DAMAGE',
    'TWELVE_SEVEN_MM_DAMAGE',
    'FOURTEEN_FIVE_MM_DAMAGE',
]

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


def precompute_dependency_graph(ammunition_dict: Dict) -> Dict[str, Set[str]]:
    """Precompute which weapons depend on which other weapons."""
    dependencies = {}
    weapon_names = set()
    
    # First pass: collect all weapon names
    for key, value in ammunition_dict.items():
        if isinstance(key, tuple) and len(key) > 0:
            weapon_name = key[0]
            weapon_names.add(weapon_name)
            dependencies[weapon_name] = set()
    
    # Second pass: find dependencies
    for key, value in ammunition_dict.items():
        if isinstance(key, tuple) and len(key) > 0:
            weapon_name = key[0]
            
            # Find all weapon references in this weapon's data
            for field_path, field_value in _flatten_dict(value):
                # Special exception: NewTexture and Texture fields should not be treated as weapon references
                if field_path.endswith("NewTexture") or field_path.endswith("Texture"):
                    continue
                    
                if isinstance(field_value, str) and field_value in weapon_names:
                    dependencies[weapon_name].add(field_value)
    
    return dependencies


def precompute_circular_references(dependencies: Dict[str, Set[str]]) -> Set[str]:
    """Precompute which weapons have circular references."""
    circular_weapons = set()
    
    def has_cycle(weapon: str, visited: Set[str], rec_stack: Set[str]) -> bool:
        visited.add(weapon)
        rec_stack.add(weapon)
        
        for dep in dependencies.get(weapon, set()):
            if dep not in visited:
                if has_cycle(dep, visited, rec_stack):
                    return True
            elif dep in rec_stack:
                circular_weapons.add(weapon)
                return True
        
        rec_stack.remove(weapon)
        return False
    
    for weapon in dependencies:
        if weapon not in circular_weapons:
            has_cycle(weapon, set(), set())
    
    return circular_weapons


def precompute_resolution_order(dependencies: Dict[str, Set[str]]) -> List[str]:
    """Precompute optimal order to resolve weapons (topological sort)."""
    # Count incoming dependencies for each weapon
    in_degree = {weapon: 0 for weapon in dependencies}
    for weapon, deps in dependencies.items():
        for dep in deps:
            if dep in in_degree:
                in_degree[dep] += 1
    
    # Start with weapons that have no dependencies
    queue = [weapon for weapon, degree in in_degree.items() if degree == 0]
    resolution_order = []
    
    while queue:
        weapon = queue.pop(0)
        resolution_order.append(weapon)
        
        # Reduce in-degree for all weapons that depend on this one
        for dep in dependencies.get(weapon, set()):
            in_degree[dep] -= 1
            if in_degree[dep] == 0:
                queue.append(dep)
    
    # Add any remaining weapons (those with circular references)
    for weapon in dependencies:
        if weapon not in resolution_order:
            resolution_order.append(weapon)
    
    return resolution_order


def precompute_field_resolution_cache(ammunition_dict: Dict) -> Dict[str, Dict[str, Any]]:
    """Precompute resolved field values for each weapon to avoid repeated lookups."""
    weapon_name_to_data = {}
    for key, value in ammunition_dict.items():
        if isinstance(key, tuple) and len(key) > 0:
            weapon_name = key[0]
            weapon_name_to_data[weapon_name] = value
    
    # Precompute resolved field values for each weapon
    field_cache = {}
    for weapon_name, weapon_data in weapon_name_to_data.items():
        field_cache[weapon_name] = {}
        # Pre-resolve all potential field references
        for field_path, field_value in _flatten_dict(weapon_data):
            if isinstance(field_value, str) and field_value in weapon_name_to_data:
                donor_weapon = weapon_name_to_data[field_value]
                # Extract the specific field value from donor weapon
                resolved_value = _extract_field_value(donor_weapon, field_path)
                if resolved_value is not None:
                    field_cache[weapon_name][field_path] = resolved_value
    
    return field_cache


def _resolve_weapon_with_cache(weapon_data: Any, weapon_name: str, field_cache: Dict[str, Dict[str, Any]], weapon_name_to_data: Dict[str, Any]) -> Any:
    """Resolve a single weapon using precomputed field cache."""
    
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
            # Special exception: NewTexture field should not be resolved as references
            if current_path.endswith("NewTexture") or current_path.endswith("Texture"):
                return value
            
            # Check if this string references a weapon name
            if value in weapon_name_to_data:
                # Check if we have a precomputed field value
                if weapon_name in field_cache and current_path in field_cache[weapon_name]:
                    logger.debug(f"Using cached field reference '{value}.{current_path.split('.')[-1]}' for path '{current_path}'")
                    cached_value = field_cache[weapon_name][current_path]
                    # Convert numeric values to strings for NDF compatibility
                    if isinstance(cached_value, (int, float)):
                        return str(cached_value)
                    return cached_value
                
                referenced_value = weapon_name_to_data[value]
                
                # Strict field resolution: extract the specific field from the referenced weapon
                if isinstance(referenced_value, dict):
                    # Extract the field using the current path
                    extracted_value = _extract_field_value(referenced_value, current_path)
                    if extracted_value is not None:
                        logger.debug(f"Resolving field reference '{value}.{current_path}' for path '{current_path}'")
                        # Convert numeric values to strings for NDF compatibility
                        if isinstance(extracted_value, (int, float)):
                            return str(extracted_value)
                        return extracted_value
                
                # No fallback - if we can't find the field, raise an error
                logger.error(f"Failed to resolve field reference '{value}' for path '{current_path}' - field not found in referenced weapon")
                raise ValueError(f"Field '{current_path}' not found in referenced weapon '{value}'")
            else:
                # String doesn't reference a weapon, return as-is
                return value
        else:
            # Non-string value, return as-is
            return value
    
    return resolve_value(weapon_data, "")





def resolve_ammunition_shared_values_optimized(ammunition_dict: Dict) -> Dict:
    """
    Optimized version of resolve_ammunition_shared_values with precomputation.
    
    This version precomputes dependency graphs, field resolution caches, and optimal
    resolution order to improve performance, especially for large datasets with many
    shared references.
    """
    logger.info("Precomputing dependency graph and resolution caches...")
    
    # Precompute all the caches and graphs
    dependencies = precompute_dependency_graph(ammunition_dict)
    circular_refs = precompute_circular_references(dependencies)
    resolution_order = precompute_resolution_order(dependencies)
    field_cache = precompute_field_resolution_cache(ammunition_dict)
    
    if circular_refs:
        logger.warning(f"Detected circular references in weapons: {circular_refs}")
    
    # Create weapon name mapping
    weapon_name_to_data = {}
    for key, value in ammunition_dict.items():
        if isinstance(key, tuple) and len(key) > 0:
            weapon_name = key[0]
            weapon_name_to_data[weapon_name] = value
    
    logger.info(f"Resolving {len(resolution_order)} weapons in optimal order...")
    
    # Resolve in optimal order using precomputed caches
    resolved_dict = {}
    for weapon_name in resolution_order:
        if weapon_name in weapon_name_to_data:
            weapon_data = weapon_name_to_data[weapon_name]
            resolved_data = _resolve_weapon_with_cache(
                weapon_data, weapon_name, field_cache, weapon_name_to_data
            )
            # Find the original key for this weapon
            for key in ammunition_dict:
                if isinstance(key, tuple) and key[0] == weapon_name:
                    resolved_dict[key] = resolved_data
                    break
    
    logger.info(f"Successfully resolved {len(resolved_dict)} weapons with optimizations")
    return resolved_dict


# Resolve shared values in ammunition dictionary
logger.info("Resolving shared values in ammunition dictionaries...")
ammunitions = resolve_ammunition_shared_values_optimized(raw_ammunitions)
# Convert tuple keys to strings for JSON serialization
ammunitions_for_json = {str(k): v for k, v in ammunitions.items()}
logs_dir = Path(__file__).parents[3] / "logs"
logs_dir.mkdir(exist_ok=True)
with open(logs_dir / "ammunitions.json", "w") as f:
    json.dump(ammunitions_for_json, f, indent=4)
logger.info(f"Resolved shared values for {len(ammunitions)} ammunition entries")

# Resolve shared values in missile dictionary
logger.info("Resolving shared values in missile dictionaries...")
missiles = resolve_ammunition_shared_values_optimized(raw_missiles)
# Convert tuple keys to strings for JSON serialization
missiles_for_json = {str(k): v for k, v in missiles.items()}
with open(logs_dir / "missiles.json", "w") as f:
    json.dump(missiles_for_json, f, indent=4)
logger.info(f"Resolved shared values for {len(missiles)} missile entries")
