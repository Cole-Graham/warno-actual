from pathlib import Path
from typing import Any, Dict, List  # noqa

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def get_mod_src_path(config: Dict) -> Path:
    """Get mod source directory path based on config."""
    warno_mods = Path(config['directories']['warno_mods'])

    # Use base game as source
    mod_name = config['directories']['base_game']
    
    return warno_mods / mod_name


def get_mod_name(config: Dict) -> str:
    """Return the destination mod folder name for the current build target."""
    build_config = config['build_config']
    dirs = config['directories']
    target = build_config['target']
    is_dev = build_config['write_dev']

    if target == 'gameplay':
        return dirs['gameplay_dev'] if is_dev else dirs['gameplay_release']
    if target == 'ui_only':
        return dirs['ui_only_dev'] if is_dev else dirs['ui_only_release']
    raise ValueError(f"Invalid build target: {target}")


def get_mod_dst_path(config_data: Dict) -> Path:
    """Determine the correct destination path based on build configuration"""
    dirs = config_data['directories']
    warno_mods = Path(dirs['warno_mods'])
    return warno_mods / get_mod_name(config_data)
