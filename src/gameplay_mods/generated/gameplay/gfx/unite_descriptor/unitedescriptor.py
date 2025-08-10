"""Functions for modifying UniteDescriptor.ndf"""

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.constants.new_units import NEW_UNITS
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

from .handlers import (
    handle_capacite_module,
    handle_supply_module,
    handle_tags_module,
    handle_unitui_module,
)

logger = setup_logger(__name__)


def edit_unitedescriptor(source_path, game_db) -> None:
    """GameData/Generated/Gameplay/Gfx/UniteDescriptor.ndf"""

    unit_edits = load_unit_edits()
    unit_edits_dic_entries = []
    new_units_dic_entries = []
    _handle_unit_edits(source_path, game_db, unit_edits, unit_edits_dic_entries)
    _handle_new_units(source_path, game_db, new_units_dic_entries)

    merged_dic_entries = unit_edits_dic_entries + new_units_dic_entries
    write_dictionary_entries(merged_dic_entries, dictionary_type="units")

def _handle_unit_edits(source_path, game_db, unit_edits, unit_edits_dic_entries) -> None:
    """Handle unit edits for existing units in UniteDescriptor.ndf"""

    for unit, edits in unit_edits.items():
        unit_name = unit
        descr_n = f"Descriptor_Unit_{unit_name}"
        modules_list = source_path.by_n(descr_n).v.by_m("ModulesDescriptors")
        _handle_modules_list(game_db, unit_edits_dic_entries, "unit_edits", unit_name, edits, modules_list)
        logger.info(f"Processed unit edits for {unit_name}")


def _handle_new_units(source_path, game_db, new_units_dic_entries) -> None:
    """Handle new unit creation in UniteDescriptor.ndf"""

    for unit, edits in NEW_UNITS.items():
        unit_name = unit[0] # unit is a tuple of (donor_name, unique_key_identifier)
        descr_n = f"Descriptor_Unit_{unit_name}"
        modules_list = source_path.by_n(descr_n).v.by_m("ModulesDescriptors")
        _handle_modules_list(game_db, new_units_dic_entries, "new_units", unit_name, edits, modules_list)
        logger.info(f"Processed new unit edits for {unit_name}")


def _handle_modules_list(game_db, dictionary_entries, edit_type, unit_name, edits, modules_list) -> None:
    """Handle modules list edits for new and existing units"""

    unit_data = game_db["unit_data"][unit_name]

    found_capacite_module = modules_list.v.find_by_cond(
        lambda m: isinstance(m.v, ndf.model.Object) and m.v.type == "TCapaciteModuleDescriptor"
    ) is not None

    module_handlers = {
        # "TTypeUnitModuleDescriptor": { "handler": handle_typeunit_module, "args": [] },
        # "TFormationModuleDescriptor": { "handler": handle_formation_module, "args": [] },
        "TTagsModuleDescriptor": { "handler": handle_tags_module, "args": [] },
        # "TExperienceModuleDescriptor": { "handler": handle_experience_module, "args": [] },
        "TVisibilityModuleDescriptor": { "handler": _handle_visibility_module, "args": [] },
        # "VehicleApparenceModuleDescriptor": { "handler": handle_vehicleapparence_module, "args": [] },
        # "TAutoCoverModuleDescriptor": { "handler": handle_autocover_module, "args": [] },
        "TBaseDamageModuleDescriptor": { "handler": _handle_basedamage_module, "args": [] },
        "TDamageModuleDescriptor": { "handler": _handle_damage_module, "args": [] },
        # "TDangerousnessModuleDescriptor": { "handler": handle_dangerousness_module, "args": [] },
        # "TRoutModuleDescriptor": { "handler": handle_rout_module, "args": [] },
        "TInfantrySquadModuleDescriptor": { "handler": _handle_infantrysquad_module, "args": [] },
        "TGenericMovementModuleDescriptor": { "handler": _handle_genericmovement_module, "args": [] },
        # "THelicopterMovementModuleDescriptor": { "handler": handle_helicoptermovement_module, "args": [] },
        "TLandMovementModuleDescriptor": { "handler": _handle_landmovement_module, "args": [] },
        "AirplaneMovementDescriptor": { "handler": _handle_airplanemovement_module, "args": [] },
        # "TFuelModuleDescriptor": { "handler": handle_fuel_module, "args": [] },
        "TSupplyModuleDescriptor": { "handler": handle_supply_module, "args": [] },
        "TScannerConfigurationDescriptor": { "handler": _handle_scannerconfiguration_module, "args": [] },
        "TReverseScannerWithIdentificationDescriptor": { "handler": _handle_reversescanner_module, "args": [] },
        "TTransportableModuleDescriptor": { "handler": _handle_transportable_module, "args": [] },
        "TTransporterModuleDescriptor": { "handler": _handle_transporter_module, "args": [] },
        # "UnitCadavreGeneratorModuleDescriptor": { "handler": handle_unitcadavre_module, "args": [] },
        # "TIAStratModuleDescriptor": { "handler": handle_iastrat_module, "args": [] },
        "TCapaciteModuleDescriptor": {
            "handler": handle_capacite_module,
            "args": [found_capacite_module],
        },
        "TProductionModuleDescriptor": { "handler": _handle_production_module, "args": [] },
        "TZoneInfluenceMapModuleDescriptor": { "handler": _handle_zoneinfluencemap_module, "args": [modules_list] },
        "TInfluenceScoutModuleDescriptor": { "handler": _handle_influencescout_module, "args": [modules_list] },
        # "TAutomaticBehaviorModuleDescriptor": { "handler": handle_automaticbehavior_module, "args": [] },
        # "TCubeActionModuleDescriptor": { "handler": handle_cubeaction_module, "args": [] },
        # "TMinimapDisplayModuleDescriptor": { "handler": handle_minimapdisplay_module, "args": [] },
        # "TOrderConfigModuleDescriptor": { "handler": handle_orderconfig_module, "args": [] },
        # "TOrderableModuleDescriptor": { "handler": handle_orderable_module, "args": [] },
        "TTacticalLabelModuleDescriptor": { "handler": _handle_tacticallabel_module, "args": [] },
        "TStrategicDataModuleDescriptor": { "handler": _handle_strategicdata_module, "args": [] },
        "TUnitUIModuleDescriptor": { "handler": handle_unitui_module, "args": [dictionary_entries] },
        # "TShowRoomEquivalenceModuleDescriptor": { "handler": handle_showroomequivalence_module, "args": [] },
        # "TUnitUpkeepModuleDescriptor": { "handler": handle_unitupkeep_module, "args": [] },
        "TDeploymentShiftModuleDescriptor": { "handler": _handle_deploymentshift_module, "args": [] },
    }
    # Iterate over module handlers
    for module_type, handling_data in module_handlers.items():
        module = modules_list.v.find_by_cond(
            lambda m: isinstance(m.v, ndf.model.Object) and m.v.type == module_type)
        if not module:
            continue

        handling_data["handler"](logger, game_db, unit_data, edit_type, unit_name, 
                                 edits, module, *handling_data["args"])
    
    # Manual addition/removal of modules
    _add_modules(game_db, edit_type, unit_name, edits, modules_list)
    _remove_modules(game_db, edit_type, unit_name, edits, modules_list)

# ------------------------------ Simple handlers -------------------------------
# Add modules
def _add_modules(game_db, edit_type, unit_name, edits, modules_list) -> None:
    """Add modules to new and existing units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        unit_db = game_db["unit_data"]

        found_transporter_module = modules_list.v.find_by_cond(
            lambda m: isinstance(m.v, ndf.model.Object) and m.v.type == "TTransporterModuleDescriptor"
        ) is not None
        
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
        
        if not found_transporter_module and "UnloadFromTransport" in edits.get(
            "orders", {}).get("add_orders", []):
            modules_list.v.add(transporter_module)
        
        for module in edits.get("modules_add", []):
            modules_list.v.add(module)
        
        if "sell" in edits.get("orders", {}).get("add_orders", []):
            sell_module = "~/SellModuleDescriptor"
            modules_list.v.add(sell_module)  # noqa


# Remove modules
def _remove_modules(game_db, edit_type, unit_name, edits, modules_list) -> None:
    """Remove modules from new and existing units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        for module_to_remove in edits.get("modules_remove", []):
            modules_list.v.remove(modules_list.v.find_by_cond(
                lambda m: is_obj_type(m.v, module_to_remove)
            ))


# TInfantrySquadModuleDescriptor
def _handle_infantrysquad_module(logger, game_db, unit_data, edit_type, unit_name,
                                 edits, module, *args) -> None:
    """Handle TInfantrySquadModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "strength" in edits:
            module.v.by_m("NbSoldatInGroupeCombat").v = str(edits["strength"])
            logger.info(f"Updated {unit_name} strength to {edits['strength']}")
            

# TGenericMovementModuleDescriptor
def _handle_genericmovement_module(logger, game_db, unit_data, edit_type, unit_name,
                                   edits, module, *args) -> None:
    """Handle TGenericMovementModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "max_speed" in edits:
            module.v.by_m("MaxSpeedInKmph").v = str(edits["max_speed"])
            logger.info(f"Updated {unit_name} max speed to {edits['max_speed']}")
            

# TLandMovementModuleDescriptor
def _handle_landmovement_module(logger, game_db, unit_data, edit_type, unit_name,
                                edits, module, *args) -> None:
    """Handle TLandMovementModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
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
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "max_speed" in edits:
            old_value = module.v.by_m("SpeedInKmph").v
            module.v.by_m("SpeedInKmph").v = str(edits["max_speed"])
            logger.info(f"Updated {unit_name} max speed from {old_value} to {edits['max_speed']}")

        if "AirplaneMovement" in edits and "parent_membr" in edits["AirplaneMovement"]:
            for key, value in edits["AirplaneMovement"]["parent_membr"].items():
                old_value = module.v.by_m(key).v
                module.v.by_m(key).v = str(value)
                logger.info(f"Updated {unit_name} {key} from {old_value} to {value}")


# TTransportableModuleDescriptor
def _handle_transportable_module(logger, game_db, unit_data, edit_type, unit_name,
                                 edits, module, *args) -> None:
    """Handle TTransportableModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "TransportedTexture" in edits:
            module.v.by_m("TransportedTexture").v = f'"{edits["TransportedTexture"]}"'
            logger.info(f"Updated transported texture for {unit_name}")
            

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

        add_unit_transport = "UnloadFromTransport" in edits.get("orders", {}).get("add_orders", [])

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
            

# TBaseDamageModuleDescriptor
def _handle_basedamage_module(logger, game_db, unit_data, edit_type, unit_name,
                              edits, module, *args) -> None:
    """Handle TBaseDamageModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "strength" in edits:
            module.v.by_m("MaxPhysicalDamages").v = str(edits["strength"])
            

# TDamageModuleDescriptor
def _handle_damage_module(logger, game_db, unit_data, edit_type, unit_name,
                                edits, module, *args) -> None:
    """Handle TDamageModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "armor" in edits:
            blindage_obj = module.v.by_m("BlindageProperties").v
            armor_parts = {
                "front": "ResistanceFront",
                "sides": "ResistanceSides",
                "rear": "ResistanceRear",
                "top": "ResistanceTop",
            }
            for part, resistance in armor_parts.items():
                if part in edits["armor"]:
                    blindage_obj.by_m(resistance).v.by_m("Index").v = str(edits["armor"][part])
            if "era" in edits["armor"]:
                blindage_obj.by_m("ExplosiveReactiveArmor").v = str(edits["armor"]["era"])

        if "ECM" in edits:
            module.v.by_m("HitRollECM").v = str(edits["ECM"])
            
            
# TScannerConfigurationDescriptor
def _handle_scannerconfiguration_module(logger, game_db, unit_data, edit_type, unit_name,
                                        edits, module, *args) -> None:
    """Handle TScannerConfigurationDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "optics" not in edits:
            return
        
        if "OpticalStrengths" in edits["optics"]:
            for key, value in edits["optics"]["OpticalStrengths"].items():
                module.v.by_m("OpticalStrengths").v.by_k(key).v = str(value)
                
        if "SpecialtiesList" in edits and "add_specs" in edits["SpecialtiesList"]:
            for spec in edits["SpecialtiesList"]["add_specs"]:
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
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        visibility_rolls_obj = module.v.by_m("VisibilityRollRule")

        current_base_prob = float(visibility_rolls_obj.v.by_m("IdentifyBaseProbability").v)
        new_base_prob = min(current_base_prob * 1.25, 1.0)
            
        visibility_rolls_obj.v.by_m("IdentifyBaseProbability").v = str(new_base_prob)

        custom_roll_freq = edits.get("optics", {}).get("TimeBetweenEachIdentifyRoll", None)
        if custom_roll_freq:
            visibility_rolls_obj.v.by_m("TimeBetweenEachIdentifyRoll").v = str(custom_roll_freq)
        else:
            current_roll_freq = float(visibility_rolls_obj.v.by_m("TimeBetweenEachIdentifyRoll").v)
            visibility_rolls_obj.v.by_m("TimeBetweenEachIdentifyRoll").v = str(current_roll_freq / 2)


# TProductionModuleDescriptor
def _handle_production_module(logger, game_db, unit_data, edit_type, unit_name,
                              edits, module, *args) -> None:
    """Handle TProductionModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "CommandPoints" in edits:
            cmd_points = "$/GFX/Resources/Resource_CommandPoints"
            module.v.by_m("ProductionRessourcesNeeded").v.by_k(cmd_points).v = str(edits["CommandPoints"])

        if "Factory" in edits:
            module.v.by_m("FactoryType").v = edits["Factory"]
            

# TTacticalLabelModuleDescriptor
def _handle_tacticallabel_module(logger, game_db, unit_data, edit_type, unit_name,
                                 edits, module, *args) -> None:
    """Handle TTacticalLabelModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
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
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "UnitAttackValue" in edits:
            module.v.by_m("UnitAttackValue").v = str(edits["UnitAttackValue"])
            module.v.by_m("UnitDefenseValue").v = str(edits["UnitDefenseValue"])
            

# TDeploymentShiftModuleDescriptor
def _handle_deploymentshift_module(logger, game_db, unit_data, edit_type, unit_name,
                                   edits, module, *args) -> None:
    """Handle TDeploymentShiftModuleDescriptor for existing and new units"""
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "DeploymentShift" in edits and edits["DeploymentShift"] == 0:
            module.v.remove(module.index)  # noqa
            logger.info(f"Removed {module.v.type} from {unit_name}")
            

# TZoneInfluenceMapModuleDescriptor
def _handle_zoneinfluencemap_module(logger, game_db, unit_data, edit_type, unit_name,
                                    edits, module, *args) -> None:
    """Handle TZoneInfluenceMapModuleDescriptor for existing and new units"""
    modules_list = args[0]
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "remove_zone_capture" in edits:
            modules_list.v.remove(module.index)  # noqa
            

# TInfluenceScoutModuleDescriptor
def _handle_influencescout_module(logger, game_db, unit_data, edit_type, unit_name,
                                  edits, module, *args) -> None:
    """Handle TInfluenceScoutModuleDescriptor for existing and new units"""
    modules_list = args[0]
    if edit_type == "new_units":
        pass
    
    if edit_type == "unit_edits":
        if "remove_zone_capture" in edits:
            modules_list.v.remove(module.index)  # noqa