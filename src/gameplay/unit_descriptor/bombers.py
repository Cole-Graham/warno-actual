"""misc. edits to bombers"""

from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_namespace, get_modules_list, ndf

logger = setup_logger("bombers")

def global_bomber_edits(source_path, game_db):
    """add terrain radar to bombers and adjust stealth"""
    unit_db = game_db["unit_data"]
    
    unit_edits = load_unit_edits()
    for unit_descr in source_path:
        edits = find_namespace(unit_descr, unit_edits, prefix="Descriptor_Unit_")
        if edits is None:
            continue
        
        unit_name = unit_descr.namespace.replace("Descriptor_Unit_", "")
        
        has_terrain_radar = False
        dive_attack = False
        is_sead = False
        if "SpecialtiesList" in edits:
            if "add_specs" in edits["SpecialtiesList"]:
                if "'terrain_radar'" in edits["SpecialtiesList"]["add_specs"]:
                    has_terrain_radar = True
        
        attack_strategies = unit_db[unit_name].get("attack_strategies", None)
        if attack_strategies and "DiveBombAttackStrategyDescriptor" in attack_strategies:
            dive_attack = True
            
        tags = unit_db[unit_name].get("tags", None)
        if tags and "Avion_SEAD" in tags:
            is_sead = True
                    
        modules_list = get_modules_list(unit_descr.v, "ModulesDescriptors")
        if not modules_list:
            continue
        
        for module in modules_list.v:
            if not isinstance(module.v, ndf.model.Object):
                continue
            
            module_type = module.v.type
            
            if module_type == "TVisibilityModuleDescriptor" and has_terrain_radar:
                module.v.by_m("UnitConcealmentBonus").v = "1.5"
                logger.debug(f"Set {unit_name} concealment bonus to 1.5")
                
            elif module_type == "AirplaneMovementDescriptor" and has_terrain_radar:
                if is_sead:
                    module.v.by_m("AltitudeGRU").v = "300"
                else:
                    module.v.by_m("AltitudeGRU").v = "125"
                logger.debug(f"Set {unit_name} altitude to 125m")
                    
            elif module_type == "TUnitUIModuleDescriptor":
                if dive_attack:
                    module.v.by_m("SpecialtiesList").v.add("'dive_attack'")
                    logger.debug(f"Added dive_attack to {unit_name}")
