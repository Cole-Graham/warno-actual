"""Detect duplicate keys in unit_edits / new_units dict literals via AST.

Python keeps only the last value when a dict literal repeats a key. That cannot be
detected after import; this module scans source files before loaders merge data.

Exemptions (dict blocks where duplicate literal keys are allowed):
- ``Salves`` under ``WeaponDescriptor``: authors may repeat an ammo name when the
  donor has multiple mounts of that weapon; one salvo value applies to every index
  in ``salvo_mapping`` (duplicate keys with the same value are redundant but OK).

Not exempt: ``equipmentchanges.replace`` (use a list under one old-weapon key per
``replace_schema.py``), ``quantity``, unit-level fields, etc. A repo scan found
duplicate keys only under ``Salves`` aside from real bugs (e.g. two ``WeaponDescriptor``
blocks, two ``ECM``, duplicate ``replace`` entries).
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

# Dict levels at which duplicate literal keys are not reported (see module docstring).
_DUPLICATE_KEY_EXEMPT_BLOCK_KEYS = frozenset({"Salves"})


def _unquote_path_segment(segment: str) -> str:
    if len(segment) >= 2 and segment[0] == segment[-1] and segment[0] in ("'", '"'):
        return segment[1:-1]
    return segment


def _skip_duplicate_check_for_dict_level(path_parts: list[str]) -> bool:
    """True when *path_parts* identifies an exempt dict block (e.g. Salves body)."""
    if not path_parts:
        return False
    return _unquote_path_segment(path_parts[-1]) in _DUPLICATE_KEY_EXEMPT_BLOCK_KEYS


@dataclass(frozen=True)
class DuplicateKeyFinding:
    """A duplicate key inside one dict literal block in a source file."""

    file_stem: str
    path: str
    key_repr: str
    first_line: int
    duplicate_line: int


def _literal_key(key_node: ast.expr | None) -> str | int | tuple[Any, ...] | None:
    if key_node is None:
        return None
    if isinstance(key_node, ast.Constant):
        if isinstance(key_node.value, (str, int)):
            return key_node.value
        return None
    if isinstance(key_node, ast.Tuple):
        parts: list[Any] = []
        for elt in key_node.elts:
            if not isinstance(elt, ast.Constant) or not isinstance(elt.value, (str, int)):
                return None
            parts.append(elt.value)
        return tuple(parts)
    return None


def _format_key(key: str | int | tuple[Any, ...]) -> str:
    if isinstance(key, tuple):
        inner = ", ".join(repr(part) for part in key)
        return f"({inner})"
    return repr(key)


def _context_for_message(path_parts: list[str]) -> str:
    if len(path_parts) <= 1:
        return path_parts[0] if path_parts else "top level"
    return " -> ".join(path_parts[:-1])


def _duplicate_keys_in_dict(
    dict_node: ast.Dict,
    path_parts: list[str],
    file_stem: str,
    findings: list[DuplicateKeyFinding],
) -> None:
    check_duplicates = not _skip_duplicate_check_for_dict_level(path_parts)
    seen: dict[Any, int] = {}
    for key_node, value_node in zip(dict_node.keys, dict_node.values):
        lk = _literal_key(key_node)
        if lk is not None:
            key_fmt = _format_key(lk)
            sub_path = path_parts + [key_fmt]
            if check_duplicates:
                if lk in seen:
                    findings.append(
                        DuplicateKeyFinding(
                            file_stem=file_stem,
                            path=" -> ".join(sub_path),
                            key_repr=key_fmt,
                            first_line=seen[lk],
                            duplicate_line=key_node.lineno,
                        ),
                    )
                else:
                    seen[lk] = key_node.lineno
            if isinstance(value_node, ast.Dict):
                _duplicate_keys_in_dict(value_node, sub_path, file_stem, findings)
        elif isinstance(value_node, ast.Dict):
            _duplicate_keys_in_dict(value_node, path_parts, file_stem, findings)


def _findings_in_module_dict(assign: ast.Assign, file_stem: str) -> list[DuplicateKeyFinding]:
    if not isinstance(assign.value, ast.Dict):
        return []
    findings: list[DuplicateKeyFinding] = []
    root = assign.value
    seen_top: dict[Any, int] = {}
    for key_node, value_node in zip(root.keys, root.values):
        lk = _literal_key(key_node)
        if lk is not None:
            key_fmt = _format_key(lk)
            if lk in seen_top:
                findings.append(
                    DuplicateKeyFinding(
                        file_stem=file_stem,
                        path=key_fmt,
                        key_repr=key_fmt,
                        first_line=seen_top[lk],
                        duplicate_line=key_node.lineno,
                    ),
                )
            else:
                seen_top[lk] = key_node.lineno
            if isinstance(value_node, ast.Dict):
                _duplicate_keys_in_dict(value_node, [key_fmt], file_stem, findings)
        elif isinstance(value_node, ast.Dict):
            _duplicate_keys_in_dict(value_node, [], file_stem, findings)
    return findings


def find_duplicate_keys_in_file(path: Path) -> list[DuplicateKeyFinding]:
    """Return duplicate-key findings for module-level dict assignments in *path*."""
    file_stem = path.stem
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as e:
        logger.error(f"Syntax error in {file_stem}, skipping duplicate-key check: {e}")
        return []

    findings: list[DuplicateKeyFinding] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            findings.extend(_findings_in_module_dict(node, file_stem))
    return findings


def _log_finding(finding: DuplicateKeyFinding) -> None:
    path_parts = finding.path.split(" -> ")
    context = _context_for_message(path_parts)
    logger.error(
        f"Duplicate key {finding.key_repr} in {finding.file_stem}.py at {context} "
        f"(first line {finding.first_line}, duplicate line {finding.duplicate_line}). "
        f"Python keeps the last value only.",
    )


def validate_dict_literal_files(
    files: Iterable[Path],
    *,
    label: str,
) -> int:
    """Scan dict-literal source files and log ERROR for each duplicate key.

    Returns the total number of duplicate-key findings.
    """
    total = 0
    for path in sorted(files):
        if path.name == "__init__.py":
            continue
        for finding in find_duplicate_keys_in_file(path):
            _log_finding(finding)
            total += 1
    if total:
        logger.error(f"{total} duplicate key(s) in {label} source files")
    else:
        logger.info(f"No duplicate keys in {label} source files")
    return total
