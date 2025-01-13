"""Functions for modifying vanilla weapon instances."""

from typing import List, Tuple

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def apply_vanilla_renames(source, renames: List[Tuple[str, str]]) -> None:
    """Apply renames to vanilla weapon instances.
    
    Args:
        source: NDF file containing weapon descriptors
        renames: List of (old_name, new_name) tuples
    """
    for descriptor in source.findall("TAmmunitionDescriptor"):
        old_name = descriptor.name
        for old, new in renames:
            if old_name == old:
                logger.info(f"Renaming {old_name} to {new}")
                descriptor.name = new
                break


def remove_vanilla_instances(source, removals: List[str]) -> None:
    """Remove specified vanilla weapon instances.
    
    Args:
        source: NDF file containing weapon descriptors
        removals: List of instance names to remove
    """
    for descriptor in source.findall("TAmmunitionDescriptor"):
        name = descriptor.name
        if name in removals:
            logger.info(f"Removing vanilla instance: {name}")
            source.remove(descriptor) 