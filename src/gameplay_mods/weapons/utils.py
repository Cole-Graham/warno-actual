import re
from typing import Any, Dict, List, Tuple

from src.utils.logging_utils import setup_logger

logger = setup_logger('weapons')


def rename_descriptor(source: Any, old_name: str, new_name: str) -> None:
    """Rename a descriptor in the source."""
    try:
        descriptor = source.by_n(old_name)
        if descriptor:
            descriptor.namespace = new_name
            logger.debug(f"Renamed {old_name} to {new_name}")
        else:
            logger.warning(f"Could not find descriptor {old_name} to rename")
    except Exception as e:
        logger.error(f"Failed to rename {old_name}: {str(e)}")


def get_salvo_renames(source: Any) -> List[Tuple[str, str]]:
    """Get list of renames from _x{n} to _salvoLen{n}."""
    renames = []
    for row in source:
        if not hasattr(row, 'namespace'):
            continue
            
        name = row.namespace
        if match := re.match(r'Ammo_(.+)_x(\d+)$', name):
            base_name, salvo_len = match.groups()
            new_name = f"Ammo_{base_name}_salvoLen{salvo_len}"
            renames.append((name, new_name))
            
    return renames 

# Shared utility functions for weapon editing


def get_supply_costs(weapons_dict: Dict) -> List[Tuple[str, int]]:
    """Get base supply costs for weapons."""
    weapon_costs = []
    for (weapon, _, _, _), data in weapons_dict.items():
        if data is None:
            continue
        if supply_cost := data.get("Ammunition", {}).get("parent_membr", {}).get("SupplyCost", None):
            weapon_costs.append((weapon, supply_cost))
        elif base_supply_cost := data.get("BaseSupplyCost", None):
            weapon_costs.append((weapon, base_supply_cost))
    return weapon_costs
