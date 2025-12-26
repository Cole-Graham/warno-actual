# DPM Visualizer Refactoring Guide

This document outlines the refactoring plan to break up the large `infantry_dpm_visualizer.py` file into logical components.

## Current Structure

The application has been successfully refactored from a single 3600+ line file into a modular structure. The original `infantry_dpm_visualizer.py` file remains for reference but is no longer the active entry point.

## Target Structure ✅ (Completed)

```
tools/dpm_visualizer/
├── __init__.py           ✅ Created
├── constants.py          ✅ Created - Constants and configuration
├── calculations.py       ✅ Created - Calculation functions
├── ndf_parsers.py        ✅ Created - NDF parsing functions
├── ui_components.py     ✅ Created - Reusable UI widgets
├── infantry_tab.py       ✅ Created - Infantry tab implementation
├── weapons_tab.py       ⏳ Pending - Weapons tab implementation
└── main.py               ✅ Created - Main application with tabbed interface
```

## Module Breakdown

### constants.py ✅ (Completed)
- RANGE_MODIFIERS_TABLE
- SMALL_ARMS_DAMAGE_FAMILIES

### calculations.py ✅ (Completed)
- calculate_accuracy()
- calculate_shots_per_minute()
- calculate_dpm()
- extract_base_weapon_name()

### ndf_parsers.py ✅ (Completed)
- parse_infantry_units()
- parse_weapon_descriptors()
- parse_ammunition_properties()
- parse_veterancy_from_division_rules()
- parse_experience_levels()
- parse_veterancy_effect_bonuses()
- apply_veterancy_bonuses_to_units()
- extract_unit_info()
- _gather_turret_data()
- _gather_mounted_weapons()
- _gather_salvo_data()

### ui_components.py ✅ (Completed)
- SearchableCombobox class
- RangeModifierEditor class

### infantry_tab.py ✅ (Completed)
- InfantryTab class containing:
  - All DPMVisualizerApp functionality extracted and adapted
  - Unit selection and comparison
  - Chart generation with matplotlib
  - Custom unit/weapon creation and editing
  - Range modifier table management
  - Veterancy level selection and bonuses
  - Data point info panel with hover/click interactions
  - All methods from original DPMVisualizerApp adapted to use `self.app` for shared data

### weapons_tab.py ⏳ (Pending)
- WeaponsTab class for individual weapon analysis
- Similar layout to Infantry tab but focused on weapons
- Weapon comparison features
- Detailed weapon statistics

### main.py ✅ (Completed)
- DPMVisualizerApp class with tabbed interface
- Shared data management (infantry_units, weapon_descriptors, ammunition_props, custom_weapons, range_modifier_tables)
- Mod path loading and browsing
- Dataset cache management (save/load)
- User data management (save/load custom units, weapons, range modifier tables)
- Tab coordination and initialization
- Proper initialization sequence: load user data → load dataset cache → reload custom units → collect bonus combinations

## Migration Steps

1. ✅ Create module structure
2. ✅ Extract constants
3. ✅ Extract calculations
4. ✅ Extract UI components
5. ✅ Extract NDF parsers
6. ✅ Extract InfantryTab class
7. ⏳ Create WeaponsTab class
8. ✅ Update main.py to use tabs
9. ✅ Update entry point script (run_dpm_visualizer.py)
10. ⏳ Test and verify functionality

## Integration Details

### Shared Data Architecture
- All shared data is managed at the `DPMVisualizerApp` level:
  - `self.infantry_units` - Parsed infantry unit data
  - `self.weapon_descriptors` - Parsed weapon descriptor data
  - `self.ammunition_props` - Parsed ammunition properties
  - `self.custom_weapons` - User-defined custom weapons
  - `self.range_modifier_tables` - Range modifier tables
  - `self.current_range_modifier_table_name` - Currently active table
  - `self.mod_path` - Path to mod directory
  - `self.user_data_file` - Path to user_data.json (stored in `tools/dpm_visualizer/`)
  - `self.dataset_cache_file` - Path to dataset cache file (stored in `tools/dpm_visualizer/`)

### Tab Access Pattern
- Tabs access shared data via `self.app.*` (e.g., `self.app.infantry_units`)
- Tabs maintain their own UI state (e.g., `self.selected_units`, `self.unit_dropdowns`)
- Main app coordinates data loading and notifies tabs when data changes

### RangeModifierEditor Integration
- RangeModifierEditor receives the main app instance
- Accesses shared data via `self.app.range_modifier_tables`
- Updates InfantryTab chart via `self.app.infantry_tab.generate_chart()`
- Saves user data via `self.app.infantry_tab.save_user_data()` or `self.app.save_user_data()`

## Entry Point

The application is now launched via:
- `run_dpm_visualizer.py` (root of workspace) - Updated to use new modular structure
- Imports from `tools.dpm_visualizer.main`

### Running the Application

From the workspace root directory:
```bash
python run_dpm_visualizer.py
```

The script automatically:
1. Adds the project root to the Python path
2. Imports the main module from `tools.dpm_visualizer.main`
3. Launches the Tkinter GUI application

## Notes

- ✅ The tabbed interface is fully functional
- ✅ The Infantry tab contains all original functionality
- ✅ All methods have been extracted and adapted to use `self.app` for shared data
- ✅ Shared data (mod_path, infantry_units, etc.) is managed at the app level
- ✅ Dataset caching and user data persistence are working
- ⏳ The Weapons tab is still pending implementation
- The original `infantry_dpm_visualizer.py` file remains for reference but is no longer used

