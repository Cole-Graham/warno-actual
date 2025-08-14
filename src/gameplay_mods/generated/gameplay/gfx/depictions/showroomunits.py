"""Functions for modifying ShowRoomUnits.ndf"""
from typing import Any, Dict

from src import ndf
from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_type, find_obj_by_namespace, generate_guid

logger = setup_logger(__name__)


def edit_gen_gp_gfx_showroomunits(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/ShowRoomUnits.ndf"""
    
    unit_edits = load_unit_edits()
    
    logger.info("Processing unit edits for ShowRoomUnits.ndf")
    _handle_unit_edits(source_path, unit_edits)
    
    logger.info("Processing new units for ShowRoomUnits.ndf")
    _handle_new_units(source_path)


def _handle_unit_edits(source_path: Any, unit_edits: Dict[str, Any]) -> None:
    """Handle unit edits for ShowRoomUnits.ndf"""
    for unit_name, edits in unit_edits.items():
        prefix = "Descriptor_ShowRoomUnit_"
        unit_obj = find_obj_by_namespace(source_path, f"{prefix}{unit_name}")
        if not unit_obj:
            logger.warning(f"Unit {unit_name} not found in ShowRoomUnits.ndf")
            continue
        
        modules_list = unit_obj.v.by_m("ModulesDescriptors")
        for module in modules_list.v:
            new_name = edits.get("NewName", None)
            if not isinstance(module.v, ndf.model.Object):
                if new_name and module.startswith("$/GFX/Weapon/WeaponDescriptor_"):
                    modules_list.replace(module, f"$/GFX/Weapon/WeaponDescriptor_{new_name}")
                else:
                    continue
                
        infantry_squad_module = find_obj_by_type(modules_list.v, "TInfantrySquadModuleDescriptor")
        if infantry_squad_module and edits.get("strength", None):
            infantry_squad_module.v.by_m("NbSoldatInGroupeCombat").v = str(edits["strength"])
            logger.info(f"Updated strength for {unit_name} to {edits['strength']}")
         
            
def _handle_new_units(source_path: Any) -> None:
    """Handle new units for ShowRoomUnits.ndf"""
    
    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if "NewName" not in edits:
            continue

        unit_name = edits["NewName"]
        donor_unit = source_path.by_n(f"Descriptor_ShowRoomUnit_{donor_name}")
        if not donor_unit:
            logger.warning(f"Donor showroom unit {donor_name} not found")
            continue

        # Clone donor showroom unit
        try:
            new_unit = donor_unit.copy()
        except Exception as e:
            logger.error(f"Failed to copy donor showroom unit {donor_name}: {str(e)}")
            raise

        new_unit.namespace = f"Descriptor_ShowRoomUnit_{unit_name}"

        # Update basic properties
        new_unit.v.by_member("DescriptorId").v = f"GUID:{{{edits['ShowroomGUID']}}}"
        new_unit.v.by_member("ClassNameForDebug").v = f"'ShowRoomUnit_{unit_name}'"

        # Update modules
        modules_list = new_unit.v.by_member("ModulesDescriptors")
        for module in modules_list.v:

            if "modules_remove" in edits:
                if "WeaponDescriptor" in edits["modules_remove"]:
                    if not isinstance(module.v, ndf.model.Object):
                        if module.v == "$/GFX/Weapon/WeaponDescriptor_" + donor_name:
                            modules_list.v.remove(module.index)
                            continue

            if not isinstance(module.v, ndf.model.Object):
                if module.v == "$/GFX/Weapon/WeaponDescriptor_" + donor_name:
                    modules_list.v.replace(module, f"$/GFX/Weapon/WeaponDescriptor_{edits['NewName']}")
                    continue
                else:
                    continue

            module_type = module.v.type

            if module_type == "TTypeUnitModuleDescriptor":
                if "TypeUnit" in edits:
                    for member, value in edits["TypeUnit"].items():
                        module.v.by_member(member).v = value

            elif module_type == "TApparenceModuleDescriptor":
                if not edits.get("is_ground_vehicle", False):
                    module.v.by_member("Depiction").v = "$/DepictionCore/InfantryDepictionSquadShowroom"
                else:
                    module.v.by_member("Depiction").v = f"$/GFX/Depiction/Gfx_{unit_name}_Showroom"

            elif module_type == "TInfantrySquadModuleDescriptor":
                if "strength" in edits:
                    module.v.by_member("NbSoldatInGroupeCombat").v = str(edits["strength"])
                module.v.by_member("InfantryMimeticName").v = f"'{unit_name}'"
                module.v.by_member("WeaponUnitFXKey").v = f"'{unit_name}'"

                # Update mimetic descriptor
                mimetic = module.v.by_member("MimeticDescriptor").v
                mimetic.by_member("DescriptorId").v = f"GUID:{{{generate_guid()}}}"  # noqa
                mimetic.by_member("MimeticName").v = f"'{unit_name}'"  # noqa

            # elif module_type == "TInfantrySquadWeaponAssignmentModuleDescriptor":
            #     if "WeaponAssignment" in edits:
            #         module.v.by_member("InitialSoldiersToTurretIndexMap").v = f"MAP {str(edits['WeaponAssignment'])}"

            elif module_type == "TCameraShowroomModuleDescriptor":
                if edits.get("is_infantry", False):
                    module.v.by_member("SpawnType").v = "EShowroomSpawnType/Infantry"
                elif edits.get("is_ground_vehicle", False):
                    module.v.by_member("SpawnType").v = "EShowroomSpawnType/Vehicle"

            elif module_type == "TTypeUnitModuleDescriptor":
                module.v.by_member("MotherCountry").v = f"'{edits['Nation']}'"
                if edits.get("is_infantry", False):
                    module.v.by_member("AcknowUnitType").v = "~/TAcknowUnitType_Inf"
                    module.v.by_member("TypeUnitFormation").v = "'Char'"

        # Add the new showroom unit
        source_path.add(new_unit)
        logger.info(f"Added showroom entry for {unit_name}")