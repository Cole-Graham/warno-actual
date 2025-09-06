"""editing FireDescriptors.ndf"""

from src.utils.logging_utils import setup_logger
from src import ndf

logger = setup_logger(__name__)


def edit_gen_gp_gfx_firedescriptor(source_path) -> None:
    """GameData/Generated/Gameplay/Gfx/FireDescriptor.ndf"""
    logger.info("Editing FireDescriptor.ndf")

    fire_descriptors = {
        ("NapalmLeger_53m", "NapalmLeger", True): {
            "DescriptorId": "d2f2fea0-26c5-4256-bb0f-40384e8387b4",
            "TFireModuleDescriptor": {
                "RadiusGRU": 53,
                "AmmunitionForBurn": "$/GFX/Weapon/Ammo_Degats_napalm_leger_53m",
            },
        },
        ("NapalmLeger", None, False): {
            "TFireModuleDescriptor": {
                "RadiusGRU": 80,
            },
        },
        ("NapalmMoyenBomb", "NapalmMoyen", True): {
            "DescriptorId": "5372aa53-0162-4d29-8d96-d52f48c8bb50",
            "TFireModuleDescriptor": {
                "TimeBetweenBurns": 0.5,
            },
        },
    }

    for (name, donor, is_new), data in fire_descriptors.items():
        if is_new:
            new_entry = source_path.by_name(f"Descriptor_Fire_{donor}").copy()
            new_entry.namespace = f"Descriptor_Fire_{name}"

            if "DescriptorId" in data:
                new_guid = f"GUID:{{{data['DescriptorId']}}}"
                new_entry.v.by_m("DescriptorId").v = new_guid
            else:
                logger.warning(f"New DescriptorId not found for donor {donor}")
                
            new_entry.v.by_m("ClassNameForDebug").v = f"'FireDescriptor_{name}'"

            modules_list = new_entry.v.by_m("ModulesDescriptors")
            for module in modules_list.v:

                if not isinstance(module.v, ndf.model.Object):
                    continue
                module_type = module.v.type
                if module_type not in data:
                    continue

                for key, value in data["TFireModuleDescriptor"].items():
                    module.v.by_m(key).v = str(value)

                source_path.add(new_entry)
                logger.info(f"Added Descriptor_Fire_{name} to FireDescriptors.ndf")
        else:
            fire_descr = source_path.by_name(f"Descriptor_Fire_{name}")
            modules_list = fire_descr.v.by_m("ModulesDescriptors")
            for module in modules_list.v:
                if not isinstance(module.v, ndf.model.Object):
                    continue

                module_type = module.v.type
                if module_type == "TApparenceModuleDescriptor":
                    RadiusGRU = data.get("TFireModuleDescriptor", {}).get("RadiusGRU", None)
                    if RadiusGRU is not None:
                        depiction_obj = module.v.by_m("Depiction")
                        depiction_descriptor = depiction_obj.v.by_m("DepictionDescriptor")
                        depiction_descriptor.v.by_m("Radius").v = f"{RadiusGRU} * 26 * 2.83"
                elif module_type == "TFireModuleDescriptor":
                    for key, value in data["TFireModuleDescriptor"].items():
                        module.v.by_m(key).v = str(value)
