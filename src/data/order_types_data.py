"""Functions for building order types data from OrderAvailability_Tactic.ndf."""

from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

from src import ndf
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

ORDER_AVAILABILITY_NDF_PATH = "GameData/Generated/Gameplay/Gfx/OrderAvailability_Tactic.ndf"
ORDER_DESCRIPTOR_PREFIX = "Descriptor_OrderAvailability_"


def _order_type_string(item: Any) -> str:
    """Extract EOrderType/XXX string from a list item (object with .v or plain string)."""
    if hasattr(item, "v"):
        return str(item.v).strip()
    return str(item).strip()


def _unit_name_from_namespace(namespace: str) -> str:
    """Extract unit name from order descriptor namespace, e.g. RCL_L6_Wombat_UK."""
    if namespace.startswith(ORDER_DESCRIPTOR_PREFIX):
        return namespace[len(ORDER_DESCRIPTOR_PREFIX) :]
    return namespace


def gather_order_types(mod_src_path: Path) -> Dict[str, Any]:
    """Gather all unique order types and unique order sets with their units.

    Parses the NDF file and collects:
    - Every EOrderType/XXX referenced across all Descriptor_OrderAvailability_* entries.
    - Every unique set of orders and the list of unit names that have that set.

    Returns:
        Dict with "all_order_types" and "order_sets_to_units".
    """
    all_order_types: Set[str] = set()
    # Map canonical order set (tuple of sorted order strings) -> list of unit names
    order_set_to_units: Dict[Tuple[str, ...], List[str]] = {}

    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        parse_source = mod.parse_src(ORDER_AVAILABILITY_NDF_PATH)

        for order_list in parse_source:
            if not hasattr(order_list, "namespace"):
                continue
            if not hasattr(order_list, "v"):
                continue

            unit_name = _unit_name_from_namespace(order_list.namespace)
            descriptor_orders: List[str] = []

            try:
                for item in order_list.v:
                    order_str = _order_type_string(item)
                    if order_str and order_str.startswith("EOrderType/"):
                        all_order_types.add(order_str)
                        descriptor_orders.append(order_str)
            except (TypeError, AttributeError) as e:
                logger.debug(f"Skip non-list value for {getattr(order_list, 'namespace', '?')}: {e}")
                continue

            if descriptor_orders:
                key = tuple(sorted(descriptor_orders))
                if key not in order_set_to_units:
                    order_set_to_units[key] = []
                order_set_to_units[key].append(unit_name)

        # Serialize order sets to JSON-friendly list of {orders, units}
        order_sets_to_units = [
            {
                "orders": list(orders_tuple),
                "units": sorted(units),
            }
            for orders_tuple, units in sorted(order_set_to_units.items(), key=lambda x: (len(x[0]), x[0]))
        ]

        result = {
            "all_order_types": sorted(all_order_types),
            "order_sets_to_units": order_sets_to_units,
        }
        logger.info(
            f"Gathered {len(all_order_types)} unique order types and {len(order_sets_to_units)} unique order sets from {ORDER_AVAILABILITY_NDF_PATH}"
        )
        return result

    except Exception as e:
        logger.error(f"Error gathering order types from {ORDER_AVAILABILITY_NDF_PATH}: {e}", exc_info=True)
        return {"all_order_types": [], "order_sets_to_units": []}


def compare_order_types_with_previous(
    current_order_types: list,
    previous_order_types: list,
) -> None:
    """Log warnings if order types were added or removed compared to previous build."""
    current_set = set(current_order_types)
    previous_set = set(previous_order_types)

    added = current_set - previous_set
    removed = previous_set - current_set

    if added:
        logger.warning(
            "Order types added in game data (new order types): %s",
            sorted(added),
        )
    if removed:
        logger.warning(
            "Order types removed from game data (no longer present): %s",
            sorted(removed),
        )
