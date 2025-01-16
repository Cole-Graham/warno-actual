"""Main UI modification module."""

from typing import Any, Callable, Dict

from src.constants.variants import VARIANT_FUNCTIONS
from src.utils.logging_utils import log_time, setup_logger
from src.utils.variant_utils import validate_variant_config

logger = setup_logger('ui_mod')

def get_file_editor(file_path: str, config: Dict) -> Callable:
    """Get the appropriate edit function for UI files.
    
    Args:
        file_path: Path to the file being edited
        config: Configuration dictionary
        
    Returns:
        Editor function for the specified file, or None if no editor exists
    """
    # Check if file is in variants
    variants = config.get("variants", {})
    try:
        validate_variant_config(variants)
    except ValueError as e:
        logger.error(f"Invalid variant configuration: {e}")
        return None
    
    if file_path in variants:
        variant_funcs = variants[file_path].get("ui", [])
        logger.debug(f"Found UI variant functions for {file_path}: {variant_funcs}")
        
        def apply_variant_editors(source):
            with log_time(logger, f"Processing UI variants for {file_path}"):
                for func_name in variant_funcs:
                    logger.debug(f"Applying UI variant function: {func_name}")
                    VARIANT_FUNCTIONS[func_name](source)
        return apply_variant_editors
    else:
        # Get editors from UI module
        from src.ui import get_editors
        editors = get_editors()
        
        if file_path in editors:
            def apply_editors(source):
                with log_time(logger, f"Processing UI file {file_path}"):
                    logger.debug(f"Starting UI edits for {file_path}")
                    for editor in editors[file_path]:
                        editor(source)
                    logger.debug(f"Completed UI edits for {file_path}")
            return apply_editors
    return None 