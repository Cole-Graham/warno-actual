from typing import Any, Dict

from src import ndf
from src.utils.ndf_utils import determine_characteristics


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
    donor = args[1]
        
    # Global bomber edits TODO: Use dic references instead for standardization
    if edit_type == "unit_edits":
        search_conditions = [
            ("uses_dive_bomb", "DiveBombAttackStrategyDescriptor", unit_data.get("attack_strategies", {})),
        ]
        uses_dive_bomb, = determine_characteristics(search_conditions)
        if uses_dive_bomb:
            module.v.by_m("SpecialtiesList").v.add("'dive_attack'")
            logger.info(f"Added dive_attack specialty to {unit_name}")
    
    if "UnitRole" in edits:
        module.v.by_m("UnitRole").v = "'" + edits["UnitRole"] + "'"
    
    specialties_list = module.v.by_m("SpecialtiesList")
    if "SpecialtiesList" in edits:
        if edit_type == "unit_edits":
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
        
        if edit_type == "new_units":
            edited_list = ndf.convert(str(edits["SpecialtiesList"]))
            specialties_list.v = edited_list
    
    # Supply unit specialties
    if "SupplyDescriptor" in edits:
        if "RunnerSupply" in edits["SupplyDescriptor"]:
            specialties_list.v.add("'_supply_runner'")
        elif "RunnerHeloSupply" in edits["SupplyDescriptor"]:
            specialties_list.v.add("'_supply_runner_helo'")
        elif "SquadSupply" in edits["SupplyDescriptor"]:
            specialties_list.v.add("'_supply_squad'")
        elif "PrimarySupply" in edits["SupplyDescriptor"]:
            specialties_list.v.add("'_supply_primary'")
        elif "PrimaryHeloSupply" in edits["SupplyDescriptor"]:
            specialties_list.v.add("'_supply_primary_helo'")
        elif "DvisionalSupply" in edits["SupplyDescriptor"]:
            specialties_list.v.add("'_supply_divisional'")
        elif "DvisionalHeloSupply" in edits["SupplyDescriptor"]:
            specialties_list.v.add("'_supply_divisional_helo'")

    if "InfoPanelConfig" in edits:
        module.v.by_m("InfoPanelConfigurationToken").v = f"'{edits['InfoPanelConfig']}'"
    
    # If display name isn't being changed, check if donor unit had its vanilla token modified
    if edit_type == "new_units" and not edits.get("GameName", {}):
        # check if token matches vanilla name token of donor unit
        vanilla_token = game_db["unit_data"].get(donor, {}).get("name_token")
        if not vanilla_token == module.v.by_m("NameToken").v[1:-1]:
            module.v.by_m("NameToken").v = f"'{vanilla_token}'"
            logger.debug(f"Corrected name token for new unit {unit_name} back to vanilla donor token {vanilla_token}")
 
    elif edits.get("GameName", {}).get("display"):
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
        # Check if member exists already
        if module.v.by_m("UpgradeFromUnit", False) is not None:
            if edits["UpgradeFromUnit"] is None:
                module.v.remove_by_member("UpgradeFromUnit")
            else:
                module.v.by_m("UpgradeFromUnit").v = f"Descriptor_Unit_{edits['UpgradeFromUnit']}"
        # If member doesn't exist, add it if dic value is not None (None -> remove module)
        elif edits["UpgradeFromUnit"] is not None:
            module.v.add(f"UpgradeFromUnit = Descriptor_Unit_{edits['UpgradeFromUnit']}")

    if "MenuIconTexture" in edits:
        module.v.by_m("MenuIconTexture").v = "'" + edits["MenuIconTexture"] + "'"
    
    # Check for custom button texture in edits, else default to unit name
    module.v.by_m("ButtonTexture").v = f"'Texture_Button_Unit_{edits.get('ButtonTexture', unit_name)}'"
    
    if "TypeStrategicCount" in edits:
        module.v.by_m("TypeStrategicCount").v = edits["TypeStrategicCount"]  # noqa