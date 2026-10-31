from pathlib import Path
from typing import Any, Dict, List  # noqa

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


def is_dev_build(config: Dict) -> bool:
    """VIP builds are development builds. write_dev applies only when write_vip is false."""
    build_config = config['build_config']
    if build_config.get('write_vip'):
        return True
    return bool(build_config['write_dev'])


def get_base_mod_name(config: Dict) -> str:
    """Source mod folder name. VIP builds read base_vip."""
    dirs = config['directories']
    if config['build_config'].get('write_vip'):
        return dirs['base_vip']
    return dirs['base_game']


def get_mod_src_path(config: Dict) -> Path:
    """Get mod source directory path based on config."""
    warno_mods = Path(config['directories']['warno_mods'])
    return warno_mods / get_base_mod_name(config)


def get_mod_name(config: Dict) -> str:
    """Return the destination mod folder name for the current build target."""
    build_config = config['build_config']
    dirs = config['directories']
    target = build_config['target']
    write_vip = bool(build_config.get('write_vip'))

    if target == 'gameplay':
        if write_vip:
            return dirs['vip_dev']
        return dirs['gameplay_dev'] if build_config['write_dev'] else dirs['gameplay_release']
    if target == 'ui_only':
        if write_vip or build_config['write_dev']:
            return dirs['ui_only_dev']
        return dirs['ui_only_release']
    raise ValueError(f"Invalid build target: {target}")


def get_mod_dst_path(config_data: Dict) -> Path:
    """Determine the correct destination path based on build configuration"""
    dirs = config_data['directories']
    warno_mods = Path(dirs['warno_mods'])
    return warno_mods / get_mod_name(config_data)


def get_vanilla_units_csv_path(config: Dict) -> Path:
    """Path to vanilla UNITS.csv under ExampleAssets (warno_mods from config)."""
    warno_mods = Path(config['directories']['warno_mods'])
    return warno_mods / 'ExampleAssets' / 'Localisation' / 'UNITS.csv'
