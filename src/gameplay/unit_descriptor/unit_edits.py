"""Unit descriptor editing functionality."""

from typing import Any, Dict

from src import ndf
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_namespace

logger = setup_logger('unit_descriptor_edits')

def edit_units(source_path: Any) -> None:
    """Edit unit descriptors."""
    logger.info("Starting UniteDescriptor.ndf modifications")
    
    units_processed = 0
    units_modified = 0
    unit_edits = load_unit_edits()
    
    for unit_row in source_path:
        units_processed += 1
        unit_name = unit_row.namespace.replace("Descriptor_Unit_", "")
        
        edits = find_namespace(unit_row, "Descriptor_Unit_", unit_edits)
        if edits is None:
            continue
            
        units_modified += 1
        
        try:
            modules_list = unit_row.v.by_m("ModulesDescriptors").v
            for i, descr_row in enumerate(modules_list, start=0):
                if not isinstance(descr_row.v, ndf.model.Object):
                    continue
                    
                modify_module(unit_row, descr_row, edits, i, modules_list)
        except Exception as e:
            logger.error(f"Error modifying {unit_name}: {str(e)}")
    
    logger.info(f"Processed {units_processed} units total")
    logger.info(f"Modified {units_modified} units")

def modify_module(
    unit_row: Any, descr_row: Any, edits: dict, index: int, modules_list: list
) -> None:
    """Apply edits to a specific module based on its type."""
    descr_type = descr_row.v.type
    namespace = descr_row.namespace

    # Handle module-specific edits
    module_handlers = {
        "TTagsModuleDescriptor": _handle_tags,
        "TVisibilityModuleDescriptor": _handle_visibility,
        "TBaseDamageModuleDescriptor": _handle_base_damage,
        "TDamageModuleDescriptor": _handle_damage,
        "TScannerConfigurationDescriptor": _handle_scanner,
        "TProductionModuleDescriptor": _handle_production,
        "TTacticalLabelModuleDescriptor": _handle_tactical_label,
        "TStrategicDataModuleDescriptor": _handle_strategic_data,
        "TIconModuleDescriptor": _handle_icon,
        "TUnitUIModuleDescriptor": _handle_unit_ui,
        "TDeploymentShiftModuleDescriptor": _handle_deployment_shift,
    }

    # Handle special namespace cases
    if namespace == "GroupeCombat" and "Strength" in edits:
        descr_row.v.by_m("Default").v.by_m("NbSoldatInGroupeCombat").v = str(edits["Strength"])
    
    elif namespace == "GenericMovement" and "max_speed" in edits:
        descr_row.v.by_m("Default").v.by_m("MaxSpeedInKmph").v = str(edits["max_speed"])
    
    elif namespace == "AirplaneMovement" and "AirplaneMovement" in edits:
        if "parent_membr" in edits["AirplaneMovement"]:
            for key, value in edits["AirplaneMovement"]["parent_membr"].items():
                descr_row.v.by_m(key).v = str(value)

    # Apply module-specific handler if it exists
    if handler := module_handlers.get(descr_type):
        handler(unit_row, descr_row, edits, index, modules_list)

def _handle_tags(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:
    if "TagSet" not in edits:
        return
    tagset = descr_row.v.by_m("TagSet").v
    if "add_tags" in edits["TagSet"]:
        for tag in edits["TagSet"]["add_tags"]:
            tagset.add(tag)
            logger.info(f"Added tag {tag} to {unit_row.namespace}")

def _handle_visibility(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:
    if "stealth" in edits:
        descr_row.v.by_m("UnitConcealmentBonus").v = str(edits["stealth"])

def _handle_base_damage(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:
    if "Strength" in edits:
        descr_row.v.by_m("MaxPhysicalDamages").v = str(edits["Strength"])

def _handle_damage(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:
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

def _handle_scanner(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:
    if "optics" not in edits:
        return
    
    if "OpticalStrength" in edits["optics"]:
        descr_row.v.by_m("OpticalStrength").v = str(edits["optics"]["OpticalStrength"])
    
    if "OpticalStrengthAltitude" in edits["optics"]:
        descr_row.v.by_m("OpticalStrengthAltitude").v = str(
            edits["optics"]["OpticalStrengthAltitude"]
        )
    
    if "SpecializedOpticalStrengths" in edits["optics"]:
        for key, value in edits["optics"]["SpecializedOpticalStrengths"].items():
            descr_row.v.by_m("SpecializedOpticalStrengths").v.by_k(key).v = str(value)

def _handle_production(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:
    if "CommandPoints" in edits:
        cmd_points = "$/GFX/Resources/Resource_CommandPoints"
        descr_row.v.by_m("ProductionRessourcesNeeded").v.by_k(cmd_points).v = (
            edits["CommandPoints"]
        )
    
    if "category" in edits:
        descr_row.v.by_m("Factory").v = f"EDefaultFactories/{edits['category']}"

def _handle_tactical_label(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:
    if "SortingOrder" in edits:
        descr_row.v.by_m("MultiSelectionSortingOrder").v = edits["SortingOrder"]
    if "Strength" in edits:
        descr_row.v.by_m("NbSoldiers").v = str(edits["Strength"])

def _handle_strategic_data(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:
    if "UnitAttackValue" in edits:
        descr_row.v.by_m("UnitAttackValue").v = edits["UnitAttackValue"]
        descr_row.v.by_m("UnitDefenseValue").v = edits["UnitDefenseValue"]

def _handle_icon(unit_row: Any, descr_row: Any, edits: dict, *_) -> None:
    if "IdentifiedTextures" in edits:
        descr_row.v.by_m("IdentifiedTextures").v = str(edits["IdentifiedTextures"])
        descr_row.v.by_m("UnidentifiedTextures").v = str(edits["UnidentifiedTextures"])

def _handle_unit_ui(unit_row: Any, descr_row: Any, edits: dict, index: int, modules_list: list) -> None:
    if "SpecialtiesList" in edits:
        specialties_list = descr_row.v.by_m("SpecialtiesList").v
        if "add_specs" in edits["SpecialtiesList"]:
            for spec in edits["SpecialtiesList"]["add_specs"]:
                specialties_list.add(spec)
                logger.info(f"Added specialty {spec} to {unit_row.namespace}")
        if "remove_specs" in edits["SpecialtiesList"]:
            for spec in edits["SpecialtiesList"]["remove_specs"]:
                for tag in specialties_list:
                    if tag.v == spec:
                        specialties_list.remove(tag.index)
                        logger.info(f"Removed specialty {spec} from {unit_row.namespace}")

    if "GameName" in edits:
        descr_row.v.by_m("NameToken").v = "'" + edits["GameName"]["nametoken"] + "'"
    
    if "UpgradeFromUnit" in edits and descr_row.v.by_m("UpgradeFromUnit", False) is not None:
        descr_row.v.by_m("UpgradeFromUnit").v = f"Descriptor_Unit_{edits['UpgradeFromUnit']}"
    
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
            modules_list.insert(index + 1, sell_module)

def _handle_deployment_shift(unit_row: Any, descr_row: Any, edits: dict, index: int, modules_list: list) -> None:
    """Handle deployment shift module removal."""
    if "DeploymentShift" in edits and edits["DeploymentShift"] == 0:
        descr_type = descr_row.v.type
        modules_list.remove(index)
        logger.info(f"Removed {descr_type} from {unit_row.namespace}") 