"""Functions for loading source NDF files."""

from pathlib import Path
from typing import Any, Dict

from src import ndf
from src.utils.config_utils import get_mod_src_path
from src.utils.logging_utils import setup_logger

logger = setup_logger('source_loader')

def get_source_files(config: Dict[str, Any]) -> Dict[str, str]:
    """Get NDF source files from configured source path.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        Dictionary mapping NDF file paths to their parsed contents
    """
    mod_src_path = get_mod_src_path(config)
    logger.debug(f"Reading NDF files from: {mod_src_path}")
    
    source_files = {}
    if not mod_src_path.exists():
        logger.error(f"Source path does not exist: {mod_src_path}")
        return {}
        
    for file_path in mod_src_path.rglob("*.ndf"):
        try:
            relative_path = file_path.relative_to(mod_src_path)
            ndf_path = str(relative_path)
            logger.debug(f"Found NDF file: {ndf_path}")
                
            with open(file_path, "r", encoding="utf-8") as f:
                source_files[ndf_path] = ndf.parse(f.read())
        except Exception as e:
            logger.error(f"Error loading {file_path}: {e}")
            continue

    if not source_files:
        logger.error("No NDF files found in source paths")
        return {}

    return source_files 