"""Variant validation utilities."""

from pathlib import Path
from typing import Dict, List

from src.constants.variants import VARIANT_FUNCTIONS
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def validate_variant_config(variants: Dict, mod_src_path: Path = None) -> None:
    """Validate variant configuration."""
    if not variants:
        return
        
    for ndf_path, config in variants.items():
        # Validate file exists if source path provided
        if mod_src_path:
            full_path = mod_src_path / ndf_path
            if not full_path.exists():
                raise ValueError(f"Variant file not found: {full_path}")
            
        # Check config format
        if not isinstance(config, dict):
            raise ValueError(f"Invalid variant config for {ndf_path}: must be dictionary")
            
        # For variant files, check UI/gameplay lists
        if "ui" in config or "gameplay" in config:
            if "ui" not in config or "gameplay" not in config:
                raise ValueError(f"Missing required keys in variant config for {ndf_path}")
                
            # Validate UI functions
            _validate_function_list(config["ui"], ndf_path, "ui")
            
            # Validate gameplay functions  
            _validate_function_list(config["gameplay"], ndf_path, "gameplay")
            
            # Ensure UI functions are subset of gameplay functions
            ui_funcs = set(config["ui"])
            gameplay_funcs = set(config["gameplay"])
            if not ui_funcs.issubset(gameplay_funcs):
                invalid_funcs = ui_funcs - gameplay_funcs
                raise ValueError(
                    f"UI functions must be subset of gameplay functions. "
                    f"Invalid functions: {invalid_funcs}"
                )
        # For shared files, check single function list
        else:
            if not isinstance(config, list):
                raise ValueError(f"Shared file config must be list for {ndf_path}")
            _validate_function_list(config, ndf_path, "shared")


def _validate_function_list(functions: List[str], file_path: str, mod_type: str) -> None:
    """Validate list of function names."""
    if not isinstance(functions, list):
        raise ValueError(f"Invalid {mod_type} functions for {file_path}: must be list")
        
    for func_name in functions:
        if func_name not in VARIANT_FUNCTIONS:
            raise ValueError(f"Unknown function '{func_name}' in {file_path} {mod_type} config") 


def validate_source(source) -> bool:
    """Validate source file structure."""
    if not source:
        logger.error("Empty source file")
        return False
        
    if not hasattr(source, '__iter__'):
        logger.error("Source file not iterable")
        return False
        
    return True
