"""Main UI modification module."""

from typing import Any, Callable, Dict

from src.constants.variants import VARIANT_FUNCTIONS
from src.utils.logging_utils import log_time, setup_logger
from src.utils.variant_utils import validate_variant_config

logger = setup_logger('ui_mod')

def get_file_editor(ndf_path: str, config: Dict) -> Callable:
    """Get the appropriate edit function for UI files.
    
    Args:
        ndf_path: Path to the file being edited
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
    
    if ndf_path in variants:
        variant_funcs = variants[ndf_path].get("ui", [])
        logger.debug(f"Found UI variant functions for {ndf_path}: {variant_funcs}")
        
        def apply_variant_editors(source_path):
            with log_time(logger, f"Processing UI variants for {ndf_path}"):
                for func_name in variant_funcs:
                    logger.debug(f"Applying UI variant function: {func_name}")
                    VARIANT_FUNCTIONS[func_name](source_path)
        return apply_variant_editors
    else:
        # Get editors from UI module
        from src.ui import get_editors
        editors = get_editors()
        
        if ndf_path in editors:
            def apply_editors(source_path):
                with log_time(logger, f"Processing UI file {ndf_path}"):
                    logger.debug(f"Starting UI edits for {ndf_path}")
                    for editor in editors[ndf_path]:
                        editor(source_path)
                    logger.debug(f"Completed UI edits for {ndf_path}")
            return apply_editors
    return None 