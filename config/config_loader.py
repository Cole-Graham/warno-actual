import os

import ruamel.yaml


class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = None

    def load(self):
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

        try:
            with open(self.config_file, "r") as file:
                yaml = ruamel.yaml.YAML()
                self.config_data = yaml.load(file)
            self._validate_config()
            return self.config_data
        except Exception as e:
            raise ValueError(f"Error loading configuration: {e}")

    def _validate_config(self):
        """Validates required configuration fields exist"""
        required_fields = ["write_dev", "directories"]
        required_dirs = ["warno_mods", "source_mod", "dev_mod", "release_mod", "textures"]
        
        for field in required_fields:
            if field not in self.config_data:
                raise ValueError(f"Missing required field: {field}")
        
        for dir_field in required_dirs:
            if dir_field not in self.config_data["directories"]:
                raise ValueError(f"Missing required directory: {dir_field}")

    def get(self, key, default=None):
        """Returns the value for the given key, or default if not found."""
        if self.config_data is None:
            raise ValueError("Config data is not loaded. Call load() first.")
        return self.config_data.get(key, default)

    def get_directories(self):
        """Get the directories section of the configuration."""
        return self.get("directories", {})

    def get_write_dev(self):
        """Get the write_dev setting."""
        return self.get("write_dev", False)
