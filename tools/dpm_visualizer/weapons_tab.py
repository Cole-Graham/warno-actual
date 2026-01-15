"""Weapons Tab for DPM Visualizer."""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import matplotlib
matplotlib.use('TkAgg')  # Use TkAgg backend for tkinter integration
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from .constants import RANGE_MODIFIERS_TABLE
from .calculations import (
    calculate_dpm,
    calculate_accuracy,
    calculate_shots_per_minute,
    extract_base_weapon_name,
)
from .ndf_parsers import (
    parse_ammunition_properties,
)
from .ui_components import SearchableCombobox, RangeModifierEditor


class WeaponsTab:
    """Weapons tab for DPM visualization."""
    
    def __init__(self, parent: ttk.Frame, app):
        """Initialize the Weapons tab.
        
        Args:
            parent: Parent frame (the tab frame)
            app: Main application instance (for shared data)
        """
        self.parent = parent
        self.app = app
        
        # Tab-specific state
        self.selected_weapons: List[str] = []  # List of selected weapon names
        self.weapon_dropdowns: List[SearchableCombobox] = []  # List of weapon dropdown widgets
        self.weapon_quantity_vars: List[tk.IntVar] = []  # Quantity for each weapon
        self.weapon_display_names: List[str] = []  # Cached weapon names list
        self.successive_hits: int = 0
        self.range_step: float = 25.0  # Fixed at 25m
        
        # Veterancy bonus controls per weapon
        self.weapon_bonus_combos: List[SearchableCombobox] = []  # List of bonus combo widgets
        self.weapon_visibility_vars: List[tk.BooleanVar] = []  # List of visibility checkboxes for each weapon
        self.weapon_use_vanilla_range_table_vars: List[tk.BooleanVar] = []  # List of checkboxes to use vanilla range table per weapon
        self.bonus_combinations: List[Tuple[float, float, str]] = []  # List of (acc_bonus, reload_mult, display_string)
        self.use_multiplicative_vet_bonus_var = tk.BooleanVar(value=True)  # Default to multiplicative
        # Track this separately from range modifier table setting - weapons tab has its own control
        
        # Chart state
        self.fig: Optional[Figure] = None
        self.ax = None
        self.canvas: Optional[FigureCanvasTkAgg] = None
        self.hover_cid = None
        self.click_cid = None
        self.selected_marker = None
        self.selected_range = None
        self.hover_marker = None
        self.line_data: Dict[str, List[Tuple[float, float]]] = {}  # Store line data for each weapon
        
        # Setup UI
        self.setup_ui()
        
        # Initialize after UI is set up
        self._initialize_data()
    
    def _initialize_data(self):
        """Initialize data after UI is set up."""
        # Update range table dropdown values
        if hasattr(self, 'range_table_combo'):
            self.range_table_combo['values'] = list(self.app.range_modifier_tables.keys())
            if self.app.current_range_modifier_table_name in self.app.range_modifier_tables:
                self.range_table_var.set(self.app.current_range_modifier_table_name)
        
        # Collect bonus combinations
        self.collect_bonus_combinations()
        
        # Update weapon dropdowns if data is already loaded
        self.weapon_display_names = []
        
        # Include regular ammunition if loaded
        if hasattr(self.app, 'ammunition_props') and self.app.ammunition_props:
            for ammo_name in sorted(self.app.ammunition_props.keys()):
                self.weapon_display_names.append(ammo_name)
        
        # Add custom weapons (always include these, even if ammunition_props isn't loaded yet)
        if hasattr(self.app, 'custom_weapons') and self.app.custom_weapons:
            for custom_name in sorted(self.app.custom_weapons.keys()):
                if custom_name not in self.weapon_display_names:
                    self.weapon_display_names.append(custom_name)
        
        # Update all existing dropdowns if we have any weapons
        if self.weapon_display_names:
            for dropdown in self.weapon_dropdowns:
                if isinstance(dropdown, SearchableCombobox):
                    dropdown.set_values(self.weapon_display_names)
        
        # Update bonus dropdowns
        bonus_strings = self.get_bonus_display_strings()
        for bonus_combo in self.weapon_bonus_combos:
            bonus_combo.set_values(bonus_strings)
        
        # Update load weapon combo with ALL weapons (including vehicle weapons)
        if hasattr(self, 'load_weapon_combo'):
            all_weapon_names = []
            # Include all ammunition props (not filtered by damage family)
            if hasattr(self.app, 'ammunition_props') and self.app.ammunition_props:
                for ammo_name in sorted(self.app.ammunition_props.keys()):
                    ammo_props = self.app.ammunition_props[ammo_name]
                    # Only require basic properties, not damage family
                    if ammo_props.get("idling") and ammo_props.get("max_range") and ammo_props.get("physical_damages"):
                        all_weapon_names.append(ammo_name)
            # Add custom weapons
            if hasattr(self.app, 'custom_weapons') and self.app.custom_weapons:
                for custom_name in sorted(self.app.custom_weapons.keys()):
                    if custom_name not in all_weapon_names:
                        all_weapon_names.append(custom_name)
            self.load_weapon_combo.set_values(all_weapon_names)
    
    def on_load_weapon_selected(self, event=None):
        """Populate custom weapon fields from selected existing weapon."""
        weapon_name = self.load_weapon_combo.get().strip()
        if not weapon_name:
            return
        
        # Get weapon properties (check custom weapons first, then regular)
        ammo_props = self.app.custom_weapons.get(weapon_name) or self.app.ammunition_props.get(weapon_name)
        if not ammo_props:
            return
        
        # Populate all fields
        self.custom_weapon_name_var.set(weapon_name)
        self.custom_weapon_max_range_var.set(str(ammo_props.get("max_range", 400)))
        self.custom_weapon_accuracy_var.set(str(ammo_props.get("idling", 0.5)))
        self.custom_weapon_damage_var.set(str(ammo_props.get("physical_damages", 10)))
        self.custom_weapon_suppress_damage_var.set(str(ammo_props.get("suppress_damages", 10)))
        self.custom_weapon_damage_family_var.set(ammo_props.get("damage_family", ""))
        self.custom_weapon_shots_per_salvo_var.set(str(ammo_props.get("shots_count_per_salvo", 1)))
        self.custom_weapon_time_between_salvos_var.set(str(ammo_props.get("time_between_salvos", 2.0)))
        
        time_between_shots = ammo_props.get("time_between_shots")
        if time_between_shots is not None:
            self.custom_weapon_time_between_shots_var.set(str(time_between_shots))
        else:
            self.custom_weapon_time_between_shots_var.set("")
        
        self.custom_weapon_aiming_time_var.set(str(ammo_props.get("aiming_time", 1.0)))
        self.custom_weapon_ammo_per_salvo_var.set(str(ammo_props.get("affichage_munition_par_salve", 1)))
        
        # Update preview after loading weapon
        if hasattr(self, 'update_preview'):
            self.update_preview()
    
    def update_preview(self):
        """Update the live preview of DPM, Shots/min, and Ammo/min based on current form values."""
        try:
            # Get values from form, with defaults if empty
            max_range_str = self.custom_weapon_max_range_var.get().strip()
            accuracy_str = self.custom_weapon_accuracy_var.get().strip()
            damage_str = self.custom_weapon_damage_var.get().strip()
            suppress_damage_str = self.custom_weapon_suppress_damage_var.get().strip()
            shots_per_salvo_str = self.custom_weapon_shots_per_salvo_var.get().strip()
            time_between_salvos_str = self.custom_weapon_time_between_salvos_var.get().strip()
            time_between_shots_str = self.custom_weapon_time_between_shots_var.get().strip()
            aiming_time_str = self.custom_weapon_aiming_time_var.get().strip()
            ammo_per_salvo_str = self.custom_weapon_ammo_per_salvo_var.get().strip()
            
            # Get damage type from dropdown
            damage_type = self.damage_type_var.get() if hasattr(self, 'damage_type_var') else "Physical"
            
            # Validate that required fields have values
            required_damage_str = suppress_damage_str if damage_type == "Suppression" else damage_str
            if not all([max_range_str, accuracy_str, required_damage_str, shots_per_salvo_str, time_between_salvos_str]):
                self.preview_dpm_label.config(text="DPM: --")
                self.preview_shots_label.config(text="Shots/min: --")
                self.preview_ammo_label.config(text="Ammo/min: --")
                return
            
            # Parse values
            max_range = float(max_range_str)
            accuracy = float(accuracy_str)
            if damage_type == "Suppression":
                damage = float(suppress_damage_str) if suppress_damage_str else 0.0
            else:
                damage = float(damage_str)
            shots_per_salvo = int(shots_per_salvo_str) if shots_per_salvo_str else 1
            time_between_salvos = float(time_between_salvos_str)
            time_between_shots = float(time_between_shots_str) if time_between_shots_str else None
            aiming_time = float(aiming_time_str) if aiming_time_str else 0.0
            ammo_per_salvo = float(ammo_per_salvo_str) if ammo_per_salvo_str else 1.0
            
            # Validate basic constraints
            if max_range <= 0 or accuracy < 0 or accuracy > 1 or damage <= 0 or shots_per_salvo <= 0 or time_between_salvos <= 0:
                self.preview_dpm_label.config(text="DPM: Invalid")
                self.preview_shots_label.config(text="Shots/min: Invalid")
                self.preview_ammo_label.config(text="Ammo/min: Invalid")
                return
            
            # Get bonus values from preview bonus dropdown
            bonus_display = self.preview_bonus_combo.get() if hasattr(self, 'preview_bonus_combo') else "No bonuses"
            veterancy_accuracy_bonus, reload_speed_multiplier = self.get_bonus_values_from_display(bonus_display)
            
            # Create temporary ammo_props dict for calculations
            ammo_props = {
                "max_range": max_range,
                "idling": accuracy,
                "physical_damages": float(damage_str) if damage_str else 0.0,
                "suppress_damages": float(suppress_damage_str) if suppress_damage_str else 0.0,
                "shots_count_per_salvo": shots_per_salvo,
                "time_between_salvos": time_between_salvos,
                "time_between_shots": time_between_shots,
                "aiming_time": aiming_time,
                "affichage_munition_par_salve": ammo_per_salvo,
            }
            
            # Use appropriate damage value based on damage type
            if damage_type == "Suppression":
                effective_damage = ammo_props.get("suppress_damages", 0.0)
            else:
                effective_damage = ammo_props.get("physical_damages", 0.0)
            
            # Calculate shots per minute with reload multiplier
            shots_per_minute = calculate_shots_per_minute(ammo_props, reload_speed_multiplier=reload_speed_multiplier, shot_time_multiplier=1.0)
            
            # Calculate ammo per minute
            ammo_per_minute = shots_per_minute * (ammo_per_salvo / shots_per_salvo) if shots_per_salvo > 0 else 0.0
            
            # Calculate DPM at max range for preview
            # Use the current range modifier table from the app
            range_modifiers_table = self.get_current_range_modifier_table() if hasattr(self, 'get_current_range_modifier_table') else RANGE_MODIFIERS_TABLE
            use_multiplicative_vet_bonus = self.app.range_modifier_vet_bonus_type.get(
                self.app.current_range_modifier_table_name, True
            )
            
            # Calculate accuracy at max range
            preview_accuracy = calculate_accuracy(
                max_range,  # Range at max range
                max_range,
                accuracy,
                successive_hits=0,  # No successive hits for preview
                veterancy_level=0,  # No veterancy for preview
                veterancy_accuracy_bonus=veterancy_accuracy_bonus,
                range_modifiers_table=range_modifiers_table,
                use_multiplicative_vet_bonus=use_multiplicative_vet_bonus,
            )
            
            # Calculate DPM (assuming 1 weapon for preview)
            dpm = preview_accuracy * effective_damage * shots_per_minute * 1
            
            # Update labels with formatted values
            self.preview_dpm_label.config(text=f"DPM: {dpm:.2f}")
            self.preview_shots_label.config(text=f"Shots/min: {shots_per_minute:.1f}")
            self.preview_ammo_label.config(text=f"Ammo/min: {ammo_per_minute:.1f}")
            
        except (ValueError, ZeroDivisionError):
            # Invalid input, show dashes
            self.preview_dpm_label.config(text="DPM: --")
            self.preview_shots_label.config(text="Shots/min: --")
            self.preview_ammo_label.config(text="Ammo/min: --")
        except Exception:
            # Any other error, show dashes
            self.preview_dpm_label.config(text="DPM: --")
            self.preview_shots_label.config(text="Shots/min: --")
            self.preview_ammo_label.config(text="Ammo/min: --")
    
    def create_custom_weapon(self):
        """Create a custom weapon from user input."""
        weapon_name = self.custom_weapon_name_var.get().strip()
        if not weapon_name:
            messagebox.showwarning("Warning", "Please enter a weapon name")
            return
        
        try:
            # Parse all values
            max_range = float(self.custom_weapon_max_range_var.get())
            accuracy = float(self.custom_weapon_accuracy_var.get())
            damage = float(self.custom_weapon_damage_var.get())
            suppress_damage_str = self.custom_weapon_suppress_damage_var.get().strip()
            suppress_damage = float(suppress_damage_str) if suppress_damage_str else 0.0
            damage_family = self.custom_weapon_damage_family_var.get().strip()
            shots_per_salvo = int(self.custom_weapon_shots_per_salvo_var.get())
            time_between_salvos = float(self.custom_weapon_time_between_salvos_var.get())
            time_between_shots_str = self.custom_weapon_time_between_shots_var.get().strip()
            time_between_shots = float(time_between_shots_str) if time_between_shots_str else None
            aiming_time = float(self.custom_weapon_aiming_time_var.get())
            ammo_per_salvo = float(self.custom_weapon_ammo_per_salvo_var.get())
            
            # Validate values
            if max_range <= 0 or accuracy < 0 or accuracy > 1 or damage <= 0:
                messagebox.showerror("Error", "Invalid weapon properties. Please check your values.")
                return
            
            # Create custom weapon properties
            custom_weapon_props = {
                "max_range": max_range,
                "idling": accuracy,
                "physical_damages": damage,
                "suppress_damages": suppress_damage,
                "damage_family": damage_family if damage_family else None,
                "shots_count_per_salvo": shots_per_salvo,
                "time_between_salvos": time_between_salvos,
                "time_between_shots": time_between_shots,
                "aiming_time": aiming_time,
                "affichage_munition_par_salve": ammo_per_salvo,
            }
            
            # Store custom weapon
            self.app.custom_weapons[weapon_name] = custom_weapon_props
            
            # Save user data
            self.app.save_user_data()
            
            # Update dropdowns
            self._initialize_data()
            
            # Update infantry tab dropdowns if it exists
            if hasattr(self.app, 'infantry_tab') and hasattr(self.app.infantry_tab, 'update_custom_weapon_dropdowns'):
                self.app.infantry_tab.update_custom_weapon_dropdowns()
            
            messagebox.showinfo("Success", f"Custom weapon '{weapon_name}' created successfully!")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}. Please check all fields are valid numbers.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create custom weapon: {e}")
    
    def edit_custom_weapon(self):
        """Edit an existing custom weapon."""
        if not self.app.custom_weapons:
            messagebox.showwarning("Warning", "No custom weapons found to edit.")
            return
        
        # Show selection dialog
        dialog = tk.Toplevel(self.app.root)
        dialog.title("Edit Custom Weapon")
        dialog.geometry("300x150")
        dialog.transient(self.app.root)
        dialog.grab_set()
        
        ttk.Label(dialog, text="Select weapon to edit:").pack(pady=10)
        weapon_var = tk.StringVar()
        weapon_combo = ttk.Combobox(dialog, textvariable=weapon_var, values=list(self.app.custom_weapons.keys()), width=30, state="readonly")
        weapon_combo.pack(pady=5)
        if self.app.custom_weapons:
            weapon_combo.current(0)
        
        def load_for_edit():
            weapon_name = weapon_var.get()
            if weapon_name:
                self.on_load_weapon_selected_for_edit(weapon_name)
                dialog.destroy()
        
        ttk.Button(dialog, text="Edit", command=load_for_edit).pack(pady=5)
    
    def on_load_weapon_selected_for_edit(self, weapon_name: str):
        """Load weapon data into form for editing."""
        weapon_props = self.app.custom_weapons.get(weapon_name, {})
        if not weapon_props:
            return
        
        # Store original name for update
        self.editing_weapon_name = weapon_name
        
        # Populate form fields
        self.custom_weapon_name_var.set(weapon_name)
        self.custom_weapon_max_range_var.set(str(weapon_props.get("max_range", 0)))
        self.custom_weapon_accuracy_var.set(str(weapon_props.get("idling", 0)))
        self.custom_weapon_damage_var.set(str(weapon_props.get("physical_damages", 0)))
        self.custom_weapon_suppress_damage_var.set(str(weapon_props.get("suppress_damages", 0)))
        self.custom_weapon_damage_family_var.set(weapon_props.get("damage_family", ""))
        self.custom_weapon_shots_per_salvo_var.set(str(weapon_props.get("shots_count_per_salvo", 1)))
        self.custom_weapon_time_between_salvos_var.set(str(weapon_props.get("time_between_salvos", 1.0)))
        time_between_shots = weapon_props.get("time_between_shots")
        self.custom_weapon_time_between_shots_var.set(str(time_between_shots) if time_between_shots is not None else "")
        self.custom_weapon_aiming_time_var.set(str(weapon_props.get("aiming_time", 0)))
        self.custom_weapon_ammo_per_salvo_var.set(str(weapon_props.get("affichage_munition_par_salve", 1.0)))
        
        # Update preview after loading weapon for editing
        if hasattr(self, 'update_preview'):
            self.update_preview()
        
        # Update button text to show we're editing
        if hasattr(self, 'weapon_button_frame'):
            for widget in self.weapon_button_frame.winfo_children():
                if isinstance(widget, ttk.Button) and widget.cget("text") == "Create Custom Weapon":
                    widget.config(text="Update Custom Weapon", command=self.update_custom_weapon)
                    break
    
    def update_custom_weapon(self):
        """Update an existing custom weapon."""
        if not hasattr(self, 'editing_weapon_name'):
            messagebox.showwarning("Warning", "No weapon selected for editing.")
            return
        
        original_name = self.editing_weapon_name
        new_name = self.custom_weapon_name_var.get().strip()
        
        if not new_name:
            messagebox.showwarning("Warning", "Please enter a weapon name")
            return
        
        # If name changed and new name exists, ask for confirmation
        if new_name != original_name and new_name in self.app.custom_weapons:
            response = messagebox.askyesno("Confirm", f"Weapon '{new_name}' already exists. Replace it?")
            if not response:
                return
        
        # Remove old weapon if name changed
        if new_name != original_name and original_name in self.app.custom_weapons:
            del self.app.custom_weapons[original_name]
        
        # Create/update the weapon (reuse create logic)
        self.create_custom_weapon()
        
        # Reset button text
        if hasattr(self, 'weapon_button_frame'):
            for widget in self.weapon_button_frame.winfo_children():
                if isinstance(widget, ttk.Button) and widget.cget("text") == "Update Custom Weapon":
                    widget.config(text="Create Custom Weapon", command=self.create_custom_weapon)
                    break
        
        # Clear editing flag
        if hasattr(self, 'editing_weapon_name'):
            delattr(self, 'editing_weapon_name')
    
    def setup_ui(self):
        """Set up the Weapons tab UI."""
        # Main content area - vertical layout
        main_container = ttk.Frame(self.parent)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Top section - Left panel and Right panel (chart)
        top_section = ttk.Frame(main_container)
        top_section.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Left panel - Controls
        left_panel = ttk.Frame(top_section, width=375)  # Increased by 25% from 300
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left_panel.pack_propagate(False)
        
        # Weapon selection section
        weapon_section = ttk.LabelFrame(left_panel, text="Weapons to Compare", padding="5")
        weapon_section.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Scrollable frame for weapon dropdowns
        weapon_canvas_frame = ttk.Frame(weapon_section)
        weapon_canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        weapon_canvas = tk.Canvas(weapon_canvas_frame)
        weapon_scrollbar = ttk.Scrollbar(weapon_canvas_frame, orient="vertical", command=weapon_canvas.yview)
        weapon_scrollable_frame = ttk.Frame(weapon_canvas)
        
        def update_scrollregion(event):
            weapon_canvas.configure(scrollregion=weapon_canvas.bbox("all"))
        
        weapon_scrollable_frame.bind("<Configure>", update_scrollregion)
        
        weapon_canvas.create_window((0, 0), window=weapon_scrollable_frame, anchor="nw")
        weapon_canvas.configure(yscrollcommand=weapon_scrollbar.set)
        
        # Make canvas scrollable with mouse wheel
        def on_mousewheel(event):
            weapon_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        
        weapon_canvas.bind("<MouseWheel>", on_mousewheel)
        
        weapon_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        weapon_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.weapon_dropdowns_frame = weapon_scrollable_frame
        self.weapon_canvas = weapon_canvas  # Store reference to canvas
        
        # Add initial weapon dropdown
        self.add_weapon_dropdown()
        
        # Buttons for adding/removing weapons
        button_frame = ttk.Frame(weapon_section)
        button_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Button(button_frame, text="Add Weapon", command=self.add_weapon_dropdown).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Remove Last", command=self.remove_last_weapon_dropdown).pack(side=tk.LEFT, padx=2)
        
        # Configuration section
        config_section = ttk.LabelFrame(left_panel, text="Configuration", padding="5")
        config_section.pack(fill=tk.X, pady=(0, 10))
        
        # Successive hits
        hits_frame = ttk.Frame(config_section)
        hits_frame.pack(fill=tk.X, pady=2)
        ttk.Label(hits_frame, text="Successive Hits:").pack(side=tk.LEFT, padx=(0, 5))
        self.successive_hits_var = tk.IntVar(value=0)
        hits_spinbox = ttk.Spinbox(hits_frame, from_=0, to=5, textvariable=self.successive_hits_var, width=5)
        hits_spinbox.pack(side=tk.LEFT)
        hits_spinbox.bind('<ButtonRelease-1>', lambda e: [self.update_graph(), self.app.auto_save_state()])
        hits_spinbox.bind('<KeyRelease>', lambda e: [self.update_graph(), self.app.auto_save_state()])
        
        # Range modifier table selection
        range_frame = ttk.Frame(config_section)
        range_frame.pack(fill=tk.X, pady=2)
        ttk.Label(range_frame, text="Range Table:").pack(side=tk.LEFT, padx=(0, 5))
        self.range_table_var = tk.StringVar(value=self.app.current_range_modifier_table_name)
        self.range_table_combo = ttk.Combobox(range_frame, textvariable=self.range_table_var, state="readonly", width=20)
        self.range_table_combo.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.range_table_combo['values'] = list(self.app.range_modifier_tables.keys())
        self.range_table_combo.bind("<<ComboboxSelected>>", self.on_range_table_selected)
        
        ttk.Button(range_frame, text="Edit", command=self.open_range_modifier_editor).pack(side=tk.LEFT)
        
        # Veterancy bonus mode checkbox
        vet_mode_frame = ttk.Frame(config_section)
        vet_mode_frame.pack(fill=tk.X, pady=2)
        vet_mode_checkbox = ttk.Checkbutton(
            vet_mode_frame,
            text="Use multiplicative veterancy accuracy bonus (unchecked = flat bonus)",
            variable=self.use_multiplicative_vet_bonus_var,
            command=lambda: [self.update_graph(), self.app.auto_save_state()]
        )
        vet_mode_checkbox.pack(side=tk.LEFT)
        
        # Damage type dropdown
        damage_type_frame = ttk.Frame(config_section)
        damage_type_frame.pack(fill=tk.X, pady=2)
        ttk.Label(damage_type_frame, text="DPM:").pack(side=tk.LEFT, padx=(0, 5))
        self.damage_type_var = tk.StringVar(value="Physical")
        damage_type_combo = ttk.Combobox(
            damage_type_frame,
            textvariable=self.damage_type_var,
            values=["Physical", "Suppression"],
            state="readonly",
            width=12,
        )
        damage_type_combo.pack(side=tk.LEFT, padx=(0, 2))
        damage_type_combo.bind("<<ComboboxSelected>>", lambda e: [self.update_graph(), self.app.auto_save_state()])
        
        # Generate chart button
        ttk.Button(config_section, text="Generate Chart", command=self.generate_chart).pack(fill=tk.X, pady=(5, 0))
        
        # Right panel - Chart and Info
        right_panel = ttk.Frame(top_section)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Chart frame
        chart_frame = ttk.LabelFrame(right_panel, text="DPM vs Range", padding="5")
        chart_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.fig = Figure(figsize=(10, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel("Range (m)")
        self.ax.set_ylabel("DPM (Damage Per Minute)")
        self.ax.grid(True, alpha=0.3)
        self.ax.set_title("Weapon DPM Comparison")
        
        self.canvas = FigureCanvasTkAgg(self.fig, chart_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Bottom section - Info panel and Custom Weapon side by side
        bottom_section = ttk.Frame(right_panel)
        bottom_section.pack(fill=tk.BOTH, expand=True)
        
        # Info panel (smaller, left side)
        text_frame = ttk.LabelFrame(bottom_section, text="Data Point Info", padding="5")
        text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.info_text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            width=20,
            height=12,
            font=('Consolas', 9),
            state=tk.DISABLED,
            bg='#f0f0f0',
            relief=tk.FLAT,
            yscrollcommand=scrollbar.set
        )
        self.info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.info_text.yview)
        
        # Initial message
        self.info_text.config(state=tk.NORMAL)
        self.info_text.insert('1.0', 'Select weapons and generate\na chart to see DPM comparison.\n\nHover over data points\nto see details.\n\nClick on a data point\nto select it and see\nall weapons at that range.')
        self.info_text.config(state=tk.DISABLED)
        
        # Custom Weapon Section (right side of bottom section)
        custom_weapon_section = ttk.LabelFrame(bottom_section, text="Create Custom Weapon", padding="5")
        custom_weapon_section.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Load from existing weapon dropdown (all weapons, not just small arms)
        ttk.Label(custom_weapon_section, text="Load from existing weapon:").pack(anchor=tk.W)
        self.load_weapon_combo = SearchableCombobox(custom_weapon_section, width=25)
        self.load_weapon_combo.pack(fill=tk.X, pady=(0, 5))
        self.load_weapon_combo.bind("<<ComboboxSelected>>", self.on_load_weapon_selected)
        
        # Custom weapon name
        ttk.Label(custom_weapon_section, text="Weapon Name:").pack(anchor=tk.W)
        self.custom_weapon_name_var = tk.StringVar()
        ttk.Entry(custom_weapon_section, textvariable=self.custom_weapon_name_var, width=25).pack(fill=tk.X, pady=(0, 5))
        
        # Weapon properties grid
        props_frame = ttk.Frame(custom_weapon_section)
        props_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Row 1: Max Range, Base Accuracy (Idling)
        row1 = ttk.Frame(props_frame)
        row1.pack(fill=tk.X, pady=2)
        
        ttk.Label(row1, text="Max Range (m):", width=15).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_max_range_var = tk.StringVar(value="400")
        ttk.Entry(row1, textvariable=self.custom_weapon_max_range_var, width=10).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Label(row1, text="Base Accuracy:", width=15).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_accuracy_var = tk.StringVar(value="0.5")
        ttk.Entry(row1, textvariable=self.custom_weapon_accuracy_var, width=10).pack(side=tk.LEFT)
        
        # Row 2: Physical Damage, Suppression Damage
        row2 = ttk.Frame(props_frame)
        row2.pack(fill=tk.X, pady=2)
        
        ttk.Label(row2, text="Physical Damage:", width=15).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_damage_var = tk.StringVar(value="10")
        ttk.Entry(row2, textvariable=self.custom_weapon_damage_var, width=10).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Label(row2, text="Suppression Damage:", width=18).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_suppress_damage_var = tk.StringVar(value="10")
        ttk.Entry(row2, textvariable=self.custom_weapon_suppress_damage_var, width=10).pack(side=tk.LEFT)
        
        # Row 2b: Damage Family (optional, can be empty for vehicle weapons)
        row2b = ttk.Frame(props_frame)
        row2b.pack(fill=tk.X, pady=2)
        
        ttk.Label(row2b, text="Damage Family:", width=15).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_damage_family_var = tk.StringVar(value="")
        damage_family_entry = ttk.Entry(row2b, textvariable=self.custom_weapon_damage_family_var, width=25)
        damage_family_entry.pack(side=tk.LEFT)
        
        # Row 3: Shots per salvo, Time between salvos, Time between shots
        row3 = ttk.Frame(props_frame)
        row3.pack(fill=tk.X, pady=2)
        
        ttk.Label(row3, text="Shots/Salvo:", width=15).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_shots_per_salvo_var = tk.StringVar(value="1")
        ttk.Entry(row3, textvariable=self.custom_weapon_shots_per_salvo_var, width=10).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Label(row3, text="Time Between Salvos (s):", width=20).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_time_between_salvos_var = tk.StringVar(value="2.0")
        ttk.Entry(row3, textvariable=self.custom_weapon_time_between_salvos_var, width=10).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Label(row3, text="Time Between Shots (s):", width=20).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_time_between_shots_var = tk.StringVar(value="")
        ttk.Entry(row3, textvariable=self.custom_weapon_time_between_shots_var, width=10).pack(side=tk.LEFT)
        
        # Row 4: Aiming time, Ammo per salvo
        row4 = ttk.Frame(props_frame)
        row4.pack(fill=tk.X, pady=2)
        
        ttk.Label(row4, text="Aiming Time (s):", width=15).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_aiming_time_var = tk.StringVar(value="1.0")
        ttk.Entry(row4, textvariable=self.custom_weapon_aiming_time_var, width=10).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Label(row4, text="Ammo Per Salvo:", width=15).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_ammo_per_salvo_var = tk.StringVar(value="1")
        ttk.Entry(row4, textvariable=self.custom_weapon_ammo_per_salvo_var, width=10).pack(side=tk.LEFT)
        
        # Create/Edit custom weapon buttons
        self.weapon_button_frame = ttk.Frame(custom_weapon_section)
        self.weapon_button_frame.pack(fill=tk.X, pady=(5, 0))
        ttk.Button(self.weapon_button_frame, text="Create Custom Weapon", command=self.create_custom_weapon).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 2))
        ttk.Button(self.weapon_button_frame, text="Edit Custom Weapon", command=self.edit_custom_weapon).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(2, 0))
        
        # Live preview section
        preview_frame = ttk.Frame(custom_weapon_section)
        preview_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Label(preview_frame, text="Live Preview:", font=("TkDefaultFont", 9, "bold")).pack(anchor=tk.W, pady=(0, 2))
        
        # Bonus selector for preview
        bonus_preview_row = ttk.Frame(preview_frame)
        bonus_preview_row.pack(fill=tk.X, pady=(0, 5))
        ttk.Label(bonus_preview_row, text="Bonuses:").pack(side=tk.LEFT, padx=(0, 5))
        self.preview_bonus_combo = SearchableCombobox(bonus_preview_row, width=30)
        self.preview_bonus_combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
        # Ensure bonus combinations are collected before setting values
        if not hasattr(self, 'bonus_combinations') or not self.bonus_combinations:
            self.collect_bonus_combinations()
        self.preview_bonus_combo.set_values(self.get_bonus_display_strings())
        self.preview_bonus_combo.set("No bonuses")  # Set default value
        self.preview_bonus_combo.bind("<<ComboboxSelected>>", lambda e: self.update_preview())
        
        preview_info_frame = ttk.Frame(preview_frame)
        preview_info_frame.pack(fill=tk.X)
        
        self.preview_dpm_label = ttk.Label(preview_info_frame, text="DPM: --", foreground="blue")
        self.preview_dpm_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.preview_shots_label = ttk.Label(preview_info_frame, text="Shots/min: --", foreground="green")
        self.preview_shots_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.preview_ammo_label = ttk.Label(preview_info_frame, text="Ammo/min: --", foreground="orange")
        self.preview_ammo_label.pack(side=tk.LEFT)
        
        # Bind update_preview to all custom weapon input fields
        self.custom_weapon_max_range_var.trace_add("write", lambda *args: self.app.root.after_idle(self.update_preview))
        self.custom_weapon_accuracy_var.trace_add("write", lambda *args: self.app.root.after_idle(self.update_preview))
        self.custom_weapon_damage_var.trace_add("write", lambda *args: self.app.root.after_idle(self.update_preview))
        self.custom_weapon_suppress_damage_var.trace_add("write", lambda *args: self.app.root.after_idle(self.update_preview))
        self.custom_weapon_shots_per_salvo_var.trace_add("write", lambda *args: self.app.root.after_idle(self.update_preview))
        self.custom_weapon_time_between_salvos_var.trace_add("write", lambda *args: self.app.root.after_idle(self.update_preview))
        self.custom_weapon_time_between_shots_var.trace_add("write", lambda *args: self.app.root.after_idle(self.update_preview))
        self.custom_weapon_aiming_time_var.trace_add("write", lambda *args: self.app.root.after_idle(self.update_preview))
        self.custom_weapon_ammo_per_salvo_var.trace_add("write", lambda *args: self.app.root.after_idle(self.update_preview))
        
        # Bind mouse motion for tooltips
        self.connect_hover_handler()
    
    def connect_hover_handler(self):
        """Connect or reconnect the hover and click event handlers."""
        # Disconnect old handlers if they exist
        if self.hover_cid is not None:
            self.canvas.mpl_disconnect(self.hover_cid)
        if self.click_cid is not None:
            self.canvas.mpl_disconnect(self.click_cid)
        
        # Connect new handlers
        self.hover_cid = self.canvas.mpl_connect("motion_notify_event", self.on_hover)
        self.click_cid = self.canvas.mpl_connect("button_press_event", self.on_click)
    
    def add_weapon_dropdown(self):
        """Add a new weapon selection dropdown."""
        weapon_frame = ttk.Frame(self.weapon_dropdowns_frame)
        weapon_frame.pack(fill=tk.X, pady=(5, 2))
        
        # Separator line (except for first weapon)
        if len(self.weapon_dropdowns) > 0:
            separator = ttk.Separator(weapon_frame, orient='horizontal')
            separator.pack(fill=tk.X, pady=(0, 5))
        
        # Weapon dropdown row with visibility checkbox
        weapon_row = ttk.Frame(weapon_frame)
        weapon_row.pack(fill=tk.X, pady=(0, 2))
        # Visibility checkbox
        visibility_var = tk.BooleanVar(value=True)  # Default to visible
        self.weapon_visibility_vars.append(visibility_var)
        visibility_checkbox = ttk.Checkbutton(
            weapon_row,
            variable=visibility_var,
            command=lambda: [self.update_graph(), self.app.auto_save_state()]
        )
        visibility_checkbox.pack(side=tk.LEFT, padx=(0, 5))
        ttk.Label(weapon_row, text="Weapon:").pack(side=tk.LEFT, padx=(0, 5))
        weapon_combo = SearchableCombobox(weapon_row, width=30)
        weapon_combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
        weapon_combo.set_values(self.weapon_display_names)
        weapon_combo.bind("<<ComboboxSelected>>", lambda e: self.on_weapon_selected(weapon_combo))
        self.weapon_dropdowns.append(weapon_combo)
        
        # Quantity selector row
        quantity_row = ttk.Frame(weapon_frame)
        quantity_row.pack(fill=tk.X, pady=(0, 2))
        ttk.Label(quantity_row, text="Qty:").pack(side=tk.LEFT, padx=(0, 5))
        quantity_var = tk.IntVar(value=1)
        self.weapon_quantity_vars.append(quantity_var)
        quantity_spinbox = ttk.Spinbox(quantity_row, from_=1, to=10, textvariable=quantity_var, width=5)
        quantity_spinbox.pack(side=tk.LEFT, padx=(0, 5))
        quantity_spinbox.bind('<ButtonRelease-1>', lambda e: [self.update_graph(), self.app.auto_save_state()])
        quantity_spinbox.bind('<KeyRelease>', lambda e: [self.update_graph(), self.app.auto_save_state()])
        # Vanilla range table checkbox
        use_vanilla_var = tk.BooleanVar(value=False)  # Default to using selected range table
        self.weapon_use_vanilla_range_table_vars.append(use_vanilla_var)
        vanilla_checkbox = ttk.Checkbutton(
            quantity_row,
            text="Use vanilla range table",
            variable=use_vanilla_var,
            command=self.update_graph
        )
        vanilla_checkbox.pack(side=tk.LEFT, padx=(0, 5))
        
        # Veterancy bonus dropdown row
        bonus_row = ttk.Frame(weapon_frame)
        bonus_row.pack(fill=tk.X)
        ttk.Label(bonus_row, text="Bonuses:").pack(side=tk.LEFT, padx=(0, 5))
        bonus_combo = SearchableCombobox(bonus_row, width=30)
        bonus_combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
        # Ensure bonus combinations are collected before setting values
        if not self.bonus_combinations:
            self.collect_bonus_combinations()
        bonus_combo.set_values(self.get_bonus_display_strings())
        bonus_combo.set("No bonuses")  # Set default value
        bonus_combo.bind("<<ComboboxSelected>>", lambda e: [self.update_graph(), self.app.auto_save_state()])
        self.weapon_bonus_combos.append(bonus_combo)
        
        # Update scroll region
        self.weapon_dropdowns_frame.update_idletasks()
        self.weapon_canvas.configure(scrollregion=self.weapon_canvas.bbox("all"))
    
    def remove_last_weapon_dropdown(self):
        """Remove the last weapon dropdown."""
        if len(self.weapon_dropdowns) > 1:
            # Remove widgets
            last_dropdown = self.weapon_dropdowns.pop()
            last_quantity = self.weapon_quantity_vars.pop()
            if self.weapon_bonus_combos:
                self.weapon_bonus_combos.pop()
            if self.weapon_visibility_vars:
                self.weapon_visibility_vars.pop()
            if self.weapon_use_vanilla_range_table_vars:
                self.weapon_use_vanilla_range_table_vars.pop()
            # Destroy the entire weapon_frame (which contains weapon_row, quantity_row, bonus_row, and separator)
            # last_dropdown.master is weapon_row, last_dropdown.master.master is weapon_frame
            weapon_frame = last_dropdown.master.master
            weapon_frame.destroy()
            
            # Update scroll region
            self.weapon_dropdowns_frame.update_idletasks()
            self.weapon_canvas.configure(scrollregion=self.weapon_canvas.bbox("all"))
            
            # Update graph if needed
            self.update_graph()
    
    def on_weapon_selected(self, combo: SearchableCombobox):
        """Handle weapon selection."""
        ammo_name = combo.get()
        if ammo_name and (ammo_name in self.app.ammunition_props or 
                         (hasattr(self.app, 'custom_weapons') and ammo_name in self.app.custom_weapons)):
            self.update_graph()
    
    def collect_bonus_combinations(self):
        """Collect all unique veterancy bonus combinations from existing units."""
        bonus_set = set()
        
        # Add default "No bonuses" option
        bonus_set.add((0.0, 1.0, "No bonuses"))
        
        # Collect from all units
        if hasattr(self.app, 'infantry_units'):
            for unit_name, unit_info in self.app.infantry_units.items():
                acc_bonuses = unit_info.get("veterancy_accuracy_bonuses", {})
                reload_multipliers = unit_info.get("veterancy_reload_speed_multipliers", {})
                
                # Collect all unique combinations
                all_levels = set(acc_bonuses.keys()) | set(reload_multipliers.keys())
                for level in all_levels:
                    acc_bonus = acc_bonuses.get(level, 0.0)
                    reload_mult = reload_multipliers.get(level, 1.0)
                    
                    # Format as string for display
                    acc_percent = acc_bonus * 100.0
                    if acc_bonus == 0.0 and reload_mult == 1.0:
                        display = "No bonuses"
                    elif acc_bonus == 0.0:
                        display = f"Reload: {reload_mult:.2f}x"
                    elif reload_mult == 1.0:
                        display = f"Acc: +{acc_percent:.1f}%"
                    else:
                        display = f"Acc: +{acc_percent:.1f}%, Reload: {reload_mult:.2f}x"
                    
                    bonus_set.add((acc_bonus, reload_mult, display))
        
        # Convert to sorted list (by accuracy bonus, then reload multiplier)
        self.bonus_combinations = sorted(bonus_set, key=lambda x: (x[0], x[1]))
    
    def get_bonus_display_strings(self) -> List[str]:
        """Get list of bonus display strings."""
        return [combo[2] for combo in self.bonus_combinations]
    
    def get_bonus_values_from_display(self, display_string: str) -> Tuple[float, float]:
        """Get accuracy bonus and reload multiplier from display string."""
        # Find matching combination
        for combo in self.bonus_combinations:
            if combo[2] == display_string:
                return combo[0], combo[1]  # acc_bonus, reload_mult
        # Default to no bonuses
        return 0.0, 1.0
    
    def on_range_table_selected(self, event=None):
        """Handle range modifier table selection."""
        selected_table = self.range_table_var.get()
        if selected_table in self.app.range_modifier_tables:
            self.app.current_range_modifier_table_name = selected_table
            self.update_graph()
            self.app.auto_save_state()
    
    def open_range_modifier_editor(self):
        """Open the range modifier table editor window."""
        editor = RangeModifierEditor(self.app.root, self.app)
        self.app.root.wait_window(editor.window)
        # After editor closes, update range table dropdown and regenerate chart if needed
        self.range_table_combo['values'] = list(self.app.range_modifier_tables.keys())
        if self.app.current_range_modifier_table_name in self.app.range_modifier_tables:
            self.range_table_var.set(self.app.current_range_modifier_table_name)
        if hasattr(self, 'ax') and self.ax.lines:
            self.generate_chart()
    
    def get_current_range_modifier_table(self) -> List[Tuple[float, float]]:
        """Get the currently selected range modifier table."""
        table_name = self.app.current_range_modifier_table_name
        return self.app.range_modifier_tables.get(table_name, RANGE_MODIFIERS_TABLE)
    
    def generate_chart(self):
        """Generate the DPM chart for selected weapons."""
        # Store the currently selected range before clearing (to restore it after regeneration)
        saved_selected_range = self.selected_range if self.selected_range is not None else None
        
        # Clear previous chart and selection
        self.ax.clear()
        self.selected_range = None
        self.line_data = {}  # Clear line data
        if self.selected_marker is not None:
            try:
                self.selected_marker.remove()
            except:
                pass
            self.selected_marker = None
        self.ax.set_xlabel("Range (m)")
        self.ax.set_ylabel("DPM (Damage Per Minute)")
        self.ax.grid(True, alpha=0.3)
        
        # Get current range modifier table
        range_modifiers_table = self.get_current_range_modifier_table()
        table_name = self.app.current_range_modifier_table_name
        
        # Update title with range modifier table name
        self.ax.set_title(f"Weapon DPM Comparison (Range Modifier: {table_name})")
        
        # Get successive hits
        self.successive_hits = self.successive_hits_var.get()
        
        # Collect selected weapons (ammunition) with quantities and bonuses
        selected_weapons_data = []
        for i, dropdown in enumerate(self.weapon_dropdowns):
            ammo_name = dropdown.get()
            if ammo_name:
                # Check visibility checkbox
                is_visible = self.weapon_visibility_vars[i].get() if i < len(self.weapon_visibility_vars) else True
                if not is_visible:
                    continue  # Skip this weapon if it's not visible
                
                # Check if it's in ammunition_props or custom_weapons
                quantity = self.weapon_quantity_vars[i].get() if i < len(self.weapon_quantity_vars) else 1
                # Get bonus values for this weapon - read directly from combo widget
                bonus_combo = self.weapon_bonus_combos[i] if i < len(self.weapon_bonus_combos) else None
                bonus_display = bonus_combo.get() if bonus_combo else "No bonuses"
                veterancy_accuracy_bonus, reload_speed_multiplier = self.get_bonus_values_from_display(bonus_display)
                # Check if this weapon should use vanilla range table
                use_vanilla_range_table = self.weapon_use_vanilla_range_table_vars[i].get() if i < len(self.weapon_use_vanilla_range_table_vars) else False
                
                if ammo_name in self.app.ammunition_props:
                    selected_weapons_data.append((ammo_name, quantity, False, veterancy_accuracy_bonus, reload_speed_multiplier, use_vanilla_range_table, i))  # False = not custom, i = dropdown index
                elif hasattr(self.app, 'custom_weapons') and ammo_name in self.app.custom_weapons:
                    selected_weapons_data.append((ammo_name, quantity, True, veterancy_accuracy_bonus, reload_speed_multiplier, use_vanilla_range_table, i))  # True = custom, i = dropdown index
        
        if not selected_weapons_data:
            self.ax.text(0.5, 0.5, 'Select weapons to compare', 
                        horizontalalignment='center', verticalalignment='center',
                        transform=self.ax.transAxes, fontsize=14)
            self.ax.set_ylim(bottom=0)
            self.canvas.draw()
            return
        
        # Generate DPM data for each weapon
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
        max_chart_range = 0
        
        for ammo_name, quantity, is_custom, veterancy_accuracy_bonus, reload_speed_multiplier, use_vanilla_range_table, dropdown_idx in selected_weapons_data:
            # Get ammunition properties
            if is_custom:
                ammo_props = self.app.custom_weapons[ammo_name].copy()
            else:
                ammo_props = self.app.ammunition_props[ammo_name].copy()
            
            # Set weapon quantity
            ammo_props["weapon_quantity"] = quantity
            
            # Determine which range table to use for this weapon
            weapon_range_table = RANGE_MODIFIERS_TABLE if use_vanilla_range_table else range_modifiers_table
            
            # Calculate DPM with selected bonuses
            # Read checkbox value fresh each time
            use_multiplicative = self.use_multiplicative_vet_bonus_var.get()
            damage_type = self.damage_type_var.get() if hasattr(self, 'damage_type_var') else "Physical"
            dpm_data = calculate_dpm(
                ammo_props,
                quantity,
                self.successive_hits,
                self.range_step,
                veterancy_level=0,  # Not used when bonuses are provided directly
                veterancy_accuracy_bonus=veterancy_accuracy_bonus,
                reload_speed_multiplier=reload_speed_multiplier,
                range_modifiers_table=weapon_range_table,
                use_multiplicative_vet_bonus=use_multiplicative,
                damage_type=damage_type
            )
            
            if dpm_data:
                ranges = [point[0] for point in dpm_data]
                dpm_values = [point[1] for point in dpm_data]
                
                # Track maximum range for x-axis ticks
                max_chart_range = max(max_chart_range, max(ranges))
                
                # Use dropdown index to determine color (maintains color based on position in left panel)
                color = colors[dropdown_idx % len(colors)]
                # Build label with bonuses if applicable
                bonus_label = ""
                if veterancy_accuracy_bonus != 0.0 or reload_speed_multiplier != 1.0:
                    bonus_parts = []
                    if veterancy_accuracy_bonus != 0.0:
                        bonus_parts.append(f"+{veterancy_accuracy_bonus * 100:.0f}% acc")
                    if reload_speed_multiplier != 1.0:
                        bonus_parts.append(f"{reload_speed_multiplier:.2f}x reload")
                    bonus_label = f" [{', '.join(bonus_parts)}]"
                label = f"{ammo_name} (x{quantity}){bonus_label}"
                # Use dashed line style if using vanilla range table
                linestyle = '--' if use_vanilla_range_table else '-'
                self.ax.plot(ranges, dpm_values, label=label, color=color, linewidth=2, linestyle=linestyle)
                
                # Store line data for marker placement
                self.line_data[label] = list(zip(ranges, dpm_values))
        
        if self.ax.lines:
            self.ax.legend(loc='best')
            
            # Set x-axis ticks to 175m intervals
            if max_chart_range > 0:
                # Create ticks at 175m intervals up to max range
                x_ticks = list(range(0, int(max_chart_range) + 175, 175))
                self.ax.set_xticks(x_ticks)
                self.ax.set_xticklabels([str(x) for x in x_ticks])
            
            # Restore the selected range if it was set before and is still valid
            if saved_selected_range is not None:
                # Check if the saved range is within the chart's range
                if saved_selected_range <= max_chart_range and saved_selected_range >= 0:
                    # Restore the selection
                    self.selected_range = saved_selected_range
                    
                    # Draw marker at selected range for all weapons
                    marker_x = []
                    marker_y = []
                    for weapon_label, data_points in self.line_data.items():
                        dpm_at_range = self._get_dpm_at_range(data_points, saved_selected_range)
                        if dpm_at_range > 0:
                            marker_x.append(saved_selected_range)
                            marker_y.append(dpm_at_range)
                    
                    if marker_x:
                        self.selected_marker = self.ax.scatter(marker_x, marker_y, s=100, c='red', marker='X', zorder=10, label='Selected Range')
                    
                    # Update info panel with all weapons at this range
                    self.show_weapons_at_range(saved_selected_range)
        
        self.ax.set_ylim(bottom=0)
        self.canvas.draw()
        
        # Update info text
        self.update_info_text()
    
    def update_graph(self):
        """Update the chart (alias for generate_chart for consistency)."""
        # Always regenerate the chart when called - this ensures checkbox changes trigger updates
        if hasattr(self, 'ax'):
            # Force full regeneration
            self.generate_chart()
    
    def update_info_text(self):
        """Update the info text panel."""
        info_lines = []
        
        if not self.ax.lines:
            info_lines.append("No weapons selected.")
            info_lines.append("")
            info_lines.append("Select weapons and generate")
            info_lines.append("a chart to see DPM comparison.")
        else:
            info_lines.append("Selected Weapons:")
            info_lines.append("")
            
            for i, dropdown in enumerate(self.weapon_dropdowns):
                ammo_name = dropdown.get()
                if ammo_name and (ammo_name in self.app.ammunition_props or 
                                 (hasattr(self.app, 'custom_weapons') and ammo_name in self.app.custom_weapons)):
                    quantity = self.weapon_quantity_vars[i].get() if i < len(self.weapon_quantity_vars) else 1
                    info_lines.append(f"  {ammo_name} (x{quantity})")
            
            info_lines.append("")
            info_lines.append("─" * 40)
            info_lines.append("")
            info_lines.append("Hover over data points")
            info_lines.append("on the chart to see")
            info_lines.append("detailed information.")
        
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete('1.0', tk.END)
        self.info_text.insert('1.0', '\n'.join(info_lines))
        self.info_text.config(state=tk.DISABLED)
    
    def on_hover(self, event):
        """Handle mouse hover events to show data point info."""
        if event.inaxes != self.ax:
            return
        
        # Don't update hover info if a point is already selected
        if self.selected_range is not None:
            return
        
        # Find closest data point
        closest_line = None
        closest_point_idx = None
        min_distance = float('inf')
        
        for line in self.ax.lines:
            xdata = line.get_xdata()
            ydata = line.get_ydata()
            
            for i in range(len(xdata)):
                distance = ((event.xdata - xdata[i]) ** 2 + (event.ydata - ydata[i]) ** 2) ** 0.5
                if distance < min_distance:
                    min_distance = distance
                    closest_line = line
                    closest_point_idx = i
        
        # Show info if close enough (within reasonable distance)
        if closest_line and min_distance < 50:  # Adjust threshold as needed
            range_val = closest_line.get_xdata()[closest_point_idx]
            dpm_val = closest_line.get_ydata()[closest_point_idx]
            ammo_label = closest_line.get_label()
            
            # Update info text
            info_lines = [
                f"Range: {range_val:.0f} m",
                f"DPM: {dpm_val:.2f}",
                f"Ammunition: {ammo_label}",
                "",
                "Click to select this point"
            ]
            
            self.info_text.config(state=tk.NORMAL)
            self.info_text.delete('1.0', tk.END)
            self.info_text.insert('1.0', '\n'.join(info_lines))
            self.info_text.config(state=tk.DISABLED)
    
    def on_click(self, event):
        """Handle mouse click events to select a data point."""
        if event.inaxes != self.ax:
            return
        
        # Find closest data point
        closest_line = None
        closest_point_idx = None
        min_distance = float('inf')
        
        for line in self.ax.lines:
            xdata = line.get_xdata()
            ydata = line.get_ydata()
            
            for i in range(len(xdata)):
                distance = ((event.xdata - xdata[i]) ** 2 + (event.ydata - ydata[i]) ** 2) ** 0.5
                if distance < min_distance:
                    min_distance = distance
                    closest_line = line
                    closest_point_idx = i
        
        # Select point if close enough
        if closest_line and min_distance < 50:
            range_val = closest_line.get_xdata()[closest_point_idx]
            
            # Toggle selection: if clicking the same range, deselect; otherwise select new range
            if self.selected_range is not None and abs(self.selected_range - range_val) < 1.0:
                # Deselect - remove all markers
                self.selected_range = None
                if self.selected_marker:
                    self.selected_marker.remove()
                    self.selected_marker = None
                # Update info text to default
                self.update_info_text()
            else:
                # Select new range - remove old marker first
                if self.selected_marker:
                    self.selected_marker.remove()
                
                # Store selected range
                self.selected_range = range_val
                
                # Draw marker at selected range for all weapons
                marker_x = []
                marker_y = []
                for weapon_label, data_points in self.line_data.items():
                    dpm_at_range = self._get_dpm_at_range(data_points, range_val)
                    if dpm_at_range > 0:
                        marker_x.append(range_val)
                        marker_y.append(dpm_at_range)
                
                if marker_x:
                    self.selected_marker = self.ax.scatter(marker_x, marker_y, s=100, c='red', marker='X', zorder=10, label='Selected Range')
                
                # Show all weapons at this range
                self.show_weapons_at_range(range_val)
            
            self.canvas.draw()
    
    def show_weapons_at_range(self, range_val: float):
        """Show detailed information for all weapons at a specific range."""
        info_lines = [
            f"Range: {range_val:.0f} m",
            "",
            "Weapons at this range:",
            ""
        ]
        
        range_modifiers_table = self.get_current_range_modifier_table()
        
        for i, dropdown in enumerate(self.weapon_dropdowns):
            ammo_name = dropdown.get()
            if ammo_name:
                quantity = self.weapon_quantity_vars[i].get() if i < len(self.weapon_quantity_vars) else 1
                # Get bonus values for this weapon - read directly from combo widget
                bonus_combo = self.weapon_bonus_combos[i] if i < len(self.weapon_bonus_combos) else None
                bonus_display = bonus_combo.get() if bonus_combo else "No bonuses"
                veterancy_accuracy_bonus, reload_speed_multiplier = self.get_bonus_values_from_display(bonus_display)
                # Check if this weapon should use vanilla range table
                use_vanilla_range_table = self.weapon_use_vanilla_range_table_vars[i].get() if i < len(self.weapon_use_vanilla_range_table_vars) else False
                
                ammo_props = None
                is_custom = False
                
                # Get ammunition properties
                if ammo_name in self.app.ammunition_props:
                    ammo_props = self.app.ammunition_props[ammo_name].copy()
                elif hasattr(self.app, 'custom_weapons') and ammo_name in self.app.custom_weapons:
                    ammo_props = self.app.custom_weapons[ammo_name].copy()
                    is_custom = True
                
                if ammo_props:
                    max_range = ammo_props.get("max_range", 0)
                    base_accuracy = ammo_props.get("idling", 0)
                    damage_type = self.damage_type_var.get() if hasattr(self, 'damage_type_var') else "Physical"
                    if damage_type == "Suppression":
                        base_damage = ammo_props.get("suppress_damages", 0)
                        damage_label = "Suppression Damage"
                    else:
                        base_damage = ammo_props.get("physical_damages", 0)
                        damage_label = "Physical Damage"
                    
                    if range_val <= max_range:
                        # Determine which range table to use for this weapon
                        weapon_range_table = RANGE_MODIFIERS_TABLE if use_vanilla_range_table else range_modifiers_table
                        # Read checkbox value fresh each time
                        use_multiplicative = self.use_multiplicative_vet_bonus_var.get()
                        accuracy = calculate_accuracy(
                            range_val,
                            max_range,
                            base_accuracy,
                            self.successive_hits,
                            veterancy_level=0,
                            veterancy_accuracy_bonus=veterancy_accuracy_bonus,
                            range_modifiers_table=weapon_range_table,
                            use_multiplicative_vet_bonus=use_multiplicative
                        )
                        shots_per_min = calculate_shots_per_minute(ammo_props, reload_speed_multiplier)
                        dpm = accuracy * base_damage * shots_per_min * quantity
                        per_weapon_dpm = dpm / quantity if quantity > 0 else 0
                        
                        # Calculate ammo consumption per minute
                        shots_per_salvo = ammo_props.get("shots_count_per_salvo", 1)
                        ammo_per_salvo = ammo_props.get("affichage_munition_par_salve", 0.0)
                        ammo_per_min = shots_per_min * (ammo_per_salvo / shots_per_salvo) if shots_per_salvo > 0 else 0
                        
                        # Get additional weapon stats
                        salvo_reload = ammo_props.get("time_between_salvos", 0.0)
                        shot_reload = ammo_props.get("time_between_shots", None)
                        per_weapon_damage = base_damage
                        total_damage = base_damage * quantity if quantity > 0 else 0.0
                        
                        custom_label = " (custom)" if is_custom else ""
                        bonus_label = ""
                        if veterancy_accuracy_bonus != 0.0 or reload_speed_multiplier != 1.0:
                            bonus_parts = []
                            if veterancy_accuracy_bonus != 0.0:
                                bonus_parts.append(f"Acc: +{veterancy_accuracy_bonus * 100:.1f}%")
                            if reload_speed_multiplier != 1.0:
                                bonus_parts.append(f"Reload: {reload_speed_multiplier:.2f}x")
                            bonus_label = f" [{', '.join(bonus_parts)}]"
                        
                        info_lines.append(f"{ammo_name}{custom_label} (x{quantity}){bonus_label}:")
                        info_lines.append(f"  DPM: {dpm:.2f} ({per_weapon_dpm:.2f} per weapon)")
                        info_lines.append(f"  {damage_label}: {total_damage:.2f} ({per_weapon_damage:.2f} per weapon)")
                        info_lines.append(f"  Base Accuracy: {base_accuracy * 100:.1f}%")
                        info_lines.append(f"  Accuracy: {accuracy * 100:.1f}%")
                        info_lines.append(f"  Shots/min: {shots_per_min:.1f} (per weapon)")
                        info_lines.append(f"  Ammo/min: {ammo_per_min:.1f} (per weapon)")
                        info_lines.append(f"  Shots per Salvo: {shots_per_salvo}")
                        info_lines.append(f"  Salvo Reload: {salvo_reload:.2f}s")
                        if shot_reload is not None:
                            info_lines.append(f"  Shot Reload: {shot_reload:.2f}s")
                        else:
                            info_lines.append(f"  Shot Reload: N/A")
                        info_lines.append("")
        
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete('1.0', tk.END)
        self.info_text.insert('1.0', '\n'.join(info_lines))
        self.info_text.config(state=tk.DISABLED)
    
    def _get_dpm_at_range(self, dpm_data: List[Tuple[float, float]], target_range: float) -> float:
        """Get DPM value at a specific range, interpolating if necessary."""
        if not dpm_data:
            return 0.0
        
        # If target_range exactly matches a data point, return it
        for r, dpm in dpm_data:
            if abs(r - target_range) < 0.01:  # Small tolerance for floating point
                return dpm
        
        # Find the two closest points for interpolation
        for i in range(len(dpm_data) - 1):
            r1, dpm1 = dpm_data[i]
            r2, dpm2 = dpm_data[i + 1]
            
            if r1 <= target_range <= r2:
                # Linear interpolation
                if abs(r2 - r1) < 0.01:  # Avoid division by zero
                    return dpm1
                t = (target_range - r1) / (r2 - r1)
                return dpm1 + t * (dpm2 - dpm1)
        
        # If target_range is beyond the data, return 0 (weapon can't fire beyond max range)
        if target_range > dpm_data[-1][0]:
            return 0.0
        
        # If target_range is before the data, return the first value
        return dpm_data[0][1]
    
    def save_tab_state(self) -> Dict[str, Any]:
        """Save the current state of the weapons tab."""
        state = {
            "selected_weapons": [],
            "quantities": [],
            "bonuses": [],
            "visibility_states": [],
            "vanilla_range_table_states": [],
            "successive_hits": self.successive_hits_var.get() if hasattr(self, 'successive_hits_var') else 0,
            "use_multiplicative_vet_bonus": self.use_multiplicative_vet_bonus_var.get() if hasattr(self, 'use_multiplicative_vet_bonus_var') else True,
            "range_table": self.range_table_var.get() if hasattr(self, 'range_table_var') else "vanilla",
        }
        
        for idx, dropdown in enumerate(self.weapon_dropdowns):
            weapon_name = dropdown.get() if hasattr(dropdown, 'get') else ""
            state["selected_weapons"].append(weapon_name)
            
            # Get quantity
            quantity = self.weapon_quantity_vars[idx].get() if idx < len(self.weapon_quantity_vars) else 1
            state["quantities"].append(quantity)
            
            # Get bonus selection
            bonus = self.weapon_bonus_combos[idx].get() if idx < len(self.weapon_bonus_combos) else "No bonuses"
            state["bonuses"].append(bonus)
            
            # Get visibility state
            visibility = self.weapon_visibility_vars[idx].get() if idx < len(self.weapon_visibility_vars) else True
            state["visibility_states"].append(visibility)
            
            # Get vanilla range table checkbox state
            use_vanilla = self.weapon_use_vanilla_range_table_vars[idx].get() if idx < len(self.weapon_use_vanilla_range_table_vars) else False
            state["vanilla_range_table_states"].append(use_vanilla)
        
        return state
    
    def load_tab_state(self, state: Dict[str, Any]):
        """Load a saved state into the weapons tab."""
        if not state:
            return
        
        # Load successive hits
        if "successive_hits" in state and hasattr(self, 'successive_hits_var'):
            self.successive_hits_var.set(state["successive_hits"])
            self.successive_hits = state["successive_hits"]
        
        # Load multiplicative vet bonus checkbox
        if "use_multiplicative_vet_bonus" in state and hasattr(self, 'use_multiplicative_vet_bonus_var'):
            self.use_multiplicative_vet_bonus_var.set(state["use_multiplicative_vet_bonus"])
        
        # Load range table selection
        if "range_table" in state and hasattr(self, 'range_table_var'):
            range_table = state["range_table"]
            if range_table in self.app.range_modifier_tables:
                self.range_table_var.set(range_table)
                self.app.current_range_modifier_table_name = range_table
        
        # Ensure we have enough dropdowns
        selected_weapons = state.get("selected_weapons", [])
        while len(self.weapon_dropdowns) < len(selected_weapons):
            self.add_weapon_dropdown()
        
        # Load state for each dropdown
        for idx, weapon_name in enumerate(selected_weapons):
            if idx < len(self.weapon_dropdowns):
                dropdown = self.weapon_dropdowns[idx]
                
                # Set weapon selection
                if weapon_name:
                    dropdown.set(weapon_name)
                    self.on_weapon_selected(dropdown)
                
                # Set quantity
                quantities = state.get("quantities", [])
                if idx < len(quantities) and idx < len(self.weapon_quantity_vars):
                    self.weapon_quantity_vars[idx].set(quantities[idx])
                
                # Set bonus selection
                bonuses = state.get("bonuses", [])
                if idx < len(bonuses) and idx < len(self.weapon_bonus_combos):
                    self.weapon_bonus_combos[idx].set(bonuses[idx])
                
                # Set visibility state
                visibility_states = state.get("visibility_states", [])
                if idx < len(visibility_states) and idx < len(self.weapon_visibility_vars):
                    self.weapon_visibility_vars[idx].set(visibility_states[idx])
                
                # Set vanilla range table checkbox state
                vanilla_states = state.get("vanilla_range_table_states", [])
                if idx < len(vanilla_states) and idx < len(self.weapon_use_vanilla_range_table_vars):
                    self.weapon_use_vanilla_range_table_vars[idx].set(vanilla_states[idx])
        
        # Update graph after loading all state
        if hasattr(self, 'update_graph'):
            self.update_graph()

