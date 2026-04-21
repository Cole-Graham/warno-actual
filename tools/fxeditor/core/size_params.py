"""Scale size- and count-related named params with scale-down floors."""

from __future__ import annotations

import re
from typing import Any, Iterable, List, Optional, Set, Tuple

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .ndf_io import _list_row_child_v, find_actions_list

SIZE_PARAM_PATTERNS = [
    r"parSize\b", r"parSize1\b", r"parSize2\b",
    r"parFinalSize\b", r"parInitialSize\b", r"parStartSize\b", r"parEndSize\b",
    r"parDustSize\b", r"parMudSize\b", r"parParticleSize\b",
    r"parFireParticleStartSize\b", r"parFireParticleEndSize\b",
    r"parSmokeParticleStartSize\b", r"parSmokeParticleEndSize\b",
    r"parSizeLBU\b", r"parRadius\b", r"parRadiusPhysical\b",
    r"parRadiusSuppress\b", r"parPositionRadius\b", r"parSpawnRadius\b",
    r"parStartRandomRadius\b", r"parRandomInitPosRadius\b",
    r"parScaleSizeFactor\b", r"parDebritSizeMul\b",
    r"parHeight\b", r"parCloudsize\b", r"parDispersion\b",
]

SIZE_PARAM_RE = re.compile(r"(" + "|".join(SIZE_PARAM_PATTERNS) + r")", re.IGNORECASE)

COUNT_PARAM_PATTERNS = [
    r"parCount\b",
    r"parCountDebrits\b",
    r"parCountDebritsWithFire\b",
]

COUNT_PARAM_RE = re.compile(r"(" + "|".join(COUNT_PARAM_PATTERNS) + r")", re.IGNORECASE)


def is_size_param(name: str) -> bool:
    return bool(SIZE_PARAM_RE.search(name))


def is_count_param(name: str) -> bool:
    return bool(COUNT_PARAM_RE.search(name))


def _format_scaled(value: float, source_text: str) -> str:
    s = source_text.strip()
    if re.match(r"^-?\d+$", s):
        return str(int(round(value)))
    m = re.match(r"^(-?\d+)\.(\d*)$", s)
    if m:
        frac = m.group(2)
        if not frac or re.match(r"^0+$", frac):
            return str(int(round(value)))
        places = len(frac)
        rounded = round(value, places)
        fmt = f"{rounded:.{places}f}"
        return fmt.rstrip("0").rstrip(".") if "." in fmt else fmt
    try:
        float(s)
        if float(s) == int(float(s)):
            return str(int(round(value)))
    except ValueError:
        pass
    if value == int(value):
        return str(int(value))
    return str(value)


def scale_size_params(
    parsed_root: ndf.model.List,
    scale_factor: float,
    *,
    min_size_ratio: float = 0.3,
    min_count_value: int = 1,
    allowed_size_names: Optional[Set[str]] = None,
    scale_counts_enabled: bool = True,
) -> int:
    """Scale size/count named params in-place. Returns number of changes.

    When *allowed_size_names* is an empty set, no size params are scaled.
    When *scale_counts_enabled* is False, count params are skipped.
    """
    changes = 0
    sf = float(scale_factor)

    def _allowed(key: str) -> bool:
        if allowed_size_names is None:
            return True
        if not allowed_size_names:
            return False
        return any(a.lower() == key.lower() for a in allowed_size_names)

    def walk(node: Any) -> None:
        nonlocal changes
        if isinstance(node, ndf.model.Object):
            if node.type == "TActionCall":
                for member in node:
                    if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
                        continue
                    for mr in member.v:
                        key = strip_quotes(str(mr.k)) if mr.k is not None else ""
                        if is_size_param(key) and _allowed(key):
                            _scale_map_value(mr, sf, is_count=False, min_size_ratio=min_size_ratio)
                            changes += 1
                        elif is_count_param(key) and scale_counts_enabled:
                            _scale_map_value(mr, sf, is_count=True, min_count=min_count_value)
                            changes += 1
            for member in node:
                walk(member.v)
        elif isinstance(node, ndf.model.List):
            for row in node:
                walk(row.v)
        elif isinstance(node, ndf.model.MemberRow):
            walk(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                walk(mr.v)
        elif isinstance(node, ndf.model.ListRow):
            walk(node.v)

    walk(parsed_root)

    changes += _scale_declaration_params(
        parsed_root, sf, min_size_ratio, min_count_value,
        allowed_size_names, scale_counts_enabled,
    )
    return changes


def _scale_map_value(
    mr: Any,
    sf: float,
    *,
    is_count: bool,
    min_size_ratio: float = 0.3,
    min_count: int = 1,
) -> None:
    old = mr.v
    if isinstance(old, (int, float)):
        if is_count:
            new_val = max(min_count, int(round(float(old) * sf)))
            mr.v = new_val
        else:
            scaled = float(old) * sf
            floored = max(float(old) * min_size_ratio, scaled) if sf < 1.0 else scaled
            src = str(int(old)) if isinstance(old, int) else str(old)
            mr.v = _try_parse_ndf_scalar(_format_scaled(floored, src))
    elif isinstance(old, str):
        try:
            numeric = float(old.strip())
        except ValueError:
            return
        if is_count:
            new_val = max(min_count, int(round(numeric * sf)))
            mr.v = str(new_val)
        else:
            scaled = numeric * sf
            floored = max(numeric * min_size_ratio, scaled) if sf < 1.0 else scaled
            mr.v = _format_scaled(floored, old)


def _try_parse_ndf_scalar(text: str) -> Any:
    try:
        parsed = ndf.expression(text)
        if isinstance(parsed, dict) and "value" in parsed:
            return parsed["value"]
    except Exception:
        pass
    try:
        if re.match(r"^-?\d+$", text.strip()):
            return int(text.strip())
        return float(text)
    except ValueError:
        return text


def _scale_declaration_params(
    parsed_root: ndf.model.List,
    sf: float,
    min_size_ratio: float,
    min_count: int,
    allowed_names: Optional[Set[str]],
    scale_counts_enabled: bool = True,
) -> int:
    changes = 0
    for top in parsed_root:
        if not isinstance(top, ndf.model.ListRow):
            continue
        obj = top.v
        if not isinstance(obj, ndf.model.Object):
            continue
        for member in obj:
            if member.member != "Params" or not isinstance(member.v, ndf.model.List):
                continue
            for alias_row in member.v:
                if not isinstance(alias_row, ndf.model.ListRow):
                    continue
                ns = strip_quotes(str(alias_row.namespace or "")).strip()
                if " is " in ns:
                    ns = ns.split(" is ")[0].strip()
                if ns.startswith("private "):
                    ns = ns[8:].strip()
                if not isinstance(alias_row.v, ndf.model.Object):
                    continue
                for m in alias_row.v:
                    if not isinstance(m, ndf.model.MemberRow) or m.member != "DefaultValue":
                        continue
                    if is_size_param(ns):
                        if allowed_names is not None and not any(a.lower() == ns.lower() for a in allowed_names):
                            continue
                        _scale_map_value(m, sf, is_count=False, min_size_ratio=min_size_ratio)
                        changes += 1
                    elif is_count_param(ns) and scale_counts_enabled:
                        _scale_map_value(m, sf, is_count=True, min_count=min_count)
                        changes += 1
    return changes
