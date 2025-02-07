"""Main entry point for the mod patcher."""
from typing import Dict

from . import ModConfig, ndf
from .editors import get_all_editors
from .utils.asset_utils import copy_assets
from .utils.config_utils import get_mod_dst_path, get_mod_src_path
from .utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def main() -> None:
    """Run the mod patcher."""
    try:
        config = ModConfig.get_instance().config_data
        
        # Get paths and initialize mod
        mod_src_path = get_mod_src_path(config)
        mod_dst_path = get_mod_dst_path(config)
        mod = ndf.Mod(mod_src_path, mod_dst_path)
        mod.check_if_src_is_newer()
        
        # Get all file editors based on build target
        editors = get_all_editors(config)
        
        # Process each file
        for file_path, editor_list in editors.items():
            if not editor_list:  # Skip empty editor lists
                continue
                
            try:
                logger.info(f"Processing {file_path}")
                with mod.edit(file_path) as source:
                    for editor in editor_list:
                        try:
                            editor(source)
                        except Exception as e:
                            logger.error(f"Editor failed for {file_path}: {str(e)}")
                            raise
                            
            except Exception as e:
                logger.error(f"Failed processing {file_path}: {str(e)}")
                raise
                
        # Copy assets
        copy_assets(config)
        
        logger.info("Build completed successfully")
        
    except Exception as e:
        logger.error(f"Build failed: {str(e)}")
        raise

if __name__ == "__main__":
    main()
