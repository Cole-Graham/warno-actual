import os

import ruamel.yaml


class ConfigLoader:
    def __init__(self, config_file):
        # Initialize with the path to the configuration file
        self.config_file = config_file
        self.config_data = None

    def load(self):
        """Loads the configuration from the YAML file."""
        if not os.path.isfile(self.config_file):
            raise FileNotFoundError(f"Configuration file not found: {self.config_file}")

        try:
            with open(self.config_file, "r") as file:
                yaml = ruamel.yaml.YAML()
                self.config_data = yaml.load(file)
        except Exception as e:
            raise ValueError(f"Error loading configuration: {e}")

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
