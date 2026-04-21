"""Functions for modifying various depiction resources"""

import textwrap
from pathlib import Path
from typing import Dict, Generator, Tuple

from src.constants.new_units import NEW_DEPICTIONS
from src.constants.unit_edits import load_depiction_edits
from src.utils.logging_utils import setup_logger
from src.utils.config_utils import get_mod_dst_path

logger = setup_logger(__name__)


def _iter_mesh_definitions(unit_data: Dict) -> Generator[Tuple[str, str, str], None, None]:
    """Yield (file_name, directory, ndf_code) for each mesh definition in a unit data dict.
    
    Mesh definitions are top-level string keys whose value is a dict containing
    both "directory" and "ndf_code". The file name is derived by stripping the
    "_ndf" suffix from the key.
    """
    for key, value in unit_data.items():
        if (isinstance(key, str)
                and isinstance(value, dict)
                and "directory" in value
                and "ndf_code" in value):
            file_name = key.removesuffix("_ndf")
            yield file_name, value["directory"], value["ndf_code"]


def _write_mesh_ndf(mod_dst_path: Path, file_name: str, directory: str, ndf_code: str) -> None:
    """Write a TResourceMesh NDF file to the DepictionResources directory."""
    target_path = mod_dst_path / "GameData" / "Gameplay" / "Gfx" / "DepictionResources" / directory

    if not target_path.exists():
        raise FileNotFoundError(f"Target directory does not exist: {target_path}")

    ndf_file_path = target_path / f"{file_name}.ndf"

    try:
        cleaned_code = textwrap.dedent(ndf_code)
        with open(ndf_file_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_code)
        logger.info(f"Created/overwritten {ndf_file_path}")
    except Exception as e:
        logger.error(f"Failed to write {ndf_file_path}: {e}")
        raise


def add_unit_meshes(config: Dict) -> None:
    """Add specific unit meshes by creating new .ndf files in the correct directory structure.
    
    Args:
        config: Configuration dictionary containing mod paths and settings
    """
    mod_dst_path = get_mod_dst_path(config)
    
    for unit_descr_name, unit_data in NEW_DEPICTIONS.items():
        for file_name, directory, ndf_code in _iter_mesh_definitions(unit_data):
            _write_mesh_ndf(mod_dst_path, file_name, directory, ndf_code)

    depiction_edits = load_depiction_edits()
    for unit_name, unit_data in depiction_edits.items():
        for file_name, directory, ndf_code in _iter_mesh_definitions(unit_data):
            _write_mesh_ndf(mod_dst_path, file_name, directory, ndf_code)