"""Main application entry point for DPM Visualizer."""

import json
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from .constants import RANGE_MODIFIERS_TABLE
from .ndf_parsers import (
    parse_infantry_units,
    parse_weapon_descriptors,
    parse_ammunition_properties,
    parse_shock_bonuses,
    parse_shock_range,
    parse_militia_bonuses,
    parse_reservist_bonuses,
)
from .ui_components import SearchableCombobox
from .infantry_tab import InfantryTab
from .weapons_tab import WeaponsTab


class DPMVisualizerApp:
    """Main application class with tabbed interface."""
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("DPM Visualizer")
        self.root.geometry("1600x1200")  # Taller window to accommodate chart, info panel, and custom sections
        
        # Shared data that both tabs will use
        self.mod_path: Optional[Path] = None
        self.infantry_units: Dict[str, Dict[str, Any]] = {}
        self.weapon_descriptors: Dict[str, Dict[str, Any]] = {}
        self.ammunition_props: Dict[str, Dict[str, Any]] = {}
        self.custom_weapons: Dict[str, Dict[str, Any]] = {}
        
        # Shock trait bonuses and range (parsed from game files)
        self.shock_bonuses: Dict[str, float] = {
            "damage_multiplier": 1.15,
            "salvo_reload_multiplier": 0.85,
            "shot_time_multiplier": 0.85,
            "aim_time_multiplier": 0.85,
        }
        self.shock_range: float = 100.0
        
        # Militia trait bonuses (parsed from game files)
        self.militia_bonuses: Dict[str, float] = {
            "reload_speed_multiplier": 1.20,
            "aim_time_multiplier": 1.20,
        }
        
        # Reservist trait bonuses (parsed from game files)
        self.reservist_bonuses: Dict[str, float] = {
            "reload_speed_multiplier": 1.20,
            "aim_time_multiplier": 1.20,
        }
        
        # Range modifier tables (shared between tabs, global across profiles)
        self.range_modifier_tables: Dict[str, List[Tuple[float, float]]] = {
            "vanilla": RANGE_MODIFIERS_TABLE.copy()
        }
        # Flag for each table: True = multiplicative veterancy bonus, False = flat bonus
        self.range_modifier_vet_bonus_type: Dict[str, bool] = {
            "vanilla": False  # Vanilla uses flat bonus by default
        }
        self.current_range_modifier_table_name: str = "vanilla"
        
        # Profile management (profiles contain custom_units and custom_weapons)
        self.current_profile: str = "default"
        self.profiles: Dict[str, Dict[str, Any]] = {}  # profile_name -> {custom_units: {}, custom_weapons: {}}
        
        # User data file path (stored in dpm_visualizer subdirectory)
        self.user_data_file = Path(__file__).parent / "user_data.json"
        self.dataset_cache_file = Path(__file__).parent / "dpm_visualizer_cache.json"
        
        # Store pending custom units to load after dataset cache
        self._pending_custom_units = {}
        # Store pending UI state to load after tabs are initialized
        self._pending_ui_state = {}
        
        self.setup_ui()
        
        # Bind window close event to save data
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Load saved user data (range modifier tables, custom units, custom weapons)
        self.load_user_data()
        
        # Update profile dropdown after loading
        if hasattr(self, 'profile_combo'):
            self.update_profile_dropdown()
        
        # Update range table dropdowns after loading user data
        if hasattr(self, 'weapons_tab') and hasattr(self.weapons_tab, 'range_table_combo'):
            self.weapons_tab.range_table_combo['values'] = list(self.range_modifier_tables.keys())
            if self.current_range_modifier_table_name in self.range_modifier_tables:
                self.weapons_tab.range_table_var.set(self.current_range_modifier_table_name)
        
        # Try to load cached dataset (after UI is set up so mod_path_var exists)
        self.load_dataset_cache()
        
        # Reload custom units after cache (they may have been overwritten)
        self.reload_custom_units_after_cache()
        
        # Load UI state after everything is initialized
        self.load_ui_state()
        
        # Collect bonus combinations after loading data (needed for veterancy dropdowns)
        if self.infantry_units:
            if hasattr(self.infantry_tab, 'collect_bonus_combinations'):
                self.infantry_tab.collect_bonus_combinations()
            # Also collect for weapons tab
            if hasattr(self, 'weapons_tab') and hasattr(self.weapons_tab, 'collect_bonus_combinations'):
                self.weapons_tab.collect_bonus_combinations()
                # Update bonus dropdowns
                if hasattr(self.weapons_tab, 'weapon_bonus_combos'):
                    bonus_strings = self.weapons_tab.get_bonus_display_strings()
                    for bonus_combo in self.weapons_tab.weapon_bonus_combos:
                        bonus_combo.set_values(bonus_strings)
    
    def setup_ui(self):
        """Set up the tabbed interface."""
        # Top frame for mod path selection (shared across tabs)
        top_frame = ttk.Frame(self.root, padding="10")
        top_frame.pack(fill=tk.X)
        
        ttk.Label(top_frame, text="Mod Path:").pack(side=tk.LEFT, padx=5)
        self.mod_path_var = tk.StringVar()
        ttk.Entry(top_frame, textvariable=self.mod_path_var, width=50).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        ttk.Button(top_frame, text="Browse", command=self.browse_mod_path).pack(side=tk.LEFT, padx=5)
        ttk.Button(top_frame, text="Load Data", command=self.load_data).pack(side=tk.LEFT, padx=5)
        
        # Profile selection frame
        profile_frame = ttk.Frame(top_frame)
        profile_frame.pack(side=tk.RIGHT, padx=5)
        ttk.Label(profile_frame, text="Profile:").pack(side=tk.LEFT, padx=(10, 5))
        self.profile_var = tk.StringVar(value=self.current_profile)
        self.profile_combo = ttk.Combobox(profile_frame, textvariable=self.profile_var, state="readonly", width=15)
        self.profile_combo.pack(side=tk.LEFT, padx=2)
        self.profile_combo.bind("<<ComboboxSelected>>", self.on_profile_changed)
        ttk.Button(profile_frame, text="New", command=self.create_profile).pack(side=tk.LEFT, padx=2)
        ttk.Button(profile_frame, text="Delete", command=self.delete_profile).pack(side=tk.LEFT, padx=2)
        self.update_profile_dropdown()
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Bind tab change event to close all dropdowns and auto-save
        self.notebook.bind("<<NotebookTabChanged>>", lambda e: [self.on_tab_changed(), self.auto_save_state()])
        
        # Bind window focus events to close dropdowns when window loses focus
        self.root.bind("<FocusOut>", self.on_window_focus_out)
        
        # Create Infantry tab frame
        self.infantry_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.infantry_frame, text="Infantry")
        
        # Create Weapons tab frame
        self.weapons_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.weapons_frame, text="Weapons")
        
        # Initialize tabs
        self.infantry_tab = InfantryTab(self.infantry_frame, self)
        self.weapons_tab = WeaponsTab(self.weapons_frame, self)
    
    def on_tab_changed(self, event=None):
        """Handle tab change - close all open dropdowns."""
        from .ui_components import SearchableCombobox
        SearchableCombobox.close_all_dropdowns()
    
    def on_window_focus_out(self, event=None):
        """Handle window focus loss - close all open dropdowns."""
        from .ui_components import SearchableCombobox
        SearchableCombobox.close_all_dropdowns()
    
    def browse_mod_path(self):
        """Browse for mod directory."""
        # Try to get default path from config if available
        initial_dir = None
        try:
            from config.config_loader import ConfigLoader
            config_path = Path(__file__).parent.parent.parent / "config" / "config.YAML"
            if config_path.exists():
                config_loader = ConfigLoader(str(config_path))
                config_data = config_loader.load()
                if config_data and "directories" in config_data:
                    warno_mods = config_data["directories"].get("warno_mods", "")
                    gameplay_dev = config_data["directories"].get("gameplay_dev", "")
                    if warno_mods and gameplay_dev:
                        initial_dir = str(Path(warno_mods) / gameplay_dev)
        except Exception:
            pass  # Ignore config errors
        
        path = filedialog.askdirectory(title="Select Mod Directory", initialdir=initial_dir)
        if path:
            self.mod_path_var.set(path)
            self.mod_path = Path(path)
    
    def load_data(self):
        """Load data from NDF files."""
        mod_path_str = self.mod_path_var.get()
        if not mod_path_str:
            messagebox.showerror("Error", "Please select a mod directory")
            return
        
        self.mod_path = Path(mod_path_str)
        
        if not self.mod_path.exists():
            messagebox.showerror("Error", f"Mod path does not exist: {self.mod_path}")
            return
        
        try:
            # Preserve custom units before parsing
            custom_units_backup = {}
            for unit_name, unit_info in self.infantry_units.items():
                if unit_info.get("custom_unit", False):
                    custom_units_backup[unit_name] = unit_info
            
            # Parse data
            self.infantry_units = parse_infantry_units(self.mod_path)
            self.weapon_descriptors = parse_weapon_descriptors(self.mod_path)
            self.ammunition_props = parse_ammunition_properties(self.mod_path)
            
            # Restore custom units after parsing
            self.infantry_units.update(custom_units_backup)
            
            # Parse shock bonuses and range
            self.shock_bonuses = parse_shock_bonuses(self.mod_path)
            self.shock_range = parse_shock_range(self.mod_path)
            
            # Parse militia bonuses
            self.militia_bonuses = parse_militia_bonuses(self.mod_path)
            
            # Parse reservist bonuses
            self.reservist_bonuses = parse_reservist_bonuses(self.mod_path)
            
            # Save dataset to cache file
            self.save_dataset_cache()
            
            # Update Infantry tab UI
            if hasattr(self, 'infantry_tab'):
                # Update unit dropdowns
                self.infantry_tab.unit_display_names = []
                for unit_name in sorted(self.infantry_units.keys()):
                    self.infantry_tab.unit_display_names.append(unit_name)
                
                # Update all existing dropdowns
                for dropdown in self.infantry_tab.unit_dropdowns:
                    if hasattr(dropdown, 'set_values'):
                        dropdown.set_values(self.infantry_tab.unit_display_names)
                
                # Update custom unit weapon dropdowns
                if hasattr(self.infantry_tab, 'update_custom_weapon_dropdowns'):
                    self.infantry_tab.update_custom_weapon_dropdowns()
                
                # Update bonus combinations dropdowns
                if hasattr(self.infantry_tab, 'collect_bonus_combinations'):
                    self.infantry_tab.collect_bonus_combinations()
                
                # Update load unit dropdown
                if hasattr(self.infantry_tab, 'load_unit_combo'):
                    self.infantry_tab.load_unit_combo.set_values(self.infantry_tab.unit_display_names)
                
                # Reload custom units from user_data.json after loading data
                # First, load user data to populate _pending_custom_units
                self.load_user_data()
                # Then reload custom units
                if hasattr(self.infantry_tab, 'reload_custom_units_after_cache'):
                    self.infantry_tab.reload_custom_units_after_cache()
                elif hasattr(self, 'reload_custom_units_after_cache'):
                    self.reload_custom_units_after_cache()
            
            # Update Weapons tab UI
            if hasattr(self, 'weapons_tab'):
                # Collect bonus combinations
                if hasattr(self.weapons_tab, 'collect_bonus_combinations'):
                    self.weapons_tab.collect_bonus_combinations()
                
                # Update weapon dropdowns (use ammunition_props instead of weapon_descriptors)
                self.weapons_tab.weapon_display_names = []
                for ammo_name in sorted(self.ammunition_props.keys()):
                    self.weapons_tab.weapon_display_names.append(ammo_name)
                # Add custom weapons
                if hasattr(self, 'custom_weapons') and self.custom_weapons:
                    for custom_name in sorted(self.custom_weapons.keys()):
                        if custom_name not in self.weapons_tab.weapon_display_names:
                            self.weapons_tab.weapon_display_names.append(custom_name)
                
                # Update all existing dropdowns
                for dropdown in self.weapons_tab.weapon_dropdowns:
                    if hasattr(dropdown, 'set_values'):
                        dropdown.set_values(self.weapons_tab.weapon_display_names)
                
                # Update bonus dropdowns
                if hasattr(self.weapons_tab, 'weapon_bonus_combos'):
                    bonus_strings = self.weapons_tab.get_bonus_display_strings()
                    for bonus_combo in self.weapons_tab.weapon_bonus_combos:
                        bonus_combo.set_values(bonus_strings)
            
            messagebox.showinfo("Success", f"Loaded {len(self.infantry_units)} infantry units")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")
    
    def save_dataset_cache(self):
        """Save the current dataset to cache file (saves mod path and parsed data)."""
        try:
            # Serialize the data structures
            cache_data = {
                "cache_version": "2.4",  # Version 2.4: Added reservist trait support
                "mod_path": str(self.mod_path),
                "infantry_units": self._serialize_infantry_units(),
                "weapon_descriptors": self._serialize_weapon_descriptors(),
                "ammunition_props": self.ammunition_props,  # Already JSON-serializable (includes suppress_damages)
                "shock_bonuses": self.shock_bonuses,
                "shock_range": self.shock_range,
                "militia_bonuses": self.militia_bonuses,
                "reservist_bonuses": self.reservist_bonuses,
            }
            
            with open(self.dataset_cache_file, 'w', encoding='utf-8') as f:
                json.dump(cache_data, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            print(f"Warning: Failed to save dataset cache: {e}")
    
    def _serialize_infantry_units(self) -> Dict[str, Dict[str, Any]]:
        """Serialize infantry units data to JSON-serializable format."""
        serialized = {}
        for unit_name, unit_info in self.infantry_units.items():
            # Skip custom units - they're saved in user_data.json
            if unit_info.get("custom_unit", False):
                continue
            
            # Convert any multiplicative bonuses to flat before serializing (safety check)
            acc_bonuses = unit_info.get("veterancy_accuracy_bonuses", {})
            if acc_bonuses:
                converted_bonuses = {}
                for level, bonus_value in acc_bonuses.items():
                    if bonus_value > 1.0:
                        # This looks like a multiplier (e.g., 1.12), convert to flat (0.12)
                        converted_bonuses[level] = bonus_value - 1.0
                    else:
                        # Already flat or zero
                        converted_bonuses[level] = bonus_value
                acc_bonuses = converted_bonuses
            
            serialized[unit_name] = {
                "is_infantry": unit_info.get("is_infantry", False),
                "tags": unit_info.get("tags", []),
                "unit_role": unit_info.get("unit_role"),
                "display_name": unit_info.get("display_name"),
                "veterancy_pack": unit_info.get("veterancy_pack", "simple_v3"),
                "available_veterancy_levels": unit_info.get("available_veterancy_levels", [0, 1, 2, 3]),
                "experience_levels_pack": unit_info.get("experience_levels_pack"),
                "veterancy_accuracy_bonuses": acc_bonuses,
                "veterancy_reload_speed_multipliers": unit_info.get("veterancy_reload_speed_multipliers", {}),
                "has_shock_trait": unit_info.get("has_shock_trait", False),
                "has_militia_trait": unit_info.get("has_militia_trait", False),
                "has_reservist_trait": unit_info.get("has_reservist_trait", False),
                "price": unit_info.get("price"),
                "strength": unit_info.get("strength"),  # Include strength for target strength dropdown
            }
        return serialized
    
    def _serialize_weapon_descriptors(self) -> Dict[str, Dict[str, Any]]:
        """Serialize weapon descriptors data to JSON-serializable format."""
        serialized = {}
        for weapon_name, weapon_data in self.weapon_descriptors.items():
            serialized_weapon = {
                "turrets": {},
                "salvos": weapon_data.get("salvos", {}),
            }
            
            # Serialize turret data
            for turret_idx, turret_data in weapon_data.get("turrets", {}).items():
                serialized_turret = {
                    "yul_bone": turret_data.get("yul_bone"),
                    "weapons": {},
                }
                
                # Serialize weapon data
                for ammo_name, weapon_info in turret_data.get("weapons", {}).items():
                    serialized_turret["weapons"][ammo_name] = {
                        "salvo_index": weapon_info.get("salvo_index"),
                        "salvos": weapon_info.get("salvos", 0),
                        "quantity": weapon_info.get("quantity", 1),
                    }
                
                serialized_weapon["turrets"][turret_idx] = serialized_turret
            
            serialized[weapon_name] = serialized_weapon
        
        return serialized
    
    def load_dataset_cache(self):
        """Load dataset cache file if it exists (restores mod path and cached data)."""
        if not self.dataset_cache_file.exists():
            return False
        
        try:
            with open(self.dataset_cache_file, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
            
            # Check cache version - invalidate old caches that don't have multiplicative->flat conversion
            cache_version = cache_data.get("cache_version", "1.0")
            if cache_version < "2.4":
                print(f"Warning: Cache version {cache_version} is outdated (needs 2.4+). Cache will be regenerated.")
                return False
            
            # Restore mod path
            cached_mod_path = cache_data.get("mod_path", "")
            if not cached_mod_path:
                return False
            
            # Check if cached mod path still exists
            if not Path(cached_mod_path).exists():
                print(f"Warning: Cached mod path no longer exists: {cached_mod_path}")
                return False
            
            if hasattr(self, 'mod_path_var'):
                self.mod_path_var.set(cached_mod_path)
            self.mod_path = Path(cached_mod_path)
            
            # Load cached data if available
            if "infantry_units" in cache_data and "weapon_descriptors" in cache_data and "ammunition_props" in cache_data:
                try:
                    # Preserve custom units before overwriting infantry_units
                    custom_units_backup = {}
                    for unit_name, unit_info in self.infantry_units.items():
                        if unit_info.get("custom_unit", False):
                            custom_units_backup[unit_name] = unit_info
                    
                    # Deserialize infantry units (bonuses should be included)
                    self.infantry_units = cache_data["infantry_units"]
                    self.weapon_descriptors = cache_data["weapon_descriptors"]
                    self.ammunition_props = cache_data["ammunition_props"]
                    
                    # Convert any multiplicative bonuses to flat when loading from cache (safety check)
                    for unit_name, unit_info in self.infantry_units.items():
                        acc_bonuses = unit_info.get("veterancy_accuracy_bonuses", {})
                        if acc_bonuses:
                            converted_bonuses = {}
                            for level, bonus_value in acc_bonuses.items():
                                bonus_float = float(bonus_value) if isinstance(bonus_value, (str, int)) else bonus_value
                                if bonus_float > 1.0:
                                    # This looks like a multiplier (e.g., 1.12), convert to flat (0.12)
                                    converted_bonuses[level] = bonus_float - 1.0
                                else:
                                    # Already flat or zero
                                    converted_bonuses[level] = bonus_float
                            unit_info["veterancy_accuracy_bonuses"] = converted_bonuses
                    
                    # Restore custom units after loading cache
                    self.infantry_units.update(custom_units_backup)
                    
                    # Load shock bonuses and range if available
                    if "shock_bonuses" in cache_data:
                        self.shock_bonuses = cache_data["shock_bonuses"]
                    if "shock_range" in cache_data:
                        self.shock_range = float(cache_data["shock_range"])
                    
                    # Load militia bonuses if available
                    if "militia_bonuses" in cache_data:
                        self.militia_bonuses = cache_data["militia_bonuses"]
                    else:
                        # Default values if not in cache
                        self.militia_bonuses = {
                            "reload_speed_multiplier": 1.20,
                            "aim_time_multiplier": 1.20,
                        }
                    
                    # Load reservist bonuses if available
                    if "reservist_bonuses" in cache_data:
                        self.reservist_bonuses = cache_data["reservist_bonuses"]
                    else:
                        # Default values if not in cache
                        self.reservist_bonuses = {
                            "reload_speed_multiplier": 1.20,
                            "aim_time_multiplier": 1.20,
                        }
                    
                    # Ensure bonus dictionary keys are integers (JSON loads them as strings)
                    # Also convert any multiplicative bonuses to flat bonuses (safety check for old cache files)
                    for unit_name, unit_info in self.infantry_units.items():
                        # Convert veterancy_accuracy_bonuses keys from string to int if needed
                        # Also convert multiplicative values (> 1.0) to flat values
                        if "veterancy_accuracy_bonuses" in unit_info:
                            acc_bonuses = unit_info["veterancy_accuracy_bonuses"]
                            if acc_bonuses:
                                sample_key = next(iter(acc_bonuses.keys())) if acc_bonuses else None
                                if sample_key is not None and isinstance(sample_key, str):
                                    acc_bonuses = {int(k): float(v) for k, v in acc_bonuses.items()}
                                
                                # Convert multiplicative bonuses to flat (detect multipliers > 1.0)
                                converted_bonuses = {}
                                for level, bonus_value in acc_bonuses.items():
                                    if bonus_value > 1.0:
                                        # This looks like a multiplier (e.g., 1.12), convert to flat (0.12)
                                        converted_bonuses[level] = bonus_value - 1.0
                                    else:
                                        # Already flat or zero
                                        converted_bonuses[level] = bonus_value
                                
                                unit_info["veterancy_accuracy_bonuses"] = converted_bonuses
                        
                        # Convert veterancy_reload_speed_multipliers keys from string to int if needed
                        if "veterancy_reload_speed_multipliers" in unit_info:
                            reload_multipliers = unit_info["veterancy_reload_speed_multipliers"]
                            if reload_multipliers:
                                sample_key = next(iter(reload_multipliers.keys())) if reload_multipliers else None
                                if sample_key is not None and isinstance(sample_key, str):
                                    unit_info["veterancy_reload_speed_multipliers"] = {int(k): float(v) for k, v in reload_multipliers.items()}
                    
                    # Debug: Check if bonuses are in the loaded data
                    has_bonuses = False
                    bonus_count = 0
                    for unit_name, unit_info in self.infantry_units.items():
                        acc_bonuses = unit_info.get("veterancy_accuracy_bonuses", {})
                        reload_multipliers = unit_info.get("veterancy_reload_speed_multipliers", {})
                        if acc_bonuses and any(v != 0.0 for v in acc_bonuses.values()):
                            has_bonuses = True
                            bonus_count += 1
                        elif reload_multipliers and any(v != 1.0 for v in reload_multipliers.values()):
                            has_bonuses = True
                            bonus_count += 1
                    
                    # If bonuses are missing, re-parse to get them
                    if not has_bonuses:
                        print("Warning: Cached data missing veterancy bonuses, re-parsing...")
                        # Preserve custom units before re-parsing
                        custom_units_backup = {}
                        for unit_name, unit_info in self.infantry_units.items():
                            if unit_info.get("custom_unit", False):
                                custom_units_backup[unit_name] = unit_info
                        
                        self.infantry_units = parse_infantry_units(self.mod_path)
                        self.weapon_descriptors = parse_weapon_descriptors(self.mod_path)
                        self.ammunition_props = parse_ammunition_properties(self.mod_path)
                        
                        # Restore custom units after re-parsing
                        self.infantry_units.update(custom_units_backup)
                        
                        # Parse shock bonuses and range
                        self.shock_bonuses = parse_shock_bonuses(self.mod_path)
                        self.shock_range = parse_shock_range(self.mod_path)
                        
                        # Parse militia and reservist bonuses
                        self.militia_bonuses = parse_militia_bonuses(self.mod_path)
                        self.reservist_bonuses = parse_reservist_bonuses(self.mod_path)
                        
                        self.save_dataset_cache()
                    
                    # Update Infantry tab UI if it exists
                    if hasattr(self, 'infantry_tab'):
                        # Update unit dropdowns
                        self.infantry_tab.unit_display_names = []
                        for unit_name in sorted(self.infantry_units.keys()):
                            self.infantry_tab.unit_display_names.append(unit_name)
                        
                        # Update all existing dropdowns
                        for dropdown in self.infantry_tab.unit_dropdowns:
                            if hasattr(dropdown, 'set_values'):
                                dropdown.set_values(self.infantry_tab.unit_display_names)
                                # Update veterancy selector if unit is already selected
                                unit_name = dropdown.get()
                                if unit_name and unit_name in self.infantry_units:
                                    if hasattr(self.infantry_tab, 'on_unit_selected'):
                                        self.infantry_tab.on_unit_selected(dropdown)
                        
                        # Update load unit dropdown
                        if hasattr(self.infantry_tab, 'load_unit_combo'):
                            self.infantry_tab.load_unit_combo.set_values(self.infantry_tab.unit_display_names)
                        
                        # Update custom unit weapon dropdowns
                        if hasattr(self.infantry_tab, 'update_custom_weapon_dropdowns'):
                            self.infantry_tab.update_custom_weapon_dropdowns()
                        
                        # Reload custom units from user_data.json (they may have been overwritten)
                        if hasattr(self.infantry_tab, 'reload_custom_units_after_cache'):
                            self.infantry_tab.reload_custom_units_after_cache()
                        
                        # Collect bonus combinations and populate veterancy bonus dropdowns
                        if hasattr(self.infantry_tab, 'collect_bonus_combinations'):
                            self.infantry_tab.collect_bonus_combinations()
                    
                    # Update Weapons tab UI if it exists
                    if hasattr(self, 'weapons_tab'):
                        # Collect bonus combinations for weapons tab
                        if hasattr(self.weapons_tab, 'collect_bonus_combinations'):
                            self.weapons_tab.collect_bonus_combinations()
                        
                        # Update weapon dropdowns (use ammunition_props instead of weapon_descriptors)
                        self.weapons_tab.weapon_display_names = []
                        for ammo_name in sorted(self.ammunition_props.keys()):
                            self.weapons_tab.weapon_display_names.append(ammo_name)
                        # Add custom weapons
                        for custom_name in sorted(self.custom_weapons.keys()):
                            if custom_name not in self.weapons_tab.weapon_display_names:
                                self.weapons_tab.weapon_display_names.append(custom_name)
                        
                        # Update all existing dropdowns
                        for dropdown in self.weapons_tab.weapon_dropdowns:
                            if hasattr(dropdown, 'set_values'):
                                dropdown.set_values(self.weapons_tab.weapon_display_names)
                        
                        # Update bonus dropdowns
                        if hasattr(self.weapons_tab, 'weapon_bonus_combos'):
                            bonus_strings = self.weapons_tab.get_bonus_display_strings()
                            for bonus_combo in self.weapons_tab.weapon_bonus_combos:
                                bonus_combo.set_values(bonus_strings)
                    
                    return True
                except Exception as e:
                    print(f"Warning: Failed to load cached data: {e}")
                    # Fall through to re-parse if cache is corrupted
            
            # If cache doesn't have data, re-parse from NDF files
            try:
                # Preserve custom units before parsing
                custom_units_backup = {}
                for unit_name, unit_info in self.infantry_units.items():
                    if unit_info.get("custom_unit", False):
                        custom_units_backup[unit_name] = unit_info
                
                self.infantry_units = parse_infantry_units(self.mod_path)
                self.weapon_descriptors = parse_weapon_descriptors(self.mod_path)
                self.ammunition_props = parse_ammunition_properties(self.mod_path)
                
                # Restore custom units after parsing
                self.infantry_units.update(custom_units_backup)
                
                # Parse shock bonuses and range
                self.shock_bonuses = parse_shock_bonuses(self.mod_path)
                self.shock_range = parse_shock_range(self.mod_path)
                
                # Parse militia and reservist bonuses
                self.militia_bonuses = parse_militia_bonuses(self.mod_path)
                self.reservist_bonuses = parse_reservist_bonuses(self.mod_path)
                
                # Save the newly parsed data
                self.save_dataset_cache()
                
                # Update Infantry tab UI if it exists
                if hasattr(self, 'infantry_tab'):
                    # Update unit dropdowns
                    self.infantry_tab.unit_display_names = []
                    for unit_name in sorted(self.infantry_units.keys()):
                        self.infantry_tab.unit_display_names.append(unit_name)
                    
                    # Update all existing dropdowns
                    for dropdown in self.infantry_tab.unit_dropdowns:
                        if hasattr(dropdown, 'set_values'):
                            dropdown.set_values(self.infantry_tab.unit_display_names)
                    
                    # Update custom unit weapon dropdowns
                    if hasattr(self.infantry_tab, 'update_custom_weapon_dropdowns'):
                        self.infantry_tab.update_custom_weapon_dropdowns()
                    
                    # Update load unit dropdown
                    if hasattr(self.infantry_tab, 'load_unit_combo'):
                        self.infantry_tab.load_unit_combo.set_values(self.infantry_tab.unit_display_names)
                    
                    # Reload custom units from user_data.json (they may have been overwritten)
                    if hasattr(self.infantry_tab, 'reload_custom_units_after_cache'):
                        self.infantry_tab.reload_custom_units_after_cache()
                    
                    # Collect bonus combinations and populate veterancy bonus dropdowns
                    if hasattr(self.infantry_tab, 'collect_bonus_combinations'):
                        self.infantry_tab.collect_bonus_combinations()
                
                # Update Weapons tab UI if it exists
                if hasattr(self, 'weapons_tab'):
                    # Update weapon dropdowns (use ammunition_props instead of weapon_descriptors)
                    self.weapons_tab.weapon_display_names = []
                    for ammo_name in sorted(self.ammunition_props.keys()):
                        self.weapons_tab.weapon_display_names.append(ammo_name)
                    # Add custom weapons
                    for custom_name in sorted(self.custom_weapons.keys()):
                        if custom_name not in self.weapons_tab.weapon_display_names:
                            self.weapons_tab.weapon_display_names.append(custom_name)
                    
                    # Update all existing dropdowns
                    for dropdown in self.weapons_tab.weapon_dropdowns:
                        if hasattr(dropdown, 'set_values'):
                            dropdown.set_values(self.weapons_tab.weapon_display_names)
                
                return True
            except Exception as e:
                print(f"Warning: Failed to parse data from mod path: {e}")
                return False
            
        except Exception as e:
            print(f"Warning: Failed to load dataset cache: {e}")
            return False
    
    def load_user_data(self):
        """Load user data from JSON file (range modifier tables, custom units, custom weapons)."""
        # Try loading from new consolidated file first
        if self.user_data_file.exists():
            try:
                with open(self.user_data_file, 'r') as f:
                    data = json.load(f)
                    
                    # Load range modifier tables (global, not profile-specific)
                    if "range_modifier_tables" in data:
                        for name, table in data["range_modifier_tables"].items():
                            if name != "vanilla":  # Don't overwrite vanilla
                                self.range_modifier_tables[name] = [tuple(row) for row in table]
                    # Load veterancy bonus type flags
                    if "range_modifier_vet_bonus_type" in data:
                        for name, use_multiplicative in data["range_modifier_vet_bonus_type"].items():
                            if name != "vanilla":  # Don't overwrite vanilla default
                                self.range_modifier_vet_bonus_type[name] = use_multiplicative
                    # Ensure all tables have a flag (default to multiplicative for new tables)
                    for name in self.range_modifier_tables.keys():
                        if name not in self.range_modifier_vet_bonus_type:
                            self.range_modifier_vet_bonus_type[name] = True  # Default to multiplicative for non-vanilla
                    if "current_range_modifier_table" in data:
                        if data["current_range_modifier_table"] in self.range_modifier_tables:
                            self.current_range_modifier_table_name = data["current_range_modifier_table"]
                    
                    # Load profiles
                    if "profiles" in data:
                        self.profiles = data["profiles"]
                    else:
                        # No profiles found, initialize with default
                        self.profiles = {"default": {"custom_units": {}, "custom_weapons": {}}}
                    
                    # Load current profile
                    if "current_profile" in data:
                        self.current_profile = data["current_profile"]
                    else:
                        self.current_profile = "default"
                    
                    # Ensure current profile exists
                    if self.current_profile not in self.profiles:
                        self.profiles[self.current_profile] = {"custom_units": {}, "custom_weapons": {}}
                    
                    # Load current profile's custom units and weapons
                    profile_data = self.profiles[self.current_profile]
                    
                    # Store custom units data for later loading (after dataset cache loads)
                    self._pending_custom_units = {}
                    if "custom_units" in profile_data:
                        for unit_name, unit_info in profile_data["custom_units"].items():
                            # Ensure bonus dictionary keys are integers
                            # Also convert any multiplicative bonuses to flat bonuses (safety check)
                            if "veterancy_accuracy_bonuses" in unit_info:
                                acc_bonuses = unit_info["veterancy_accuracy_bonuses"]
                                if acc_bonuses:
                                    # Convert keys from string to int if needed
                                    if isinstance(next(iter(acc_bonuses.keys())), str):
                                        acc_bonuses = {int(k): float(v) for k, v in acc_bonuses.items()}
                                    
                                    # Convert multiplicative bonuses to flat (detect multipliers > 1.0)
                                    converted_bonuses = {}
                                    for level, bonus_value in acc_bonuses.items():
                                        if bonus_value > 1.0:
                                            # This looks like a multiplier (e.g., 1.12), convert to flat (0.12)
                                            converted_bonuses[level] = bonus_value - 1.0
                                        else:
                                            # Already flat or zero
                                            converted_bonuses[level] = bonus_value
                                    
                                    unit_info["veterancy_accuracy_bonuses"] = converted_bonuses
                            if "veterancy_reload_speed_multipliers" in unit_info:
                                reload_multipliers = unit_info["veterancy_reload_speed_multipliers"]
                                if reload_multipliers and isinstance(next(iter(reload_multipliers.keys())), str):
                                    unit_info["veterancy_reload_speed_multipliers"] = {int(k): float(v) for k, v in reload_multipliers.items()}
                            self._pending_custom_units[unit_name] = unit_info
                            # Also add immediately if infantry_units is already populated
                            if self.infantry_units:
                                self.infantry_units[unit_name] = unit_info
                    
                    # Load custom weapons from current profile
                    if "custom_weapons" in profile_data:
                        self.custom_weapons = profile_data["custom_weapons"].copy()
                        # Update custom weapon dropdowns if UI is set up
                        if hasattr(self, 'infantry_tab') and hasattr(self.infantry_tab, 'update_custom_weapon_dropdowns'):
                            self.infantry_tab.update_custom_weapon_dropdowns()
                        # Update weapons tab dropdowns
                        if hasattr(self, 'weapons_tab') and hasattr(self.weapons_tab, '_initialize_data'):
                            self.weapons_tab._initialize_data()
                    
                    # Store UI state for loading after tabs are initialized
                    if "ui_state" in data:
                        self._pending_ui_state = data["ui_state"]
                    else:
                        self._pending_ui_state = {}
                        
            except Exception as e:
                print(f"Error loading user data: {e}")
                self._pending_ui_state = {}
    
    def reload_custom_units_after_cache(self):
        """Reload custom units from pending data after dataset cache has loaded."""
        if hasattr(self, '_pending_custom_units') and self._pending_custom_units:
            # Add custom units to infantry_units
            for unit_name, unit_info in self._pending_custom_units.items():
                self.infantry_units[unit_name] = unit_info
            
            # Update Infantry tab UI if it exists
            if hasattr(self, 'infantry_tab'):
                # Update unit dropdowns
                self.infantry_tab.unit_display_names = []
                for name in sorted(self.infantry_units.keys()):
                    self.infantry_tab.unit_display_names.append(name)
                
                # Update all existing dropdowns
                for dropdown in self.infantry_tab.unit_dropdowns:
                    if hasattr(dropdown, 'set_values'):
                        dropdown.set_values(self.infantry_tab.unit_display_names)
                
                # Update load unit dropdown
                if hasattr(self.infantry_tab, 'load_unit_combo'):
                    self.infantry_tab.load_unit_combo.set_values(self.infantry_tab.unit_display_names)
            
            # Update Weapons tab dropdowns with custom weapons
            if hasattr(self, 'weapons_tab') and hasattr(self.weapons_tab, '_initialize_data'):
                self.weapons_tab._initialize_data()
    
    def save_user_data(self):
        """Save user data to JSON file (range modifier tables, custom units, custom weapons, UI state)."""
        try:
            # Ensure current profile exists
            if self.current_profile not in self.profiles:
                self.profiles[self.current_profile] = {"custom_units": {}, "custom_weapons": {}}
            
            # Update current profile with current custom units and weapons
            profile_data = self.profiles[self.current_profile]
            profile_data["custom_units"] = {}
            profile_data["custom_weapons"] = self.custom_weapons.copy()
            
            # Save custom units (only those marked as custom_unit)
            for unit_name, unit_info in self.infantry_units.items():
                if unit_info.get("custom_unit", False):
                    profile_data["custom_units"][unit_name] = unit_info.copy()
            
            # Save tab states
            ui_state = {}
            if hasattr(self, 'infantry_tab') and hasattr(self.infantry_tab, 'save_tab_state'):
                ui_state["infantry_tab"] = self.infantry_tab.save_tab_state()
            if hasattr(self, 'weapons_tab') and hasattr(self.weapons_tab, 'save_tab_state'):
                ui_state["weapons_tab"] = self.weapons_tab.save_tab_state()
            
            # Save window geometry
            try:
                geometry = self.root.geometry()
                ui_state["window_geometry"] = geometry
            except:
                pass
            
            # Save selected tab
            try:
                if hasattr(self, 'notebook'):
                    selected_tab = self.notebook.index(self.notebook.select())
                    ui_state["selected_tab"] = selected_tab
            except:
                pass
            
            data = {
                "current_range_modifier_table": self.current_range_modifier_table_name,
                "current_profile": self.current_profile,
                "range_modifier_tables": {},
                "range_modifier_vet_bonus_type": {},
                "profiles": {},
                "ui_state": ui_state,
            }
            
            # Convert range modifier tables tuples to lists for JSON serialization
            for name, table in self.range_modifier_tables.items():
                data["range_modifier_tables"][name] = [list(row) for row in table]
            
            # Save veterancy bonus type flags
            for name, use_multiplicative in self.range_modifier_vet_bonus_type.items():
                data["range_modifier_vet_bonus_type"][name] = use_multiplicative
            
            # Save all profiles
            for profile_name, profile_info in self.profiles.items():
                data["profiles"][profile_name] = {
                    "custom_units": {},
                    "custom_weapons": {}
                }
                # Convert custom units
                for unit_name, unit_info in profile_info.get("custom_units", {}).items():
                    data["profiles"][profile_name]["custom_units"][unit_name] = unit_info.copy()
                # Convert custom weapons
                for weapon_name, weapon_info in profile_info.get("custom_weapons", {}).items():
                    data["profiles"][profile_name]["custom_weapons"][weapon_name] = weapon_info.copy()
            
            with open(self.user_data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save user data: {e}")
    
    def update_profile_dropdown(self):
        """Update the profile dropdown with current profiles."""
        if hasattr(self, 'profile_combo'):
            profile_names = sorted(self.profiles.keys())
            self.profile_combo['values'] = profile_names
            if self.current_profile in profile_names:
                self.profile_var.set(self.current_profile)
    
    def on_profile_changed(self, event=None):
        """Handle profile selection change."""
        new_profile = self.profile_var.get()
        if new_profile == self.current_profile:
            return
        
        # Save current profile data before switching
        self.save_user_data()
        
        # Switch to new profile
        self.current_profile = new_profile
        self.profile_var.set(new_profile)  # Ensure UI is in sync
        
        # Ensure profile exists
        if self.current_profile not in self.profiles:
            self.profiles[self.current_profile] = {"custom_units": {}, "custom_weapons": {}}
        
        # Load new profile's custom units and weapons
        profile_data = self.profiles[self.current_profile]
        
        # Clear current custom units (remove those marked as custom_unit)
        units_to_remove = [name for name, info in self.infantry_units.items() if info.get("custom_unit", False)]
        for unit_name in units_to_remove:
            del self.infantry_units[unit_name]
        
        # Clear current custom weapons
        self.custom_weapons = {}
        
        # Load new profile's custom units
        self._pending_custom_units = {}
        if "custom_units" in profile_data:
            for unit_name, unit_info in profile_data["custom_units"].items():
                # Ensure bonus dictionary keys are integers
                if "veterancy_accuracy_bonuses" in unit_info:
                    acc_bonuses = unit_info["veterancy_accuracy_bonuses"]
                    if acc_bonuses and isinstance(next(iter(acc_bonuses.keys())), str):
                        unit_info["veterancy_accuracy_bonuses"] = {int(k): float(v) for k, v in acc_bonuses.items()}
                if "veterancy_reload_speed_multipliers" in unit_info:
                    reload_multipliers = unit_info["veterancy_reload_speed_multipliers"]
                    if reload_multipliers and isinstance(next(iter(reload_multipliers.keys())), str):
                        unit_info["veterancy_reload_speed_multipliers"] = {int(k): float(v) for k, v in reload_multipliers.items()}
                self._pending_custom_units[unit_name] = unit_info
                # Add immediately if infantry_units is already populated
                if self.infantry_units:
                    self.infantry_units[unit_name] = unit_info
        
        # Load new profile's custom weapons
        if "custom_weapons" in profile_data:
            self.custom_weapons = profile_data["custom_weapons"].copy()
        
        # Reload custom units after cache (if cache is loaded)
        if self.infantry_units:
            self.reload_custom_units_after_cache()
        
        # Update UI
        if hasattr(self, 'infantry_tab'):
            # Update unit dropdowns
            if hasattr(self.infantry_tab, 'unit_display_names'):
                self.infantry_tab.unit_display_names = []
                for name in sorted(self.infantry_units.keys()):
                    self.infantry_tab.unit_display_names.append(name)
                
                # Update all existing dropdowns
                for dropdown in self.infantry_tab.unit_dropdowns:
                    if hasattr(dropdown, 'set_values'):
                        dropdown.set_values(self.infantry_tab.unit_display_names)
                
                # Update load unit dropdown
                if hasattr(self.infantry_tab, 'load_unit_combo'):
                    self.infantry_tab.load_unit_combo.set_values(self.infantry_tab.unit_display_names)
            
            # Update custom weapon dropdowns
            if hasattr(self.infantry_tab, 'update_custom_weapon_dropdowns'):
                self.infantry_tab.update_custom_weapon_dropdowns()
        
        if hasattr(self, 'weapons_tab'):
            # Update weapon dropdowns
            if hasattr(self.weapons_tab, '_initialize_data'):
                self.weapons_tab._initialize_data()
        
        # Save again with the new current_profile
        self.save_user_data()
    
    def create_profile(self):
        """Create a new profile."""
        profile_name = simpledialog.askstring("New Profile", "Enter profile name:")
        if profile_name:
            profile_name = profile_name.strip()
            if not profile_name:
                messagebox.showerror("Error", "Profile name cannot be empty")
                return
            if profile_name in self.profiles:
                messagebox.showerror("Error", f"Profile '{profile_name}' already exists")
                return
            
            # Save current profile before creating new one
            self.save_user_data()
            
            # Create new profile
            self.profiles[profile_name] = {"custom_units": {}, "custom_weapons": {}}
            self.current_profile = profile_name
            self.profile_var.set(profile_name)
            self.update_profile_dropdown()
            
            # Clear current custom units and weapons
            units_to_remove = [name for name, info in self.infantry_units.items() if info.get("custom_unit", False)]
            for unit_name in units_to_remove:
                del self.infantry_units[unit_name]
            self.custom_weapons = {}
            
            # Update UI
            if hasattr(self, 'infantry_tab'):
                if hasattr(self.infantry_tab, 'unit_display_names'):
                    self.infantry_tab.unit_display_names = []
                    for name in sorted(self.infantry_units.keys()):
                        self.infantry_tab.unit_display_names.append(name)
                    
                    for dropdown in self.infantry_tab.unit_dropdowns:
                        if hasattr(dropdown, 'set_values'):
                            dropdown.set_values(self.infantry_tab.unit_display_names)
                    
                    if hasattr(self.infantry_tab, 'load_unit_combo'):
                        self.infantry_tab.load_unit_combo.set_values(self.infantry_tab.unit_display_names)
                
                if hasattr(self.infantry_tab, 'update_custom_weapon_dropdowns'):
                    self.infantry_tab.update_custom_weapon_dropdowns()
            
            if hasattr(self, 'weapons_tab'):
                if hasattr(self.weapons_tab, '_initialize_data'):
                    self.weapons_tab._initialize_data()
            
            # Save the new profile
            self.save_user_data()
    
    def delete_profile(self):
        """Delete the current profile."""
        if len(self.profiles) <= 1:
            messagebox.showerror("Error", "Cannot delete the last profile")
            return
        
        if not messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete profile '{self.current_profile}'?"):
            return
        
        # Save current profile before deletion
        self.save_user_data()
        
        # Delete profile
        del self.profiles[self.current_profile]
        
        # Switch to default profile (or first available)
        if "default" in self.profiles:
            self.current_profile = "default"
        else:
            self.current_profile = sorted(self.profiles.keys())[0]
        
        # Load the new current profile
        self.on_profile_changed()
        
        # Update dropdown
        self.update_profile_dropdown()
    
    def load_ui_state(self):
        """Load saved UI state after tabs are initialized."""
        if not hasattr(self, '_pending_ui_state') or not self._pending_ui_state:
            return
        
        ui_state = self._pending_ui_state
        
        # Load window geometry
        if "window_geometry" in ui_state:
            try:
                self.root.geometry(ui_state["window_geometry"])
            except:
                pass
        
        # Load selected tab
        if "selected_tab" in ui_state and hasattr(self, 'notebook'):
            try:
                tab_index = ui_state["selected_tab"]
                if 0 <= tab_index < self.notebook.index("end"):
                    self.notebook.select(tab_index)
            except:
                pass
        
        # Load infantry tab state
        if "infantry_tab" in ui_state and hasattr(self, 'infantry_tab') and hasattr(self.infantry_tab, 'load_tab_state'):
            try:
                self.infantry_tab.load_tab_state(ui_state["infantry_tab"])
            except Exception as e:
                print(f"Error loading infantry tab state: {e}")
        
        # Load weapons tab state
        if "weapons_tab" in ui_state and hasattr(self, 'weapons_tab') and hasattr(self.weapons_tab, 'load_tab_state'):
            try:
                self.weapons_tab.load_tab_state(ui_state["weapons_tab"])
            except Exception as e:
                print(f"Error loading weapons tab state: {e}")
    
    def auto_save_state(self):
        """Auto-save UI state (called periodically or on state changes)."""
        try:
            # Only save if tabs are initialized
            if hasattr(self, 'infantry_tab') and hasattr(self, 'weapons_tab'):
                # Save user data (which includes UI state)
                self.save_user_data()
        except Exception as e:
            # Silently fail for auto-save to avoid interrupting user
            pass
    
    def on_closing(self):
        """Handle window close event - save data before closing."""
        self.save_user_data()
        self.root.destroy()


def main():
    """Main entry point."""
    root = tk.Tk()
    app = DPMVisualizerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

