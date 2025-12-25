"""Functions for modifying DepictionVehicles.ndf"""

from typing import Any
import traceback

from src import ndf
from src.constants.new_units import NEW_DEPICTIONS, NEW_UNITS
from src.constants.unit_edits import load_depiction_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_type, find_obj_by_namespace, find_obj_by_coating_name

logger = setup_logger(__name__)


def edit_gen_gp_gfx_depictionvehicles(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionVehicles.ndf"""
    
    # TODO: Hastily written (albeit functional) code that needs rewriting and refactoring
    _handle_new_units(source_path)
    _handle_unit_edits(source_path)
 
    
def _handle_new_units(source_path: Any) -> None:
    """Handle new units for DepictionVehicles.ndf"""
    
    logger.info("Creating vehicle depiction entries")

    def get_base_namespace(namespace_: str, prefix: str) -> str:
        """Extract the base namespace after the given prefix.
        Only used for DepictionOperator objects (unit models are unnamed)."""
        if namespace_.startswith("DepictionOperator"):
            parts = namespace_.split(f"{prefix}_")[-1].rsplit("_", 1)[0]
            return parts  # Return parts directly
        return ""

    def create_new_object(
        obj_row_: Any, unit_name_: str, is_weapon: bool, weapon_num: int = 0, edits: dict = None
    ) -> Any:
        """Create a new depiction object with updated namespace or CoatingName."""
        new_obj = obj_row_.copy()
        if is_weapon:
            new_obj.namespace = f"DepictionOperator_{unit_name_}_Weapon{weapon_num}"
        else:
            # For TacticVehicleDepictionRegistration, set CoatingName instead of namespace
            # Unit model objects are always unnamed now
            new_obj.namespace = None
            coating_member = new_obj.v.by_m("CoatingName")
            coating_member.v = f"'{unit_name_}'"
            depiction_veh_edits = edits.get("depictions", {}).get("remove", {}).get("DepictionVehicles_ndf", {})
            if "remove_members" in depiction_veh_edits:
                for member in depiction_veh_edits["remove_members"]:
                    new_obj.v.remove_by_member(member)
        return new_obj
    
    # TMimeticUnitRegistration no longer exists in these files

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if not edits.get("is_ground_vehicle", False):
            continue

        unit_name = edits["NewName"]

        custom_depictions = edits.get("depictions", {}).get("custom", {}).get("DepictionVehicles.ndf", [])
        custom_veh_added = False
        custom_operator_added = False

        # Handle custom depictions first
        depiction_key = unit_name.lower()
        if depiction_key in NEW_DEPICTIONS:
            # Add TacticVehicleDepictionRegistration if present
            if "TacticVehicleDepictionRegistration" in custom_depictions:
                custom_veh_added = True
                custom_veh_depiction = NEW_DEPICTIONS[depiction_key]["DepictionVehicles_ndf"][
                    "TacticVehicleDepictionRegistration"
                ]
                source_path.add(custom_veh_depiction)
                logger.info(f"Added custom vehicle depiction for {unit_name}")

            # Add DepictionOperator if present
            if "DepictionOperator_WeaponContinuousFire" in custom_depictions:
                custom_operator_added = True
                custom_operator = NEW_DEPICTIONS[depiction_key]["DepictionVehicles_ndf"][
                    "DepictionOperator_WeaponContinuousFire"
                ]
                source_path.add(custom_operator)
                logger.info(f"Added custom operator depiction for {unit_name}")
        else:
            if (
                "TacticVehicleDepictionRegistration" in custom_depictions
                or "DepictionOperator_WeaponContinuousFire" in custom_depictions
            ):
                logger.warning(f"No custom depiction found for {unit_name} (key: {depiction_key})")

        # Handle default depictions if customs were not added
        if not custom_veh_added or not custom_operator_added:
            weapon_count = 0
            new_objects = []

            # Find donor vehicle depiction by CoatingName
            donor_vehicle = find_obj_by_coating_name(source_path, donor_name, "TacticVehicleDepictionRegistration")
            
            for obj_row in source_path:
                namespace = obj_row.namespace
                
                if "DepictionOperator_" in (namespace or "") and not custom_operator_added:
                    base_namespace = get_base_namespace(namespace, "DepictionOperator")
                    if donor_name == base_namespace:
                        weapon_count += 1
                        new_objects.append(create_new_object(obj_row, unit_name, True, weapon_count, edits))

                elif not custom_veh_added and donor_vehicle and obj_row.v == donor_vehicle.v:
                    # Found the donor vehicle depiction
                    new_objects.append(create_new_object(obj_row, unit_name, False, weapon_count, edits))

            for obj in new_objects:
                obj_desc = obj.namespace if obj.namespace else f"CoatingName={obj.v.by_m('CoatingName').v}"
                logger.info(f"Adding new object to DepictionVehicles.ndf: {obj_desc}")
                source_path.add(obj)
        
        # TMimeticUnitRegistration no longer exists in these files
                

def _handle_unit_edits(source_path: Any) -> None:
    """Handle unit edits for DepictionVehicles.ndf"""
    
    ndf_file = "DepictionVehicles.ndf"

    # Load all depiction edits
    depiction_edits = load_depiction_edits()

    # Process each unit's edits
    for unit_name, unit_data in depiction_edits.items():
        # Skip if this file isn't relevant for this unit
        if ndf_file not in unit_data["valid_files"]:
            continue

        # Get edits for this file
        if "DepictionVehicles_ndf" not in unit_data:
            logger.error(f"{ndf_file} is valid for {unit_name} but no edits found")
            continue

        unit_edits = unit_data["DepictionVehicles_ndf"]

        for key, edits in unit_edits.items():
            if not isinstance(key, tuple):
                logger.error(f"Key is not a tuple: {key}")
                continue

            namespace, obj_type = key
            if "copy" in edits:
                if namespace and namespace.startswith("DepictionOperator_"):
                    # Handle weapon operator copy
                    donor = source_path.by_n(namespace)
                    if not donor:
                        logger.error(f"Could not find donor {namespace} for {unit_name}")
                        continue

                    new_entry = donor.copy()
                    new_entry.namespace = edits["copy"]
                    new_entry.type = obj_type
                    new_entry = _handle_weapon_operator(unit_name, new_entry, edits)

                    # Calculate insertion index - find vehicle depiction by CoatingName
                    vehicle_depiction = find_obj_by_coating_name(
                        source_path, unit_name, "TacticVehicleDepictionRegistration")
                    if vehicle_depiction:
                        source_path.insert(vehicle_depiction.index, new_entry)
                    else:
                        source_path.add(new_entry)
                    logger.info(f"Inserted new weapon operator for {unit_name}")

                elif obj_type == "TacticVehicleDepictionRegistration":
                    # Handle vehicle depiction copy - unit model objects are unnamed, find by CoatingName
                    # Extract donor name from copy target or use unit_name
                    donor_name = edits.get("copy", "").replace("TacticDepiction_", "").replace("_", "")
                    if not donor_name:
                        # If no copy target specified, use the unit_name as donor
                        donor_name = unit_name
                    donor = find_obj_by_coating_name(source_path, donor_name, "TacticVehicleDepictionRegistration")
                    
                    if not donor:
                        logger.error(f"Could not find donor TacticVehicleDepictionRegistration with CoatingName='{donor_name}' for {unit_name}")
                        continue

                    new_entry = donor.copy()
                    new_entry.namespace = None  # Unit model objects are always unnamed
                    new_entry = _handle_vehicle_depiction(unit_name, new_entry, edits)
                    source_path.insert(donor.index + 1, new_entry)
                    logger.info(f"Inserted new vehicle depiction for {unit_name}")

            else:
                # Handle direct edits
                if namespace and namespace.startswith("DepictionOperator_"):
                    weapon_operator = source_path.by_n(namespace)
                    if weapon_operator:
                        _handle_weapon_operator(unit_name, weapon_operator, edits)
                        logger.info(f"Updated weapon operator for {unit_name}")

                elif obj_type == "TacticVehicleDepictionRegistration":
                    # Find vehicle depiction by CoatingName instead of namespace
                    vehicle_depiction = find_obj_by_coating_name(
                        source_path, unit_name, "TacticVehicleDepictionRegistration")
                    if vehicle_depiction:
                        _handle_vehicle_depiction(unit_name, vehicle_depiction, edits)
                        logger.info(f"Updated vehicle depiction for {unit_name}")
                    else:
                        logger.error(f"Could not find TacticVehicleDepictionRegistration with CoatingName='{unit_name}'")


def _handle_weapon_operator(unit_name, weapon_operator, edits, is_new_entry=False):  # noqa
    for row_name_or_type, value in edits.items():
        if row_name_or_type == "copy":
            continue

        member_access = weapon_operator.v.by_m(row_name_or_type)
        if row_name_or_type == "FireEffectTag":
            member_access.v = value
        elif row_name_or_type == "WeaponShootDataPropertyName":
            member_access.v = "[" + ",".join(value) + "]"

    return weapon_operator


def _handle_vehicle_depiction(unit_name, vehicle_depiction, edits, is_new_entry=False):  # noqa
    for row_name_or_type, value in edits.items():
        if row_name_or_type == "copy":
            continue

        member_access = vehicle_depiction.v.by_m(row_name_or_type, False)
        if row_name_or_type == "Operators":
            operators = member_access

            for op_index, op_edits in value.items():
                if isinstance(op_edits, tuple) and op_edits[0] == "add":
                    operators.v.insert(op_index, op_edits[1])
                else:
                    logger.error(f"Unknown operator edit: {op_edits}")
                    pass

        elif row_name_or_type == "Actions":
            try:
                member_access.v = value
            except Exception as e:
                logger.error(f"Unknown action edit: {value}")
                logger.error(f"Exception: {str(e)}")
                logger.error(f"Traceback: {traceback.format_exc()}")

        elif row_name_or_type == "SubDepictions":
            sub_depictions = member_access

            try:
                for sub_depict_index, sub_depict_edits in value.items():
                    sub_depiction = sub_depictions.v[sub_depict_index]
                    for member_name_or_type, member_edits in sub_depict_edits.items():

                        if member_name_or_type == "Depiction":
                            depiction_member = sub_depiction.v.by_m(member_name_or_type)
                            for dep_name_or_type, dep_edits in member_edits.items():

                                if dep_name_or_type == "Operators":
                                    operator_member = depiction_member.v.by_m(dep_name_or_type)
                                    for op_index, op_edits in dep_edits.items():
                                        if isinstance(op_edits, tuple) and op_edits[0] == "add":
                                            operator_member.v.insert(op_index, op_edits[1])
                                        else:
                                            logger.error(f"Unknown operator edit: {op_edits}")
                                            pass

                                elif dep_name_or_type == "Actions":
                                    action_member = depiction_member.v.by_m(dep_name_or_type)
                                    for action_index, action_edits in dep_edits.items():
                                        if isinstance(action_edits, tuple) and action_edits[0] == "add":
                                            action_member.v.insert(action_index, action_edits[1])
                                        else:
                                            logger.error(f"Unknown action edit: {action_edits}")
                                            pass
            except Exception as e:
                logger.error(f"Unknown subdepiction edit: {row_name_or_type}")
                logger.error(f"Exception: {str(e)}")
                logger.error(f"Traceback: {traceback.format_exc()}")

        elif row_name_or_type == "SubDepictionGenerators":
            if vehicle_depiction.v.by_m("SubDepictionGenerators", False) is None:
                sub_dep_generators = ndf.model.MemberRow(member="SubDepictionGenerators", value=ndf.model.List())
            else:
                sub_dep_generators = member_access

            for sub_dep_type, sub_dep_value in value.items():
                if sub_dep_type == "TransportedInfantrySubGenerator":
                    for edit_type, edit_value in sub_dep_value.items():
                        if edit_type == "add":
                            new_entry = f"""TransportedInfantrySubGenerator
                                (
                                    Mesh = $/GFX/DepictionResources/Modele_{unit_name}
                                )"""
                            sub_dep_generators.v.add(new_entry)
                            vehicle_depiction.v.add(sub_dep_generators)

        else:
            logger.error(f"Unknown row name or type: {row_name_or_type}")
            pass

    return vehicle_depiction