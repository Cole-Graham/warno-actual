"""Copy active map, scenario, and decor packs without running the patcher.

Uses config/config.YAML the same way the patcher does, including filling any
keys missing from config.template.YAML. Files go to the gameplay mod selected
by write_dev / write_vip (WARNO ACTUAL when write_dev is false). Files already
in those mod folders that are not on the allowlist are removed.
"""

from pathlib import Path

from config.config_loader import ConfigLoader
from src.utils.config_utils import get_mod_name, get_saved_games_warno_root
from src.utils.logging_utils import configure_logging
from src.utils.map_pack_copy import copy_active_map_packs

configure_logging()


def main() -> None:
    config_path = Path(__file__).resolve().parent / "config" / "config.YAML"
    config = ConfigLoader(str(config_path)).load()

    build = config["build_config"]
    # Running this script is the request to copy, even when copy_maps is off.
    build["copy_maps"] = True
    if build.get("target") != "gameplay":
        print(f"config target is {build.get('target')}; copying into the gameplay mod")
        build["target"] = "gameplay"

    destination = get_saved_games_warno_root(config) / "mod" / get_mod_name(config)
    print(f"Copying active map packs into {destination}")
    copy_active_map_packs(config)


if __name__ == "__main__":
    main()
