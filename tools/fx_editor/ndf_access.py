"""NDF file access helpers for FX editor."""

import sys
from pathlib import Path
from typing import Optional

# Add project root to path for imports (same as dpm_visualizer)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src import ndf


def parse_ndf_file(file_path: Path) -> ndf.model.List:
    """Parse an NDF file into an ndf_parse model.List."""
    with open(file_path, 'r', encoding='utf-8') as handle:
        content = handle.read()
    parsed = ndf.convert(content)
    if not isinstance(parsed, ndf.model.List):
        raise ValueError(f'Expected ndf.model.List, got {type(parsed).__name__}')
    return parsed


def format_ndf(parsed_root: ndf.model.List) -> str:
    """Format the parsed NDF model to string."""
    return ndf.printer.string(parsed_root)


def write_ndf_file(file_path: Path, parsed_root: ndf.model.List) -> None:
    """Write formatted NDF back to disk."""
    content = format_ndf(parsed_root)
    with open(file_path, 'w', encoding='utf-8') as handle:
        handle.write(content)


def get_export_row(parsed_root: ndf.model.List) -> Optional[ndf.model.ListRow]:
    """Get the first export/list row if present."""
    if len(parsed_root) == 0:
        return None
    row = parsed_root[0]
    if isinstance(row, ndf.model.ListRow):
        return row
    return None


def update_namespace(parsed_root: ndf.model.List, new_namespace: str) -> None:
    """Update the namespace in the export statement.
    
    Args:
        parsed_root: The parsed NDF root (ndf.model.List)
        new_namespace: The new namespace to set
        
    Raises:
        ValueError: If no export row is found or namespace cannot be updated
    """
    if len(parsed_root) == 0:
        raise ValueError("No export statement found in file")
    
    row = parsed_root[0]
    if not isinstance(row, ndf.model.ListRow):
        raise ValueError("First row is not an export statement (ListRow)")
    
    # Update the namespace
    row.namespace = new_namespace
