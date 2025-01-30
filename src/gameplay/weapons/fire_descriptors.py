"""editing FireDescriptors.ndf"""

from src.utils.logging_utils import setup_logger
from src import ndf

logger = setup_logger(__name__)

def edit_fire_descriptors(source_path) -> None:
    """Edit FireDescriptors.ndf"""
    logger.info("Editing FireDescriptors.ndf")

    fire_descriptors = {
        ("NapalmMoyenBomb", "NapalmMoyen", True): {
            "DescriptorId": "5372aa53-0162-4d29-8d96-d52f48c8bb50",
            "TFireModuleDescriptor": {
                "TimeBetweenBurns": 0.6,
            },
        },
    }
    
    for (new_name, donor, is_new), data in fire_descriptors.items():
        if is_new:
            new_entry = source_path.by_name(f"Descriptor_Fire_{donor}").copy()
            new_entry.namespace = f"Descriptor_Fire_{new_name}"

            if "DescriptorId" in data:
                new_guid = f"GUID:{{{data['DescriptorId']}}}"
                new_entry.v.by_m("DescriptorId").v = new_guid
            else:
                logger.warning(f"New DescriptorId not found for donor {donor}")

            modules_list = new_entry.v.by_m("ModulesDescriptors")
            for module in modules_list.v:
                
                if not isinstance(module.v, ndf.model.Object):
                    continue
                module_type = module.v.type
                if not module_type in data:
                    continue
                
                for key, value in data["TFireModuleDescriptor"].items():
                    module.v.by_m(key).v = str(value)
                    
                source_path.add(new_entry)
                logger.info(f"Added Descriptor_Fire_{new_name} to FireDescriptors.ndf")
                
def change_fire_descriptors(source_path) -> None:
    """Change fire descriptors in Ammunition.ndf"""
    
    for ammo_descr in source_path:
        
        is_napalm = False
        is_bomb = False
        
        traits_list = ammo_descr.v.by_m("TraitsToken")
        if any("'napalm'" in trait.v for trait in traits_list.v):
            is_napalm = True
            
        minmax_category = ammo_descr.v.by_m("MinMaxCategory", None)
        if minmax_category and minmax_category.v == "MinMax_Bombe":
            is_bomb = True
        
        if is_napalm and is_bomb:
            ammo_descr.v.by_m("FireDescriptor").v = "Descriptor_Fire_NapalmMoyenBomb"
            logger.info(f"Changed fire descriptor for {ammo_descr.namespace} to "
                        "Descriptor_Fire_NapalmMoyenBomb")

                
