"""Batch size-parameter scaling for FX NDF files using ndf_parse."""

import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, DefaultDict, Dict, Iterable, List, Optional, Set, Tuple

# Add project root to path for imports (same as dpm_visualizer)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .ndf_access import update_namespace
from .scatter_analyze import vfx_effect_group_burst_counts
from .scatter_timeline import _list_row_child_v


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
    r'parRadiusPhysical\b',
    r'parRadiusSuppress\b',
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

# Count-like parameters (NamedParams / counts); scaled as integers (rounded).
COUNT_PARAM_PATTERNS = [
    r'parCount\b',
    r'parCountDebrits\b',
    r'parCountDebritsWithFire\b',
]

COUNT_PARAM_REGEX = re.compile(
    r'(' + '|'.join(COUNT_PARAM_PATTERNS) + r')',
    re.IGNORECASE,
)


def _pattern_to_param_name(pattern: str) -> str:
    if pattern.endswith(r'\b'):
        return pattern[:-2]
    return pattern


KNOWN_SIZE_PARAM_NAMES: Tuple[str, ...] = tuple(
    _pattern_to_param_name(p) for p in SIZE_PARAM_PATTERNS
)


def is_size_param_name_allowed(key_text: str, allowed_names: Optional[Set[str]]) -> bool:
    """If ``allowed_names`` is ``None``, any size param may be scaled. If empty, none. Else case-insensitive match."""
    if allowed_names is None:
        return True
    if not allowed_names:
        return False
    kl = key_text.lower()
    return any(a.lower() == kl for a in allowed_names)

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


@dataclass
class ParamDefaultTarget:
    """``DefaultValue`` member inside a ``Params`` list ``TActionAlias`` row (e.g. parRadiusPhysical)."""

    member_row: ndf.model.MemberRow
    param_name: str


def param_alias_name_from_list_row(list_row: ndf.model.ListRow) -> str:
    """Strip ``private`` / `` is TActionAlias`` from a Params list row label."""
    ns = strip_quotes(str(list_row.namespace or '')).strip()
    if ' is ' in ns:
        ns = ns.split(' is ')[0].strip()
    if ns.startswith('private '):
        ns = ns[8:].strip()
    return ns


def iter_param_default_targets(parsed_root: ndf.model.List) -> Iterable[ParamDefaultTarget]:
    """Yield ``DefaultValue`` members for declaration ``Params`` (e.g. parRadiusPhysical).

    Walks every top-level ``ListRow`` so files with a leading comment row (or multiple exports)
    still resolve the declaration block.
    """
    for top in parsed_root:
        if not isinstance(top, ndf.model.ListRow):
            continue
        obj = top.v
        if not isinstance(obj, ndf.model.Object):
            continue
        for member in obj:
            if member.member != 'Params' or not isinstance(member.v, ndf.model.List):
                continue
            for alias_row in member.v:
                if not isinstance(alias_row, ndf.model.ListRow):
                    continue
                name = param_alias_name_from_list_row(alias_row)
                if not isinstance(alias_row.v, ndf.model.Object):
                    continue
                for m in alias_row.v:
                    if isinstance(m, ndf.model.MemberRow) and m.member == 'DefaultValue':
                        yield ParamDefaultTarget(m, name)


def _format_count_scaled(value: float, scale_factor: float, source_text: str) -> str:
    scaled = float(value) * scale_factor
    out = int(round(scaled))
    if out < 0:
        out = 0
    return str(out)


def _ndf_scalar_from_scaled_string(
    new_value_str: str,
    *,
    prefer_int: bool,
    fallback_for_size: Optional[float] = None,
) -> Any:
    """Parse scaled text like str-originated params (``ndf.expression``), not raw Python float.

    Assigning bare ``float``/``int`` to NDF ``MapRow``/``MemberRow`` values can violate Row typing
    (e.g. validation: Row expects str | List | Row | tuple[2], got float).
    """
    try:
        parsed = ndf.expression(new_value_str)
        if isinstance(parsed, dict) and 'value' in parsed:
            return parsed['value']
    except Exception:
        pass
    if prefer_int:
        try:
            return int(new_value_str.strip())
        except ValueError:
            return new_value_str
    try:
        if re.match(r'^-?\d+$', new_value_str.strip()):
            return int(new_value_str.strip())
        return float(new_value_str)
    except ValueError:
        return fallback_for_size if fallback_for_size is not None else new_value_str


def scale_param_default_member(
    target: ParamDefaultTarget,
    scale_factor: float,
    dry_run: bool,
    *,
    scale_size: bool,
    scale_count: bool,
    allowed_names: Optional[Set[str]],
) -> Optional[SizeChange]:
    """Scale ``DefaultValue`` in ``Params`` when the alias name matches size/count rules."""
    name = target.param_name
    if is_size_param(name):
        if not scale_size:
            return None
        if not is_size_param_name_allowed(name, allowed_names):
            return None
    elif is_count_param(name):
        if not scale_count:
            return None
    else:
        return None

    mr = target.member_row
    old_value = mr.v
    old_value_str = _stringify_value(old_value)

    new_value: Any = None
    new_value_str: Optional[str] = None

    if isinstance(old_value, (int, float)):
        if is_count_param(name):
            new_value_str = _format_count_scaled(float(old_value), scale_factor, str(old_value))
            new_value = _ndf_scalar_from_scaled_string(new_value_str, prefer_int=True)
        else:
            scaled = float(old_value) * scale_factor
            src_text = _numeric_format_source_text(old_value)
            new_value_str = _format_scaled_from_source_text(scaled, src_text)
            new_value = _ndf_scalar_from_scaled_string(
                new_value_str,
                prefer_int=False,
                fallback_for_size=scaled,
            )
    elif isinstance(old_value, ndf.model.List):
        scaled_list = _scale_list_value(old_value, scale_factor)
        if scaled_list is not None:
            new_value = scaled_list
            new_value_str = _stringify_value(new_value)
    elif isinstance(old_value, str):
        if is_count_param(name):
            try:
                numeric = float(old_value)
            except ValueError:
                return None
            new_value_str = _format_count_scaled(numeric, scale_factor, old_value)
            try:
                parsed = ndf.expression(new_value_str)
                if isinstance(parsed, dict) and 'value' in parsed:
                    new_value = parsed['value']
                else:
                    new_value = int(new_value_str)
            except Exception:
                new_value = int(new_value_str)
        else:
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
        mr.v = new_value

    display_name = f'{name} (Params DefaultValue)'
    return SizeChange(
        name=display_name,
        old_value=old_value_str,
        new_value=new_value_str,
    )


def is_size_param(name: str) -> bool:
    """Check if a parameter name is size-related."""
    return bool(SIZE_PARAM_REGEX.search(name))


def is_count_param(name: str) -> bool:
    """Check if a parameter name is count-related (integer-like scaling)."""
    return bool(COUNT_PARAM_REGEX.search(name))


def _format_number(value: float) -> str:
    """Fallback formatting when source text shape is unknown."""
    if value.is_integer():
        return str(int(value))
    return str(value)


def _format_float_with_decimal_places(scaled: float, places: int) -> str:
    """Round to ``places`` fractional digits and trim redundant trailing zeros."""
    if places <= 0:
        return str(int(round(scaled)))
    rounded = round(scaled, places)
    formatted = f'{rounded:.{places}f}'
    return formatted.rstrip('0').rstrip('.') if '.' in formatted else formatted


def _format_scaled_from_source_text(scaled: float, source_text: str) -> str:
    """Round ``scaled`` to match the lexical form of the source number (int vs decimal)."""
    s = source_text.strip()
    if re.match(r'^-?\d+$', s):
        return str(int(round(scaled)))
    m = re.match(r'^(-?\d+)\.(\d*)$', s)
    if m:
        frac = m.group(2)
        if frac == '' or re.match(r'^0+$', frac):
            return str(int(round(scaled)))
        places = len(frac)
        return _format_float_with_decimal_places(scaled, places)
    if re.search(r'[eE]', s):
        try:
            src = float(s)
        except ValueError:
            return _format_number(scaled)
        if src == int(src):
            return str(int(round(scaled)))
        return _format_float_with_decimal_places(scaled, 6)
    try:
        src = float(s)
        if src == int(src):
            return str(int(round(scaled)))
        return _format_float_with_decimal_places(scaled, 6)
    except ValueError:
        return _format_number(scaled)


def _numeric_format_source_text(original: Any) -> str:
    """Text form of a numeric ``original`` for format inference (int / float / double)."""
    if isinstance(original, bool):
        return str(int(original))
    if isinstance(original, int):
        return str(original)
    if isinstance(original, float):
        if original.is_integer():
            return str(int(original))
        s = str(original)
        if re.search(r'[eE]', s):
            return s
        return s
    return str(original).strip()


def _stringify_value(value: Any) -> str:
    if isinstance(value, (ndf.model.List, ndf.model.Map, ndf.model.Object)):
        return ndf.printer.string(value).strip()
    return str(value)


def _scale_numeric_string(text: str, scale_factor: float) -> Optional[str]:
    try:
        numeric = float(text)
    except ValueError:
        return None
    return _format_scaled_from_source_text(numeric * scale_factor, text)


def _scale_float3_string(text: str, scale_factor: float) -> Optional[str]:
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
    scaled_strs = [
        _format_scaled_from_source_text(values[i] * scale_factor, parts[i])
        for i in range(len(parts))
    ]
    formatted = ','.join(scaled_strs)
    return f'float3[{formatted}]'


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
    scaled = _format_scaled_from_source_text(number * scale_factor, number_text)
    return f'{var_name} {operator} {scaled}'


def _scale_list_value(value: ndf.model.List, scale_factor: float) -> Optional[ndf.model.List]:
    if value.type and value.type.lower() == 'float3':
        for row in value:
            try:
                numeric = float(row.v)
            except (TypeError, ValueError):
                return None
            src = (
                _numeric_format_source_text(row.v)
                if isinstance(row.v, (int, float))
                else str(row.v).strip()
            )
            row.v = _format_scaled_from_source_text(numeric * scale_factor, src)
        return value
    return None


def _action_short_from_taction(obj: ndf.model.Object) -> Optional[str]:
    """Short VFX name from ``TActionCall`` (last path segment of ``Action``)."""
    if obj.type != 'TActionCall':
        return None
    for member in obj:
        if member.member == 'Action':
            av = strip_quotes(str(member.v))
            return av.split('/')[-1] if av else None
    return None


def _numeric_value_for_map_value(v: Any) -> Optional[float]:
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        try:
            return float(v.strip())
        except ValueError:
            return None
    return None


def _iter_taction_call_objects(root: Any) -> Iterable[ndf.model.Object]:
    if isinstance(root, ndf.model.Object):
        if root.type == 'TActionCall':
            yield root
        for member in root:
            yield from _iter_taction_call_objects(member.v)
        return
    if isinstance(root, ndf.model.Map):
        for map_row in root:
            yield from _iter_taction_call_objects(map_row.v)
        return
    if isinstance(root, ndf.model.List):
        for row in root:
            yield from _iter_taction_call_objects(row.v)
        return
    if isinstance(root, ndf.model.MemberRow):
        yield from _iter_taction_call_objects(root.v)
        return
    if isinstance(root, ndf.model.ListRow):
        yield from _iter_taction_call_objects(root.v)
        return


def _size_score_from_tactioncall(tact: ndf.model.Object) -> float:
    score = 0.0
    for member in tact:
        if member.member != 'NamedParams' or not isinstance(member.v, ndf.model.Map):
            continue
        for map_row in member.v:
            key_text = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
            if not is_size_param(key_text):
                continue
            nv = _numeric_value_for_map_value(map_row.v)
            if nv is not None:
                score = max(score, abs(nv))
    return score


def compute_tactioncall_count_variant_t(parsed_root: ndf.model.List) -> Dict[int, float]:
    """Map ``id(TActionCall)`` → ``t`` in ``[0, 1]`` (0 = smallest size score for that VFX, 1 = largest)."""
    by_vfx: DefaultDict[str, List[Tuple[ndf.model.Object, float]]] = defaultdict(list)
    for tact in _iter_taction_call_objects(parsed_root):
        vfx = _action_short_from_taction(tact)
        if not vfx:
            continue
        by_vfx[vfx].append((tact, _size_score_from_tactioncall(tact)))
    out: Dict[int, float] = {}
    for _vfx, pairs in by_vfx.items():
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)
        if n == 0:
            continue
        if n == 1:
            out[id(pairs[0][0])] = 1.0
        else:
            for i, (tact, _) in enumerate(pairs):
                out[id(tact)] = i / (n - 1)
    return out


def _variant_t_from_by_vfx(by_vfx: DefaultDict[str, List[Tuple[ndf.model.Object, float]]]) -> Dict[int, float]:
    out: Dict[int, float] = {}
    for _vfx, pairs in by_vfx.items():
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)
        if n == 0:
            continue
        if n == 1:
            out[id(pairs[0][0])] = 1.0
        else:
            for i, (tact, _) in enumerate(pairs):
                out[id(tact)] = i / (n - 1)
    return out


def compute_variant_t_and_collect_taction_rows(
    parsed_root: ndf.model.List,
) -> Tuple[Dict[int, float], Dict[str, List[Tuple[ndf.model.List, ndf.model.ListRow]]]]:
    """One tree walk: same ``variant_t`` as :func:`compute_tactioncall_count_variant_t` (via
    :func:`_iter_taction_call_objects` order) plus :func:`~tools.fx_editor.call_scale._collect_taction_call_rows`
    grouping. ``by_vfx`` scores are recorded only in the ``TActionCall`` object branch to avoid duplicates."""
    rows_by_vfx: Dict[str, List[Tuple[ndf.model.List, ndf.model.ListRow]]] = {}
    by_vfx: DefaultDict[str, List[Tuple[ndf.model.Object, float]]] = defaultdict(list)

    def walk(node: Any) -> None:
        if isinstance(node, ndf.model.Object):
            if node.type == 'TActionCall':
                vfx = _action_short_from_taction(node)
                if vfx:
                    by_vfx[vfx].append((node, _size_score_from_tactioncall(node)))
            for member in node:
                walk(member.v)
            return
        if isinstance(node, ndf.model.Map):
            for map_row in node:
                walk(map_row.v)
            return
        if isinstance(node, ndf.model.List):
            try:
                rows = list(node)
            except Exception:
                return
            for row in rows:
                rv = _list_row_child_v(row)
                if rv is None:
                    continue
                if isinstance(rv, ndf.model.Object) and rv.type == 'TActionCall':
                    vfx = _action_short_from_taction(rv)
                    if vfx:
                        rows_by_vfx.setdefault(vfx, []).append((node, row))
                walk(rv)
            return
        if isinstance(node, ndf.model.MemberRow):
            walk(node.v)
            return
        if isinstance(node, ndf.model.ListRow):
            lr = _list_row_child_v(node)
            if lr is not None:
                walk(lr)
            return

    walk(parsed_root)
    return _variant_t_from_by_vfx(by_vfx), rows_by_vfx


def count_variant_multiplier(
    effect_count_scale_pct: Optional[Dict[str, float]],
    variant_t_by_id: Dict[int, float],
    action_ctx: Optional[str],
    tact: Optional[ndf.model.Object],
) -> float:
    """Extra multiplier for count params: ``1 + (p - 1) * t`` with ``p`` = Param Qty %% as 0–1."""
    if effect_count_scale_pct is None or not action_ctx or tact is None:
        return 1.0
    pct = effect_count_scale_pct.get(action_ctx, 100.0)
    p = max(0.0, min(100.0, float(pct))) / 100.0
    t = variant_t_by_id.get(id(tact), 1.0)
    return 1.0 + (p - 1.0) * t


EffectNamedFlagsMap = Dict[str, Dict[str, bool]]
EffectCountScalePctMap = Dict[str, float]


def effect_named_has_size_keys(keys: Iterable[str]) -> bool:
    """True if any catalog key is a size-type parameter for batch scaling."""
    return any(is_size_param(k) for k in keys)


def effect_named_has_count_keys(keys: Iterable[str]) -> bool:
    """True if any catalog key is a count-type parameter for batch scaling."""
    return any(is_count_param(k) for k in keys)


def _named_param_allowed_for_effect(
    action_context: Optional[str],
    is_size: bool,
    is_count: bool,
    effect_named_flags: Optional[EffectNamedFlagsMap],
    effect_count_scale_pct: Optional[EffectCountScalePctMap] = None,
) -> bool:
    """Per-effect size/count toggles for ``NamedParams``. ``None`` = all effects allowed for both.

    When Param Qty %% is below 100%% for a VFX, count-like params are allowed so the cap can apply
    even when the per-group Count checkbox is off.
    """
    if effect_named_flags is None:
        return True
    if not effect_named_flags:
        return False
    if action_context is None:
        return False
    ef = effect_named_flags.get(action_context)
    if ef is None:
        return False
    if is_size:
        return ef.get('size', True)
    if is_count:
        if effect_count_scale_pct is not None:
            pct = float(effect_count_scale_pct.get(action_context, 100.0))
            if pct < 99.999:
                return True
        return ef.get('count', True)
    return False


def scale_map_row(
    map_row: ndf.model.MapRow,
    scale_factor: float,
    dry_run: bool,
    allowed_names: Optional[Set[str]] = None,
    *,
    action_context: Optional[str] = None,
    effect_named_flags: Optional[EffectNamedFlagsMap] = None,
    effect_count_scale_pct: Optional[EffectCountScalePctMap] = None,
    count_variant_scale: float = 1.0,
    scale_size: bool = True,
    scale_count: bool = True,
) -> Optional[SizeChange]:
    """Scale a MapRow value if it matches size or count parameter patterns.

    ``count_variant_scale`` multiplies the radius scale for **count** params only (Param Qty %%).
    """
    key_text = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
    is_count = is_count_param(key_text)
    is_size = is_size_param(key_text)
    if not is_count and not is_size:
        return None
    if not _named_param_allowed_for_effect(
        action_context,
        is_size,
        is_count,
        effect_named_flags,
        effect_count_scale_pct=effect_count_scale_pct,
    ):
        return None
    if is_size:
        if not scale_size:
            return None
        if not is_size_param_name_allowed(key_text, allowed_names):
            return None

    if is_count:
        if not scale_count and count_variant_scale >= 1.0 - 1e-9:
            return None
        count_sf = scale_factor * count_variant_scale if scale_count else count_variant_scale
    else:
        count_sf = scale_factor

    old_value = map_row.v
    old_value_str = _stringify_value(old_value)

    new_value: Any = None
    new_value_str: Optional[str] = None

    if isinstance(old_value, (int, float)):
        if is_count:
            new_value_str = _format_count_scaled(float(old_value), count_sf, str(old_value))
            new_value = _ndf_scalar_from_scaled_string(new_value_str, prefer_int=True)
        else:
            scaled = float(old_value) * scale_factor
            src_text = _numeric_format_source_text(old_value)
            new_value_str = _format_scaled_from_source_text(scaled, src_text)
            new_value = _ndf_scalar_from_scaled_string(
                new_value_str,
                prefer_int=False,
                fallback_for_size=scaled,
            )
    elif isinstance(old_value, ndf.model.List):
        if is_count:
            return None
        scaled_list = _scale_list_value(old_value, scale_factor)
        if scaled_list is not None:
            new_value = scaled_list
            new_value_str = _stringify_value(new_value)
    elif isinstance(old_value, str):
        if is_count:
            try:
                numeric = float(old_value)
            except ValueError:
                return None
            new_value_str = _format_count_scaled(numeric, count_sf, old_value)
            try:
                parsed = ndf.expression(new_value_str)
                if isinstance(parsed, dict) and 'value' in parsed:
                    new_value = parsed['value']
                else:
                    new_value = int(new_value_str)
            except Exception:
                new_value = int(new_value_str)
        else:
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


def iter_map_rows_with_action_context(
    root: Any,
    current_action: Optional[str] = None,
) -> Iterable[Tuple[ndf.model.MapRow, Optional[str]]]:
    """Yield each ``MapRow`` with the enclosing ``TActionCall`` Action short name (or ``None``)."""
    if isinstance(root, ndf.model.Object):
        ca = current_action
        if root.type == 'TActionCall':
            ca = _action_short_from_taction(root)
        for member in root:
            yield from iter_map_rows_with_action_context(member.v, ca)
        return
    if isinstance(root, ndf.model.Map):
        for map_row in root:
            yield map_row, current_action
            yield from iter_map_rows_with_action_context(map_row.v, current_action)
        return
    if isinstance(root, ndf.model.List):
        for row in root:
            yield from iter_map_rows_with_action_context(row.v, current_action)
        return
    if isinstance(root, ndf.model.MemberRow):
        yield from iter_map_rows_with_action_context(root.v, current_action)
        return
    if isinstance(root, ndf.model.ListRow):
        yield from iter_map_rows_with_action_context(root.v, current_action)
        return


def iter_map_rows_with_action_context_and_taction(
    root: Any,
    current_action: Optional[str] = None,
    enclosing_taction: Optional[ndf.model.Object] = None,
) -> Iterable[Tuple[ndf.model.MapRow, Optional[str], Optional[ndf.model.Object]]]:
    """Like :func:`iter_map_rows_with_action_context` but also yields the enclosing ``TActionCall`` object."""
    if isinstance(root, ndf.model.Object):
        ca = current_action
        tact = enclosing_taction
        if root.type == 'TActionCall':
            ca = _action_short_from_taction(root)
            tact = root
        for member in root:
            yield from iter_map_rows_with_action_context_and_taction(member.v, ca, tact)
        return
    if isinstance(root, ndf.model.Map):
        for map_row in root:
            yield map_row, current_action, enclosing_taction
            yield from iter_map_rows_with_action_context_and_taction(map_row.v, current_action, enclosing_taction)
        return
    if isinstance(root, ndf.model.List):
        for row in root:
            yield from iter_map_rows_with_action_context_and_taction(row.v, current_action, enclosing_taction)
        return
    if isinstance(root, ndf.model.MemberRow):
        yield from iter_map_rows_with_action_context_and_taction(root.v, current_action, enclosing_taction)
        return
    if isinstance(root, ndf.model.ListRow):
        yield from iter_map_rows_with_action_context_and_taction(root.v, current_action, enclosing_taction)
        return


def scale_size_params(
    parsed_root: ndf.model.List,
    scale_factor: float,
    dry_run: bool,
    allowed_names: Optional[Set[str]] = None,
    *,
    scale_size: bool = True,
    scale_count: bool = True,
    include_declaration_params: bool = True,
    effect_named_flags: Optional[EffectNamedFlagsMap] = None,
    effect_count_scale_pct: Optional[EffectCountScalePctMap] = None,
    param_radius_falloff_mult_by_taction_id: Optional[Dict[int, float]] = None,
) -> List[SizeChange]:
    """Scale size- and count-related parameters for a parsed NDF tree (maps + declaration Params).

    ``effect_named_flags`` controls per-VFX ``NamedParams`` rows (size vs count). ``None`` means all
    effects allowed. Declaration ``Params`` use ``scale_size`` / ``scale_count`` only.

    ``effect_count_scale_pct`` maps VFX short names to 0–100. When set, count-type NamedParams
    multiply by an extra factor derived from ``compute_tactioncall_count_variant_t`` (smaller
    size-variant calls interpolate toward 100%; largest variants use the slider %).

    ``param_radius_falloff_mult_by_taction_id`` multiplies count scaling per ``TActionCall`` from
    distance from scatter center / target radius (when set).
    """
    changes: List[SizeChange] = []
    variant_t_by_id: Dict[int, float] = (
        compute_tactioncall_count_variant_t(parsed_root)
        if effect_count_scale_pct is not None
        else {}
    )
    for map_row, action_ctx, tact in iter_map_rows_with_action_context_and_taction(parsed_root):
        cvs = count_variant_multiplier(
            effect_count_scale_pct,
            variant_t_by_id,
            action_ctx,
            tact,
        )
        if param_radius_falloff_mult_by_taction_id is not None and tact is not None:
            rf = float(param_radius_falloff_mult_by_taction_id.get(id(tact), 1.0))
            cvs = cvs * rf
        change = scale_map_row(
            map_row,
            scale_factor,
            dry_run,
            allowed_names,
            action_context=action_ctx,
            effect_named_flags=effect_named_flags,
            effect_count_scale_pct=effect_count_scale_pct,
            count_variant_scale=cvs,
            scale_size=scale_size,
            scale_count=scale_count,
        )
        if change:
            changes.append(change)
    if include_declaration_params:
        for target in iter_param_default_targets(parsed_root):
            change = scale_param_default_member(
                target,
                scale_factor,
                dry_run,
                scale_size=scale_size,
                scale_count=scale_count,
                allowed_names=allowed_names,
            )
            if change:
                changes.append(change)
    return changes


def process_file(
    file_path: Path,
    scale_factor: float,
    dry_run: bool,
    allowed_names: Optional[Set[str]] = None,
    *,
    scale_size: bool = True,
    scale_count: bool = True,
    include_declaration_params: bool = True,
    effect_named_flags: Optional[EffectNamedFlagsMap] = None,
    effect_count_scale_pct: Optional[EffectCountScalePctMap] = None,
    effect_call_scale_pct: Optional[Dict[str, float]] = None,
    effect_call_batch_scale_min: Optional[float] = None,
    effect_call_batch_scale_max: Optional[float] = None,
    param_radius_falloff_by_vfx: Optional[Dict[str, List[float]]] = None,
    call_radius_falloff_by_vfx: Optional[Dict[str, List[float]]] = None,
    target_radius_m: Optional[float] = None,
    ref_m: Optional[float] = None,
    anchor_r: Optional[float] = None,
    burst_gameplay_xy_m: Optional[List[Tuple[float, float]]] = None,
) -> Dict[str, Any]:
    """Process a file and scale size/count parameters."""
    from .call_scale import scale_effect_calls

    stats: Dict[str, Any] = {
        'file': str(file_path),
        'changes': [],
        'call_changes': [],
        'error': None,
    }
    try:
        with open(file_path, 'r', encoding='utf-8') as handle:
            content = handle.read()
        parsed = ndf.convert(content)
        if not isinstance(parsed, ndf.model.List):
            raise ValueError(f'Expected ndf.model.List, got {type(parsed).__name__}')
        stats['vfx_burst_denoms'] = vfx_effect_group_burst_counts(parsed)
        call_changes = scale_effect_calls(
            parsed,
            effect_call_scale_pct,
            dry_run=dry_run,
            scale_factor=scale_factor,
            effect_call_batch_scale_min=effect_call_batch_scale_min,
            effect_call_batch_scale_max=effect_call_batch_scale_max,
            call_radius_falloff_by_vfx=call_radius_falloff_by_vfx,
            target_radius_m=target_radius_m,
            ref_m=ref_m,
            anchor_r=anchor_r,
            burst_gameplay_xy_m=burst_gameplay_xy_m,
        )
        stats['call_changes'] = call_changes
        param_mults: Optional[Dict[int, float]] = None
        if (
            param_radius_falloff_by_vfx is not None
            and len(param_radius_falloff_by_vfx) > 0
            and target_radius_m is not None
            and ref_m is not None
            and anchor_r is not None
        ):
            from .radius_falloff import burst_gameplay_xy_m_from_parsed_root, taction_radius_falloff_multipliers

            param_burst_xy = burst_gameplay_xy_m_from_parsed_root(
                parsed,
                float(ref_m),
                float(anchor_r),
            )
            param_mults = taction_radius_falloff_multipliers(
                parsed,
                float(target_radius_m),
                param_radius_falloff_by_vfx,
                float(ref_m),
                float(anchor_r),
                burst_gameplay_xy_m=param_burst_xy,
                log_label='param',
            )
        changes = scale_size_params(
            parsed,
            scale_factor,
            dry_run,
            allowed_names,
            scale_size=scale_size,
            scale_count=scale_count,
            include_declaration_params=include_declaration_params,
            effect_named_flags=effect_named_flags,
            effect_count_scale_pct=effect_count_scale_pct,
            param_radius_falloff_mult_by_taction_id=param_mults,
        )
        stats['changes'] = changes
        if not dry_run and (call_changes or changes):
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


# --- Batch size variations (scaled copies with custom names) ------------------------------------

STEM_TRAILING_INDEX_RE = re.compile(r'_(\d+)$')


def extract_trailing_index_suffix(stem: str) -> Tuple[str, str, str]:
    """Split stem into base, trailing '_N' suffix, and numeric part.

    Returns:
        (stem_without_suffix, suffix_with_underscore, number_only)
        If no trailing ``_digits`` pattern, suffix and number are empty strings.
    """
    match = STEM_TRAILING_INDEX_RE.search(stem)
    if not match:
        return stem, '', ''
    start = match.start()
    return stem[:start], match.group(0), match.group(1)


# Default for fx_editor batch “size variations”: stem includes target effect radius (m).
DEFAULT_VARIATION_FILENAME_TEMPLATE = '{rootname}_r{radiusinmeters}m_{n}.ndf'


def format_radius_meters_for_name(radius_m: float) -> str:
    """Format an effect-radius value in meters for filenames (no trailing .0 for integers)."""
    if abs(radius_m - round(radius_m)) < 1e-9:
        return str(int(round(radius_m)))
    return _format_number(radius_m)


def render_variation_filename(
    template: str,
    rootname: str,
    radius_m: float,
    source_stem: str,
) -> str:
    """Fill ``{rootname}``, ``{radiusinmeters}``, ``{suffix}``, ``{n}`` in template.

    ``radius_m`` is the target **effect radius** in meters (same value used in scaling).

    ``{suffix}`` is the trailing ``_1``-style segment from ``source_stem`` (or empty).
    ``{n}`` is the numeric part only (``1``, ``2``, …) or empty if absent.
    """
    _, suffix_underscore, n = extract_trailing_index_suffix(source_stem)
    r_str = format_radius_meters_for_name(radius_m)
    result = template
    result = result.replace('{rootname}', rootname)
    result = result.replace('{radiusinmeters}', r_str)
    result = result.replace('{suffix}', suffix_underscore)
    result = result.replace('{n}', n)
    return result


def parse_target_sizes(text: str) -> List[float]:
    """Parse comma/newline/semicolon-separated target radii in meters."""
    sizes: List[float] = []
    for raw in re.split(r'[\s,;]+', text.strip()):
        if not raw:
            continue
        try:
            sizes.append(float(raw))
        except ValueError:
            continue
    return sizes


def effect_call_batch_scale_bounds(source_m: float, targets_text: str) -> Tuple[float, float]:
    """Min/max ``target_m / source_m`` from the batch target radii field (for Call Qty %% easing)."""
    if source_m <= 0:
        return (1.0, 1.0)
    targets = parse_target_sizes(targets_text)
    if not targets:
        return (1.0, 1.0)
    sfs = [t / source_m for t in targets]
    return (min(sfs), max(sfs))


def _walk_collect_taction_named_params(root: Any, merged: DefaultDict[str, Set[str]]) -> None:
    """Merge TActionCall Action short names with NamedParams keys from ``root``."""
    if isinstance(root, ndf.model.Object):
        if root.type == 'TActionCall':
            action_short = ''
            for member in root:
                if member.member == 'Action':
                    av = strip_quotes(str(member.v))
                    action_short = av.split('/')[-1] if av else ''
                    break
            if action_short:
                for member in root:
                    if member.member == 'NamedParams' and isinstance(member.v, ndf.model.Map):
                        for map_row in member.v:
                            kt = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
                            if kt:
                                merged[action_short].add(kt)
        for member in root:
            _walk_collect_taction_named_params(member.v, merged)
        return
    if isinstance(root, ndf.model.Map):
        for map_row in root:
            _walk_collect_taction_named_params(map_row.v, merged)
        return
    if isinstance(root, ndf.model.List):
        for row in root:
            _walk_collect_taction_named_params(row.v, merged)
        return
    if isinstance(root, ndf.model.MemberRow):
        _walk_collect_taction_named_params(root.v, merged)
        return
    if isinstance(root, ndf.model.ListRow):
        _walk_collect_taction_named_params(root.v, merged)
        return


def collect_fx_parameter_catalog(paths: List[Path]) -> Tuple[Dict[str, List[str]], List[str]]:
    """Per-VFX named param keys and declaration ``Params`` alias names from ``paths``."""
    merged: DefaultDict[str, Set[str]] = defaultdict(set)
    decl: Set[str] = set()
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as handle:
                content = handle.read()
            parsed = ndf.convert(content)
            if not isinstance(parsed, ndf.model.List):
                continue
            for t in iter_param_default_targets(parsed):
                decl.add(t.param_name)
            _walk_collect_taction_named_params(parsed, merged)
        except Exception:
            continue
    return {k: sorted(v) for k, v in sorted(merged.items())}, sorted(decl)


def collect_size_param_keys_in_files(paths: List[Path]) -> List[str]:
    """Unique map keys in ``paths`` that match size-parameter patterns (sorted)."""
    found: Set[str] = set()
    for path in paths:
        try:
            with open(path, 'r', encoding='utf-8') as handle:
                content = handle.read()
            parsed = ndf.convert(content)
            if not isinstance(parsed, ndf.model.List):
                continue
            for map_row in iter_map_rows(parsed):
                key_text = strip_quotes(str(map_row.k)) if map_row.k is not None else ''
                if is_size_param(key_text):
                    found.add(key_text)
        except Exception:
            continue
    return sorted(found)


def write_scaled_copy(
    file_path: Path,
    dest_path: Path,
    scale_factor: float,
    allowed_names: Optional[Set[str]] = None,
    *,
    scale_size: bool = True,
    scale_count: bool = True,
    include_declaration_params: bool = True,
    effect_named_flags: Optional[EffectNamedFlagsMap] = None,
    effect_count_scale_pct: Optional[EffectCountScalePctMap] = None,
    effect_call_scale_pct: Optional[Dict[str, float]] = None,
    effect_call_batch_scale_min: Optional[float] = None,
    effect_call_batch_scale_max: Optional[float] = None,
    param_radius_falloff_by_vfx: Optional[Dict[str, List[float]]] = None,
    call_radius_falloff_by_vfx: Optional[Dict[str, List[float]]] = None,
    target_radius_m: Optional[float] = None,
    ref_m: Optional[float] = None,
    anchor_r: Optional[float] = None,
    burst_gameplay_xy_m: Optional[List[Tuple[float, float]]] = None,
) -> Dict[str, Any]:
    """Read ``file_path``, scale size/count params, set export namespace to ``dest_path`` stem, write."""
    from .call_scale import scale_effect_calls

    stats: Dict[str, Any] = {
        'file': str(file_path),
        'dest': str(dest_path),
        'changes': [],
        'call_changes': [],
        'error': None,
    }
    try:
        with open(file_path, 'r', encoding='utf-8') as handle:
            content = handle.read()
        parsed = ndf.convert(content)
        if not isinstance(parsed, ndf.model.List):
            raise ValueError(f'Expected ndf.model.List, got {type(parsed).__name__}')
        stats['vfx_burst_denoms'] = vfx_effect_group_burst_counts(parsed)
        call_changes = scale_effect_calls(
            parsed,
            effect_call_scale_pct,
            dry_run=False,
            scale_factor=scale_factor,
            effect_call_batch_scale_min=effect_call_batch_scale_min,
            effect_call_batch_scale_max=effect_call_batch_scale_max,
            call_radius_falloff_by_vfx=call_radius_falloff_by_vfx,
            target_radius_m=target_radius_m,
            ref_m=ref_m,
            anchor_r=anchor_r,
            burst_gameplay_xy_m=burst_gameplay_xy_m,
        )
        stats['call_changes'] = call_changes
        param_mults: Optional[Dict[int, float]] = None
        if (
            param_radius_falloff_by_vfx is not None
            and len(param_radius_falloff_by_vfx) > 0
            and target_radius_m is not None
            and ref_m is not None
            and anchor_r is not None
        ):
            from .radius_falloff import burst_gameplay_xy_m_from_parsed_root, taction_radius_falloff_multipliers

            param_burst_xy = burst_gameplay_xy_m_from_parsed_root(
                parsed,
                float(ref_m),
                float(anchor_r),
            )
            param_mults = taction_radius_falloff_multipliers(
                parsed,
                float(target_radius_m),
                param_radius_falloff_by_vfx,
                float(ref_m),
                float(anchor_r),
                burst_gameplay_xy_m=param_burst_xy,
                log_label='param',
            )
        changes = scale_size_params(
            parsed,
            scale_factor,
            dry_run=False,
            allowed_names=allowed_names,
            scale_size=scale_size,
            scale_count=scale_count,
            include_declaration_params=include_declaration_params,
            effect_named_flags=effect_named_flags,
            effect_count_scale_pct=effect_count_scale_pct,
            param_radius_falloff_mult_by_taction_id=param_mults,
        )
        stats['changes'] = changes
        update_namespace(parsed, dest_path.stem)
        formatted = ndf.printer.string(parsed)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dest_path, 'w', encoding='utf-8') as handle:
            handle.write(formatted)
    except Exception as exc:
        stats['error'] = str(exc)
    return stats
