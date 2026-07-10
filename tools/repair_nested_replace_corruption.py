"""Repair replace dicts corrupted by nested sibling entries (missing closing braces).

Also folds donor->target with nested target->target_salvolength into one replace,
and drops bare->magazine remount-only siblings (remount handler covers those).
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Tuple

from src.data.infantry_magazine_salvo import is_infantry_magazine_category

REPO = Path(__file__).resolve().parents[1]
_MAG = re.compile(r"_(?:salvolength|infmagazine)\d+$")


def _is_bare_to_magazine(old: str, new: str) -> bool:
    if _MAG.search(old) or not _MAG.search(new):
        return False
    if _MAG.sub("", new) != old:
        return False
    return is_infantry_magazine_category(old)


def _extract_entries(body: str) -> List[Tuple[str, str, str]]:
    """Return (old_weapon, full_entry_text, new_weapon) for top-level entries."""
    entries: List[Tuple[str, str, str]] = []
    i = 0
    while i < len(body):
        m = re.match(r'\s*(["\'])([^"\']+)\1\s*:\s*\{', body[i:])
        if not m:
            if body[i] in " \t\n\r,":
                i += 1
                continue
            break
        old = m.group(2)
        start = i + m.end() - 1
        depth = 0
        j = start
        while j < len(body):
            if body[j] == "{":
                depth += 1
            elif body[j] == "}":
                depth -= 1
                if depth == 0:
                    j += 1
                    break
            j += 1
        k = j
        while k < len(body) and body[k] in " \t":
            k += 1
        if k < len(body) and body[k] == ",":
            k += 1
        while k < len(body) and body[k] in " \t\r":
            k += 1
        if k < len(body) and body[k] == "\n":
            k += 1
        full = body[i:k]
        inner = body[start:j]
        nw = re.search(r'"new_weapon"\s*:\s*"([^"]+)"', inner)
        entries.append((old, full, nw.group(1) if nw else ""))
        i = k
    return entries


def _nested_weapon_entries(entry_text: str) -> List[Tuple[str, str, str]]:
    """Find wrongly nested sibling weapon entries inside a payload."""
    # After the first closing of schema fields, look for "Weapon": { "new_weapon"
    # Heuristic: any "Name": { containing new_weapon that isn't the outer key line
    inner_matches = list(
        re.finditer(
            r'^([ \t]*)"([^"]+)"\s*:\s*\{',
            entry_text,
            re.M,
        )
    )
    if len(inner_matches) <= 1:
        return []
    # First match is the outer entry key line inside full_entry - skip it
    nested: List[Tuple[str, str, str]] = []
    for match in inner_matches[1:]:
        key = match.group(2)
        # skip known schema-only nested dicts (none expected with new_weapon)
        start = match.start()
        # find this nested object's span within entry_text
        brace_at = entry_text.find("{", match.end() - 1)
        depth = 0
        j = brace_at
        while j < len(entry_text):
            if entry_text[j] == "{":
                depth += 1
            elif entry_text[j] == "}":
                depth -= 1
                if depth == 0:
                    j += 1
                    break
            j += 1
        chunk = entry_text[start:j]
        nw = re.search(r'"new_weapon"\s*:\s*"([^"]+)"', chunk)
        if not nw:
            continue
        nested.append((key, chunk, nw.group(1)))
    return nested


def _strip_nested_from_entry(entry_text: str, nested_chunks: List[str]) -> str:
    text = entry_text
    for chunk in nested_chunks:
        text = text.replace(chunk, "", 1)
    # ensure payload closes with },
    text = text.rstrip()
    # remove trailing orphan commas/whitespace inside before final }
    text = re.sub(r",\s*$", "", text)
    if not text.rstrip().endswith("},") and not text.rstrip().endswith("}"):
        pass
    # normalize: entry should end with },
    text = text.rstrip()
    if text.endswith("},"):
        return text + "\n"
    if text.endswith("}"):
        return text + ",\n"
    # missing close brace entirely
    if not text.endswith("}"):
        text = text.rstrip(", \t\n") + "\n                    },\n"
    return text


def _format_entry(old: str, new_weapon: str, swap: bool, baked: bool, extra_lines: str = "") -> str:
    swap_s = "True" if swap else "False"
    baked_s = "True" if baked else "False"
    body = (
        f'                    "{old}": {{\n'
        f'                        "new_weapon": "{new_weapon}",\n'
        f'                        "swap_fire_effect": {swap_s},\n'
        f'                        "depiction_baked_in": {baked_s},\n'
    )
    if extra_lines:
        body += extra_lines
        if not extra_lines.endswith("\n"):
            body += "\n"
    body += "                    },\n"
    return body


def _parse_flags(chunk: str) -> Tuple[bool, bool, str]:
    swap = "True" in (re.search(r'"swap_fire_effect"\s*:\s*(True|False)', chunk) or [None, "False"])[1]
    baked_m = re.search(r'"depiction_baked_in"\s*:\s*(True|False)', chunk)
    baked = baked_m.group(1) == "True" if baked_m else False
    # preserve old_new_effect line if present
    extra = ""
    one = re.search(r'[ \t]*"old_new_effect"\s*:\s*\([^)]*\)\s*,?\n', chunk)
    if one:
        extra = one.group(0)
        if not extra.strip().endswith(","):
            extra = extra.rstrip() + ",\n"
    return swap, baked, extra


def repair_replace_body(body: str) -> Tuple[str, int]:
    entries = _extract_entries(body)
    if not entries:
        return body, 0

    repaired: List[Tuple[str, str, str]] = []  # old, new, formatted
    changes = 0

    for old, full, new in entries:
        nested = _nested_weapon_entries(full)
        if not nested:
            # drop bare->magazine remount-only top-level
            if new and _is_bare_to_magazine(old, new):
                changes += 1
                continue
            repaired.append((old, new, full if full.endswith("\n") else full + "\n"))
            continue

        changes += 1
        nested_chunks = [c for _, c, _ in nested]
        parent = _strip_nested_from_entry(full, nested_chunks)
        parent_nw = re.search(r'"new_weapon"\s*:\s*"([^"]+)"', parent)
        parent_new = parent_nw.group(1) if parent_nw else new

        # Fold: if a nested remount targets parent_new, fold into parent
        fold_variant = None
        remaining_nested = []
        for n_old, n_chunk, n_new in nested:
            if parent_new and n_old == parent_new and _is_bare_to_magazine(n_old, n_new):
                fold_variant = n_new
                continue
            if _is_bare_to_magazine(n_old, n_new):
                # drop remount-only
                continue
            remaining_nested.append((n_old, n_chunk, n_new))

        if fold_variant and parent_nw:
            parent = re.sub(
                r'("new_weapon"\s*:\s*")' + re.escape(parent_new) + r'(")',
                r"\g<1>" + fold_variant + r"\2",
                parent,
                count=1,
            )
            parent_new = fold_variant

        # Re-format parent cleanly from flags
        swap, baked, extra = _parse_flags(parent)
        if parent_new:
            repaired.append((old, parent_new, _format_entry(old, parent_new, swap, baked, extra)))
        else:
            repaired.append((old, new, parent if parent.endswith("\n") else parent + "\n"))

        for n_old, n_chunk, n_new in remaining_nested:
            swap, baked, extra = _parse_flags(n_chunk)
            repaired.append((n_old, n_new, _format_entry(n_old, n_new, swap, baked, extra)))

    if not changes:
        return body, 0

    out = "\n" + "".join(e[2] for e in repaired)
    return out, changes


def repair_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    total = 0
    out: List[str] = []
    i = 0
    key_re = re.compile(r'^([ \t]*)"replace":\s*\{', re.M)
    while True:
        m = key_re.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i:m.start()])
        indent = m.group(1)
        brace_start = m.end() - 1
        depth = 0
        j = brace_start
        while j < len(text):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    j += 1
                    break
            j += 1
        body = text[brace_start + 1 : j - 1]
        k = j
        while k < len(text) and text[k] in " \t":
            k += 1
        if k < len(text) and text[k] == ",":
            k += 1
        while k < len(text) and text[k] in " \t":
            k += 1
        if k < len(text) and text[k] == "\n":
            k += 1

        new_body, changes = repair_replace_body(body)
        total += changes
        if changes:
            out.append(f'{indent}"replace": {{{new_body}{indent}}},\n')
        else:
            out.append(text[m.start():k])
        i = k

    new_text = "".join(out)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return total


def main() -> None:
    total = 0
    for directory in (
        REPO / "src" / "constants" / "unit_edits",
        REPO / "src" / "constants" / "new_units",
    ):
        for path in sorted(directory.glob("*_unit_edits.py")) + sorted(directory.glob("*_new_units.py")):
            n = repair_file(path)
            if n:
                print(f"{path.relative_to(REPO)}: repaired {n} replace entries")
                total += n
    print(f"Done. total_changes={total}")


if __name__ == "__main__":
    main()
