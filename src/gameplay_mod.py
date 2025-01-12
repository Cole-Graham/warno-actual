from typing import Any, Callable, Dict, List

from src.data.data_builder import load_data
from src.gameplay import division_rules, divisions, unit_descriptor, weapons
from src.utils.logging_utils import log_time, setup_logger

logger = setup_logger('gameplay_mod')

def get_file_editor(file_path: str, config: Dict) -> Callable:
    """Get the appropriate edit function for gameplay files."""
    logger.info(f"Loading data for {file_path}")
    
    with log_time(logger, "Loading unit database"):
        unit_db = load_data(config, "units")
    
    editors: Dict[str, List[Callable]] = {
        "GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf": 
            unit_descriptor.get_editors(unit_db),
        "GameData/Generated/Gameplay/DivisionRules.ndf":
            division_rules.get_editors(unit_db),
        "GameData/Generated/Gameplay/Divisions.ndf":
            divisions.get_editors(unit_db),
        "GameData/Generated/Gameplay/Gfx/WeaponDescriptor.ndf":
            weapons.get_editors(unit_db),
    }
    
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