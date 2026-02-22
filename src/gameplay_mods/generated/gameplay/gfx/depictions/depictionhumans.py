"""Functions for modifying DepictionHumans.ndf"""

from typing import Any
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)

# Base path for mesh descriptors (Servant vs Driver)
_MESH_BASE = "$/GFX/DepictionResources/"


def _mesh_descriptor_path(servant_id: str, type_name: str) -> str:
    """Return mesh descriptor path for a servant and subdepiction type (e.g. Driver vs Servant)."""
    if type_name == "Driver":
        return f"{_MESH_BASE}MeshDescriptor_Driver_{servant_id}"
    return f"{_MESH_BASE}MeshDescriptor_Servant_{servant_id}"


def _build_subdepictions_ndf(
    unit_name: str,
    servant_types_by_servant: dict[str, list[str]],
    servant_order: tuple[str, ...],
) -> tuple[str, list[str]]:
    """
    Build HumanSubDepictions NDF block (in-game view).
    Returns (ndf_string, list of mesh paths for catalog).
    """
    mesh_paths: list[str] = []
    entries: list[str] = []
    for servant_id in servant_order:
        type_names = servant_types_by_servant.get(servant_id, [])
        for type_name in type_names:
            mesh_high = _mesh_descriptor_path(servant_id, type_name)
            mesh_low = f"{mesh_high}_LOW"
            mesh_paths.append(mesh_high)
            entries.append(
                f"    SubDepiction_{type_name}\n"
                f"    (\n"
                f"        MeshDescriptorHigh = {mesh_high}\n"
                f"        MeshDescriptorLow = {mesh_low}\n"
                f"    )"
            )
    body = ",\n".join(entries)
    ndf = f"HumanSubDepictions_{unit_name} is\n[\n{body}\n]\n"
    return ndf, mesh_paths


def _build_showroom_ndf(
    unit_name: str,
    servant_types_by_servant: dict[str, list[str]],
    servant_order: tuple[str, ...],
) -> str:
    """
    Build HumanSubDepictionsShowroom NDF block (showroom/armory view).
    Returns "[]" if no showroom types.
    """
    entries: list[str] = []
    for servant_id in servant_order:
        type_names = servant_types_by_servant.get(servant_id, [])
        for type_name in type_names:
            mesh = _mesh_descriptor_path(servant_id, type_name)
            entries.append(
                f"    ShowroomSubDepiction_{type_name}\n"
                f"    (\n"
                f"        MeshDescriptor = {mesh}\n"
                f"    )"
            )
    if not entries:
        return f"HumanSubDepictionsShowroom_{unit_name} is []\n"
    body = ",\n".join(entries)
    return f"HumanSubDepictionsShowroom_{unit_name} is\n[\n{body}\n]\n"


def edit_gen_gp_gfx_depictionhumans(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionHumans.ndf"""
    
    _handle_new_units(source_path)
    
    
def _handle_new_units(source_path: Any) -> None:
    """Handle new units for DepictionHumans.ndf"""
    
    logger.info("Creating human depiction entries for vehicles")

    for donor, edits in NEW_UNITS.items():
        donor_name = donor[0]
        if not (edits.get("is_ground_vehicle", False) and edits.get("is_heavy_equipment", False)):
            logger.info(f"Skipping {donor_name} because it's not a vehicle or heavy equipment")
            continue

        unit_name = edits["NewName"]

        # Find donor mesh names
        mesh_names = None
        if "servants" in edits:
            mesh_names = edits["servants"]

        if not mesh_names:
            logger.warning(f"Could not find mesh names for {donor_name}")
            continue

        servant_order = mesh_names
        servant_types = edits.get("servant_types", {})
        showroom_servant_types = servant_types.get("showroom", {})
        subdepictions_servant_types = servant_types.get("subdepictions", {})

        if subdepictions_servant_types:
            # New format: build from servant_types keys
            human_depiction, catalog_mesh_paths = _build_subdepictions_ndf(
                unit_name,
                subdepictions_servant_types,
                servant_order,
            )
            showroom_depiction = _build_showroom_ndf(
                unit_name,
                showroom_servant_types,
                servant_order,
            )
        else:
            # Fallback: no servant_types — use legacy is_heavy_equipment logic
            logger.warning(f"No servant_types found for {unit_name}, using legacy logic")
            left_mesh, right_mesh = servant_order[0], servant_order[1]
            if edits.get("is_heavy_equipment", False):
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
            catalog_mesh_paths = [
                f"{_MESH_BASE}MeshDescriptor_Servant_{left_mesh}",
                f"{_MESH_BASE}MeshDescriptor_Servant_{right_mesh}",
            ]

        # Find insertion point and add entries
        for row in source_path:
            if not is_obj_type(row.v, "TTransportedInfantryCatalogEntries"):
                continue

            source_path.insert(row.index, showroom_depiction)
            source_path.insert(row.index, human_depiction)
            logger.info(f"Added human depictions for {unit_name}")

            # Add catalog entry (unique mesh paths in order)
            unique_meshes = list(dict.fromkeys(catalog_mesh_paths))
            meshes_lines = ",\n".join(f"        {p}" for p in unique_meshes)
            catalog_entry = (
                f"TTransportedInfantryEntry\n"
                f"(\n"
                f'    Count = {edits["alternatives_count"]}\n'
                f'    Identifier = "{unit_name}"\n'
                f"    Meshes =\n"
                f"    [\n"
                f"{meshes_lines}\n"
                f"    ]\n"
                f'    UniqueCount = {edits["alternatives_count"]}\n'
                f")\n"
            )

            row.v.by_m("Entries").v.add(catalog_entry)
            logger.info(f"Added catalog entry for {unit_name}")
            break
