"""Main gameplay modification module."""

from typing import Any, Callable, Dict, List

from src.constants.variants import VARIANT_FUNCTIONS
from src.utils.logging_utils import log_time, setup_logger
from src.utils.variant_utils import validate_variant_config

logger = setup_logger('gameplay_mod')

def get_file_editor(ndf_path: str, config: Dict) -> Callable:
    """Get the appropriate edit function for gameplay files.
    
    Args:
        ndf_path: Path to the file being edited
        config: Configuration dictionary
        
    Returns:
        Editor function for the specified file, or None if no editor exists
    """
    logger.info(f"Loading data for {ndf_path}")
    
    # Check variants first
    variants = config.get("variants", {})
    if ndf_path in variants:
        variant_funcs = variants[ndf_path].get("gameplay", [])
        def apply_variant_editors(source_path):
            with log_time(logger, f"Processing variants for {ndf_path}"):
                for func_name in variant_funcs:
                    VARIANT_FUNCTIONS[func_name](source_path)
        return apply_variant_editors

    # Check shared files next
    shared = config.get("shared", {})
    if ndf_path in shared:
        shared_funcs = shared[ndf_path].get("gameplay", [])
        def apply_shared_editors(source_path):
            with log_time(logger, f"Processing shared file {ndf_path}"):
                for func_name in shared_funcs:
                    VARIANT_FUNCTIONS[func_name](source_path)
        return apply_shared_editors
        
    # Finally check gameplay editors
    from src.gameplay import get_editors
    editors = get_editors(config['game_db'])
    if ndf_path in editors:
        def apply_editors(source_path):
            with log_time(logger, f"Processing {ndf_path}"):
                for i, editor in enumerate(editors[ndf_path], 1):
                    with log_time(logger, f"Running editor {i}"):
                        editor(source_path)
        return apply_editors

    return None 