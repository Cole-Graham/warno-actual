"""Batch size-parameter scaling for FX NDF files using ndf_parse."""

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple

# Add project root to path for imports (same as dpm_visualizer)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src import ndf
from src.utils.ndf_utils import strip_quotes


# Size-related parameter patterns to scale (migrated from fx_size_scaler)
SIZE_PARAM_PATTERNS = [
    r'parSize\b',
    r'parSize1\b',
    r'parSize2\b',
    r'parFinalSize\b',
    r'parInitialSize\b',
    r'parStartSize\b',
    r'parEndSize\b',
    r'parDustSize\b',
    r'parMudSize\b',
    r'parParticleSize\b',
    r'parFireParticleStartSize\b',
    r'parFireParticleEndSize\b',
    r'parSmokeParticleStartSize\b',
    r'parSmokeParticleEndSize\b',
    r'parSizeLBU\b',
    r'parRadius\b',
    r'parPositionRadius\b',
    r'parSpawnRadius\b',
    r'parStartRandomRadius\b',
    r'parRandomInitPosRadius\b',
    r'parScaleSizeFactor\b',
    r'parDebritSizeMul\b',
    r'parHeight\b',
    r'parCloudsize\b',
    r'parDispersion\b',
]

SIZE_PARAM_REGEX = re.compile(
    r'(' + '|'.join(SIZE_PARAM_PATTERNS) + r')',
    re.IGNORECASE,
)

FLOAT3_REGEX = re.compile(
    r'^float3\s*\[\s*([^\]]+)\s*\]\s*$',
    re.IGNORECASE,
)

EXPR_NUMERIC_REGEX = re.compile(
    r'^([a-zA-Z_][a-zA-Z0-9_]*)\s*([+\-])\s*([+\-]?\d+(?:\.\d+)?)\s*$',
)


@dataclass
class SizeChange:
    """Represents a scaled size parameter change."""
    name: str
    old_value: str
    new_value: str


def is_size_param(name: str) -> bool:
    """Check if a parameter name is size-related."""
    return bool(SIZE_PARAM_REGEX.search(name))


def _format_number(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    return str(value)


def _parse_float3(text: str) -> Optional[List[float]]:
    match = FLOAT3_REGEX.match(text)
    if not match:
        return None
    parts = [part.strip() for part in match.group(1).split(',')]
    values: List[float] = []
    for part in parts:
        try:
            values.append(float(part))
        except ValueError:
            return None
    return values


def _format_float3(values: Iterable[float]) -> str:
    formatted = ','.join(_format_number(v) for v in values)
    return f'float3[{formatted}]'


def _stringify_value(value: Any) -> str:
    if isinstance(value, (ndf.model.List, ndf.model.Map, ndf.model.Object)):
        return ndf.printer.string(value).strip()
    return str(value)


def _scale_numeric_string(text: str, scale_factor: float) -> Optional[str]:
    try:
        numeric = float(text)
    except ValueError:
        return None
    return _format_number(numeric * scale_factor)


def _scale_float3_string(text: str, scale_factor: float) -> Optional[str]:
    values = _parse_float3(text)
    if values is None:
        return None
    scaled = [v * scale_factor for v in values]
    return _format_float3(scaled)


def _scale_expression_string(text: str, scale_factor: float) -> Optional[str]:
    match = EXPR_NUMERIC_REGEX.match(text)
    if not match:
        return None
    var_name = match.group(1)
    operator = match.group(2)
    number_text = match.group(3)
    try:
        number = float(number_text)
    except ValueError:
        return None
    scaled = _format_number(number * scale_factor)
    return f'{var_name} {operator} {scaled}'


def _scale_list_value(value: ndf.model.List, scale_factor: float) -> Optional[ndf.model.List]:
    if value.type and value.type.lower() == 'float3':
        for row in value:
            try:
                numeric = float(row.v)
            except (TypeError, ValueError):
                return None
            row.v = _format_number(numeric * scale_factor)
        return value
    return None


def scale_map_row(map_row: ndf.model.MapRow, scale_factor: float, dry_run: bool) -> Optional[SizeChange]:
    """Scale a MapRow value if it matches size parameter patterns."""
    key_text = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
    if not is_size_param(key_text):
        return None

    old_value = map_row.v
    old_value_str = _stringify_value(old_value)

    new_value: Any = None
    new_value_str: Optional[str] = None

    if isinstance(old_value, (int, float)):
        new_value = old_value * scale_factor
        new_value_str = _format_number(float(new_value))
    elif isinstance(old_value, ndf.model.List):
        scaled_list = _scale_list_value(old_value, scale_factor)
        if scaled_list is not None:
            new_value = scaled_list
            new_value_str = _stringify_value(new_value)
    elif isinstance(old_value, str):
        new_value_str = _scale_numeric_string(old_value, scale_factor)
        if new_value_str is None:
            new_value_str = _scale_float3_string(old_value, scale_factor)
        if new_value_str is None:
            new_value_str = _scale_expression_string(old_value, scale_factor)
        if new_value_str is not None:
            try:
                parsed = ndf.expression(new_value_str)
                if isinstance(parsed, dict) and 'value' in parsed:
                    new_value = parsed['value']
                else:
                    new_value = new_value_str
            except Exception:
                new_value = new_value_str

    if new_value_str is None:
        return None

    if not dry_run:
        map_row.v = new_value

    return SizeChange(
        name=key_text,
        old_value=old_value_str,
        new_value=new_value_str,
    )


def iter_map_rows(root: Any) -> Iterable[ndf.model.MapRow]:
    """Yield all MapRow objects in the parsed tree."""
    if isinstance(root, ndf.model.Map):
        for map_row in root:
            yield map_row
            yield from iter_map_rows(map_row.v)
        return
    if isinstance(root, ndf.model.List):
        for row in root:
            yield from iter_map_rows(row.v)
        return
    if isinstance(root, ndf.model.Object):
        for member in root:
            yield from iter_map_rows(member.v)
        return
    if isinstance(root, ndf.model.MemberRow):
        yield from iter_map_rows(root.v)
        return
    if isinstance(root, ndf.model.ListRow):
        yield from iter_map_rows(root.v)
        return


def scale_size_params(parsed_root: ndf.model.List, scale_factor: float, dry_run: bool) -> List[SizeChange]:
    """Scale size-related parameters for a parsed NDF tree."""
    changes: List[SizeChange] = []
    for map_row in iter_map_rows(parsed_root):
        change = scale_map_row(map_row, scale_factor, dry_run)
        if change:
            changes.append(change)
    return changes


def process_file(file_path: Path, scale_factor: float, dry_run: bool) -> Dict[str, Any]:
    """Process a file and scale size parameters."""
    stats: Dict[str, Any] = {
        'file': str(file_path),
        'changes': [],
        'error': None,
    }
    try:
        with open(file_path, 'r', encoding='utf-8') as handle:
            content = handle.read()
        parsed = ndf.convert(content)
        if not isinstance(parsed, ndf.model.List):
            raise ValueError(f'Expected ndf.model.List, got {type(parsed).__name__}')
        changes = scale_size_params(parsed, scale_factor, dry_run)
        stats['changes'] = changes
        if not dry_run and changes:
            formatted = ndf.printer.string(parsed)
            with open(file_path, 'w', encoding='utf-8') as handle:
                handle.write(formatted)
    except Exception as exc:
        stats['error'] = str(exc)
    return stats


def find_fx_files(directory: Path, pattern: str = '*.ndf') -> List[Path]:
    """Find FX NDF files in a directory."""
    if not directory.exists():
        return []
    return sorted(directory.glob(pattern))
