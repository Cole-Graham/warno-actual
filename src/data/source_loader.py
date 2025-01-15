"""Functions for loading source NDF files."""

from pathlib import Path
from typing import Any, Dict

from src import ndf
from src.utils.config_utils import get_source_path
from src.utils.logging_utils import setup_logger

logger = setup_logger('source_loader')

def get_source_files(config: Dict[str, Any]) -> Dict[str, str]:
    """Get NDF source files from configured source path.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        Dictionary mapping file paths to their parsed NDF contents
    """
    source_path = get_source_path(config)
    logger.debug(f"Reading NDF files from: {source_path}")
    
    source_files = {}
    if not source_path.exists():
        logger.error(f"Source path does not exist: {source_path}")
        return {}
        
    for file_path in source_path.rglob("*.ndf"):
        try:
            relative_path = file_path.relative_to(source_path)
            path_str = str(relative_path)
            logger.debug(f"Found NDF file: {path_str}")
                
            with open(file_path, "r", encoding="utf-8") as f:
                source_files[path_str] = ndf.parse(f.read())
        except Exception as e:
            logger.error(f"Error loading {file_path}: {e}")
            continue

    if not source_files:
        logger.error("No NDF files found in source paths")
        return {}

    return source_files 