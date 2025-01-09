import os

import ndf_parse as ndf

from config.config_loader import ConfigLoader


class ModConfig:
    _instance = None
    
    def __init__(self):
        config_file_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
        self.loader = ConfigLoader(config_file_path)
        self.loader.load()
        self.config_data = self.loader.config_data
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def get_mod_paths(cls):
        """Returns preconfigured source and destination paths"""
        instance = cls.get_instance()
        write_dev = instance.config_data.get("write_dev", True)
        dirs = instance.config_data["directories"]
        
        warno_mods = dirs["warno_mods"]
        source_mod = dirs["source_mod"]
        dest_mod = dirs["dev_mod" if write_dev else "release_mod"]
        
        return {
            "source": warno_mods + source_mod,
            "destination": warno_mods + dest_mod,
            "textures": dirs["textures"]
        }

    @classmethod
    def reset(cls):
        """Reset the singleton (useful for testing)"""
        cls._instance = None

__all__ = ["ModConfig"]
