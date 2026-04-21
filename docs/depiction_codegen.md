# Depiction-Edit Codegen & Promotion Workflow

This page documents the end-to-end workflow for the depiction-edit
generator added in `src/data/depiction_codegen.py`, the audit that drives
it (`src/data/depiction_audit.py`), and the manual review / promotion
loop that turns auto-generated drafts into committed depiction edits.

## When to (re)generate

Regenerate drafts whenever any of the following changes:

- A unit's `WeaponDescriptor.equipmentchanges["replace"]` block.
- The `depiction_data.json` cache (i.e. after a fresh
  `constants_precomputation` run that picks up new meshes / fire effects /
  animation tags from the source NDF).
- A new unit was added to `src/constants/new_units/<FACTION>_new_units.py`
  with `WeaponDescriptor.equipmentchanges` set.

Run from the repo root:

```bash
.\.venv\Scripts\python.exe -m src.data.depiction_codegen --all
```

Other invocations:

- `--unit Para_POL` — generate one unit only.
- `--faction POL` — generate every flagged unit for one faction.
- (no flag) — equivalent to `--all`.

The audit is run implicitly to populate the worklist; you can also run it
standalone via `python -m src.data.depiction_audit` if you only want the
JSON report at `logs/depiction_audit.json`.

## What gets written

For every unit on the audit's worklist that has at least one *non-no-op*
`replace` spec, the generator writes two sibling files:

- `..._generated/<UnitName>.py` — the draft Python module (importable as
  the depiction-edit dictionary).
- `..._generated/<UnitName>.codegen.json` — the per-unit diagnostic
  describing what was resolved, what wasn't, and which
  `equipmentchanges` keys were out-of-scope for codegen.

Drafts land in:

- Existing units → `src/constants/unit_edits/depiction_edits/<FACTION>_depiction_edits/_generated/`
- New units → `src/constants/new_units/new_depictions/<FACTION>_new_depictions/_generated/`

`_generated/` is intentionally **not** picked up by either faction's
`__init__.py`, so drafts cannot affect the build until they are reviewed
and promoted.

## Reviewing a draft

1. Read the `.codegen.json` first. The `notes` array on each spec
   explains anything that could not be resolved (missing
   `all_weapon_meshes` entry, missing `animation_weapon_map` entry, etc.).
2. Open the matching `.py` file. Search for `# TODO_CODEGEN:` — every
   unresolved row, out-of-scope key, or non-infantry classification
   produces a TODO comment that has to be answered before promotion.
3. Cross-check the indices in `("AllWeaponAlternatives_<unit>", None)`
   against the donor unit's actual `WeaponAlternatives_*` rows in the
   live NDF. The codegen takes them straight from `depiction_data`, but
   the donor row indices can drift if the source NDF was patched between
   generations.
4. For ground-vehicle / aerial stubs (classification != `infantry`), the
   draft only contains a header and the TODO list. Hand-author the
   `DepictionVehicles.ndf` / `DepictionAerialUnits.ndf` operators using
   neighbouring promoted edits as a template.

## Promoting a draft

1. Move the `.py` file out of `_generated/` into the parent
   `<FACTION>_depiction_edits/` (or `<FACTION>_new_depictions/`) folder.
2. Delete the `.codegen.json` sidecar — it is an artefact of generation
   and should not be committed.
3. Register the import + `__all__` (or `<FACTION>_NEW_DEPICTIONS` dict)
   entry in the faction's `__init__.py`. Existing pattern:

   ```python
   # src/constants/unit_edits/depiction_edits/POL_depiction_edits/__init__.py
   from .Para_POL import para_pol

   __all__ = [
       ...,
       "para_pol",
   ]
   ```

   ```python
   # src/constants/new_units/new_depictions/POL_new_depictions/__init__.py
   from .MANPAD_Igla_POL import manpad_igla_pol

   POL_NEW_DEPICTIONS = {
       ...,
       "manpad_igla_pol": manpad_igla_pol,
   }
   ```
4. Re-run the audit to confirm the unit is no longer flagged:

   ```bash
   .\.venv\Scripts\python.exe -m src.data.depiction_audit
   ```

   The unit should be absent from `logs/depiction_audit.json`.
5. Run a normal patcher pass (`python -m src.patcher`) and verify the
   unit's mesh / fire effect / animation in-game.

## Suppressing false positives without writing edits

If a `replace` block is intentionally a pure ammo rename (no depiction
change), set `swap_fire_effect: False` in the dict entry:

```python
"replace": {
    "FM_kbk_AKM": {
        "new_weapon": "FM_Tantal",
        "swap_fire_effect": False,
    },
},
```

The audit's `_is_replace_spec_noop` will skip the unit unless mesh data
positively contradicts that claim, so no draft will be generated.

## Re-running cleanly

To wipe every existing draft (drafts are deterministic — regenerating
overwrites them anyway, but a clean slate makes diffs easier to read):

```powershell
Get-ChildItem -Path src\constants\unit_edits\depiction_edits, `
                    src\constants\new_units\new_depictions `
              -Recurse -Directory -Filter "_generated" |
    ForEach-Object { Remove-Item -Path $_.FullName -Recurse -Force }
.\.venv\Scripts\python.exe -m src.data.depiction_codegen --all
```
