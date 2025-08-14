from typing import Any, Dict
from src import ndf
from src.constants.weapons import missiles
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

def edit_gen_gp_gfx_missiledescriptors(source: Any, game_db: Dict[str, Any]) -> None:
    """GameData/Generated/Gameplay/Gfx/MissileDescriptors.ndf"""
    logger.info("Adjusting missile speed and acceleration")

    ammo_db = game_db["ammunition"]
    missile_inst_renames = ammo_db.get("renames_new_old", {})

    for missile_decr in source:
        # Strip Ammo_ prefix for comparison
        stripped_namespace = missile_decr.namespace.replace("Descriptor_Missile_", "")

        for (missile, category, donor, is_new), data in missiles.items():
            if data is None or "MissileDescriptor" not in data:
                continue

            # Check for renames
            if stripped_namespace in missile_inst_renames:
                stripped_namespace = missile_inst_renames[stripped_namespace]

            if missile != stripped_namespace:
                continue

            modules_list = missile_decr.v.by_m("ModulesDescriptors")
            for module in modules_list.v:
                if not isinstance(module.v, ndf.model.Object):
                    continue

                if module.v.type != "TGuidedMissileMovementModuleDescriptor":
                    continue

                default_cfg = module.v.by_m("DefaultConfig")
                uncontrollable_cfg = module.v.by_m("UncontrollableConfig")
                if "MaxSpeedGRU" in data["MissileDescriptor"]:
                    max_speed = data["MissileDescriptor"]["MaxSpeedGRU"]
                    default_cfg.v.by_m("MaxSpeedGRU").v = str(max_speed)  # noqa
                    logger.debug(f"Changed {missile_decr.namespace} max speed to {max_speed}")

                    uncontrollable_cfg.v.by_m("MaxSpeedGRU").v = str(max_speed)  # noqa
                    logger.debug(f"Changed {missile_decr.namespace} uncontrollable speed to {max_speed}")

                if "MaxAccelerationGRU" in data["MissileDescriptor"]:
                    max_accel = data["MissileDescriptor"]["MaxAccelerationGRU"]
                    default_cfg.v.by_m("MaxAccelerationGRU").v = str(max_accel)  # noqa
                    logger.debug(f"Changed {missile_decr.namespace} max acceleration to {max_accel}")

                if "AutoGyr" in data["MissileDescriptor"]:
                    auto_gyr = data["MissileDescriptor"]["AutoGyr"]
                    default_cfg.v.by_m("AutoGyr").v = str(auto_gyr)  # noqa
                    logger.debug(f"Changed {missile_decr.namespace} auto gyr to {auto_gyr} (90 degrees)")
            break