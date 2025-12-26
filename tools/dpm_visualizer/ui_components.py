"""UI Components for DPM Visualizer."""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import List, Optional, Tuple


class SearchableCombobox(ttk.Frame):
    """A searchable combobox using Entry + Listbox that stays open while typing."""
    
    # Class-level registry to track all instances
    _instances = []
    
    def __init__(self, parent, values=None, width=25, **kwargs):
        super().__init__(parent)
        self.values = values or []
        self._original_values = self.values.copy()
        
        self.var = tk.StringVar()
        self.entry = ttk.Entry(self, textvariable=self.var, width=width)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.dropdown_btn = ttk.Button(self, text="▼", width=3, command=self.toggle_dropdown)
        self.dropdown_btn.pack(side=tk.RIGHT)
        
        # Create popup window for dropdown
        self.popup = None
        self.listbox = None
        self.is_open = False
        self._just_selected = False  # Flag to prevent closing immediately after selection
        
        # Register this instance
        SearchableCombobox._instances.append(self)
        
        # Bind events
        self.entry.bind('<KeyRelease>', self.on_key_release)
        self.entry.bind('<FocusIn>', self.on_focus_in)
        self.entry.bind('<Button-1>', lambda e: self.show_dropdown())
    
    @classmethod
    def close_all_dropdowns(cls):
        """Close all open dropdowns across all instances."""
        for instance in cls._instances:
            if instance.is_open:
                instance.hide_dropdown()
    
    def destroy(self):
        """Clean up when widget is destroyed."""
        if self in SearchableCombobox._instances:
            SearchableCombobox._instances.remove(self)
        if self.popup:
            self.popup.destroy()
        super().destroy()
    
    def set_values(self, values):
        """Update the values list."""
        self._original_values = values.copy()
        self.values = values.copy()
        if self.listbox:
            self.update_listbox()
    
    def get(self):
        """Get the current selected value."""
        return self.var.get()
    
    def set(self, value):
        """Set the current selected value."""
        self.var.set(value)
    
    def on_key_release(self, event):
        """Handle key release for filtering."""
        current_text = self.var.get().lower()
        if not current_text:
            self.values = self._original_values.copy()
        else:
            self.values = [v for v in self._original_values if current_text in v.lower()]
        
        if self.is_open:
            self.update_listbox()
        elif event.keysym not in ['Return', 'Tab', 'Escape']:
            # Show dropdown when typing (except for navigation keys)
            self.show_dropdown()
    
    def on_focus_in(self, event):
        """Update values when entry gets focus."""
        if hasattr(self, '_parent_app') and hasattr(self._parent_app, 'unit_display_names'):
            self._original_values = self._parent_app.unit_display_names.copy()
            if not self.var.get():
                self.values = self._original_values.copy()
                if self.listbox:
                    self.update_listbox()
    
    def toggle_dropdown(self):
        """Toggle dropdown visibility."""
        if self.is_open:
            self.hide_dropdown()
        else:
            self.show_dropdown()
    
    def show_dropdown(self):
        """Show the dropdown listbox."""
        if not self.values:
            return
        
        # Get root window for proper parent binding
        root = self.winfo_toplevel()
        
        # Create popup window if it doesn't exist
        if not self.popup:
            self.popup = tk.Toplevel(root)
            self.popup.overrideredirect(True)
            self.popup.attributes('-topmost', True)
            
            # Create listbox with scrollbar
            list_frame = ttk.Frame(self.popup)
            list_frame.pack(fill=tk.BOTH, expand=True)
            
            scrollbar = ttk.Scrollbar(list_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=min(10, len(self.values)))
            self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.config(command=self.listbox.yview)
            
            # Make listbox focusable
            self.listbox.config(takefocus=True)
            
            # Bind listbox events
            self.listbox.bind('<Button-1>', self.on_listbox_select)
            self.listbox.bind('<Double-Button-1>', self.on_listbox_double_click)
            
            # Don't rely on FocusOut for closing - it fires when mouse enters listbox
            # Instead, we'll rely on tab switching and window focus loss (handled in main.py)
            # and a root click handler for clicking outside
        
        # Bind to root window to detect clicks outside (only once per root)
        # Use ButtonRelease-1 which fires AFTER Button-1, so listbox clicks process first
        root = self.winfo_toplevel()
        if not hasattr(SearchableCombobox, '_root_click_bound'):
            def on_root_release(event):
                # Store event data for delayed check
                root_x = event.x_root
                root_y = event.y_root
                clicked_widget = event.widget
                
                # Schedule check after delay to let listbox selection process
                def delayed_check():
                    for instance in SearchableCombobox._instances:
                        if instance.is_open and instance.popup:
                            # Don't close if a selection was just made
                            if getattr(instance, '_just_selected', False):
                                continue
                            
                            # Check if clicked widget is part of this dropdown
                            widget = clicked_widget
                            is_part_of_dropdown = False
                            
                            # Walk up widget tree to see if click was on dropdown
                            while widget:
                                if widget == instance.popup or widget == instance.listbox or widget == instance.entry or widget == instance.dropdown_btn or widget == instance:
                                    is_part_of_dropdown = True
                                    break
                                # Check if widget is a child of popup
                                try:
                                    parent = widget.master
                                    while parent:
                                        if parent == instance.popup:
                                            is_part_of_dropdown = True
                                            break
                                        try:
                                            parent = parent.master
                                        except:
                                            break
                                    if is_part_of_dropdown:
                                        break
                                except:
                                    pass
                                try:
                                    widget = widget.master
                                    if widget is None:
                                        break
                                except:
                                    break
                            
                            # Only close if click was definitely outside
                            if not is_part_of_dropdown:
                                try:
                                    # Double-check with coordinates
                                    popup_x = instance.popup.winfo_x()
                                    popup_y = instance.popup.winfo_y()
                                    popup_width = instance.popup.winfo_width()
                                    popup_height = instance.popup.winfo_height()
                                    
                                    in_popup = (popup_x <= root_x <= popup_x + popup_width and 
                                               popup_y <= root_y <= popup_y + popup_height)
                                    
                                    entry_x = instance.winfo_rootx()
                                    entry_y = instance.winfo_rooty()
                                    entry_width = instance.winfo_width()
                                    entry_height = instance.winfo_height()
                                    
                                    in_entry = (entry_x <= root_x <= entry_x + entry_width and 
                                               entry_y <= root_y <= entry_y + entry_height)
                                    
                                    if not in_popup and not in_entry:
                                        instance.hide_dropdown()
                                except:
                                    pass
                
                # Delay to allow listbox selection to process
                root.after(200, delayed_check)
            
            root.bind('<ButtonRelease-1>', on_root_release, add='+')
            SearchableCombobox._root_click_bound = True
        
        # Bind to root window movement to update popup position (only if not already bound)
        if not hasattr(self, '_move_binding_active'):
            root.bind('<Configure>', self._on_root_configure, add='+')
            self._move_binding_active = True
        
        self.update_listbox()
        self.position_popup()
        self.popup.deiconify()
        self.is_open = True
        # Don't set focus on popup - let listbox receive focus naturally
        # This prevents immediate FocusOut from closing the dropdown
    
    def _on_root_configure(self, event):
        """Handle root window movement - update popup position."""
        # Only update if this is the root window being moved (not child widgets)
        if event.widget == self.winfo_toplevel() and self.is_open and self.popup:
            try:
                self.position_popup()
            except:
                # Widget may have been destroyed
                pass
    
    
    def check_close(self):
        """Check if we should close the dropdown."""
        try:
            # Don't close if a selection was just made
            if getattr(self, '_just_selected', False):
                return
            focus = self.focus_get()
            if focus not in [self.entry, self.popup, self.listbox]:
                self.hide_dropdown()
        except:
            pass
    
    def check_close_entry(self):
        """Check if we should close the dropdown when entry loses focus."""
        try:
            # Don't close if a selection was just made
            if getattr(self, '_just_selected', False):
                return
            focus = self.focus_get()
            # Only close if focus is not on popup or listbox
            if focus not in [self.popup, self.listbox]:
                self.hide_dropdown()
        except:
            pass
    
    def update_listbox(self):
        """Update listbox with filtered values."""
        if not self.listbox:
            return
        
        self.listbox.delete(0, tk.END)
        for value in self.values:
            self.listbox.insert(tk.END, value)
        
        # Update height
        self.listbox.config(height=min(10, len(self.values)))
    
    def position_popup(self):
        """Position the popup below the entry."""
        self.update_idletasks()
        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.winfo_height()
        width = max(self.winfo_width(), 200)
        
        height = min(200, len(self.values) * 20 + 10)
        self.popup.geometry(f"{width}x{height}")
        self.popup.geometry(f"+{x}+{y}")
    
    def hide_dropdown(self):
        """Hide the dropdown."""
        if self.popup:
            self.popup.withdraw()
        self.is_open = False
        
        # Note: We keep the binding active so popup follows window movement
        # The binding checks if popup is open before updating position
    
    def on_listbox_select(self, event):
        """Handle listbox selection."""
        # Set flag immediately to prevent root click handler from closing
        self._just_selected = True
        
        # Process selection after a small delay to ensure listbox updates
        def process_selection():
            selection = self.listbox.curselection()
            if selection:
                value = self.listbox.get(selection[0])
                self.var.set(value)
                # Hide dropdown
                self.hide_dropdown()
                # Clear flag after hiding
                self.after(50, lambda: setattr(self, '_just_selected', False))
                # Trigger selection event
                self.event_generate('<<ComboboxSelected>>')
            else:
                # No selection made, clear flag
                self._just_selected = False
        
        self.after(10, process_selection)
    
    def on_listbox_double_click(self, event):
        """Handle double click on listbox."""
        self.on_listbox_select(event)


class RangeModifierEditor:
    """Window for editing range modifier tables."""
    
    def __init__(self, parent: tk.Tk, app):
        self.parent = parent
        self.app = app
        self.window = tk.Toplevel(parent)
        self.window.title("Range Modifier Tables Editor")
        self.window.geometry("600x500")
        
        # Store current editing state
        self.current_table_name = app.current_range_modifier_table_name
        self.table_entries = []  # List of (range_var, multiplier_var) tuples
        
        self.setup_ui()
        # Initialize checkbox after UI is set up
        # Default to False for vanilla, True for others
        default_value = False if self.current_table_name == "vanilla" else True
        use_multiplicative = self.app.range_modifier_vet_bonus_type.get(self.current_table_name, default_value)
        self.vet_bonus_multiplicative_var.set(use_multiplicative)
        self.load_table(self.current_table_name)
    
    def setup_ui(self):
        """Set up the editor UI."""
        main_frame = ttk.Frame(self.window, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Table selection
        selection_frame = ttk.LabelFrame(main_frame, text="Select Table", padding="5")
        selection_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(selection_frame, text="Table Name:").pack(side=tk.LEFT, padx=5)
        self.table_combo = ttk.Combobox(selection_frame, width=30, state="readonly")
        self.table_combo.pack(side=tk.LEFT, padx=5)
        self.table_combo.bind("<<ComboboxSelected>>", self.on_table_selected)
        self.update_table_list()
        
        ttk.Button(selection_frame, text="New Table", command=self.create_new_table).pack(side=tk.LEFT, padx=5)
        ttk.Button(selection_frame, text="Delete Table", command=self.delete_table).pack(side=tk.LEFT, padx=5)
        
        # Table editor (6 rows fixed)
        editor_frame = ttk.LabelFrame(main_frame, text="Range Modifier Table (6 rows)", padding="5")
        editor_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Header
        header_frame = ttk.Frame(editor_frame)
        header_frame.pack(fill=tk.X, pady=(0, 5))
        ttk.Label(header_frame, text="Range Fraction", width=15).pack(side=tk.LEFT, padx=5)
        ttk.Label(header_frame, text="Multiplier", width=15).pack(side=tk.LEFT, padx=5)
        
        # Veterancy bonus type checkbox
        vet_bonus_frame = ttk.LabelFrame(main_frame, text="Veterancy Accuracy Bonus", padding="5")
        vet_bonus_frame.pack(fill=tk.X, pady=(0, 10))
        self.vet_bonus_multiplicative_var = tk.BooleanVar()
        vet_bonus_checkbox = ttk.Checkbutton(
            vet_bonus_frame,
            text="Use multiplicative veterancy bonus (unchecked = flat bonus)",
            variable=self.vet_bonus_multiplicative_var,
            command=self.on_vet_bonus_type_changed
        )
        vet_bonus_checkbox.pack(side=tk.LEFT, padx=5)
        
        # Create 6 rows
        self.table_entries = []
        for i in range(6):
            row_frame = ttk.Frame(editor_frame)
            row_frame.pack(fill=tk.X, pady=2)
            
            ttk.Label(row_frame, text=f"Row {i+1}:", width=8).pack(side=tk.LEFT, padx=5)
            
            range_var = tk.StringVar()
            range_entry = ttk.Entry(row_frame, textvariable=range_var, width=15)
            range_entry.pack(side=tk.LEFT, padx=5)
            
            multiplier_var = tk.StringVar()
            multiplier_entry = ttk.Entry(row_frame, textvariable=multiplier_var, width=15)
            multiplier_entry.pack(side=tk.LEFT, padx=5)
            
            self.table_entries.append((range_var, multiplier_var))
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X)
        
        ttk.Button(button_frame, text="Apply", command=self.apply_table).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Save", command=self.save_table).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Close", command=self.window.destroy).pack(side=tk.RIGHT, padx=5)
    
    def update_table_list(self):
        """Update the table selection combobox."""
        table_names = list(self.app.range_modifier_tables.keys())
        self.table_combo['values'] = table_names
        if self.current_table_name in table_names:
            self.table_combo.set(self.current_table_name)
    
    def load_table(self, table_name: str):
        """Load a table into the editor."""
        if table_name not in self.app.range_modifier_tables:
            return
        
        table = self.app.range_modifier_tables[table_name]
        self.current_table_name = table_name
        
        # Load veterancy bonus type flag
        # Default to False for vanilla, True for others
        default_value = False if table_name == "vanilla" else True
        use_multiplicative = self.app.range_modifier_vet_bonus_type.get(table_name, default_value)
        if hasattr(self, 'vet_bonus_multiplicative_var'):
            self.vet_bonus_multiplicative_var.set(use_multiplicative)
        
        # Fill entries (pad with empty rows if table has fewer than 6 rows)
        for i in range(6):
            range_var, multiplier_var = self.table_entries[i]
            if i < len(table):
                range_var.set(str(table[i][0]))
                multiplier_var.set(str(table[i][1]))
            else:
                range_var.set("")
                multiplier_var.set("")
    
    def on_table_selected(self, event=None):
        """Handle table selection change."""
        selected = self.table_combo.get()
        if selected:
            self.load_table(selected)
    
    def on_vet_bonus_type_changed(self):
        """Handle veterancy bonus type checkbox change - save immediately."""
        if hasattr(self, 'current_table_name') and self.current_table_name:
            self.app.range_modifier_vet_bonus_type[self.current_table_name] = self.vet_bonus_multiplicative_var.get()
    
    def create_new_table(self):
        """Create a new table."""
        dialog = tk.Toplevel(self.window)
        dialog.title("New Table")
        dialog.geometry("300x100")
        dialog.transient(self.window)
        dialog.grab_set()
        
        ttk.Label(dialog, text="Table Name:").pack(pady=10)
        name_var = tk.StringVar()
        name_entry = ttk.Entry(dialog, textvariable=name_var, width=30)
        name_entry.pack(pady=5)
        name_entry.focus()
        
        def create():
            name = name_var.get().strip()
            if not name:
                messagebox.showwarning("Warning", "Please enter a table name")
                return
            if name in self.app.range_modifier_tables:
                messagebox.showwarning("Warning", "A table with this name already exists")
                return
            
            # Create new table with default values (copy from vanilla)
            self.app.range_modifier_tables[name] = self.app.range_modifier_tables["vanilla"].copy()
            # Default new tables to multiplicative (can be changed)
            self.app.range_modifier_vet_bonus_type[name] = True
            self.update_table_list()
            self.table_combo.set(name)
            self.load_table(name)
            dialog.destroy()
        
        ttk.Button(dialog, text="Create", command=create).pack(pady=5)
        name_entry.bind('<Return>', lambda e: create())
    
    def delete_table(self):
        """Delete the current table."""
        if self.current_table_name == "vanilla":
            messagebox.showwarning("Warning", "Cannot delete the 'vanilla' table")
            return
        
        if messagebox.askyesno("Confirm", f"Delete table '{self.current_table_name}'?"):
            del self.app.range_modifier_tables[self.current_table_name]
            if self.app.current_range_modifier_table_name == self.current_table_name:
                self.app.current_range_modifier_table_name = "vanilla"
            self.current_table_name = "vanilla"
            self.update_table_list()
            self.load_table("vanilla")
    
    def apply_table(self):
        """Apply the current table to the app."""
        table = self.get_table_from_entries()
        if table is None:
            return
        
        self.app.range_modifier_tables[self.current_table_name] = table
        # Save veterancy bonus type flag
        if hasattr(self, 'vet_bonus_multiplicative_var'):
            self.app.range_modifier_vet_bonus_type[self.current_table_name] = self.vet_bonus_multiplicative_var.get()
        self.app.current_range_modifier_table_name = self.current_table_name
        
        # Save user data - try tab's save_user_data first, then app's
        if hasattr(self.app, 'infantry_tab') and hasattr(self.app.infantry_tab, 'save_user_data'):
            self.app.infantry_tab.save_user_data()
        elif hasattr(self.app, 'save_user_data'):
            self.app.save_user_data()
        
        # Regenerate chart if it exists (check both tabs)
        if hasattr(self.app, 'infantry_tab') and hasattr(self.app.infantry_tab, 'generate_chart'):
            if hasattr(self.app.infantry_tab, 'ax') and self.app.infantry_tab.ax.lines:
                self.app.infantry_tab.generate_chart()
        if hasattr(self.app, 'weapons_tab') and hasattr(self.app.weapons_tab, 'generate_chart'):
            if hasattr(self.app.weapons_tab, 'ax') and self.app.weapons_tab.ax.lines:
                self.app.weapons_tab.generate_chart()
        
        messagebox.showinfo("Success", f"Table '{self.current_table_name}' applied successfully")
    
    def save_table(self):
        """Save the current table."""
        table = self.get_table_from_entries()
        if table is None:
            return
        
        self.app.range_modifier_tables[self.current_table_name] = table
        # Save veterancy bonus type flag
        self.app.range_modifier_vet_bonus_type[self.current_table_name] = self.vet_bonus_multiplicative_var.get()
        
        # Save user data - try tab's save_user_data first, then app's
        if hasattr(self.app, 'infantry_tab') and hasattr(self.app.infantry_tab, 'save_user_data'):
            self.app.infantry_tab.save_user_data()
        elif hasattr(self.app, 'save_user_data'):
            self.app.save_user_data()
        
        messagebox.showinfo("Success", f"Table '{self.current_table_name}' saved successfully")
    
    def get_table_from_entries(self) -> Optional[List[Tuple[float, float]]]:
        """Get table data from entry fields."""
        table = []
        for i, (range_var, multiplier_var) in enumerate(self.table_entries):
            range_str = range_var.get().strip()
            multiplier_str = multiplier_var.get().strip()
            
            if not range_str or not multiplier_str:
                messagebox.showerror("Error", f"Row {i+1} is incomplete. Please fill all fields.")
                return None
            
            try:
                range_val = float(range_str)
                multiplier_val = float(multiplier_str)
                
                if range_val < 0 or range_val > 1.0:
                    messagebox.showerror("Error", f"Row {i+1}: Range fraction must be between 0 and 1.0")
                    return None
                
                table.append((range_val, multiplier_val))
            except ValueError:
                messagebox.showerror("Error", f"Row {i+1}: Invalid number format")
                return None
        
        # Validate that ranges are in ascending order
        for i in range(len(table) - 1):
            if table[i][0] >= table[i + 1][0]:
                messagebox.showerror("Error", f"Range fractions must be in ascending order. Row {i+1} >= Row {i+2}")
                return None
        
        # Validate that last row has range fraction 1.0
        if table[-1][0] != 1.0:
            messagebox.showerror("Error", "Last row must have range fraction of 1.0")
            return None
        
        return table

