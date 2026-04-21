"""Functions for modifying DepictionAlternatives.ndf"""

from typing import Any

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_depiction_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

_NDF_FILE = "DepictionAlternatives.ndf"
_MESH_PREFIX = "$/GFX/DepictionResources/Modele_"


def edit_gen_gp_gfx_depictionalternatives(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionAlternatives.ndf"""
    _handle_new_units(source_path)
    _apply_depiction_edits(source_path)


def _handle_new_units(source_path: Any) -> None:
    """Handle new units for DepictionAlternatives.ndf"""

    logger.info("Creating alternatives depiction entries")

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if not edits.get("is_ground_vehicle", False) and not edits.get("is_aerial", False):
            continue

        unit_name = edits["NewName"]
        new_mesh = edits.get("depictions", {}).get("new_mesh", False)
        existing_mesh = edits.get("depictions", {}).get("alternatives", False)
        uses_donor_mesh = not new_mesh and not existing_mesh

        if new_mesh:
            entry = (
                f"Alternatives_{unit_name} is ["
                f"    DepictionVisual_LOD_High( MeshDescriptor = {_MESH_PREFIX}{unit_name} ),"
                f"    DepictionVisual_LOD_Mid( MeshDescriptor = {_MESH_PREFIX}{unit_name}_MID ),"
                f"    DepictionVisual_LOD_Low( MeshDescriptor = {_MESH_PREFIX}{unit_name}_LOW ),"
                f"]"
            )
        elif existing_mesh:
            entry = (
                f"Alternatives_{unit_name} is ["
                f"    DepictionVisual_LOD_High( MeshDescriptor = {_MESH_PREFIX}{existing_mesh} ),"
                f"    DepictionVisual_LOD_Mid( MeshDescriptor = {_MESH_PREFIX}{existing_mesh}_MID ),"
                f"    DepictionVisual_LOD_Low( MeshDescriptor = {_MESH_PREFIX}{existing_mesh}_LOW ),"
                f"]"
            )
        elif uses_donor_mesh:
            entry = (
                f"Alternatives_{unit_name} is ["
                f"    DepictionVisual_LOD_High( MeshDescriptor = {_MESH_PREFIX}{donor_name} ),"
                f"    DepictionVisual_LOD_Mid( MeshDescriptor = {_MESH_PREFIX}{donor_name}_MID ),"
                f"    DepictionVisual_LOD_Low( MeshDescriptor = {_MESH_PREFIX}{donor_name}_LOW ),"
                f"]"
            )
        else:
            logger.error(f"No mesh found for {unit_name}")
            continue
        source_path.add(entry)
        logger.info(f"Added alternatives depiction for {unit_name}")


def _apply_depiction_edits(source_path: Any) -> None:
    """Apply hand-authored depiction_edits to existing Alternatives_<unit> lists.

    Expected schema in a depiction_edits file:

        "valid_files": ["DepictionAlternatives.ndf", ...],
        "DepictionAlternatives_ndf": {
            ("Alternatives_<unit>", None): {
                "mesh": "<mesh_stem>",   # writes High/Mid/Low MeshDescriptors
            },
        }
    """
    logger.info("Updating alternatives depiction entries from depiction_edits")

    depiction_edits = load_depiction_edits()
    for unit_name, unit_data in depiction_edits.items():
        if _NDF_FILE not in unit_data.get("valid_files", []):
            continue

        if "DepictionAlternatives_ndf" not in unit_data:
            logger.error(f"{_NDF_FILE} is valid for {unit_name} but no edits found")
            continue

        unit_edits = unit_data["DepictionAlternatives_ndf"]
        for key, edits in unit_edits.items():
            if not isinstance(key, tuple):
                logger.error(f"Key is not a tuple: {key}")
                continue

            namespace, _obj_type = key
            if not namespace:
                logger.error(f"Empty namespace in DepictionAlternatives edits for {unit_name}")
                continue

            alternatives_list = source_path.by_namespace(namespace, False)
            if not alternatives_list:
                logger.error(f"No alternatives list found for {namespace} ({unit_name})")
                continue

            mesh_stem = edits.get("mesh") if isinstance(edits, dict) else None
            if mesh_stem:
                alternatives_list.v[0].v.by_m("MeshDescriptor").v = f"{_MESH_PREFIX}{mesh_stem}"
                alternatives_list.v[1].v.by_m("MeshDescriptor").v = f"{_MESH_PREFIX}{mesh_stem}_MID"
                alternatives_list.v[2].v.by_m("MeshDescriptor").v = f"{_MESH_PREFIX}{mesh_stem}_LOW"
                logger.info(f"Updated alternatives mesh for {unit_name} -> {mesh_stem}")
