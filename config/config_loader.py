import os

import ruamel.yaml


class ConfigLoader:
    """Handles loading and validation of YAML configuration files."""

    def __init__(self, yaml_path):
        """Initialize the config loader with path to YAML file.
        
        Args:
            yaml_path (str): Path to the configuration YAML file
        """
        self.config_file_path = yaml_path
        self.config_data = None

    def load(self):
        """Load and validate the YAML configuration file.
        
        Returns:
            dict: The loaded configuration data
        """
        if not os.path.isfile(self.config_file_path):
            raise FileNotFoundError(f"Configuration file not found: {self.config_file_path}")

        try:
            with open(self.config_file_path, "r") as file:
                yaml = ruamel.yaml.YAML()
                self.config_data = yaml.load(file)
        except ruamel.yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML format: {e}")
        except PermissionError as e:
            raise ValueError(f"Permission denied reading config file: {e}")
        
        try:
            self._validate_config()
        except KeyError as e:
            raise ValueError(f"Missing required configuration key: {e}")
        
        return self.config_data

    def _validate_config(self):
        """Validates required configuration fields exist."""
        required_fields = ["write_dev", "directories"]
        required_dirs = ["warno_mods", "source_mod", "dev_mod", "release_mod", "textures"]
        
        for field in required_fields:
            if field not in self.config_data:
                raise KeyError(f"Missing required field: {field}")
        
        for dir_field in required_dirs:
            if dir_field not in self.config_data["directories"]:
                raise KeyError(f"Missing required directory: {dir_field}")

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
