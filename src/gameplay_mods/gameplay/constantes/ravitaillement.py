"""Miscellaneous game constant edits."""

from typing import Any, Dict

from src.utils.logging_utils import setup_logger
from src.constants import NEW_SUPPLY_CONSTANTS as new_supply_constants

logger = setup_logger(__name__)

# Expected vanilla values for validation
EXPECTED_VANILLA_VALUES = {
    "FuelSupplyBySecond": 30.0,
    "FuelSupplyCostBySecond": 1.5,
    "HealthSupplyBySecond": 0.10,
    "HealthSupplyCostBySecond": 3.0,
    "AmmunitionSupplyBySecond": 60,
    "CriticsSupplyBySecond": 10,
    "CriticsSupplyCostBySecond": 20,
}

# Field configuration: (field_name, requires_int_conversion)
SUPPLY_FIELDS = [
    ("FuelSupplyBySecond", False),
    ("FuelSupplyCostBySecond", False),
    ("HealthSupplyBySecond", False),
    ("HealthSupplyCostBySecond", False),
    ("AmmunitionSupplyBySecond", True),  # must be int
    ("CriticsSupplyBySecond", False),
    ("CriticsSupplyCostBySecond", False),
]


def _read_vanilla_values(standard_supply_descr) -> Dict[str, float]:
    """Read vanilla supply values from StandardSupply descriptor."""
    vanilla_values = {}
    descr_membr = standard_supply_descr.v.by_m
    
    for field_name, _ in SUPPLY_FIELDS:
        vanilla_values[field_name] = float(descr_membr(field_name).v)
    
    return vanilla_values


def _validate_vanilla_values(vanilla_values: Dict[str, float]) -> None:
    """Validate that vanilla values match expected values."""
    for field_name, expected_value in EXPECTED_VANILLA_VALUES.items():
        actual_value = vanilla_values[field_name]
        if actual_value != expected_value:
            logger.warning(
                f"{field_name} value {actual_value} is not expected value ({expected_value}), "
                f"Eugen has likely changed this value"
            )


def _create_supply_variant(source_path, variant_name: str, settings: Dict[str, Any], vanilla_values: Dict[str, float]) -> None:
    """Create and add a new supply variant descriptor."""
    variant_descriptor = source_path.by_n("StandardSupply").copy()
    variant_descriptor.namespace = variant_name
    logger.info(f"Adding {variant_name} descriptor")
    
    descr_membr = variant_descriptor.v.by_m
    
    # Set DefaultSupplyRangeGRU (not a multiplier)
    descr_membr("DefaultSupplyRangeGRU").v = str(settings["DefaultSupplyRangeGRU"])
    
    # Set all supply fields using multipliers
    for field_name, requires_int in SUPPLY_FIELDS:
        multiplier = settings[field_name]
        calculated_value = vanilla_values[field_name] * multiplier
        
        if requires_int:
            calculated_value = int(calculated_value)
        else:
            calculated_value = float(calculated_value)
        
        descr_membr(field_name).v = str(calculated_value)
        logger.info(f"{field_name}: {descr_membr(field_name).v}")
    
    source_path.add(variant_descriptor)
    logger.info(f"Added {variant_name} descriptor")


def edit_gameplay_constantes_ravitaillement(source_path) -> None:
    """GameData/Gameplay/Constantes/Ravitaillement.ndf"""
    logger.info("Editing Ravitaillement.ndf")

    # Read vanilla values from StandardSupply
    standard_supply_descr = source_path.by_n("StandardSupply")
    vanilla_values = _read_vanilla_values(standard_supply_descr)
    
    # Validate vanilla values match expected values
    _validate_vanilla_values(vanilla_values)

    # Create and add new supply variants
    for variant_name, settings in new_supply_constants.items():
        _create_supply_variant(source_path, variant_name, settings, vanilla_values)