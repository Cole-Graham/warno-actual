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


def get_mod_dst_path(config_data: Dict) -> Path:
    """Determine the correct destination path based on build configuration"""
    build_config = config_data['build_config']
    dirs = config_data['directories']
    warno_mods = Path(dirs['warno_mods'])
    
    if build_config['target'] == 'gameplay':
        dest = dirs['gameplay_dev'] if build_config['write_dev'] else dirs['gameplay_release']
    else:  # ui_only
        dest = dirs['ui_only_dev'] if build_config['write_dev'] else dirs['ui_only_release']
    return warno_mods / dest
