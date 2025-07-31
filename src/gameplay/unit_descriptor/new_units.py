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
    create_unit_descriptors(source_path, game_db)


def write_new_unit_dictionary_entries(unit_edits: Dict[str, Any]) -> None:
    """Write dictionary entries for new units."""
    entries = []
    
    for _, edits in unit_edits.items():
        if "GameName" in edits and "token" in edits["GameName"]:
            entries.append((edits["GameName"]["token"], edits["GameName"]["display"]))
    
    if entries:
        write_dictionary_entries(entries, dictionary_type="units")


def create_unit_descriptors(source_path: Any, game_db: Dict[str, Any]) -> None:
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
        modify_new_unit(donor_name,new_unit_row, edits, game_db)
        
        # Add the new unit to the source
        source_path.add(new_unit_row)
        logger.info(f"Added new unit: {unit_name}")


def modify_new_unit(donor_name: str, unit_row: Any, edits: Dict[str, Any], game_db: Dict[str, Any]) -> None:
    """New unit modifications in UniteDescriptor.ndf"""
    # Update basic unit properties
    unit_row.v.by_member("DescriptorId").v = f"GUID:{{{edits['GUID']}}}"
    unit_row.v.by_member("ClassNameForDebug").v = f"'Unite_{edits['NewName']}'"
    found_capacite_module = False
    
    # Process each module
    modules_list = unit_row.v.by_member("ModulesDescriptors")
    
    # First add any new modules
    modules_to_add = edits.get("modules_add", [])
    if modules_to_add:
        for module in modules_to_add:
            modules_list.v.add(module)
    
    # Then handle module removal and modifications
    modules_to_remove = []
    for descr_row in modules_list.v:
        # Check if module should be removed
        if "modules_remove" in edits:
            should_remove = False
            if isinstance(descr_row.v, ndf.model.Object):
                # Handle object modules
                if descr_row.v.type in edits["modules_remove"]:
                    should_remove = True
                elif hasattr(descr_row, "namespace") and descr_row.namespace in edits["modules_remove"]:
                    should_remove = True
            else:
                # Handle string modules
                if hasattr(descr_row, "namespace") and descr_row.namespace in edits["modules_remove"]:
                    should_remove = True
                elif any(descr_row.v == module for module in edits["modules_remove"]):
                    should_remove = True
            
            if should_remove:
                modules_to_remove.append(descr_row)
                logger.info(f"Marked for removal: {getattr(descr_row, 'namespace', descr_row.v)}")
                continue
        
        # If not being removed, handle module modifications
        if isinstance(descr_row.v, ndf.model.Object):
            descr_type = descr_row.v.type
            

            if descr_type == "TTypeUnitModuleDescriptor":
                if "TypeUnit" in edits:
                    for member, value in edits["TypeUnit"].items():
                        if member == "TypeUnitFormation":
                            # TODO: Confirm if Eugen removed this or if they moved it somewhere else
                            continue
                        else:
                            descr_row.v.by_member(member).v = value
                        
            if descr_type == "TTagsModuleDescriptor":
                if "TagSet" not in edits:
                    logger.warning(f"No TagSet found for {unit_row.namespace}")
                else:
                    _handle_tags_module(descr_row, edits)
                
            elif descr_type == "TVisibilityModuleDescriptor":
                if "Stealth" in edits:
                    descr_row.v.by_member("UnitConcealmentBonus").v = str(edits["Stealth"])
                    
            elif descr_type == "TAutoCoverModuleDescriptor":
                descr_row.v.by_member("AutoCoverRangeGRU").v = "70"
                
            elif descr_type == "TBaseDamageModuleDescriptor":
                if "strength" in edits:
                    descr_row.v.by_member("MaxPhysicalDamages").v = str(edits["strength"])
                    
            elif descr_type == "TDamageModuleDescriptor":
                _handle_damage_module(descr_row, edits)
                
            elif descr_type == "TDangerousnessModuleDescriptor":
                if "Dangerousness" in edits:
                    descr_row.v.by_member("Dangerousness").v = str(edits["Dangerousness"])
                    
            # elif descr_type == "TInfantrySquadWeaponAssignmentModuleDescriptor":
            #     if "WeaponAssignment" in edits:
            #         descr_row.v.by_member("InitialSoldiersToTurretIndexMap").v = f"MAP {str(edits['WeaponAssignment'])}"
                    
            elif descr_type == "TTransportableModuleDescriptor":
                if "TransportedTexture" in edits:
                    descr_row.v.by_member("TransportedTexture").v = f"'{edits['TransportedTexture']}'"
                if "TransportedSoldier" in edits:
                    descr_row.v.by_member("TransportedSoldier").v = f"'{edits['TransportedSoldier']}'"
            
            elif descr_type == "TModuleSelector":
                if "capacities" in edits:
                    default_membr = descr_row.v.by_m("Default")
                    if hasattr(default_membr.v, 'type') and default_membr.v.type == "TCapaciteModuleDescriptor":
                        found_capacite_module = True
                        _handle_capacities_module(default_membr, edits)
                    
            elif descr_type == "TCadavreGeneratorModuleDescriptor":
                descr_row.v.by_member("CadavreDescriptor").v = f"~/Descriptor_UnitCadavre_{edits['NewName']}"
                    
            elif descr_type == "TProductionModuleDescriptor":
                if "Factory" in edits:
                    descr_row.v.by_member("FactoryType").v = edits["Factory"]
                if "CommandPoints" in edits:
                    cmd_points = "$/GFX/Resources/Resource_CommandPoints"
                    descr_row.v.by_member("ProductionRessourcesNeeded").v.by_key(cmd_points).v = str(edits["CommandPoints"])  # noqa
            
            elif descr_type == "TCubeActionModuleDescriptor":
                if "CubeActionDescriptor" in edits:
                    new_value = f"$/GFX/UI/CubeAction_Menu_Ordres_{edits['CubeActionDescriptor']}"
                    descr_row.v.by_member("CubeActionDescriptor").v = new_value
                    
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
        
        # Handle special namespace cases
        if hasattr(descr_row, "namespace"):
            if descr_row.namespace == "ApparenceModel":
                if "NewName" in edits and "depictions" in edits:
                    descr_row.v.by_member("Depiction").v = f"$/GFX/Depiction/Gfx_{edits['NewName']}"
                    
            elif descr_row.namespace == "WeaponManager":
                if "NewName" in edits:
                    descr_row.v.by_member("Default").v = f"$/GFX/Weapon/WeaponDescriptor_{edits['NewName']}"
                    
            elif descr_row.namespace == "GroupeCombat":
                _handle_groupe_combat(descr_row, edits)
                
            elif descr_row.namespace == "GenericMovement":
                if "max_speed" in edits:
                    descr_row.v.by_member("Default").v.by_member("MaxSpeedInKmph").v = str(edits["max_speed"])  # noqa
    
    if not found_capacite_module:
        capacities_to_add = edits.get("capacities", {}).get("add_capacities", [])
        if capacities_to_add:
            skill_prefix = "$/GFX/EffectCapacity/Capacite_"
            new_entry = (
                f'TModuleSelector'
                f'('
                f'    Default = TCapaciteModuleDescriptor'
                f'    ('
                f'        DefaultSkillList = ['
                f'            {", ".join(skill_prefix + skill for skill in capacities_to_add)}'
                f'        ]'
                f'    )'
                f'    Condition = ~/IfNotCadavreCondition'
                f')'
            )
            modules_list.v.add(new_entry)
            logger.info(f"Added capacity module to {unit_row.namespace}")
    
    # Remove all marked modules at the end
    for module in modules_to_remove:
        modules_list.v.remove(module)


def _handle_damage_module(descr_row: Any, edits: Dict[str, Any]) -> None:
    """Handle damage module modifications."""
    if "armor" in edits:
        blindage_obj = descr_row.v.by_member("BlindageProperties").v
        armor_parts = {
            "front": "ResistanceFront",
            "sides": "ResistanceSides",
            "rear": "ResistanceRear",
            "top": "ResistanceTop"
        }
        for part, resistance in armor_parts.items():
            if part in edits["armor"]:
                blindage_obj.by_member(resistance).v.by_member("Index").v = str(edits["armor"][part])
        if "era" in edits["armor"]:
            blindage_obj.by_member("ExplosiveReactiveArmor").v = str(edits["armor"]["era"])
    
    elif not edits.get("is_ground_vehicle", False) and edits.get("is_infantry", False):
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
    # if "strength" in edits:
    #     descr_row.v.by_member("NbSoldiers").v = str(edits["strength"])


def _handle_tags_module(descr_row: Any, edits: Dict[str, Any]) -> None:
    """Handle tags module modifications."""
    tagset = descr_row.v.by_member("TagSet")
    if "overwrite_all" in edits["TagSet"]:
        new_tags = []
        for tag in edits["TagSet"]["overwrite_all"]:
            new_tags.append(tag)
        tagset.v = ndf.convert(str(new_tags))
    elif "add_tags" in edits["TagSet"]:
        for tag in edits["TagSet"]["add_tags"]:
            formatted_tag = '"' + tag + '"'
            tagset.v.add(formatted_tag)
            logger.info(f"Added tag {formatted_tag} to {descr_row.namespace}")


def _handle_unit_ui(descr_row: Any, edits: Dict[str, Any]) -> None:
    """Handle unit UI module modifications."""
    if "SpecialitiesList" in edits:
        edited_list = ndf.convert(str(edits["SpecialitiesList"]))
        descr_row.v.by_member("SpecialtiesList").v = edited_list
    if "InfoPanelConfig" in edits:
        descr_row.v.by_member("InfoPanelConfigurationToken").v = f"'{edits['InfoPanelConfig']}'"
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
    if "Nation" in edits:
        descr_row.v.by_member("CountryTexture").v = f"'CommonTexture_MotherCountryFlag_{edits['Nation']}'"
    if "TypeStrategicCount" in edits:
        descr_row.v.by_member("TypeStrategicCount").v = edits["TypeStrategicCount"]
    descr_row.v.by_member("ButtonTexture").v = f"'Texture_Button_Unit_{edits['NewName']}'"


def _handle_capacities_module(default_membr: Any, edits: Dict[str, Any]) -> None:
    """Handle capacities module modifications."""
        
    capacities_to_add = edits["capacities"].get("add_capacities", [])
    capacities_to_remove = edits["capacities"].get("remove_capacities", [])
        
    skill_list = default_membr.v.by_m("DefaultSkillList")
    skill_prefix = "$/GFX/EffectCapacity/Capacite_"
    for skill in skill_list.v:
        if skill.v.replace(skill_prefix, "") in capacities_to_remove:
            skill_list.v.remove(skill.index)
    for skill in capacities_to_add:
        skill_list.v.add(skill_prefix + skill)
