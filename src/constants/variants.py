"""Variant function mapping."""

from typing import Any, Callable, Dict

from src.gameplay.buildings import edit_fob_attributes, edit_fob_minimap

# Validate function types
VARIANT_FUNCTIONS: Dict[str, Callable] = {
    "edit_fob_attributes": edit_fob_attributes,
    "edit_fob_minimap": edit_fob_minimap,
}

def validate_editor_function(func: Callable) -> bool:
    """Validate editor function signature."""
    import inspect
    sig = inspect.signature(func)
    
    # Check param count
    if len(sig.parameters) != 1:
        raise TypeError(f"Editor function {func.__name__} must take exactly one parameter")
        
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