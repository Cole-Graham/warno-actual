"""Fix infantry magazine migration replace warnings.

1. Fold donor->target + target->target_salvolength into donor->target_salvolength
2. Drop bare->magazine remount-only replaces (remount handler / LIGHT_AT cover these)
3. Drop list-form replace blocks that are only bare->magazine remounts

Does not touch vehicle salvo changes where the old name already has a magazine suffix.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from src.data.infantry_magazine_salvo import is_infantry_magazine_category

REPO = Path(__file__).resolve().parents[1]
EDIT_DIRS = [
    REPO / "src" / "constants" / "unit_edits",
    REPO / "src" / "constants" / "new_units",
]

_MAG_SUFFIX = re.compile(r"_(?:salvolength|infmagazine)\d+$")


def _is_bare_to_magazine(old: str, new: str) -> bool:
    """True for infantry AT/AA remount-only replaces (bare -> same ammo magazine)."""
    if _MAG_SUFFIX.search(old):
        return False
    if not _MAG_SUFFIX.search(new):
        return False
    if _MAG_SUFFIX.sub("", new) != old:
        return False
    return is_infantry_magazine_category(old)


def _remove_list_magazine_replaces(text: str) -> Tuple[str, int]:
    """Remove ``\"replace\": [ (bare, bare_salvolengthN), ... ]`` blocks that are remount-only."""
    pattern = re.compile(
        r'^([ \t]*)"replace":\s*\[(.*?)\]\s*,?\s*\n',
        re.MULTILINE | re.DOTALL,
    )
    removed = 0

    def repl(match: re.Match) -> str:
        nonlocal removed
        indent, body = match.group(1), match.group(2)
        tuples = re.findall(
            r'\(\s*["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']\s*\)',
            body,
        )
        if not tuples:
            return match.group(0)
        # Keep any non remount-only pairs
        keep = [(a, b) for a, b in tuples if not _is_bare_to_magazine(a, b)]
        dropped = len(tuples) - len(keep)
        if dropped == 0:
            return match.group(0)
        removed += dropped
        if not keep:
            return ""
        lines = [f'{indent}"replace": [']
        for a, b in keep:
            lines.append(f'{indent}    ("{a}", "{b}"),')
        lines.append(f"{indent}],")
        return "\n".join(lines) + "\n"

    return pattern.sub(repl, text), removed


def _extract_dict_entries(body: str) -> List[Tuple[str, str, str]]:
    """Return list of (old_weapon, entry_text, new_weapon) for top-level replace dict entries."""
    entries: List[Tuple[str, str, str]] = []
    # Match "Old": { ... },  with balanced braces
    i = 0
    while i < len(body):
        m = re.match(r'\s*(["\'])([^"\']+)\1\s*:\s*\{', body[i:])
        if not m:
            # skip whitespace / comments-ish
            if body[i] in " \t\n\r,":
                i += 1
                continue
            break
        quote, old = m.group(1), m.group(2)
        start = i + m.end() - 1  # at '{'
        depth = 0
        j = start
        while j < len(body):
            ch = body[j]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    j += 1
                    break
            j += 1
        entry_inner = body[start:j]  # includes { ... }
        # trailing comma
        k = j
        while k < len(body) and body[k] in " \t":
            k += 1
        if k < len(body) and body[k] == ",":
            k += 1
        while k < len(body) and body[k] in " \t":
            k += 1
        if k < len(body) and body[k] == "\n":
            k += 1
        full_entry = body[i:k]
        nw = re.search(r'"new_weapon"\s*:\s*"([^"]+)"', entry_inner)
        new_weapon = nw.group(1) if nw else ""
        entries.append((old, full_entry, new_weapon))
        i = k
    return entries


def _rewrite_replace_dicts(text: str) -> Tuple[str, int, int]:
    """Fold and drop bare->magazine remount entries inside dict-form replace blocks."""
    dropped = 0
    folded = 0
    out: List[str] = []
    i = 0
    key_re = re.compile(r'^([ \t]*)"replace":\s*\{', re.MULTILINE)

    while True:
        m = key_re.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i:m.start()])
        indent = m.group(1)
        brace_start = m.end() - 1  # '{'
        depth = 0
        j = brace_start
        while j < len(text):
            ch = text[j]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    j += 1
                    break
            j += 1
        body = text[brace_start + 1 : j - 1]
        # trailing comma / whitespace / newline after closing brace
        k = j
        while k < len(text) and text[k] in " \t":
            k += 1
        if k < len(text) and text[k] == ",":
            k += 1
        while k < len(text) and text[k] in " \t":
            k += 1
        if k < len(text) and text[k] == "\n":
            k += 1

        entries = _extract_dict_entries(body)
        if not entries:
            out.append(text[m.start():k])
            i = k
            continue

        remounts: Dict[str, str] = {}
        for old, _entry, new in entries:
            if new and _is_bare_to_magazine(old, new):
                remounts[old] = new

        new_entries: List[str] = []
        for old, entry, new in entries:
            if new and _is_bare_to_magazine(old, new):
                dropped += 1
                continue
            if new and new in remounts:
                variant = remounts[new]
                updated = re.sub(
                    r'("new_weapon"\s*:\s*")' + re.escape(new) + r'(")',
                    r"\g<1>" + variant + r"\2",
                    entry,
                    count=1,
                )
                if updated != entry:
                    folded += 1
                    entry = updated
            entry = entry.rstrip()
            if not entry.endswith(","):
                entry = re.sub(r"(\})(\s*)$", r"\1,\2", entry)
            new_entries.append(entry + "\n")

        if not new_entries:
            i = k
            continue

        block = f'{indent}"replace": {{\n'
        for entry in new_entries:
            block += entry
        block += f"{indent}}},\n"
        out.append(block)
        i = k

    return "".join(out), dropped, folded


def fix_file(path: Path) -> Dict[str, int]:
    original = path.read_text(encoding="utf-8")
    text, list_removed = _remove_list_magazine_replaces(original)
    text, dropped, folded = _rewrite_replace_dicts(text)
    if text != original:
        path.write_text(text, encoding="utf-8")
    return {
        "list_removed": list_removed,
        "dict_dropped": dropped,
        "dict_folded": folded,
        "changed": int(text != original),
    }


def main() -> None:
    totals = {"list_removed": 0, "dict_dropped": 0, "dict_folded": 0, "files": 0}
    for directory in EDIT_DIRS:
        for path in sorted(directory.glob("*_unit_edits.py")) + sorted(directory.glob("*_new_units.py")):
            stats = fix_file(path)
            if stats["changed"]:
                totals["files"] += 1
                print(
                    f"{path.relative_to(REPO)}: "
                    f"list_removed={stats['list_removed']} "
                    f"dict_dropped={stats['dict_dropped']} "
                    f"dict_folded={stats['dict_folded']}"
                )
            totals["list_removed"] += stats["list_removed"]
            totals["dict_dropped"] += stats["dict_dropped"]
            totals["dict_folded"] += stats["dict_folded"]
    print(
        f"Done. files={totals['files']} list_removed={totals['list_removed']} "
        f"dict_dropped={totals['dict_dropped']} dict_folded={totals['dict_folded']}"
    )


if __name__ == "__main__":
    main()
