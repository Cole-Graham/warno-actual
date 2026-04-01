# Build portable Artillery Arc Preview via PyInstaller (bundles Python — no Python install needed on target PCs).
# Prerequisites: repo .venv with matplotlib (see requirements.txt). PyInstaller is installed on demand.
#
# Modes:
#   OneDir  (default) — dist\ArtilleryArcPreview\ArtilleryArcPreview.exe + _internal\ (ship the WHOLE folder)
#   OneFile — dist\ArtilleryArcPreview.exe only (single file to share; slower first launch)
#
# State: user_state.json next to the .exe

param(
    [ValidateSet("OneDir", "OneFile")]
    [string]$Mode = "OneDir"
)

$ErrorActionPreference = "Stop"
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
Set-Location $RepoRoot

$Python = Join-Path $RepoRoot ".venv\Scripts\python.exe"
if (-not (Test-Path $Python)) {
    Write-Error "Missing $Python — create the repo venv and install requirements first."
}

$SpecName = if ($Mode -eq "OneFile") { "arc_preview_onefile.spec" } else { "arc_preview.spec" }

& $Python -m pip install --quiet pyinstaller
& $Python -m PyInstaller --noconfirm --clean (Join-Path $PSScriptRoot $SpecName)

if ($Mode -eq "OneFile") {
    Write-Host "Done: dist\ArtilleryArcPreview.exe (single file — copy this one file only)"
} else {
    Write-Host "Done: dist\ArtilleryArcPreview\ — copy the ENTIRE folder (exe + _internal), not just the .exe"
}
