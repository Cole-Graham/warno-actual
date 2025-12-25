"""Asset copying utilities."""

import shutil
from pathlib import Path
from typing import Dict

from src.utils.logging_utils import log_time, setup_logger

logger = setup_logger(__name__)


def copy_assets(config: Dict) -> None:
    """Copy assets to mod directory.
    
    Args:
        config: Configuration dictionary containing paths
    """
    source_dir = Path("assets")  # Always copy from assets/
    if not source_dir.exists():
        logger.warning(f"Assets directory not found: {source_dir}")
        return
        
    # Get target mod path based on config
    warno_mods = Path(config['directories']['warno_mods'])
    build_config = config['build_config']
    build_target = build_config['target']
    
    # Determine mod type and target directory name
    if build_target == 'ui_only':
        target_mod = (config['directories']['ui_only_dev'] 
                     if build_config['write_dev'] 
                     else config['directories']['ui_only_release'])
        mod_type = 'ui_only'
    else:
        target_mod = (config['directories']['gameplay_dev']
                     if build_config['write_dev']
                     else config['directories']['gameplay_release'])
        mod_type = 'gameplay'
    
    # Target is GameData/assets/
    target_dir = warno_mods / target_mod / config['asset_config']['target_dir'] / source_dir.name
    
    with log_time(logger, "Copying assets"):
        gameplay_mod_assets = Path("assets/gameplaymod")
        ui_mod_assets = Path("assets/uimod")
        if not gameplay_mod_assets.exists() or not ui_mod_assets.exists():
            logger.warning(f"Assets directories not found: {gameplay_mod_assets} or {ui_mod_assets}")
            return
        
        # Walk through all files in assets directory
        if mod_type == 'gameplay':
            for source_file in gameplay_mod_assets.rglob('*'):
                # Skip readme.md
                if source_file.name.lower() == 'readme.md':
                    continue
                    
                if source_file.is_file():
                    # Get relative path from assets root
                    rel_path = source_file.relative_to(gameplay_mod_assets)
                    # Construct target path
                    target_path = target_dir / rel_path
                    
                    # Create target directory if needed
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    try:
                        shutil.copy2(source_file, target_path)
                        logger.debug(f"Copied {rel_path} to {target_path}")
                    except Exception as e:
                        logger.error(f"Failed to copy {rel_path}: {e}")

            for source_file in ui_mod_assets.rglob('*'):
                # Skip readme.md
                if source_file.name.lower() == 'readme.md':
                    continue
                    
                if source_file.is_file():
                    # Get relative path from assets root
                    rel_path = source_file.relative_to(ui_mod_assets)
                    # Construct target path
                    target_path = target_dir / rel_path
                    
                    # Create target directory if needed
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    try:
                        shutil.copy2(source_file, target_path)
                        logger.debug(f"Copied {rel_path} to {target_path}")
                    except Exception as e:
                        logger.error(f"Failed to copy {rel_path}: {e}")
        
        elif mod_type == 'ui_only':
            for source_file in ui_mod_assets.rglob('*'):
                # Skip readme.md
                if source_file.name.lower() == 'readme.md':
                    continue
                    
                if source_file.is_file():
                    # Get relative path from assets root
                    rel_path = source_file.relative_to(ui_mod_assets)
                    # Construct target path
                    target_path = target_dir / rel_path
                    
                    # Create target directory if needed
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    try:
                        shutil.copy2(source_file, target_path)
                        logger.debug(f"Copied {rel_path} to {target_path}")
                    except Exception as e:
                        logger.error(f"Failed to copy {rel_path}: {e}")