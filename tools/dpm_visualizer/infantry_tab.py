"""Infantry Tab for DPM Visualizer."""

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

from .constants import RANGE_MODIFIERS_TABLE, SMALL_ARMS_DAMAGE_FAMILIES
from .calculations import (
    calculate_dpm,
    calculate_accuracy,
    calculate_shots_per_minute,
    extract_base_weapon_name,
)
from .ndf_parsers import (
    parse_infantry_units,
    parse_weapon_descriptors,
    parse_ammunition_properties,
)
from .ui_components import SearchableCombobox, RangeModifierEditor


class InfantryTab:
    """Infantry tab for DPM visualization."""
    
    def __init__(self, parent: ttk.Frame, app):
        """Initialize the Infantry tab.
        
        Args:
            parent: Parent frame (the tab frame)
            app: Main application instance (for shared data)
        """
        self.parent = parent
        self.app = app
        
        # Tab-specific state
        self.selected_units: List[str] = []  # List of selected unit names
        self.unit_dropdowns: List[SearchableCombobox] = []  # List of unit dropdown widgets
        self.veterancy_selectors: Dict[SearchableCombobox, ttk.Frame] = {}  # Map unit dropdown to veterancy button frame
        self.veterancy_buttons: Dict[SearchableCombobox, Dict[int, ttk.Button]] = {}  # Map unit dropdown to veterancy level buttons
        self.unit_veterancy_levels: Dict[SearchableCombobox, int] = {}  # Map unit dropdown to veterancy level
        self.unit_display_names: List[str] = []  # Cached display names list
        self.successive_hits: int = 0
        self.range_step: float = 25.0  # Fixed at 25m
        
        # Configure styles for veterancy buttons
        self.style = ttk.Style()
        self.style.configure('SelectedVet.TButton', background='#90EE90', foreground='black')
        self.style.configure('DisabledVet.TButton', background='#505050', foreground='#666666', relief='flat')
        self.style.map('DisabledVet.TButton', 
                      background=[('disabled', '#505050'), ('!disabled', '#505050'), ('active', '#505050'), ('pressed', '#505050')],
                      foreground=[('disabled', '#666666'), ('!disabled', '#666666'), ('active', '#666666'), ('pressed', '#666666')],
                      relief=[('disabled', 'flat'), ('!disabled', 'flat'), ('active', 'flat'), ('pressed', 'flat')])
        
        # Setup UI
        self.setup_ui()
        
        # Initialize after UI is set up
        self._initialize_data()
    
    def _initialize_data(self):
        """Initialize data after UI is set up."""
        # Update unit dropdowns if data is already loaded
        if hasattr(self.app, 'infantry_units') and self.app.infantry_units:
            self.unit_display_names = []
            for unit_name in sorted(self.app.infantry_units.keys()):
                self.unit_display_names.append(unit_name)
            
            # Update all existing dropdowns
            for dropdown in self.unit_dropdowns:
                if isinstance(dropdown, SearchableCombobox):
                    dropdown.set_values(self.unit_display_names)
            
            # Update custom unit weapon dropdowns
            self.update_custom_weapon_dropdowns()
            
            # Update bonus combinations dropdowns
            if hasattr(self, 'custom_unit_bonus_combos'):
                self.collect_bonus_combinations()
            
            # Update load unit dropdown
            if hasattr(self, 'load_unit_combo'):
                self.load_unit_combo.set_values(self.unit_display_names)
    
    def setup_ui(self):
        """Set up the Infantry tab UI."""
        # Main content area - vertical layout
        main_container = ttk.Frame(self.parent)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Top section - Left panel and Right panel (chart)
        top_section = ttk.Frame(main_container)
        top_section.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Left panel - Controls
        left_panel = ttk.Frame(top_section, width=300)
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        left_panel.pack_propagate(False)
        
        # Unit selection section
        unit_section = ttk.LabelFrame(left_panel, text="Infantry Units to Compare", padding="5")
        unit_section.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Scrollable frame for unit dropdowns
        unit_canvas_frame = ttk.Frame(unit_section)
        unit_canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        unit_canvas = tk.Canvas(unit_canvas_frame)
        unit_scrollbar = ttk.Scrollbar(unit_canvas_frame, orient="vertical", command=unit_canvas.yview)
        unit_scrollable_frame = ttk.Frame(unit_canvas)
        
        def update_scrollregion(event):
            unit_canvas.configure(scrollregion=unit_canvas.bbox("all"))
        
        unit_scrollable_frame.bind("<Configure>", update_scrollregion)
        
        unit_canvas.create_window((0, 0), window=unit_scrollable_frame, anchor="nw")
        unit_canvas.configure(yscrollcommand=unit_scrollbar.set)
        
        # Make canvas scrollable with mouse wheel
        def on_mousewheel(event):
            unit_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        
        unit_canvas.bind("<MouseWheel>", on_mousewheel)
        
        unit_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        unit_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.unit_dropdowns_frame = unit_scrollable_frame
        self.unit_canvas = unit_canvas  # Store reference to canvas
        
        # Add/Remove unit buttons
        unit_button_frame = ttk.Frame(unit_section)
        unit_button_frame.pack(fill=tk.X, pady=(5, 0))
        ttk.Button(unit_button_frame, text="+ Add Unit", command=self.add_unit_dropdown).pack(side=tk.LEFT, padx=2)
        ttk.Button(unit_button_frame, text="- Remove", command=self.remove_unit_dropdown).pack(side=tk.LEFT, padx=2)
        
        # Add initial unit dropdown
        self.add_unit_dropdown()
        
        # Successive hits slider
        ttk.Label(left_panel, text="Successive Hits:").pack(anchor=tk.W, pady=(0, 5))
        self.hits_var = tk.IntVar(value=0)
        self.hits_label = ttk.Label(left_panel, text="0")
        self.hits_label.pack(anchor=tk.W)
        hits_scale = ttk.Scale(left_panel, from_=0, to=5, variable=self.hits_var, orient=tk.HORIZONTAL, command=self.on_hits_changed)
        hits_scale.pack(fill=tk.X, pady=(0, 10))
        
        # Buttons
        ttk.Button(left_panel, text="Generate Chart", command=self.generate_chart).pack(fill=tk.X, pady=(0, 5))
        ttk.Button(left_panel, text="Range Modifier Tables", command=self.open_range_modifier_editor).pack(fill=tk.X, pady=(0, 5))
        ttk.Button(left_panel, text="Export Chart", command=self.export_chart).pack(fill=tk.X)
        
        # Right panel - Chart and Info Panel
        right_panel = ttk.Frame(top_section)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Chart frame (takes most of the space)
        chart_frame = ttk.Frame(right_panel)
        chart_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Matplotlib figure
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlabel("Range (m)")
        self.ax.set_ylabel("DPM (Damage Per Minute)")
        self.ax.grid(True)
        table_name = getattr(self.app, 'current_range_modifier_table_name', 'vanilla')
        self.ax.set_title(f"Infantry Weapon DPM vs Range (Range Modifier: {table_name})")
        
        # No need for extra right margin since we have a dedicated info panel
        self.fig.subplots_adjust(right=0.95)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=chart_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Info panel on the right
        info_panel = ttk.LabelFrame(right_panel, text="Data Point Info", padding="10")
        info_panel.pack(side=tk.RIGHT, fill=tk.BOTH, padx=(10, 0))
        info_panel.config(width=400)  # Fixed width - wider to show more characters per line
        
        # Scrollable text widget for displaying hover information
        text_frame = ttk.Frame(info_panel)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.info_text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            width=45,  # Increased from 30 to show more characters per line
            height=20,
            font=('Consolas', 9),
            state=tk.DISABLED,
            bg='#f0f0f0',
            relief=tk.FLAT,
            yscrollcommand=scrollbar.set
        )
        self.info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.info_text.yview)
        
        # Initial message (will be updated when chart is generated)
        self.info_text.config(state=tk.NORMAL)
        self.info_text.insert('1.0', 'Generate a chart to see\nveterancy bonuses.\n\nHover over data points\nto see details.\n\nClick on a data point\nto select it and see\nall units at that range.')
        self.info_text.config(state=tk.DISABLED)
        
        # Store veterancy info reference
        self.current_veterancy_info = None
        
        # Bottom section - Custom Unit and Custom Weapons (horizontal layout)
        bottom_section = ttk.LabelFrame(main_container, text="Custom Units & Weapons", padding="5")
        bottom_section.pack(fill=tk.X, pady=(10, 0))
        
        # Custom Unit Section (left side of bottom section)
        custom_unit_section = ttk.LabelFrame(bottom_section, text="Custom Unit", padding="5")
        custom_unit_section.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Load from existing unit dropdown
        ttk.Label(custom_unit_section, text="Load from existing unit:").pack(anchor=tk.W)
        self.load_unit_combo = SearchableCombobox(custom_unit_section, width=25)
        self.load_unit_combo.pack(fill=tk.X, pady=(0, 5))
        self.load_unit_combo.bind("<<ComboboxSelected>>", self.on_load_unit_selected)
        
        # Custom unit name entry
        ttk.Label(custom_unit_section, text="Unit Name:").pack(anchor=tk.W)
        self.custom_unit_name_var = tk.StringVar(value="Custom Unit")
        ttk.Entry(custom_unit_section, textvariable=self.custom_unit_name_var, width=25).pack(fill=tk.X, pady=(0, 5))
        
        # Weapon selection dropdowns (up to 3) with quantity selectors
        ttk.Label(custom_unit_section, text="Weapons:").pack(anchor=tk.W)
        self.custom_weapon_vars = []
        self.custom_weapon_combos = []
        self.custom_weapon_quantity_vars = []
        
        for i in range(3):
            weapon_frame = ttk.Frame(custom_unit_section)
            weapon_frame.pack(fill=tk.X, pady=2)
            
            ttk.Label(weapon_frame, text=f"Weapon {i+1}:", width=10).pack(side=tk.LEFT, padx=(0, 5))
            
            weapon_var = tk.StringVar()
            self.custom_weapon_vars.append(weapon_var)
            
            combo = SearchableCombobox(weapon_frame, textvariable=weapon_var, width=15)
            combo.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
            self.custom_weapon_combos.append(combo)
            
            # Quantity selector
            ttk.Label(weapon_frame, text="Qty:").pack(side=tk.LEFT, padx=(0, 2))
            quantity_var = tk.IntVar(value=1)
            self.custom_weapon_quantity_vars.append(quantity_var)
            quantity_spinbox = ttk.Spinbox(weapon_frame, from_=1, to=10, textvariable=quantity_var, width=5)
            quantity_spinbox.pack(side=tk.LEFT)
        
        # Custom unit veterancy selector (checkboxes for available levels)
        vet_frame = ttk.Frame(custom_unit_section)
        vet_frame.pack(fill=tk.X, pady=(5, 5))
        
        ttk.Label(vet_frame, text="Available Vet:", width=12).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_unit_vet_checkboxes = []
        self.custom_unit_vet_vars = []
        
        for level in range(4):
            var = tk.BooleanVar(value=(level == 0))  # Default to level 0 checked
            self.custom_unit_vet_vars.append(var)
            checkbox = ttk.Checkbutton(vet_frame, text=str(level), variable=var)
            checkbox.pack(side=tk.LEFT, padx=2)
            self.custom_unit_vet_checkboxes.append(checkbox)
        
        # Veterancy bonuses section
        bonuses_frame = ttk.LabelFrame(custom_unit_section, text="Veterancy Bonuses", padding="5")
        bonuses_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Create bonus dropdowns for each veterancy level
        self.custom_unit_bonus_vars = []  # Bonus selection vars
        self.custom_unit_bonus_combos = []  # Bonus dropdown combos
        self.bonus_combinations = []  # List of available bonus combinations
        
        for level in range(4):
            level_frame = ttk.Frame(bonuses_frame)
            level_frame.pack(fill=tk.X, pady=2)
            
            ttk.Label(level_frame, text=f"Lv {level}:", width=6).pack(side=tk.LEFT, padx=(0, 5))
            
            # Bonus dropdown
            bonus_var = tk.StringVar()
            self.custom_unit_bonus_vars.append(bonus_var)
            bonus_combo = SearchableCombobox(level_frame, width=30)
            bonus_combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
            self.custom_unit_bonus_combos.append(bonus_combo)
        
        # Create/Edit custom unit buttons
        self.unit_button_frame = ttk.Frame(custom_unit_section)
        self.unit_button_frame.pack(fill=tk.X, pady=(5, 0))
        ttk.Button(self.unit_button_frame, text="Create Custom Unit", command=self.create_custom_unit).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 2))
        ttk.Button(self.unit_button_frame, text="Edit Custom Unit", command=self.edit_custom_unit).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(2, 0))
        
        # Custom Weapon Section (right side of bottom section)
        custom_weapon_section = ttk.LabelFrame(bottom_section, text="Create Custom Weapon", padding="5")
        custom_weapon_section.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Load from existing weapon dropdown
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
        
        # Row 2: Physical Damage, Damage Family
        row2 = ttk.Frame(props_frame)
        row2.pack(fill=tk.X, pady=2)
        
        ttk.Label(row2, text="Physical Damage:", width=15).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_damage_var = tk.StringVar(value="10")
        ttk.Entry(row2, textvariable=self.custom_weapon_damage_var, width=10).pack(side=tk.LEFT, padx=(0, 10))
        
        ttk.Label(row2, text="Damage Family:", width=15).pack(side=tk.LEFT, padx=(0, 5))
        self.custom_weapon_damage_family_var = tk.StringVar(value="DamageFamily_sa_intermediate")
        damage_family_combo = ttk.Combobox(row2, textvariable=self.custom_weapon_damage_family_var, width=25, state="readonly")
        damage_family_combo['values'] = list(SMALL_ARMS_DAMAGE_FAMILIES)
        damage_family_combo.pack(side=tk.LEFT)
        
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
        
        # Store line data for tooltips
        self.line_data: Dict[str, List[Tuple[float, float]]] = {}  # Total DPM by range
        self.weapon_dpm_data: Dict[str, Dict[str, List[Tuple[float, float]]]] = {}  # Unit -> Weapon -> DPM data
        self.hover_cid = None  # Store connection ID
        self.click_cid = None  # Store click connection ID
        self.selected_range: Optional[float] = None  # Selected range for locked display
        self.selected_marker = None  # Marker for selected data point
        self.hover_marker = None  # Marker for hovered data point
        
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

    def add_unit_dropdown(self):
        """Add a new unit selection dropdown with searchable functionality and veterancy buttons."""
        frame = ttk.Frame(self.unit_dropdowns_frame)
        frame.pack(fill=tk.X, pady=2)
        
        # Top row: Unit selection
        unit_row = ttk.Frame(frame)
        unit_row.pack(fill=tk.X)
        
        # Add label with number
        dropdown_num = len(self.unit_dropdowns) + 1
        label = ttk.Label(unit_row, text=f"Unit {dropdown_num}:", width=8)
        label.pack(side=tk.LEFT, padx=(0, 5))
        
        combo = SearchableCombobox(unit_row, width=25)
        combo.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Store reference to parent app for updating values
        combo._parent_app = self
        
        if hasattr(self, 'unit_display_names') and self.unit_display_names:
            combo.set_values(self.unit_display_names)
        
        combo.bind("<<ComboboxSelected>>", lambda e, c=combo: self.on_unit_selected(c))
        
        # Bottom row: Veterancy buttons
        veterancy_row = ttk.Frame(frame)
        veterancy_row.pack(fill=tk.X, pady=(2, 0))
        
        veterancy_label = ttk.Label(veterancy_row, text="Vet:", width=8)
        veterancy_label.pack(side=tk.LEFT, padx=(0, 2))
        
        veterancy_frame = ttk.Frame(veterancy_row)
        veterancy_frame.pack(side=tk.LEFT)
        
        # Create veterancy buttons (always visible, labeled I, II, III, IV)
        veterancy_buttons_dict = {}
        vet_labels = ['I', 'II', 'III', 'IV']
        for level in [0, 1, 2, 3]:
            btn = ttk.Button(
                veterancy_frame,
                text=vet_labels[level],
                width=3,
                command=lambda l=level, c=combo: self.set_veterancy_level(c, l)
            )
            btn.pack(side=tk.LEFT, padx=1)
            veterancy_buttons_dict[level] = btn
            # Always show buttons (don't hide initially)
        
        self.unit_dropdowns.append(combo)
        self.veterancy_selectors[combo] = veterancy_frame
        self.veterancy_buttons[combo] = veterancy_buttons_dict
        self.unit_veterancy_levels[combo] = 0
        
        # Update scroll region after adding
        self.unit_dropdowns_frame.update_idletasks()
        if hasattr(self, 'unit_canvas'):
            self.unit_canvas.configure(scrollregion=self.unit_canvas.bbox("all"))
        
        # Update all labels to reflect correct numbering
        self.update_dropdown_labels()
    
    def set_veterancy_level(self, combo: SearchableCombobox, level: int):
        """Set veterancy level for a unit and update button states."""
        # Check if this level is available for the selected unit
        unit_name = combo.get()
        if unit_name and unit_name in self.app.infantry_units:
            unit_info = self.app.infantry_units[unit_name]
            available_levels = unit_info.get("available_veterancy_levels", [0, 1, 2, 3])
            if level not in available_levels:
                # Don't allow selection of unavailable levels
                return
        
        self.unit_veterancy_levels[combo] = level
        
        # Update button states - use style to show selected state
        if combo in self.veterancy_buttons:
            vet_labels = ['I', 'II', 'III', 'IV']
            for btn_level, btn in self.veterancy_buttons[combo].items():
                # Ensure text is preserved
                btn.configure(text=vet_labels[btn_level])
                if btn_level == level:
                    btn.configure(style='SelectedVet.TButton')  # Visual indication of selected
                else:
                    # Check if button should be disabled
                    unit_name = combo.get()
                    if unit_name and unit_name in self.app.infantry_units:
                        unit_info = self.app.infantry_units[unit_name]
                        available_levels = unit_info.get("available_veterancy_levels", [0, 1, 2, 3])
                        if btn_level not in available_levels:
                            btn.configure(style='DisabledVet.TButton', state='disabled')
                        else:
                            btn.configure(style='TButton', state='normal')
                    else:
                        btn.configure(style='TButton', state='normal')
        
        # Regenerate chart
        self.generate_chart()
    
    def remove_unit_dropdown(self):
        """Remove the last unit dropdown."""
        if self.unit_dropdowns:
            dropdown = self.unit_dropdowns.pop()
            if isinstance(dropdown, SearchableCombobox):
                # Close popup if open
                if dropdown.is_open:
                    dropdown.hide_dropdown()
                # Remove veterancy selector references
                if dropdown in self.veterancy_selectors:
                    del self.veterancy_selectors[dropdown]
                if dropdown in self.veterancy_buttons:
                    del self.veterancy_buttons[dropdown]
                if dropdown in self.unit_veterancy_levels:
                    del self.unit_veterancy_levels[dropdown]
                # Destroy the entire frame (which contains unit_row + veterancy_row)
                # dropdown.master is unit_row, dropdown.master.master is frame
                parent_frame = dropdown.master.master
                if parent_frame:
                    parent_frame.destroy()
            
            # Update scroll region
            self.unit_dropdowns_frame.update_idletasks()
            if hasattr(self, 'unit_canvas'):
                self.unit_canvas.configure(scrollregion=self.unit_canvas.bbox("all"))
            
            # Update all labels to reflect correct numbering
            self.update_dropdown_labels()
    
    def update_dropdown_labels(self):
        """Update labels on all dropdowns to show correct numbering."""
        for idx, dropdown in enumerate(self.unit_dropdowns):
            frame = dropdown.master
            # Find the label in the frame
            for widget in frame.winfo_children():
                if isinstance(widget, ttk.Label):
                    widget.config(text=f"Unit {idx + 1}:")
                    break
    
    def on_unit_selected(self, combo=None):
        """Handle unit selection - update veterancy button states based on selected unit."""
        if combo is None:
            return
        
        unit_name = combo.get()
        if not unit_name or unit_name not in self.app.infantry_units:
            # Reset all buttons to default style if no unit selected
            if combo in self.veterancy_buttons:
                current_vet = self.unit_veterancy_levels.get(combo, 0)
                vet_labels = ['I', 'II', 'III', 'IV']
                for level, btn in self.veterancy_buttons[combo].items():
                    # Ensure text is preserved
                    btn.configure(text=vet_labels[level])
                    if level == current_vet:
                        btn.configure(style='SelectedVet.TButton', state='normal')
                    else:
                        btn.configure(style='TButton', state='normal')
            return
        
        # Get veterancy info for this unit
        unit_info = self.app.infantry_units[unit_name]
        available_levels = unit_info.get("available_veterancy_levels", [0, 1, 2, 3])
        
        # Update veterancy buttons for this dropdown
        if combo in self.veterancy_buttons:
            current_vet = self.unit_veterancy_levels.get(combo, 0)
            
            # Ensure current veterancy level is valid, if not use first available
            if current_vet not in available_levels:
                current_vet = available_levels[0] if available_levels else 0
                self.unit_veterancy_levels[combo] = current_vet
            
            # Update button states - all buttons always visible
            vet_labels = ['I', 'II', 'III', 'IV']
            for level, btn in self.veterancy_buttons[combo].items():
                # Ensure text is preserved
                btn.configure(text=vet_labels[level])
                
                # Update button state based on selection and availability
                if level not in available_levels:
                    # Disabled button - use distinct style
                    if level == current_vet:
                        # Shouldn't happen, but handle it
                        btn.configure(style='DisabledVet.TButton', state='disabled')
                    else:
                        btn.configure(style='DisabledVet.TButton', state='disabled')
                else:
                    # Enabled button
                    if level == current_vet:
                        btn.configure(style='SelectedVet.TButton', state='normal')
                    else:
                        btn.configure(style='TButton', state='normal')
    
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
    
    def on_hits_changed(self, value=None):
        """Handle successive hits slider change."""
        self.successive_hits = self.hits_var.get()
        self.hits_label.config(text=str(self.successive_hits))
    
    def generate_chart(self):
        """Generate the DPM chart comparing total squad DPM."""
        # Store the currently selected range before clearing (to restore it after regeneration)
        saved_selected_range = self.selected_range if self.selected_range is not None else None
        
        # Get selected units and their veterancy levels from all dropdowns
        selected_units = []
        unit_veterancy_map = {}  # Map unit_name to veterancy_level
        
        for dropdown in self.unit_dropdowns:
            if isinstance(dropdown, SearchableCombobox):
                unit_name = dropdown.get()
            else:
                unit_name = dropdown.get()
            
            if unit_name and unit_name in self.app.infantry_units:
                selected_units.append(unit_name)
                # Get veterancy level from stored value
                veterancy_level = self.unit_veterancy_levels.get(dropdown, 0)
                unit_veterancy_map[unit_name] = veterancy_level
        
        # Check if we have any units to plot
        if not selected_units:
            messagebox.showwarning("Warning", "Please select at least one infantry unit")
            self.ax.set_ylim(bottom=0)
            self.canvas.draw()
            return
        
        # Clear previous chart and selection
        self.ax.clear()
        self.selected_range = None
        if self.selected_marker is not None:
            try:
                self.selected_marker.remove()
            except:
                pass
            self.selected_marker = None
        if self.hover_marker is not None:
            try:
                self.hover_marker.remove()
            except:
                pass
            self.hover_marker = None
        self.ax.set_xlabel("Range (m)")
        self.ax.set_ylabel("Total Squad DPM (Damage Per Minute)")
        self.ax.grid(True)
        table_name = getattr(self.app, 'current_range_modifier_table_name', 'vanilla')
        self.ax.set_title(f"Infantry Squad Total DPM vs Range (Range Modifier: {table_name})")
        
        # No need for extra right margin since we have a dedicated info panel
        self.fig.subplots_adjust(right=0.95)
        
        # Clear previous line data
        self.line_data = {}
        self.weapon_dpm_data = {}
        
        # Reconnect hover handler (in case it was disconnected)
        self.connect_hover_handler()
        
        # Plot each selected unit's total DPM
        colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'cyan', 'magenta']
        color_idx = 0
        max_chart_range = 0.0  # Track maximum range across all units
        
        for unit_name in selected_units:
            unit_info = self.app.infantry_units.get(unit_name, {})
            
            # Skip custom units here - they'll be processed separately
            if unit_info.get("custom_unit", False):
                continue
            
            # Get weapon descriptor for this unit
            weapon_descr_name = f"WeaponDescriptor_{unit_name}"
            if weapon_descr_name not in self.app.weapon_descriptors:
                continue
            
            weapon_descr = self.app.weapon_descriptors[weapon_descr_name]
            
            # Calculate total DPM for all small arms weapons in the squad
            # First, collect all DPM data points from all weapons
            all_weapon_dpm_data = []
            unit_weapon_data = {}  # Store individual weapon DPM data for this unit
            max_unit_range = 0.0
            
            # Iterate through all weapons in the unit
            for turret_data in weapon_descr.get("turrets", {}).values():
                for ammo_name, weapon_info in turret_data.get("weapons", {}).items():
                    base_name = extract_base_weapon_name(ammo_name)
                    
                    # Get ammunition properties
                    ammo_props = self.app.ammunition_props.get(ammo_name) or self.app.ammunition_props.get(base_name)
                    if not ammo_props:
                        continue
                    
                    # Check if this is a small arms weapon by damage family
                    damage_family = ammo_props.get("damage_family", "")
                    if damage_family not in SMALL_ARMS_DAMAGE_FAMILIES:
                        continue
                    
                    # Must have required properties for DPM calculation
                    if not (ammo_props.get("idling") and ammo_props.get("max_range") and ammo_props.get("physical_damages")):
                        continue
                    
                    # Track max range for this unit
                    max_unit_range = max(max_unit_range, ammo_props.get("max_range", 0.0))
                    
                    # Get veterancy level for this unit
                    veterancy_level = unit_veterancy_map.get(unit_name, 0)
                    
                    # Get veterancy bonuses from unit info
                    unit_info = self.app.infantry_units.get(unit_name, {})
                    veterancy_accuracy_bonuses = unit_info.get("veterancy_accuracy_bonuses", {})
                    veterancy_accuracy_bonus = veterancy_accuracy_bonuses.get(veterancy_level, 0.0)
                    veterancy_reload_multipliers = unit_info.get("veterancy_reload_speed_multipliers", {})
                    reload_speed_multiplier = veterancy_reload_multipliers.get(veterancy_level, 1.0)
                    
                    # Calculate DPM for this weapon
                    dpm_data = calculate_dpm(
                        ammo_props,
                        weapon_info["quantity"],
                        self.successive_hits,
                        self.range_step,
                        veterancy_level,
                        veterancy_accuracy_bonus,
                        reload_speed_multiplier,
                        self.get_current_range_modifier_table(),
                        use_multiplicative_vet_bonus=self.app.range_modifier_vet_bonus_type.get(
                            self.app.current_range_modifier_table_name, True
                        )
                    )
                    
                    # Calculate shots per minute and ammunition consumption
                    shots_per_minute = calculate_shots_per_minute(ammo_props, reload_speed_multiplier)
                    nb_tir_par_salves = ammo_props.get("nb_tir_par_salves", 1)
                    affichage_munition_par_salve = ammo_props.get("affichage_munition_par_salve", nb_tir_par_salves)
                    ammo_per_shot = affichage_munition_par_salve / nb_tir_par_salves if nb_tir_par_salves > 0 else 1.0
                    ammo_consumption_per_minute = shots_per_minute * ammo_per_shot
                    
                    # Store individual weapon DPM data with quantity info and firing stats
                    weapon_display_name = f"{base_name} (x{weapon_info['quantity']})"
                    unit_weapon_data[weapon_display_name] = {
                        "dpm_data": dpm_data,
                        "quantity": weapon_info["quantity"],
                        "base_name": base_name,
                        "ammo_props": ammo_props,  # Store for accuracy calculation
                        "veterancy_level": veterancy_level,
                        "veterancy_accuracy_bonus": veterancy_accuracy_bonus,
                        "shots_per_minute": shots_per_minute,
                        "ammo_consumption_per_minute": ammo_consumption_per_minute,
                    }
                    
                    all_weapon_dpm_data.append(dpm_data)
            
            # Combine all weapon DPM data at common range points
            if all_weapon_dpm_data:
                # Get all unique range points
                all_ranges = set()
                for dpm_data in all_weapon_dpm_data:
                    all_ranges.update(r for r, _ in dpm_data)
                
                # Sort ranges
                sorted_ranges = sorted(all_ranges)
                
                # Calculate total DPM at each range by interpolating from each weapon's data
                total_dpm_by_range = {}
                for range_val in sorted_ranges:
                    total_dpm = 0.0
                    for dpm_data in all_weapon_dpm_data:
                        # Find DPM value at this range (interpolate if needed)
                        dpm_val = self._get_dpm_at_range(dpm_data, range_val)
                        total_dpm += dpm_val
                    total_dpm_by_range[range_val] = total_dpm
            else:
                total_dpm_by_range = {}
            
            # Plot total squad DPM
            if total_dpm_by_range:
                ranges = sorted(total_dpm_by_range.keys())
                dpm_values = [total_dpm_by_range[r] for r in ranges]
                color = colors[color_idx % len(colors)]
                
                # Track maximum range for x-axis ticks
                max_chart_range = max(max_chart_range, max(ranges))
                
                # Use unit name for legend (not display name/token)
                line, = self.ax.plot(ranges, dpm_values, label=unit_name, color=color, linewidth=2)
                
                # Store line data for tooltips (total DPM)
                self.line_data[unit_name] = list(zip(ranges, dpm_values))
                
                # Store individual weapon DPM data for this unit
                self.weapon_dpm_data[unit_name] = unit_weapon_data
                
                color_idx += 1
        
        # Process custom units (units with custom_unit flag)
        for unit_name in selected_units:
            unit_info = self.app.infantry_units.get(unit_name, {})
            if not unit_info.get("custom_unit", False):
                continue  # Skip regular units, they're already processed above
            
            # This is a custom unit
            selected_weapons = unit_info.get("custom_weapons", {})  # Dict mapping weapon_name -> quantity
            if not selected_weapons:
                continue
            
            # Get veterancy level (use default if not set in dropdown)
            veterancy_level = unit_veterancy_map.get(unit_name, unit_info.get("default_veterancy_level", 0))
            
            # Calculate total DPM for custom unit
            all_weapon_dpm_data = []
            unit_weapon_data = {}
            max_unit_range = 0.0
            
            for weapon_name, quantity in selected_weapons.items():
                # Get ammunition properties (check custom weapons first, then regular)
                ammo_props = self.app.custom_weapons.get(weapon_name) or self.app.ammunition_props.get(weapon_name)
                if not ammo_props:
                    continue
                
                # Must have required properties for DPM calculation
                if not (ammo_props.get("idling") and ammo_props.get("max_range") and ammo_props.get("physical_damages")):
                    continue
                
                # Track max range for this unit
                max_unit_range = max(max_unit_range, ammo_props.get("max_range", 0.0))
                
                # Get veterancy bonuses from unit info
                veterancy_accuracy_bonuses = unit_info.get("veterancy_accuracy_bonuses", {})
                veterancy_accuracy_bonus = veterancy_accuracy_bonuses.get(veterancy_level, 0.0)
                veterancy_reload_multipliers = unit_info.get("veterancy_reload_speed_multipliers", {})
                reload_speed_multiplier = veterancy_reload_multipliers.get(veterancy_level, 1.0)
                
                # Calculate DPM for this weapon using the standard calculate_dpm function
                weapon_dpm_data = calculate_dpm(
                    ammo_props,
                    quantity,  # Use stored quantity
                    self.successive_hits,
                    self.range_step,
                    veterancy_level,
                    veterancy_accuracy_bonus,
                    reload_speed_multiplier,
                    self.get_current_range_modifier_table(),
                    use_multiplicative_vet_bonus=self.app.range_modifier_vet_bonus_type.get(
                        self.app.current_range_modifier_table_name, True
                    )
                )
                
                # Store weapon data with quantity
                unit_weapon_data[weapon_name] = {
                    "dpm_data": weapon_dpm_data,
                    "quantity": quantity,
                    "ammo_props": ammo_props,  # Store for accuracy calculation
                    "veterancy_level": veterancy_level,
                    "veterancy_accuracy_bonus": veterancy_accuracy_bonus,
                    "shots_per_minute": calculate_shots_per_minute(ammo_props, reload_speed_multiplier),
                    "ammo_consumption_per_minute": calculate_shots_per_minute(ammo_props, reload_speed_multiplier) * (ammo_props.get("affichage_munition_par_salve", 0.0) / ammo_props.get("nb_tir_par_salves", 1.0)),
                }
                
                # Add to total DPM
                for r, dpm in weapon_dpm_data:
                    all_weapon_dpm_data.append((r, dpm))
            
            if all_weapon_dpm_data:
                # Combine DPM from all weapons at each range
                total_dpm_by_range = {}
                for r, dpm in all_weapon_dpm_data:
                    if r not in total_dpm_by_range:
                        total_dpm_by_range[r] = 0.0
                    total_dpm_by_range[r] += dpm
                
                # Convert to sorted list
                ranges = sorted(total_dpm_by_range.keys())
                dpm_values = [total_dpm_by_range[r] for r in ranges]
                color = colors[color_idx % len(colors)]
                
                # Track maximum range for x-axis ticks
                max_chart_range = max(max_chart_range, max(ranges))
                
                # Plot custom unit
                line, = self.ax.plot(ranges, dpm_values, label=unit_name, color=color, linewidth=2, linestyle='--')
                
                # Store line data for tooltips
                self.line_data[unit_name] = list(zip(ranges, dpm_values))
                
                # Store individual weapon DPM data for this unit
                self.weapon_dpm_data[unit_name] = unit_weapon_data
                
                color_idx += 1
        
        # All units for display (custom units are already in selected_units)
        all_units_for_display = selected_units
        all_unit_veterancy_map = unit_veterancy_map.copy()
        
        if color_idx > 0:
            # Display veterancy bonuses in the info panel
            self._display_veterancy_bonuses_in_info_panel(all_units_for_display, all_unit_veterancy_map)
            
            self.ax.legend()
            
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
                    
                    # Draw marker at selected range for all units
                    marker_x = []
                    marker_y = []
                    for unit_name, data_points in self.line_data.items():
                        dpm_at_range = self._get_dpm_at_range(data_points, saved_selected_range)
                        if dpm_at_range > 0:
                            marker_x.append(saved_selected_range)
                            marker_y.append(dpm_at_range)
                    
                    if marker_x:
                        self.selected_marker = self.ax.scatter(marker_x, marker_y, s=100, c='red', marker='X', zorder=10, label='Selected Range')
                    
                    # Update info panel with all units at this range
                    self._update_info_panel_for_range(saved_selected_range)
        
        self.ax.set_ylim(bottom=0)
        self.canvas.draw()
    
    def update_custom_weapon_dropdowns(self):
        """Update custom unit weapon dropdowns with available small arms ammunition and custom weapons."""
        if not hasattr(self, 'custom_weapon_combos'):
            return
        
        # Get all small arms ammunition names
        weapon_names = []
        for ammo_name, ammo_props in self.app.ammunition_props.items():
            damage_family = ammo_props.get("damage_family", "")
            if damage_family in SMALL_ARMS_DAMAGE_FAMILIES:
                # Check if it has required properties
                if ammo_props.get("idling") and ammo_props.get("max_range") and ammo_props.get("physical_damages"):
                    weapon_names.append(ammo_name)
        
        # Add custom weapons
        weapon_names.extend(sorted(self.app.custom_weapons.keys()))
        
        weapon_names = sorted(weapon_names)
        
        # Update all weapon dropdowns
        for combo in self.custom_weapon_combos:
            combo.set_values(weapon_names)
        
        # Update load weapon dropdown
        if hasattr(self, 'load_weapon_combo'):
            self.load_weapon_combo.set_values(weapon_names)
    
    def collect_bonus_combinations(self):
        """Collect all unique veterancy bonus combinations from existing units."""
        bonus_set = set()
        
        # Add default "No bonuses" option
        bonus_set.add((0.0, 1.0, "No bonuses"))
        
        # Collect from all units
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
        
        # Extract display strings
        bonus_display_strings = [combo[2] for combo in self.bonus_combinations]
        
        # Update all bonus dropdowns
        if hasattr(self, 'custom_unit_bonus_combos'):
            for combo in self.custom_unit_bonus_combos:
                combo.set_values(bonus_display_strings)
        
        return bonus_display_strings
    
    def get_bonus_values_from_display(self, display_string: str):
        """Get accuracy bonus and reload multiplier from display string."""
        # Find matching combination
        for combo in self.bonus_combinations:
            if combo[2] == display_string:
                return combo[0], combo[1]  # acc_bonus, reload_mult
        
        # Default if not found
        return 0.0, 1.0
    
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
        self.custom_weapon_damage_family_var.set(ammo_props.get("damage_family", "DamageFamily_sa_intermediate"))
        self.custom_weapon_shots_per_salvo_var.set(str(ammo_props.get("nb_tir_par_salves", 1)))
        self.custom_weapon_time_between_salvos_var.set(str(ammo_props.get("time_between_salvos", 2.0)))
        
        time_between_shots = ammo_props.get("time_between_shots")
        if time_between_shots is not None:
            self.custom_weapon_time_between_shots_var.set(str(time_between_shots))
        else:
            self.custom_weapon_time_between_shots_var.set("")
        
        self.custom_weapon_aiming_time_var.set(str(ammo_props.get("aiming_time", 1.0)))
        self.custom_weapon_ammo_per_salvo_var.set(str(ammo_props.get("affichage_munition_par_salve", 1)))
    
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
            damage_family = self.custom_weapon_damage_family_var.get()
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
                "damage_family": damage_family,
                "nb_tir_par_salves": shots_per_salvo,
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
            self.update_custom_weapon_dropdowns()
            
            # Update weapons tab dropdowns
            if hasattr(self.app, 'weapons_tab') and hasattr(self.app.weapons_tab, '_initialize_data'):
                self.app.weapons_tab._initialize_data()
            
            messagebox.showinfo("Success", f"Custom weapon '{weapon_name}' created successfully!")
            
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}. Please check all fields are valid numbers.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create custom weapon: {e}")
    
    
    def create_custom_unit(self):
        """Create a custom unit and add it to the unit dropdowns."""
        unit_name = self.custom_unit_name_var.get().strip()
        if not unit_name:
            messagebox.showwarning("Warning", "Please enter a unit name")
            return
        
        # Get selected weapons with quantities - use combo.get() instead of var.get()
        selected_weapons = {}  # Dict mapping weapon_name -> quantity
        for i, combo in enumerate(self.custom_weapon_combos):
            weapon_name = combo.get().strip()
            if weapon_name:
                # Verify weapon exists (either in ammunition_props or custom_weapons)
                if weapon_name in self.app.ammunition_props or weapon_name in self.app.custom_weapons:
                    quantity = self.custom_weapon_quantity_vars[i].get()
                    if quantity > 0:
                        selected_weapons[weapon_name] = quantity
                else:
                    messagebox.showwarning("Warning", f"Weapon '{weapon_name}' not found. Please create it first or select a valid weapon.")
                    return
        
        if not selected_weapons:
            messagebox.showwarning("Warning", "Please select at least one weapon")
            return
        
        # Get available veterancy levels from checkboxes
        available_vet_levels = []
        for level, var in enumerate(self.custom_unit_vet_vars):
            if var.get():
                available_vet_levels.append(level)
        
        if not available_vet_levels:
            messagebox.showwarning("Warning", "Please select at least one veterancy level")
            return
        
        # Get veterancy bonuses from dropdowns
        veterancy_accuracy_bonuses = {}
        veterancy_reload_speed_multipliers = {}
        
        for level in range(4):
            if level in available_vet_levels:
                # Get selected bonus from dropdown
                bonus_display = self.custom_unit_bonus_combos[level].get().strip()
                if not bonus_display:
                    # Default to no bonuses
                    veterancy_accuracy_bonuses[level] = 0.0
                    veterancy_reload_speed_multipliers[level] = 1.0
                else:
                    acc_bonus, reload_mult = self.get_bonus_values_from_display(bonus_display)
                    veterancy_accuracy_bonuses[level] = acc_bonus
                    veterancy_reload_speed_multipliers[level] = reload_mult
        
        # Create custom unit entry in infantry_units (so it appears in dropdowns)
        custom_unit_info = {
            "is_infantry": True,
            "tags": [],
            "unit_role": "infantry",
            "display_name": unit_name,
            "veterancy_pack": "simple_v3",
            "available_veterancy_levels": available_vet_levels,
            "experience_levels_pack": None,
            "veterancy_accuracy_bonuses": veterancy_accuracy_bonuses,
            "veterancy_reload_speed_multipliers": veterancy_reload_speed_multipliers,
            "custom_unit": True,  # Flag to identify custom units
            "custom_weapons": selected_weapons,  # Store selected weapons with quantities
            "default_veterancy_level": available_vet_levels[0],  # Store default veterancy (first available)
        }
        
        # Add to infantry_units (replace if name already exists)
        if unit_name in self.app.infantry_units:
            response = messagebox.askyesno("Confirm", f"Unit '{unit_name}' already exists. Replace it?")
            if not response:
                return
        
        self.app.infantry_units[unit_name] = custom_unit_info
        
        # Save user data
        self.save_user_data()
        
        # Update unit dropdowns
        self.unit_display_names = []
        for name in sorted(self.app.infantry_units.keys()):
            self.unit_display_names.append(name)
        
        # Update all existing dropdowns
        for dropdown in self.unit_dropdowns:
            if isinstance(dropdown, SearchableCombobox):
                dropdown.set_values(self.unit_display_names)
        
        # Update load unit dropdown
        if hasattr(self, 'load_unit_combo'):
            self.load_unit_combo.set_values(self.unit_display_names)
        
        messagebox.showinfo("Success", f"Custom unit '{unit_name}' created! You can now select it from the unit dropdowns.")
        
        # Clear the custom unit form
        self.custom_unit_name_var.set("Custom Unit")
        for var in self.custom_weapon_vars:
            var.set("")
        for var in self.custom_weapon_quantity_vars:
            var.set(1)
        # Reset veterancy checkboxes (only level 0 checked)
        for i, var in enumerate(self.custom_unit_vet_vars):
            var.set(i == 0)
        # Reset veterancy bonuses (set to "No bonuses")
        for combo in self.custom_unit_bonus_combos:
            combo.var.set("No bonuses")
    
    def edit_custom_unit(self):
        """Edit an existing custom unit."""
        # Get list of custom units
        custom_unit_names = [name for name, info in self.app.infantry_units.items() if info.get("custom_unit", False)]
        
        if not custom_unit_names:
            messagebox.showwarning("Warning", "No custom units found to edit.")
            return
        
        # Show selection dialog
        dialog = tk.Toplevel(self.app.root)
        dialog.title("Edit Custom Unit")
        dialog.geometry("300x150")
        dialog.transient(self.app.root)
        dialog.grab_set()
        
        ttk.Label(dialog, text="Select unit to edit:").pack(pady=10)
        unit_var = tk.StringVar()
        unit_combo = ttk.Combobox(dialog, textvariable=unit_var, values=custom_unit_names, width=30, state="readonly")
        unit_combo.pack(pady=5)
        unit_combo.current(0)
        
        def load_for_edit():
            unit_name = unit_var.get()
            if unit_name:
                self.on_load_unit_selected_for_edit(unit_name)
                dialog.destroy()
        
        ttk.Button(dialog, text="Edit", command=load_for_edit).pack(pady=5)
    
    def on_load_unit_selected_for_edit(self, unit_name: str):
        """Load unit data into form for editing."""
        unit_info = self.app.infantry_units.get(unit_name, {})
        if not unit_info:
            return
        
        # Store original name for update
        self.editing_unit_name = unit_name
        
        # Populate form using existing on_load_unit_selected logic
        self.on_load_unit_selected()
        
        # Update button text to show we're editing
        if hasattr(self, 'unit_button_frame'):
            for widget in self.unit_button_frame.winfo_children():
                if isinstance(widget, ttk.Button) and widget.cget("text") == "Create Custom Unit":
                    widget.config(text="Update Custom Unit", command=self.update_custom_unit)
                    break
    
    def update_custom_unit(self):
        """Update an existing custom unit."""
        if not hasattr(self, 'editing_unit_name'):
            messagebox.showwarning("Warning", "No unit selected for editing.")
            return
        
        original_name = self.editing_unit_name
        new_name = self.custom_unit_name_var.get().strip()
        
        if not new_name:
            messagebox.showwarning("Warning", "Please enter a unit name")
            return
        
        # If name changed and new name exists, ask for confirmation
        if new_name != original_name and new_name in self.app.infantry_units:
            response = messagebox.askyesno("Confirm", f"Unit '{new_name}' already exists. Replace it?")
            if not response:
                return
        
        # Remove old unit if name changed
        if new_name != original_name and original_name in self.app.infantry_units:
            del self.app.infantry_units[original_name]
        
        # Create/update the unit (reuse create logic)
        self.create_custom_unit()
        
        # Reset button text
        if hasattr(self, 'unit_button_frame'):
            for widget in self.unit_button_frame.winfo_children():
                if isinstance(widget, ttk.Button) and widget.cget("text") == "Update Custom Unit":
                    widget.config(text="Create Custom Unit", command=self.create_custom_unit)
                    break
        
        # Clear editing flag
        if hasattr(self, 'editing_unit_name'):
            delattr(self, 'editing_unit_name')
    
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
        self.custom_weapon_damage_family_var.set(weapon_props.get("damage_family", "DamageFamily_sa_intermediate"))
        self.custom_weapon_shots_per_salvo_var.set(str(weapon_props.get("nb_tir_par_salves", 1)))
        self.custom_weapon_time_between_salvos_var.set(str(weapon_props.get("time_between_salvos", 1.0)))
        time_between_shots = weapon_props.get("time_between_shots")
        self.custom_weapon_time_between_shots_var.set(str(time_between_shots) if time_between_shots is not None else "")
        self.custom_weapon_aiming_time_var.set(str(weapon_props.get("aiming_time", 0)))
        self.custom_weapon_ammo_per_salvo_var.set(str(weapon_props.get("affichage_munition_par_salve", 1.0)))
        
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
    
    def on_load_unit_selected(self, event=None):
        """Populate custom unit fields from selected existing unit."""
        unit_name = self.load_unit_combo.get().strip()
        if not unit_name:
            return
        
        unit_info = self.app.infantry_units.get(unit_name, {})
        if not unit_info:
            return
        
        # Populate unit name
        self.custom_unit_name_var.set(unit_name)
        
        # Get available veterancy levels and set checkboxes
        available_vet_levels = unit_info.get("available_veterancy_levels", [0])
        for i, var in enumerate(self.custom_unit_vet_vars):
            var.set(i in available_vet_levels)
        
        # Populate veterancy bonuses
        veterancy_accuracy_bonuses = unit_info.get("veterancy_accuracy_bonuses", {})
        veterancy_reload_multipliers = unit_info.get("veterancy_reload_speed_multipliers", {})
        
        for level in range(4):
            if level in available_vet_levels:
                # Get bonus values for this level
                acc_bonus = veterancy_accuracy_bonuses.get(level, 0.0)
                reload_mult = veterancy_reload_multipliers.get(level, 1.0)
                
                # Find matching display string
                matching_display = "No bonuses"
                if hasattr(self, 'bonus_combinations'):
                    for combo in self.bonus_combinations:
                        if abs(combo[0] - acc_bonus) < 0.0001 and abs(combo[1] - reload_mult) < 0.0001:
                            matching_display = combo[2]
                            break
                
                # Set the dropdown value
                self.custom_unit_bonus_combos[level].var.set(matching_display)
            else:
                # Clear if level not available
                self.custom_unit_bonus_combos[level].var.set("No bonuses")
        
        # Extract weapons from unit
        weapons = []
        quantities = []
        
        # Check if it's a custom unit with stored weapons
        if unit_info.get("custom_unit", False):
            custom_weapons_dict = unit_info.get("custom_weapons", {})
            if isinstance(custom_weapons_dict, dict):
                # New format: dict mapping weapon_name -> quantity
                weapons = list(custom_weapons_dict.keys())
                quantities = [custom_weapons_dict[w] for w in weapons]
            else:
                # Old format: list of weapon names (backward compatibility)
                weapons = custom_weapons_dict if isinstance(custom_weapons_dict, list) else []
                quantities = [1] * len(weapons)
        else:
            # Extract weapons from weapon descriptor
            weapon_descr_name = f"WeaponDescriptor_{unit_name}"
            if weapon_descr_name in self.app.weapon_descriptors:
                weapon_descr = self.app.weapon_descriptors[weapon_descr_name]
                
                # Collect all small arms weapons with quantities
                for turret_data in weapon_descr.get("turrets", {}).values():
                    for ammo_name, weapon_info in turret_data.get("weapons", {}).items():
                        base_name = extract_base_weapon_name(ammo_name)
                        ammo_props = self.app.ammunition_props.get(ammo_name) or self.app.ammunition_props.get(base_name)
                        if not ammo_props:
                            continue
                        
                        damage_family = ammo_props.get("damage_family", "")
                        if damage_family in SMALL_ARMS_DAMAGE_FAMILIES:
                            if ammo_name not in weapons:
                                weapons.append(ammo_name)
                                quantities.append(weapon_info.get("quantity", 1))
        
        # Populate weapon dropdowns and quantities (up to 3)
        for i, combo in enumerate(self.custom_weapon_combos):
            if i < len(weapons):
                combo.var.set(weapons[i])
                self.custom_weapon_quantity_vars[i].set(quantities[i] if i < len(quantities) else 1)
            else:
                combo.var.set("")
                self.custom_weapon_quantity_vars[i].set(1)
    
    def _display_veterancy_bonuses_in_info_panel(self, selected_units: List[str], unit_veterancy_map: Dict[str, int]):
        """Display veterancy bonuses for each unit in the info panel."""
        if not selected_units:
            return
        
        # Build veterancy bonus text
        bonus_lines = ["Veterancy Bonuses:", ""]
        
        for unit_name in selected_units:
            veterancy_level = unit_veterancy_map.get(unit_name, 0)
            unit_info = self.app.infantry_units.get(unit_name, {})
            
            # Debug: Check if unit_info has the bonus keys
            if not unit_info:
                bonus_lines.append(f"{unit_name} (Lv {veterancy_level}):")
                bonus_lines.append("    Unit info not found")
                continue
            
            veterancy_accuracy_bonuses = unit_info.get("veterancy_accuracy_bonuses", {})
            accuracy_bonus = veterancy_accuracy_bonuses.get(veterancy_level, 0.0)
            veterancy_reload_multipliers = unit_info.get("veterancy_reload_speed_multipliers", {})
            reload_multiplier = veterancy_reload_multipliers.get(veterancy_level, 1.0)
            
            # Debug output to console
            if not veterancy_accuracy_bonuses and not veterancy_reload_multipliers:
                xp_pack = unit_info.get("experience_levels_pack", "None")
                print(f"DEBUG: {unit_name} (Lv {veterancy_level}) - No bonuses found. XP Pack: {xp_pack}")
                print(f"DEBUG: Unit info keys: {list(unit_info.keys())}")
            
            # Format bonuses
            accuracy_percent = accuracy_bonus * 100.0
            
            # Create text string
            bonus_parts = []
            if accuracy_bonus != 0.0:
                bonus_parts.append(f"Acc: +{accuracy_percent:.1f}%")
            
            # Show reload bonus if multiplier is not 1.0 (faster or slower reload)
            if reload_multiplier != 1.0:
                if reload_multiplier < 1.0:
                    # Faster reload (bonus)
                    reload_speed_percent = (1.0 - reload_multiplier) * 100.0  # Convert multiplier to speed increase
                    bonus_parts.append(f"Reload: +{reload_speed_percent:.1f}%")
                else:
                    # Slower reload (penalty) - probably shouldn't happen but handle it
                    reload_penalty_percent = (reload_multiplier - 1.0) * 100.0
                    bonus_parts.append(f"Reload: -{reload_penalty_percent:.1f}%")
            
            # Format with indentation
            bonus_lines.append(f"{unit_name} (Lv {veterancy_level}):")
            if bonus_parts:
                for bonus_part in bonus_parts:
                    bonus_lines.append(f"    {bonus_part}")
            else:
                bonus_lines.append("    No bonuses")
        
        # Store veterancy info (without the hover message) for use when hovering
        self.current_veterancy_info = '\n'.join(bonus_lines)  # Store veterancy bonuses only
        
        # Add separator and hover message
        bonus_lines.append("")
        bonus_lines.append("─" * 40)  # Separator line
        bonus_lines.append("")
        bonus_lines.append("Hover over data points")
        bonus_lines.append("on the chart to see")
        bonus_lines.append("detailed information.")
        
        # Update info panel
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete('1.0', tk.END)
        self.info_text.insert('1.0', '\n'.join(bonus_lines))
        self.info_text.config(state=tk.DISABLED)
    
    def _get_unit_color(self, unit_name: str) -> str:
        """Get the color used for a unit's line in the chart."""
        # Find the unit in the lines
        for line in self.ax.lines:
            if line.get_label() == unit_name:
                return line.get_color()
        # Default to black if not found
        return 'black'
    
    def _remove_all_markers(self):
        """Remove all scatter plot markers (selected and hover) from the chart."""
        # Remove all red X scatter markers by iterating through collections backwards
        if hasattr(self.ax, 'collections'):
            # Work backwards through collections to safely remove items
            i = len(self.ax.collections) - 1
            while i >= 0:
                try:
                    coll = self.ax.collections[i]
                    # Check if it's a scatter plot with red color
                    if hasattr(coll, 'get_facecolors'):
                        colors = coll.get_facecolors()
                        if len(colors) > 0 and len(colors[0]) >= 3:
                            # Check if red (approximately [1.0, 0.0, 0.0])
                            if abs(colors[0][0] - 1.0) < 0.1 and abs(colors[0][1]) < 0.1 and abs(colors[0][2]) < 0.1:
                                # Remove any red scatter plot (they're all our markers)
                                coll.remove()
                                self.ax.collections.pop(i)
                except (ValueError, AttributeError, IndexError):
                    # Collection may have been removed already or doesn't exist
                    pass
                i -= 1
        
        # Clear marker references
        self.selected_marker = None
        self.hover_marker = None
    
    def on_hover(self, event):
        """Handle mouse hover events to show data point info in the info panel."""
        # If a range is selected, don't update on hover
        if self.selected_range is not None:
            return
        
        if event.inaxes != self.ax or not self.line_data:
            # Remove hover marker when mouse leaves chart area
            if self.hover_marker is not None:
                try:
                    self.hover_marker.remove()
                except:
                    pass
                self.hover_marker = None
            # Show veterancy bonuses when mouse leaves chart area
            self._update_info_panel_with_veterancy_only()
            self.canvas.draw_idle()
            return
        
        # Find the closest data point across all lines
        min_dist = float('inf')
        closest_unit = None
        closest_point = None
        
        # Calculate distance in data coordinates
        for unit_name, data_points in self.line_data.items():
            for x, y in data_points:
                if event.xdata is None or event.ydata is None:
                    continue
                # Distance in data space (normalize by axis ranges for better sensitivity)
                x_range = self.ax.get_xlim()[1] - self.ax.get_xlim()[0]
                y_range = self.ax.get_ylim()[1] - self.ax.get_ylim()[0]
                if x_range > 0 and y_range > 0:
                    dist = ((event.xdata - x) / x_range) ** 2 + ((event.ydata - y) / y_range) ** 2
                    dist = dist ** 0.5  # Normalized distance
                    if dist < min_dist:
                        min_dist = dist
                        closest_unit = unit_name
                        closest_point = (x, y)
        
        # Show tooltip if close enough (threshold in normalized coordinates)
        if closest_point and min_dist < 0.02:  # 2% of axis range
            x, y = closest_point
            
            # Update hover marker - show red X for all units at this range
            if self.hover_marker is not None:
                try:
                    self.hover_marker.remove()
                except:
                    pass
                self.hover_marker = None
            
            # Draw marker at hovered range for all units
            marker_x = []
            marker_y = []
            for unit_name, data_points in self.line_data.items():
                dpm_at_range = self._get_dpm_at_range(data_points, x)
                if dpm_at_range > 0:
                    marker_x.append(x)
                    marker_y.append(dpm_at_range)
            
            if marker_x:
                self.hover_marker = self.ax.scatter(marker_x, marker_y, s=100, c='red', marker='X', zorder=10, label='Hovered Range')
            
            # Build tooltip text with weapon breakdown
            tooltip_lines = [f'{closest_unit}', f'Range: {x:.0f}m', f'Total DPM: {y:.2f}', '']
            
            # Add individual weapon DPM breakdown
            if closest_unit in self.weapon_dpm_data:
                tooltip_lines.append('Weapon Breakdown:')
                weapon_data = self.weapon_dpm_data[closest_unit]
                for weapon_name, weapon_info in weapon_data.items():
                    # Get DPM at this range for this weapon (total for all instances)
                    total_weapon_dpm = self._get_dpm_at_range(weapon_info["dpm_data"], x)
                    if total_weapon_dpm > 0:
                        quantity = weapon_info["quantity"]
                        per_weapon_dpm = total_weapon_dpm / quantity if quantity > 0 else 0
                        shots_per_min = weapon_info.get("shots_per_minute", 0.0)
                        ammo_per_min = weapon_info.get("ammo_consumption_per_minute", 0.0)
                        
                        # Calculate accuracy at this range
                        accuracy = 0.0
                        if "ammo_props" in weapon_info:
                            ammo_props = weapon_info["ammo_props"]
                            base_accuracy = ammo_props.get("idling", 0.0)
                            max_range = ammo_props.get("max_range", 0.0)
                            veterancy_level = weapon_info.get("veterancy_level", 0)
                            veterancy_accuracy_bonus = weapon_info.get("veterancy_accuracy_bonus", 0.0)
                            
                            if max_range > 0:
                                accuracy = calculate_accuracy(
                                    x,
                                    max_range,
                                    base_accuracy,
                                    self.successive_hits,
                                    veterancy_level,
                                    veterancy_accuracy_bonus,
                                    self.get_current_range_modifier_table(),
                                    use_multiplicative_vet_bonus=self.app.range_modifier_vet_bonus_type.get(
                                        self.app.current_range_modifier_table_name, True
                                    )
                                )
                        
                        # Get additional weapon stats from ammo_props
                        ammo_props_for_stats = weapon_info.get("ammo_props", {})
                        salvo_reload = ammo_props_for_stats.get("time_between_salvos", 0.0)
                        shot_reload = ammo_props_for_stats.get("time_between_shots", None)
                        shots_per_salvo = ammo_props_for_stats.get("nb_tir_par_salves", 1)
                        physical_damage = ammo_props_for_stats.get("physical_damages", 0.0)
                        per_weapon_damage = physical_damage  # Physical damage is per weapon
                        total_damage = physical_damage * quantity if quantity > 0 else 0.0
                        
                        tooltip_lines.append(f'  {weapon_name}:')
                        tooltip_lines.append(f'    DPM: {total_weapon_dpm:.2f} ({per_weapon_dpm:.2f} per weapon)')
                        tooltip_lines.append(f'    Physical Damage: {total_damage:.2f} ({per_weapon_damage:.2f} per weapon)')
                        tooltip_lines.append(f'    Base Accuracy: {base_accuracy * 100:.1f}%')
                        tooltip_lines.append(f'    Accuracy: {accuracy * 100:.1f}%')
                        tooltip_lines.append(f'    Shots/min: {shots_per_min:.1f} (per weapon)')
                        tooltip_lines.append(f'    Ammo/min: {ammo_per_min:.1f} (per weapon)')
                        tooltip_lines.append(f'    Shots per Salvo: {shots_per_salvo}')
                        tooltip_lines.append(f'    Salvo Reload: {salvo_reload:.2f}s')
                        if shot_reload is not None:
                            tooltip_lines.append(f'    Shot Reload: {shot_reload:.2f}s')
                        else:
                            tooltip_lines.append(f'    Shot Reload: N/A')
            
            tooltip_text = '\n'.join(tooltip_lines)
            
            # Update info panel with veterancy bonuses always at top, then data point info
            self.info_text.config(state=tk.NORMAL)
            self.info_text.delete('1.0', tk.END)
            
            # Build complete text content
            content_lines = []
            
            # Always show veterancy bonuses at the top if available
            if hasattr(self, 'current_veterancy_info') and self.current_veterancy_info:
                content_lines.append(self.current_veterancy_info)
                content_lines.append('')
                content_lines.append('─' * 40)
                content_lines.append('')
            
            # Add data point information
            content_lines.append(tooltip_text)
            content_lines.append('')
            content_lines.append('─' * 40)
            content_lines.append('Click to select this range')
            content_lines.append('and see all units.')
            
            # Insert all content at once
            self.info_text.insert('1.0', '\n'.join(content_lines))
            self.info_text.config(state=tk.DISABLED)
            self.info_text.see('1.0')
            
            self.canvas.draw_idle()
        else:
            # Remove hover marker when not hovering over a point
            if self.hover_marker is not None:
                try:
                    self.hover_marker.remove()
                except:
                    pass
                self.hover_marker = None
            # Always show veterancy bonuses when not hovering over a point
            self._update_info_panel_with_veterancy_only()
            self.canvas.draw_idle()
    
    def on_click(self, event):
        """Handle mouse click events to select/deselect data points."""
        if event.inaxes != self.ax or not self.line_data:
            return
        
        if event.button != 1:  # Only handle left mouse button
            return
        
        # Find the closest data point across all lines
        min_dist = float('inf')
        closest_point = None
        
        # Calculate distance in data coordinates
        for unit_name, data_points in self.line_data.items():
            for x, y in data_points:
                if event.xdata is None or event.ydata is None:
                    continue
                # Distance in data space (normalize by axis ranges for better sensitivity)
                x_range = self.ax.get_xlim()[1] - self.ax.get_xlim()[0]
                y_range = self.ax.get_ylim()[1] - self.ax.get_ylim()[0]
                if x_range > 0 and y_range > 0:
                    dist = ((event.xdata - x) / x_range) ** 2 + ((event.ydata - y) / y_range) ** 2
                    dist = dist ** 0.5  # Normalized distance
                    if dist < min_dist:
                        min_dist = dist
                        closest_point = (x, y)
        
        # Select/deselect if close enough (threshold in normalized coordinates)
        if closest_point and min_dist < 0.02:  # 2% of axis range
            x, y = closest_point
            
            # Toggle selection: if clicking the same range, deselect; otherwise select new range
            if self.selected_range is not None and abs(self.selected_range - x) < 1.0:
                # Deselect - remove all markers
                self.selected_range = None
                self._remove_all_markers()
                # Show veterancy bonuses
                self._update_info_panel_with_veterancy_only()
            else:
                # Select new range - remove all existing markers first
                self._remove_all_markers()
                
                # Select new range
                self.selected_range = x
                
                # Draw marker at selected range for all units
                marker_x = []
                marker_y = []
                for unit_name, data_points in self.line_data.items():
                    dpm_at_range = self._get_dpm_at_range(data_points, x)
                    if dpm_at_range > 0:
                        marker_x.append(x)
                        marker_y.append(dpm_at_range)
                
                if marker_x:
                    self.selected_marker = self.ax.scatter(marker_x, marker_y, s=100, c='red', marker='X', zorder=10, label='Selected Range')
                
                # Update info panel with all units at this range
                self._update_info_panel_for_range(x)
            
            # Force immediate redraw to ensure old markers are removed and new ones are shown
            self.canvas.draw()
    
    def _update_info_panel_for_range(self, range_val: float):
        """Update info panel to show all units at the specified range."""
        if not self.line_data:
            return
        
        # Build info for all units at this range
        info_lines = []
        
        # Always show veterancy bonuses at the top
        if hasattr(self, 'current_veterancy_info') and self.current_veterancy_info:
            info_lines.append(self.current_veterancy_info)
            info_lines.append("")
            info_lines.append("─" * 40)
            info_lines.append("")
        
        info_lines.append(f"Selected Range: {range_val:.0f}m")
        info_lines.append("")
        
        # Get all units and their DPM at this range
        unit_dpm_at_range = []
        for unit_name, data_points in self.line_data.items():
            dpm_at_range = self._get_dpm_at_range(data_points, range_val)
            if dpm_at_range > 0:
                unit_dpm_at_range.append((unit_name, dpm_at_range))
        
        # Sort by DPM (highest first)
        unit_dpm_at_range.sort(key=lambda x: x[1], reverse=True)
        
        # Display each unit's information
        for unit_name, total_dpm in unit_dpm_at_range:
            info_lines.append(f"{unit_name}")
            info_lines.append(f"  Total DPM: {total_dpm:.2f}")
            info_lines.append("")
            
            # Add weapon breakdown for this unit
            if unit_name in self.weapon_dpm_data:
                info_lines.append("  Weapon Breakdown:")
                weapon_data = self.weapon_dpm_data[unit_name]
                for weapon_name, weapon_info in weapon_data.items():
                    weapon_dpm = self._get_dpm_at_range(weapon_info["dpm_data"], range_val)
                    if weapon_dpm > 0:
                        quantity = weapon_info["quantity"]
                        per_weapon_dpm = weapon_dpm / quantity if quantity > 0 else 0
                        shots_per_min = weapon_info.get("shots_per_minute", 0.0)
                        ammo_per_min = weapon_info.get("ammo_consumption_per_minute", 0.0)
                        
                        # Calculate accuracy at this range
                        accuracy = 0.0
                        if "ammo_props" in weapon_info:
                            ammo_props = weapon_info["ammo_props"]
                            base_accuracy = ammo_props.get("idling", 0.0)
                            max_range = ammo_props.get("max_range", 0.0)
                            veterancy_level = weapon_info.get("veterancy_level", 0)
                            veterancy_accuracy_bonus = weapon_info.get("veterancy_accuracy_bonus", 0.0)
                            
                            if max_range > 0:
                                accuracy = calculate_accuracy(
                                    range_val,
                                    max_range,
                                    base_accuracy,
                                    self.successive_hits,
                                    veterancy_level,
                                    veterancy_accuracy_bonus,
                                    self.get_current_range_modifier_table(),
                                    use_multiplicative_vet_bonus=self.app.range_modifier_vet_bonus_type.get(
                                        self.app.current_range_modifier_table_name, True
                                    )
                                )
                        
                        # Get additional weapon stats from ammo_props
                        ammo_props_for_stats = weapon_info.get("ammo_props", {})
                        salvo_reload = ammo_props_for_stats.get("time_between_salvos", 0.0)
                        shot_reload = ammo_props_for_stats.get("time_between_shots", None)
                        shots_per_salvo = ammo_props_for_stats.get("nb_tir_par_salves", 1)
                        physical_damage = ammo_props_for_stats.get("physical_damages", 0.0)
                        per_weapon_damage = physical_damage  # Physical damage is per weapon
                        total_damage = physical_damage * quantity if quantity > 0 else 0.0
                        
                        info_lines.append(f"    {weapon_name}:")
                        info_lines.append(f"      DPM: {weapon_dpm:.2f} ({per_weapon_dpm:.2f} per weapon)")
                        info_lines.append(f"      Physical Damage: {total_damage:.2f} ({per_weapon_damage:.2f} per weapon)")
                        info_lines.append(f"      Base Accuracy: {base_accuracy * 100:.1f}%")
                        info_lines.append(f"      Accuracy: {accuracy * 100:.1f}%")
                        info_lines.append(f"      Shots/min: {shots_per_min:.1f} (per weapon)")
                        info_lines.append(f"      Ammo/min: {ammo_per_min:.1f} (per weapon)")
                        info_lines.append(f"      Shots per Salvo: {shots_per_salvo}")
                        info_lines.append(f"      Salvo Reload: {salvo_reload:.2f}s")
                        if shot_reload is not None:
                            info_lines.append(f"      Shot Reload: {shot_reload:.2f}s")
                        else:
                            info_lines.append(f"      Shot Reload: N/A")
                
                info_lines.append("")
        
        info_lines.append("─" * 40)
        info_lines.append("")
        info_lines.append("Click on a data point to select it.")
        info_lines.append("Click again to deselect.")
        
        # Update info panel
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete('1.0', tk.END)
        self.info_text.insert('1.0', '\n'.join(info_lines))
        self.info_text.config(state=tk.DISABLED)
        # Scroll to top
        self.info_text.see('1.0')
    
    def _update_info_panel_with_veterancy_only(self):
        """Update info panel to show only veterancy bonuses."""
        self.info_text.config(state=tk.NORMAL)
        self.info_text.delete('1.0', tk.END)
        if hasattr(self, 'current_veterancy_info') and self.current_veterancy_info:
            self.info_text.insert('1.0', self.current_veterancy_info + '\n\n')
            self.info_text.insert(tk.END, '─' * 40 + '\n\n')
            self.info_text.insert(tk.END, 'Click on a data point to select it\nand see all units at that range.')
        else:
            self.info_text.insert('1.0', 'Click on a data point to select it\nand see all units at that range.')
        self.info_text.config(state=tk.DISABLED)
        self.info_text.see('1.0')
    
    def load_user_data(self):
        """Load user data from JSON file (range modifier tables, custom units, custom weapons)."""
        # Try loading from new consolidated file first
        if self.app.user_data_file.exists():
            try:
                with open(self.app.user_data_file, 'r') as f:
                    data = json.load(f)
                    
                    # Load range modifier tables
                    if "range_modifier_tables" in data:
                        for name, table in data["range_modifier_tables"].items():
                            if name != "vanilla":  # Don't overwrite vanilla
                                self.app.range_modifier_tables[name] = [tuple(row) for row in table]
                    if "current_range_modifier_table" in data:
                        if data["current_range_modifier_table"] in self.app.range_modifier_tables:
                            self.app.current_range_modifier_table_name = data["current_range_modifier_table"]
                    
                    # Store custom units data for later loading (after dataset cache loads)
                    self._pending_custom_units = {}
                    if "custom_units" in data:
                        for unit_name, unit_info in data["custom_units"].items():
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
                            # Also add immediately if infantry_units is already populated
                            if hasattr(self, 'infantry_units') and self.app.infantry_units:
                                self.app.infantry_units[unit_name] = unit_info
                    
                    # Load custom weapons
                    if "custom_weapons" in data:
                        self.app.custom_weapons.update(data["custom_weapons"])
                        # Update custom weapon dropdowns if UI is set up
                        if hasattr(self, 'update_custom_weapon_dropdowns'):
                            self.update_custom_weapon_dropdowns()
                        
            except Exception as e:
                print(f"Error loading user data: {e}")
    
    def reload_custom_units_after_cache(self):
        """Reload custom units from pending data after dataset cache has loaded."""
        if hasattr(self, '_pending_custom_units') and self._pending_custom_units:
            # Add custom units to infantry_units
            for unit_name, unit_info in self._pending_custom_units.items():
                self.app.infantry_units[unit_name] = unit_info
            
            # Update unit dropdowns
            if hasattr(self, 'unit_display_names'):
                self.unit_display_names = []
                for name in sorted(self.app.infantry_units.keys()):
                    self.unit_display_names.append(name)
                
                # Update all existing dropdowns
                if hasattr(self, 'unit_dropdowns'):
                    for dropdown in self.unit_dropdowns:
                        if isinstance(dropdown, SearchableCombobox):
                            dropdown.set_values(self.unit_display_names)
                
                # Update load unit dropdown
                if hasattr(self, 'load_unit_combo'):
                    self.load_unit_combo.set_values(self.unit_display_names)
    
    def save_user_data(self):
        """Save user data to JSON file (range modifier tables, custom units, custom weapons)."""
        try:
            data = {
                "current_range_modifier_table": self.app.current_range_modifier_table_name,
                "range_modifier_tables": {},
                "custom_units": {},
                "custom_weapons": self.app.custom_weapons.copy(),
            }
            
            # Convert range modifier tables tuples to lists for JSON serialization
            for name, table in self.app.range_modifier_tables.items():
                data["range_modifier_tables"][name] = [list(row) for row in table]
            
            # Save custom units (only those marked as custom_unit)
            for unit_name, unit_info in self.app.infantry_units.items():
                if unit_info.get("custom_unit", False):
                    data["custom_units"][unit_name] = unit_info.copy()
            
            with open(self.app.user_data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save user data: {e}")
    
    def open_range_modifier_editor(self):
        """Open the range modifier table editor window."""
        editor = RangeModifierEditor(self.app.root, self.app)
        self.app.root.wait_window(editor.window)
        # After editor closes, regenerate chart if needed
        if hasattr(self, 'ax') and self.ax.lines:
            self.generate_chart()
    
    def get_current_range_modifier_table(self) -> List[Tuple[float, float]]:
        """Get the currently selected range modifier table."""
        return self.app.range_modifier_tables.get(self.app.current_range_modifier_table_name, RANGE_MODIFIERS_TABLE)
    
    def export_chart(self):
        """Export chart as PNG."""
        if not self.ax.lines:
            messagebox.showwarning("Warning", "Please generate a chart first")
            return
        
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                self.fig.savefig(filename, dpi=150, bbox_inches='tight')
                messagebox.showinfo("Success", f"Chart exported to {filename}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to export chart: {e}")

