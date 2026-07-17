# AGENTS & contributor conventions

Local **Cursor** rules live in **`.cursor/rules/*.mdc`**, but **only** [`.cursor/rules/sync-agents-md-with-cursor-rules.mdc`](.cursor/rules/sync-agents-md-with-cursor-rules.mdc) is **tracked in git**; other `.mdc` files stay **private** (see [`.gitignore`](.gitignore)). This **`AGENTS.md`** is the **versioned** summary of project conventions for **all** devs and tools (and should mirror the substance of your private rules, as that policy file describes).

**Keep in sync:** (1) **From convention → Cursor:** when you change a project convention, update this file first, then copy into your local `.cursor/rules/*.mdc` if you use Cursor (see Cursor *Rules* docs: `description`, `globs`, `alwaysApply` in the front matter). (2) **From Cursor → this file:** when you **add or materially change** a rule in `.cursor/rules/`, update **`AGENTS.md` in the same change** so the repo stays authoritative. The checked-in **`.cursor/rules/sync-agents-md-with-cursor-rules.mdc`** nudges the agent to do (2) when it touches rule files.

**Also read:** [README.md](README.md) (Python env, install, config), [docs/onboarding.md](docs/onboarding.md) (editor/venv quality-of-life), [docs/validation/infantry_small_arms_vs_strength.md](docs/validation/infantry_small_arms_vs_strength.md) (infantry small-arms validation), the **Depiction edits** section below, and [pyproject.toml](pyproject.toml) (dependencies and optional extras).

---

## Python: use the repo virtualenv

The project uses **`ndf-parse`** (import name `ndf_parse`) and other packages from [requirements.txt](requirements.txt) / [pyproject.toml](pyproject.toml). The system `python` on `PATH` often does not have the right environment.

- **Activate the venv** (interactive): Windows `.\.venv\Scripts\Activate.ps1`, Unix `source .venv/bin/activate`, then use `python` as usual.
- **Or call the interpreter by path** (reliable in fresh shells or scripts): Windows `.\.venv\Scripts\python.exe`, Unix `.venv/bin/python` — e.g. `.\.venv\Scripts\python.exe -m unittest ...`

Do not assume bare `python` or `py` has project dependencies unless the environment is confirmed.

---

## Do not run the patcher to test agent changes

**Never** run `run_patcher.py`, `run_patcher_with_bat.py`, or equivalent patch/build scripts to verify code changes unless the user **explicitly** asks. The patcher writes game data and is not an appropriate agent self-test loop.

Use read-only checks instead: import modules, `unittest` / `pytest`, grep, or small one-off scripts (e.g. audit constants dicts). Only run the patcher when the user requests it.

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

**Category fixed standards run before dict edits.** Dict edits may override those fixed values; standards **never** override dict edits.

- **`ammunition.py`:** pattern passes first, then per-weapon: category standards (fixed values) → `_apply_weapon_edits` → CLU bomb dispersion (precomputed, see below).
- **`missiles.py`:** file-wide passes first, then per-missile: category standards (SEAD, AA suppress precompute apply, …) → `_apply_missile_edits` → AA range-scaled accuracy where needed.

When adding a new **fixed** standard, call it **before** `_apply_weapon_edits` / `_apply_missile_edits`.

**CLU bomb dispersion** is an exception: `CLU_BOMB_STANDARDS["ratios"]` are not applied in `apply_category_bomb_standards`. They are precomputed in `build_clu_bomb_dispersion` (constants radius + `CLU_BOMB_STANDARDS` ratios, or explicit `DispersionAt*` in `parent_membr`) and written by `apply_clu_bomb_dispersion_standard` **after** dict edits so dispersion tracks constants `RadiusSplashPhysicalDamagesGRU`.

### Constants precomputation

If a standard needs values from **both** constants dicts and **vanilla** game data:

1. Add a `build_*` in [`src/data/constants_precomputation.py`](src/data/constants_precomputation.py), call it from `build_constants_precomputation_data`, emit JSON under `src/data/database/constants_precomputation/`.
2. Wire into `game_db` in `run_patcher.py` and `run_patcher_with_bat.py`.
3. Read from `game_db` in the handler at NDF edit time (for CLU dispersion, apply **after** dict edits on that weapon).

### NDF namespace and salvo variants

- Descriptors: `Ammo_{weapon_name}` (e.g. `Ammo_SAM_Strela10M3`).
- Salvo suffix: `_salvolength{N}` (e.g. `Ammo_SAM_Strela10M3_salvolength4`).
- Precomputed maps: key by **base `weapon_name`** (no `Ammo_`, no `_salvolength` suffix).
- `game_db["ammunition"]["ammo_properties"]` is keyed by full NDF namespace: use `f"Ammo_{weapon_name}"` when you need that entry.

### Export chain for new constants

1. Define under `src/constants/weapons/standards/` (category or new file under `pattern/`).
2. Re-export from `src/constants/weapons/standards/__init__.py` and `src/constants/weapons/__init__.py`.
3. Import in the handler that applies the standard.

### HOBS no-HMD (weapon descriptors)

Some HOBS missiles require a helmet-mounted display (`_hmd`) for full off-boresight capability. **Existing** units that mount configured HOBS ammo **without** projected `_hmd` from `unit_edits` `SpecialtiesList` get narrowed turret arcs on turrets carrying that missile and ammo swapped to `*_NoOBS` variants.

- **Constants:** [`src/constants/unit_edits/standards/pattern/hobs_no_hmd.py`](src/constants/unit_edits/standards/pattern/hobs_no_hmd.py) — `HOBS_NO_HMD_PATTERN_STANDARD` with a `missile_rules` tuple (append entries for more HOBS weapons later).
- **Handler:** [`weapon_descriptor/handlers/hobs_no_hmd.py`](src/gameplay_mods/generated/gameplay/gfx/weapon_descriptor/handlers/hobs_no_hmd.py).
- **Ordering:** `apply_hobs_no_hmd_pattern_standard` runs on vanilla `WeaponDescriptor.ndf` rows **after** `vanilla_renames_weapondescriptor`, **before** `new_units_weapondescriptor` and `unit_edits_weapondescriptor`, so per-unit dict edits override. **New units** are not scanned here; set turret angles and ammo in `NEW_UNITS["WeaponDescriptor"]` instead. TBAGRU HAGRU attachment in `unit_edits_weapondescriptor` still runs afterward and can add `*_NoOBS_HAGRU` clones on existing units.

### Air rocket platform (weapon descriptors)

Dumbfire rockets (`Arme.Family == DamageFamily_roquette_ap`) must use **avion** ammo on planes and **non-avion** ammo on helicopters. Mixed vanilla loadouts (e.g. one B8 pod `_avion`, one not) are corrected in batch.

- **Constants:** [`src/constants/unit_edits/standards/pattern/air_rocket_platform.py`](src/constants/unit_edits/standards/pattern/air_rocket_platform.py) — `AIR_ROCKET_PLATFORM_PAIRS` (`helo_ammo` ↔ `avion_ammo`, **same salvo length only**, distinct descriptors). A `_helo` suffix is just the non-avion name (same treatment as any other helo-side rocket). Missing siblings are authored in [`rocket.py`](src/constants/weapons/ammunition/rocket.py) (`is_new` donor clones), never auto-created at patch time and never self-paired. Intentional different-salvo remounts stay in `unit_edits`.
- **Handler:** [`weapon_descriptor/handlers/air_rocket_platform.py`](src/gameplay_mods/generated/gameplay/gfx/weapon_descriptor/handlers/air_rocket_platform.py).
- **Ordering:** `apply_air_rocket_platform_standard` runs **after** `unit_edits_weapondescriptor`, **before** `apply_helo_aa_turret_angles_pattern_standard`. Unpaired mounts log a warning. EffectTag is not rewritten. Ground RocketAir vehicles are skipped. **New units** are not scanned; set ammo in `NEW_UNITS` / constants.

### Shock no-resolute specialty (unit descriptors)

Shock units receive `Capacite_resolute` via the Choc skill auto-add in `tcapacite.py`. They must **not** also carry the `_resolute` specialty tag, or the UI implies a stacked resolute bonus.

- **Handler:** [`unite_descriptor/handlers/shock_no_resolute_specialty.py`](src/gameplay_mods/generated/gameplay/gfx/unite_descriptor/handlers/shock_no_resolute_specialty.py).
- **Ordering:** `apply_shock_no_resolute_specialty_pattern_standard` runs **after** `unit_edits` and `new_units` so `SpecialtiesList` patches are applied first, then `_resolute` is stripped when the unit has the Choc skill or `_choc` specialty. `Capacite_resolute` from tcapacite is unchanged.

### ATGM infantry team strength (unit descriptors)

Dedicated ATGM infantry teams (`is_at_team` / `ATteam_` name) whose mounts include ammo with `TypeCategoryName` token `JTOYRAARTS` (`ANTI-TANK MISSILE`) get strength **4** with `infantry_equip_veryheavy`, otherwise **3**. Recoilless AT teams (rocket-launch / tank-gun TypeCategory) are excluded. Units with an explicit `"strength"` in `unit_edits` / `NEW_UNITS` are skipped.

- **Constants:** [`src/constants/unit_edits/standards/pattern/atgm_infantry_team_strength.py`](src/constants/unit_edits/standards/pattern/atgm_infantry_team_strength.py).
- **Handler:** [`unite_descriptor/handlers/atgm_infantry_team_strength.py`](src/gameplay_mods/generated/gameplay/gfx/unite_descriptor/handlers/atgm_infantry_team_strength.py).
- **Ordering:** `apply_atgm_infantry_team_strength_pattern_standard` runs **after** `unit_edits` and `new_units` (so specialty adds are visible), **before** infantry WA armor and shock no-resolute. Writes `MaxPhysicalDamages` on `TBaseDamageModuleDescriptor` (weapon teams often have no `TInfantrySquadModuleDescriptor` / `SoldierCount`); updates `SoldierCount` and infantryWA armor Index when those modules exist.

### Infantry WA armor (unit descriptors)

Infantry squads (live `Infanterie` tag) automatically get `ResistanceFamily_infanterieWA` Blindage with `Index = max(15 - strength, 1)` from live `MaxPhysicalDamages`. Dedicated AT weapon teams are excluded via live `Infanterie_AT` (covers `ATteam_*` and non-prefix names like `RCL_L6_Wombat_UK`). Dedicated HMG/MMG teams (`HMGteam_` / `MMGteam_`) are excluded by name and keep vanilla `ResistanceFamily_infanterie`. MANPADs (`Infanterie_AA`), snipers, and line squads are included. Do **not** add manual `"armor": "Infantry_armor_reference"` in `unit_edits` / `NEW_UNITS`.

- **Constants:** [`src/constants/unit_edits/standards/pattern/infantry_armor.py`](src/constants/unit_edits/standards/pattern/infantry_armor.py).
- **Handler:** [`unite_descriptor/handlers/infantry_armor.py`](src/gameplay_mods/generated/gameplay/gfx/unite_descriptor/handlers/infantry_armor.py).
- **Ordering:** `apply_infantry_armor_pattern_standard` runs **after** ATGM team strength (so Index tracks final HP), **before** shock no-resolute. Units with an explicit `"armor"` **dict** in `unit_edits` / `NEW_UNITS` are skipped (vehicle / custom Blindage overrides).

### Commander / infantry leader Capacite (unit descriptors)

Vanilla `TCommanderModuleDescriptor` cannot be edited, so remaining commander modules are replaced with custom Instructor Capacites after `unit_edits` / `new_units`. Tank/arty leaders already strip the module and use `LDR_TNK` / `LDR_ARTY` via per-unit edits; this pass only hits units that still have the commander module.

- **Capacites:** [`src/constants/capacities/cmd.py`](src/constants/capacities/cmd.py) (`Capacite_CMD_UNIT`, range 900) and [`src/constants/capacities/ldr.py`](src/constants/capacities/ldr.py) (`Capacite_LDR_INF`, range 550). Both use `~/UnitEffect_Instructor`. Registered in [`capacitelist.py`](src/gameplay_mods/generated/gameplay/gfx/capacitelist.py).
- **ForbiddenTargetTags:** `CMD_UNIT` — `Canon_AA`, `CMD_Unit`, `Avion`, `Instructor_immune`. `LDR_INF` — same plus `LDR_Unit`, `LDR_SOV_Unit`, and `Artillerie` (infantry leaders do not buff artillery).
- **Constants:** [`src/constants/unit_edits/standards/pattern/commander_capacite.py`](src/constants/unit_edits/standards/pattern/commander_capacite.py) — classify by live TagSet (flatten nested lists from `overwrite_all` convert): `Infanterie` + (`LDR_Unit` / `LDR_SOV_Unit` or `_leader` / `leader_sov` specialty) and not `CMD_Unit` → `LDR_INF`; otherwise → `CMD_UNIT`. Do not key off `_CMD_` / `CMD2` names.
- **Handler:** [`unite_descriptor/handlers/commander_capacite.py`](src/gameplay_mods/generated/gameplay/gfx/unite_descriptor/handlers/commander_capacite.py).
- **Ordering:** `apply_commander_capacite_pattern_standard` runs **after** `unit_edits` and `new_units`, **before** ATGM team strength / infantry WA armor / shock no-resolute. Do **not** `modules_add` `TCommanderModuleDescriptor()` on new units. If a CMD clone’s donor lacks the commander module, add `"CMD_UNIT"` via `capacities.add_capacities` instead.

### Artillery deployment time

Howitzers, MLRS, and mortars get deployment time via category + unit pattern standards (most units no longer need manual `"WeaponDeployment"` in `unit_edits`).

- **Ammo constants:** [`standards/by_category.py`](src/constants/weapons/standards/by_category.py) — `ARTILLERY_DEPLOYMENT_CATEGORIES` (`howitzer`, `MLRS`, `mortar`) sets `HasDeploymentTime = True` in [`ammunition.py`](src/gameplay_mods/generated/gameplay/gfx/ammunition_/ammunition.py) before dict edits.
- **Precompute:** [`build_deployment_time_units`](src/data/constants_precomputation.py) extends `protected_ammo` / `protected_units` and emits `unit_deployment_seconds` (7 s or 15 s tier). Mounted ammo names from `weapons_db` are resolved through equipment `replace` edits, [`AMMUNITION_RENAMES`](src/constants/weapons/vanilla_inst_modifications.py), and salvo suffix variants (`_x{N}` → `_salvolength{N}`) before lookup. Aircraft and helos are excluded when the protected ammo is artillery-only.
- **Unit handler:** [`handlers/tweapondeployment.py`](src/gameplay_mods/generated/gameplay/gfx/unite_descriptor/handlers/tweapondeployment.py) — runs after batch module add/remove, before `unit_edits`, so explicit `"WeaponDeployment"` dict edits still override.
- **Tier rule:** 15 s if `RadiusSplashPhysicalDamagesGRU >= 152` **or** `PhysicalDamages >= 4.2`; otherwise 7 s. All packup times are 0 s.
- **Blanket disable:** unchanged — `_blanket_disable_deployment_time` strips non-protected ammo using the same name-resolution rules as precompute (`ammo_name_keeps_deployment_time`). DCA/ATGM ammo with explicit `HasDeploymentTime` in constants uses the same protection path.

---

## Infantry small arms vs strength validation

Precompute validation in [`src/data/infantry_small_arms_strength_validation.py`](src/data/infantry_small_arms_strength_validation.py) checks that edited/new infantry squads have countable small-arms totals matching `strength - occupied_slots`. Full write-up: [docs/validation/infantry_small_arms_vs_strength.md](docs/validation/infantry_small_arms_vs_strength.md).

- **Weapon teams** are skipped by **resolved loadout** (zero `countable` mounts, all mounts `team_mg` / `occupied` / `specialist`). Unit names (`ATteam`, `RCL_`) are not used.
- **`specialist`** mounts (RPG, portable `MinMax_ATGM`, Milan on dedicated teams, etc.) are excluded from `small_arms_total` only. Infantry with rifles + portable ATGM (e.g. Metis, Dragon) **is validated**; `MinMax_ATGM` does not occupy a rifle slot.
- **Occupied slots:** per-turret `max` for `MinMax_CanonAP` (dual AP/HE on one crew = one slot), per-turret `sum` for `MinMax_FLAME`.
- Manual override: `INFANTRY_SMALL_ARMS_STRENGTH_SKIP_UNITS` in the validation module.

---

## Depiction edits

**Cursor:** private rule [`.cursor/rules/depiction-edits.mdc`](.cursor/rules/depiction-edits.mdc) (file-scoped to depiction / unit-edit paths). Substance below is the versioned copy.

Shared apply logic: [`_apply.py`](src/gameplay_mods/generated/gameplay/gfx/depictions/_apply.py). Do **not** run the patcher to test depiction edits unless asked.

### Which path?

| Goal | Where |
|---|---|
| Patch an **existing** unit | `src/constants/unit_edits/depiction_edits/<FACTION>_depiction_edits/<Unit>.py` — tuple-key patches |
| Override a **new** unit after donor clone | `src/constants/new_units/new_depictions/<FACTION>_new_depictions/<Unit>.py` — same tuple-key schema **or** raw NDF |
| Full custom vehicle/aerial registration | `NEW_UNITS["depictions"]["custom"]` **plus** raw NDF string keys in `NEW_DEPICTIONS` |
| Vehicle High/Mid/Low mesh (existing) | `unit_edits[unit]["alternatives"]["mesh"]` — **not** depiction_edits |
| New vehicle/aircraft mesh LODs | `NEW_UNITS["depictions"]["new_mesh"]` and/or `"alternatives"` |
| Heavy-equipment crew meshes | `NEW_UNITS`: `servants` + `servant_types` → `depictionhumans` (no depiction file) |
| Supply-transport tow hook | Add donor to [`SUPPLY_TRANSPORT_VARIANT_CONFIG`](src/constants/supply_transport_variants.py) — depiction auto-built via [`_supply_transport.py`](src/constants/new_units/new_depictions/_supply_transport.py) |
| New `InfantrySelectorTactic_UU_SS` | Append `(uu, ss)` to `NEW_SELECTOR_TACTIC_OBJECTS` in [`selector_tactic.py`](src/constants/unit_edits/depiction_edits/selector_tactic.py) |
| SPAAG `he_dca` AIR fire FX | Automatic ([`he_dca_air_depiction`](src/gameplay_mods/generated/gameplay/gfx/depictions/he_dca_air_depiction.py)) — do not hand-author |

### Envelope and value shapes

Every edit dict needs `"unit_name"`, `"valid_files"`, and one or more `<FileStem>_ndf` sections (`.` → `_`). `load_depiction_edits()` merges by `unit_name`; `NEW_DEPICTIONS` keys must be `unit_name.lower()`.

| Shape | Detection | Use |
|---|---|---|
| Indexed ops | all-`int` keys | `{ i: ("edit"\|"insert"\|"remove"\|"replace"\|"add", payload) }` |
| Member map | all-`str` keys | `{ "MemberName": value }` |
| Wholesale list | string starting `[`, or list/tuple | Replace entire list (1-tuple of NDF string OK) |

Common tuple keys: `AllWeaponAlternatives_*`, `AllWeaponSubDepiction_*`, `TacticDepiction_*_{Soldier\|Ghost\|Alternatives}`, `(None, "TTransportedInfantryEntry")`, `(None, "TacticVehicleDepictionRegistration")`, aerial/missile carriage namespaces, `"new_objects"`. Infantry mesh/`FireEffectTag`/`Selector` values are auto-prefixed in `_apply.py`. Selector `UU_SS`: UniqueCount=`UU`, Surrogates use **SS**. Soldier `skeleton_tags` early-returns (skips Selector/Operators).

### By unit type (short)

- **Infantry existing:** indexed/member patches under `DepictionInfantry_ndf` (e.g. [`Ranger_US.py`](src/constants/unit_edits/depiction_edits/USA_depiction_edits/Ranger_US.py), [`Scout_US.py`](src/constants/unit_edits/depiction_edits/USA_depiction_edits/Scout_US.py)). Plan insert/remove before edit when indices shift.
- **Infantry new:** six blocks clone from donor automatically; optional `NEW_DEPICTIONS` uses the **new** unit name; set `selector_tactic` / counts on `NEW_UNITS` (e.g. [`MANPAD_Stinger_FJ_RFA.py`](src/constants/new_units/new_depictions/RFA_new_depictions/MANPAD_Stinger_FJ_RFA.py)).
- **Vehicles existing:** patch registration by `BlackHoleKey`; tow hook via `TowedUnitSubDepictionGenerator` `{"add": None}` (e.g. [`HEMTT_US.py`](src/constants/unit_edits/depiction_edits/USA_depiction_edits/HEMTT_US.py)).
- **Vehicles new:** auto-clone unless `depictions.custom` + matching raw NDF keys (e.g. [`DCA_M167A2_Vulcan_20mm_UK.py`](src/constants/new_units/new_depictions/UK_new_depictions/DCA_M167A2_Vulcan_20mm_UK.py)); tuple-key patches apply after clone.
- **Aerial / pylons:** existing = Op_ edits + indexed carriages; new = usually full raw NDF. Showroom aerial section key: `DepictionAerialUnitsShowroom_ndf`.
- **Towed / heavy equipment:** catalog clone in `towable.py`; crews via `servants` / `servant_types`.

### Registration

- **Existing:** country `__init__.py` import + `__all__` (loader uses `_DEPICTION_EDIT_FACTION_MODULES`); optional re-export from `depiction_edits/__init__.py`.
- **New:** country `*_NEW_DEPICTIONS` dict keyed by lowercase name; root [`new_depictions/__init__.py`](src/constants/new_units/new_depictions/__init__.py) merges factions.

### Pitfalls

`equipmentchanges` does not auto-update infantry depictions (`depiction_audit` warns). Vehicle/aerial registrations have no namespace (use `BlackHoleKey`). Custom vehicles need **both** `NEW_UNITS.depictions.custom` and `NEW_DEPICTIONS` keys. Missing `unit_name` → edit never loads. Prefer plain NDF strings or `(string,)` over `{f'...'}` set wrappers.

---

## Unit edits and new units: duplicate dict keys

`load_unit_edits()` and `load_new_units()` AST-scan `*_unit_edits.py` / `*_new_units.py` for duplicate keys at every nesting level in dict literals and log **ERROR** if found (Python keeps only the last value; merged dicts cannot be checked after import). Fix duplicates in the source file. **Exception:** duplicate keys inside a `WeaponDescriptor` → `Salves` block are allowed (multiple mounts, same ammo). For multiple `replace` rows per donor ammo, use a list under one key per `replace_schema.py`, not duplicate dict keys.

## New units: static UnitId

Every real `NEW_UNITS` entry (one with `"NewName"`) must define a unique integer `"UnitId"` **>= 50000**. Reference templates without `NewName` skip this. IDs are validated in `load_new_units()` (`validate_unit_ids`) and written to `DeckSerializer.ndf` by [`deck_serializer.py`](src/gameplay_mods/generated/gameplay/decks/deck_serializer.py). Do **not** renumber existing units (player decks encode these IDs). Gaps are fine. Supply-transport clones set `UnitId` in [`SUPPLY_TRANSPORT_VARIANT_CONFIG`](src/constants/supply_transport_variants.py). After a successful patcher run, the log includes `Highest new unit UnitId: …` so the next free ID is easy to see.

---

## Optional tools (not everyone installs)

Core install covers the patcher and **dpm_visualizer** (including **matplotlib** for its charts). **Qt** `tools/fxeditor` and **Excel** are in the **`optional`** extra (`PySide6`, `openpyxl`). See [docs/onboarding.md](docs/onboarding.md#optional-extras-for-one-off-work).
