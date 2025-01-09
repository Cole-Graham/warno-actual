# config/config.py

import os

import ruamel.yaml

# Path to the YAML configuration file
config_file_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")


def load_config():
    with open(config_file_path, "r") as f:
        yaml = ruamel.yaml.YAML()
        config = yaml.load(f)  # Parse the YAML file
    return config
