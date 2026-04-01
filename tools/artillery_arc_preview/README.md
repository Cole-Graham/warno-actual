# Artillery arc preview

Parabolic preview (Tk + matplotlib): fixed target range, pitch slider, derived horizontal speed and launch |v|.

## Run from source

From the repo root (with `.venv` and `matplotlib` installed per `requirements.txt`):

```text
python run_arc_preview.py
```

or:

```text
python -m tools.artillery_arc_preview
```

Settings are saved to `tools/artillery_arc_preview/user_state.json` (gitignored).

## Portable executable (Windows)

The build **embeds Python** (e.g. `python312.dll` inside the bundle). **Recipients do not need Python installed.**  
Problems on another machine almost always mean **an incomplete copy** (see below).

### One-folder build (default, faster startup)

```powershell
.\tools\artillery_arc_preview\build_portable.ps1
```

Output: `dist\ArtilleryArcPreview\ArtilleryArcPreview.exe` plus an `_internal\` folder with DLLs and libraries.

**You must distribute the entire `ArtilleryArcPreview` directory** (the `.exe` **and** `_internal`, and any other files beside them). If someone copies **only** `ArtilleryArcPreview.exe`, Windows will report **missing `python312.dll`** because that file lives under `_internal`.

### One-file build (single `.exe` to share)

```powershell
.\tools\artillery_arc_preview\build_portable.ps1 -Mode OneFile
```

Output: `dist\ArtilleryArcPreview.exe` only. Easier to hand off one file; first launch unpacks to a temp folder (slower cold start).

Requires the repo `.venv` (install deps first). The script installs PyInstaller into that venv for the build.

Settings are written to `user_state.json` **next to the executable** (same folder as the `.exe`, not inside `_internal`).

## Files

| File | Role |
|------|------|
| [`main.py`](main.py) | Application UI |
| [`trajectory.py`](trajectory.py) | Parabolic math |
| [`arc_preview.spec`](arc_preview.spec) | PyInstaller spec (onedir) |
| [`arc_preview_onefile.spec`](arc_preview_onefile.spec) | PyInstaller spec (single exe) |
| [`build_portable.ps1`](build_portable.ps1) | Build script (`-Mode OneDir` or `OneFile`) |

Repo root [`run_arc_preview.py`](../../run_arc_preview.py) is the PyInstaller entry script.
