"""Edit TCapaciteModuleDescriptor for existing and new units"""

def handle_capacite_module(
    logger,
    game_db,
    unit_data,
    edit_type,
    unit_name,
    edits,
    module,
    *args,
) -> None:
    """Handle TCapaciteModuleDescriptor for existing and new units"""
    found_capacite_module = args[0]
    default_skill_list = module.v.by_m("DefaultSkillList")
    
    if not found_capacite_module:
        _add_capacite_module(logger, unit_data, edit_type, unit_name, edits, module)
    
    else:
        _add_capacities(logger, unit_data, edit_type, unit_name, edits, default_skill_list)
    

def _add_capacite_module(logger, unit_data, edit_type, unit_name, edits, module) -> None:
    """Add a TCapaciteModuleDescriptor to a unit"""
    
    capacities_to_add = edits.get("capacities", {}).get("add_capacities", [])
    
    if capacities_to_add:
        skill_prefix = "$/GFX/EffectCapacity/Capacite_"
        capacities_module = (
            f"TCapaciteModuleDescriptor"
            f"("
            f"        DefaultSkillList = ["
            f'            {", ".join(skill_prefix + skill for skill in capacities_to_add)}'
            f"        ]"
            f")"
        )
        module.v.add(capacities_module)
        logger.info(f"Added capacities module to {unit_name}")


def _add_capacities(logger, unit_data, edit_type, unit_name, edits, default_skill_list) -> None:
    """Add shock sprint capacities to a unit"""
    
    skills_to_add = {
        "skills": {
            "Choc": [
                "$/GFX/EffectCapacity/Capacite_Choc_Move",
                # "$/GFX/EffectCapacity/Capacite_Choc_Move_ok",
                "$/GFX/EffectCapacity/Capacite_no_Choc_Move",
            ],
        },
        "specialties": {
            "'_swift'": [
                "$/GFX/EffectCapacity/Capacite_Swift",
                "$/GFX/EffectCapacity/Capacite_no_Swift",
            ],
        },
    }
    
    for condition_type, condition in skills_to_add.items():
        # Skills in database condition
        if condition_type == "skills":
            for skill, capacities in condition.items():
                if unit_data == None or not skill in unit_data.get("skills", []):
                    continue
                
                for capacity in capacities:
                    duplicate_safety = default_skill_list.v.find_by_cond(
                        lambda x: x.v == capacity, strict=False
                    )
                    if not duplicate_safety:
                        default_skill_list.v.add(capacity)
                        logger.info(f"Added {capacity} to {unit_name}")
        
        # Specialties tags in database condition
        elif condition_type == "specialties":
            for specialty, capacities in condition.items():
                if unit_data == None or not specialty in unit_data.get("specialties", []):
                    continue
                
                for capacity in capacities:
                    duplicate_safety = default_skill_list.v.find_by_cond(
                        lambda x: x.v == capacity, strict=False
                    )
                    if not duplicate_safety:
                        default_skill_list.v.add(capacity)
                        logger.info(f"Added {capacity} to {unit_name}")
    
    # capacitie_to_add
    capacities_to_add = edits.get("capacities", {}).get("add_capacities", [])
    for capacity in capacities_to_add:
        default_skill_list.v.add(f"$/GFX/EffectCapacity/Capacite_{capacity}")
        logger.info(f"Added {capacity} capacities to {unit_name}")
    
    # capacities_to_remove
    capacities_to_remove = edits.get("capacities", {}).get("remove_capacities", [])
    for capacity in capacities_to_remove:
        default_skill_list.v.remove(f"$/GFX/EffectCapacity/Capacite_{capacity}")
        logger.info(f"Removed {capacity} capacities from {unit_name}")