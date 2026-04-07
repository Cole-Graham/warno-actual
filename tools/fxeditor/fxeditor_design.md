# FX Editor — Design and Taxonomy

This document describes the architecture, spatial taxonomy, and scaling pipeline of the **fxeditor** (`tools/fxeditor`). It is the canonical reference for how the tool analyses, classifies, and scales WARNO VFX NDF files.

For the raw NDF file structure, see [warno_vfx_file_structure.md](./warno_vfx_file_structure.md).

---

## 1. Purpose

The fxeditor generates **scaled variants** of cluster/impact VFX NDF files for WARNO. Given one or more source files (e.g. the M270 227mm cluster at a 60 m gameplay radius), it produces output files at arbitrary target radii (e.g. 35 m, 75 m, 150 m, 250 m) while **preserving the artistic feel** of the original effect.

"Preserving artistic feel" means:

- The spatial distribution of composite explosions, ancillary effects, and decorative layers is kept in correct proportion.
- The internal "recipe" of each explosion (which sub-effects fire together, their relative timing, their stacking) is cloned intact — not inflated or deflated.
- Size and count parameters (`parSize`, `parCount`, etc.) are **not** modified by default. Spatial scaling only changes the **number and position** of VFX calls.

---

## 2. Module Map

```
tools/fxeditor/
├── __main__.py              Entry point (python -m tools.fxeditor)
├── vfx_editor.yaml          Calibration config
├── fxeditor_design.md       This document
├── warno_vfx_file_structure.md  NDF structure reference
│
├── core/
│   ├── config.py            Load calibration (NDF ↔ gameplay mapping)
│   ├── ndf_io.py            NDF parse/serialize, tree walking, position helpers
│   ├── spatial_classifier.py  ★ Classify VFX groups by spatial role
│   ├── scaler.py            ★ Main scaling pipeline (classify → layout → emit)
│   ├── extract.py           Burst info extraction, scatter point extraction
│   ├── grouping.py          Composite site model, effect group analysis
│   ├── layout.py            Vogel spiral disk layout
│   ├── falloff.py           Radius falloff curve (position bias)
│   ├── budget.py            TActionCall budget system
│   ├── size_params.py       Size/count parameter scaling (opt-in)
│   └── naming.py            Output filename rendering
│
└── ui/
    ├── main_window.py       PySide6 main window, tabbed scatter preview
    ├── scatter_canvas.py    2D scatter preview widget (QPainter)
    ├── effect_group_panel.py  VFX visibility checkboxes + classification
    ├── falloff_dialog.py    Radius falloff curve editor
    ├── settings_dialog.py   Calibration, naming, param scaling, budget
    ├── state.py             JSON state persistence
    └── worker.py            Background batch generation thread
```

---

## 3. Spatial Taxonomy

The core insight of the fxeditor is that every VFX call in a source file plays a specific **spatial role** relative to the composite explosion sites. Understanding these roles is essential for correct scaling.

### 3.1 Composite Sites

A source VFX file defines N **composite sites** — the positions of the main explosions. In the M270 cluster source, N=10. These positions are identified from the `parPositionRelative` / `parStartPosition` anchors inside the primary nil-Mobile `TSimultaneousAction` block.

### 3.2 Spatial Roles

Every VFX group (identified by its `TActionCall` short name, e.g. `BANK_Bomb_Flash`) is assigned one of seven spatial roles by the classifier (`core/spatial_classifier.py`):

| Role | Description | Scaling Policy |
|------|-------------|----------------|
| **`COMPOSITE_LEAD`** | Core explosion effects inside nil-Mobile blocks via `parPositionRelative` / `parStartPosition`. Precisely stacked at ALL composite sites, 1:1 with sites. | Expand nil-Mobile block: add new branches for each new site. |
| **`SITE_STACKED`** | Mobile-positioned blocks precisely at composite site coordinates. 1 per site. | Clone template block, set Mobile to new site position. |
| **`SITE_OFFSET`** | Mobile-positioned blocks near composite sites but on a slightly different coordinate lattice. 1 per site. | Clone template, set Mobile to new site + scaled offset. |
| **`SITE_REGISTERED_PRECISE`** | Appears precisely at composite sites AND at random positions. Has a site:random ratio. | Site instances: 1 per new site. Random instances: scale proportionally. |
| **`SITE_REGISTERED_OFFSET`** | Appears near (offset from) composite sites AND at random positions. Has a site:random ratio. | Site instances: 1 per new site at offset. Random instances: scale proportionally. |
| **`FIELD_RANDOM`** | All instances at random positions, no systematic site correlation. | Scale count proportionally with target/source ratio. |
| **`CENTER_ONLY`** | Single instance at or near (0,0). Not replicated. | Keep unchanged at origin. |

### 3.3 Classification Algorithm

1. **Identify composite sites** from the first nil-Mobile block's scatter-named position anchors (`parPositionRelative`, `parStartPosition`).
2. **For each VFX short name**, collect occurrence positions:
   - For Mobile blocks: one occurrence per VFX name per block, at the Mobile position. Only the **primary** (first) TActionCall determines the dot label; secondary calls inherit the block's role.
   - For nil-Mobile blocks: one occurrence per scatter-named position anchor per TActionCall.
3. **Classify each occurrence** by distance to nearest composite site:
   - `near_site_precise`: distance ≤ ε_precise (default 1.0 m gameplay)
   - `near_site_offset`: ε_precise < distance ≤ ε_offset (default 8.0 m gameplay)
   - `far_field`: distance > ε_offset
4. **Assign group role** from the breakdown:
   - All near-precise, from nil-Mobile, count ≥ N_sites → `COMPOSITE_LEAD`
   - All near-precise, from Mobile → `SITE_STACKED`
   - All near-offset → `SITE_OFFSET`
   - Mixed near + far, ≥50% of sites covered → `SITE_REGISTERED_PRECISE` or `_OFFSET`
   - Mixed near + far, <50% of sites covered → `FIELD_RANDOM` (coincidental proximity)
   - All far-field → `FIELD_RANDOM`
   - Single unique position at origin → `CENTER_ONLY`

### 3.4 Example: M270 227mm Cluster Source

| VFX Name | Role | Site | Random | Notes |
|----------|------|------|--------|-------|
| `BANK_Bomb_Flash` | COMPOSITE_LEAD | 10 | — | nil-Mobile, parPositionRelative |
| `BANK_Bomb_NewSparks_Omni_Simple` | COMPOSITE_LEAD | 10 | — | nil-Mobile, parPositionRelative |
| `BANK_Bomb_NewSparks_Simple` | COMPOSITE_LEAD | 10 | — | nil-Mobile, parPositionRelative |
| `BANK_FireBalls_HQTex_Simple` | SITE_REGISTERED_PRECISE | 9 | 1 | nil-Mobile, parStartPosition |
| `BANK_Dynamic_Flash_Repeat_Simple` | SITE_STACKED | 10 | — | Mobile, secondary call |
| `BANK_Rubble2_Oriented_Simple` | SITE_STACKED | 10 | — | Mobile, primary call |
| `Conic_Ground_Projection_Simple` | SITE_STACKED | 10 | — | Mobile, primary call |
| `Big_ground_Impact_Simple` | SITE_OFFSET | 10 | — | Mobile, different lattice |
| `DarkSmoke_Simple` | SITE_REGISTERED_PRECISE | 30 | 1 | ~3 per site + 1 random |
| `BANK_WasteGroundDustStickOnGround_Simple` | SITE_REGISTERED_PRECISE | 11 | 11 | ~1 per site + 11 random |
| `BANK_Ground_Sticker_Big_Simple` | SITE_REGISTERED_OFFSET | 11 | 21 | ~1 per site (offset) + 21 random |
| `DestroyVegetAndLB` | FIELD_RANDOM | — | 21 | Purely random distribution |
| `ShakeCamera` | CENTER_ONLY | — | — | Single instance at origin |

### 3.5 Position Parameter Keys

The classifier and scatter extractor recognize these `NamedParams` keys as spatial anchors (defined in `ndf_io._SCATTER_NAMED_POSITION_KEYS`):

- **`parPositionRelative`** — primary offset, usually `float3[dx,dy,0] + parPosition`
- **`parStartPosition`** — spawn point for some effects (e.g. fireballs), usually `float3[dx,dy,dz] + parPosition` where Z is the spawn height

Both use XY for horizontal position. When repositioning, the scaler preserves the original Z component (important for effects like `BANK_FireBalls_HQTex_Simple` which spawn at height and fall via `parDeltaPosition`).

Other keys like `parDeltaPosition`, `parRandomPosition`, `parCloudsize` are **not** spatial anchors and are never modified by the scaler.

---

## 4. Scaling Pipeline

The scaler (`core/scaler.py`) implements a multi-stage pipeline:

### 4.1 Pipeline Stages

```
Source NDF
    │
    ▼
┌─────────────────┐
│ 1. Parse         │  ndf_io.parse_ndf()
└────────┬────────┘
         ▼
┌─────────────────┐
│ 2. Classify      │  spatial_classifier.classify_source()
│                  │  → SourceClassification with per-VFX roles,
│                  │    per-block assignments, composite site positions
└────────┬────────┘
         ▼
┌─────────────────┐
│ 3. Budget        │  Compute N_target, N_effective, random counts
│                  │  given TActionCall cap
└────────┬────────┘
         ▼
┌─────────────────┐
│ 4. Layout        │  Vogel spiral for N_effective composite sites
│                  │  + falloff curve bias
└────────┬────────┘
         ▼
┌─────────────────┐
│ 5. Emit          │  Category-aware block emission:
│   a. Site blocks │  Clone per-site templates for each new site
│   b. Nil-Mobile  │  Expand with new branches per site
│   c. Random      │  Scale count, distribute on Vogel spiral
│   d. Center      │  Keep at origin
└────────┬────────┘
         ▼
┌─────────────────┐
│ 6. Param scale   │  (opt-in) Scale size/count params if enabled
└────────┬────────┘
         ▼
┌─────────────────┐
│ 7. Clamp & Name  │  Clamp to disk, set export name
└────────┬────────┘
         ▼
    Output NDF
```

### 4.2 Site Count Scaling

The number of composite sites scales linearly with radius:

```
N_target = round(N_source × target_radius / source_radius)
```

For the M270 source (N_source=10, source_radius=60m):
- 35m → 6 sites
- 75m → 12 sites
- 150m → 25 sites
- 250m → 42 sites (may be reduced by budget)

### 4.3 Nil-Mobile Block Expansion

Nil-Mobile blocks contain `COMPOSITE_LEAD` VFX for ALL source sites in a single `TSimultaneousAction`. Each VFX type has N_source branches (one per site), each structured as:

```
TSequentialAction → TWaitInSec(duration) → TActionCall(vfx, parPositionRelative/parStartPosition)
```

When expanding to N_target sites:
1. Deep copy the nil-Mobile block
2. Clear positional branches
3. For each new site × each VFX type: clone a template branch, update the position XY (preserving Z), assign a stagger wait from the source timing pool
4. Re-add non-positional branches (dummies, etc.)

### 4.4 Site-Offset Handling

`SITE_OFFSET` blocks (e.g. `Big_ground_Impact_Simple`) sit on a different coordinate lattice than the composite sites. The offset vector between the block's position and its assigned composite site is computed from the source, then applied scaled to each new site:

```
new_position = new_site + (source_offset × radius_scale_factor)
```

### 4.5 Site-Registered Ratio Preservation

For VFX with both site and random instances (e.g. `BANK_Ground_Sticker_Big_Simple` with 11 site + 21 random):
- **Site instances**: emitted automatically as part of site-block cloning (they're inside blocks assigned to sites)
- **Random instances**: scaled proportionally: `random_count_new = round(random_count_source × N_target / N_source)`

---

## 5. Budget System

The TActionCall budget prevents engine culling when multiple effects fire simultaneously (e.g. a 12-missile MLRS salvo where each missile triggers a 250m-radius VFX).

### 5.1 Budget Cap

Configurable per-file cap on total `TActionCall` rows (default 600, range 200–2000).

### 5.2 Priority-Based Reduction

When the estimated call count exceeds the cap:

1. **Phase 1**: Reduce random counts proportionally (affects `FIELD_RANDOM` and `SITE_REGISTERED` random components)
2. **Phase 2**: If still over, reduce the number of composite sites (N_effective < N_target), spreading the same count across a wider area

Never reduced below:
- 3 composite sites minimum
- 1 random instance per VFX group minimum
- `COMPOSITE_LEAD`, `SITE_STACKED`, `SITE_OFFSET` are never trimmed below 1 per site
- `CENTER_ONLY` is never touched

---

## 6. Radius Falloff Curve

An 11-sample curve (0–100% weight at normalized radius 0.0–1.0, center to edge) biases the radial distribution of composite site positions **without** reducing quantity. The falloff uses inverse-CDF sampling with marginal density proportional to `w(r) × r` on the disk.

### 6.1 Presets

| Preset | Description |
|--------|-------------|
| Flat | 100% everywhere (no bias) |
| Linear ramp | e.g. 100% center → 15% edge |
| Quadratic ramp | Faster falloff toward edge |
| Square root ramp | Slower initial falloff |
| Smoothstep ramp | S-curve with gentle transitions |
| Fourth root ramp | Very front-loaded |

### 6.2 User Curve

The falloff dialog allows dragging 11 control points and saving/loading named presets. The curve is stored in persistent state.

---

## 7. Scatter Preview

The scatter preview shows the spatial distribution of all VFX calls as colored dots on a 2D top-down view.

### 7.1 Tabbed Architecture

```
┌──────────────────────────────────────────┐
│ [Source_1.ndf] [Source_2.ndf] │ [S1@75m] [S1@150m] [S1@250m] │
│                               │                                │
│    Source tabs (auto on load)  │  Preview tabs (on Refresh)     │
└──────────────────────────────────────────┘
```

- **Source tabs**: populated automatically when files are loaded. Show the raw scatter dots from the unmodified source NDF.
- **Preview tabs**: populated on "Refresh Preview" click. Run the full classified emit pipeline (`scale_single_file_in_memory`) on a deep copy for each (source file × target radius) pair, then extract dots from the emitted tree.

### 7.2 Dot Extraction

`extract_scatter_points_with_vfx()` walks every `TSimultaneousAction` block:

- **Mobile blocks**: one dot at the Mobile position, labeled with the first (primary) `TActionCall` short name
- **Nil-Mobile blocks**: one dot per scatter-named position (`parPositionRelative` or `parStartPosition`), each labeled with its own `TActionCall` short name

This ensures that effects like `BANK_Bomb_Flash` (which only exist as `parPositionRelative` entries inside nil-Mobile blocks) get their own dots on the scatter preview.

### 7.3 Overlay Information

Each scatter canvas shows:
- **Header**: `Dots: visible/total | TSimultaneous: N | Radius: Rm`
- **Footer**: `TActionCalls: N / cap` (color-coded: green = OK, yellow = near cap, red = over cap)

### 7.4 Refresh Behavior

- Config changes (radii, source radius, falloff, cap) mark the preview as **dirty** (button text changes to "Refresh Preview *")
- Preview is NOT regenerated automatically on config changes (too expensive)
- Source tabs ARE auto-populated on file load (lightweight extraction only)
- "Refresh Preview" button runs the full pipeline and creates/replaces preview tabs

---

## 8. Parameter Scaling (Opt-In)

Size and count parameter scaling is **disabled by default**. When the scaler runs, it only changes the number and positions of VFX calls — all `parSize`, `parRadius`, `parCount`, etc. values remain exactly as they were in the source templates.

### 8.1 Configuration

Two independent toggles in Settings → Param Scaling:

| Toggle | What it scales | Default |
|--------|---------------|---------|
| **Scale sizes** | `parSize`, `parRadius`, `parHeight`, `parDispersion`, etc. (~25 recognized patterns) | OFF |
| **Scale counts** | `parCount`, `parCountDebrits`, `parCountDebritsWithFire` | OFF |

### 8.2 Scale-Down Floors

When param scaling is enabled and the target radius is smaller than the source:
- **Min size ratio** (default 0.3): size params are never reduced below 30% of their source value
- **Min count value** (default 1): count params are never reduced below 1

---

## 9. Coordinate Calibration

NDF coordinates are not 1:1 with gameplay meters. The mapping is linear:

```
gameplay_xy = ndf_xy × (reference_gameplay_radius_m / anchor_max_ndf_radius)
```

### 9.1 Configuration

Stored in `vfx_editor.yaml`:

```yaml
reference_gameplay_radius_m: 60.0
anchor_max_ndf_radius: 4240.282686
```

Editable in Settings → Calibration. The "Reload from YAML" button reloads from disk.

### 9.2 Usage

- `CalibrationConfig.ndf_to_gameplay(dx, dy)` — convert NDF to gameplay meters
- `CalibrationConfig.gameplay_to_ndf(gx, gy)` — convert gameplay meters to NDF

---

## 10. Output Naming

Default template: `{rootname}_{radiusinmeters}m_{n}.ndf`

| Placeholder | Value |
|-------------|-------|
| `{rootname}` | User-specified root name (e.g. `fx_impact_mlrs_cluster_ap`) |
| `{radiusinmeters}` | Target radius in meters (e.g. `250`) |
| `{n}` | Trailing index from source filename (e.g. `1` from `..._Cluster_1.ndf`) |
| `{suffix}` | Trailing `_N` from source filename including underscore |

---

## 11. State Persistence

All UI fields and settings are saved to `%LOCALAPPDATA%/warno_vfx_editor/state.json`:

- Window geometry and splitter positions
- Source file paths, source radius, root name, target radii text
- Output directory
- TActionCall cap
- Falloff curve and named presets
- VFX visibility toggles
- Calibration values
- Naming template
- Scale sizes / scale counts toggles
- Scale-down floor values

State is auto-saved on window close and on File → Save State (Ctrl+S).

---

## 12. Terminology Reference

| Term | Definition |
|------|------------|
| **Composite site** | One of the N main explosion positions in the source NDF, identified from the primary nil-Mobile block's position anchors. |
| **Spatial role** | One of the 7 categories (`COMPOSITE_LEAD` through `CENTER_ONLY`) assigned to each VFX group by the classifier. |
| **Nil-Mobile block** | A `TSimultaneousAction` with `Mobile = nil`. Positions come from per-call `parPositionRelative` / `parStartPosition`, not from a shared Mobile frame. Contains `COMPOSITE_LEAD` effects for ALL sites. |
| **Mobile block** | A `TSimultaneousAction` with a `TMobileWithLocalRepereMatrixFactory` Mobile. The `Position` member sets the XY anchor for all calls in the block. |
| **Primary VFX** | The first `TActionCall` (in preorder traversal) inside a `TSimultaneousAction`. Determines the block's label in scatter preview and drives spatial classification for the block. |
| **Secondary VFX** | Non-first `TActionCall`s in a Mobile block. They share the block's position and are carried along when the block is cloned. Not independently classified. |
| **Scatter-named position** | A `NamedParams` key recognized as a spatial anchor: `parPositionRelative` or `parStartPosition`. |
| **Scale factor (sf)** | `target_radius / source_radius`. Drives site count scaling and proportional random scaling. |
| **N_source** | Number of composite sites in the source file. |
| **N_target** | Ideal number of composite sites at the target radius: `round(N_source × sf)`. |
| **N_effective** | Actual site count after budget cap: `min(N_target, budget_limit)`. |
| **Budget cap** | Maximum total `TActionCall` rows in the output file. |
| **Falloff curve** | 11-sample radial weight curve that biases composite site placement toward the center without reducing count. |
| **Vogel spiral** | Deterministic golden-angle disk layout algorithm for even spatial distribution. |
| **Stagger** | Per-site `TWaitInSec` leading wait, sampled from the source timing pool. Preserves the visual impression of impacts arriving at different times. |
