"""Configuration loading and validation."""

from pathlib import Path

import ruamel.yaml


class ConfigLoader:
    """Handles loading and validation of YAML configuration files."""

    def __init__(self, yaml_path: str):
        """Initialize the config loader with path to YAML file.
        
        Args:
            yaml_path (str): Path to the configuration YAML file
        """
        self.config_file_path = Path(yaml_path)
        self.config_data = None

    def load(self):
        """Load and validate the YAML configuration file.
        
        Returns:
            dict: The loaded configuration data
        """
        if not self.config_file_path.is_file():
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
        """Validate the configuration has all required fields."""
        # Check build_config section exists
        if 'build_config' not in self.config_data:
            raise KeyError("Missing required section: build_config")
        
        # Check required fields in build_config
        build_config_fields = [
            'write_dev',
            'target',
            'use_ui_as_base'
        ]
        
        for field in build_config_fields:
            if field not in self.config_data['build_config']:
                raise KeyError(f"Missing required field in build_config: {field}")
            
        # Check directories section exists
        if 'directories' not in self.config_data:
            raise KeyError("Missing required section: directories")
            
        # Check required directories exist
        required_dirs = [
            'warno_mods',
            'base_game',
            'ui_release',
            'ui_dev',
            'gameplay_dev',
            'ui_only_dev',
            'gameplay_release',
            'ui_only_release'
        ]
        
        for dir_field in required_dirs:
            if dir_field not in self.config_data['directories']:
                raise KeyError(f"Missing required directory: {dir_field}")

        # Validate asset configuration
        if 'asset_config' not in self.config_data:
            raise KeyError("Missing required section: asset_config")
        
        if 'target_dir' not in self.config_data['asset_config']:
            raise KeyError("Missing required field in asset_config: target_dir")

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
        build_config = self.get("build_config", {})
        return build_config.get("write_dev", False)
