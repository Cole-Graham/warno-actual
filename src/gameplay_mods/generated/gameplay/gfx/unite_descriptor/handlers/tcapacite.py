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
    modules_list = args[1]
    # TODO: this is convoluted and uses inconsistent terminology. Capacitie translates to ability
    # in english, so I should just use that term consistently. I use "skill" and "capacitie"
    # interchangeably here when they mean the same thing, and also imply that the shock (Choc)
    # speciality is a "skill" when its a unit trait/specialty. I will refactor this later
    # and just use the terms "ability" and "trait" everywhere since its what these are called
    # in game. I also plan on fixing the names of capacities to make more sense. e.g. Deploy 
    # and Deploy_ok should be called Deploy and Deployed, implying the real meaning of what they do.
    # There is also a lot of redundant code between _add_capacite_module and _add_capacities.
    if not found_capacite_module:
        _add_capacite_module(logger, unit_data, edit_type, unit_name,
                             edits, module, modules_list)
    
    else:
        default_skill_list = module.v.by_m("DefaultSkillList")
        _add_capacities(logger, unit_data, edit_type, unit_name, edits, default_skill_list)
    

def _add_capacite_module(
    logger,
    unit_data,
    edit_type,
    unit_name,
    edits,
    module,
    modules_list,
) -> None:
    """Add a TCapaciteModuleDescriptor to a unit"""
    
    capacities_to_add = edits.get("capacities", {}).get("add_capacities", [])
    
    skills_to_add = {
        "skills": {
            "Choc": [
                "Choc_Move",
                "Choc_Move_ok",
                "no_Choc_Move",
            ],
        },
        "specialties": {
            "'_swift'": [
                "Swift",
                "no_Swift",
            ],
            "'infantry_equip_medium'": [
                "Medium_Cohesion_Loss",
            ],
            "'infantry_equip_heavy'": [
                "Medium_Cohesion_Loss",
            ],
            
        },
    }
    for condition_type, condition in skills_to_add.items():
        if condition_type == "skills":
            for skill, capacities in condition.items():
                if unit_data == None or not skill in unit_data.get("skills", []):
                    continue
                
                for capacity in capacities:
                    capacities_to_add.append(capacity)
        elif condition_type == "specialties":
            for specialty, capacities in condition.items():
                
                # Check if specialty is in database or being added in unit edits
                if unit_data == None or not specialty in unit_data.get("specialties", []):
                    specialty_in_database = False
                else:
                    specialty_in_database = True
                
                if edit_type == "unit_edits":
                    specialties_to_add = edits.get("SpecialtiesList", {}).get("add_specs", [])
                else:
                    specialties_to_add = edits.get("SpecialtiesList", [])
                
                if not specialty_in_database and not specialty in specialties_to_add:
                    continue
                
                # If so, add relevant capacities
                for capacity in capacities:
                    # This will resolve to True if 'capacity' is already in the 'capacities_to_add' list, otherwise False.
                    duplicate_safety = capacity in capacities_to_add
                    if not duplicate_safety:
                        capacities_to_add.append(capacity)
                        logger.info(f"Added {capacity} to {unit_name}")
    
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
        modules_list.v.add(capacities_module)
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
            "'infantry_equip_medium'": [
                "$/GFX/EffectCapacity/Capacite_Medium_Cohesion_Loss",
            ],
            "'infantry_equip_heavy'": [
                "$/GFX/EffectCapacity/Capacite_Medium_Cohesion_Loss",
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
                
                # Check if specialty is in database or being added in unit edits
                if unit_data == None or not specialty in unit_data.get("specialties", []):
                    specialty_in_database = False
                else:
                    specialty_in_database = True
                
                if edit_type == "unit_edits":
                    specialties_to_add = edits.get("SpecialtiesList", {}).get("add_specs", [])
                else:
                    specialties_to_add = edits.get("SpecialtiesList", [])
                
                if not specialty_in_database and not specialty in specialties_to_add:
                    continue
                
                # If so, add relevant capacities
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