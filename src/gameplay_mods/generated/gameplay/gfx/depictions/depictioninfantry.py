"""Functions for modifying DepictionInfantry.ndf"""

from typing import Any, Dict

from src import ndf
from src.constants.new_units import NEW_DEPICTIONS, NEW_UNITS
from src.constants.unit_edits import load_depiction_edits, load_unit_edits
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type, strip_quotes

logger = setup_logger(__name__)


def edit_gen_gp_gfx_depictioninfantry(source_path: Any, game_db: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionInfantry.ndf"""
    
    # TODO: Hastily written (albeit functional) code that needs rewriting and refactoring
    _handle_new_units(source_path, game_db)
    _handle_unit_edits(source_path, game_db)
    _handle_complex_unit_edits(source_path)
    
def _handle_new_units(source_path: Any, game_db: Any) -> None:
    """Handle new units for DepictionInfantry.ndf"""
    
    depiction_db = game_db["depiction_data"]
    
    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if not edits.get("is_infantry", False) or edits.get("is_ground_vehicle", False):
            continue

        unit_name = edits["NewName"]
        depiction_key = unit_name.lower()

        # Clone all required objects

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
                    weaponalternatives_obj.v = depiction_edits
                    
                    # rows_to_insert = []
                    # for row_index, (edit_type, edit_list) in depiction_edits.items():
                    #     if edit_type == "edit":
                    #         for member, value in edit_list:
                    #             if member == "SelectorId":
                    #                 weaponalternatives_obj.v[row_index].v.by_m(member).v = f"['{value}']"
                    #             if member == "MeshDescriptor" or member == "ReferenceMeshForSkeleton":
                    #                 new_mesh = f"$/GFX/DepictionResources/Modele_{value}"
                    #                 weaponalternatives_obj.v[row_index].v.by_m(member).v = new_mesh
                    #                 logger.info(f"Changed {member} for {unit_name} to {new_mesh}")
                    #     elif edit_type == "add":
                    #         for member, value in edit_list:
                    #             if member == "SelectorId":
                    #                 selector_id = "['" + f"{value}" + "']"
                    #             elif member == "MeshDescriptor":
                    #                 mesh_member = "MeshDescriptor"
                    #                 mesh_descriptor = f"$/GFX/DepictionResources/Modele_{value}"
                    #             elif member == "ReferenceMeshForSkeleton":
                    #                 mesh_member = "ReferenceMeshForSkeleton"
                    #                 mesh_descriptor = f"$/GFX/DepictionResources/Modele_{value}"
                    #         new_entry = (
                    #             f"TDepictionVisual"
                    #             f"("
                    #             f"    SelectorId = {selector_id}"
                    #             f"    {mesh_member} = {mesh_descriptor}"
                    #             f")"
                    #         )
                    #         weaponalternatives_obj.v.insert(row_index, new_entry)
                    #     elif edit_type == "insert":
                    #         for member, value in edit_list:
                    #             if member == "SelectorId":
                    #                 selector_id = "['" + f"{value}" + "']"
                    #             elif member == "MeshDescriptor":
                    #                 mesh_member = "MeshDescriptor"
                    #                 mesh_descriptor = f"$/GFX/DepictionResources/Modele_{value}"
                    #             elif member == "ReferenceMeshForSkeleton":
                    #                 mesh_member = "ReferenceMeshForSkeleton"
                    #                 mesh_descriptor = f"$/GFX/DepictionResources/Modele_{value}"
                    #         new_entry = (
                    #             f"TDepictionVisual"
                    #             f"("
                    #             f"    SelectorId = {selector_id}"
                    #             f"    {mesh_member} = {mesh_descriptor}"
                    #             f")"
                    #         )
                    #         rows_to_insert.append((row_index, new_entry))
                    # for row_index, new_entry in reversed(rows_to_insert):
                    #     weaponalternatives_obj.v.insert(row_index, new_entry)

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
                    operator_edits = depiction_edits.get("Operators", {})
                    operators.v = operator_edits
                    
                    # rows_to_remove = []
                    # rows_to_insert = []
                    # operator_edits = depiction_edits.get("Operators", {})
                    # for operator_index, (edit_type, edit_list) in operator_edits.items():
                    #     if edit_type == "edit":
                    #         for member, value in edit_list:
                    #             if member == "FireEffectTag":
                    #                 operator = operators.v[operator_index]
                    #                 operator.v.by_m(member).v = f'"FireEffect_{value}"'
                    #     elif edit_type == "remove":
                    #         rows_to_remove.append(operator_index)
                    #     elif edit_type == "add":
                    #         for member, value in edit_list:
                    #             if member == "FireEffectTag":
                    #                 effect_tag = f'"FireEffect_{value}"'
                    #             elif member == "WeaponShootDataPropertyName":
                    #                 shoot_data_property = f'"WeaponShootData_{value}"'
                    #         new_entry = (
                    #             f"DepictionOperator_WeaponInstantFireInfantry"
                    #             f"("
                    #             f"    FireEffectTag = {effect_tag}"
                    #             f"    WeaponShootDataPropertyName = {shoot_data_property}"
                    #             f")"
                    #         )
                    #         operators.v.insert(operator_index, new_entry)
                    # for row_index in reversed(rows_to_remove):
                    #     operators.v.remove(row_index)

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
                    depictionalternatives_list.v = depiction_edits
                    
                    # rows_to_remove = []
                    # for row_index, (edit_type, edit_list) in depiction_edits.items():
                    #     if edit_type == "edit":
                    #         for member, value in edit_list:
                    #             if member == "MeshDescriptor" or member == "ReferenceMeshForSkeleton":
                    #                 new_mesh = f"$/GFX/DepictionResources/Modele_{value}"
                    #                 depictionalternatives_list.v[row_index].v.by_m(member).v = new_mesh
                    #                 logger.info(f"Changed {member} for {unit_name} to {new_mesh}")
                    #     elif edit_type == "remove":
                    #         rows_to_remove.append(row_index)
                    # for row_index in reversed(rows_to_remove):
                    #     depictionalternatives_list.v.remove(row_index)

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
                model_name = donor_name if not edits.get("model", False) else edits["model"]
                new_mesh_list = [f"$/GFX/DepictionResources/Modele_{model_name}"]
                for i in range(2, edits.get("alternatives_count", 1) + 1):
                    new_mesh_list.append(f"$/GFX/DepictionResources/Modele_{model_name}_{i:02}")

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
            
def _handle_complex_unit_edits(source_path: Any) -> None:
    """Edit unit depictions in DepictionInfantry.ndf"""
    ndf_file = "DepictionInfantry.ndf"

    # Load all depiction edits
    depiction_edits = load_depiction_edits()

    # Process each unit's edits
    for unit_name, unit_data in depiction_edits.items():
        # Skip if this file isn't relevant for this unit
        if ndf_file not in unit_data["valid_files"]:
            continue

        if "DepictionInfantry_ndf" not in unit_data:
            logger.error(f"{ndf_file} is valid for {unit_name} but no edits found")
            continue

        unit_edits = unit_data["DepictionInfantry_ndf"]
        logger.debug(f"Processing infantry edits for {unit_name}")
        logger.debug(f"  Found {len(unit_edits)} edit groups for {unit_name}")

        for (namespace, obj_type), edits in unit_edits.items():
            logger.debug(f"  Processing namespace: {namespace}, obj_type: {obj_type}")
            if namespace and namespace.startswith("AllWeaponAlternatives_"):
                weapon_alternatives = source_path.by_n(namespace)
                if not weapon_alternatives:
                    logger.error(f"Could not find weapon alternatives {namespace} for {unit_name}")
                    continue

                for row_index, (edit_type, edit_list) in edits.items():
                    if edit_type == "edit":
                        for member, value in edit_list:
                            if member == "SelectorId":
                                weapon_alternatives.v[row_index].v.by_m(member).v = f"['{value}']"
                                logger.info(f"Changed SelectorId for {unit_name} to {value}")
                            elif member == "MeshDescriptor" or member == "ReferenceMeshForSkeleton":
                                new_mesh = f"$/GFX/DepictionResources/Modele_{value}"
                                weapon_alternatives.v[row_index].v.by_m(member).v = new_mesh
                                logger.info(f"Changed {member} for {unit_name} to {new_mesh}")
                    elif edit_type == "insert":
                        selector_id = None
                        new_mesh = None
                        for member, value in edit_list:
                            if member == "SelectorId":
                                selector_id = f"['{value}']"
                            elif member == "MeshDescriptor" or member == "ReferenceMeshForSkeleton":
                                new_mesh = f"$/GFX/DepictionResources/Modele_{value}"
                        if selector_id and new_mesh:
                            new_entry = (
                                f"TDepictionVisual"
                                f"("
                                f"    SelectorId = {selector_id}"
                                f"    MeshDescriptor = {new_mesh}"
                                f")"
                            )
                            weapon_alternatives.v.insert(row_index, new_entry)
                            logger.info(f"Inserted {member} for {unit_name} at index {row_index}")
                        else:
                            logger.error(f"Could not insert {member} for {unit_name} at index {row_index}")

            elif namespace and namespace.startswith("AllWeaponSubDepiction_"):
                weapon_subdepictions = source_path.by_n(namespace)
                if not weapon_subdepictions:
                    logger.error(f"Could not find weapon subdepictions {namespace} for {unit_name}")
                    continue

                for member, member_edits in edits.items():
                    if member == "Operators":
                        operators_member = weapon_subdepictions.v.by_m(member)
                        for index, (edit_type, edit_list) in member_edits.items():
                            
                            if edit_type == "edit":
                                for submember, value in edit_list:
                                    if submember == "FireEffectTag":
                                        # Remove quotes if present
                                        value = value.strip('"').strip("'")
                                        new_value = f'"FireEffect_{value}"'
                                        operators_member.v[index].v.by_m(submember).v = new_value
                                    elif submember == "WeaponShootDataPropertyName":
                                        operators_member.v[index].v.by_m(submember).v = '"' + value + '"'
                            
                            elif edit_type == "insert":
                                effect_tag = None
                                shoot_property = None
                                for submember, value in edit_list:
                                    if submember == "FireEffectTag":
                                        # Remove quotes if present
                                        value = value.strip('"').strip("'")
                                        effect_tag = f'"FireEffect_{value}"'
                                    elif submember == "WeaponShootDataPropertyName":
                                        shoot_property = f'"{value}"'
                                if effect_tag and shoot_property:
                                    new_entry = (
                                        f"DepictionOperator_WeaponInstantFireInfantry"
                                        f"("
                                        f"    FireEffectTag = {effect_tag}"
                                        f"    WeaponShootDataPropertyName = {shoot_property}"
                                        f")"
                                    )
                                    operators_member.v.insert(index, new_entry)
            
            elif namespace and namespace.startswith("TacticDepiction_") and namespace.endswith("_Alternatives"):
                tacticdepiction_alternatives = source_path.by_n(namespace)
                if not tacticdepiction_alternatives:
                    logger.error(f"Unit Edits: Could not find tactic depiction {namespace} for {unit_name}")
                    continue
                    
                tacticdepiction_alternatives.v = edits

            elif namespace and namespace.startswith("TacticDepiction_") and namespace.endswith("_Soldier"):
                logger.debug(f"  Found TacticDepiction_*_Soldier match for {namespace}")
                tacticdepiction_soldier = source_path.by_n(namespace)
                if not tacticdepiction_soldier:
                    logger.error(f"Could not find tactic depiction {namespace} for {unit_name}")
                    continue
                logger.debug(f"  Found tactic depiction object for {namespace}")

                for member, member_edits in edits.items():
                    if member == "Selector":
                        
                        # check if appropriate InfantrySelectorTactic exists, else create it
                        template_infantry_selector_tactic = source_path.by_n(f"InfantrySelectorTactic_{member_edits}", False)
                        if not template_infantry_selector_tactic:
                            # member_edits = "{new_count}_{new_unique_count}"
                            new_unique_count = f"{int(member_edits.split('_')[0]):02d}"
                            new_count = int(member_edits.split("_")[1])
                            new_template = (
                                f"InfantrySelectorTactic_{member_edits} is TemplateInfantrySelectorTactic"
                                f"("
                                f"    Surrogates = TacticDepiction_{new_unique_count}_Surrogates"
                                f"    UniqueCount = {new_count}"
                                f")"
                            )
                            source_path.add(new_template)
                        
                        # update selector tactic
                        tacticdepiction_soldier.v.by_m(member).v = f"InfantrySelectorTactic_{member_edits}"
                        
                    if member == "Operators":
                        operators_member = tacticdepiction_soldier.v.by_m(member)
                        
                        # Find the DepictionOperator_SkeletalAnimation2_Default operator
                        skeletal_animation_operator = None
                        for obj in operators_member.v:
                            if is_obj_type(obj.v, "DepictionOperator_SkeletalAnimation2_Default"):
                                skeletal_animation_operator = obj.v
                                break
                        
                        if skeletal_animation_operator is None:
                            logger.error(f"Could not find DepictionOperator_SkeletalAnimation2_Default in Operators for {namespace}")
                            continue
                        
                        # Need to check if ConditionalTags member exists, else create it
                        conditional_tags = skeletal_animation_operator.by_m("ConditionalTags", False)
                        if conditional_tags is None:
                            logger.debug(f"Creating ConditionalTags for {namespace}")
                            skeletal_animation_operator.add("ConditionalTags = []")
                            conditional_tags = skeletal_animation_operator.by_m("ConditionalTags")
                        
                        logger.debug(f"  Processing {len(member_edits)} operator edits for {namespace}")
                        for index, (edit_type, edit_list) in member_edits.items():
                            logger.debug(f"    Edit at ConditionalTags index {index}: type={edit_type}, list={edit_list}")
                            if edit_type == "edit":
                                # Index refers to the position in ConditionalTags list
                                if index < len(conditional_tags.v):
                                    for new_tag, mesh_alternative in edit_list:
                                        tag_tuple = conditional_tags.v[index]
                                        tag_tuple.v = f"('{new_tag}', '{mesh_alternative}')"
                                        logger.info(
                                            f"Updated ConditionalTags[{index}] to ('{new_tag}', '{mesh_alternative}') for {unit_name}"
                                        )
                                else:
                                    logger.warning(
                                        f"Index {index} out of range for ConditionalTags (length {len(conditional_tags.v)}) "
                                        f"for {unit_name}. Edit operation skipped."
                                    )
                            elif edit_type == "insert":
                                logger.debug(f"    Processing insert operation at ConditionalTags index {index}")
                                for new_tag, mesh_alternative in edit_list:
                                    new_entry = (
                                        f"('{new_tag}', '{mesh_alternative}')"
                                    )
                                    conditional_tags.v.insert(index, new_entry)
                                    logger.info(f"Inserted tag {new_tag} for mesh {mesh_alternative} at ConditionalTags index {index} for {unit_name}")
                            else:
                                logger.warning(f"    Unknown edit_type '{edit_type}' for {unit_name} at index {index}")
                                            
            elif namespace and namespace.startswith("TacticDepiction_") and namespace.endswith("_Ghost"):
                tacticdepiction_ghost = source_path.by_n(namespace)
                if not tacticdepiction_ghost:
                    logger.error(f"Unit Edits: Could not find tactic depiction {namespace} for {unit_name}")
                    continue
                    
                for member, member_edits in edits.items():
                    if member == "Selector":
                        tacticdepiction_ghost.v.by_m(member).v = f"InfantrySelectorTactic_{member_edits}"
                        
            elif obj_type == "TTransportedInfantryEntry":
                transport_catalog = source_path.find_by_cond(
                    lambda x: is_obj_type(x.v, "TTransportedInfantryCatalogEntries"))
                if not transport_catalog:
                    logger.error(f"Unit Edits: Could not find transport catalog")
                    continue
                
                catalog_entries = transport_catalog.v.by_member("Entries").v
                    
                transportedinfantryentry = catalog_entries.find_by_cond(
                    lambda x: x.v.by_member("Identifier").v == f'"{unit_name}"')
                if not transportedinfantryentry:
                    logger.error(f"Unit Edits: Could not find transported infantry entry {unit_name}")
                    continue
                    
                for member, member_edits in edits.items():
                    if member == "Count":
                        transportedinfantryentry.v.by_m(member).v = str(member_edits)
                    elif member == "Meshes":
                        new_mesh_list = []
                        for mesh in member_edits:
                            new_mesh_list.append(f"$/GFX/DepictionResources/Modele_{mesh}")
                        new_meshes = ndf.model.List()
                        for mesh in new_mesh_list:
                            new_meshes.add(mesh)
                        transportedinfantryentry.v.by_member("Meshes").v = new_meshes
                    elif member == "UniqueCount":
                        transportedinfantryentry.v.by_member("UniqueCount").v = str(member_edits)
                    else:
                        logger.error(f"Unit Edits: Unknown member {member} for {unit_name}")
                                            
def _handle_unit_edits(source_path: Any, game_db: Dict[str, Any]) -> None:
    # this function is so limited and could easily break if the unit edits are not formatted correctly
    """Edit DepictionInfantry.ndf.
    
    Args:
        source_path: NDF file containing infantry depictions
        game_db: Game database
    """
    logger.info("Editing DepictionInfantry.ndf")
    
    unit_edits = load_unit_edits()
    ammo_db = game_db["ammunition"]
    depiction_data = game_db["depiction_data"]
    
    for unit_name, edits in unit_edits.items():
        if "WeaponDescriptor" not in edits:
            continue
        
        if "replace" in edits["WeaponDescriptor"].get("equipmentchanges", {}):
            weapon_replacements = edits["WeaponDescriptor"].get("equipmentchanges", {}).get("replace", [])
            for replacement in weapon_replacements:
                if len(replacement) == 4:
                    old_fire_effect = replacement[2]
                    new_fire_effect = replacement[3]
                    
                    # AllWeaponSubDepiction
                    weapon_subdepictions = source_path.find_by_cond(
                        lambda x: x.namespace == f"AllWeaponSubDepiction_{unit_name}", False)
                    if not weapon_subdepictions:
                        logger.debug(f"No infantry weapon subdepictions found for {unit_name}")
                        continue
                    operators_list = weapon_subdepictions.v.by_m("Operators").v
                    target_operator = operators_list.find_by_cond(
                        lambda x: x.v.by_m("FireEffectTag").v == f'"FireEffect_{old_fire_effect}"')
                    if target_operator:
                        target_operator.v.by_m("FireEffectTag").v = f'"FireEffect_{new_fire_effect}"'
                        logger.info(f"Replaced fire effect {old_fire_effect} with {new_fire_effect} for {unit_name}")
            
        weapon_changes = edits["WeaponDescriptor"].get("equipmentchanges", {})
        
        # Old depiction edit code
        if "add" in weapon_changes:
            
            
            # Get weapon info (salvo_index, weapon_name), e.g:
            # "add": [
            #     (2, "MMG_inf_M240B_7_62mm"),
            #     (3, "RocketInf_M72A3_LAW_66mm"),
            # ]
            # todo: handle multiple changes for a single unit (example dosn't work right now xD trolololol)
            turret_index = weapon_changes["add"][0][0] # [change_1][salvo_index] turret index?? not sure trololol
            weapon_name = weapon_changes["add"][0][1] # [change_1][weapon_name]
            
            # Get depiction data for weapon
            if weapon_name in ammo_db["renames_new_old"]:
                old_name = ammo_db["renames_new_old"][weapon_name] 
                if old_name in depiction_data["animation_weapon_map"]:
                    weapon_data = {
                        "weapon_alt_mesh": depiction_data["all_weapon_meshes"][old_name],
                        "fire_effect": depiction_data["all_fire_effects"][old_name],
                        "animation_tag": depiction_data["animation_weapon_map"].get(old_name, None)
                    }
                else:
                    weapon_data = {}
                    logger.warning(f"No animation tag found for {old_name}")
            else:
                weapon_data = {
                    "weapon_alt_mesh": depiction_data["all_weapon_meshes"][weapon_name],
                    "fire_effect": depiction_data["all_fire_effects"][weapon_name],
                    "animation_tag": depiction_data["animation_weapon_map"].get(weapon_name, None)
                }
            
            try:
                # Add weapon mesh alternative
                _add_weapon_mesh(source_path, unit_name, turret_index, weapon_data["weapon_alt_mesh"])
                
                # Add weapon fire effect
                _add_fire_effect(source_path, unit_name, turret_index, weapon_data["fire_effect"])
                
                # Add conditional animation tag if it exists
                if "animation_tag" in weapon_data and weapon_data["animation_tag"] is not None:
                    _add_animation_tag(source_path, unit_name, turret_index, weapon_data["animation_tag"])
                
            except Exception as e:
                logger.error(f"Failed to edit depictions for {unit_name}: {str(e)}")


def _add_weapon_mesh(source_path: Any, unit_name: str, turret_index: int, mesh: str) -> None:
    """Add weapon mesh alternative to unit."""
    try:
        weapon_alts = source_path.by_n(f"AllWeaponAlternatives_{unit_name}").v
        new_entry = (
            f"TDepictionVisual("
            f"    SelectorId = ['WeaponAlternative_{turret_index + 1}']"
            f"    MeshDescriptor = $/GFX/DepictionResources/Modele_{mesh}"
            f")"
        )
        
        for i, obj in enumerate(weapon_alts):
            if is_obj_type(obj.v, "TMeshlessDepictionDescriptor"):
                weapon_alts.insert(i, new_entry)
                obj.v.by_m("ReferenceMeshForSkeleton").v = f"$/GFX/DepictionResources/Modele_{mesh}"
                logger.info(f"Added mesh alternative {mesh} to {unit_name}")
                break
                
    except Exception as e:
        logger.error(f"Failed to add weapon mesh for {unit_name}: {str(e)}")


def _add_fire_effect(source_path: Any, unit_name: str, turret_index: int, fire_effect: str) -> None:
    """Add weapon fire effect to unit."""
    try:
        weapon_subdepictions = source_path.by_n(f"AllWeaponSubDepiction_{unit_name}").v
        operators_list = weapon_subdepictions.by_m("Operators").v
        
        new_entry = (
            f'DepictionOperator_WeaponInstantFireInfantry('
            f'    FireEffectTag = "{fire_effect}"'
            f'    WeaponShootDataPropertyName = "WeaponShootData_0_{turret_index + 1}"'
            f')'
        )
        operators_list.add(new_entry)
        logger.info(f"Added fire effect for {unit_name} turret {turret_index}")
        
    except Exception as e:
        logger.error(f"Failed to add fire effect for {unit_name}: {str(e)}")


def _add_animation_tag(source_path: Any, unit_name: str, turret_index: int, tag: str) -> None:
    """Add conditional animation tag to unit."""
    try:
        soldier_depiction = source_path.by_n(f"TacticDepiction_{unit_name}_Soldier").v
        operators_list = soldier_depiction.by_m("Operators").v
        
        for obj in operators_list:
            if is_obj_type(obj.v, "DepictionOperator_SkeletalAnimation2_Default"):
                # Check if ConditionalTags exists
                if obj.v.by_m("ConditionalTags", False) is not None:
                    conditional_tags = obj.v.by_m("ConditionalTags")
                else:
                    # Create ConditionalTags if it doesn't exist using ndf.convert
                    obj.v.add(ndf.convert("ConditionalTags = []"))
                    conditional_tags = obj.v.by_m("ConditionalTags")
                
                # Add the new tag
                conditional_tags.v.add(
                    f"('{tag}', 'WeaponAlternative_{turret_index + 1}')"
                )
                logger.info(f"Added animation tag for {unit_name} turret {turret_index}")
                break
                
    except Exception as e:
        logger.error(f"Failed to add animation tag for {unit_name}: {str(e)}")