from src import ModConfig, ndf


def main():
    # Get paths from ModConfig
    paths = ModConfig.get_instance().get_mod_paths()
    
    # Print configuration details
    print("\nConfiguration Details:")
    print("-" * 50)
    print(f"Write to Dev: {ModConfig.get_instance().config_data['write_dev']}")
    print("\nPaths:")
    print("-" * 50)
    print(f"Source Path:      {paths['source']}")
    print(f"Destination Path: {paths['destination']}")
    print(f"Textures Path:    {paths['textures']}")
    print("-" * 50)
    
    mod = ndf.Mod(paths["source"], paths["destination"])
    mod.check_if_src_is_newer()


if __name__ == "__main__":
    main()
