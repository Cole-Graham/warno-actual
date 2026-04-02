"""Parse WA-format damage resistance CSV tables for the DPM visualizer."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple


def normalize_damage_family(name: Optional[str]) -> str:
    """Strip DamageFamily_ prefix and lowercase for CSV row keys."""
    if not name:
        return ""
    s = str(name).strip()
    if s.startswith("DamageFamily_"):
        s = s[len("DamageFamily_") :]
    return s.lower()


def normalize_resistance_family(name: Optional[str]) -> str:
    """Strip ResistanceFamily_ prefix and lowercase for CSV column keys."""
    if not name:
        return ""
    s = str(name).strip()
    if s.startswith("ResistanceFamily_"):
        s = s[len("ResistanceFamily_") :]
    return s.lower()


class DamageTableCsv:
    """In-memory damage vs resistance ratio table from a WA-export CSV."""

    def __init__(self) -> None:
        self.source_path: Optional[Path] = None
        # row_keys[r] = (damage_family, damage_level)
        self._row_keys: List[Tuple[str, int]] = []
        # col_keys[c] = (resistance_family, armor_level)
        self._col_keys: List[Tuple[str, int]] = []
        self._grid: List[List[float]] = []
        self._row_index: Dict[Tuple[str, int], int] = {}
        self._col_index: Dict[Tuple[str, int], int] = {}

    def load_path(self, path: Path) -> None:
        """Load and parse a CSV file. Raises on missing file or invalid layout."""
        path = path.resolve()
        self.source_path = path
        self._row_keys = []
        self._col_keys = []
        self._grid = []
        self._row_index = {}
        self._col_index = {}

        with path.open(newline="", encoding="utf-8-sig") as f:
            rows = list(csv.reader(f))

        if len(rows) < 4:
            raise ValueError(f"CSV too short (need header + data): {path}")

        # Row 0: ,,Column Index, 0, 1, ...
        # Row 1: ,,Resistance Family, ...
        # Row 2: Row Index, Damage Family, Levels, ...
        fam_row = rows[1]
        lvl_row = rows[2]

        if len(fam_row) < 4 or len(lvl_row) < 4:
            raise ValueError(f"CSV header rows too narrow: {path}")

        for col_idx in range(3, len(fam_row)):
            if col_idx >= len(lvl_row):
                break
            rf_raw = fam_row[col_idx].strip()
            lvl_raw = lvl_row[col_idx].strip()
            if not rf_raw:
                continue
            try:
                armor_level = int(float(lvl_raw))
            except ValueError:
                continue
            rf = normalize_resistance_family(rf_raw)
            key = (rf, armor_level)
            c = len(self._col_keys)
            self._col_keys.append(key)
            self._col_index[key] = c

        for r in range(3, len(rows)):
            row = rows[r]
            if len(row) < 4:
                continue
            try:
                int(row[0].strip())
            except ValueError:
                continue
            df_raw = row[1].strip()
            try:
                dmg_level = int(float(row[2].strip()))
            except ValueError:
                continue
            df = normalize_damage_family(df_raw)
            rk = (df, dmg_level)
            row_i = len(self._row_keys)
            self._row_keys.append(rk)
            self._row_index[rk] = row_i

            values: List[float] = []
            for c in range(len(self._col_keys)):
                col_csv = c + 3
                if col_csv < len(row):
                    cell = row[col_csv].strip()
                    try:
                        values.append(float(cell))
                    except ValueError:
                        values.append(0.0)
                else:
                    values.append(0.0)
            self._grid.append(values)

    def lookup(
        self,
        damage_family: Optional[str],
        damage_level: Optional[int],
        resistance_family: Optional[str],
        resistance_level: Optional[int],
    ) -> Optional[float]:
        """Return cell value or None if row/column key missing."""
        if damage_level is None or resistance_level is None:
            return None
        df = normalize_damage_family(damage_family)
        rf = normalize_resistance_family(resistance_family)
        rk = (df, int(damage_level))
        ck = (rf, int(resistance_level))
        ri = self._row_index.get(rk)
        ci = self._col_index.get(ck)
        if ri is None or ci is None:
            return None
        if ri >= len(self._grid) or ci >= len(self._grid[ri]):
            return None
        return self._grid[ri][ci]

    def has_damage_row(self, damage_family: Optional[str], damage_level: Optional[int]) -> bool:
        if damage_level is None:
            return False
        df = normalize_damage_family(damage_family)
        return (df, int(damage_level)) in self._row_index

    def resistance_families(self) -> List[str]:
        """Distinct resistance family names (sorted)."""
        seen: Set[str] = set()
        for rf, _ in self._col_keys:
            seen.add(rf)
        return sorted(seen)

    def resistance_levels_for(self, resistance_family: Optional[str]) -> List[int]:
        """Armor levels present for the given resistance family."""
        rf = normalize_resistance_family(resistance_family)
        levels: List[int] = []
        for rfk, lvl in self._col_keys:
            if rfk == rf:
                levels.append(lvl)
        return sorted(set(levels))

    def damage_families(self) -> List[str]:
        seen: Set[str] = set()
        for df, _ in self._row_keys:
            seen.add(df)
        return sorted(seen)

    def damage_levels_for(self, damage_family: Optional[str]) -> List[int]:
        df = normalize_damage_family(damage_family)
        levels: List[int] = []
        for dfn, lvl in self._row_keys:
            if dfn == df:
                levels.append(lvl)
        return sorted(set(levels))


def default_damage_table_dir() -> Path:
    """Directory containing bundled `*.csv` damage tables."""
    return Path(__file__).resolve().parent / "damage_table"


def list_damage_table_csvs(directory: Optional[Path] = None) -> List[str]:
    """Sorted basenames of `*.csv` files in the damage table directory."""
    d = directory if directory is not None else default_damage_table_dir()
    if not d.is_dir():
        return []
    names = [p.name for p in d.glob("*.csv") if p.is_file()]
    return sorted(names)


def pick_default_csv_name(names: List[str]) -> Optional[str]:
    if not names:
        return None
    if "wa_damage-table.csv" in names:
        return "wa_damage-table.csv"
    return names[0]


def load_damage_table(filename: str, directory: Optional[Path] = None) -> DamageTableCsv:
    """Load `filename` from the damage table directory."""
    d = directory if directory is not None else default_damage_table_dir()
    path = d / filename
    table = DamageTableCsv()
    table.load_path(path)
    return table
