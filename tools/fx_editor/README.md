## FX Editor

Tkinter-based dev tool for browsing and editing FX NDF files using `ndf_parse`.

### Features

- Tree view of the parsed NDF structure
- Property editor for object members, maps, and lists
- **Batch size-parameter scaling** using curated size/count patterns (NamedParams + declaration Params; default rules apply to all effects)
- **Scatter layout** (under **Batch Size** → **Scatter layout** sub-tab): gameplay-calibrated XY footprint with **integer** gameplay coordinates (vanilla-style), **hex grid + jitter** (both constrained to **R (m)**), **VFX-colored** preview with per-VFX checkboxes, and codegen by cloning `TSimultaneousAction` templates. Run the app **maximized** for the best layout.

### Run

Use the project virtual environment so `ndf_parse` is available (see root `requirements.txt`).

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
python -m tools.fx_editor.main
```

Or from the repo root: `python run_fx_editor.py` (after activating the venv).

**Unix:**

```sh
source .venv/bin/activate
python -m tools.fx_editor.main
```

### Environment variables (optional)

- **`FX_EDITOR_LOG_LEVEL`**: `DEBUG`, `INFO`, or `WARNING` (default `INFO`) — stderr verbosity for the FX editor logger.
- **`FX_EDITOR_PROFILE`**: set to `1`, `true`, or `yes` — logs `time.perf_counter` spans for the cluster emit/scale pipeline (`scatter_pipeline` logger at **DEBUG**).
- **`FX_EDITOR_PREVIEW_WORKERS`**: integer `1`–`16` (default `1`) — for **cluster** batch preview only, run up to this many `preview_cluster_variation` jobs in parallel via `ProcessPoolExecutor` when there is more than one file × target combination. The UI thread is unchanged; only compute runs in worker processes.

### Workflow: layout vs param scale

1. **Scatter layout** (**Batch Size** → **Scatter layout**, or **Open Scatter layout…** on the General batch screen): Import a template NDF, edit bursts as **integer** x/y **gameplay meters** (see calibration below). **Hex grid** and **jitter** keep bursts inside the **R (m)** disk; manual drag and free text stay integer-rounded. The canvas **dashed reference circle** follows **R (m)** (visual guide). **Gameplay ↔ NDF** scaling uses `scatter_calibration.yaml` on import/emit; emitted NDF uses **integer** `float3` components like vanilla. Pick emit mode (Mobile `Position` vs `parPositionRelative`), set **template row index**, then **Generate NDF…**.
2. **Optional**: Enable **After write, run batch param scale** on the Scatter sub-tab to chain the Batch **General** tab percentage.
3. **Param-only scaling** (Preview / Apply / variations) for fine-tuning sizes on simpler effects, or as a second pass after scatter.
4. **Cluster size variations** (**Batch Size** → **General** → **Batch size variations**): check **Cluster: scale number of impacts** to map source/target gameplay size to a **new burst count** (linear: N scales with target/source size), lay out impacts on a **hex grid** (same geometry as the Scatter **Hex grid** preset: **N** and **R (m)**), redistribute **anchor** `TWaitInSec` durations between an **inferred minimum** (from the template file’s first waits per `TSimultaneousAction`) and your **Max anchor wait (s)** (the **Min (from file)** hint updates when cluster mode is on and a batch file is selected). Then the pipeline runs **scatter emit** + **param scale** like a normal variation. The **Scatter layout** sub-tab is updated from the last preview or written file so you see the same footprint.
5. **Effect summary** and **Timing preview** on the **Scatter layout** sub-tab: per–short-name `TActionCall` counts, burst total, emit mode, and a scrubber/playhead over accumulated `TWaitInSec` + `TActionCall` times (parallel bursts, **authoring preview** only).

Order of operations: **layout first** (structure + positions), **param scaling second** when needed.

### Calibration (`tools/fx_editor/scatter_calibration.yaml`)

NDF XY units are not 1:1 with gameplay meters. The default anchor uses the vanilla MLRS cluster footprint at **120 m** gameplay radius vs the **maximum** Euclidean offset of Mobile `Position` points in that reference file. Adjust `anchor_max_ndf_radius` if you recompute from a different baseline. This file drives **import/emit** mapping only; the scatter canvas **reference ring** uses the **R (m)** field in the UI.

### Notes

- This tool relies exclusively on `ndf_parse` (`from src import ndf`).
- When saving, the file is written using `ndf.printer.string`, which may reformat output.
- Scatter emit **replaces** the entire `Actions` list with one clone per burst. Use a dedicated copy of a template file if you need to preserve the original.
