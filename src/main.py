from src import ModConfig
from src.utils import process_mod


def main():
    # Get paths
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

    # Process mod
    process_mod(paths["source"], paths["destination"])

if __name__ == "__main__":
    main()
