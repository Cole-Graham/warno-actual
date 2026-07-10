"""One-time migration: rewrite in-scope squad AT/AA Salves to magazine variants.

Usage (from repo root, with venv):
  .\\.venv\\Scripts\\python.exe tools/migrate_infantry_magazine_salves.py
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from src.constants.new_units import NEW_UNITS
from src.constants.unit_edits import load_unit_edits
from src.constants.unit_edits.replace_schema import normalize_replace
from src.data.infantry_magazine_salvo import (
    INFANTRY_MAGAZINE_CATEGORIES,
    build_infantry_at_aa_magazine_salvos,
    magazine_ammo_name,
    parse_magazine_length,
    split_hagru_base,
    strip_magazine_suffixes,
)
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)

REPO = Path(__file__).resolve().parents[1]
UNIT_EDITS_DIR = REPO / "src" / "constants" / "unit_edits"
NEW_UNITS_DIR = REPO / "src" / "constants" / "new_units"


def _load_game_db() -> Dict[str, Any]:
    import sys

    import yaml

    from src.data import load_database_from_disk

    repo = Path(__file__).resolve().parents[1]
    if str(repo) not in sys.path:
        sys.path.insert(0, str(repo))

    config_path = repo / "config" / "config.YAML"
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    return load_database_from_disk(config)


def _find_unit_edits_file(unit_name: str) -> Optional[Path]:
    for path in UNIT_EDITS_DIR.glob("*_unit_edits.py"):
        text = path.read_text(encoding="utf-8")
        if re.search(rf'^\s*"{re.escape(unit_name)}"\s*:', text, re.MULTILINE):
            return path
    return None


def _find_new_units_file(unit_name: str) -> Optional[Path]:
    for path in NEW_UNITS_DIR.glob("*_new_units.py"):
        text = path.read_text(encoding="utf-8")
        if f'"NewName": "{unit_name}"' in text or f"'NewName': '{unit_name}'" in text:
            return path
    return None


def _salves_key_candidates(base: str, length: int, variant: str) -> List[str]:
    return [base, variant, f"{base}_salvolength{length}", f"{base}_infmagazine{length}"]


def _rewrite_salves_in_unit_block(
    block: str,
    base: str,
    length: int,
    variant: str,
) -> Tuple[str, bool]:
    """Rewrite Salves entries for base ammo inside a unit dict block."""
    changed = False
    # Match "AmmoName": N  or 'AmmoName': N inside Salves
    pattern = re.compile(
        rf'(["\'])({re.escape(base)}(?:_salvolength\d+|_infmagazine\d+)?)(\1)\s*:\s*(\d+)',
    )

    def repl(match: re.Match) -> str:
        nonlocal changed
        quote, key, _q2, val = match.group(1), match.group(2), match.group(3), match.group(4)
        key_len = parse_magazine_length(key)
        if key_len is not None and key_len != length and strip_magazine_suffixes(key) != base:
            return match.group(0)
        if strip_magazine_suffixes(key) != base and key != base:
            return match.group(0)
        old_n = int(val)
        # Only rewrite AT/AA magazine candidates (N>1 or already magazine with wrong value)
        if old_n <= 1 and key == variant:
            return match.group(0)
        if old_n <= 1 and key_len is None and key == base:
            # Already 1 without magazine suffix — still rename to variant
            pass
        elif old_n <= 1 and key_len is None:
            return match.group(0)
        changed = True
        return f"{quote}{variant}{quote}: 1"

    new_block, n = pattern.subn(repl, block)
    if n:
        return new_block, changed
    return block, False


def _ensure_replace_in_block(block: str, old_ammo: str, new_ammo: str) -> Tuple[str, bool]:
    """Ensure equipmentchanges.replace contains (old_ammo, new_ammo) as a sibling entry."""
    if old_ammo == new_ammo:
        return block, False
    if re.search(
        rf'\(\s*["\']{re.escape(old_ammo)}["\']\s*,\s*["\']{re.escape(new_ammo)}["\']',
        block,
    ) or re.search(
        rf'["\']{re.escape(old_ammo)}["\']\s*:\s*["\']{re.escape(new_ammo)}["\']',
        block,
    ):
        return block, False

    eq_match = re.search(r'("equipmentchanges"\s*:\s*\{)', block)
    if not eq_match:
        wd_match = re.search(r'("WeaponDescriptor"\s*:\s*\{)', block)
        if not wd_match:
            return block, False
        insert_at = wd_match.end()
        snippet = (
            f'\n            "equipmentchanges": {{\n'
            f'                "replace": {{\n'
            f'                    "{old_ammo}": {{\n'
            f'                        "new_weapon": "{new_ammo}",\n'
            f'                        "swap_fire_effect": False,\n'
            f'                        "depiction_baked_in": True,\n'
            f'                    }},\n'
            f'                }},\n'
            f'            }},'
        )
        return block[:insert_at] + snippet + block[insert_at:], True

    replace_match = re.search(
        r'("replace"\s*:\s*)(\[[\s\S]*?\]|\{[\s\S]*?\n\s*\})',
        block[eq_match.start():],
    )
    if not replace_match:
        brace = block.find("{", eq_match.start())
        if brace < 0:
            return block, False
        snippet = (
            f'\n                "replace": {{\n'
            f'                    "{old_ammo}": {{\n'
            f'                        "new_weapon": "{new_ammo}",\n'
            f'                        "swap_fire_effect": False,\n'
            f'                        "depiction_baked_in": True,\n'
            f'                    }},\n'
            f'                }},'
        )
        return block[: brace + 1] + snippet + block[brace + 1 :], True

    abs_list_start = eq_match.start() + replace_match.start(2)
    list_part = replace_match.group(2)
    abs_list_end = abs_list_start + len(list_part)
    inner = list_part.rstrip()

    payload = (
        f'"{old_ammo}": {{\n'
        f'                        "new_weapon": "{new_ammo}",\n'
        f'                        "swap_fire_effect": False,\n'
        f'                        "depiction_baked_in": True,\n'
        f'                    }}'
    )

    if inner.startswith("["):
        # List-form replace is legacy; append a tuple for remount/Salves lookup
        # via equipmentchanges path that still scans raw tuples in some tools.
        if inner.endswith("]"):
            insert = f'\n                    ("{old_ammo}", "{new_ammo}"),\n                '
            new_list = inner[:-1] + insert + "]"
            return block[:abs_list_start] + new_list + block[abs_list_end:], True

    if inner.startswith("{"):
        if inner.endswith("}"):
            insert = f'\n                    {payload},\n                '
            new_list = inner[:-1] + insert + "}"
            return block[:abs_list_start] + new_list + block[abs_list_end:], True

    return block, False


def _extract_unit_block(text: str, unit_name: str) -> Optional[Tuple[int, int, str]]:
    """Return (start, end, block) for a top-level unit entry dict."""
    pattern = re.compile(rf'^(\s*)("{re.escape(unit_name)}"\s*:\s*\{{)', re.MULTILINE)
    match = pattern.search(text)
    if not match:
        return None
    start = match.start(2)
    # Brace scan from opening {
    i = text.find("{", match.start(2))
    if i < 0:
        return None
    depth = 0
    for j in range(i, len(text)):
        ch = text[j]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return start, j + 1, text[start : j + 1]
    return None


def _extract_new_unit_block(text: str, unit_name: str) -> Optional[Tuple[int, int, str]]:
    """Find NEW_UNITS entry whose NewName matches."""
    marker = f'"NewName": "{unit_name}"'
    idx = text.find(marker)
    if idx < 0:
        return None
    # Walk backward to the tuple key opening
    key_match = None
    for m in re.finditer(r'\(\s*"[^"]+"\s*,\s*\d+\s*\)\s*:\s*\{', text):
        if m.start() < idx:
            key_match = m
        else:
            break
    if not key_match:
        return None
    start = key_match.start()
    i = text.find("{", key_match.start())
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return start, j + 1, text[start : j + 1]
    return None


def migrate_file(
    path: Path,
    unit_rewrites: Dict[str, List[Dict[str, Any]]],
    *,
    is_new_units: bool,
) -> int:
    text = path.read_text(encoding="utf-8")
    original = text
    changes = 0

    for unit_name, rows in unit_rewrites.items():
        extracted = (
            _extract_new_unit_block(text, unit_name)
            if is_new_units
            else _extract_unit_block(text, unit_name)
        )
        if not extracted:
            continue
        start, end, block = extracted
        new_block = block
        for row in rows:
            base = row["base_ammo"]
            length = int(row["length"])
            variant = row["variant_ammo"]
            if row.get("hagru"):
                continue  # HAGRU mounts are auto-attached; Salves usually on TBAGRU name
            new_block, salves_changed = _rewrite_salves_in_unit_block(
                new_block, base, length, variant,
            )
            new_block, replace_changed = _ensure_replace_in_block(new_block, base, variant)
            if salves_changed or replace_changed:
                changes += 1
                logger.info(
                    "%s: %s -> %s (Salves=1)",
                    unit_name,
                    base,
                    variant,
                )
        if new_block != block:
            text = text[:start] + new_block + text[end:]

    if text != original:
        path.write_text(text, encoding="utf-8")
        logger.info("Wrote %s", path)
    return changes


def main() -> None:
    logger.info("Loading game_db for infantry magazine Salves migration")
    game_db = _load_game_db()
    inventory = build_infantry_at_aa_magazine_salvos(game_db)
    remounts = inventory["remounts"]

    by_unit_edits: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    by_new_units: Dict[str, List[Dict[str, Any]]] = defaultdict(list)

    for row in remounts:
        if row.get("hagru"):
            continue
        if int(row["length"]) <= 1:
            continue
        if row["source"] == "unit_edits":
            by_unit_edits[row["unit"]].append(row)
        elif row["source"] == "NEW_UNITS":
            by_new_units[row["unit"]].append(row)
        # vanilla leftovers: no constants file to rewrite; runtime remount covers them

    total = 0
    # Group unit_edits by file
    file_units: Dict[Path, Dict[str, List[Dict[str, Any]]]] = defaultdict(dict)
    for unit_name, rows in by_unit_edits.items():
        path = _find_unit_edits_file(unit_name)
        if not path:
            logger.warning("No unit_edits file for %s", unit_name)
            continue
        file_units[path][unit_name] = rows

    for path, units in file_units.items():
        total += migrate_file(path, units, is_new_units=False)

    new_file_units: Dict[Path, Dict[str, List[Dict[str, Any]]]] = defaultdict(dict)
    for unit_name, rows in by_new_units.items():
        path = _find_new_units_file(unit_name)
        if not path:
            logger.warning("No new_units file for %s", unit_name)
            continue
        new_file_units[path][unit_name] = rows

    for path, units in new_file_units.items():
        total += migrate_file(path, units, is_new_units=True)

    logger.info(
        "Migration complete: %s unit weapon rewrites across %s unit_edits + %s NEW_UNITS units",
        total,
        len(by_unit_edits),
        len(by_new_units),
    )


if __name__ == "__main__":
    main()
