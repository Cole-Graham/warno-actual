"""Functions for creating new units."""

from typing import Any, Dict

from src import ndf
from src.constants.new_units import NEW_UNITS
from src.utils.dictionary_utils import write_dictionary_entries
from src.utils.logging_utils import setup_logger
# from src.utils.ndf_utils import get_modules_list, is_obj_type

logger = setup_logger(__name__)


def create_new_units(source_path: Any, game_db: Dict[str, Any]) -> None:  # noqa
    """Create new units based on donor units."""
    logger.info("Creating new units")
    
    # First write dictionary entries for new units
    write_new_unit_dictionary_entries(NEW_UNITS)
    
    # Create unit descriptors
    create_unit_descriptors(source_path)


def write_new_unit_dictionary_entries(unit_edits: Dict[str, Any]) -> None:
    """Write dictionary entries for new units."""
    entries = []
    
    for _, edits in unit_edits.items():
        if "GameName" in edits and "token" in edits["GameName"]:
            entries.append((edits["GameName"]["token"], edits["GameName"]["display"]))
    
    if entries:
        write_dictionary_entries(entries, dictionary_type="units")


def create_unit_descriptors(source_path: Any) -> None:
    """Create unit descriptors for new units."""
    logger.info("Creating unit descriptors")
    
    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if "NewName" not in edits:
            continue
            
        unit_name = edits["NewName"]
        logger.info(f"Creating new unit {unit_name} from donor {donor_name}")
        # donor is now a tuple to allow repeated use of a donor
        # former donor values now located at donor[0], rest of tuple is irrelevant

        # Clone donor unit
        donor_unit = source_path.by_n(f"Descriptor_Unit_{donor_name}")
        if not donor_unit:
            logger.error(f"Donor unit {donor_name} not found")
            continue
            
        new_unit_row = donor_unit.copy()
        new_unit_row.namespace = f"Descriptor_Unit_{unit_name}"
        
        # Modify the new unit based on edits
        modify_new_unit(new_unit_row, edits)
        
        # Add the new unit to the source
        source_path.add(new_unit_row)
        logger.info(f"Added new unit: {unit_name}")


def modify_new_unit(unit_row: Any, edits: Dict[str, Any]) -> None:
    """Modify a new unit based on edit specifications.
    
    Args:
        unit_row: The unit row to modify
        edits: Dictionary of edits to apply
    """
    # Update basic unit properties
    unit_row.v.by_member("DescriptorId").v = f"GUID:{{{edits['GUID']}}}"
    unit_row.v.by_member("ClassNameForDebug").v = f"'Unite_{edits['NewName']}'"
    
    # Process each module
    for descr_row in unit_row.v.by_member("ModulesDescriptors").v:
        if not isinstance(descr_row.v, ndf.model.Object):
            continue
            
        descr_type = descr_row.v.type
        
        # Handle each module type
        if descr_type == "TTagsModuleDescriptor":
            if "TagSet" in edits:
                tagset = descr_row.v.by_member("TagSet").v
                if "overwrite_all" in edits["TagSet"]:
                    tagset.v = str(edits["TagSet"]["overwrite_all"])
                elif "add_tags" in edits["TagSet"]:
                    for tag in edits["TagSet"]["add_tags"]:
                        tagset.add(tag)
                        logger.info(f"Added tag {tag} to {unit_row.namespace}")
                
        elif descr_type == "TVisibilityModuleDescriptor":
            if "Stealth" in edits:
                descr_row.v.by_member("UnitConcealmentBonus").v = str(edits["Stealth"])
                
        elif descr_row.namespace == "ApparenceModel":
            if "NewName" in edits and not edits["is_ground_vehicle"]:
                descr_row.v.by_member("Depiction").v = f"$/GFX/Depiction/Gfx_{edits['NewName']}"
                
        elif descr_row.namespace == "WeaponManager":
            if "NewName" in edits:
                descr_row.v.by_member("Default").v = f"$/GFX/Weapon/WeaponDescriptor_{edits['NewName']}"
                
        elif descr_type == "TBaseDamageModuleDescriptor":
            if "strength" in edits:
                descr_row.v.by_member("MaxPhysicalDamages").v = str(edits["strength"])
                
        elif descr_type == "TDamageModuleDescriptor":
            _handle_damage_module(descr_row, edits)
                
        elif descr_type == "TDangerousnessModuleDescriptor":
            if "Dangerousness" in edits:
                descr_row.v.by_member("Dangerousness").v = str(edits["Dangerousness"])
                
        elif descr_row.namespace == "GroupeCombat":
            _handle_groupe_combat(descr_row, edits)
                
        elif descr_type == "TInfantrySquadWeaponAssignmentModuleDescriptor":
            if "WeaponAssignment" in edits:
                descr_row.v.by_member("InitialSoldiersToTurretIndexMap").v = f"MAP {str(edits['WeaponAssignment'])}"
                
        elif descr_row.namespace == "GenericMovement":
            if "max_speed" in edits:
                descr_row.v.by_member("Default").v.by_member("MaxSpeedInKmph").v = str(edits["max_speed"])  # noqa
                
        elif descr_type == "TTransportableModuleDescriptor":
            if "TransportedTexture" in edits:
                descr_row.v.by_member("TransportedTexture").v = f"'{edits['TransportedTexture']}'"
            if "TransportedSoldier" in edits:
                descr_row.v.by_member("TransportedSoldier").v = f"'{edits['TransportedSoldier']}'"
            
        elif descr_type == "TCadavreGeneratorModuleDescriptor":
            descr_row.v.by_member("CadavreDescriptor").v = f"~/Descriptor_UnitCadavre_{edits['NewName']}"
            
        elif descr_type == "TProductionModuleDescriptor":
            if "Factory" in edits:
                descr_row.v.by_member("Factory").v = edits["Factory"]
            if "CommandPoints" in edits:
                cmd_points = "$/GFX/Resources/Resource_CommandPoints"
                descr_row.v.by_member("ProductionRessourcesNeeded").v.by_key(cmd_points).v = str(edits["CommandPoints"])  # noqa
                
        elif descr_type == "TOrderConfigModuleDescriptor":
            if "NewName" in edits:
                descr_row.v.by_member("ValidOrders").v = f"~/Descriptor_OrderAvailability_{edits['NewName']}"
                
        elif descr_type == "TOrderableModuleDescriptor":
            if "NewName" in edits:
                descr_row.v.by_member("UnlockableOrders").v = f"~/Descriptor_OrderAvailability_{edits['NewName']}"
                
        elif descr_type == "TTacticalLabelModuleDescriptor":
            _handle_tactical_label(descr_row, edits)
                
        elif descr_type == "TStrategicDataModuleDescriptor":
            if "UnitAttackValue" in edits:
                descr_row.v.by_member("UnitAttackValue").v = str(edits["UnitAttackValue"])
            if "UnitDefenseValue" in edits:
                descr_row.v.by_member("UnitDefenseValue").v = str(edits["UnitDefenseValue"])
                
        elif descr_type == "TUnitUIModuleDescriptor":
            _handle_unit_ui(descr_row, edits)
                
        elif descr_type == "TShowRoomEquivalenceModuleDescriptor":
            descr_row.v.by_member("ShowRoomDescriptor").v = f"~/Descriptor_ShowRoomUnit_{edits['NewName']}"


def _handle_damage_module(descr_row: Any, edits: Dict[str, Any]) -> None:
    """Handle damage module modifications."""
    if "armor" in edits:
        blindage_obj = descr_row.v.by_member("BlindageProperties").v
        armor_parts = {
            "front": "ResistanceFront",
            "sides": "ResistanceSide",
            "rear": "ResistanceRear",
            "top": "ResistanceTop"
        }
        for part, resistance in armor_parts.items():
            if part in edits["armor"]:
                blindage_obj.by_member(resistance).v.by_member("Index").v = str(edits["armor"][part])
        if "era" in edits["armor"]:
            blindage_obj.by_member("ExplosiveReactiveArmor").v = str(edits["armor"]["era"])
    
    elif not edits["is_ground_vehicle"] and edits["is_infantry"]:
        inf_strength = int(edits["strength"])
        armor_level = str(15 - inf_strength)
        blindage_obj = descr_row.v.by_member("BlindageProperties").v
        for side in ["Front", "Sides", "Rear", "Top"]:
            side_blindage_obj = blindage_obj.by_member(f"Resistance{side}").v
            side_blindage_obj.by_member("Family").v = "ResistanceFamily_infanterieWA"
            side_blindage_obj.by_member("Index").v = armor_level


def _handle_groupe_combat(descr_row: Any, edits: Dict[str, Any]) -> None:
    """Handle groupe combat module modifications."""
    default_member = descr_row.v.by_member("Default")
    mimetic_descr = default_member.v.by_member("MimeticDescriptor")
    mimetic_descr.v.by_member("DescriptorId").v = f"GUID:{{{edits['GroupeCombatGUID']}}}"
    
    if "strength" in edits:
        default_member.v.by_member("NbSoldatInGroupeCombat").v = str(edits["strength"])
        
    if "NewName" in edits:
        default_member.v.by_member("InfantryMimeticName").v = f"'{edits['NewName']}'"
        default_member.v.by_member("WeaponUnitFXKey").v = f"'{edits['NewName']}'"
        mimetic_descr.v.by_member("MimeticName").v = f"'{edits['NewName']}'"


def _handle_tactical_label(descr_row: Any, edits: Dict[str, Any]) -> None:
    """Handle tactical label module modifications."""
    if "SortingOrder" in edits:
        descr_row.v.by_member("MultiSelectionSortingOrder").v = str(edits["SortingOrder"])
    if "IdentifiedTextures" in edits:
        id_textures_member = descr_row.v.by_member("IdentifiedTexture")
        id_textures_member.v.by_member("Values").v = str(edits["IdentifiedTextures"])
    if "UnidentifiedTextures" in edits:
        unid_textures_member = descr_row.v.by_member("UnidentifiedTexture")
        unid_textures_member.v.by_member("Values").v = str(edits["UnidentifiedTextures"])
    if "strength" in edits:
        descr_row.v.by_member("NbSoldiers").v = str(edits["strength"])


def _handle_unit_ui(descr_row: Any, edits: Dict[str, Any]) -> None:
    """Handle unit UI module modifications."""
    if "SpecialitiesList" in edits:
        edited_list = ndf.convert(str(edits["SpecialitiesList"]))
        descr_row.v.by_member("SpecialtiesList").v = edited_list
    if "GameName" in edits and "token" in edits["GameName"]:
        descr_row.v.by_member("NameToken").v = f'\"{edits["GameName"]["token"]}\"'
    if "UpgradeFromUnit" in edits:
        if descr_row.v.by_m("UpgradeFromUnit", False) is not None:
            if edits["UpgradeFromUnit"] is None:
                descr_row.v.remove_by_member("UpgradeFromUnit")
            else:
                descr_row.v.by_m("UpgradeFromUnit").v = f"Descriptor_Unit_{edits['UpgradeFromUnit']}"
        elif edits["UpgradeFromUnit"] is not None:
            descr_row.v.add(f"UpgradeFromUnit = Descriptor_Unit_{edits['UpgradeFromUnit']}")
    if "MenuIconTexture" in edits:
        descr_row.v.by_member("MenuIconTexture").v = f"'{edits['MenuIconTexture']}'"
    if "ButtonTexture" in edits:
        descr_row.v.by_member("ButtonTexture").v = f"'Texture_Button_Unit_{edits['ButtonTexture']}'"
    if "TypeStrategicCount" in edits:
        descr_row.v.by_member("TypeStrategicCount").v = edits["TypeStrategicCount"]
    descr_row.v.by_member("ButtonTexture").v = f"'Texture_Button_Unit_{edits['NewName']}'"
