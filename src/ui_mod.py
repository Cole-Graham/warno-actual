"""Main UI modification module."""
from typing import Any, Callable, Dict, List, Optional, Set  # noqa

from src.constants.variants import VARIANT_FUNCTIONS
from src.shared import get_shared_editors
from src.ui import get_ui_editors
from src.utils.logging_utils import log_time, setup_logger
from src.utils.variant_utils import validate_variant_config

logger = setup_logger('ui_mod')


def get_file_editor(ndf_path: str, config: Dict) -> Optional[Callable]:
    """Get the appropriate edit function for UI files."""
    editors_to_apply: Set[Callable] = set()  # Use set to deduplicate editors
    
    # First check UI editors
    editors = get_ui_editors()
    if ndf_path in editors:
        logger.debug(f"Found UI editor for {ndf_path}")
        editors_to_apply.update(editors[ndf_path])
    
    # Then check shared editors from module
    shared_editors = get_shared_editors()
    if ndf_path in shared_editors:
        logger.debug(f"Found shared editor(s) for {ndf_path} in shared module")
        editors_to_apply.update(shared_editors[ndf_path])
    
    # Check shared section from config
    shared_files = config.get("files", {}).get("shared", {})
    if ndf_path in shared_files:
        shared_funcs = shared_files[ndf_path]
        logger.debug(f"Found shared functions for {ndf_path} in config: {shared_funcs}")
        
        for func_name in shared_funcs:
            if func_name not in VARIANT_FUNCTIONS:
                logger.error(f"Function {func_name} not found in VARIANT_FUNCTIONS")
                continue
            logger.debug(f"Adding shared function from config: {func_name}")
            editors_to_apply.add(VARIANT_FUNCTIONS[func_name])

    # Finally check variants
    variants = config.get("variants", {})
    try:
        validate_variant_config(variants)
    except ValueError as e:
        logger.error(f"Invalid variant configuration: {e}")
        return None
    
    if ndf_path in variants:
        variant_funcs = variants[ndf_path].get("ui", [])
        logger.debug(f"Found UI variant functions for {ndf_path}: {variant_funcs}")
        
        for func_name in variant_funcs:
            if func_name not in VARIANT_FUNCTIONS:
                logger.error(f"Function {func_name} not found in VARIANT_FUNCTIONS")
                continue
            logger.debug(f"Adding variant function: {func_name}")
            editors_to_apply.add(VARIANT_FUNCTIONS[func_name])

    if not editors_to_apply:
        return None
        
    def apply_all_editors(source_path):
        with log_time(logger, f"Processing all editors for {ndf_path}"):
            for editor in editors_to_apply:
                logger.debug(f"Applying editor: {editor.__name__}")
                editor(source_path)
                
    return apply_all_editors
