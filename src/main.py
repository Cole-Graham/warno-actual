from src import config, get_mod_directories

# Use the config directly as loaded by ConfigLoader
get_mod_directories(config)  # No need to call load() again, it was done in __init__.py
