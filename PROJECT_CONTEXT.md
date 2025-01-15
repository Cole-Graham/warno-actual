# WARNO ACTUAL Mod Patcher - Project Context

## Project Structure

### Root Level
├── run_patcher.py        # Entry point script
├── pyproject.toml        # Project metadata and dependencies
├── README.md            # Project documentation
├── PROJECT_CONTEXT.md   # Project overview for LLM context
├── .gitignore          # Git ignore rules
└── .gitattributes      # Git attributes

### Assets
/assets/
├── 2d/
│   └── interface/
│       ├── common/
│       │   └── unitsicons/
│       │       ├── armes/
│       │       │   └── panel_info/
│       │       ├── cover/
│       │       └── specialties/
│       ├── useingame/
│       │   ├── icones/
│       │   └── minimap/
│       └── useoutgame/
│           ├── division/
│           │   └── emblem/
│           └── tagmod/
└── README.md          # Asset documentation

### Configuration
/config/
├── __init__.py
├── config_loader.py     # Configuration loading logic
├── config.template.YAML # Template configuration
└── config.YAML         # User-specific configuration (gitignored)

### Source Code
/src/
├── __init__.py         # ModConfig singleton
├── main.py            # Main build process
├── gameplay_mod.py    # Gameplay modification pipeline
├── ui_mod.py         # UI modification pipeline
│
├── dics/             # Dictionary/Localization data
│   ├── ui/          # UI-related text
│   │   ├── traits.py
│   │   └── unit_info_panel.py
│   └── veterancy/   # veterancy-related text
│       └── vet_bonuses.py
│
├── data/              # Game data management
│   ├── database/     # Persistent JSON database storage
│   │   ├── depictions.json
│   │   ├── units.json
│   │   └── weapons.json
│   ├── __init__.py      # Data collection orchestration
│   ├── source_loader.py # Source file loading
│   ├── depiction_data.py # Weapon depiction data
│   ├── persistence.py  # Database persistence utilities
│   ├── unit_data.py    # Unit data processing
│   └── ammo_data.py    # Ammunition data processing
│
├── constants/         # Game constants and data
│   ├── division_edits/
│   │   └── matrix_data.py
│   ├── effects/
│   │   └── capacities.py
│   ├── ui/
│   │   ├── divisions.py
│   │   └── icons.py
│   ├── unit_edits/   # Unit edits by nation
│   │   ├── FR_unit_edits.py
│   │   ├── POL_unit_edits.py
│   │   ├── RDA_unit_edits.py
│   │   ├── RFA_unit_edits.py
│   │   ├── SOV_unit_edits.py
│   │   ├── UK_unit_edits.py
│   │   └── USA_unit_edits.py
│   └── weapons/
│       ├── ammunition/
│       │   ├── autocanon.py
│       │   ├── canon.py
│       │   ├── howitzer.py
│       │   ├── mlrs.py
│       │   └── ...
│       ├── missiles/
│       │   ├── a2a.py
│       │   ├── aa.py
│       │   ├── atgm.py
│       │   └── ...
│       └── damage_values.py
│
├── gameplay/         # Gameplay modification modules
│   ├── depictions/  # Visual representation editors
│   │   ├── infantry.py
│   │   └── showroom.py
│   ├── divisions/   # Division modification
│   │   ├── matrices.py
│   │   └── unit_edits.py
│   ├── division_rules/
│   │   ├── mg_teams.py
│   │   └── unit_edits.py
│   ├── effects/     # Game effect editors
│   │   ├── critical_effects.py
│   │   └── effects.py
│   ├── terrains/    # Terrain modification
│   │   └── terrains.py
│   ├── ui/          # UI modification
│   │   ├── divisions.py
│   │   ├── ingame_icons.py
│   │   ├── traits.py
│   │   └── unit_info_panel.py
│   ├── unit_descriptor/  # Unit property editors
│   │   ├── cover.py
│   │   ├── deployment.py
│   │   ├── infantry.py
│   │   ├── mg_teams.py
│   │   ├── optics.py
│   │   ├── team.py
│   │   └── unit_edits.py
│   ├── veterancy/   # Experience system
│   │   └── vet_bonuses.py
│   ├── weapons/     # Weapon system editors
│   │   ├── ammunition.py
│   │   ├── damage_families.py
│   │   ├── missiles.py
│   │   ├── mortar_mods.py
│   │   └── vanilla_modifications.py
│   ├── editors.py   # Top-level editor organization
│   └── gd_constants.py  # Game data constants
│
└── utils/            # Utility functions
    ├── config_utils.py
    ├── dictionary_utils.py
    ├── logging_utils.py
    └── ndf_utils.py

### Development
/logs/                # Log files (gitignored)
└── .gitkeep

warno-actual.code-workspace  # VSCode workspace settings

## Key Components and Responsibilities

### 1. Configuration Management
- config_loader.py: Loads and validates YAML configuration
- ModConfig (src/__init__.py): Singleton for accessing configuration
- Handles paths, build targets, and mod settings

### Configuration Loading Flow:
1. config_loader.py:
   - ConfigLoader class that handles validation and processing
   - Validates required sections (build_config, directories, etc.)
   - Validates required fields in each section
   - Provides structured access to configuration data

2. ModConfig (src/__init__.py):
   - Singleton pattern ensures single configuration instance
   - Uses ConfigLoader to load and validate configuration
   - Provides application-wide access to configuration
   - Adds helper methods like get_mod_paths()

### Configuration Hierarchy:
```
config_loader.py (validation)
    ↓
ModConfig (singleton access)
    ↓
Application code
```

The separation allows:
- Simple YAML loading (config.py) to be separated from validation logic
- Complex validation rules to be centralized in ConfigLoader
- Clean singleton access through ModConfig

### 2. Build Pipeline
- run_patcher.py: Entry point, initializes configuration
- main.py: Orchestrates the build process
- gameplay_mod.py: Handles gameplay modifications
- ui_mod.py: Handles UI modifications

### 3. Data Management
├── data/              # Game data management
│   ├── database/     # Persistent JSON database storage
│   │   ├── depictions.json
│   │   ├── units.json
│   │   └── weapons.json
│   ├── __init__.py      # Data collection orchestration
│   ├── source_loader.py # Source file loading
│   ├── depiction_data.py # Weapon depiction data
│   ├── persistence.py  # Database persistence utilities
│   ├── unit_data.py    # Unit data processing
│   └── ammo_data.py    # Ammunition data processing

### Database System
1. Build Process (when build_database=true):
   - Loads NDF files from source paths
   - Collects data processing functions
   - Executes data builders in sequence
   - Processes into structured data
   - Caches in memory for immediate use
   - Saves to JSON for future use

2. Load Process (when build_database=false):
   - Loads pre-built JSON database
   - Caches in memory for reuse

3. Data Collection Flow:
   ```
   data/__init__.py (collects builders)
       ↓
   source_loader.py (loads NDF files)
       ↓
   Individual data processors
   (unit_data.py, ammo_data.py, etc.)
       ↓
   persistence.py (saves to disk)
   ```

4. Usage:
   - Gameplay editors access cached database
   - Single load/build per patcher run
   - Persistent storage for faster startup

### 4. Utilities
- dictionary_utils.py: Handles writing to localization files (INTERFACE_INGAME.csv, UNITS.csv, etc.)
- ndf_utils.py: NDF file parsing and modification
- logging_utils.py: Centralized logging functionality
- config_utils.py: Configuration utility functions

### 5. Dictionary/Localization System
- dics/ui/: UI-related text definitions
  - traits.py: Unit trait and specialty descriptions
  - unit_info_panel.py: Unit panel text and tooltips
- dics/veterancy/: Experience-related text
  - vet_bonuses.py: Veterancy level descriptions
- Writes to various .csv files:
  - INTERFACE_INGAME.csv: In-game UI text
  - UNITS.csv: Unit-related text
  - INTERFACE_OUTGAME.csv: Menu and setup text

### 6. Gameplay Modifications
- divisions/: Division-related modifications
- weapons/: Weapon system modifications
- veterancy/: Experience and veterancy systems
- editors.py: Editor function mapping

## File Types
- .py: Python source code
- .YAML: Configuration files
- .csv: Dictionary/localization files
- .ndf: Game data files (modified by the patcher)
- .md: Documentation

## Development Notes
- Uses singleton pattern for configuration management
- Modular design for separate gameplay and UI modifications
- Extensive logging for debugging and verification
- Configuration-driven build process 

### Database System
1. Build Process (when build_database=true):
   - Loads NDF files from source paths
   - Collects data processing functions
   - Executes data builders in sequence
   - Processes into structured data
   - Caches in memory for immediate use
   - Saves to JSON for future use

2. Load Process (when build_database=false):
   - Loads pre-built JSON database
   - Caches in memory for reuse

3. Data Collection Flow:
   ```
   data/__init__.py (collects builders)
       ↓
   source_loader.py (loads NDF files)
       ↓
   Individual data processors
   (unit_data.py, ammo_data.py, etc.)
       ↓
   persistence.py (saves to disk)
   ```

4. Usage:
   - Gameplay editors access cached database
   - Single load/build per patcher run
   - Persistent storage for faster startup 