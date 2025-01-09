from src import config, get_mod_directories

# you have to run all src scripts through src package with 'python -m src.main'
# for debugging, there is a debugger configuration in the .code-workspace file

# Use the config directly as loaded by ConfigLoader
get_mod_directories(config)  # No need to call load() again, it was done in __init__.py
