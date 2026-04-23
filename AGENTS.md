# AGENTS & contributor conventions

Local **Cursor** rules live in **`.cursor/rules/*.mdc`**, but **only** [`.cursor/rules/sync-agents-md-with-cursor-rules.mdc`](.cursor/rules/sync-agents-md-with-cursor-rules.mdc) is **tracked in git**; other `.mdc` files stay **private** (see [`.gitignore`](.gitignore)). This **`AGENTS.md`** is the **versioned** summary of project conventions for **all** devs and tools (and should mirror the substance of your private rules, as that policy file describes).

**Keep in sync:** (1) **From convention → Cursor:** when you change a project convention, update this file first, then copy into your local `.cursor/rules/*.mdc` if you use Cursor (see Cursor *Rules* docs: `description`, `globs`, `alwaysApply` in the front matter). (2) **From Cursor → this file:** when you **add or materially change** a rule in `.cursor/rules/`, update **`AGENTS.md` in the same change** so the repo stays authoritative. The checked-in **`.cursor/rules/sync-agents-md-with-cursor-rules.mdc`** nudges the agent to do (2) when it touches rule files.

**Also read:** [README.md](README.md) (Python env, install, config), [docs/onboarding.md](docs/onboarding.md) (editor/venv quality-of-life), and [pyproject.toml](pyproject.toml) (dependencies and optional extras).

---

## Python: use the repo virtualenv

The project uses **`ndf-parse`** (import name `ndf_parse`) and other packages from [requirements.txt](requirements.txt) / [pyproject.toml](pyproject.toml). The system `python` on `PATH` often does not have the right environment.

- **Activate the venv** (interactive): Windows `.\.venv\Scripts\Activate.ps1`, Unix `source .venv/bin/activate`, then use `python` as usual.
- **Or call the interpreter by path** (reliable in fresh shells or scripts): Windows `.\.venv\Scripts\python.exe`, Unix `.venv/bin/python` — e.g. `.\.venv\Scripts\python.exe -m unittest ...`

Do not assume bare `python` or `py` has project dependencies unless the environment is confirmed.

---

## `ndf_parse` map lookups: `by_k`, `by_key`, `by_m` and strictness

When using **map rows** from `ndf_parse` (as `ndf` / `ndf_parse`):

- **`by_k(key)`** / **`by_key(key)`** / **`by_m(...)`** — **strictness defaults to `True`**: a missing key **raises** instead of returning `None`.
- For **optional** keys, pass **`strict=False`** so you get `None` when missing.

**Required** lookup (bug if missing): keep default `strict=True`. **Optional** lookup: `by_k(key, False)` (or the matching API for your version).

```python
# Optional — key may be missing
row = descriptors_map.by_k('"some_trait"', False)
if row:
    ...

# Required — expect to raise if wrong
row = descriptors_map.by_k('"cluster"')
```

---

## Formatting and refactors (unless the task says otherwise)

- **Do not churn whitespace** for its own sake. **Do not** switch quote styles (single vs double) in passing edits.
- **Avoid over-extraction:** do not add tiny one-off helpers that only wrap a few lines at a single call site unless there is real duplication, a clear shared boundary, or the author asks to split. Prefer one readable linear flow (early returns, then loops, then logging).

---

## Weapon standards system (high level)

Standards enforce balance rules across ammunition and missile descriptors. They live under `src/constants/weapons/standards/` and are applied by handlers under `src/gameplay_mods/generated/gameplay/gfx/ammunition_/handlers/`.

### Two kinds of standards

- **Category standards** ([`standards/by_category.py`](src/constants/weapons/standards/by_category.py)) — keyed by weapon **category** from the `ammunitions` / `missiles` dict tuples (e.g. `A2A`, `SAM`, `MANPAD`, …). Handler files in `handlers/*_category_standards.py` match on category and apply the right dict.
- **Pattern standards** ([`standards/pattern/`](src/constants/weapons/standards/pattern/)) — rules matched by **scanning** NDF descriptors (traits, name substrings, `TypeCategoryName`, calibers, ranges). Full-file passes live in `handlers/standards.py` (e.g. `apply_aim_time_standards`, `apply_he_damage_standards`).

### Edit ordering

**All standards run before dict edits.** Dict edits may override any standard; standards **never** override dict edits.

- **`ammunition.py`:** pattern passes first, then per-weapon: category standards → `_apply_weapon_edits`.
- **`missiles.py`:** file-wide passes first, then per-missile: category standards (SEAD, AA hit-roll, AA suppress) → `_apply_missile_edits`.

When adding a new standard, call it **before** `_apply_weapon_edits` / `_apply_missile_edits` — **never** after dict edits.

### Constants precomputation

If a standard needs values from **both** constants dicts and **vanilla** game data:

1. Add a `build_*` in [`src/data/constants_precomputation.py`](src/data/constants_precomputation.py), call it from `build_constants_precomputation_data`, emit JSON under `src/data/database/constants_precomputation/`.
2. Wire into `game_db` in `run_patcher.py` and `run_patcher_with_bat.py`.
3. Read from `game_db` in the handler at NDF edit time.

### NDF namespace and salvo variants

- Descriptors: `Ammo_{weapon_name}` (e.g. `Ammo_SAM_Strela10M3`).
- Salvo suffix: `_salvolength{N}` (e.g. `Ammo_SAM_Strela10M3_salvolength4`).
- Precomputed maps: key by **base `weapon_name`** (no `Ammo_`, no `_salvolength` suffix).
- `game_db["ammunition"]["ammo_properties"]` is keyed by full NDF namespace: use `f"Ammo_{weapon_name}"` when you need that entry.

### Export chain for new constants

1. Define under `src/constants/weapons/standards/` (category or new file under `pattern/`).
2. Re-export from `src/constants/weapons/standards/__init__.py` and `src/constants/weapons/__init__.py`.
3. Import in the handler that applies the standard.

---

## Optional tools (not everyone installs)

Core install covers the patcher and **dpm_visualizer** (including **matplotlib** for its charts). **Qt** `tools/fxeditor` and **Excel** are in the **`optional`** extra (`PySide6`, `openpyxl`). See [docs/onboarding.md](docs/onboarding.md#optional-extras-for-one-off-work).
