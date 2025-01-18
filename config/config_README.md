# Configuration Guide

## File Categories

The mod system handles four categories of files:

1. UI-only files
2. Gameplay-only files  
3. Variant files (modified differently between mods)
4. Shared files (modified identically in both mods)

## File Processing Flow

### Basic Flow
```mermaid
graph TD
    A[Base Game File] --> B[get_file_editor]
    B --> C{files: section?}
    C -->|variants:| D1[Variant Processing]
    C -->|shared:| D2[Shared Processing] 
    C -->|ui_only:| D3[UI Processing]
    C -->|gameplay_only:| D4[Gameplay Processing]
    D1 & D2 & D3 & D4 --> E[Modified File]
```

### Example: BuildingDescriptors.ndf (Variant File)
```mermaid
graph TD
    A[BuildingDescriptors.ndf] --> B[get_file_editor]
    B --> C{Check Config}
    C -->|variants:| D[Get variant functions]
    D --> E{Build_config:
              target: }
    E -->|"''ui''"| F1[shared/ui/buildings.py: edit_fob_minimap]
    E -->|"''gameplay''"| F2[Apply Both:]
    F2 --> G2[gameplay/buildings/fob.py: edit_fob_attributes]
    F1 --> H[Modified File]
    G2 --> F1
```

### Example: UniteDescriptor.ndf (Gameplay-Only)
```mermaid
graph TD
    A[UniteDescriptor.ndf] --> B[get_file_editor]
    B --> C{files: section?}
    C -->|gameplay_only:| D[Get gameplay editors]
    D --> E[gameplay/editors.py]
    E --> F[Apply Functions in Order:]
    F --> G1[1. edit_units]
    F --> G2[2. edit_antirad_optics]
    F --> G3[3. edit_forward_deploy]
    F --> G4[4. create_new_units]
    G1 & G2 & G3 & G4 --> H[Modified File]

    I[build_config:] --> J{target:}
    J -->|gameplay| D
```

### Example: MinimapIcons.ndf (Shared File)
```mermaid
graph TD
    A[MinimapIcons.ndf] --> B[get_file_editor]
    B --> C{files: section?}
    C -->|shared:| D[Get shared functions]
    D --> E[shared/shared_editors.py]
    E --> F[edit_minimap_icons]
    F --> G[Modified File]
    
    H[build_config:] --> I{target:}
    I -->|ui| J1[Apply UI shared functions]
    I -->|gameplay| J2[Apply gameplay shared functions]
    J1 & J2 --> F
```

### Example: UISpecificUnitInfoPanelView.ndf (UI File Modified by Gameplay)
```mermaid
graph TD
    A[UISpecificUnitInfoPanelView.ndf] --> B[get_file_editor]
    B --> C{files: section?}
    C -->|variants:| D[Get variant functions]
    D --> E{build_config:
            target:}
    E -->|ui| F1[No modifications]
    E -->|gameplay| F2[gameplay/ui/unit_info_panel.py: edit_unit_info_panel]
    F1 & F2 --> G[Modified File]
```

## Configuration Examples

### Variant File Example
```yaml
variants:
  "GameData/.../BuildingDescriptors.ndf": {
    "ui": [
      "edit_fob_minimap"  # UI mod only gets minimap function
    ],
    "gameplay": [
      "edit_fob_minimap",    # Gameplay mod gets both functions
      "edit_fob_attributes"  # Additional gameplay-specific changes
    ]
  }
```

### Shared File Example
```yaml
shared:
  "GameData/.../MinimapIcons.ndf": {
    "gameplay": [
      "edit_minimap_icons"
    ],
    "ui": [
      "edit_minimap_icons"  # Same function for both mods
    ]
  }
```

## Function Organization

Functions are organized based on their usage:

```
src/
├── shared/               # Functions used identically by both mods
│   └── ui/
│       └── buildings/
│           └── fob.py   # edit_fob_minimap
│
├── gameplay/            # Functions only used by gameplay mod
│   ├── editors.py      # Main gameplay editors
│   └── ui/             # UI functions specific to gameplay
│       └── unit_info_panel.py
│
└── ui/                 # Functions only used by UI mod
    └── ui/
        └── styles.py
```

## Key Points

1. File Categories:
   - UI-only: Files that only exist in UI mod
   - Gameplay-only: Files that only exist in gameplay mod
   - Variants: Files modified by both mods, but with different functions
   - Shared: Files modified identically in both mods

2. Function Location:
   - Functions live in modules based on their usage
   - Config specifies which functions to apply to each file
   - Order of functions matters within each file

3. Processing Order:
   1. Check if file is variant
   2. Check if file is shared
   3. Check if file has mod-specific editors

4. Editor Types:
   - Variant editors: Different between mods
   - Shared editors: Same in both mods
   - Mod-specific editors: Only exist in one mod

## Common Patterns

1. UI Files Modified by Gameplay:
   ```yaml
   variants:
     "GameData/.../UISpecificUnitInfoPanelView.ndf": {
       "gameplay": ["edit_unit_info_panel"]
     }
   ```

2. Multiple Functions Per File:
   ```yaml
   gameplay_only:
     "GameData/.../UniteDescriptor.ndf": [
       "edit_units",
       "create_new_units"
     ]
   ```

3. Shared UI Components:
   ```yaml
   shared:
     "GameData/.../MinimapIcons.ndf": {
       "gameplay": ["edit_minimap_icons"],
       "ui": ["edit_minimap_icons"]
     }
   ```
