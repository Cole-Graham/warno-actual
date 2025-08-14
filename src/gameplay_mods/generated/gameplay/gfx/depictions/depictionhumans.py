"""Functions for modifying DepictionHumans.ndf"""

from typing import Any
from src.constants.new_units import NEW_UNITS
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def edit_gen_gp_gfx_depictionhumans(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionHumans.ndf"""
    
    _handle_new_units(source_path)
    
    
def _handle_new_units(source_path: Any) -> None:
    """Handle new units for DepictionHumans.ndf"""
    
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
