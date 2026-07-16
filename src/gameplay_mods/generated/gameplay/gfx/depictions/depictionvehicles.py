"""Functions for modifying DepictionVehicles.ndf"""

from typing import Any
import traceback

from src import ndf
from src.constants.new_units import NEW_DEPICTIONS, NEW_UNITS
from src.constants.unit_edits import load_depiction_edits
from src.gameplay_mods.generated.gameplay.gfx.depictions._apply import apply_indexed_list_ops
from src.gameplay_mods.generated.gameplay.gfx.depictions.he_dca_air_depiction import (
    apply_he_dca_air_depiction_weapons,
)
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_blackhole_key

logger = setup_logger(__name__)


def _mesh_stem_for_subdepiction_generator(unit_name: str, edit_value: Any = None) -> str:
    """Resolve the Modele_ stem used by towed/transported subdepiction generators.

    New units cloned from a donor reuse the donor mesh unless ``depictions.new_mesh``
    is set. An explicit ``edit_value`` of ``{"mesh": "<stem>"}`` or a string stem
    overrides the default.
    """
    if isinstance(edit_value, str) and edit_value:
        return edit_value
    if isinstance(edit_value, dict) and edit_value.get("mesh"):
        return edit_value["mesh"]

    for donor_key, edits in NEW_UNITS.items():
        if edits.get("NewName") != unit_name:
            continue
        donor_name = donor_key[0] if isinstance(donor_key, tuple) else donor_key
        depiction_opts = edits.get("depictions", {})
        if depiction_opts.get("new_mesh"):
            return unit_name
        if depiction_opts.get("alternatives"):
            return depiction_opts["alternatives"]
        return donor_name

    return unit_name


def edit_gen_gp_gfx_depictionvehicles(source_path: Any, game_db: Any = None) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionVehicles.ndf"""
    
    # TODO: Hastily written (albeit functional) code that needs rewriting and refactoring
    _handle_new_units(source_path)
    _handle_unit_edits(source_path)
    # After new-unit clones and hand-authored depiction_edits so AIR operators append.
    apply_he_dca_air_depiction_weapons(source_path, game_db or {}, logger)
 
    
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
        """Create a new depiction object with updated namespace or BlackHoleKey."""
        new_obj = obj_row_.copy()
        if is_weapon:
            new_obj.namespace = f"DepictionOperator_{unit_name_}_Weapon{weapon_num}"
        else:
            # For TacticVehicleDepictionRegistration, set BlackHoleKey instead of namespace
            # Unit model objects are always unnamed now
            new_obj.namespace = None
            blackhole_key_member = new_obj.v.by_m("BlackHoleKey")
            blackhole_key_member.v = f"'{unit_name_}'"
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

            # Find donor vehicle depiction by BlackHoleKey
            donor_vehicle = find_obj_by_blackhole_key(source_path, donor_name, "TacticVehicleDepictionRegistration")
            
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
                obj_desc = obj.namespace if obj.namespace else f"BlackHoleKey={obj.v.by_m('BlackHoleKey').v}"
                logger.info(f"Adding new object to DepictionVehicles.ndf: {obj_desc}")
                source_path.add(obj)

    _apply_new_unit_vehicle_depiction_edits(source_path)


def _apply_new_unit_vehicle_depiction_edits(source_path: Any) -> None:
    """Apply tuple-key NEW_DEPICTIONS patches to cloned vehicle registrations."""

    for donor, edits in NEW_UNITS.items():
        if not edits.get("is_ground_vehicle", False):
            continue

        unit_name = edits["NewName"]
        depiction_key = unit_name.lower()
        veh_edits = NEW_DEPICTIONS.get(depiction_key, {}).get("DepictionVehicles_ndf", {}) or {}

        for key, section_edits in veh_edits.items():
            if not isinstance(key, tuple):
                continue

            namespace, obj_type = key

            if namespace and namespace.startswith("DepictionOperator_"):
                weapon_operator = source_path.by_n(namespace)
                if weapon_operator:
                    _handle_weapon_operator(unit_name, weapon_operator, section_edits)
                    logger.info(f"Updated weapon operator for {unit_name}")

            elif obj_type == "TacticVehicleDepictionRegistration":
                vehicle_depiction = find_obj_by_blackhole_key(
                    source_path, unit_name, "TacticVehicleDepictionRegistration",
                )
                if vehicle_depiction:
                    _handle_vehicle_depiction(unit_name, vehicle_depiction, section_edits)
                    logger.info(f"Updated vehicle depiction for {unit_name}")
                else:
                    logger.error(
                        f"Could not find TacticVehicleDepictionRegistration with "
                        f"BlackHoleKey='{unit_name}' for NEW_DEPICTIONS patch",
                    )


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
            if key == "new_objects":
                registration = find_obj_by_blackhole_key(
                    source_path, unit_name, "TacticVehicleDepictionRegistration")
                if registration is None:
                    logger.error(f"Could not find TacticVehicleDepictionRegistration for {unit_name}, appending new objects to end")
                    for obj_key, ndf_str in edits.items():
                        source_path.add(ndf.convert(ndf_str))
                        logger.info(f"Added new operator {obj_key} for {unit_name}")
                else:
                    insert_index = registration.index
                    for obj_key, ndf_str in edits.items():
                        source_path.insert(insert_index, ndf.convert(ndf_str))
                        logger.info(f"Inserted new operator {obj_key} for {unit_name}")
                        insert_index += 1
                continue

            if not isinstance(key, tuple):
                logger.error(f"Key is not a tuple: {key}")
                continue

            namespace, obj_type = key

            if namespace and namespace.startswith("DepictionOperator_"):
                weapon_operator = source_path.by_n(namespace)
                if weapon_operator:
                    _handle_weapon_operator(unit_name, weapon_operator, edits)
                    logger.info(f"Updated weapon operator for {unit_name}")

            elif obj_type == "TacticVehicleDepictionRegistration":
                vehicle_depiction = find_obj_by_blackhole_key(
                    source_path, unit_name, "TacticVehicleDepictionRegistration")
                if vehicle_depiction:
                    _handle_vehicle_depiction(unit_name, vehicle_depiction, edits)
                    logger.info(f"Updated vehicle depiction for {unit_name}")
                else:
                    logger.error(f"Could not find TacticVehicleDepictionRegistration with BlackHoleKey='{unit_name}'")


def _handle_weapon_operator(unit_name, weapon_operator, edits, is_new_entry=False):  # noqa
    for row_name_or_type, value in edits.items():
        member_access = weapon_operator.v.by_m(row_name_or_type, False)
        if member_access is None:
            continue

        if row_name_or_type == "FireEffectTag":
            member_access.v = value
        elif row_name_or_type == "WeaponActiveAndCanShootPropertyName":
            member_access.v = value
        elif row_name_or_type == "Connoisseur":
            member_access.v = value
        elif row_name_or_type == "WeaponShootDataPropertyName":
            # ContinuousFire uses scalar; InstantFire/MissileCarriage use list
            if getattr(weapon_operator.v, "type", None) == "DepictionOperator_WeaponContinuousFire" and isinstance(value, list) and len(value) == 1:
                member_access.v = value[0]
            else:
                member_access.v = "[" + ",".join(value) + "]"

    return weapon_operator


def _vehicle_op_add(list_member: Any, op_index: int, payload: Any) -> None:
    """Insert a vehicle operator at ``op_index`` (used by the ``add`` op)."""
    list_member.v.insert(op_index, payload)


def _handle_vehicle_depiction(unit_name, vehicle_depiction, edits, is_new_entry=False):  # noqa
    for row_name_or_type, value in edits.items():
        member_access = vehicle_depiction.v.by_m(row_name_or_type, False)
        if row_name_or_type == "Operators":
            apply_indexed_list_ops(
                member_access,
                value,
                label=f"Vehicle Operators ({unit_name})",
                op_handlers={"add": _vehicle_op_add},
            )

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
                                    apply_indexed_list_ops(
                                        depiction_member.v.by_m(dep_name_or_type),
                                        dep_edits,
                                        label=f"SubDepictions[{sub_depict_index}].Operators ({unit_name})",
                                        op_handlers={"add": _vehicle_op_add},
                                    )

                                elif dep_name_or_type == "Actions":
                                    apply_indexed_list_ops(
                                        depiction_member.v.by_m(dep_name_or_type),
                                        dep_edits,
                                        label=f"SubDepictions[{sub_depict_index}].Actions ({unit_name})",
                                        op_handlers={"add": _vehicle_op_add},
                                    )
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
                            mesh_stem = _mesh_stem_for_subdepiction_generator(unit_name, edit_value)
                            new_entry = f"""TransportedInfantrySubGenerator
                                (
                                    Mesh = $/GFX/DepictionResources/Modele_{mesh_stem}
                                )"""
                            sub_dep_generators.v.add(new_entry)
                            vehicle_depiction.v.add(sub_dep_generators)
                elif sub_dep_type == "TowedUnitSubDepictionGenerator":
                    for edit_type, edit_value in sub_dep_value.items():
                        if edit_type == "add":
                            mesh_stem = _mesh_stem_for_subdepiction_generator(unit_name, edit_value)
                            new_entry = f"""TowedUnitSubDepictionGenerator
                                (
                                    Mesh = $/GFX/DepictionResources/Modele_{mesh_stem}
                                )"""
                            sub_dep_generators.v.add(new_entry)
                            vehicle_depiction.v.add(sub_dep_generators)

        else:
            logger.error(f"Unknown row name or type: {row_name_or_type}")
            pass

    return vehicle_depiction