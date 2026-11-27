# EasyNDF feasibility for WARNO ACTUAL

**Question:** could [EasyNDF](https://github.com/ShadowofChernobyl/EasyNDF) replace the custom Python patcher for developing WARNO ACTUAL?

**Short answer:** no, not as a replacement. EasyNDF is a capable GUI editor built around one rule list per NDF file. WARNO ACTUAL is a code-driven build. Much of its balance comes from rules that join data across several files after earlier edits have run, from precomputed tables, and from build steps outside NDF. EasyNDF cannot express those, and it has no command-line or headless way to run a full export. It is still worth installing next to the patcher, to browse data, compare units, view 3D models, read NDF docs, and check conflicts with other mods.

Reviewed at EasyNDF commit `3cfcb05` (v1.1.4, 2026-11-26), cloned and read locally. WARNO ACTUAL numbers come from importing the constants on `main` (2026-11-27).

---

## 1. What EasyNDF is

| Fact | Value |
|---|---|
| Kind | Windows desktop app (C# / WPF on .NET 10). An HTML version runs in the browser. |
| Platform | Windows 10/11 64-bit only. The WPF project builds only on Windows. |
| License | GNU AGPL-3.0, plus two extra terms: forks may not call themselves EasyNDF, and modified versions must be marked as different. |
| Age and activity | Repository history starts 2025-10-29 (the WinForms app, now on `archive/winforms`). The current WPF app started 2026-10-14: 57 commits and eight releases since (v1.0.0 to v1.1.4). One author. |
| Size | About 100k lines of C# in three projects: `EasyNdf.Engine` (no UI), `EasyNdf.Data`, `EasyNdf.App`. |
| Tests | None. The solution has no test project. CI only runs `dotnet build`. |
| Scripting | None. The only command-line switches are `--render software` and `--frame native`. Export happens in the GUI. |

### How it edits NDF

A **mod** is a JSON file (`*.mod.json`, kept in `%LOCALAPPDATA%\EasyNDF\Mods`) holding **rule sets**, usually one per game file. Each rule has a kind, **conditions** (which descriptors it matches), and **actions** (what it changes). The engine (`src/EasyNdf.Engine/Rules/RuleRunner.cs`) loads **one** NDF file and runs that file's rules in order.

Rule kinds: `Edit`, `Add`, `Clone`, `Remove`, `Replace`, `Scale`, `Formula`, `Table`, `Lookup`, `Check`, `Group`, `Variable`, plus `Text` and `File` (dictionary entries and carried files, written on export).

Conditions test a property, the descriptor name, its type, or the whole descriptor's text with `Starts With`, `Contains`, `Is Equal To`, number comparisons, and so on (`Conditions.cs`). Actions are `Set To`, `Add`, `Subtract`, `Multiply`, `Divide`, `Append`, `Prepend`, `Insert`, `Remove`, `Add Property`, `Remove Property`, and similar.

A real example, from the bundled WARNO Tactical Overhaul mod: "every unit that is not aircraft, infantry, helicopter or artillery loses `FacingInfosModuleDescriptor`". It is written as four `Entire Descriptor` / `Does Not Contain` text tests, such as `"Infanterie",`, plus a `Remove [array]` action. That whole mod is about 90 rules across 19 files.

The **Armory** tab (units, weapons, divisions, battlegroups) is a GUI over the same system. Edits there are saved in the mod and turned into ordinary locked rules at export (`EasyNdf.Data/Units/UnitChangeRules.cs`, `Divisions/DivisionChangeRules.cs`). New vehicles get cloned depiction, ghost and showroom entries (`Units/OwnModel.cs`). New units get deck numbers, and export checks that `DeckSerializer.ndf` names resolve.

### What it does well

- **The writer keeps the file intact** (`Writing/ExportWriter.cs`). It copies the source text and replaces only the values that changed, so comments, spacing and line endings survive. `ndf_parse` reformats whole files, which is why `src/main.py` skips opening files that no editor will touch.
- **It shows changes before writing.** A preview of every change, logs of what each rule matched, and warnings for rules that did nothing.
- **It is good for exploring data.** Every unit, weapon and division can be browsed and compared, units can be viewed in 3D with turrets and firing points, and pressing F1 shows docs for any NDF type or property.
- **It checks for clashes with other mods.** A conflicts viewer shows which mods touch the same values, which matters for WARNO ACTUAL's compatibility with other mods.
- **It warns when the game has updated.** Export notices when `UpdateMod.bat` needs to run first.

---

## 2. What the WARNO ACTUAL patcher covers

| Area | Count |
|---|---|
| Existing-unit edits (`unit_edits`) | 1,844 units |
| New units (`NEW_UNITS`, static `UnitId` >= 50000) | 117 |
| Ammunition entries (`ammunitions`) | 603 |
| Missile entries (`missiles`) | 210 |
| NDF files edited | 118 (46 UI-only) |
| Precomputation builders (`constants_precomputation.py`) | 8 |
| Pattern-standard handlers (units, weapon descriptors, ammo) | about 27 `apply_*` functions |
| Constants (Python) | about 73,600 lines |
| Handlers and editors | about 17,500 lines in `src/gameplay_mods`, 5,000 in `src/ui_mods` |
| Tests | 34 `test_*.py` files |

It also builds the game database from vanilla data (`--rebuild-db`). It writes dev, release, VIP and UI-only targets from one config. It also copies assets, FX and map packs, adds unit meshes, initializes dictionary CSVs, and syncs `config.yaml` with the template.

---

## 3. Why EasyNDF cannot replace it

### 3.1 Standards that join several files after edits

Many standards read one file, decide something, then write another. They must also run at a fixed point relative to the dict edits (see `AGENTS.md`). Examples:

| Standard | Data it combines |
|---|---|
| ATGM infantry team strength | Unit, then its mounts in `WeaponDescriptor.ndf`, then each ammo's `TypeCategoryName` in `Ammunition.ndf`. Runs after `unit_edits` / `new_units`. |
| Infantry WA armor | Final `MaxPhysicalDamages` after the strength standard, then Blindage `Index = max(15 - strength, 1)`. |
| Artillery deployment time | The unit's mounted ammo, resolved through renames and salvo suffixes, then that ammo's radius or damage, giving a 7 s or 15 s tier on the unit. |
| HOBS no-HMD | The unit's final `SpecialtiesList`, then turret arcs and `*_NoOBS` ammo swaps in `WeaponDescriptor.ndf`. |
| Air rocket platform | Whether the unit is a plane or a helicopter, then avion vs non-avion rocket pairs on its mounts. |
| Commander / LDR Capacite | Live TagSet and specialties after edits, then which Capacite replaces `TCommanderModuleDescriptor`. |

EasyNDF's only cross-file rule is **Lookup** (`RuleRunner.RunLookup`). It reads the other file as loaded on the Files tab, not that file's output after rules (`FileRunner.OtherFilesFor`). It makes one hop and only collects names or values to **match** on. It applies fixed actions to the matches and cannot copy a value from the other file. None of the standards above fit that model. A two-hop join (unit, then weapon descriptor, then ammo) or anything that depends on post-edit values is out of reach.

### 3.2 Precomputation from vanilla data and constants

Standards such as AA suppression, CLU bomb dispersion and deployment tiers use `game_db` plus maps built from both the constants dicts and vanilla data. EasyNDF has no database and no build step before rules run. `Variable` rules hold single text or number values, set by hand.

### 3.3 Values that refer to other units

Many edits copy a value from another unit, for example `"CommandPoints": "HMGteam_M60_US"` and `"strength": "HMGteam_M60_US"` in `RFA_unit_edits.py`. Division availability (`"availability": [6, 4, 0, 0]`) is written into division rules in other files. EasyNDF edits set literal values (`Table` rules set values by descriptor name). Every reference would have to be resolved by hand and kept in sync by hand.

### 3.4 Validation

The patcher checks infantry small arms against strength. It checks for duplicate dict keys, using AST scans of the constants files, and for unique `UnitId` values of 50000 or more. Depiction audits warn when equipment changes are not reflected in depictions. EasyNDF's `Check` rule only counts matching descriptors, and its export checks cover deck numbers and battlegroup units. None of WARNO ACTUAL's own checks have an equivalent.

### 3.5 Steps that are not NDF edits

Asset and FX copying, map-pack allowlist copying, unit meshes, dictionary CSV setup, folder layout, and the dev / release / VIP / UI-only targets all sit outside EasyNDF. `File` rules can carry files into a mod. There is no notion of build targets, and no way to pull from Saved Games working folders.

### 3.6 Automation and collaboration

- **Export runs only from the GUI.** The engine is a headless library, but running many files in order, deck checks and file writing all live in the WPF app (`EasyNdf.App/Files/FileRunner.cs`). A script, CI job or the existing `.bat` flow cannot run an export. Using it from Python would mean writing and maintaining a .NET host around the engine.
- **Content would live in one large JSON file** stored in AppData. It can be exported for git, but around 2,800 unit and weapon entries become verbose rule JSON (see the sample above). Reviews and merges between developers would be much harder than with the per-faction Python dicts.
- **Matching relies on searching text.** Conditions such as `"Entire Descriptor" Does Not Contain "\"Infanterie\","` depend on exact NDF formatting. The patcher matches parsed structure: tags, `TypeCategoryName`, module types.

### 3.7 Depictions

The Armory copies depictions only for new **vehicles** with their own model. WARNO ACTUAL also patches infantry depictions with indexed and member edits, selector tactics, aerial carriages and pylons, servant crews, supply-transport tow hooks, and `he_dca` AIR FX. Indexed list `Insert`/`Remove` actions exist, but the rules WARNO ACTUAL depends on (auto-prefixing, reading the donor clone, ordering) would all need to be rewritten as hand-made rules.

### 3.8 Maturity risk

The current WPF app is six weeks old (the project itself dates to October 2025), has one maintainer, no tests and near-daily releases. Its engine must match the JavaScript app's output byte for byte (`EasyNdf.Engine/README.md`). That keeps the two apps consistent, but every engine fix has to land in both. Moving a project of WARNO ACTUAL's size onto it would make WARNO ACTUAL's release schedule depend on a young tool's.

---

## 4. Cost of migrating anyway

A full migration would mean the following:

1. Turning 1,844 unit edits, 117 new units and 813 weapon entries into Armory edits or rules, with every cross-unit reference resolved by hand.
2. Rewriting or dropping more than 20 standards and 8 precompute builders. Most cannot be rules (section 3.1), so they would become hand-kept tables that go stale whenever constants change.
3. Replacing build targets, asset and FX copying, map packs and validation with separate scripts, which brings back the Python tooling the migration was meant to remove.
4. Losing scripted builds and the test suite as safety nets.

The result would be two toolchains, more manual sync, and fewer checks. None of the work is justified by the benefits in section 1.

---

## 5. Options

| Option | Verdict |
|---|---|
| **A. Replace the patcher with EasyNDF** | Not feasible (section 3). |
| **B. Layer EasyNDF rules on top of the patcher's output** | Not recommended. The patcher rebuilds the mod from `sourcemod`, so EasyNDF would have to run again after every build, by hand in the GUI. Balance would live in two places. |
| **C. Use EasyNDF as a dev aid next to the patcher** | **Recommended.** Read-only use: browse and compare units and weapons in the Armory, view 3D models and firing points, read NDF type docs, preview a built mod's files, and check conflicts with other mods. No change to the repo or build. |
| **D. Borrow ideas** | Worth considering separately. Possible areas: a pre-write diff and preview of patched files, `Check`-style assertions ("at least N descriptors matched this standard"), and keeping unchanged text untouched to cut `ndf_parse` whitespace churn. |

### Licensing note (not legal advice)

Using the EasyNDF app to view or export files puts no obligations on WARNO ACTUAL. Bundling or distributing its engine with WARNO ACTUAL tooling would bring in AGPL-3.0 terms and the two extra naming terms. This repo has no `LICENSE` file, so settle licensing before taking that path.

---

## 6. What would change this answer

Re-check if EasyNDF gains all of these:

- a command-line export that runs a whole mod in order without the GUI;
- cross-file rules that read other files **after** their rules have run, can chain lookups, and can copy values across files;
- a way to feed in computed data (a script hook or imported tables) instead of hand-set variables;
- build variants, or rule sets that can be switched on for each target;
- a test suite and a slower, versioned release schedule.

Even then, the per-faction Python constants and their tests probably remain the better place to author and review WARNO ACTUAL's content.

---

## Sources

- EasyNDF repository: <https://github.com/ShadowofChernobyl/EasyNDF> at `3cfcb05`. Files read: `README.md`, `src/EasyNdf.Engine/README.md`, `src/EasyNdf.Data/README.md`, `Rules/Rule.cs`, `Rules/Conditions.cs`, `Rules/RuleRunner.cs`, `NdfEngine.cs`, `EasyNdf.App/Files/FileRunner.cs`, `EasyNdf.App/Startup.cs` / `App.xaml.cs`, `EasyNdf.Data/Units/UnitChangeRules.cs`, `Units/OwnModel.cs`, `Assets/DefaultMod.json`, `.github/workflows/dotnet.yml`, `LICENSE.txt`.
- WARNO ACTUAL: `src/main.py`, `src/editors` (`get_all_editors`), `load_unit_edits()`, `load_new_units()`, `src.constants.weapons` (`ammunitions`, `missiles`), `src/data/constants_precomputation.py`, handler folders under `src/gameplay_mods/generated/gameplay/gfx/*/handlers/`, and `AGENTS.md`.
