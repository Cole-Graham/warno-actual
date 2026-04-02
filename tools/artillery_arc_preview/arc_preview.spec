# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec: one-folder build (ArtilleryArcPreview.exe + dependencies).
# Run from repo root: .\tools\artillery_arc_preview\build_portable.ps1
# SPECPATH is injected by PyInstaller (directory containing this .spec file).

from pathlib import Path

from PyInstaller.utils.hooks import collect_all

spec_dir = Path(SPECPATH).resolve()
repo_root = spec_dir.parent.parent

datas_mpl, binaries_mpl, hiddenimports_mpl = collect_all(
    "matplotlib",
    include_py_files=True,
)

block_cipher = None

a = Analysis(
    [str(repo_root / "run_arc_preview.py")],
    pathex=[str(repo_root)],
    binaries=binaries_mpl,
    datas=datas_mpl,
    hiddenimports=hiddenimports_mpl
    + [
        "matplotlib.backends.backend_tkagg",
        "matplotlib.backends.backend_agg",
        "tools.artillery_arc_preview",
        "tools.artillery_arc_preview.main",
        "tools.artillery_arc_preview.trajectory",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="ArtilleryArcPreview",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    name="ArtilleryArcPreview",
)
