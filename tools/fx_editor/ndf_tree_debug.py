"""Locate invalid NDF tree state after mutations (validation / printer failures)."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, List

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src import ndf


def describe_first_list_row_access_errors(root: Any, max_errors: int = 5) -> str:
    """Walk the tree and report the first failing ``ListRow.v`` or ``list(List)`` accesses."""
    errors: List[str] = []

    def walk(path: str, n: Any) -> None:
        if len(errors) >= max_errors:
            return
        if isinstance(n, ndf.model.Object):
            for member in n:
                walk(f'{path}/{member.member}', member.v)
            return
        if isinstance(n, ndf.model.Map):
            for mr in n:
                try:
                    walk(f'{path}/{getattr(mr, "k", "?")}', mr.v)
                except Exception as exc:
                    errors.append(f'MapRow@{path}: {exc}')
            return
        if isinstance(n, ndf.model.List):
            try:
                rows = list(n)
            except Exception as exc:
                errors.append(f'List@{path}: list() failed: {exc}')
                return
            for i, row in enumerate(rows):
                try:
                    v = row.v
                except Exception as exc:
                    errors.append(f'ListRow[{i}]@{path}: row.v: {exc}')
                    continue
                walk(f'{path}[{i}]', v)
            return
        if isinstance(n, ndf.model.MemberRow):
            walk(path, n.v)
            return
        if isinstance(n, ndf.model.ListRow):
            try:
                vv = n.v
            except Exception as exc:
                errors.append(f'ListRow@{path}: {exc}')
                return
            walk(f'{path}/v', vv)
            return

    walk('root', root)
    if not errors:
        return ''
    return 'Tree access diagnostics (first failures):\n' + '\n'.join(errors)


def _raw_float_in_row_v_report(root: Any, max_errors: int = 8) -> str:
    """Detect ListRow/MapRow with ``__dict__['v']`` a bare float (invalid for NDF Row typing)."""
    errors: List[str] = []

    def check_row(path: str, row: Any, label: str, idx: int) -> None:
        if len(errors) >= max_errors:
            return
        if not isinstance(row, (ndf.model.ListRow, ndf.model.MapRow)):
            return
        d = getattr(row, '__dict__', None)
        if not isinstance(d, dict) or 'v' not in d:
            return
        vv = d['v']
        if isinstance(vv, float) and not isinstance(vv, bool):
            errors.append(f'{label}[{idx}]@{path}: __dict__ v is float {vv!r}')

    def walk(path: str, n: Any) -> None:
        if len(errors) >= max_errors:
            return
        if isinstance(n, ndf.model.Object):
            for member in n:
                walk(f'{path}/{member.member}', member.v)
            return
        if isinstance(n, ndf.model.Map):
            try:
                mrows = list(n)
            except Exception:
                return
            for j, mr in enumerate(mrows):
                check_row(path, mr, 'MapRow', j)
                try:
                    walk(f'{path}/MapRow[{j}]', mr.v)
                except Exception as exc:
                    errors.append(f'MapRow[{j}]@{path}: mr.v access: {exc}')
            return
        if isinstance(n, ndf.model.List):
            try:
                rows = list(n)
            except Exception:
                return
            for i, row in enumerate(rows):
                check_row(path, row, 'ListRow', i)
                try:
                    v = row.v
                except Exception:
                    continue
                walk(f'{path}[{i}]', v)
            return
        if isinstance(n, ndf.model.MemberRow):
            walk(path, n.v)
            return
        if isinstance(n, ndf.model.ListRow):
            try:
                vv = n.v
            except Exception:
                return
            walk(f'{path}/v', vv)
            return

    walk('root', root)
    if not errors:
        return ''
    return 'Raw __dict__ scan (suspect float in Row.v):\n' + '\n'.join(errors)


def describe_ndf_tree_issues(root: Any, max_errors: int = 8) -> str:
    """Printer probe, property-access walk, and raw-float Row scan."""
    parts: List[str] = []
    try:
        ndf.printer.string(root)
    except Exception as exc:
        parts.append(f'ndf.printer.string(root) failed: {exc}')
    acc = describe_first_list_row_access_errors(root, max_errors=max_errors)
    if acc:
        parts.append(acc)
    raw = _raw_float_in_row_v_report(root, max_errors=max_errors)
    if raw:
        parts.append(raw)
    return '\n\n'.join(parts)
