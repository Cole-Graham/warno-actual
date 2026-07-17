"""Functions for modifying DepictionInfantry.ndf"""

import re
from typing import Any

from src import ndf
from src.constants.new_units import NEW_DEPICTIONS, NEW_UNITS
from src.constants.unit_edits import load_depiction_edits
from src.constants.unit_edits.depiction_edits.selector_tactic import (
    NEW_SELECTOR_TACTIC_OBJECTS,
)
from src.gameplay_mods.generated.gameplay.gfx.depictions._apply import (
    apply_infantry_section,
    overwrite_skeleton_conditional_tags,
)
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

_NDF_FILE = "DepictionInfantry.ndf"
_MESH_PREFIX = "$/GFX/DepictionResources/Modele_"
_SELECTOR_TACTIC_NAMESPACE_RE = re.compile(r"^InfantrySelectorTactic_(\d+)_(\d+)$")


def edit_gen_gp_gfx_depictioninfantry(source_path: Any, game_db: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionInfantry.ndf"""
    _create_new_selector_tactic_objects(source_path)
    _create_new_units(source_path, game_db)
    _apply_depiction_edits(source_path, game_db)


def _create_new_selector_tactic_objects(source_path: Any) -> None:
    """Insert new ``InfantrySelectorTactic_UU_SS`` rows declared in
    :data:`NEW_SELECTOR_TACTIC_OBJECTS` amongst the existing numbered rows.

    The ``existing`` index is built from the live parsed ``source_path`` so any
    upstream-authored rows (e.g. new ones shipped in a future game patch) are
    detected as duplicates and skipped with a debug log.
    """
    if not NEW_SELECTOR_TACTIC_OBJECTS:
        logger.debug("NEW_SELECTOR_TACTIC_OBJECTS is empty; no selector rows to add")
        return

    existing: dict[tuple[int, int], int] = {}
    for row_index, row in enumerate(source_path):
        namespace = getattr(row, "namespace", None)
        if not namespace:
            continue
        match = _SELECTOR_TACTIC_NAMESPACE_RE.match(namespace)
        if match:
            uu, ss = int(match.group(1)), int(match.group(2))
            existing[(uu, ss)] = row_index

    for uu, ss in NEW_SELECTOR_TACTIC_OBJECTS:
        name = f"InfantrySelectorTactic_{uu:02}_{ss:02}"
        if (uu, ss) in existing or source_path.by_n(name, False):
            logger.debug(f"{name} already present; skipping")
            continue

        higher_keys = sorted(k for k in existing if k > (uu, ss))
        if higher_keys:
            insert_idx = existing[higher_keys[0]]
        else:
            anchor = source_path.by_n("InfantrySelectorTactic_00_01", False)
            if anchor is None:
                logger.error(
                    f"Cannot place {name}: neither a higher-numbered selector row nor "
                    f"the InfantrySelectorTactic_00_01 anchor exists; skipping."
                )
                continue
            insert_idx = None
            for row_index, row in enumerate(source_path):
                if getattr(row, "namespace", None) == "InfantrySelectorTactic_00_01":
                    insert_idx = row_index
                    break
            if insert_idx is None:
                logger.error(f"Lost InfantrySelectorTactic_00_01 anchor while placing {name}")
                continue

        new_row = (
            f"{name} is TemplateInfantrySelectorTactic"
            f"("
            f"    Surrogates = TacticDepiction_{ss:02}_Surrogates"
            f"    UniqueCount = {uu}"
            f")"
        )
        source_path.insert(insert_idx, new_row)
        logger.info(f"Inserted {name} at row {insert_idx}")

        existing[(uu, ss)] = insert_idx
        for key, idx in list(existing.items()):
            if key != (uu, ss) and idx >= insert_idx:
                existing[key] = idx + 1


def _create_new_units(source_path: Any, game_db: Any = None) -> None:
    """Clone donor depiction objects for new infantry units and apply NEW_DEPICTIONS overrides."""

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if not edits.get("is_infantry", False) or edits.get("is_ground_vehicle", False):
            continue

        unit_name = edits["NewName"]
        depiction_key = unit_name.lower()
        infantry_depiction_edits = (
            NEW_DEPICTIONS.get(depiction_key, {}).get("DepictionInfantry_ndf", {}) or {}
        )

        cloned_targets: dict[str, Any] = {}

        # AllWeaponAlternatives_<unit>
        weaponalternatives_obj = source_path.by_namespace(f"AllWeaponAlternatives_{donor_name}").copy()
        weaponalternatives_obj.namespace = f"AllWeaponAlternatives_{unit_name}"
        cloned_targets[weaponalternatives_obj.namespace] = weaponalternatives_obj

        # AllWeaponSubDepiction_<unit>
        weaponsubdepictions_obj = source_path.by_namespace(f"AllWeaponSubDepiction_{donor_name}").copy()
        weaponsubdepictions_obj.namespace = f"AllWeaponSubDepiction_{unit_name}"
        weaponsubdepictions_obj.v.by_member("Alternatives").v = f"AllWeaponAlternatives_{unit_name}"
        cloned_targets[weaponsubdepictions_obj.namespace] = weaponsubdepictions_obj

        # AllWeaponSubDepictionBackpack_<unit>
        weaponbackpack_obj = source_path.by_namespace(f"AllWeaponSubDepictionBackpack_{donor_name}").copy()
        weaponbackpack_obj.namespace = f"AllWeaponSubDepictionBackpack_{unit_name}"
        weaponbackpack_obj.v.by_member("Alternatives").v = f"AllWeaponAlternatives_{unit_name}"
        cloned_targets[weaponbackpack_obj.namespace] = weaponbackpack_obj

        # TacticDepiction_<unit>_Alternatives
        depictionalternatives_list = source_path.by_namespace(f"TacticDepiction_{donor_name}_Alternatives").copy()
        depictionalternatives_list.namespace = f"TacticDepiction_{unit_name}_Alternatives"
        mesh_name = depictionalternatives_list.v[0].v.by_m("MeshDescriptor").v.split("Modele_")[-1]
        if mesh_name != donor_name:
            logger.debug(
                f"Mesh name for {donor_name} is not the same as the unit descriptor name, "
                f"using {mesh_name} instead."
            )
        cloned_targets[depictionalternatives_list.namespace] = depictionalternatives_list

        # TacticDepiction_<unit>_Soldier
        soldierdepiction_obj = source_path.by_namespace(f"TacticDepiction_{donor_name}_Soldier").copy()
        soldierdepiction_obj.namespace = f"TacticDepiction_{unit_name}_Soldier"
        soldierdepiction_obj.v.by_member("Selector").v = f"InfantrySelectorTactic_{edits['selector_tactic']}"
        soldierdepiction_obj.v.by_member("Alternatives").v = f"TacticDepiction_{unit_name}_Alternatives"
        soldierdepiction_obj.v.by_member("SubDepictions").v = (
            f"[AllWeaponSubDepiction_{unit_name}, AllWeaponSubDepictionBackpack_{unit_name}]"
        )
        cloned_targets[soldierdepiction_obj.namespace] = soldierdepiction_obj

        # TacticDepiction_<unit>_Ghost
        ghostdepiction_obj = source_path.by_namespace(f"TacticDepiction_{donor_name}_Ghost").copy()
        ghostdepiction_obj.namespace = f"TacticDepiction_{unit_name}_Ghost"
        ghostdepiction_obj.v.by_member("Selector").v = f"InfantrySelectorTactic_{edits['selector_tactic']}"
        ghostdepiction_obj.v.by_member("Alternatives").v = f"TacticDepiction_{unit_name}_Alternatives"
        cloned_targets[ghostdepiction_obj.namespace] = ghostdepiction_obj

        # Apply NEW_DEPICTIONS overrides for any keyed-by-namespace section.
        for (namespace, obj_type), value in infantry_depiction_edits.items():
            if obj_type == "TTransportedInfantryEntry":
                continue
            if not namespace:
                logger.warning(
                    f"NEW_DEPICTIONS for {unit_name}: section with empty namespace and "
                    f"obj_type={obj_type} skipped"
                )
                continue
            target = cloned_targets.get(namespace)
            if target is None:
                logger.warning(
                    f"NEW_DEPICTIONS for {unit_name}: namespace '{namespace}' does not match any "
                    f"cloned object; skipped"
                )
                continue
            handled = apply_infantry_section(
                source_path,
                target,
                namespace,
                obj_type,
                value,
                unit_name=unit_name,
                game_db=game_db,
            )
            if not handled:
                logger.warning(
                    f"NEW_DEPICTIONS for {unit_name}: section "
                    f"(namespace='{namespace}', obj_type={obj_type}) not handled"
                )

        # Find insertion point and add the cloned block.
        append_row = None
        for row_count, row in enumerate(source_path, start=0):
            if row.namespace == "InfantrySelectorTactic_00_01":
                append_row = row_count
                break

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
        source_path.insert(append_row, new_entries)
        logger.info(f"Added depiction entries for {unit_name}")

        # Synthesize the transported infantry catalog entry from the donor's row.
        _add_transported_infantry_entry(
            source_path,
            unit_name=unit_name,
            donor_name=donor_name,
            mesh_name=mesh_name,
            edits=edits,
            infantry_depiction_edits=infantry_depiction_edits,
        )


def _add_transported_infantry_entry(
    source_path: Any,
    *,
    unit_name: str,
    donor_name: str,
    mesh_name: str,
    edits: dict,
    infantry_depiction_edits: dict,
) -> None:
    """Clone the donor's TTransportedInfantryEntry catalog row and customize it for ``unit_name``."""

    transported_overrides = None
    for (_namespace, obj_type), depiction_edits in infantry_depiction_edits.items():
        if obj_type == "TTransportedInfantryEntry":
            transported_overrides = depiction_edits
            break

    for row in source_path:
        if not isinstance(row.v, ndf.model.Object) or row.v.type != "TTransportedInfantryCatalogEntries":
            continue

        entry_list = row.v.by_member("Entries").v
        new_catalog_entry = None
        for entry in entry_list:
            if entry.v.by_member("Identifier").v == f'"{donor_name}"':
                new_catalog_entry = entry.copy()
                break

        if new_catalog_entry is None:
            logger.error(
                f"Could not find donor TTransportedInfantryEntry for {donor_name} ({unit_name})"
            )
            return

        if transported_overrides is not None and "Meshes" in transported_overrides:
            new_meshes = ndf.model.List()
            for mesh in transported_overrides["Meshes"]:
                new_meshes.add(f"{_MESH_PREFIX}{mesh}")
            new_catalog_entry.v.by_member("Meshes").v = new_meshes
        else:
            model_name = mesh_name if not edits.get("model", False) else edits["model"]
            mesh_paths = [f"{_MESH_PREFIX}{model_name}"]
            for i in range(2, edits.get("alternatives_count", 1) + 1):
                mesh_paths.append(f"{_MESH_PREFIX}{model_name}_{i:02}")
            new_meshes = ndf.model.List()
            for mesh in mesh_paths:
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
        return


def _apply_depiction_edits(source_path: Any, game_db: Any = None) -> None:
    """Apply hand-authored depiction_edits to existing infantry units."""

    depiction_edits = load_depiction_edits()
    for unit_name, unit_data in depiction_edits.items():
        if _NDF_FILE not in unit_data["valid_files"]:
            continue

        if "DepictionInfantry_ndf" not in unit_data:
            logger.error(f"{_NDF_FILE} is valid for {unit_name} but no edits found")
            continue

        unit_edits = unit_data["DepictionInfantry_ndf"]
        logger.debug(f"Processing infantry edits for {unit_name} ({len(unit_edits)} sections)")

        for (namespace, obj_type), value in unit_edits.items():
            target = _resolve_target(source_path, namespace, obj_type, unit_name=unit_name)
            if target is None:
                continue

            handled = apply_infantry_section(
                source_path,
                target,
                namespace,
                obj_type,
                value,
                unit_name=unit_name,
                game_db=game_db,
            )
            if not handled:
                logger.warning(
                    f"depiction_edits for {unit_name}: section "
                    f"(namespace='{namespace}', obj_type={obj_type}) not handled"
                )


def _resolve_target(
    source_path: Any,
    namespace: str,
    obj_type: str,
    *,
    unit_name: str,
) -> Any:
    """Locate the target object/row in ``source_path`` for this section.

    For TTransportedInfantryEntry sections we resolve the matching catalog row;
    otherwise we use the section's namespace.
    """
    if obj_type == "TTransportedInfantryEntry":
        transport_catalog = source_path.find_by_cond(
            lambda x: is_obj_type(x.v, "TTransportedInfantryCatalogEntries")
        )
        if not transport_catalog:
            logger.error(f"depiction_edits for {unit_name}: could not find transport catalog")
            return None
        catalog_entries = transport_catalog.v.by_member("Entries").v
        entry = catalog_entries.find_by_cond(
            lambda x: x.v.by_member("Identifier").v == f'"{unit_name}"'
        )
        if not entry:
            logger.error(
                f"depiction_edits for {unit_name}: could not find TTransportedInfantryEntry"
            )
            return None
        return entry

    if not namespace:
        logger.error(
            f"depiction_edits for {unit_name}: section with empty namespace and "
            f"obj_type={obj_type} cannot be resolved"
        )
        return None

    target = source_path.by_n(namespace, False)
    if not target:
        logger.error(f"depiction_edits for {unit_name}: could not find {namespace}")
        return None
    return target


# Re-export for backwards compatibility with any external callers.
__all__ = [
    "edit_gen_gp_gfx_depictioninfantry",
    "overwrite_skeleton_conditional_tags",
]
