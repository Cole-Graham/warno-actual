"""Functions for modifying UniteDescriptor.ndf"""

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.constants.new_units import NEW_UNITS
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_type, find_obj_by_namespace, determine_characteristics

from .handlers import (
    handle_capacite_module,
    handle_experience_module,
    handle_supply_module,
    handle_tags_module,
    handle_unitui_module,
)

logger = setup_logger(__name__)

forward_deploy_old_values = []
forward_deploy_new_values = [750.0, 1750.0]

def edit_gen_gp_gfx_unitedescriptor(source_path, game_db) -> None:
    """GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf"""

    new_units_dic_entries = []
    _handle_new_units(source_path, game_db, new_units_dic_entries)
    
    unit_edits = load_unit_edits()
    unit_edits_dic_entries = []
    _handle_unit_edits(source_path, game_db, unit_edits, unit_edits_dic_entries)

    merged_dic_entries = unit_edits_dic_entries + new_units_dic_entries
    write_dictionary_entries(merged_dic_entries, dictionary_type="units")


def _handle_unit_edits(source_path, game_db, unit_edits, unit_edits_dic_entries) -> None:
    """Handle unit edits for existing units in UniteDescriptor.ndf"""
    logger.info("Processing unit edits for existing units:")
    
    for unit, edits in unit_edits.items():
        
        unit_name = unit
        descr_n = f"Descriptor_Unit_{unit_name}"
        modules_list = source_path.by_n(descr_n).v.by_m("ModulesDescriptors")
        _handle_modules_list(game_db, unit_edits_dic_entries, "unit_edits", None, unit_name, edits, modules_list)
        logger.info(f"- Processed unit edits for {unit_name}")
    
    forward_deploy_old_values.sort()
    logger.info(f"Forward deploy nerfed from {forward_deploy_old_values} to {forward_deploy_new_values}")


def _handle_new_units(source_path, game_db, new_units_dic_entries) -> None:
    """Handle new unit creation in UniteDescriptor.ndf"""
    logger.info("Processing new unit creation:")
    
    for donor, edits in NEW_UNITS.items():
        # Might already be handled by unitui.py handler
        # new_units_dic_entries.append((edits["GameName"]["token"], edits["GameName"]["display"]))
        
        unit_name = edits["NewName"]
        new_unit_descr = source_path.by_n(f"Descriptor_Unit_{donor[0]}").copy()
        new_unit_descr.namespace = f"Descriptor_Unit_{unit_name}"
        
        new_unit_descr.v.by_m("DescriptorId").v = f"GUID:{{{edits['GUID']}}}"
        new_unit_descr.v.by_m("ClassNameForDebug").v = f"'Unite_{edits['NewName']}'"

        modules_list = new_unit_descr.v.by_m("ModulesDescriptors")
        _handle_modules_list(game_db, new_units_dic_entries, "new_units", donor[0], unit_name, edits, modules_list)
        
        source_path.add(new_unit_descr)
        logger.info(f"- Processed new unit {unit_name}")


def _handle_modules_list(game_db, dictionary_entries, edit_type, donor, unit_name, edits, modules_list) -> None:
    """Handle modules list edits for new and existing units"""

    unit_data = game_db["unit_data"].get(unit_name, None)

    found_capacite_module = find_obj_by_type(modules_list.v, "TCapaciteModuleDescriptor") is not None
    found_zoneinfluence_module = find_obj_by_type(modules_list.v, "TZoneInfluenceMapModuleDescriptor") is not None

    module_handlers = {
        "TTypeUnitModuleDescriptor": { "handler": _handle_typeunit_module, "args": [] },
        "TFormationModuleDescriptor": { "handler": _handle_formation_module, "args": [] },
        "TTagsModuleDescriptor": { "handler": handle_tags_module, "args": [] },
        "TExperienceModuleDescriptor": { "handler": handle_experience_module, "args": [] },
        "TVisibilityModuleDescriptor": { "handler": _handle_visibility_module, "args": [] },
        "InfantryApparenceModuleDescriptor": { "handler": _handle_infantryapparence_module, "args": [] },
        "VehicleApparenceModuleDescriptor": { "handler": _handle_vehicleapparence_module, "args": [] },
        "TAutoCoverModuleDescriptor": { "handler": _handle_autocover_module, "args": [] },
        "TBaseDamageModuleDescriptor": { "handler": _handle_basedamage_module, "args": [] },
        "TDamageModuleDescriptor": { "handler": _handle_damage_module, "args": [] },
        "TDangerousnessModuleDescriptor": { "handler": _handle_dangerousness_module, "args": [] },
        # "TRoutModuleDescriptor": { "handler": handle_rout_module, "args": [] },
        "TInfantrySquadModuleDescriptor": { "handler": _handle_infantrysquad_module, "args": [] },
        "TGenericMovementModuleDescriptor": { "handler": _handle_genericmovement_module, "args": [] },
        # "THelicopterMovementModuleDescriptor": { "handler": handle_helicoptermovement_module, "args": [] },
        "TLandMovementModuleDescriptor": { "handler": _handle_landmovement_module, "args": [] },
        "AirplaneMovementDescriptor": { "handler": _handle_airplanemovement_module, "args": [donor] },
        # "TFuelModuleDescriptor": { "handler": handle_fuel_module, "args": [] },
        "TSupplyModuleDescriptor": { "handler": handle_supply_module, "args": [] },
        "TScannerConfigurationDescriptor": { "handler": _handle_scannerconfiguration_module, "args": [] },
        "TReverseScannerWithIdentificationDescriptor": { "handler": _handle_reversescanner_module, "args": [] },
        "TMissileCarriageModuleDescriptor": { "handler": _handle_missilecarriage_module, "args": [] },
        "TTransportableModuleDescriptor": { "handler": _handle_transportable_module, "args": [] },
        "TTransporterModuleDescriptor": { "handler": _handle_transporter_module, "args": [] },
        # "UnitCadavreGeneratorModuleDescriptor": { "handler": handle_unitcadavre_module, "args": [] },
        # "TIAStratModuleDescriptor": { "handler": handle_iastrat_module, "args": [] },
        "TCapaciteModuleDescriptor": { "handler": handle_capacite_module, "args": [found_capacite_module, modules_list] },
        "TProductionModuleDescriptor": { "handler": _handle_production_module, "args": [] },
        "TZoneInfluenceMapModuleDescriptor": { "handler": _handle_zoneinfluencemap_module, "args": [] },
        "TInfluenceScoutModuleDescriptor": { "handler": _handle_influencescout_module, "args": [] },
        # "TAutomaticBehaviorModuleDescriptor": { "handler": handle_automaticbehavior_module, "args": [] },
        "TCubeActionModuleDescriptor": { "handler": _handle_cubeaction_module, "args": [] },
        # "TMinimapDisplayModuleDescriptor": { "handler": handle_minimapdisplay_module, "args": [] },
        "TOrderConfigModuleDescriptor": { "handler": _handle_orderconfig_module, "args": [] },
        "TOrderableModuleDescriptor": { "handler": _handle_orderable_module, "args": [] },
        "TTacticalLabelModuleDescriptor": { "handler": _handle_tacticallabel_module, "args": [] },
        "TStrategicDataModuleDescriptor": { "handler": _handle_strategicdata_module, "args": [] },
        "TUnitUIModuleDescriptor": { "handler": handle_unitui_module, "args": [dictionary_entries, donor] },
        # "TUnitUpkeepModuleDescriptor": { "handler": handle_unitupkeep_module, "args": [] },
        "TDeploymentShiftModuleDescriptor": { "handler": _handle_deploymentshift_module, "args": [found_zoneinfluence_module] },
        "TCameraShowroomModuleDescriptor": { "handler": _handle_camerashowroom_module, "args": [] },
    }
    # Iterate over module handlers
    for module_type, handling_data in module_handlers.items():
        module = find_obj_by_type(modules_list.v, module_type)
        if not module:
            continue

        handling_data["handler"](logger, game_db, unit_data, edit_type, unit_name, 
                                 edits, module, *handling_data["args"])
    
    # Call handle_capacite_module if not found (otherwise it would have already been called)
    if not found_capacite_module:
        args = [found_capacite_module, modules_list]
        handle_capacite_module(logger, game_db, unit_data, edit_type, unit_name,
                               edits, None, *args)
    
    # Handle weapon descriptor for new units
    if edit_type == "new_units":
        weapon_descr = modules_list.v.find_by_cond(
            lambda m: not isinstance(m.v, ndf.model.Object) and
            m.v.startswith("$/GFX/Weapon/WeaponDescriptor_"), strict=False)
        if weapon_descr:
            if not edits.get("is_unarmed", False):
                modules_list.v.replace(weapon_descr, f"$/GFX/Weapon/WeaponDescriptor_{unit_name}")
            else:
                modules_list.v.remove(weapon_descr)
    
    # Manual addition/removal of modules
    _add_modules(game_db, edit_type, unit_name, edits, modules_list)
    _remove_modules(game_db, edit_type, unit_name, edits, modules_list)


# ------------------------------ Simple handlers -------------------------------
# Add modules
def _add_modules(game_db, edit_type, unit_name, edits, modules_list) -> None:
    """Add modules to new and existing units"""
    if edit_type == "new_units":
        for module in edits.get("modules_add", []):
            modules_list.v.add(module)
    
    if edit_type == "unit_edits":
        unit_db = game_db["unit_data"]
        
        found_transporter_module = find_obj_by_type(
            modules_list.v, "TTransporterModuleDescriptor") is not None
        
        wreck_type = "Default" if not unit_db.get(
            unit_name, {}).get("is_helo_unit", False) else "Chopper"
            
        transporter_module = (
            f"TTransporterModuleDescriptor"
            f"("
            f'    TransportableTagSet = ["Crew", "Unite_transportable"]'
            f"    NbSeatsAvailable = 1"
            f"    WreckUnloadPhysicalDamageBonus = WreckUnloadDamageBonus_{wreck_type}_Physical"
            f"    WreckUnloadSuppressDamageBonus = WreckUnloadDamageBonus_{wreck_type}_Suppress"
            f"    WreckUnloadStunDamageBonus = WreckUnloadDamageBonus_{wreck_type}_Stun"
            f"    LoadRadiusGRU = 70"
            f")"
        )
        
        if not found_transporter_module and "EOrderType/UnloadFromTransport" in edits.get(
            "orders", {}).get("add_orders", []):
            modules_list.v.add(transporter_module)
        
        for module in edits.get("modules_add", []):
            modules_list.v.add(module)

        if "EOrderType/Sell" in edits.get("orders", {}).get("add_orders", []):
            sell_module = "~/SellModuleDescriptor"
            modules_list.v.add(sell_module)  # noqa


# Remove modules
def _remove_modules(game_db, edit_type, unit_name, edits, modules_list) -> None:
    """Remove modules from new and existing units"""
    
    for module_to_remove in edits.get("modules_remove", []):
        if module_to_remove.startswith("~/"):
            for module in modules_list.v:
                if not isinstance(module.v, ndf.model.Object) and module.v == module_to_remove:
                    modules_list.v.remove(module.index)
            continue
        
        module = find_obj_by_type(modules_list.v, module_to_remove)
        if module:
            modules_list.v.remove(module.index)
        else:
            module = find_obj_by_namespace(modules_list.v, module_to_remove)
            if module:
                modules_list.v.remove(module.index)


# TTypeUnitModuleDescriptor
def _handle_typeunit_module(logger, game_db, unit_data, edit_type, unit_name,
                            edits, module, *args) -> None:
    """Handle TTypeUnitModuleDescriptor for existing and new units"""
    # TODO: Add the keys and values back to the dictionary entries
    for member, value in edits.get("TypeUnit", {}).items():
        module.v.by_m(member).v = value
        

# TFormationModuleDescriptor
def _handle_formation_module(logger, game_db, unit_data, edit_type, unit_name,
                            edits, module, *args) -> None:
    """Handle TFormationModuleDescriptor for existing and new units"""
    if edits.get("TypeUnitFormation", None) is not None:
        module.v.by_m("TypeUnitFormation").v = str(edits["TypeUnitFormation"])


# TInfantrySquadModuleDescriptor
def _handle_infantrysquad_module(logger, game_db, unit_data, edit_type, unit_name,
                                 edits, module, *args) -> None:
    """Handle TInfantrySquadModuleDescriptor for existing and new units"""
    
    if edit_type == "new_units":
        module.v.by_m("InfantryMimeticName").v = f"'{unit_name}'"
        module.v.by_m("WeaponUnitFXKey").v = f"'{unit_name}'"
        
        mimetic_descr = module.v.by_m("MimeticDescriptor")
        mimetic_descr.v.by_m("DescriptorId").v = f"GUID:{{{edits['GroupeCombatGUID']}}}"
        mimetic_descr.v.by_m("MimeticName").v = f"'{unit_name}'"
    
    if "strength" in edits:
        module.v.by_m("NbSoldatInGroupeCombat").v = str(edits["strength"])
        logger.info(f"Updated {unit_name} strength to {edits['strength']}")
            

# TGenericMovementModuleDescriptor
def _handle_genericmovement_module(logger, game_db, unit_data, edit_type, unit_name,
                                   edits, module, *args) -> None:
    """Handle TGenericMovementModuleDescriptor for existing and new units"""
    
    if "max_speed" in edits:
        module.v.by_m("MaxSpeedInKmph").v = str(edits["max_speed"])
        logger.info(f"Updated {unit_name} max speed to {edits['max_speed']}")
            

# TLandMovementModuleDescriptor
def _handle_landmovement_module(logger, game_db, unit_data, edit_type, unit_name,
                                edits, module, *args) -> None:
    """Handle TLandMovementModuleDescriptor for existing and new units"""
    
    if "factor" in edits.get("road_speed", {}):
        factor = edits["road_speed"]["factor"]
        module.v.by_m("SpeedBonusFactorOnRoad").v = "{:0.2f}".format(factor)
        logger.info(f"Updated {unit_name} road speed factor to {factor}")

    elif "road_speed" in edits.get("road_speed", {}) and "base_speed" in edits.get("road_speed", {}):
        factor = edits["road_speed"]["road_speed"] / edits["road_speed"]["base_speed"]
        module.v.by_m("SpeedBonusFactorOnRoad").v = "{:0.2f}".format(factor)
        logger.info(f"Updated {unit_name} road speed factor to {factor}")
            

# AirplaneMovementDescriptor
def _handle_airplanemovement_module(logger, game_db, unit_data, edit_type, unit_name,
                                    edits, module, *args) -> None:
    """Handle AirplaneMovementDescriptor for existing and new units"""

    if "max_speed" in edits:
        old_value = module.v.by_m("SpeedInKmph").v
        module.v.by_m("SpeedInKmph").v = str(edits["max_speed"])
        logger.info(f"Updated {unit_name} max speed from {old_value} to {edits['max_speed']}")

    if "AirplaneMovement" in edits and "parent_membr" in edits["AirplaneMovement"]:
        for key, value in edits["AirplaneMovement"]["parent_membr"].items():
            old_value = module.v.by_m(key).v
            module.v.by_m(key).v = str(value)
            logger.info(f"Updated {unit_name} {key} from {old_value} to {value}")
            
    # Global bomber edits TODO: Use dic references instead for standardization
    if edit_type == "new_units":
        donor = args[0]
        unit_or_donor_data = game_db["unit_data"].get(donor, None)
    else:
        unit_or_donor_data = unit_data

    search_conditions = [
        ("has_terrain_radar", "'terrain_radar'", edits.get("specialties", {})),
        ("is_sead", "Avion_SEAD", unit_or_donor_data.get("tags", {})),
        ("is_ew", "_electronic_warfare", unit_or_donor_data.get("specialties", {})),
    ]
    has_terrain_radar, is_sead, is_ew = determine_characteristics(search_conditions)
    
    if has_terrain_radar and is_sead and not is_ew:
        new_value = "300"
        module.v.by_m("AltitudeGRU").v = new_value
        logger.info(f"Updated {unit_name} altitude to {new_value}")


# TTransportableModuleDescriptor
def _handle_transportable_module(logger, game_db, unit_data, edit_type, unit_name,
                                 edits, module, *args) -> None:
    """Handle TTransportableModuleDescriptor for existing and new units"""
    if "TransportedTexture" in edits:
        module.v.by_m("TransportedTexture").v = f"'{edits['TransportedTexture']}'"
        
    if "TransportedSoldier" in edits:
        module.v.by_m("TransportedSoldier").v = f"'{edits['TransportedSoldier']}'"
            

# TTransporterModuleDescriptor
def _handle_transporter_module(logger, game_db, unit_data, edit_type, unit_name,
                               edits, module, *args) -> None:
    """Handle TTransporterModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "is_prime_mover" in edits:

            transport_tags = module.v.by_m("TransportableTagSet")
            can_transport_unit = edits.get("is_prime_mover", False)

            if can_transport_unit:
                transport_tags.v = '["Crew", "Unite_transportable"]'
                logger.info(f"Updated {unit_name} to prime mover")

            else:
                transport_tags.v = '["Crew"]'
                logger.info(f"Updated {unit_name} to regular transport")

        add_unit_transport = "EOrderType/UnloadFromTransport" in edits.get("orders", {}).get("add_orders", [])

        if add_unit_transport:
            transport_tags = '["Crew", "Unite_transportable"]'
            module.v.by_m("TransportableTagSet").v = transport_tags
            logger.info(f"Updated {unit_name} to prime mover")
            

# TVisibilityModuleDescriptor
def _handle_visibility_module(logger, game_db, unit_data, edit_type, unit_name,
                              edits, module, *args) -> None:
    """Handle TVisibilityModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "stealth" in edits:
            module.v.by_m("UnitConcealmentBonus").v = str(edits["stealth"])
            logger.info(f"Updated {unit_name} stealth to {edits['stealth']}")
        
        # global bomber edits TODO: Use dic references instead for standardization
        conditions_search = [
            ("has_terrain_radar", "'terrain_radar'", edits.get("specialties", {})),
            ("is_sead", "Avion_SEAD", unit_data.get("tags", {})),
            ("is_ew", "_electronic_warfare", unit_data.get("specialties", {})),
        ]
        has_terrain_radar, is_sead, is_ew = determine_characteristics(conditions_search)

        if has_terrain_radar and is_sead and not is_ew:
            module.v.by_m("UnitConcealmentBonus").v = "1.75"
            logger.info(f"Updated {unit_name} stealth to 1.75")

# InfantryApparenceModuleDescriptor
def _handle_infantryapparence_module(logger, game_db, unit_data, edit_type, unit_name,
                                     edits, module, *args) -> None:
    """Handle InfantryApparenceModuleDescriptor for existing and new units"""
    if edit_type == "new_units" and "depictions" in edits:
        module.v.by_m("Depiction").v = f"$/GFX/Depiction/TacticDepiction_{unit_name}"
    
    if edit_type == "unit_edits":
        pass


# VehicleApparenceModuleDescriptor
def _handle_vehicleapparence_module(logger, game_db, unit_data, edit_type, unit_name,
                                    edits, module, *args) -> None:
    """Handle VehicleApparenceModuleDescriptor for existing and new units"""
    if edit_type == "new_units" and "depictions" in edits:
        if edits.get("depictions", {}).get("new_mesh", False):
            new_name = edits["NewName"]
            module.v.by_m("MimeticName").v = f'"{new_name}"'
            module.v.by_m("BlackHoleIdentifier").v = f'"{new_name}"'
            module.v.by_m("ReferenceMesh").v = f'$/GFX/DepictionResources/Modele_{new_name}'
        else:
            module.v.by_m("MimeticName").v = f'"{unit_name}"'
    
    if edit_type == "unit_edits":
        pass


# TAutoCoverModuleDescriptor
def _handle_autocover_module(logger, game_db, unit_data, edit_type, unit_name,
                             edits, module, *args) -> None:
    """Handle TAutoCoverModuleDescriptor for existing and new units"""
    
    module.v.by_m("AutoCoverRangeGRU").v = "70.0"


# TBaseDamageModuleDescriptor
def _handle_basedamage_module(logger, game_db, unit_data, edit_type, unit_name,
                              edits, module, *args) -> None:
    """Handle TBaseDamageModuleDescriptor for existing and new units"""
    
    if "strength" in edits:
        module.v.by_m("MaxPhysicalDamages").v = str(edits["strength"])
            

# TDamageModuleDescriptor
def _handle_damage_module(logger, game_db, unit_data, edit_type, unit_name,
                                edits, module, *args) -> None:
    """Handle TDamageModuleDescriptor for existing and new units"""
    
    if "ECM" in edits:
        module.v.by_m("HitRollECM").v = str(edits["ECM"])
    
    if "armor" in edits:
        blindage_obj = module.v.by_m("BlindageProperties").v
        ARMOR_PARTS = {
            "front": "ResistanceFront",
            "sides": "ResistanceSides",
            "rear": "ResistanceRear",
            "top": "ResistanceTop",
        }
        
        for part_name, resistance_key in ARMOR_PARTS.items():
            part_edits = edits["armor"].get(part_name, None)
            if part_edits is not None:
                armor_level, armor_family = part_edits
                
                # Handle custom infantry armor reference
                if armor_family == "ResistanceFamily_infanterieWA":
                    
                    inf_strength = edits.get("strength", None)
                    if not inf_strength:
                        inf_strength = unit_data.get("strength", None)
                    
                    if inf_strength is not None:
                        armor_level = str(max(15 - inf_strength, 1))
                        blindage_obj.by_m(resistance_key).v.by_m("Family").v = armor_family
                        blindage_obj.by_m(resistance_key).v.by_m("Index").v = armor_level
                    
                # Standard edits
                else:
                    if armor_level is not None:
                        blindage_obj.by_m(resistance_key).v.by_m("Index").v = str(armor_level)
                    if armor_family is not None:
                        blindage_obj.by_m(resistance_key).v.by_m("Family").v = armor_family
        
        for part, resistance in ARMOR_PARTS.items():
            armor_level = None
            armor_family = None
            armor_tuple = edits["armor"].get(part, None)
            if armor_tuple is not None and isinstance(armor_tuple, tuple) and len(armor_tuple) == 2:
                armor_level = armor_tuple[0]
                armor_family = armor_tuple[1]
            if armor_level is not None:
                blindage_obj.by_m(resistance).v.by_m("Index").v = str(armor_level)
            if armor_family is not None:
                blindage_obj.by_m(resistance).v.by_m("Family").v = armor_family
        
        if "era" in edits["armor"]:
            blindage_obj.by_m("ExplosiveReactiveArmor").v = str(edits["armor"]["era"])
    

# TDangerousnessModuleDescriptor
def _handle_dangerousness_module(logger, game_db, unit_data, edit_type, unit_name,
                                 edits, module, *args) -> None:
    """Handle TDangerousnessModuleDescriptor for existing and new units"""
    if "Dangerousness" in edits:
        module.v.by_m("Dangerousness").v = str(edits["Dangerousness"])


# TScannerConfigurationDescriptor
def _handle_scannerconfiguration_module(logger, game_db, unit_data, edit_type, unit_name,
                                        edits, module, *args) -> None:
    """Handle TScannerConfigurationDescriptor for existing and new units"""
    # if edit_type == "new_units":
    #     pass

    if "VisionRangesGRU" in edits.get("optics", {}):
        for key, value in edits["optics"]["VisionRangesGRU"].items():
            module.v.by_m("VisionRangesGRU").v.by_k(key).v = str(value)

    if "OpticalStrengths" in edits.get("optics", {}):
        for key, value in edits["optics"]["OpticalStrengths"].items():
            module.v.by_m("OpticalStrengths").v.by_k(key).v = str(value)

    if edit_type == "unit_edits":
        for spec in edits.get("SpecialtiesList", {}).get("add_specs", []):
            # TODO: Good vs. very good needs more testing/research to find a workable differentiation
            # It might have to involve optical strength instead of just vision range
            # For now good has just been bumped up to very good (12000m)
            if spec == "'verygood_airoptics'":
                vision_ranges = module.v.by_m("VisionRangesGRU")
                vision_ranges.v.by_k("EVisionRange/HighAltitude").v = "12000.0"
            elif spec == "'good_airoptics'":
                vision_ranges = module.v.by_m("VisionRangesGRU")
                vision_ranges.v.by_k("EVisionRange/HighAltitude").v = "12000.0"
                    
                    
# TReverseScannerWithIdentificationDescriptor
def _handle_reversescanner_module(logger, game_db, unit_data, edit_type, unit_name,
                                   edits, module, *args) -> None:
    """Handle TReverseScannerWithIdentificationDescriptor for existing and new units"""

    current_base_prob = float(module.v.by_m("IdentifyBaseProbability").v)
    new_base_prob = min(current_base_prob * 1.25, 1.0)
        
    module.v.by_m("IdentifyBaseProbability").v = str(new_base_prob)

    custom_roll_freq = edits.get("optics", {}).get("TimeBetweenEachIdentifyRoll", None)
    if custom_roll_freq:
        module.v.by_m("TimeBetweenEachIdentifyRoll").v = str(custom_roll_freq)
    else:
        current_roll_freq = float(module.v.by_m("TimeBetweenEachIdentifyRoll").v)
        module.v.by_m("TimeBetweenEachIdentifyRoll").v = str(current_roll_freq / 2)


def _handle_missilecarriage_module(logger, game_db, unit_data, edit_type, unit_name,
                                   edits, module, *args) -> None:
    """Handle TMissileCarriageModuleDescriptor for existing and new units"""
    if edit_type == "new_units" and "depictions" in edits:
        if edits.get("depictions", {}).get("new_mesh", False):
            new_name = edits["NewName"]
            module.v.by_m("Connoisseur").v = f'$/GFX/Depiction/MissileCarriage_{new_name}'
        else:
            pass
    
    if edit_type == "unit_edits":
        pass
    
    
# TProductionModuleDescriptor
def _handle_production_module(logger, game_db, unit_data, edit_type, unit_name,
                              edits, module, *args) -> None:
    """Handle TProductionModuleDescriptor for existing and new units"""
    
    if "CommandPoints" in edits:
        cmd_points = "$/GFX/Resources/Resource_CommandPoints"
        production_ressources_needed = module.v.by_m("ProductionRessourcesNeeded")
        production_ressources_needed.v.by_k(cmd_points).v = str(edits["CommandPoints"]) # noqa

    if "Factory" in edits:
        module.v.by_m("FactoryType").v = edits["Factory"]
            

# TTacticalLabelModuleDescriptor
def _handle_tacticallabel_module(logger, game_db, unit_data, edit_type, unit_name,
                                 edits, module, *args) -> None:
    """Handle TTacticalLabelModuleDescriptor for existing and new units"""
    
    if "SortingOrder" in edits:
        module.v.by_m("MultiSelectionSortingOrder").v = str(edits["SortingOrder"])
    if "IdentifiedTextures" in edits:
        id_textures_member = module.v.by_m("IdentifiedTexture")
        id_textures_member.v.by_m("Values").v = str(edits["IdentifiedTextures"])
    if "UnidentifiedTextures" in edits:
        unid_textures_member = module.v.by_m("UnidentifiedTexture")
        unid_textures_member.v.by_m("Values").v = str(edits["UnidentifiedTextures"])
            

# TStrategicDataModuleDescriptor
def _handle_strategicdata_module(logger, game_db, unit_data, edit_type, unit_name,
                                 edits, module, *args) -> None:
    """Handle TStrategicDataModuleDescriptor for existing and new units"""
    if "UnitAttackValue" in edits:
        module.v.by_m("UnitAttackValue").v = str(edits["UnitAttackValue"])
    if "UnitDefenseValue" in edits:
        module.v.by_m("UnitDefenseValue").v = str(edits["UnitDefenseValue"])
        

# TDeploymentShiftModuleDescriptor
def _handle_deploymentshift_module(logger, game_db, unit_data, edit_type, unit_name,
                                   edits, module, *args) -> None:
    """Handle TDeploymentShiftModuleDescriptor for existing and new units"""
    
    found_zoneinfluence_module = args[0]
    
    # Remove forward deploy for command units
    if found_zoneinfluence_module:
        logger.info(f"Removed {module.v.type} from {unit_name}")
        module.parent.remove(module.index)
    
    # Adjust forward deploy for units with helicopter transports
    elif edits.get("DeploymentShift", None) is not None:
        module.v.by_m("DeploymentShiftGRU").v = str(edits["DeploymentShift"])
    
    else:
        # Nerf forward deploy
        shift_val = float(module.v.by_m("DeploymentShiftGRU").v)
        if shift_val not in forward_deploy_old_values:
            forward_deploy_old_values.append(shift_val)
            
        if shift_val >= 2501:
            module.v.by_m("DeploymentShiftGRU").v = str(forward_deploy_new_values[1])
        else:
            module.v.by_m("DeploymentShiftGRU").v = str(forward_deploy_new_values[0])

# TZoneInfluenceMapModuleDescriptor
def _handle_zoneinfluencemap_module(logger, game_db, unit_data, edit_type, unit_name,
                                    edits, module, *args) -> None:
    """Handle TZoneInfluenceMapModuleDescriptor for existing and new units"""

    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "remove_zone_capture" in edits:
            module.parent.remove(module.index)  # noqa
            

# TInfluenceScoutModuleDescriptor
def _handle_influencescout_module(logger, game_db, unit_data, edit_type, unit_name,
                                  edits, module, *args) -> None:
    """Handle TInfluenceScoutModuleDescriptor for existing and new units"""

    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "remove_zone_capture" in edits:
            module.parent.remove(module.index)  # noqa
            

# TCubeActionModuleDescriptor
def _handle_cubeaction_module(logger, game_db, unit_data, edit_type, unit_name,
                              edits, module, *args) -> None:
    """Handle TCubeActionModuleDescriptor for existing and new units"""
    if "CubeActionDescriptor" in edits:
        new_value = f"$/GFX/UI/CubeAction_Menu_Ordres_{edits['CubeActionDescriptor']}"
        module.v.by_m("CubeActionDescriptor").v = new_value
        

# TOrderConfigModuleDescriptor
def _handle_orderconfig_module(logger, game_db, unit_data, edit_type, unit_name,
                               edits, module, *args) -> None:
    """Handle TOrderConfigModuleDescriptor for existing and new units"""
    
    if edit_type == "new_units":
        module.v.by_m("ValidOrders").v = f"~/Descriptor_OrderAvailability_{unit_name}"


# TOrderableModuleDescriptor
def _handle_orderable_module(logger, game_db, unit_data, edit_type, unit_name,
                             edits, module, *args) -> None:
    """Handle TOrderableModuleDescriptor for existing and new units"""
    
    if edit_type == "new_units":
        module.v.by_m("UnlockableOrders").v = f"~/Descriptor_OrderAvailability_{unit_name}"


# TCameraShowroomModuleDescriptor
def _handle_camerashowroom_module(logger, game_db, unit_data, edit_type, unit_name,
                                  edits, module, *args) -> None:
    """Handle TCameraShowroomModuleDescriptor for existing and new units"""
    if edit_type == "new_units" and "depictions" in edits:
        if edits.get("depictions", {}).get("new_mesh", False):
            new_name = edits["NewName"]
            module.v.by_m("ShowRoomBlackHoleIdentifier").v = f'"showroom_{new_name}"'
        else:
            pass
    
    if edit_type == "unit_edits":
        pass
    