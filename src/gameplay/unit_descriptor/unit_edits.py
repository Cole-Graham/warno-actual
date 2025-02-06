"""Unit descriptor editing functionality."""

from typing import Any, Dict

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_namespace, get_modules_list  # , is_obj_type

logger = setup_logger(__name__)


def edit_units(source_path: Any, game_db: Dict[str, Any]) -> None:
    """Edit unit descriptors."""
    logger.info("Starting UniteDescriptor.ndf modifications")

    units_processed = 0
    units_modified = 0
    unit_edits = load_unit_edits()
    dictionary_entries = []  # Create list to collect entries

    _handle_supply(source_path, game_db, unit_edits)

    for unit_row in source_path:
        units_processed += 1

        # Skip if no namespace
        if not hasattr(unit_row, 'namespace'):
            continue

        unit_name = unit_row.namespace.replace("Descriptor_Unit_", "")

        try:
            # Debug logging
            logger.debug(f"Processing unit: {unit_name}")

            # Get edits for this unit
            edits = find_namespace(unit_row, unit_edits, prefix="Descriptor_Unit_")
            if edits is None:
                logger.info(f"No edits found for {unit_name}")
                continue

            logger.info(f"Applying edits to {unit_name}")
            units_modified += 1

            # Get modules list
            modules_list = get_modules_list(unit_row.v, "ModulesDescriptors")
            if not modules_list:
                logger.warning(f"No ModulesDescriptors found for {unit_name}")
                continue

            # Process each module
            for i, descr_row in enumerate(modules_list.v, start=0):  # noqa
                if not isinstance(descr_row.v, ndf.model.Object):
                    continue

                modify_module(unit_row, descr_row, edits, i, modules_list, dictionary_entries)

        except Exception as e:
            logger.error(f"Error processing {unit_name}: {str(e)}")
            continue

    # Write all dictionary entries at once
    if dictionary_entries:
        logger.info(f"Writing {len(dictionary_entries)} dictionary entries")
        write_dictionary_entries(dictionary_entries, dictionary_type="units")

    logger.info(f"Processed {units_processed} units total")
    logger.info(f"Modified {units_modified} units")


def modify_module(unit_row: Any, descr_row: Any, edits: dict, index: int,
                  modules_list: list, dictionary_entries: list) -> None:
    """Apply edits to a specific module based on its type."""
    if not hasattr(descr_row.v, 'type'):
        return

    descr_type = descr_row.v.type
    namespace = None
    if hasattr(descr_row, "namespace"):
        namespace = descr_row.namespace

    # Get unit name for logging
    unit_name = unit_row.namespace.replace("Descriptor_Unit_", "") if hasattr(unit_row, 'namespace') else "Unknown"

    try:
        # Map module types to their handlers
        module_handlers = {
            "TTagsModuleDescriptor": _handle_tags,
            "TVisibilityModuleDescriptor": _handle_visibility,
            "TBaseDamageModuleDescriptor": _handle_base_damage,
            "TDamageModuleDescriptor": _handle_damage,
            "TInfantrySquadWeaponAssignmentModuleDescriptor": _handle_weapon_assignment,
            "TScannerConfigurationDescriptor": _handle_scanner,
            "TProductionModuleDescriptor": _handle_production,
            "TTacticalLabelModuleDescriptor": _handle_tactical_label,
            "TStrategicDataModuleDescriptor": _handle_strategic_data,
            "TIconModuleDescriptor": _handle_icon,
            "TUnitUIModuleDescriptor": _handle_unit_ui,
            "TDeploymentShiftModuleDescriptor": _handle_deployment_shift,
            "TZoneInfluenceMapModuleDescriptor": _handle_zone_influence,
            "TTransportableModuleDescriptor": _handle_transportable,
        }

        # Handle special namespace cases
        if namespace:
            if namespace == "GroupeCombat" and "strength" in edits:
                descr_row.v.by_m("Default").v.by_m("NbSoldatInGroupeCombat").v = str(edits["strength"])

            elif namespace == "GenericMovement" and "max_speed" in edits:
                descr_row.v.by_m("Default").v.by_m("MaxSpeedInKmph").v = str(edits["max_speed"])

            elif namespace == "LandMovement" and "road_speed" in edits:
                if "factor" in edits["road_speed"]:
                    factor = edits["road_speed"]["factor"]
                    descr_row.v.by_m("Default").v.by_m("SpeedBonusFactorOnRoad").v = "{:0.2f}".format(factor)
                elif "road_speed" in edits["road_speed"] and "base_speed" in edits["road_speed"]:
                    factor = edits["road_speed"]["road_speed"] / edits["road_speed"]["base_speed"]
                    descr_row.v.by_m("Default").v.by_m("SpeedBonusFactorOnRoad").v = "{:0.2f}".format(factor)

            elif namespace == "AirplaneMovement":
                if "max_speed" in edits:
                    descr_row.v.by_m("SpeedInKmph").v = str(edits["max_speed"])
                if "AirplaneMovement" in edits:
                    if "parent_membr" in edits["AirplaneMovement"]:
                        for key, value in edits["AirplaneMovement"]["parent_membr"].items():
                            descr_row.v.by_m(key).v = str(value)

            elif namespace == "Transporter":
                if "is_prime_mover" in edits:

                    transport_tags = descr_row.v.by_m("Default").v.by_m("TransportableTagSet")

                    if edits["is_prime_mover"]:
                        transport_tags.v = ndf.convert(str(["Crew", "Unite_transportable"]))
                        logger.info(f"Updated {unit_row.namespace} to prime mover")

                    else:
                        transport_tags.v = ndf.convert(str(["Crew"]))
                        logger.info(f"Updated {unit_row.namespace} to regular transport")

        # Apply module-specific handler if it exists
        if handler := module_handlers.get(descr_type):
            handler(unit_row, descr_row, edits, index, modules_list, dictionary_entries)

    except Exception as e:
        logger.error(f"Error modifying module for {unit_name}: {str(e)}")


def _handle_tags(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:

    if "TagSet" not in edits:
        return

    tagset = descr_row.v.by_m("TagSet").v
    if "overwrite_all" in edits["TagSet"]:
        tagset.v = ndf.convert(str(edits["TagSet"]["overwrite_all"]))
    elif "add_tags" in edits["TagSet"]:
        for tag in edits["TagSet"]["add_tags"]:
            tagset.add(tag)
            logger.info(f"Added tag {tag} to {unit_row.namespace}")


def _handle_visibility(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:  # noqa
    if "stealth" in edits:
        descr_row.v.by_m("UnitConcealmentBonus").v = str(edits["stealth"])


def _handle_base_damage(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:  # noqa
    if "strength" in edits:
        descr_row.v.by_m("MaxPhysicalDamages").v = str(edits["strength"])


def _handle_damage(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:  # noqa
    if "armor" in edits:
        blindage_obj = descr_row.v.by_m("BlindageProperties").v
        armor_parts = {
            "front": "ResistanceFront",
            "sides": "ResistanceSide",
            "rear": "ResistanceRear",
            "top": "ResistanceTop"
        }
        for part, resistance in armor_parts.items():
            if part in edits["armor"]:
                blindage_obj.by_m(resistance).v.by_m("Index").v = str(edits["armor"][part])
        if "era" in edits["armor"]:
            blindage_obj.by_m("ExplosiveReactiveArmor").v = str(edits["armor"]["era"])

    if "ECM" in edits:
        descr_row.v.by_m("HitRollECM").v = str(edits["ECM"])


def _handle_weapon_assignment(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:  # noqa
    if "WeaponAssignment" in edits:
        descr_row.v.by_m("InitialSoldiersToTurretIndexMap").v = "MAP" + str(edits["WeaponAssignment"])


def _handle_airplane_movement(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:  # noqa
    if "max_speed" in edits:
        descr_row.v.by_m("SpeedInKmph").v = str(edits["max_speed"])


def _handle_scanner(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:  # noqa
    if "optics" not in edits:
        return

    if "OpticalStrength" in edits["optics"]:
        descr_row.v.by_m("OpticalStrength").v = str(edits["optics"]["OpticalStrength"])

    if "OpticalStrengthAltitude" in edits["optics"]:
        descr_row.v.by_m("OpticalStrengthAltitude").v = str(
            edits["optics"]["OpticalStrengthAltitude"])
        if "SpecialtiesList" in edits and "add_specs" in edits["SpecialtiesList"]:
            for spec in edits["SpecialtiesList"]["add_specs"]:
                if spec == "'verygood_airoptics'":
                    # descr_row.v.by_m("OpticalStrengthAltitude").v = "5000.0"
                    specialized_detections = descr_row.v.by_m("SpecializedDetectionsGRU")
                    specialized_detections.v.by_k("EVisionUnitType/AlwaysInHighAltitude").v = "12000.0"
                elif spec == "'good_airoptics'":
                    specialized_detections = descr_row.v.by_m("SpecializedDetectionsGRU")
                    specialized_detections.v.by_k("EVisionUnitType/AlwaysInHighAltitude").v = "15000.0"

    if "SpecializedOpticalStrengths" in edits["optics"]:
        for key, value in edits["optics"]["SpecializedOpticalStrengths"].items():
            descr_row.v.by_m("SpecializedOpticalStrengths").v.by_k(key).v = str(value)


def _handle_production(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:  # noqa
    if "CommandPoints" in edits:
        cmd_points = "$/GFX/Resources/Resource_CommandPoints"
        descr_row.v.by_m("ProductionRessourcesNeeded").v.by_k(cmd_points).v = str(edits["CommandPoints"])

    if "Factory" in edits:
        descr_row.v.by_m("Factory").v = edits["Factory"]


def _handle_tactical_label(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:  # noqa
    if "SortingOrder" in edits:
        descr_row.v.by_m("MultiSelectionSortingOrder").v = str(edits["SortingOrder"])
    if "strength" in edits:
        descr_row.v.by_m("NbSoldiers").v = str(edits["strength"])


def _handle_strategic_data(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:  # noqa
    if "UnitAttackValue" in edits:
        descr_row.v.by_m("UnitAttackValue").v = str(edits["UnitAttackValue"])
        descr_row.v.by_m("UnitDefenseValue").v = str(edits["UnitDefenseValue"])


def _handle_icon(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:  # noqa
    if "IdentifiedTextures" in edits:
        descr_row.v.by_m("IdentifiedTextures").v = str(edits["IdentifiedTextures"])
        descr_row.v.by_m("UnidentifiedTextures").v = str(edits["UnidentifiedTextures"])


def _handle_unit_ui(unit_row: Any, descr_row: Any, edits: dict, index: int, modules_list: list,
                    dictionary_entries: list) -> None:
    """Handle UI module modifications."""
    if "SpecialtiesList" in edits:
        specialties_list = descr_row.v.by_m("SpecialtiesList")
        if "overwrite_all" in edits["SpecialtiesList"]:
            specialties_list.v = ndf.convert(str(edits["SpecialtiesList"]["overwrite_all"]))
        elif "add_specs" in edits["SpecialtiesList"]:
            for spec in edits["SpecialtiesList"]["add_specs"]:
                specialties_list.v.add(spec)
                logger.info(f"Added specialty {spec} to {unit_row.namespace}")
        if "remove_specs" in edits["SpecialtiesList"]:
            for spec in edits["SpecialtiesList"]["remove_specs"]:
                for tag in specialties_list.v:
                    if tag.v == spec:
                        specialties_list.v.remove(tag.index)
                        logger.info(f"Removed specialty {spec} from {unit_row.namespace}")

    if edits.get("GameName", {}).get("display"):
        # check if token was provided
        token = edits.get("GameName", {}).get("token")
        rename = edits["GameName"]["display"]
        if token:  # if new token provided, replace unit token with the new one
            descr_row.v.by_m("NameToken").v = f"'{token}'"
            logger.debug(f"Updated name token for {unit_row.namespace}")
        else:  # otherwise, grab unit's current token
            token = descr_row.v.by_m("NameToken").v[1:-1]

        # Collect the dictionary entry
        dictionary_entries.append((token, rename))
        logger.debug(f"Collected dictionary entry: {token} = {rename}")

    if "road_speed" in edits and "road_speed" in edits["road_speed"]:
        descr_row.v.by_m("DisplayRoadSpeedInKmph").v = str(edits["road_speed"]["road_speed"])

    if "UpgradeFromUnit" in edits:
        if descr_row.v.by_m("UpgradeFromUnit", False) is not None:
            if edits["UpgradeFromUnit"] is None:
                descr_row.v.remove_by_member("UpgradeFromUnit")
            else:
                descr_row.v.by_m("UpgradeFromUnit").v = f"Descriptor_Unit_{edits['UpgradeFromUnit']}"
        elif edits["UpgradeFromUnit"] is not None:
            descr_row.v.add(f"UpgradeFromUnit = Descriptor_Unit_{edits['UpgradeFromUnit']}")

    if "MenuIconTexture" in edits:
        descr_row.v.by_m("MenuIconTexture").v = "'" + edits["MenuIconTexture"] + "'"

    if "ButtonTexture" in edits:
        button_texture = "'Texture_Button_Unit_" + edits["ButtonTexture"] + "'"
        descr_row.v.by_m("ButtonTexture").v = button_texture

    if "TypeStrategicCount" in edits:
        descr_row.v.by_m("TypeStrategicCount").v = edits["TypeStrategicCount"]

    if "orders" in edits and "add_orders" in edits["orders"]:
        if "sell" in edits["orders"]["add_orders"]:
            sell_module = (
                'TModuleSelector('
                '    Default = TSellModuleDescriptor()'
                '    Condition = ~/IfNotCadavreCondition'
                '),'
            )
            modules_list.v.insert(index + 1, sell_module)  # noqa


def _handle_deployment_shift(unit_row: Any, descr_row: Any, edits: dict, index: int, modules_list: list, *_) -> None:
    """Handle deployment shift module removal."""
    if "DeploymentShift" in edits and edits["DeploymentShift"] == 0:
        descr_type = descr_row.v.type
        modules_list.v.remove(index)  # noqa
        logger.info(f"Removed {descr_type} from {unit_row.namespace}")


def _handle_supply(source_path, game_db, unit_edits, *_) -> None:  # noqa
    """Edit supply type for new supply ranges in UniteDescriptor.ndf, as well as
    supply capacities.

    Args:
        source_path: The NDF file being edited
        game_db: The game database
    """
    logger.info("Editing UniteDescriptor.ndf")

    unit_data = game_db["unit_data"]

    from src.constants.unit_edits.SUPPLY_unit_edits import supply_unit_edits

    for unit, data in unit_data.items():
        if not data["is_supply_unit"]:
            continue

        if unit not in supply_unit_edits:
            continue

        is_helo = data["is_helo_unit"]
        edits = supply_unit_edits[unit]

        try:
            # Get unit descriptor
            unit_descr = source_path.by_n(f"Descriptor_Unit_{unit}")
            if not unit_descr:
                logger.warning(f"Unit descriptor not found for {unit}")
                continue

            # Get ModulesDescriptors list
            modules_list = get_modules_list(unit_descr.v, "ModulesDescriptors")
            if not modules_list:
                logger.warning(f"No ModulesDescriptors found for {unit}")
                continue

            # Find TSupplyModuleDescriptor
            for module in modules_list.v:  # noqa
                if not hasattr(module.v, 'type'):
                    continue
                membr = module.v.by_m

                if module.v.type == "TSupplyModuleDescriptor":

                    try:
                        supply_descr = membr("SupplyDescriptor")
                        supply_capacity = membr("SupplyCapacity")

                        if not supply_descr or not supply_capacity:
                            logger.warning(f"Missing supply descriptors for {unit}")
                            continue

                        old_capacity = supply_capacity.v

                        # Update supply type based on unit type
                        if is_helo:
                            if edits.get("is_small", False):
                                supply_descr.v = "$/GFX/Weapon/SmallHeloSupply"
                                logger.info(f"Set {unit} to SmallHeloSupply")
                            else:
                                supply_descr.v = "$/GFX/Weapon/HeloSupply"
                                logger.info(f"Set {unit} to HeloSupply")

                        # Update capacity if specified
                        if "SupplyCapacity" in edits:
                            new_capacity = str(edits["SupplyCapacity"])
                            if old_capacity != new_capacity:
                                supply_capacity.v = new_capacity
                                logger.info(f"Updated {unit} supply capacity: {old_capacity} -> {new_capacity}")

                    except Exception as e:
                        logger.error(f"Error updating supply module for {unit}: {str(e)}")

                elif module.v.type == "TProductionModuleDescriptor":
                    if "CommandPoints" in edits:
                        key = "$/GFX/Resources/Resource_CommandPoints"
                        production_resources = membr("ProductionRessourcesNeeded").v.by_k(key)
                        production_resources.v = str(edits["CommandPoints"])
                        logger.info(f"Updated {unit} command points to: {edits['CommandPoints']}")

        except Exception as e:
            logger.error(f"Error processing {unit}: {str(e)}")


def _handle_zone_influence(unit_row: Any, descr_row: Any, edits: dict, index: int, modules_list: list, *_) -> None:  # noqa
    """Remove zone capture capability."""
    if "remove_zone_capture" in edits:
        modules_list.v.remove(index)  # noqa
        logger.info(f"Removed zone capture from {unit_row.namespace}")


def _handle_transportable(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:
    """Handle transportable module edits."""
    if "TransportedTexture" in edits:
        descr_row.v.by_m("TransportedTexture").v = f'"{edits["TransportedTexture"]}"'
        logger.debug(f"Updated transported texture for {unit_row.namespace}")


def temp_fix_reco_radar(source_path: Any, game_db: Dict[str, Any]) -> None:
    """2025/02/3 temp fix to Eugen's mistake of adding reco_radar to units that don't have it"""
    unit_db = game_db["unit_data"]

    exceptions = [
        "AIFV_B_Radar_NL"
        "BMD_1_Reostat"
        "BRDM_1_PSNR1_POL"
        "BRM_1_DDR",
        "BRM_1_SOV",
        "BRM_1_POL",
        "FV103_Spartan_GSR_UK",
        "M113_GreenArcher_RFA"
        "M113A1B_Radar_BEL",
        "M981_FISTV_US",
        "TPZ_Fuchs_RASIT_RFA",
        "VAB_RASIT_FR",
        "ZSU_23_Shilka_reco_SOV",
    ]

    for unit_descr in source_path:
        if not hasattr(unit_descr, "namespace"):
            continue

        unit_name = unit_descr.namespace.replace("Descriptor_Unit_", "")

        if unit_name in exceptions:
            logger.info(f"{unit_name} is in the exceptions list, skipping")
            continue

        tag_list_data = unit_db[unit_name].get("tags", [])
        specialties_list_data = unit_db[unit_name].get("specialties", [])

        if "reco_radar" in tag_list_data and "_gsr" not in specialties_list_data:
            modules_list = get_modules_list(unit_descr.v, "ModulesDescriptors")

            for module in modules_list.v:  # noqa
                if not hasattr(module.v, 'type'):
                    continue
                
                if module.v.type == "TTagsModuleDescriptor":
                    tagset = module.v.by_m("TagSet")
                    for tag in tagset.v:
                        if tag.v == '"reco_radar"':
                            tagset.v.remove(tag)
                            logger.info(f"Removed 'reco_radar' tag from {unit_name}")
                            break
        
        elif "reco_radar" in tag_list_data and "_gsr" in specialties_list_data:
            logger.info(f"{unit_name} has reco_radar and _gsr, skipping")
