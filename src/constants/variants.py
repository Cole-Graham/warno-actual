"""Variant function mapping."""

from typing import Any, Callable, Dict

# from src.gameplay_mods.buildings.fob import edit_fob_attributes
# from src.shared_mods.buildings.fob import add_fob_minimap_module, add_fob_minimap_texture
from src.ui_mods.style.common.beacons import edit_uicommonbeaconlabelresources
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Validate function types
VARIANT_FUNCTIONS: Dict[str, Callable] = {
    # shared
    # "add_fob_minimap_texture": add_fob_minimap_texture,
    # "add_fob_minimap_module": add_fob_minimap_module,
    "edit_uicommonbeaconlabelresources": edit_uicommonbeaconlabelresources,
    # variants
    # "edit_fob_attributes": edit_fob_attributes,
}

logger.debug(f"Registered variant functions: {list(VARIANT_FUNCTIONS.keys())}")


def validate_editor_function(func_: Callable) -> bool:
    """Validate editor function signature."""
    import inspect
    sig = inspect.signature(func_)
    
    # Check param count
    if len(sig.parameters) != 1:
        raise TypeError(f"Editor function {func_.__name__} must take exactly one parameter")
        
    # Check param type hints
    params = list(sig.parameters.values())
    if params[0].annotation != inspect.Parameter.empty:
        if params[0].annotation != Any:
            raise TypeError(f"Editor function parameter must be unannotated or Any")
            
    return True


# Validate all functions have correct signature
for func in VARIANT_FUNCTIONS.values():
    if not callable(func):
        raise TypeError(f"Invalid variant function: {func.__name__} is not callable")
    validate_editor_function(func)
