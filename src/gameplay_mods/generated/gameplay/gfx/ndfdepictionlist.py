"""Functions for modifying NdfDepictionList.ndf"""

from typing import Any
from src.constants.new_units import NEW_DEPICTIONS
from src.constants.unit_edits import load_depiction_edits
from src.gameplay_mods.gameplay.gfx.depictionresources import _iter_mesh_definitions
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import find_obj_by_namespace

logger = setup_logger(__name__)

def edit_gen_gp_gfx_ndfdepictionlist(source_path: Any) -> None:
    """GameData/Generated/Gameplay/Gfx/NdfDepictionList.ndf"""
    
    generateddepictionndffiles = find_obj_by_namespace(source_path, "GeneratedDepictionNdfFiles")
    _handle_new_units(generateddepictionndffiles)
    _handle_depiction_edits(generateddepictionndffiles)
    
    
def _register_mesh_path(generateddepictionndffiles: Any, file_name: str, directory: str) -> None:
    """Register a mesh NDF file path in GeneratedDepictionNdfFiles."""
    path = f'"GameData:/Gameplay/Gfx/DepictionResources/{directory}/{file_name}.ndf"'
    generateddepictionndffiles.v.add(path)
    logger.info(f"Registered {path}")


def _handle_new_units(generateddepictionndffiles: Any) -> None:
    """Handle new units for NdfDepictionList.ndf"""
    
    logger.info("Creating NdfDepictionList entries")
    
    for unit_descr_name, unit_data in NEW_DEPICTIONS.items():
        for file_name, directory, _ in _iter_mesh_definitions(unit_data):
            _register_mesh_path(generateddepictionndffiles, file_name, directory)


def _handle_depiction_edits(generateddepictionndffiles: Any) -> None:
    """Register mesh NDF files from depiction edits."""
    depiction_edits = load_depiction_edits()
    
    for unit_name, unit_data in depiction_edits.items():
        for file_name, directory, _ in _iter_mesh_definitions(unit_data):
            _register_mesh_path(generateddepictionndffiles, file_name, directory)