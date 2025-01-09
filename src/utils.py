def get_mod_directories(config):
    write_dev = config.get("write_dev", False)
    warno_mods = config["directories"].get("warno_mods")
    source_mod = config["directories"].get("source_mod")
    dev_mod = config["directories"].get("dev_mod")
    release_mod = config["directories"].get("release_mod")
    textures = config["directories"].get("textures")
    
    print(f"write_dev: {write_dev}")
    print(f"warno_mods: {warno_mods}")
    print(f"source_mod: {source_mod}")
    print(f"dev_mod: {dev_mod}")
    print(f"release_mod: {release_mod}")
    print(f"textures: {textures}")
    
    MOD_SRC = f"{warno_mods}" + f"{source_mod}"
    MOD_DST = f"{warno_mods}" + f"{dev_mod}"
    
    print()
    print(f"MOD_SRC: {MOD_SRC}")
    print(f"MOD_DEV: {MOD_DST}")