"""Functions for modifying DepictionAlternatives.ndf"""

from typing import Any
from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

UNIT_EDITS = load_unit_edits()

def edit_gen_gp_gfx_depictionalternatives(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/Depictions/DepictionAlternatives.ndf"""
    
    _handle_new_units(source_path)
    _handle_unit_edits(source_path)
    
    
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
        uses_donor_mesh = False
        if not new_mesh and not existing_mesh:
            uses_donor_mesh = True

        # Create alternatives entry using new or donor's models
        if new_mesh:
            entry = (
                f"Alternatives_{unit_name} is ["
                f"    DepictionVisual_LOD_High( MeshDescriptor = $/GFX/DepictionResources/Modele_{unit_name} ),"
                f"    DepictionVisual_LOD_Mid( MeshDescriptor = $/GFX/DepictionResources/Modele_{unit_name}_MID ),"
                f"    DepictionVisual_LOD_Low( MeshDescriptor = $/GFX/DepictionResources/Modele_{unit_name}_LOW ),"
                f"]"
            )
        elif existing_mesh:
            entry = (
                f"Alternatives_{unit_name} is ["
                f"    DepictionVisual_LOD_High( MeshDescriptor = $/GFX/DepictionResources/Modele_{existing_mesh} ),"
                f"    DepictionVisual_LOD_Mid( MeshDescriptor = $/GFX/DepictionResources/Modele_{existing_mesh}_MID ),"
                f"    DepictionVisual_LOD_Low( MeshDescriptor = $/GFX/DepictionResources/Modele_{existing_mesh}_LOW ),"
                f"]"
            )
        elif uses_donor_mesh:
            entry = (
                f"Alternatives_{unit_name} is ["
                f"    DepictionVisual_LOD_High( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor_name} ),"
                f"    DepictionVisual_LOD_Mid( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor_name}_MID ),"
                f"    DepictionVisual_LOD_Low( MeshDescriptor = $/GFX/DepictionResources/Modele_{donor_name}_LOW ),"
                f"]"
            )
        else:
            logger.error(f"No mesh found for {unit_name}")
            continue
        source_path.add(entry)
        logger.info(f"Added alternatives depiction for {unit_name}")
        
        
def _handle_unit_edits(source_path: Any) -> None:
    """Handle unit edits for DepictionAlternatives.ndf"""
    
    logger.info("Updating alternatives depiction entries")
    
    for unit_name, edits in UNIT_EDITS.items():
        if "Alternatives" in edits and "mesh" in edits["Alternatives"]:
            alternatives_list = source_path.by_namespace(f"Alternatives_{unit_name}", False)
            if alternatives_list:
                prefix = "$/GFX/DepictionResources/Modele_"
                # High
                alternatives_list.v[0].v.by_m("MeshDescriptor").v = f"{prefix}{edits["Alternatives"]["mesh"]}"
                # Mid
                alternatives_list.v[1].v.by_m("MeshDescriptor").v = f"{prefix}{edits["Alternatives"]["mesh"]}_MID"
                # Low
                alternatives_list.v[2].v.by_m("MeshDescriptor").v = f"{prefix}{edits["Alternatives"]["mesh"]}_LOW"
                logger.info(f"Updated alternatives depiction for {unit_name}")
            else:
                logger.error(f"No alternatives list found for {unit_name}")