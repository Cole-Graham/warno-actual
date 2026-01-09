"""Edit TExperienceModuleDescriptor for existing and new units"""

def handle_experience_module(
    logger,
    game_db,
    unit_data,
    edit_type,
    unit_name,
    edits,
    module,
    *args,
) -> None:
    """Handle TExperienceModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        _set_multiplicative_xp_pack(logger, unit_data, edit_type, unit_name, edits, module)

    if edit_type == "unit_edits":
        _set_multiplicative_xp_pack(logger, unit_data, edit_type, unit_name, edits, module)
                
            
def _set_multiplicative_xp_pack(logger, unit_data, edit_type, unit_name, edits, module) -> None:
    """Set the multiplicative accuracy XP pack for infantry units"""
    if edit_type == "new_units":
        required_tags = ["Infanterie"]
        invalid_tags = ["Infanterie_AA", "Infanterie_AT"]
        new_unit_tags = edits["TagSet"]["overwrite_all"]
        if all(tag in new_unit_tags for tag in required_tags):
            if not any(tag in new_unit_tags for tag in invalid_tags):
                xp_pack = module.v.by_m("ExperienceLevelsPackDescriptor")
                if xp_pack.v.endswith("SF_v2"):
                    xp_pack.v = "~/ExperienceLevelsPackDescriptor_XP_pack_SF_v2_multiplicative"
                    logger.info(f"Set {unit_name} XP pack to {xp_pack.v}")
                elif xp_pack.v.endswith("simple_v3"):
                    xp_pack.v = "~/ExperienceLevelsPackDescriptor_XP_pack_simple_v3_multiplicative"
                    logger.info(f"Set {unit_name} XP pack to {xp_pack.v}")
    
    elif edit_type == "unit_edits":
        required_tags = ["Infanterie"]
        invalid_tags = ["Infanterie_AA", "Infanterie_AT"]
        tags = unit_data["tags"]
        if all(tag in tags for tag in required_tags):
            if not any(tag in tags for tag in invalid_tags):
                xp_pack = module.v.by_m("ExperienceLevelsPackDescriptor")
                if xp_pack.v.endswith("SF_v2"):
                    xp_pack.v = "~/ExperienceLevelsPackDescriptor_XP_pack_SF_v2_multiplicative"
                    logger.info(f"Set {unit_name} XP pack to {xp_pack.v}")
                elif xp_pack.v.endswith("simple_v3"):
                    xp_pack.v = "~/ExperienceLevelsPackDescriptor_XP_pack_simple_v3_multiplicative"
                    logger.info(f"Set {unit_name} XP pack to {xp_pack.v}")