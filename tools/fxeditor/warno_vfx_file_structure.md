# Warno VFX NDF file structure and positioning

This document describes how **simultaneous-action** VFX are expressed in Warno’s **NDF** (Eugen’s data format) as seen in extracted game files such as `fx_impact_sol_HE_M270_227mm_Cluster_1.ndf`. It is meant to be **engine-accurate** for tooling: parsing, validation, and safe edits.

The runtime is not documented here; this is the **on-disk shape** that `ndf_parse` / `src.ndf` round-trips.

---

## 1. Top-level shape

A typical impact / cluster file exports **one** object:

```text
export <SymbolName> is SimultaneousActionDeclaration
(
    Params = [ ... ]      // declaration-level aliases (typed parameters)
    Actions = ActionList is
    [
        TSimultaneousAction ( ... ),
        TSimultaneousAction ( ... ),
        ...
    ]
)
```

- **`SimultaneousActionDeclaration`**: callable VFX “program” with a parameter block and a flat list of child actions.
- **`Params`**: list of `TActionAlias` rows (e.g. `parPosition`, `parRadiusPhysical`, `parDirection`). These are the **only** values the game passes in from outside; layout inside the file is expressed relative to them.
- **`Actions`**: ordered list of **`TSimultaneousAction`** rows. Each row is one **parallel bundle** (see §4). The list order is authoring order, not necessarily time order.

---

## 2. Declaration parameters (`Params`)

Common aliases in cluster / impact effects:

| Alias | Typical role |
|--------|----------------|
| `parPosition` | World anchor for the effect (`float3`). |
| `parDirection` | Direction vector (`float3`). |
| `parRadiusPhysical` / `parRadiusSuppress` | Radii exposed to gameplay / tools. |
| `parInitialShotDelay` | Scalar delay. |

`DefaultValue` on these rows is what mod tools often scale when generating size variants (e.g. 35 m → 250 m **gameplay** radius on the declaration). **In-file** offsets (see §5) are separate from these defaults.

---

## 3. `TSimultaneousAction`: one “burst bundle”

Each list entry under `Actions` is a **`TSimultaneousAction`** with:

- **`Mobile`** (optional): spatial frame for the whole bundle.
- **`Actions`**: list of child nodes that run **in parallel** with each other (subject to each branch’s internal sequencing).

### 3.1 `Mobile`

- **`TMobileWithLocalRepereMatrixFactory`** with a **`Position`** member is the usual case.
- **`Mobile = nil`**: no factory; positioning for that bundle comes entirely from **`parPositionRelative` / `parStartPosition`** on nested `TActionCall`s (§5.2).

### 3.2 `Mobile.Position` — observed forms

These all appear in vanilla files. Tools should accept them when inferring XY anchors:

1. **`float3[dx,dy,dz] + parPosition`**  
   Offset in **NDF XY space** (Z often 0) added to the call-site `parPosition`. This is the dominant pattern for **per-subburst** placement in cluster effects.

2. **`float3[dx,dy,dz]`** (no `+ parPosition`)  
   Absolute offset in file space; still a single anchor for the bundle.

3. **`parPosition`**  
   Bundle centered on the external anchor with no extra literal offset (treated as `(0,0)` offset in XY for layout math).

Other members (e.g. `EulerAngles`) may appear; they do not change the XY anchor rules above.

---

## 4. Parallelism vs sequencing inside a bundle

Under one `TSimultaneousAction.Actions`:

- **Siblings** (e.g. two `TSequentialAction` rows, or a `TSequentialAction` and a bare `TActionCall`) are **parallel**: they start together unless delayed internally.
- **`TSequentialAction`**: contains its own `Actions` list — typically **`TWaitInSec`** then **`TActionCall`** — meaning **wait, then fire** along that branch only.

So “related VFX at the same time” are often **sibling** `TSequentialAction` branches under one `TSimultaneousAction`. “Related VFX in sequence” are **one** branch with multiple waits + calls, or different rows at different `Duration`s.

---

## 5. Where “position” lives for a `TActionCall`

A **`TActionCall`** references a sub-effect:

```text
TActionCall
(
    Action = $/VFX_Bank/SomeEffect
    NamedParams = MAP[
        ( 'parSize', 1000 ),
        ( 'parPositionRelative', float3[dx,dy,0] + parPosition ),
        ...
    ]
)
```

### 5.1 Global anchor

The declaration’s **`parPosition`** is the **world anchor** for the whole effect call. Most layout expressions add **`+ parPosition`** so sub-bursts move with the impact point.

### 5.2 Per-call relative placement (`NamedParams`)

VFX tools care especially about:

| Key | Meaning |
|-----|--------|
| **`parPositionRelative`** | Offset for this call, almost always `float3[dx,dy,0] + parPosition` or the bare alias **`parPosition`** (same anchor as world center). |
| **`parStartPosition`** | Same idea for some effects (spawn/start point). |

Other keys (`parRandomPosition`, `parCloudsize`, etc.) may contain `float3[...]` but are **not** scatter anchors; parsers must not treat every `float3` as a footprint sample.

### 5.3 Stacking “related” VFX in authoring

- **Same `TSimultaneousAction` + shared `Mobile.Position`**: all nested calls share the **same** spatial frame; relative offsets inside `NamedParams` are optional for fine tuning.
- **Same `TSimultaneousAction` + `Mobile = nil`**: each `TActionCall` can carry its own **`parPositionRelative`**.  
  - If many calls use the **same** `float3[dx,dy,0] + parPosition`, they are intentionally **co-located** (e.g. multiple flashes at one sub-impact with different waits).  
  - If values **differ**, they are **different sub-sites** within one large parallel bundle (classic MLRS cluster composite block).
- **Different top-level `TSimultaneousAction` rows**: different **parallel bundles**, often different sub-bursts on the ground pattern. Pairing “this Mobile row” with “this nil-Mobile composite” is a **semantic** relationship the game establishes by file order and timing, not by a single explicit ID.

---

## 6. Cluster / multi-burst effects (footprint)

Effects like `fx_impact_sol_HE_M270_227mm_Cluster_1.ndf` combine:

1. **Many `TSimultaneousAction` rows with `Mobile`**  
   Each row is typically one **sub-impact** (e.g. crater + vegetation kill) at `float3[dx,dy,0] + parPosition`. The set of `(dx,dy)` defines the **scatter pattern** in NDF units.

2. **One (or more) large `TSimultaneousAction` with `Mobile = nil`**  
   Holds dozens of `TActionCall`s (flash, sparks, smoke, etc.), each with its own **`parPositionRelative`** aligned to the same sub-sites as in (1). This is how the game **layers** multiple VFX types on the same geometry without duplicating `Mobile` per call.

**Implication for tools:** scaling the **footprint** (more/fewer sub-bursts, larger disk) requires either:

- replicating whole `TSimultaneousAction` templates and rewriting anchors, or  
- rewriting all `Mobile.Position` and all matching `parPositionRelative` / `parStartPosition` in a **consistent** way.

NDF **XY** is not 1:1 with **gameplay meters**; mods usually calibrate with a reference file and a chosen gameplay radius (see §7).

---

## 7. NDF coordinates vs gameplay meters

Vanilla extraction uses an **engine-specific** XY scale. Mod tools map:

\[
\text{gameplay}_{xy} = \text{ndf}_{xy} \times \frac{\text{reference\_gameplay\_radius\_m}}{\text{anchor\_max\_ndf\_radius}}
\]

where `anchor_max_ndf_radius` is the **maximum** planar distance of relevant `Mobile` anchors in the reference cluster file (e.g. M270), and `reference_gameplay_radius_m` is the gameplay radius (m) you assign to that same farthest offset.

**Calibration ambiguity (important):** the pair \((\texttt{reference\_gameplay\_radius\_m},\, \texttt{anchor\_max\_ndf\_radius})\) is only fixed up to how you define “this NDF footprint equals this many meters.” Different choices can be **equivalent linear scales** if the ratio is adjusted consistently, but **halving** `reference_gameplay_radius_m` without changing `anchor_max_ndf_radius` (or the reverse) is **not** equivalent.

Observed in practice:

- **Earlier default calibration** used **`reference_gameplay_radius_m = 120`** with **`anchor_max_ndf_radius ≈ 4272.52`**, and that pairing **looked roughly correct in-game** for cluster VFX.
- A recomputed anchor for the same M270 reference file gives **`anchor_max_ndf_radius ≈ 4240.282686`**. It is plausible the “right” row is **`120` ↔ `4240.282686`** (same spirit as the old scale, updated anchor) rather than **`60` ↔ `4240.282686`** (which is a **steeper** NDF→gameplay slope and shrinks layout in gameplay space relative to 120/4272).
- **`tools/fxeditor/fxeditor.yaml`** carries the current calibration pair for **fxeditor**; treat as **config**, not as proven ground truth until validated side-by-side in-game.

**Working assumption for this document (until re-validated in-game):** use **`reference_gameplay_radius_m = 120`** with **`anchor_max_ndf_radius = 4240.282686`** when you need a single stated pair for mental math or new tooling docs. Revisit once in-game checks agree on one row.

This mapping is **linear** in XY; it does not model terrain or Z warping.

---

## 8. Other structural notes

- **`TWaitInSec`**: scalar `Duration`; drives timeline previews and batch wait redistribution.
- **`TActionCall` row duplication**: some effects scale “density” by **repeating** rows in a list; tools that edit counts must preserve list structure expected by the engine.
- **`dummy_impact_for_exporter_hack`**: seen in some files; passes `Pos`, `RadPhy`, etc. — useful for bounds / exporter hooks, not for artist layout.
- **Comments**: extracted files often start with `// Ne pas éditer...`; the parser may still see a comment row; robust walkers skip non-object rows.

---

## 9. Summary table: “how do I know if two calls are co-located?”

| Situation | Interpretation |
|-----------|----------------|
| Same `TSimultaneousAction`, same `Mobile.Position` expression | Same frame; optional per-call `parPositionRelative` for small offsets. |
| Same `TSimultaneousAction`, `Mobile = nil`, same `parPositionRelative` literal | Same sub-site (often staggered by `TWaitInSec` only). |
| Same `TSimultaneousAction`, `Mobile = nil`, different `parPositionRelative` | Different sub-sites inside one composite bundle. |
| Different top-level `TSimultaneousAction` | Different bundles; alignment is by **design** (matching coordinates, file order, timing), not a single explicit link. |

---

## 10. References in this repo

- Parsed / emitted with **`src.ndf`** (`ndf_parse`).
- **New FX editor (PySide6)** lives under **`tools/fxeditor/`**: **`core/`** (NDF I/O, extract, layout, classification, scaling pipeline) and **`ui/`** (main window, canvas, settings). Versioned calibration: **`tools/fxeditor/fxeditor.yaml`**.

This document should stay **synchronized** with **`tools/fxeditor`** when behavior is intentionally changed.
