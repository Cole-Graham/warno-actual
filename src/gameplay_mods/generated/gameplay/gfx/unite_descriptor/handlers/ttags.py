"""Edit TTagsModuleDescriptor for existing and new units"""

from src import ndf


def handle_tags_module(
    logger,
    game_db,
    unit_data,
    edit_type,
    unit_name   ,
    edits,
    module,
    *args,
) -> None:
    """Edit TTagsModuleDescriptor for existing and new units"""

    if edit_type == "new_units":
        pass

    if edit_type == "unit_edits":
        ammo_db = game_db["ammunition"]
        unit_db = game_db["unit_data"]
        weapon_db = game_db["weapons"]

        is_radar_unit = False
        if "AA_radar" in unit_db[unit_name]["tags"]:
            unit_turrets = weapon_db[f"WeaponDescriptor_{unit_name}"]["turrets"]
            for turret in unit_turrets:
                turret_ammos = unit_turrets[turret]["weapons"]
                for ammo in turret_ammos:
                    if f"Ammo_{ammo}" in ammo_db["radar_weapons"]:
                        is_radar_unit = True
                        break
                if is_radar_unit:
                    break

            if not is_radar_unit:
                tagset = module.v.by_m("TagSet")
                for tag in tagset.v:
                    if tag.v == '"AA_radar"':
                        tagset.v.remove(tag)
                        logger.info(f'Removed "AA_Radar" tag from {unit_name}')

        if "TagSet" not in edits:
            return

        tagset = module.v.by_m("TagSet")
        if "overwrite_all" in edits["TagSet"]:
            tagset.v = ndf.convert(str(edits["TagSet"]["overwrite_all"]))
        elif "add_tags" in edits["TagSet"]:
            for tag in edits["TagSet"]["add_tags"]:
                tagset.v.add(tag)
                logger.info(f"Added tag {tag} to {unit_name}")