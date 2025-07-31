"""Functions for creating depictions for new units."""

from typing import Any

from src import ndf
from src.constants.new_units import NEW_DEPICTIONS, NEW_UNITS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import generate_guid, is_obj_type, strip_quotes

logger = setup_logger(__name__)


def create_infantry_depictions(source_path: Any, game_db: Any) -> None:
    """Create infantry depiction entries in DepictionInfantry.ndf."""
    logger.info("Creating infantry depiction entries")

    depiction_db = game_db["depiction_data"]

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if not edits.get("is_infantry", False) or edits.get("is_ground_vehicle", False):
            continue

        unit_name = edits["NewName"]
        depiction_key = unit_name.lower()

        # Clone all required objects
        depictionsquad_obj = source_path.by_namespace(f"Gfx_{donor_name}").copy()
        depictionsquad_obj.namespace = f"Gfx_{unit_name}"

        # AllWeaponAlternatives_
        weaponalternatives_obj = source_path.by_namespace(f"AllWeaponAlternatives_{donor_name}").copy()
        weaponalternatives_obj.namespace = f"AllWeaponAlternatives_{unit_name}"
        if depiction_key in NEW_DEPICTIONS:
            infantry_depiction_edits = NEW_DEPICTIONS[depiction_key].get("DepictionInfantry_ndf", {})
            if not infantry_depiction_edits:
                continue
            for (namespace, obj_type), depiction_edits in infantry_depiction_edits.items():
                if namespace is None:
                    continue
                if namespace.startswith("AllWeaponAlternatives_"):
                    for row_index, (edit_type, edit_list) in depiction_edits.items():
                        if edit_type == "edit":
                            for member, value in edit_list:
                                if member == "SelectorId":
                                    weaponalternatives_obj.v[row_index].v.by_m(member).v = f"['{value}']"
                                if member == "MeshDescriptor" or member == "ReferenceMeshForSkeleton":
                                    new_mesh = f"$/GFX/DepictionResources/Modele_{value}"
                                    weaponalternatives_obj.v[row_index].v.by_m(member).v = new_mesh
                                    logger.info(f"Changed {member} for {unit_name} to {new_mesh}")
                        elif edit_type == "add":
                            for member, value in edit_list:
                                if member == "SelectorId":
                                    selector_id = "['" + f"{value}" + "']"
                                elif member == "MeshDescriptor":
                                    mesh_member = "MeshDescriptor"
                                    mesh_descriptor = f"$/GFX/DepictionResources/Modele_{value}"
                                elif member == "ReferenceMeshForSkeleton":
                                    mesh_member = "ReferenceMeshForSkeleton"
                                    mesh_descriptor = f"$/GFX/DepictionResources/Modele_{value}"
                            new_entry = (
                                f"TDepictionVisual"
                                f"("
                                f"    SelectorId = {selector_id}"
                                f"    {mesh_member} = {mesh_descriptor}"
                                f")"
                            )
                            weaponalternatives_obj.v.insert(row_index, new_entry)

        # AllWeaponSubDepiction_
        weaponsubdepictions_obj = source_path.by_namespace(f"AllWeaponSubDepiction_{donor_name}").copy()
        weaponsubdepictions_obj.namespace = f"AllWeaponSubDepiction_{unit_name}"
        weaponsubdepictions_obj.v.by_member("Alternatives").v = f"AllWeaponAlternatives_{unit_name}"
        operators = weaponsubdepictions_obj.v.by_member("Operators")
        weapon_replacements = edits.get("WeaponDescriptor", {}).get("equipmentchanges", {}).get("replace", [])
        for replacement in weapon_replacements:
            # tuples with 4 values: old_ammo, new_ammo, old_fire_effect, new_fire_effect
            if len(replacement) == 4:
                old_fire_effect = replacement[2]
                new_fire_effect = replacement[3]
                for operator in operators.v:
                    fire_effect_val = operator.v.by_m("FireEffectTag")
                    fire_effect = fire_effect_val.v
                    current_fire_effect = strip_quotes(fire_effect).replace("FireEffect_", "")
                    if current_fire_effect == old_fire_effect:
                        operator.v.by_m("FireEffectTag").v = f'"FireEffect_{new_fire_effect}"'
                        logger.debug(f"Replaced fire effect {old_fire_effect} with {new_fire_effect}")
        if depiction_key in NEW_DEPICTIONS:
            infantry_depiction_edits = NEW_DEPICTIONS[depiction_key].get("DepictionInfantry_ndf", {})
            if not infantry_depiction_edits:
                continue
            # prevent variable shadowing from weapon_replacements loop
            if "operator" in locals():
                del operator
            for (namespace, obj_type), depiction_edits in infantry_depiction_edits.items():
                if namespace is None:
                    continue
                if namespace.startswith("AllWeaponSubDepiction_"):
                    rows_to_remove = []
                    operator_edits = depiction_edits.get("Operators", {})
                    for operator_index, (edit_type, edit_list) in operator_edits.items():
                        if edit_type == "edit":
                            for member, value in edit_list:
                                if member == "FireEffectTag":
                                    operator = operators.v[operator_index]
                                    operator.v.by_m(member).v = f'"FireEffect_{value}"'
                        elif edit_type == "remove":
                            rows_to_remove.append(operator_index)
                        elif edit_type == "add":
                            for member, value in edit_list:
                                if member == "FireEffectTag":
                                    effect_tag = f'"FireEffect_{value}"'
                                elif member == "WeaponShootDataPropertyName":
                                    shoot_data_property = f'"WeaponShootData_{value}"'
                            new_entry = (
                                f"DepictionOperator_WeaponInstantFireInfantry"
                                f"("
                                f"    FireEffectTag = {effect_tag}"
                                f"    WeaponShootDataPropertyName = {shoot_data_property}"
                                f")"
                            )
                            operators.v.insert(operator_index, new_entry)
                    for row_index in reversed(rows_to_remove):
                        operators.v.remove(row_index)

        # AllWeaponSubDepictionBackpack_
        weaponbackpack_obj = source_path.by_namespace(f"AllWeaponSubDepictionBackpack_{donor_name}").copy()
        weaponbackpack_obj.namespace = f"AllWeaponSubDepictionBackpack_{unit_name}"
        weaponbackpack_obj.v.by_member("Alternatives").v = f"AllWeaponAlternatives_{unit_name}"

        # TacticDepiction_unit_Alternatives
        depictionalternatives_list = source_path.by_namespace(f"TacticDepiction_{donor_name}_Alternatives").copy()
        depictionalternatives_list.namespace = f"TacticDepiction_{unit_name}_Alternatives"
        if depiction_key in NEW_DEPICTIONS:
            infantry_depiction_edits = NEW_DEPICTIONS[depiction_key].get("DepictionInfantry_ndf", {})
            if not infantry_depiction_edits:
                continue
            for (namespace, obj_type), depiction_edits in infantry_depiction_edits.items():
                if namespace is None:
                    continue
                if namespace == f"TacticDepiction_{unit_name}_Alternatives":
                    rows_to_remove = []
                    for row_index, (edit_type, edit_list) in depiction_edits.items():
                        if edit_type == "edit":
                            for member, value in edit_list:
                                if member == "MeshDescriptor" or member == "ReferenceMeshForSkeleton":
                                    new_mesh = f"$/GFX/DepictionResources/Modele_{value}"
                                    depictionalternatives_list.v[row_index].v.by_m(member).v = new_mesh
                                    logger.info(f"Changed {member} for {unit_name} to {new_mesh}")
                        elif edit_type == "remove":
                            rows_to_remove.append(row_index)
                    for row_index in reversed(rows_to_remove):
                        depictionalternatives_list.v.remove(row_index)

        # TacticDepiction_unit_Soldier
        soldierdepiction_obj = source_path.by_namespace(f"TacticDepiction_{donor_name}_Soldier").copy()
        soldierdepiction_obj.namespace = f"TacticDepiction_{unit_name}_Soldier"
        soldierdepiction_obj.v.by_member("Selector").v = f"InfantrySelectorTactic_{edits['selector_tactic']}"
        soldierdepiction_obj.v.by_member("Alternatives").v = f"TacticDepiction_{unit_name}_Alternatives"
        soldierdepiction_obj.v.by_member("SubDepictions").v = (
            f"[AllWeaponSubDepiction_{unit_name}, AllWeaponSubDepictionBackpack_{unit_name}]"
        )
        if depiction_key in NEW_DEPICTIONS:
            infantry_depiction_edits = NEW_DEPICTIONS[depiction_key].get("DepictionInfantry_ndf", {})
            if not infantry_depiction_edits:
                continue
            for (namespace, obj_type), depiction_edits in infantry_depiction_edits.items():
                if namespace is None:
                    continue
                if namespace == f"TacticDepiction_{unit_name}_Soldier":
                    operators_list = soldierdepiction_obj.v.by_member("Operators")
                    rows_to_remove = []
                    operator_edits = depiction_edits.get("Operators", {})
                    for obj in operators_list.v:
                        if is_obj_type(obj.v, "DepictionOperator_SkeletalAnimation2_Default"):
                            if obj.v.by_m("ConditionalTags", False) is not None:
                                conditional_tags = obj.v.by_m("ConditionalTags")
                            else:
                                obj.v.add(ndf.convert("ConditionalTags = []"))
                                conditional_tags = obj.v.by_m("ConditionalTags")
                    for operator_index, (edit_type, edit_list) in operator_edits.items():
                        if edit_type == "edit":
                            for conditional_tag, mesh_alternative in edit_list:
                                conditional_tags.v.replace(
                                    operator_index, f"('{conditional_tag}', '{mesh_alternative}')"
                                )
                        elif edit_type == "add":
                            for conditional_tag, mesh_alternative in edit_list:
                                conditional_tags.v.add(f"('{conditional_tag}', '{mesh_alternative}')")
                        elif edit_type == "remove":
                            rows_to_remove.append(operator_index)
                    for operator_index in reversed(rows_to_remove):
                        conditional_tags.v.remove(operator_index)

        # TacticDepiction_unit_Ghost
        ghostdepiction_obj = source_path.by_namespace(f"TacticDepiction_{donor_name}_Ghost").copy()
        ghostdepiction_obj.namespace = f"TacticDepiction_{unit_name}_Ghost"
        ghostdepiction_obj.v.by_member("Selector").v = f"InfantrySelectorTactic_{edits['selector_tactic']}"
        ghostdepiction_obj.v.by_member("Alternatives").v = f"TacticDepiction_{unit_name}_Alternatives"

        # Find insertion point
        append_row = None
        for row_count, row in enumerate(source_path, start=0):
            if row.namespace == "InfantrySelectorTactic_00_01":
                append_row = row_count
                break

        # Create comment and new entries
        comment_title = f"// *****************************[ {unit_name} ]*****************************\n"
        new_entries = (
            comment_title,
            depictionsquad_obj,
            weaponalternatives_obj,
            weaponsubdepictions_obj,
            weaponbackpack_obj,
            depictionalternatives_list,
            soldierdepiction_obj,
            ghostdepiction_obj,
        )

        # Insert new entries
        source_path.insert(append_row, new_entries)
        logger.info(f"Added depiction entries for {unit_name}")

        # Add mimetic map entries
        # source_path.by_n("InfantryMimetic").v.add((f"'{unit_name}'", f"TacticDepiction_{unit_name}_Soldier"))
        # source_path.by_n("InfantryMimeticGhost").v.add((f"'{unit_name}'", f"TacticDepiction_{unit_name}_Ghost"))

        # Add transported infantry catalog entry
        for row in source_path:
            if not isinstance(row.v, ndf.model.Object) or row.v.type != "TTransportedInfantryCatalogEntries":
                continue

            entry_list = row.v.by_member("Entries").v
            new_catalog_entry = None
            for entry in entry_list:
                if entry.v.by_member("Identifier").v == f'"{donor_name}"':
                    new_catalog_entry = entry.copy()
                    break

            # Update meshes list
            if depiction_key in NEW_DEPICTIONS:
                infantry_depiction_edits = NEW_DEPICTIONS[depiction_key].get("DepictionInfantry_ndf", {})
                if not infantry_depiction_edits:
                    continue
                for (namespace, obj_type), depiction_edits in infantry_depiction_edits.items():
                    if obj_type is None:
                        continue
                    if obj_type == "TTransportedInfantryEntry":
                        new_mesh_list = []
                        for mesh in depiction_edits["Meshes"]:
                            new_mesh_list.append(f"$/GFX/DepictionResources/Modele_{mesh}")
                        new_meshes = ndf.model.List()
                        for mesh in new_mesh_list:
                            new_meshes.add(mesh)
                        new_catalog_entry.v.by_member("Meshes").v = new_meshes
            else:
                new_mesh_list = [f"$/GFX/DepictionResources/Modele_{donor_name}"]
                for i in range(2, edits.get("alternatives_count", 1) + 1):
                    new_mesh_list.append(f"$/GFX/DepictionResources/Modele_{donor_name}_{i:02}")

                new_meshes = ndf.model.List()
                for mesh in new_mesh_list:
                    new_meshes.add(mesh)
                new_catalog_entry.v.by_member("Meshes").v = new_meshes

            unique_count = edits.get("unique_count", 0)
            new_catalog_entry.v.by_member("Count").v = str(edits.get("alternatives_count", 1))
            new_catalog_entry.v.by_member("Identifier").v = f'"{unit_name}"'
            new_catalog_entry.v.by_member("UniqueCount").v = str(unique_count)
            new_catalog_entry.v.by_m("UnitMimetic").v = f"TacticDepiction_{unit_name}_Soldier"
            new_catalog_entry.v.by_m("UnitMimeticGhost").v = f"TacticDepiction_{unit_name}_Ghost"

            entry_list.add(new_catalog_entry)
            logger.info(f"Added transported infantry catalog entry for {unit_name}")


def create_showroom_depictions(source_path: Any) -> None:
    """Create showroom entries in ShowRoomUnits.ndf."""
    logger.info("Creating showroom depiction entries")

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
                    module.v.by_member("Depiction").v = "$/GFX/Depiction/InfantryDepictionSquadShowroom"
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


def create_button_textures(source_path: Any) -> None:
    """Create button texture entries in ButtonTexturesUnites.ndf."""
    logger.info("Creating button texture entries")

    textures_map = source_path.by_n("UnitButtonTextureAdditionalBank").v.by_member("Textures").v

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if "NewName" not in edits:
            continue

        unit_name = edits["NewName"]
        donor_texture_map = textures_map.by_key(f'"Texture_Button_Unit_{donor_name}"').v

        # Get the texture filename either from ButtonTexture override or donor unit
        if "ButtonTexture" in edits:
            # Use specified texture from another unit
            specific_texture_map = textures_map.by_key(f'"Texture_Button_Unit_{edits["ButtonTexture"]}"').v
            button_texture = specific_texture_map.by_key("~/ComponentState/Normal").v.by_member("FileName").v
        else:
            # Use donor unit's texture
            button_texture = donor_texture_map.by_key("~/ComponentState/Normal").v.by_member("FileName").v

        # Create new texture entry
        new_entry_key = f'"Texture_Button_Unit_{unit_name}"'
        new_entry_value = (
            f"MAP [(" f"~/ComponentState/Normal, " f"TUIResourceTexture( FileName = {button_texture}" f"))]"
        )

        # Add to textures map
        textures_map.add((new_entry_key, new_entry_value))
        logger.info(f"Added button texture for {unit_name} using texture {button_texture}")


def create_cadavre_depictions(source_path: Any) -> None:
    """Create cadavre depiction entries in UniteCadavreDescriptor.ndf."""
    logger.info("Creating cadavre depiction entries")

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if "NewName" not in edits or "CadavreGUID" not in edits:
            continue

        unit_name = edits["NewName"]

        # Clone the donor's cadavre descriptor
        donor_cadavre = source_path.by_namespace(f"Descriptor_UnitCadavre_{donor_name}")
        if not donor_cadavre:
            logger.warning(f"Donor cadavre descriptor for {donor_name} not found")
            continue

        new_cadavre = donor_cadavre.copy()

        # Update basic properties
        new_cadavre.namespace = f"Descriptor_UnitCadavre_{unit_name}"
        new_cadavre.v.by_member("DescriptorId").v = f"GUID:{{{edits['CadavreGUID']}}}"
        new_cadavre.v.by_member("ClassNameForDebug").v = f"'Unit_Cadavre{unit_name}'"

        # Get modules list
        modules_list = new_cadavre.v.by_m("ModulesDescriptors")

        # First pass - update unit references and find cadavre module
        cadavre_modules = None
        modules_to_remove = []

        for module in modules_list.v:
            if isinstance(module.v, str) and "~/Descriptor_Unit_" in module.v:
                # Mark modules for removal if they match the remove list
                if (
                    "depictions" in edits
                    and "cadavre" in edits["depictions"]
                    and "remove_modules" in edits["depictions"]["cadavre"]
                ):
                    module_name = module.v.split("/")[-1]
                    if module_name in edits["depictions"]["cadavre"]["remove_modules"]:
                        modules_to_remove.append(module)
                        continue

                # Update unit reference
                old_path = f"~/Descriptor_Unit_{donor_name}"
                new_path = f"~/Descriptor_Unit_{unit_name}"
                module.v = module.v.replace(old_path, new_path)

            elif isinstance(module.v, ndf.model.Object):
                if module.v.type == "TTypeUnitModuleDescriptor" and "TypeUnit" in edits:
                    for member, value in edits["TypeUnit"].items():
                        module.v.by_member(member).v = value

                elif module.v.type == "UnitCadavreModuleDescriptor":
                    cadavre_modules = module.v.by_m("ModuleDescriptorsToSteal")

        # Remove marked modules
        for module in modules_to_remove:
            modules_list.v.remove(module)
            logger.info(f"Removed module {module.v} from {unit_name}")

        # Update references in cadavre module and remove unwanted modules
        if cadavre_modules:
            modules_to_remove = []
            for module in cadavre_modules.v:
                if isinstance(module.v, str):
                    if "~/Descriptor_Unit_" in module.v:
                        # Check if module should be removed
                        if (
                            "depictions" in edits
                            and "cadavre" in edits["depictions"]
                            and "remove_modules" in edits["depictions"]["cadavre"]
                        ):
                            module_name = module.v.split("/")[-1]
                            if module_name in edits["depictions"]["cadavre"]["remove_modules"]:
                                modules_to_remove.append(module)
                                continue

                        # Update unit reference
                        old_path = f"~/Descriptor_Unit_{donor_name}"
                        new_path = f"~/Descriptor_Unit_{unit_name}"
                        module.v = module.v.replace(old_path, new_path)

            # Remove marked modules from ModuleDescriptorsToSteal
            for module in modules_to_remove:
                cadavre_modules.v.remove(module)
                logger.info(f"Removed module {module.v} from {unit_name} ModuleDescriptorsToSteal")

        # Add the new cadavre descriptor
        source_path.add(new_cadavre)
        logger.info(f"Added cadavre descriptor for {unit_name}")


def create_mimetic_depictions(source_path: Any) -> None:
    """Create mimetic depiction entries in MimeticDescriptor.ndf."""
    logger.info("Creating mimetic depiction entries")

    for donor, edits in NEW_UNITS.items():
        if "NewName" not in edits or not edits.get("is_infantry", False):
            continue

        unit_name = edits["NewName"]

        # Create mimetic descriptor
        entry = (
            f"export Descriptor_Mimetic_{unit_name} is TMimeticDescriptor\n"
            f"(\n"
            f"    MimeticName = '{unit_name}'\n"
            f"    DescriptorId = GUID:{{{edits['GroupeCombatGUID']}}}\n"
            f"    IdleAnimation = $/GFX/DepictionResources/Anim_{unit_name}_idle\n"
            f"    MovementAnimation = $/GFX/DepictionResources/Anim_{unit_name}_move\n"
            f"    DeathAnimation = $/GFX/DepictionResources/Anim_{unit_name}_death\n"
            f")\n"
        )
        source_path.add(entry)
        logger.info(f"Added mimetic depiction for {unit_name}")


def create_ghost_depictions(source_path: Any) -> None:
    """Create ghost depiction entries in DepictionGhosts.ndf."""
    logger.info("Creating ghost depiction entries")

    for donor, edits in NEW_UNITS.items():
        if not edits.get("is_ground_vehicle", False):
            continue

        unit_name = edits["NewName"]

        # Create ghost depiction entry
        entry = (
            f"GhostDepiction_{unit_name} is GhostVehicleDepictionDesc"
            f"("
            f"    Alternatives = Alternatives_{unit_name}"
            f"    Selector = SpecificVehicleDepictionSelector"
            f")"
        )
        source_path.add(entry)
        logger.info(f"Added ghost depiction for {unit_name}")


def create_alternatives_depictions(source_path: Any) -> None:
    """Create alternatives depiction entries in DepictionAlternatives.ndf."""
    logger.info("Creating alternatives depiction entries")

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if not edits.get("is_ground_vehicle", False):
            continue

        unit_name = edits["NewName"]

        # Create alternatives entry using donor's models
        entry = (
            f"Alternatives_{unit_name} is ["
            f"    DepictionDescriptor_LOD_High( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor_name} ),"
            f"    DepictionDescriptor_LOD_Mid( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor_name}_MID ),"
            f"    DepictionDescriptor_LOD_Low( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor_name}_LOW ),"
            f"]"
        )
        source_path.add(entry)
        logger.info(f"Added alternatives depiction for {unit_name}")


def create_veh_human_depictions(source_path: Any) -> None:
    """Create human depiction entries for vehicles in DepictionHumans.ndf."""
    logger.info("Creating human depiction entries for vehicles")

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if not (edits.get("is_ground_vehicle", False) and edits.get("is_infantry", False)):
            logger.info(f"Skipping {donor_name} because it's not a vehicle or infantry")
            continue

        unit_name = edits["NewName"]

        # Find donor mesh names
        mesh_names = None
        if "servants" in edits:
            mesh_names = edits["servants"]
        else:
            for row in source_path:
                if row.namespace != f"HumanSubDepictions_{donor_name}":
                    continue

                left_servant = row.v[0]
                right_servant = row.v[1]

                left_mesh = left_servant.v.by_m("MeshDescriptorHigh").v.split(
                    "$/GFX/DepictionResources/MeshDescriptor_Servant_"
                )[-1]
                right_mesh = right_servant.v.by_m("MeshDescriptorHigh").v.split(
                    "$/GFX/DepictionResources/MeshDescriptor_Servant_"
                )[-1]

                mesh_names = (left_mesh, right_mesh)
                break

        if not mesh_names:
            logger.warning(f"Could not find mesh names for {donor_name}")
            continue

        left_mesh, right_mesh = mesh_names

        if edits.get("is_heavy_equipment", False):
            # Create heavy equipment human depiction entries
            human_depiction = (
                f"HumanSubDepictions_{unit_name} is "
                f"["
                f"    SubDepiction_ServantWalkOnlyLeft"
                f"    ("
                f"        MeshDescriptorHigh = $/GFX/DepictionResources/MeshDescriptor_Servant_{left_mesh}"
                f"        MeshDescriptorLow = $/GFX/DepictionResources/MeshDescriptor_Servant_{left_mesh}_LOW"
                f"    ),"
                f"    SubDepiction_GunnerIdleOnlyLeft"
                f"    ("
                f"        MeshDescriptorHigh = $/GFX/DepictionResources/MeshDescriptor_Servant_{left_mesh}"
                f"        MeshDescriptorLow = $/GFX/DepictionResources/MeshDescriptor_Servant_{left_mesh}_LOW"
                f"    ),"
                f"    SubDepiction_ServantRight"
                f"    ("
                f"        MeshDescriptorHigh = $/GFX/DepictionResources/MeshDescriptor_Servant_{right_mesh}"
                f"        MeshDescriptorLow = $/GFX/DepictionResources/MeshDescriptor_Servant_{right_mesh}_LOW"
                f"    )"
                f"]"
            )
            showroom_depiction = (
                f"HumanSubDepictionsShowroom_{unit_name} is"
                f"["
                f"    ShowroomSubDepiction_GunnerLeft"
                f"    ("
                f"        MeshDescriptor = $/GFX/DepictionResources/MeshDescriptor_Servant_{left_mesh}"
                f"    ),"
                f"    ShowroomSubDepiction_ServantRight"
                f"    ("
                f"        MeshDescriptor = $/GFX/DepictionResources/MeshDescriptor_Servant_{right_mesh}"
                f"    )"
                f"]"
            )
        else:
            # Create human depiction entries
            human_depiction = (
                f"HumanSubDepictions_{unit_name} is\n"
                f"[\n"
                f"    SubDepiction_ATGMServantLeft\n"
                f"    (\n"
                f"        MeshDescriptorHigh = $/GFX/DepictionResources/MeshDescriptor_Servant_{left_mesh}\n"
                f"        MeshDescriptorLow = $/GFX/DepictionResources/MeshDescriptor_Servant_{left_mesh}_LOW\n"
                f"    ),\n"
                f"    SubDepiction_ATGMServantRight\n"
                f"    (\n"
                f"        MeshDescriptorHigh = $/GFX/DepictionResources/MeshDescriptor_Servant_{right_mesh}\n"
                f"        MeshDescriptorLow = $/GFX/DepictionResources/MeshDescriptor_Servant_{right_mesh}_LOW\n"
                f"    )\n"
                f"]\n"
            )

            showroom_depiction = (
                f"HumanSubDepictionsShowroom_{unit_name} is\n"
                f"[\n"
                f"    ShowroomSubDepiction_ATGMServantLeft\n"
                f"    (\n"
                f"        MeshDescriptor = $/GFX/DepictionResources/MeshDescriptor_Servant_{left_mesh}\n"
                f"    ),\n"
                f"    ShowroomSubDepiction_ATGMServantRight\n"
                f"    (\n"
                f"        MeshDescriptor = $/GFX/DepictionResources/MeshDescriptor_Servant_{right_mesh}\n"
                f"    )\n"
                f"]\n"
            )

        # Find insertion point and add entries
        for row in source_path:
            if not is_obj_type(row.v, "TTransportedInfantryCatalogEntries"):
                continue

            source_path.insert(row.index, showroom_depiction)
            source_path.insert(row.index, human_depiction)
            logger.info(f"Added human depictions for {unit_name}")

            # Add catalog entry
            catalog_entry = (
                f"TTransportedInfantryEntry\n"
                f"(\n"
                f'    Count = {edits["alternatives_count"]}\n'
                f'    Identifier = "{unit_name}"\n'
                f"    Meshes =\n"
                f"    [\n"
                f"        $/GFX/DepictionResources/MeshDescriptor_Servant_{left_mesh},\n"
                f"        $/GFX/DepictionResources/MeshDescriptor_Servant_{right_mesh}\n"
                f"    ]\n"
                f'    UniqueCount = {edits["alternatives_count"]}\n'
                f")\n"
            )

            row.v.by_m("Entries").v.add(catalog_entry)
            logger.info(f"Added catalog entry for {unit_name}")
            break


def create_veh_depictions(source_path: Any) -> None:
    """Create vehicle depiction entries in DepictionVehicles.ndf."""
    logger.info("Creating vehicle depiction entries")

    def get_base_namespace(namespace_: str, prefix: str) -> str:
        """Extract the base namespace after the given prefix."""
        if namespace_.startswith("Gfx"):
            return namespace_.split(f"{prefix}_")[-1]
        elif namespace_.startswith("DepictionOperator"):
            parts = namespace_.split(f"{prefix}_")[-1].rsplit("_", 1)[0]
            return parts  # Return parts directly

    def create_new_object(
        obj_row_: Any, unit_name_: str, is_weapon: bool, weapon_num: int = 0, edits: dict = None
    ) -> Any:
        """Create a new depiction object with updated namespace."""
        new_obj = obj_row_.copy()
        if is_weapon:
            new_obj.namespace = f"DepictionOperator_{unit_name_}_Weapon{weapon_num}"
        else:
            new_obj.namespace = f"Gfx_{unit_name_}"
            depiction_veh_edits = edits.get("depictions", {}).get("remove", {}).get("DepictionVehicles_ndf", {})
            if "remove_members" in depiction_veh_edits:
                for member in depiction_veh_edits["remove_members"]:
                    new_obj.v.remove_by_member(member)
        return new_obj

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
            # Add TacticVehicleDepictionTemplate if present
            if "TacticVehicleDepictionTemplate" in custom_depictions:
                custom_veh_added = True
                custom_veh_depiction = NEW_DEPICTIONS[depiction_key]["DepictionVehicles_ndf"][
                    "TacticVehicleDepictionTemplate"
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
                "TacticVehicleDepictionTemplate" in custom_depictions
                or "DepictionOperator_WeaponContinuousFire" in custom_depictions
            ):
                logger.warning(f"No custom depiction found for {unit_name} (key: {depiction_key})")

        # Handle default depictions if no customs were added
        if not custom_veh_added or not custom_operator_added:
            weapon_count = 0
            new_objects = []

            for obj_row in source_path:
                namespace = obj_row.namespace

                if "DepictionOperator_" in namespace and not custom_operator_added:
                    base_namespace = get_base_namespace(namespace, "DepictionOperator")
                    if donor_name == base_namespace:
                        weapon_count += 1
                        new_objects.append(create_new_object(obj_row, unit_name, True, weapon_count, edits))

                elif "Gfx_" in namespace and not custom_veh_added:
                    base_namespace = get_base_namespace(namespace, "Gfx")
                    if donor_name == base_namespace:
                        new_objects.append(create_new_object(obj_row, unit_name, False, weapon_count, edits))

            for obj in new_objects:
                logger.info(f"Adding new object to DepictionVehicles.ndf: {obj.namespace}")
                source_path.add(obj)


def create_aerial_ghost_depictions(source_path: Any) -> None:
    """Create aerial ghost depiction entries in DepictionAerialGhosts.ndf."""
    logger.info("Creating aerial ghost depiction entries")

    for donor, edits in NEW_UNITS.items():
        if edits.get("is_aerial", False):
            unit_name = edits["NewName"]
            new_object_entry = (
                f"GhostDepiction_{unit_name} is GhostAerialDepictionDesc\n"
                f"(\n"
                f"    Alternatives = Alternatives_{unit_name}\n"
                f"    Selector = SpecificAirplaneDepictionSelector\n"
                f")"
            )
            source_path.add(new_object_entry)
            logger.info(f"Added aerial ghost depiction for {unit_name}")


def create_veh_showroom_depictions(source_path: Any) -> None:
    """Create vehicle showroom depiction entries in DepictionVehiclesShowRoom.ndf."""
    logger.info("Creating vehicle showroom depiction entries")

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if edits.get("is_ground_vehicle", False):
            unit_name = edits["NewName"]
            new_depiction_obj = source_path.by_namespace(f"Gfx_{donor_name}_Showroom").copy()
            new_depiction_obj.namespace = f"Gfx_{unit_name}_Showroom"
            new_depiction_obj.v.by_member("Alternatives").v = f"Alternatives_{unit_name}"
            # new_depiction_obj.v.by_member("Selector").v = f"Selector_{unit_name}"

            if edits.get("is_infantry", False):
                new_depiction_obj.v.by_member("SubDepictions").v = f"HumanSubDepictionsShowroom_{unit_name}"

            source_path.add(new_depiction_obj)
            logger.info(f"Added vehicle showroom depiction for {unit_name}")
