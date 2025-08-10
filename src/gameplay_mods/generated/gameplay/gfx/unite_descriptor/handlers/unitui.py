from typing import Any, Dict

from src import ndf


def handle_unitui_module(
    logger,
    game_db,
    unit_data,
    edit_type,
    unit_name,
    edits,
    module,
    *args,
) -> None:  # noqa
    """Handle TUnitUIModuleDescriptor for existing and new units"""
    dictionary_entries = args[0]
    
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        
        specialties_list = module.v.by_m("SpecialtiesList")
        
        if "SpecialtiesList" in edits:
            if "overwrite_all" in edits["SpecialtiesList"]:
                specialties_list.v = ndf.convert(str(edits["SpecialtiesList"]["overwrite_all"]))
            elif "add_specs" in edits["SpecialtiesList"]:
                for spec in edits["SpecialtiesList"]["add_specs"]:
                    specialties_list.v.add(spec)
                    logger.info(f"Added specialty {spec} to {unit_name}")
            if "remove_specs" in edits["SpecialtiesList"]:
                for spec in edits["SpecialtiesList"]["remove_specs"]:
                    for tag in specialties_list.v:
                        if tag.v == spec:
                            specialties_list.v.remove(tag.index)
                            logger.info(f"Removed specialty {spec} from {unit_name}")
        
        # Supply unit specialties
        if "SupplyDescriptor" in edits:
            if "RunnerSupply" in edits["SupplyDescriptor"]:
                specialties_list.v.add("'_supply_runner'")
            elif "SquadSupply" in edits["SupplyDescriptor"]:
                specialties_list.v.add("'_supply_squad'")
            elif "PrimarySupply" in edits["SupplyDescriptor"]:
                specialties_list.v.add("'_supply_primary'")
            elif "DvisionalSupply" in edits["SupplyDescriptor"]:
                specialties_list.v.add("'_supply_divisional'")

        if edits.get("GameName", {}).get("display"):
            # check if token was provided
            token = edits.get("GameName", {}).get("token")
            rename = edits["GameName"]["display"]
            if token:  # if new token provided, replace unit token with the new one
                module.v.by_m("NameToken").v = f"'{token}'"
                logger.debug(f"Updated name token for {unit_name}")
            else:  # otherwise, grab unit's current token
                token = module.v.by_m("NameToken").v[1:-1]

            # Collect the dictionary entry
            dictionary_entries.append((token, rename))
            logger.debug(f"Collected dictionary entry: {token} = {rename}")

        if "road_speed" in edits and "road_speed" in edits["road_speed"]:
            module.v.by_m("DisplayRoadSpeedInKmph").v = str(edits["road_speed"]["road_speed"])

        if "UpgradeFromUnit" in edits:
            if module.v.by_m("UpgradeFromUnit", False) is not None:
                if edits["UpgradeFromUnit"] is None:
                    module.v.remove_by_member("UpgradeFromUnit")
                else:
                    module.v.by_m("UpgradeFromUnit").v = f"Descriptor_Unit_{edits['UpgradeFromUnit']}"
            elif edits["UpgradeFromUnit"] is not None:
                module.v.add(f"UpgradeFromUnit = Descriptor_Unit_{edits['UpgradeFromUnit']}")

        if "MenuIconTexture" in edits:
            module.v.by_m("MenuIconTexture").v = "'" + edits["MenuIconTexture"] + "'"

        if "ButtonTexture" in edits:
            button_texture = "'Texture_Button_Unit_" + edits["ButtonTexture"] + "'"
            module.v.by_m("ButtonTexture").v = button_texture

        if "TypeStrategicCount" in edits:
            module.v.by_m("TypeStrategicCount").v = edits["TypeStrategicCount"]  # noqa