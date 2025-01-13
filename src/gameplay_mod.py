"""Main gameplay modification module."""

from typing import Any, Callable, Dict

from src.data import build_database
from src.dics import load_unit_edits
from src.utils.logging_utils import log_time, setup_logger

logger = setup_logger('gameplay_mod')


def get_file_editor(file_path: str, config: Dict) -> Callable:
    """Get the appropriate edit function for gameplay files.
    
    Args:
        file_path: Path to the file being edited
        config: Configuration dictionary
        
    Returns:
        Editor function for the specified file, or None if no editor exists
    """
    logger.info(f"Loading data for {file_path}")
    
    with log_time(logger, "Loading databases"):
        # Build complete game database
        game_db = build_database(config)
        
    # Get editors from gameplay module
    from src.gameplay import get_editors
    editors = get_editors(game_db)
    
    if file_path in editors:
        def apply_editors(source):
            with log_time(logger, f"Processing {file_path}"):
                logger.debug(f"Starting edits for {file_path}")
                for i, editor in enumerate(editors[file_path], 1):
                    with log_time(logger, f"Running editor {i}"):
                        editor(source)
                logger.debug(f"Completed edits for {file_path}")
        return apply_editors
    return None 