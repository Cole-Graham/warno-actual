import os
from typing import Dict, Optional

import ndf_parse as ndf

from config.config_loader import ConfigLoader


class ModConfig:
    _instance: Optional['ModConfig'] = None
    
    def __init__(self) -> None:
        config_file_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
        
        self.loader: ConfigLoader
        self.config_data: Dict
        
        self.loader = ConfigLoader(yaml_path=config_file_path)
        self.loader.load()
        self.config_data = self.loader.config_data
    
    @classmethod
    def get_instance(cls) -> 'ModConfig':
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def get_mod_paths(cls) -> Dict[str, str]:
        """Returns the configured source and destination paths for mod processing.
        
        Returns:
            Dict[str, str]: Dictionary containing:
                - source: Path to source mod files
                - destination: Path to output directory (dev or release)
                - textures: Path to texture files
                
        Raises:
            ValueError: If configuration is invalid or missing required paths
        """
        try:
            instance = cls.get_instance()
            
            if not instance.config_data:
                raise ValueError("Configuration not loaded")
            
            try:
                write_dev = instance.config_data.get("write_dev", True)
                dirs = instance.config_data["directories"]
            except (AttributeError, TypeError) as e:
                raise ValueError(f"Invalid configuration structure: {e}")
            
            required = ["warno_mods", "source_mod", "dev_mod", "release_mod", "textures"]
            for path in required:
                if path not in dirs:
                    raise ValueError(f"Missing required path: {path}")
            
            try:
                warno_mods = dirs["warno_mods"]
                source_mod = dirs["source_mod"]
                dest_mod = dirs["dev_mod" if write_dev else "release_mod"]
                
                return {
                    "source": warno_mods + source_mod,
                    "destination": warno_mods + dest_mod,
                    "textures": dirs["textures"]
                }
            except (TypeError, KeyError) as e:
                raise ValueError(f"Error building paths: {e}")
            
        except Exception as e:
            raise ValueError(f"Unexpected error in get_mod_paths: {e}")

    @classmethod
    def reset(cls):
        """Reset the singleton (useful for testing)"""
        cls._instance = None


__all__ = ["ModConfig"]
