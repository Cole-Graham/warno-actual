## FX Editor

Tkinter-based dev tool for browsing and editing FX NDF files using `ndf_parse`.

### Features

- Tree view of the parsed NDF structure
- Property editor for object members, maps, and lists
- Batch size-parameter scaling using curated size parameter patterns

### Run

```sh
python -m tools.fx_editor.main
```

### Notes

- This tool relies exclusively on `ndf_parse` (`from src import ndf`).
- When saving, the file is written using `ndf.printer.string`, which may reformat output.
