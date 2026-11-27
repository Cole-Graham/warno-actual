---
kicker: Feasibility report
title: EasyNDF Feasibility Assessment for WARNO ACTUAL
short_title: EasyNDF feasibility assessment for WARNO ACTUAL
subtitle: Limitations of EasyNDF 1.1.4 compared with the WARNO ACTUAL Python patcher
prepared_for: ShadowofChernobyl, author of EasyNDF
prepared_by: WARNO ACTUAL development team
date: 27 November 2026
version_reviewed: EasyNDF 1.1.4 (commit 3cfcb05, 26 November 2026)
---

# EasyNDF Feasibility Assessment for WARNO ACTUAL

## Executive summary

WARNO ACTUAL is a large WARNO overhaul mod. It is built by a Python patcher that reads the game's NDF files, applies about 2,800 unit and weapon edits plus a set of automatic balance rules, validates the result, and writes the mod. We evaluated whether EasyNDF could replace that patcher, so that more contributors could work on the mod without writing Python.

**Conclusion:** EasyNDF 1.1.4 cannot replace the patcher for a project of this shape. The rule engine is careful, and the Armory, preview and conflict tools are impressive. Simple per-descriptor balance rules port well. What blocks us is architectural, not cosmetic:

1. **Rules can't react to changes in other files.** Rules run on one file at a time. The only cross-file rule, Lookup, reads the other file as it is on disk, before any rules run on it. It makes one hop, and it can only use the other file to choose which descriptors to edit, never to supply a value. About half of our automatic balance rules depend on another file's edited values.
2. **Rules can't use computed data or another unit's values.** There is no stage that builds data before rules run. Values are literals, `{Variable}` text, or a Formula over numbers in the same descriptor. 261 of our unit edits copy a value from another unit, and several of our balance rules use tables computed from vanilla data plus our own constants.
3. **There is no way to build the mod without the GUI.** Export lives in the WPF app. There is no command-line or library entry point for a full export, so builds cannot be scripted, tested or run in CI.
4. **Problems can't stop a build.** A failed `Check` rule is reported as a warning. Our build has about twenty validators, several of which stop the build when a rule of the game engine would be broken.
5. **Large content in one JSON file is hard to work on as a team.** A mod is a single JSON file stored under `%LOCALAPPDATA%`. Our content is split across 316 Python files by faction and topic, reviewed in git, and checked for duplicate keys before each build.
6. **Much of our edit vocabulary has no Armory field.** The Armory covers about twenty unit fields. Our existing-unit edits use 41 kinds of change, and our new-unit definitions use 58.

None of these are criticisms of EasyNDF's purpose. It was built to make repetitive edits easy for modders who don't write code, and it does that well. This report explains each limitation in detail, with the EasyNDF source files we read and the WARNO ACTUAL features affected. Section 6 lists the changes that would make EasyNDF viable for projects like ours, in priority order. The three most valuable would be a headless export, Lookup that reads another file's output after its rules, and values computed from other descriptors.

## 1. Purpose, scope and method

### 1.1 Why we looked at EasyNDF

WARNO ACTUAL's patcher works, but it raises the bar for contributors. Balance designers have to edit Python dictionaries, and new automatic balance rules ("standards") need someone who knows the handler code. EasyNDF offers a visual editor, a rule system that non-programmers can learn, previews of changes, and a conflict viewer. If it could carry our content, it would lower that bar a lot.

### 1.2 What we reviewed

- **EasyNDF:** the public repository at commit `3cfcb05` (version 1.1.4, 26 November 2026). We read the engine (`src/EasyNdf.Engine`), the data layer (`src/EasyNdf.Data`), and the parts of the app that run exports (`src/EasyNdf.App/Files`). Appendix A lists the files.
- **WARNO ACTUAL:** the patcher on our `main` branch, 27 November 2026. Counts in this report come from importing our constants modules and listing the editors the patcher registers, not from estimates.

We did not export WARNO ACTUAL content through EasyNDF. Every statement about EasyNDF's behaviour cites the source file it comes from. If we misread something, we would be glad to be corrected.

### 1.3 How each limitation is described

Each limitation in section 4 follows the same pattern:

- **What WARNO ACTUAL needs:** the feature and why the mod depends on it.
- **What EasyNDF does today:** with references to the source.
- **Impact:** whether it blocks a migration, forces manual work, or is a minor inconvenience.

Suggestions are collected in section 6, so the analysis stays separate from the requests.

## 2. How WARNO ACTUAL is built

### 2.1 Scale

| Area | Count |
|---|---|
| Edits to existing units (`unit_edits`) | 1,844 units, 41 distinct kinds of change |
| New units (`NEW_UNITS`) | 117 units, 58 distinct kinds of setting |
| Ammunition entries | 603 |
| Missile entries | 210 |
| Weapon categories with their own standards | 26 (for example `SAM`, `MANPAD`, `A2A`, `clu_bomb`, `howitzer`) |
| NDF files edited | 118 (46 of them UI-only) |
| Precompute builders | 7, plus one function that runs them all |
| Automatic balance rules (pattern and category standards) | more than 20 |
| Validators run during a build | about 20 |
| Python files of constants | 316 files, about 73,600 lines |
| Handler and editor code | about 17,500 lines (gameplay) and 5,000 lines (UI) |
| Unit test files | 34 |

### 2.2 The build pipeline

A build runs these steps in order:

1. **Load the game database.** A database of vanilla values (units, weapons, ammunition, loadouts, division rules) is built from the game files and cached. It is rebuilt after game updates.
2. **Precompute.** Builders combine the database with our constants into lookup tables. Examples are which ammunition needs deployment time, the AA missile suppression values, and HE autocannon accuracy inherited from the AP gun on the same turret.
3. **Edit files in a fixed order.** For each of the 118 files, the registered editors run in order on a parsed copy of the vanilla file. Inside each file the order is strict. File-wide standards run first, then per-entry category standards, then the hand-written edits, then a few standards that must see the edited values.
4. **Copy assets.** Textures, FX files, unit meshes and allowlisted map packs are copied into the mod.
5. **Validate.** Validators check the constants and the edited data. Some only warn. Others stop the build, for example when an upgrade chain would exceed the engine's limit.
6. **Select a build target.** One source tree produces development and release versions of the gameplay mod and the UI-only mod, plus a VIP build. They differ in folder names, hidden divisions and which editors run.

### 2.3 How content is written

Content lives in Python dictionaries, one file per faction or topic. A typical existing-unit edit:

```python
"HMGteam_MG3_RFA": {  # MG-3 7,62mm
    "CommandPoints": "HMGteam_M60_US",
    "GameName": {"display": "MG3 7.62mm"},
    "strength": "HMGteam_M60_US",
    "max_speed": "HMGteam_M60_US",
    "SpecialtiesList": {"add_specs": "HMGteam_M60_US"},
},
```

Three details in this entry matter for the comparison:

- **Values can name another unit.** `"HMGteam_M60_US"` means "use that unit's final value", after that unit's own edits. 261 values across 259 units are written this way.
- **Edits can be relative.** `add_specs` adds specialties rather than replacing the list, and it can take them from another unit.
- **The entry spans files.** A unit edit can touch `TacticalUnits.ndf`, `WeaponDescriptor.ndf`, division rules, textures and dictionary files. The patcher sends each part to the right file.

A typical weapon entry, keyed by name, category and flags:

```python
("AutoCanon_HE_30mm_M230", "autocannon", None, False): {
    "Ammunition": {
        "hit_roll": {"Idling": 40, "Moving": 40},
        "parent_membr": {"PhysicalDamages": 0.3, "SuppressDamages": 30,
                         "TimeBetweenTwoSalvos": 1.5, "ShotsCountPerSalvo": 20},
    },
    "WeaponDescriptor": {"Salves": 40},
},
```

The `WeaponDescriptor` part is not one descriptor. It sets the salvo count on every loadout in the game that mounts this ammunition, at the index of the ammo box that mount uses.

### 2.4 Standards and ordering

A **standard** is a balance rule applied automatically. There are two kinds:

- **Category standards** apply by weapon category. For example, all `MANPAD` missiles get the same time between salvos, and all `SEAD` missiles get the same anti-radiation settings.
- **Pattern standards** find descriptors by traits, type category, caliber, name or range. For example, aim time is set from `TypeCategoryName` plus the current aim time, and HE damage is set by caliber.

The ordering rule is strict. Standards run before hand-written edits, so the edits can override them. A few standards deliberately run after edits because they must see the final values. Infantry armor reads final strength, and cluster bomb dispersion reads the final blast radius. In several cases the order spans files. A unit standard in `TacticalUnits.ndf` can depend on edits made in `WeaponDescriptor.ndf`, which depend on edits made in `Ammunition.ndf`.

## 3. EasyNDF as we understand it

### 3.1 Architecture

EasyNDF is a C# WPF application on .NET 10, in three projects:

- **`EasyNdf.Engine`** (no UI) parses NDF, runs one file's rules, and writes the result. It is a port of the HTML app's JavaScript engine and must give byte-for-byte the same output (`src/EasyNdf.Engine/README.md`).
- **`EasyNdf.Data`** handles storage, mod files, and the Armory's conversion of unit, weapon and division edits into rules.
- **`EasyNdf.App`** is the WPF app, including the export runner (`Files/FileRunner.cs`) and shared variables (`Files/SharedVariables.cs`).

### 3.2 The rule model

A mod holds rule sets, usually one per game file. Each rule has a kind, conditions, actions and optional parameters (`Rules/Rule.cs`). The kinds are Edit, Add, Clone, Remove, Replace, Scale, Formula, Table, Lookup, Check, Group and Variable, plus Text and File for dictionary entries and carried files.

- **Conditions** test a property found by name at any depth, a list item by index, the descriptor's name or type, or the descriptor's whole canonical text (`Rules/Conditions.cs`). Operators include text tests (`Starts With`, `Contains`, `Contains Any Of`, ...) and number comparisons.
- **Actions** change every value of a target property. Targets can be paths: `Outer > Inner` finds Inner under Outer at any depth, `> A > B` is anchored at the descriptor, and `[Key]` picks one list entry (`Rules/ActionApplier.cs`). Operators include Set To, arithmetic, text Append/Prepend/Remove, list Insert/Replace/Remove, and Add or Remove Property.
- **Scope:** some kinds can work on every object of one type inside descriptors, or on the file's top-level constants, instead of on descriptors (`RuleRunner.Scope`).
- **Variables:** `{Name}` is substituted into values. A Variable can belong to one rule set, to the whole mod, or to all mods. An Edit action aimed at `{Name}` changes it for the rules and files that run after (`SharedVariables.cs`).

### 3.3 The Armory

The Armory edits units (name, nation, role, factory, picture, cost, strength, four armor values, speeds, optics, vision, stealth, fuel, specialties, divisions, loadout) and weapons, and creates new units and divisions. Its edits are stored in the mod and turned into ordinary locked rules at export (`Units/UnitChangeRules.cs`, `Divisions/DivisionChangeRules.cs`, `Weapons/LoadoutRules.cs`). New vehicles with their own model get copied depiction, ghost and showroom entries (`Units/OwnModel.cs`). Export checks that every division and unit named in `DeckSerializer.ndf` exists, and gives new units the next free deck number.

### 3.4 Strengths

We want to be clear about what EasyNDF does better than our patcher:

- **The writer keeps the file intact.** `ExportWriter` copies the source and replaces only changed values, so comments, spacing and line endings survive. Our parser reformats whole files, so we avoid opening files no editor touches.
- **Every change can be seen before writing.** The preview shows each change before export, logs record what each rule matched, and a warning appears when a rule matched nothing.
- **It shows clashes with other mods.** The conflict viewer shows which mods touch the same values. Nothing in our tooling does this.
- **It is good for exploring data.** The Armory browses and compares units, the 3D viewer shows turrets and firing points, and F1 opens docs for NDF types and properties.
- **It is careful about game updates.** Export notices when `UpdateMod.bat` needs to run, and Clone can take a descriptor from the game's own file when an earlier mod removed it.
- **The engine is careful.** It matches JavaScript number formatting, compares strings ordinally, and copies descriptors before changing them.

## 4. Limitations in detail

### 4.1 Rules can't see edits made in other files

#### 4.1.1 What WARNO ACTUAL needs

Many of our standards decide what to do in one file by reading another file after that file's edits have run. The most important case is a unit rule that depends on what the unit carries:

```text
TacticalUnits.ndf     unit X                 (after unit edits)
  -> WeaponDescriptor.ndf  X's loadout      (after remounts and new units)
    -> Ammunition.ndf      each mounted ammo (after weapon edits)
```

#### 4.1.2 What EasyNDF does today

- **Each file runs separately.** The engine loads one file and runs that file's rules in list order (`NdfEngine.Load`, `RuleRunner.Run`). `SharedVariables.cs` says directly that "a file's rules still run file by file".
- **Lookup reads the other file before any rules.** `FileRunner.OtherFilesFor` passes the listed file's text from disk or archive (`FileContent.Text`), not the output of rules run on it. A Lookup into `WeaponDescriptor.ndf` therefore sees vanilla loadouts, not our remounts.
- **Lookup makes one hop.** `RuleRunner.RunLookup` collects names or values from descriptors in one other file that pass its source conditions. A Lookup cannot feed another Lookup, so unit, then loadout, then ammunition cannot be expressed.
- **Lookup only filters.** The values it collects decide which descriptors here get the rule's actions. The actions themselves are literal. Lookup cannot write "set this unit's X to the other descriptor's Y".
- **Shared variables can't hold descriptor values.** An action aimed at `{Name}` can set a literal or do arithmetic, and can run once per match, so counters work. Nothing reads a descriptor's property into a variable.

#### 4.1.3 Worked example: ATGM infantry team strength

The rule: a dedicated anti-tank team whose loadout contains ammunition with type category `JTOYRAARTS` (anti-tank missile) gets strength 4 if it has the `infantry_equip_veryheavy` specialty, otherwise strength 3. Recoilless-rifle teams are excluded. Units whose author set `strength` by hand are skipped. The value is written to `MaxPhysicalDamages`, and `SoldierCount` and the infantry armor index are updated when present.

Trying to express it in EasyNDF:

1. **Ammunition to missile names.** A Lookup in `WeaponDescriptor.ndf` could collect `Ammo_*` names whose `TypeCategoryName` is `JTOYRAARTS`. Its result stays inside `WeaponDescriptor.ndf` and cannot reach `TacticalUnits.ndf`.
2. **Loadout to unit.** A Lookup in `TacticalUnits.ndf` could collect loadout names from `WeaponDescriptor.ndf` whose mounts contain one of those ammo names. Step 1 cannot feed it, so the list of missile ammunition would have to be typed into a `Contains Any Of` condition by hand and kept up to date.
3. **Edits are invisible.** Both Lookups read vanilla text, so a team remounted with a missile by our edits would be missed, and one whose missile we removed would still match.
4. **The author's intent is invisible.** "Skip units whose author set strength by hand" depends on what our constants say, not on NDF data. EasyNDF has no concept of it.

Result: the rule can only be approximated, with a hand-kept list of names, and it gives wrong answers for every unit our edits remount.

#### 4.1.4 Other standards, graded

We graded every automatic standard against EasyNDF's rule kinds. "Yes" means one file's rules can express it. "Partly" means it works with hand-kept lists or extra manual steps. "No" means it can't be expressed.

| Standard | Data it needs | Fits EasyNDF? |
|---|---|---|
| Aim time by type category | One ammunition descriptor | Yes (Edit) |
| Weapon range remaps | One ammunition descriptor | Yes (Edit) |
| Canon HE damage by caliber | One ammunition descriptor | Yes (Edit, name conditions) |
| HE bomb damage by weight class | One ammunition descriptor | Yes (Edit) |
| Tandem charge inversion | One ammunition descriptor | Yes (Edit) |
| Cluster bomb dispersion | Final blast radius, ratio per salvo length | Mostly (Formula; one rule per salvo-length variant) |
| Shock units lose `_resolute` | One unit (skills, specialties) | Yes (Edit) |
| Commander module to Capacite | One unit (tags, specialties) | Mostly (Edit with list actions) |
| Infantry WA armor index | Final strength, after the ATGM standard | Formula fits; its input does not (4.1.3) |
| ATGM team strength | Unit, loadout, ammunition | No |
| Artillery deployment time | Unit, loadout, ammunition radius and damage, renames | No |
| HOBS missiles without helmet sight | Unit specialties, then turret arcs and ammo swaps | No |
| Air rocket platform | Plane or helicopter, then avion or non-avion rocket pairs | No |
| Helicopter AA turret angles | Unit is a helicopter and the mount is an AA missile | No |
| HE DCA air clones and mounts | Damage family of every DCA weapon, then a clone and a mount per turret | No |
| HE autocannon accuracy inheritance | AP gun on the same turret, then its hit roll | No |
| AA missile suppression | Final physical damage, then our damage-to-suppression table | Partly (one rule per table row; see 4.3) |
| CLU SOL traits | Damage family in the same descriptor | Yes (one Edit rule per family) |
| Infantry magazine salvo remounts | Salvo-length variants and each unit's loadout | No |

Single-descriptor balance rules port well. Rules that relate a unit to what it carries do not, and those are the rules that keep a mod of 1,900+ units consistent.

#### 4.1.5 Impact

**Blocking.** About half of our standards cannot be expressed. Approximations would need hand-kept name lists that go stale with every content change, which is the problem the standards exist to solve.

### 4.2 No ordering across files

**What WARNO ACTUAL needs.** A standard sometimes has to run after another file's edits. Air rocket remounting runs after the hand-written loadout edits, so intentional remounts are kept. Infantry armor runs after ATGM team strength.

**What EasyNDF does today.** Rule order inside a file is list order, and mods and rule sets run in the Mods tab's order. Files have no dependencies on each other. The only ordering that crosses files is shared variables, which follow mod, rule-set and file order (`SharedVariables.Build`). Since variables can't carry descriptor values (4.1.2), this does not help.

**Impact.** Blocking, together with 4.1.

### 4.3 No computed data and no references between values

#### 4.3.1 No step that runs before the rules

Our precompute builders produce tables that the standards read while editing:

| Builder | What it produces |
|---|---|
| `build_deployment_time_units` | Ammunition and units that keep deployment time, and a 7 s or 15 s tier per unit. The engine requires a deployment module whenever any mounted ammo has deployment time. |
| `build_aa_suppress_damages` | Suppression damage per AA missile, from final physical damage (constants override vanilla) |
| `build_clu_bomb_dispersion` | Dispersion per cluster bomb, from constants or standard ratios |
| `build_he_dca_weapons` | Final damage family per DCA weapon, to drive automatic `_AIR` clones |
| `build_canon_he_accuracy_inheritance` | Hit roll for each HE gun, inherited from the AP gun on the same turret |
| `build_extended_upgrade_from_mapping` | Upgrade chains across vanilla, edited and new units, validated against the engine's limit |
| `build_ammunition_renames` | Renames, each checked against the database |

EasyNDF has nowhere to compute data before rules run. Variables are set by hand (`RuleRunner.CollectVariables`). Table rules accept pasted CSV text (`Rules/TableText.cs`), which could hold a computed table, but something outside EasyNDF would have to make it, and someone would have to paste it in again after every change.

#### 4.3.2 Formula works inside one descriptor

The Formula rule supports numbers, property names, `+ - * /`, brackets, and `min`, `max`, `abs`, `floor`, `ceil` and `round` (`Rules/Formula.cs`). A name is a variable holding a number, or the first plain number found anywhere in the descriptor under that property name (`RuleRunner.RunFormula`). That covers many single-descriptor calculations, such as the infantry armor index `max(15 - MaxPhysicalDamages, 1)`. It cannot:

- read a value from another descriptor or file;
- choose between values (no conditional), except with separate rules and conditions;
- pick which of several properties with the same name to read, for example the `Index` of one particular armor descriptor;
- produce text or references.

#### 4.3.3 Values that name another unit

261 of our unit edit values name another unit, as in `"CommandPoints": "HMGteam_M60_US"`, meaning "the same cost as that unit, after its own edits". Specialty additions can also come from another unit. EasyNDF actions take literal values (with `{Variable}` substitution), so each one would have to be looked up by hand and typed in. Any later change to the source unit would then have to be repeated by hand in every unit copying it.

#### 4.3.4 Impact

**Blocking** for the standards that depend on precomputed tables. **Expensive** for references between units: they can be done by hand, but drift is guaranteed.

### 4.4 Finding the right value

#### 4.4.1 Conditions match property names at any depth

Actions accept paths (`Outer > Inner`, `> A > B`, `[Key]`), but conditions do not. `Conditions.CandidatesFor` collects every value of the named property anywhere in the descriptor, or one item of a list by index. In a unit descriptor, names like `Index`, `Name`, `Family` or `Value` appear in several modules. A condition on one of them matches if any occurrence passes, which is often not what is wanted.

#### 4.4.2 Type scope hides the rest of the descriptor

With type scope, the rule works on each object of a given type, wrapped in a stand-in that has the descriptor's title but only that object as its value (`RuleRunner.Scope.StandIn`). Conditions then see only that object. A rule like "for each `TBaseDamageModuleDescriptor` of a unit whose `TagSet` contains `Infanterie`" cannot be written, because `TagSet` lives in a different module. The only link back to the parent is the descriptor's title.

#### 4.4.3 Matching on whole-descriptor text depends on formatting

When there is no suitable property, rules fall back to `Entire Descriptor` text tests. The bundled WARNO Tactical Overhaul mod tells ground units apart by testing that the whole text does not contain `"Air",`, `"Infanterie",`, `"Helo",` or `"Artillerie",`. That works, but it depends on how the canonical writer formats lists, and it can match the same text in an unrelated property. Our handlers match on parsed structure, such as a tag in the unit's `TagSet` or a module of a given type.

#### 4.4.4 Edits that depend on another value in the same descriptor

Setting the salvo count for one weapon means finding the mount whose `Ammunition` is that weapon, reading its ammo box index, and then editing that position in the loadout's `Salves` list. The Armory does this when you edit one unit's loadout (`Weapons/LoadoutRules.cs`). No rule kind can say "in every loadout that mounts X, set the matching ammo box to N". Our weapon entries do exactly that, and 125 of them carry a `WeaponDescriptor` part, while 615 units carry loadout edits.

#### 4.4.5 Impact

**Serious.** Each of these limits can be worked around for one case. Across our content, the workarounds become a large set of per-unit rules that nobody can review.

### 4.5 Generated descriptors and variants

#### 4.5.1 What WARNO ACTUAL generates

Many descriptors are not written by hand but made from patterns:

- **Salvo-length variants.** `Ammo_X_salvolength4` and similar copies, with timing changed for the new magazine size.
- **Automatic `_AIR` clones.** One per HE DCA weapon, then a mount for it on every turret that carries the original.
- **`*_NoOBS` ammunition and helmet-sight turret variants**, created for every unit that carries a high off-boresight missile without a helmet sight.
- **Companion mounts.** An anti-tank satchel charge next to every satchel charge.
- **New units across many files.** Each of our 117 new units sets explicit GUIDs (unit, infantry squad module, showroom, cadaver), a static deck number, depictions (infantry, vehicle, aerial), crew meshes for towed equipment, selector tactics, division availability and textures.

#### 4.5.2 What EasyNDF does today

Clone copies one named descriptor inside one file, with stable new GUIDs, and applies the rule's actions to the copy (`RuleRunner.RunClone`). There is no "for each descriptor matching these conditions, make a clone named by this pattern". Every variant would need its own Clone rule. Wiring a clone into other files (loadouts, depictions, textures) needs separate rules in those files, written by hand. The Armory automates this for new vehicles with their own model. Our infantry depiction edits, aerial carriages, crew meshes, supply-transport tow hooks and selector tactics are outside what it generates.

#### 4.5.3 Impact

**Serious.** Generated variants would become hundreds of hand-written rules, and adding one weapon would mean finding and updating every rule that should now include it.

### 4.6 Armory coverage of our edits

The Armory's editable unit fields are listed in `Units/UnitChanges.cs` (`UnitField`). Our existing-unit edits use 41 kinds of change. These are the most common, with how often each is used:

| Our edit key | Uses | Armory field |
|---|---|---|
| `CommandPoints` | 1,819 | Cost |
| `availability` | 1,496 | Division editor (per division) |
| `SpecialtiesList` | 869 | Specialties (whole list; no add from another unit) |
| `WeaponDescriptor` | 615 | Loadout (swap, count, salvos, add, remove) |
| `max_speed` | 583 | Speed |
| `GameName` | 448 | Name |
| `Divisions` | 408 | Divisions |
| `UpgradeFromUnit` | 316 | None found |
| `strength` | 289 | Strength |
| `TagSet` | 204 | None (read for filters) |
| `ECM` | 177 | None |
| `capacities` | 160 | None |
| `UnitRole` | 126 | Role |
| Unit textures (identified, unidentified, menu, transported) | 63 to 124 each | Picture (one texture) |
| `optics` | 124 | Optics |
| `remove_zone_capture`, `TypeStrategicCount`, `armor` (custom armor), `Supply`, `modules_remove`, `orders`, `XP`, `AirplaneMovement`, `tow_only`, `DeploymentShift`, `selector_tactic`, mesh alternatives | 3 to 120 each | None |

Everything without an Armory field would become a generic Edit rule per unit, or a rule per value shared by many units. 897 of our 1,844 edited units use at least one kind of change the Armory has no field for.

**Impact.** Serious for the people who would gain most from EasyNDF. Balance designers would be back to writing raw rules for a large part of their work.

### 4.7 Divisions and decks

EasyNDF's division generator writes division rules, decks, deck packs, the cost matrix, division textures and the deck serializer (`Divisions/DivisionChangeRules.cs`, `DivisionExtras.cs`). That covers much of what we need. The gaps are smaller here:

- **Coalitions.** Our East Germany, Poland and Czechoslovakia tables are kept separately and merged into combined NSWP divisions at build time. EasyNDF has no notion of a division assembled from other tables.
- **Consistency checks.** We warn when the same unit has different per-veterancy availability in different divisions, and when a transport override names a transport no division rule allows. We also validate the default multiplayer decks against division rules and activation limits.
- **Deck numbers.** New units get the next free number, stored in the mod (`Mod.UnitDeckNumbers`, `FileRunner`). We reserve 50000 and above for new units, so a game update that adds units never takes one of our numbers. EasyNDF handles that clash after the fact (`FileRunner`, around line 496). A configurable base number would avoid it.

**Impact.** Moderate. Divisions are the area where EasyNDF is closest to our needs.

### 4.8 Validation and stopping the build

Our validators include infantry small arms against squad strength, ammo shown per salvo against shots fired, aircraft vision against weapon range, upgrade chain length (which stops the build), duplicate keys in the constants files (found by scanning the source, since Python silently keeps the last one), unique and correctly ranged unit IDs, duplicate GUIDs, UI texture and fire-effect references, and depiction coverage after equipment changes.

EasyNDF's `Check` rule counts matching descriptors and compares the count to an expected number (`RuleRunner.RunCheck`). A failure is reported as a warning, and we found no path where it stops the export. Value checks at export (`Editing/ExportValueCheck.cs`) and deck checks are useful but specific to EasyNDF's own concerns. Nothing lets a mod define a check that compares two properties, compares across files, or stops the export.

**Impact.** Blocking for us. Several of our checks guard rules of the game engine, and breaking them produces a mod that fails to load or behaves wrongly in ways that are hard to trace.

### 4.9 Builds without the GUI

#### 4.9.1 What WARNO ACTUAL needs

A build is one command, run from a terminal or a batch file, and it can be re-run in CI. Unit tests import the same code. Contributors on different machines get the same output from the same commit.

#### 4.9.2 What EasyNDF does today

- **The only command-line options are display options.** They are `--render software` and `--frame native` (`App.xaml.cs`).
- **Export lives in the app project.** Ordering files, stacking mods, shared variables, Armory rule generation, deck checks and writing files are all in `EasyNdf.App/Files/FileRunner.cs` (about 1,650 lines) and its neighbours. The engine alone can run one file's rules. Re-creating a full export outside the app would mean re-implementing that logic and keeping it in step with every release.
- **It runs on Windows only.** The WPF app builds and runs only there.
- **There are no tests.** The solution has no test project, and CI runs `dotnet build` only.

#### 4.9.3 Integration and licensing

Without a command-line export, the only way to automate EasyNDF would be to host its engine and data libraries in our own tool. EasyNDF is AGPL-3.0 with additional naming terms, so a tool linked to it would take on those obligations. Calling a separate EasyNDF command-line program would avoid that question for projects that prefer another license.

#### 4.9.4 Impact

**Blocking.** Without a headless export we cannot script builds, run them in CI, or test our content.

### 4.10 Build targets and work outside NDF

**What WARNO ACTUAL needs.** One source produces development and release versions of the gameplay and UI-only mods, plus a VIP build. Each has its own folder name and hidden divisions and runs a different set of editors. Builds also copy textures, FX, unit meshes and map packs (allowlisted, copied only when the source is newer, with unlisted files removed), set up dictionary CSV files, and keep the developer's config file in sync with the shared template.

**What EasyNDF does today.** Rules and rule sets can be switched on or off by hand, and Group rules can switch off what they contain. There is no named build profile that selects rule sets and output folders. File rules carry files into a mod, stored once by content in the app's data folder (`AppFolders.ModFiles`), which suits a few pictures but not a tree of assets maintained outside EasyNDF.

**Impact.** Moderate. Each item has a manual or external workaround, but together they bring back the separate tooling a migration was meant to remove.

### 4.11 Source control and team work

**What WARNO ACTUAL needs.** Several developers edit content at once. Changes are reviewed as diffs in git, conflicts are merged by hand, and content is split by faction and topic so that people rarely edit the same file.

**What EasyNDF does today.** A mod is one `.mod.json` file under `%LOCALAPPDATA%\EasyNDF\Mods` (`EasyNdf.Data/README.md`). It can be exported and imported, so it can live in git, but:

- **It is one large file.** All rule sets and Armory edits are in one JSON document, so two people editing different factions still edit the same file.
- **Rules are verbose.** In the bundled mod, an Edit rule with one condition and one action is 38 lines of JSON, and the median Edit rule is 55, much of it default fields. Our 2,800 entries would produce a very large file whose diffs are hard to read.
- **Generated rules may churn.** Armory rules are locked and generated again whenever the mod's units change (`UnitChangeRules`). We have not measured it, but generated rules in a shared file are a common source of noisy diffs and merge conflicts.
- **Merges are not checked.** Python dictionaries also have this problem, which is why we scan for duplicate keys. A JSON merge that duplicates or drops a rule would not be caught.

**Impact.** Serious for a team. It may be minor for a solo modder, who is EasyNDF's main audience.

### 4.12 Game updates

**What WARNO ACTUAL needs.** After a game update we rebuild the database, check our renames against it, and let the validators report names that no longer exist.

**What EasyNDF does today.** It checks whether `UpdateMod.bat` must run first (`Files/GameUpdateCheck.cs`), notes rules that matched nothing, and can clone from the game's own file. Check rules can assert that a rule still matches. This is real help. The gap is the same as in 4.8: nothing stops the build, and nothing checks references across files.

**Impact.** Minor to moderate.

### 4.13 Project maturity

The repository goes back to October 2025, with the original WinForms app now on the `archive/winforms` branch. The current WPF app started on 14 October 2026 and has had 57 commits and eight releases since, all from one maintainer. That pace shows dedication, and we don't hold it against the project. For a mod of our size, though, moving the whole build onto a fast-changing tool without tests carries risk. The need to match the HTML engine byte for byte also means every engine fix has to be made twice. A test suite for the engine, using small NDF files and expected output, would reduce the risk for every user, not only for projects like ours.

## 5. Capability matrix

| Capability | WARNO ACTUAL patcher | EasyNDF 1.1.4 | Gap |
|---|---|---|---|
| Edit values in one descriptor | Yes | Yes | None |
| Paths to nested values in actions | Yes (parsed structure) | Yes (`>` paths, `[Key]`) | None |
| Paths in conditions | Yes | No (name at any depth) | Medium |
| Conditions on another module of the same descriptor, with type scope | Yes | No (only the title) | Medium |
| Read another file | Yes, after its edits | Lookup, before its rules | High |
| Chain lookups across files | Yes | No | High |
| Copy a value from another descriptor | Yes | No | High |
| Precomputed tables from vanilla data and constants | Yes (7 builders) | No | High |
| Formula within one descriptor | Yes | Yes | None |
| Generate variants by pattern | Yes | No (one Clone per variant) | High |
| New units across many files | Yes | Yes for vehicles; partly otherwise | Medium |
| Divisions, decks, deck numbers | Yes | Yes | Low |
| Coalition divisions from other tables | Yes | No | Low |
| Checks that stop the build | Yes | No (warnings) | High |
| Checks across files or properties | Yes | No | High |
| Build without the GUI or in CI | Yes | No | High |
| Several build targets from one source | Yes | No | Medium |
| Asset, FX and map-pack copying | Yes | File rules only | Medium |
| Content split across many files for git | Yes | No (one mod file) | Medium |
| Writer that leaves unchanged text alone | No | Yes | EasyNDF ahead |
| Preview of each change | Partial (logs) | Yes | EasyNDF ahead |
| Conflict detection with other mods | No | Yes | EasyNDF ahead |
| Data browser and 3D viewer | No | Yes | EasyNDF ahead |

## 6. What would make EasyNDF viable for projects like ours

These are offered as suggestions, in the order we think they would help most. Some are large, and we understand they may not fit EasyNDF's direction.

### 6.1 Essential

#### 6.1.1 A command-line export

Something like `EasyNDF.exe export --mod "My mod.mod.json" --game "<path>" --out "<folder>"`, running the same export as the GUI, with a non-zero exit code on errors. Moving the export runner out of the WPF project into a library would make this possible, and would also let others write tests against it.

#### 6.1.2 Lookup that reads another file's output

An option on Lookup to read the other file after its rules have run. That needs a file order, either worked out from which files Lookup rules read or set by hand. With it, cross-file standards would see edited data rather than vanilla.

#### 6.1.3 Values computed from other descriptors

A way for an action's value to come from another descriptor, in this file or another, for example a reference form in the value box:

```text
{ref: WeaponDescriptor.ndf / WeaponDescriptor_{Title} > Salves[0]}
{ref: TacticalUnits.ndf / Descriptor_Unit_HMGteam_M60_US > ProductionRessourcesNeeded > [~/Resource_CommandPoints]}
```

This sketch is only illustrative. Even same-file references would cover "copy that unit's cost". With 6.1.2, cross-file references would cover most of our standards.

#### 6.1.4 Checks that can stop the export

An option on Check to mark a failure as an error that stops the export (or makes the command-line export fail), and a way to check a value against another value, not only to count matches.

### 6.2 Important

#### 6.2.1 Paths in conditions

The same `Outer > Inner` and `> A > B` syntax that actions accept, so a condition can name one property among many with the same name.

#### 6.2.2 Parent conditions in type scope

With type scope, let conditions also test the parent descriptor, for example a `Parent:` prefix, so "every armor descriptor of an infantry unit" can be written.

#### 6.2.3 Clone by pattern

A Clone rule that takes conditions and a naming pattern (`{Title}_AIR`, `{Title}_salvolength4`) and makes one clone per match, applying its actions to each. Combined with Lookup, it would cover most of our generated variants.

#### 6.2.4 Imported data tables

Let a Table or Variable rule read a CSV or JSON file from a path instead of pasted text, read again at every export. An external tool could then compute data, and EasyNDF would apply it.

#### 6.2.5 Build profiles

Named profiles that select rule sets and output folder, for example "release" and "development", so one mod can produce several builds.

### 6.3 Helpful

- **Split mod files.** Save a mod as a folder with one file per rule set, and leave default fields out of the JSON, so mods diff and merge well in git.
- **Reserved deck numbers.** A setting for the first deck number given to new units.
- **Engine tests.** A small test project with NDF input, rules and expected output, which would also protect HTML parity.
- **A scripting hook.** A documented way to run a user script before or after a rule set, for the rare cases rules cannot express.

## 7. Where EasyNDF already helps us

We plan to use EasyNDF next to our patcher:

- **Inspection.** Browsing and comparing units and weapons, viewing models, turrets and firing points, and reading NDF docs with F1.
- **Checking our output.** Opening a built WARNO ACTUAL mod to look over changed files, and checking conflicts with other popular mods.
- **Prototyping.** Designers can try a balance idea as an EasyNDF rule on vanilla files before we write it into our constants.

We would also like to adopt two of EasyNDF's ideas: a writer that leaves unchanged text alone, and a preview of every change before writing.

## 8. Conclusion

EasyNDF is a well-made tool for its purpose. It makes repetitive NDF edits easy and safe for modders who don't write code, and it has features we lack. WARNO ACTUAL needs a build system more than an editor. Its balance depends on rules that read edited data across files, on computed tables and references between units, on checks that stop bad builds, and on builds that run without a person at the keyboard. EasyNDF 1.1.4 does not offer those today, and approximating them would mean hand-kept lists across about 2,800 entries. That is the work our patcher exists to remove.

Of the changes in section 6, a headless export, Lookup that reads another file's output, and computed values would change our assessment the most. We would be happy to test early versions of any of them against WARNO ACTUAL's content.

## Appendix A. EasyNDF source references

All paths are relative to the EasyNDF repository at commit `3cfcb05`.

| File | What we relied on |
|---|---|
| `README.md`, `src/EasyNdf.Engine/README.md`, `src/EasyNdf.Data/README.md` | Architecture, HTML parity, data folders, license |
| `src/EasyNdf.Engine/NdfEngine.cs` | One file loaded per engine run |
| `src/EasyNdf.Engine/Rules/Rule.cs` | Mod, rule set, rule, condition and action model; rule kinds |
| `src/EasyNdf.Engine/Rules/Conditions.cs` | Condition operands and operators; matching by name at any depth |
| `src/EasyNdf.Engine/Rules/ActionApplier.cs` | Action operators; target paths, anchored paths and `[Key]` entries |
| `src/EasyNdf.Engine/Rules/RuleRunner.cs` | Rule order, scope and stand-ins, Clone, Lookup, Formula, Table, Check |
| `src/EasyNdf.Engine/Rules/Formula.cs` | Formula syntax and functions |
| `src/EasyNdf.Engine/Rules/TableText.cs` | Table rule input (pasted CSV, semicolon or tab text) |
| `src/EasyNdf.App/Files/FileRunner.cs` | Export orchestration; Lookup's other-file text; deck checks |
| `src/EasyNdf.App/Files/FileContent.cs` | Other files read from disk or archive |
| `src/EasyNdf.App/Files/SharedVariables.cs` | Variable scopes; files still run one by one |
| `src/EasyNdf.App/App.xaml.cs` | Command-line switches |
| `src/EasyNdf.Data/Units/UnitChanges.cs`, `UnitChangeRules.cs`, `OwnModel.cs` | Armory unit fields, generated rules, vehicle depictions |
| `src/EasyNdf.Data/Weapons/LoadoutChange.cs`, `LoadoutRules.cs` | Loadout changes per unit |
| `src/EasyNdf.Data/Divisions/DivisionChangeRules.cs` | Files written for divisions |
| `src/EasyNdf.App/Assets/DefaultMod.json` | Size and style of a real mod's rules |
| `.github/workflows/dotnet.yml`, `EasyNDF.slnx` | CI and the lack of a test project |

## Appendix B. WARNO ACTUAL inventory

### B.1 Standards

| Group | Standards |
|---|---|
| Ammunition, applied to the whole file | Aim time, weapon range, HE bomb damage, canon HE damage, CLU SOL traits, infantry MMG close-combat trait, tandem charge inversion, damage families, fire descriptors, missile acceleration and movement |
| Ammunition, by category | AA missile hit roll and suppression, SEAD, MANPAD and SAM time between salvos, bombs, cluster dispersion, artillery deployment flag |
| Ammunition, generated | Salvo-length variants with magazine timing, HE DCA `_AIR` clones |
| Weapon descriptors | HOBS without helmet sight, default salvos, ammo quantity updates, HE DCA air mounts, satchel AT companion mounts, air rocket platform, helicopter AA turret angles, infantry magazine remounts |
| Units | Commander Capacite, ATGM team strength, infantry WA armor, shock units without `_resolute`, artillery deployment time, helicopter movement |

### B.2 Validators

| Validator | Checks |
|---|---|
| Infantry small arms vs strength | Countable small arms match squad size minus occupied slots |
| Ammunition consumption | Ammo shown per salvo equals shots per salvo times simultaneous shots |
| Aircraft vision vs weapon range | Standard vision covers the longest weapon range |
| Upgrade chain length | No chain exceeds the engine's limit (stops the build) |
| No multiple ancestors | A unit is not upgraded from two parents |
| Duplicate keys in constants | Found by scanning the Python files, since Python keeps the last key silently |
| Unit IDs and GUIDs | New units have unique IDs of 50000 or more and unique GUIDs |
| Division availability consistency | Same per-veterancy availability for a unit in every division |
| Transport overrides | Overrides only name transports that division rules allow |
| Default multiplayer decks | Decks respect division rules and activation limits |
| UI textures and fire effects | Texture fields and infantry fire effects in constants match vanilla data |
| Depiction audit | Equipment changes have matching infantry depiction edits |
| Small arms quantity variants | Unit edits and new units only use valid quantity variants |

## Appendix C. Glossary

| Term | Meaning |
|---|---|
| NDF | Eugen Systems' text format for game data |
| Descriptor | A named object in an NDF file, such as a unit, weapon or ammunition |
| Loadout | A unit's `WeaponDescriptor`: its turrets, mounted weapons and ammo boxes (`Salves`) |
| Standard | An automatic balance rule applied by the patcher across many descriptors |
| Category standard | A standard chosen by a weapon's category in our constants, such as `MANPAD` |
| Pattern standard | A standard chosen by scanning descriptors for traits, names, calibers or type categories |
| Hand-written edits | The per-unit and per-weapon dictionaries in our constants (`unit_edits`, `NEW_UNITS`, `ammunitions`, `missiles`) |
| Precompute | A build step that combines vanilla data and constants into tables used while editing |
| Salvo-length variant | A copy of an ammunition with a different magazine size, named `_salvolength{N}` |
| HOBS | High off-boresight missile, able to engage targets well off the aircraft's nose |
| HMD | Helmet-mounted display, which lets the pilot cue a HOBS missile by looking at the target |
| WA armor | Our infantry armor family, `ResistanceFamily_infanterieWA`, whose index follows squad strength |
| NSWP | Our combined Warsaw Pact division, built from the East German, Polish and Czechoslovak tables |
