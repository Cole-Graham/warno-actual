import os

import ndf_parse as ndf

from config.config_loader import ConfigLoader

from .utils import get_mod_directories

# Define path to your configuration file (adjust path as necessary)
config_file_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")

# Create a ConfigLoader instance and load the configuration
config_loader = ConfigLoader(config_file_path)
config_loader.load()

# Expose useful configuration globally
config = config_loader.config_data
write_dev = config_loader.get_write_dev()
directories = config_loader.get_directories()

__all__ = ["config", "get_mod_directories", "write_dev", "directories"]
