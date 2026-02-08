"""Main application entry point for FX Editor."""

import re
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add project root to path for imports (same as dpm_visualizer)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .ndf_access import parse_ndf_file, write_ndf_file, get_export_row, update_namespace
from .model_index import build_tree, TreeNode
from .size_batch import find_fx_files, process_file
from .preview_window import PreviewWindow
from .ui_components import format_value, parse_value_input


class FXEditorApp:
    """Main application class for FX Editor."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title('FX Editor')
        self.root.geometry('1200x800')

        self.current_file: Optional[Path] = None
        self.parsed_root: Optional[ndf.model.List] = None
        self.tree_nodes: Dict[str, TreeNode] = {}
        self.tree_item_refs: Dict[str, TreeNode] = {}
        self.property_refs: Dict[str, Any] = {}

        self.setup_ui()

    def setup_ui(self) -> None:
        main_frame = ttk.Frame(self.root, padding='10')
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.editor_tab = ttk.Frame(self.notebook)
        self.batch_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.editor_tab, text='Editor')
        self.notebook.add(self.batch_tab, text='Batch Size')

        self.setup_editor_tab()
        self.setup_batch_tab()

    def setup_editor_tab(self) -> None:
        top_frame = ttk.LabelFrame(self.editor_tab, text='FX File', padding='10')
        top_frame.pack(fill=tk.X, padx=10, pady=10)

        self.file_var = tk.StringVar()
        ttk.Entry(top_frame, textvariable=self.file_var, width=80).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(top_frame, text='Browse', command=self.browse_file).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(top_frame, text='Load', command=self.load_file).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(top_frame, text='Save', command=self.save_file).pack(side=tk.LEFT, padx=(5, 0))
        
        # Add namespace update button
        namespace_frame = ttk.Frame(top_frame)
        namespace_frame.pack(side=tk.LEFT, padx=(10, 0))
        ttk.Button(namespace_frame, text='Update Namespace', command=self.manual_namespace_update).pack()

        paned = ttk.PanedWindow(self.editor_tab, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        left_frame = ttk.LabelFrame(paned, text='Structure', padding='5')
        right_frame = ttk.LabelFrame(paned, text='Properties', padding='5')
        paned.add(left_frame, weight=1)
        paned.add(right_frame, weight=2)

        tree_frame = ttk.Frame(left_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode=tk.BROWSE)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tree_scroll.config(command=self.tree.yview)
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

        props_frame = ttk.Frame(right_frame)
        props_frame.pack(fill=tk.BOTH, expand=True)
        props_scroll = ttk.Scrollbar(props_frame)
        props_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.properties_tree = ttk.Treeview(
            props_frame,
            columns=('value',),
            show='tree headings',
            yscrollcommand=props_scroll.set,
            selectmode=tk.BROWSE,
        )
        self.properties_tree.heading('#0', text='Name')
        self.properties_tree.heading('value', text='Value')
        self.properties_tree.column('value', width=400)
        self.properties_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        props_scroll.config(command=self.properties_tree.yview)
        self.properties_tree.bind('<<TreeviewSelect>>', self.on_property_select)

        edit_frame = ttk.Frame(right_frame)
        edit_frame.pack(fill=tk.X, pady=(5, 0))
        ttk.Label(edit_frame, text='New Value:').pack(side=tk.LEFT, padx=(0, 5))
        self.value_var = tk.StringVar()
        ttk.Entry(edit_frame, textvariable=self.value_var, width=60).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(edit_frame, text='Apply', command=self.apply_property_value).pack(side=tk.LEFT, padx=(5, 0))

        self.property_info = ttk.Label(right_frame, text='Select a node to view properties.')
        self.property_info.pack(fill=tk.X, pady=(5, 0))

    def setup_batch_tab(self) -> None:
        main_frame = ttk.Frame(self.batch_tab, padding='10')
        main_frame.pack(fill=tk.BOTH, expand=True)

        dir_frame = ttk.LabelFrame(main_frame, text='Directory', padding='10')
        dir_frame.pack(fill=tk.X, pady=(0, 10))

        self.dir_var = tk.StringVar()
        ttk.Entry(dir_frame, textvariable=self.dir_var, width=60).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(dir_frame, text='Browse Dir', command=self.browse_directory).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(dir_frame, text='Browse Files', command=self.browse_files).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(dir_frame, text='Load Files', command=self.load_files).pack(side=tk.LEFT, padx=(5, 0))

        file_frame = ttk.LabelFrame(main_frame, text='Files', padding='10')
        file_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        listbox_frame = ttk.Frame(file_frame)
        listbox_frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(listbox_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.file_listbox = tk.Listbox(
            listbox_frame,
            selectmode=tk.EXTENDED,
            yscrollcommand=scrollbar.set,
        )
        self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.file_listbox.yview)

        file_buttons_frame = ttk.Frame(file_frame)
        file_buttons_frame.pack(fill=tk.X, pady=(5, 0))
        ttk.Button(file_buttons_frame, text='Select All', command=self.select_all_files).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(file_buttons_frame, text='Clear Selection', command=self.clear_selection).pack(side=tk.LEFT)

        scale_frame = ttk.LabelFrame(main_frame, text='Scale Factor', padding='10')
        scale_frame.pack(fill=tk.X, pady=(0, 10))

        scale_input_frame = ttk.Frame(scale_frame)
        scale_input_frame.pack(fill=tk.X)
        ttk.Label(scale_input_frame, text='Percentage:').pack(side=tk.LEFT, padx=(0, 5))

        self.percentage_var = tk.DoubleVar(value=100.0)
        percentage_spinbox = ttk.Spinbox(
            scale_input_frame,
            from_=1.0,
            to=1000.0,
            increment=1.0,
            textvariable=self.percentage_var,
            width=10,
            command=self.update_scale_factor,
        )
        percentage_spinbox.pack(side=tk.LEFT, padx=(0, 5))
        percentage_spinbox.bind('<KeyRelease>', lambda e: self.update_scale_factor())
        ttk.Label(scale_input_frame, text='%').pack(side=tk.LEFT, padx=(0, 10))

        self.scale_factor = 1.0
        self.scale_factor_label = ttk.Label(scale_input_frame, text='Scale factor: 1.0x')
        self.scale_factor_label.pack(side=tk.LEFT)

        quick_scale_frame = ttk.Frame(scale_frame)
        quick_scale_frame.pack(fill=tk.X, pady=(5, 0))
        ttk.Label(quick_scale_frame, text='Quick scale:').pack(side=tk.LEFT, padx=(0, 5))
        for percentage in [50, 75, 100, 125, 150, 200]:
            ttk.Button(
                quick_scale_frame,
                text=f'{percentage}%',
                width=6,
                command=lambda p=percentage: self.set_percentage(p),
            ).pack(side=tk.LEFT, padx=2)

        action_frame = ttk.Frame(main_frame)
        action_frame.pack(fill=tk.X, pady=(0, 10))
        ttk.Button(action_frame, text='Preview Changes', command=self.preview_changes).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(action_frame, text='Apply Changes', command=self.apply_changes).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(action_frame, text='Update Namespaces', command=self.batch_update_namespaces).pack(side=tk.LEFT)

        results_frame = ttk.LabelFrame(main_frame, text='Results', padding='10')
        results_frame.pack(fill=tk.BOTH, expand=True)
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            height=10,
            wrap=tk.WORD,
            state=tk.DISABLED,
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)
        self.update_scale_factor()

    def browse_file(self) -> None:
        file_path = filedialog.askopenfilename(
            title='Select FX NDF File',
            filetypes=[('NDF Files', '*.ndf')],
        )
        if file_path:
            self.file_var.set(file_path)

    def load_file(self) -> None:
        file_path = Path(self.file_var.get())
        if not file_path.exists():
            messagebox.showerror('Error', f'File does not exist:\n{file_path}')
            return
        try:
            self.parsed_root = parse_ndf_file(file_path)
            self.current_file = file_path
            # Always prompt for namespace update
            self.prompt_namespace_on_load()
            self.refresh_tree()
        except Exception as exc:
            messagebox.showerror('Parse Error', str(exc))

    def save_file(self) -> None:
        if not self.current_file or not self.parsed_root:
            messagebox.showwarning('No File', 'Load a file before saving.')
            return
        try:
            write_ndf_file(self.current_file, self.parsed_root)
            messagebox.showinfo('Saved', f'Saved changes to:\n{self.current_file}')
        except Exception as exc:
            messagebox.showerror('Save Error', str(exc))

    def refresh_tree(self, select_ref: Optional[Any] = None) -> None:
        self.tree.delete(*self.tree.get_children())
        self.tree_item_refs = {}
        self.tree_nodes = {}

        if not self.parsed_root:
            return

        root_node, node_map = build_tree(self.parsed_root)
        self.tree_nodes = node_map

        def add_tree_node(parent_item: str, node_id: str, depth: int) -> None:
            node = node_map[node_id]
            item = self.tree.insert(
                parent_item,
                'end',
                text=node.label,
                open=(depth < 2),
            )
            self.tree_item_refs[item] = node
            for child_id in node.children:
                add_tree_node(item, child_id, depth + 1)

        add_tree_node('', root_node.node_id, 0)

        if select_ref is not None:
            for item_id, node in self.tree_item_refs.items():
                if node.ref is select_ref:
                    self.tree.selection_set(item_id)
                    self.tree.see(item_id)
                    break

    def on_tree_select(self, event: Any) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        node = self.tree_item_refs.get(selection[0])
        if not node:
            return
        self.populate_properties(node)

    def populate_properties(self, node: TreeNode) -> None:
        self.properties_tree.delete(*self.properties_tree.get_children())
        self.property_refs = {}

        ref = node.ref
        title = f'Properties for {node.label}'

        if isinstance(ref, ndf.model.Object):
            for member_row in ref:
                value_text = format_value(member_row.v)
                item = self.properties_tree.insert('', 'end', text=member_row.member or '(unnamed)', values=(value_text,))
                self.property_refs[item] = member_row
        elif isinstance(ref, ndf.model.Map):
            for map_row in ref:
                key = strip_quotes(str(map_row.k)) if map_row.k is not None else '(nil)'
                value_text = format_value(map_row.v)
                item = self.properties_tree.insert('', 'end', text=key, values=(value_text,))
                self.property_refs[item] = map_row
        elif isinstance(ref, ndf.model.List):
            for idx, list_row in enumerate(ref):
                label = list_row.namespace or f'[{idx}]'
                value_text = format_value(list_row.v)
                item = self.properties_tree.insert('', 'end', text=label, values=(value_text,))
                self.property_refs[item] = list_row
        elif isinstance(ref, (ndf.model.MemberRow, ndf.model.MapRow, ndf.model.ListRow)):
            value_text = format_value(ref.v)
            label = '(value)'
            if isinstance(ref, ndf.model.MemberRow):
                label = ref.member or '(unnamed)'
            if isinstance(ref, ndf.model.MapRow):
                label = strip_quotes(str(ref.k)) if ref.k is not None else '(nil)'
            if isinstance(ref, ndf.model.ListRow):
                label = ref.namespace or '(unnamed)'
            item = self.properties_tree.insert('', 'end', text=label, values=(value_text,))
            self.property_refs[item] = ref
        else:
            title = 'No editable properties for this node.'

        self.property_info.config(text=title)
        self.value_var.set('')

    def on_property_select(self, event: Any) -> None:
        selection = self.properties_tree.selection()
        if not selection:
            return
        row = self.property_refs.get(selection[0])
        if not row:
            return
        self.value_var.set(format_value(row.v))

    def apply_property_value(self) -> None:
        selection = self.properties_tree.selection()
        if not selection:
            messagebox.showwarning('No Selection', 'Select a property to edit.')
            return
        row = self.property_refs.get(selection[0])
        if not row:
            return
        new_value_text = self.value_var.get().strip()
        if not new_value_text:
            messagebox.showwarning('No Value', 'Enter a value to apply.')
            return
        new_value = parse_value_input(new_value_text)
        row.v = new_value
        self.populate_properties(self.tree_item_refs[self.tree.selection()[0]])
        self.refresh_tree(select_ref=row)

    def browse_directory(self) -> None:
        directory = filedialog.askdirectory(
            initialdir=self.dir_var.get() or None,
            title='Select Directory with FX NDF Files',
        )
        if directory:
            self.dir_var.set(directory)

    def browse_files(self) -> None:
        file_paths = filedialog.askopenfilenames(
            title='Select FX NDF Files',
            filetypes=[('NDF Files', '*.ndf')],
        )
        if not file_paths:
            return
        files = [Path(file_path) for file_path in file_paths]
        self.file_listbox.delete(0, tk.END)
        for file_path in files:
            self.file_listbox.insert(tk.END, file_path.name)
        self.available_files = files
        self.file_listbox.selection_set(0, tk.END)
        self.log_message(f'Loaded {len(files)} file(s) from file picker')

    def load_files(self) -> None:
        directory = Path(self.dir_var.get())
        if not directory.exists():
            messagebox.showerror('Error', f'Directory does not exist:\n{directory}')
            return
        files = find_fx_files(directory, '*.ndf')
        if not files:
            messagebox.showinfo('No Files', f'No NDF files found in:\n{directory}')
            return
        self.file_listbox.delete(0, tk.END)
        for file_path in files:
            self.file_listbox.insert(tk.END, file_path.name)
        self.available_files = files
        self.file_listbox.selection_set(0, tk.END)
        self.log_message(f'Loaded {len(files)} file(s) from {directory}')

    def select_all_files(self) -> None:
        self.file_listbox.selection_set(0, tk.END)

    def clear_selection(self) -> None:
        self.file_listbox.selection_clear(0, tk.END)

    def get_selected_files(self) -> List[Path]:
        if not hasattr(self, 'available_files'):
            return []
        selected_indices = self.file_listbox.curselection()
        return [self.available_files[i] for i in selected_indices]

    def set_percentage(self, percentage: float) -> None:
        self.percentage_var.set(percentage)
        self.update_scale_factor()

    def update_scale_factor(self) -> None:
        percentage = self.percentage_var.get()
        self.scale_factor = percentage / 100.0
        self.scale_factor_label.config(text=f'Scale factor: {self.scale_factor:.2f}x')

    def clear_results(self) -> None:
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state=tk.DISABLED)

    def log_message(self, message: str) -> None:
        self.results_text.config(state=tk.NORMAL)
        self.results_text.insert(tk.END, message + '\n')
        self.results_text.see(tk.END)
        self.results_text.config(state=tk.DISABLED)
        self.root.update_idletasks()

    def preview_changes(self) -> None:
        selected_files = self.get_selected_files()
        if not selected_files:
            messagebox.showwarning('No Files', 'Please select at least one file.')
            return
        self.update_scale_factor()
        self.clear_results()
        self.log_message(f'Preview Mode - Scale factor: {self.scale_factor:.2f}x ({self.percentage_var.get():.1f}%)')
        self.log_message('=' * 60)

        total_changes = 0
        files_with_changes = 0
        preview_windows = []

        for file_path in selected_files:
            stats = process_file(file_path, self.scale_factor, dry_run=True)
            if stats.get('error'):
                self.log_message(f'✗ Error processing {file_path.name}: {stats["error"]}')
                continue
            changes = stats.get('changes', [])
            if changes:
                files_with_changes += 1
                total_changes += len(changes)
                self.log_message(f'✓ {file_path.name}: {len(changes)} change(s)')
                try:
                    preview_windows.append(PreviewWindow(self.root, file_path, self.scale_factor))
                except Exception as exc:
                    self.log_message(f'  Warning: Could not open preview for {file_path.name}: {exc}')
            else:
                self.log_message(f'○ {file_path.name}: No size parameters found')

        self.log_message('=' * 60)
        self.log_message('Summary:')
        self.log_message(f'  Files processed: {len(selected_files)}')
        self.log_message(f'  Files with changes: {files_with_changes}')
        self.log_message(f'  Total parameter changes: {total_changes}')
        if preview_windows:
            self.log_message(f'  Opened {len(preview_windows)} preview window(s)')

    def prompt_namespace_on_load(self) -> None:
        """Always prompt user to set/update namespace when loading a file."""
        if not self.parsed_root:
            return
        
        export_row = get_export_row(self.parsed_root)
        if not export_row or not export_row.namespace:
            messagebox.showwarning('No Namespace', 'No export namespace found in file.')
            return
        
        current_namespace = export_row.namespace
        filename = self.current_file.name if self.current_file else "unknown"
        
        # Always prompt for namespace update
        self.prompt_for_new_namespace(current_namespace, None)
    
    def prompt_for_new_namespace(self, current_namespace: str, suggested_namespace: Optional[str] = None) -> None:
        """Prompt user for a new namespace and update both namespace and filename.
        
        Args:
            current_namespace: The current namespace value
            suggested_namespace: Optional suggested namespace (unused, kept for compatibility)
        """
        # Create a simple dialog for namespace input
        dialog = tk.Toplevel(self.root)
        dialog.title('Set Namespace')
        dialog.geometry('600x220')
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f'+{x}+{y}')
        
        # Show current values
        current_filename = self.current_file.name if self.current_file else "unknown"
        info_text = f'Current namespace: {current_namespace}\nCurrent filename: {current_filename}'
        ttk.Label(
            dialog,
            text=info_text,
            font=('TkDefaultFont', 9),
        ).pack(pady=(10, 5))
        
        ttk.Label(
            dialog,
            text='Enter new namespace (filename will be updated to match):',
            font=('TkDefaultFont', 9, 'bold'),
        ).pack(anchor=tk.W, padx=20, pady=(10, 5))
        
        namespace_var = tk.StringVar(value=current_namespace)
        namespace_entry = ttk.Entry(dialog, textvariable=namespace_var, width=70)
        namespace_entry.pack(padx=20, pady=5, fill=tk.X)
        namespace_entry.select_range(0, tk.END)
        namespace_entry.focus()
        
        # Show preview of new filename
        preview_label = ttk.Label(
            dialog,
            text='',
            font=('TkDefaultFont', 8),
            foreground='gray',
        )
        preview_label.pack(padx=20, pady=(0, 5))
        
        def update_preview(*args) -> None:
            new_ns = namespace_var.get().strip()
            if new_ns:
                preview_label.config(text=f'New filename will be: {new_ns}.ndf')
            else:
                preview_label.config(text='')
        
        namespace_var.trace('w', update_preview)
        update_preview()
        
        def apply_namespace() -> None:
            new_namespace = namespace_var.get().strip()
            if not new_namespace:
                messagebox.showwarning('Invalid Namespace', 'Namespace cannot be empty.')
                return
            if new_namespace == current_namespace:
                # Even if same, still update filename to ensure it matches
                new_filename = f'{new_namespace}.ndf'
                if self.current_file and self.current_file.name != new_filename:
                    self.rename_file_to_match_namespace(new_namespace)
                dialog.destroy()
                return
            
            # Validate namespace format (should be a valid identifier)
            if not new_namespace.replace('_', '').replace('-', '').isalnum():
                response = messagebox.askyesno(
                    'Invalid Characters',
                    f'Namespace contains special characters.\n\n'
                    f'Namespace: {new_namespace}\n\n'
                    f'Continue anyway?',
                )
                if not response:
                    return
            
            try:
                # Update namespace in parsed NDF
                update_namespace(self.parsed_root, new_namespace)
                
                # Rename file to match new namespace
                self.rename_file_to_match_namespace(new_namespace)
                
                messagebox.showinfo(
                    'Namespace and Filename Updated',
                    f'Namespace updated from:\n{current_namespace}\n\nto:\n{new_namespace}\n\n'
                    f'File renamed to: {new_namespace}.ndf',
                )
                dialog.destroy()
                # Refresh tree to show updated namespace
                self.refresh_tree()
            except Exception as exc:
                messagebox.showerror('Error', f'Failed to update namespace:\n{exc}')
        
        def cancel() -> None:
            dialog.destroy()
        
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text='Apply', command=apply_namespace).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text='Cancel', command=cancel).pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to apply
        namespace_entry.bind('<Return>', lambda e: apply_namespace())
        namespace_entry.bind('<Escape>', lambda e: cancel())
    
    def rename_file_to_match_namespace(self, new_namespace: str) -> None:
        """Rename the current file to match the new namespace.
        
        Args:
            new_namespace: The new namespace (will become the filename without .ndf)
        """
        if not self.current_file:
            return
        
        new_filename = f'{new_namespace}.ndf'
        new_file_path = self.current_file.parent / new_filename
        
        # If file already exists and it's not the same file, ask for confirmation
        if new_file_path.exists() and new_file_path != self.current_file:
            response = messagebox.askyesno(
                'File Exists',
                f'File already exists:\n{new_file_path}\n\n'
                f'Overwrite it?',
            )
            if not response:
                return
        
        try:
            # Rename the file
            self.current_file.rename(new_file_path)
            self.current_file = new_file_path
            # Update the file path in the UI
            self.file_var.set(str(new_file_path))
        except Exception as exc:
            raise Exception(f'Failed to rename file: {exc}')
    
    def manual_namespace_update(self) -> None:
        """Manually trigger namespace update prompt."""
        if not self.parsed_root:
            messagebox.showwarning('No File', 'Load a file before updating namespace.')
            return
        
        export_row = get_export_row(self.parsed_root)
        if not export_row or not export_row.namespace:
            messagebox.showwarning('No Namespace', 'No export namespace found in file.')
            return
        
        current_namespace = export_row.namespace
        self.prompt_for_new_namespace(current_namespace, None)

    def batch_update_namespaces(self) -> None:
        """Batch update namespaces for multiple files, preserving numbering suffixes."""
        selected_files = self.get_selected_files()
        if not selected_files:
            messagebox.showwarning('No Files', 'Please select at least one file.')
            return
        
        if len(selected_files) == 1:
            # Single file - use regular namespace update
            messagebox.showinfo(
                'Single File',
                'Only one file selected. Use the "Update Namespace" button in the Editor tab for single files.',
            )
            return
        
        # Parse all files to get their current namespaces
        file_namespaces = {}
        errors = []
        
        for file_path in selected_files:
            try:
                parsed = parse_ndf_file(file_path)
                export_row = get_export_row(parsed)
                if export_row and export_row.namespace:
                    file_namespaces[file_path] = {
                        'namespace': export_row.namespace,
                        'parsed': parsed,
                    }
                else:
                    errors.append(f'{file_path.name}: No namespace found')
            except Exception as exc:
                errors.append(f'{file_path.name}: {str(exc)}')
        
        if errors:
            error_msg = 'Errors loading some files:\n\n' + '\n'.join(errors)
            response = messagebox.askyesno('Errors', error_msg + '\n\nContinue with successfully loaded files?')
            if not response:
                return
        
        if not file_namespaces:
            messagebox.showerror('No Namespaces', 'No valid namespaces found in selected files.')
            return
        
        # Extract numbering suffixes and determine base namespace pattern
        suffixes = {}
        base_examples = []
        
        for file_path, data in file_namespaces.items():
            namespace = data['namespace']
            # Try to extract number suffix (e.g., _1, _2, etc. at the end)
            match = re.search(r'_(\d+)$', namespace)
            if match:
                suffix = match.group(0)  # e.g., "_1"
                base = namespace[:-len(suffix)]  # Everything before the suffix
                suffixes[file_path] = {
                    'suffix': suffix,
                    'base': base,
                    'namespace': namespace,
                }
                if base not in base_examples:
                    base_examples.append(base)
            else:
                # No number suffix found - use full namespace as base
                suffixes[file_path] = {
                    'suffix': '',
                    'base': namespace,
                    'namespace': namespace,
                }
                if namespace not in base_examples:
                    base_examples.append(namespace)
        
        # Determine suggested base (most common base, or first one)
        if base_examples:
            # Count occurrences of each base
            base_counts = {}
            for file_path, data in suffixes.items():
                base = data['base']
                base_counts[base] = base_counts.get(base, 0) + 1
            suggested_base = max(base_counts.items(), key=lambda x: x[1])[0] if base_counts else base_examples[0]
        else:
            suggested_base = ''
        
        # Prompt for new base namespace
        dialog = tk.Toplevel(self.root)
        dialog.title('Batch Update Namespaces')
        dialog.geometry('700x350')
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Center the dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f'+{x}+{y}')
        
        # Show file list and current namespaces
        info_text = f'Selected files: {len(selected_files)}\n\n'
        info_text += 'Current namespaces (numbering suffixes will be preserved):\n'
        for file_path, data in list(suffixes.items())[:10]:  # Show first 10
            info_text += f'  {file_path.name}: {data["namespace"]}\n'
        if len(suffixes) > 10:
            info_text += f'  ... and {len(suffixes) - 10} more\n'
        
        ttk.Label(
            dialog,
            text=info_text,
            font=('TkDefaultFont', 9),
            justify=tk.LEFT,
        ).pack(pady=(10, 5), padx=20, anchor=tk.W)
        
        ttk.Label(
            dialog,
            text='Enter new base namespace (numbering suffixes will be appended automatically):',
            font=('TkDefaultFont', 9, 'bold'),
        ).pack(anchor=tk.W, padx=20, pady=(10, 5))
        
        base_var = tk.StringVar(value=suggested_base)
        base_entry = ttk.Entry(dialog, textvariable=base_var, width=80)
        base_entry.pack(padx=20, pady=5, fill=tk.X)
        base_entry.select_range(0, tk.END)
        base_entry.focus()
        
        # Show preview
        preview_frame = ttk.LabelFrame(dialog, text='Preview', padding='10')
        preview_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        preview_text = scrolledtext.ScrolledText(
            preview_frame,
            height=8,
            wrap=tk.WORD,
            state=tk.DISABLED,
            font=('TkDefaultFont', 8),
        )
        preview_text.pack(fill=tk.BOTH, expand=True)
        
        def update_preview(*args) -> None:
            new_base = base_var.get().strip()
            preview_text.config(state=tk.NORMAL)
            preview_text.delete(1.0, tk.END)
            if new_base:
                preview_text.insert(tk.END, 'New namespaces and filenames:\n\n')
                for file_path, data in list(suffixes.items())[:15]:  # Show first 15
                    new_namespace = new_base + data['suffix']
                    preview_text.insert(tk.END, f'{file_path.name} → {new_namespace}.ndf\n')
                    preview_text.insert(tk.END, f'  namespace: {data["namespace"]} → {new_namespace}\n\n')
                if len(suffixes) > 15:
                    preview_text.insert(tk.END, f'... and {len(suffixes) - 15} more files\n')
            else:
                preview_text.insert(tk.END, 'Enter a base namespace to see preview')
            preview_text.config(state=tk.DISABLED)
        
        base_var.trace('w', update_preview)
        update_preview()
        
        def apply_batch_namespace() -> None:
            new_base = base_var.get().strip()
            if not new_base:
                messagebox.showwarning('Invalid Base', 'Base namespace cannot be empty.')
                return
            
            # Validate base namespace format
            if not new_base.replace('_', '').replace('-', '').isalnum():
                response = messagebox.askyesno(
                    'Invalid Characters',
                    f'Base namespace contains special characters.\n\n'
                    f'Base: {new_base}\n\n'
                    f'Continue anyway?',
                )
                if not response:
                    return
            
            # Confirm before applying
            response = messagebox.askyesno(
                'Confirm Batch Update',
                f'Update namespaces and rename files for {len(file_namespaces)} file(s)?\n\n'
                f'Base namespace: {new_base}\n\n'
                f'This will modify files permanently.',
            )
            if not response:
                return
            
            # Apply changes
            success_count = 0
            error_count = 0
            errors_list = []
            
            for file_path, data in file_namespaces.items():
                try:
                    parsed = data['parsed']
                    suffix_data = suffixes[file_path]
                    new_namespace = new_base + suffix_data['suffix']
                    
                    # Update namespace in parsed NDF
                    update_namespace(parsed, new_namespace)
                    
                    # Write updated NDF
                    write_ndf_file(file_path, parsed)
                    
                    # Rename file
                    new_filename = f'{new_namespace}.ndf'
                    new_file_path = file_path.parent / new_filename
                    
                    if new_file_path.exists() and new_file_path != file_path:
                        # File exists - skip with warning
                        errors_list.append(f'{file_path.name}: Target file {new_filename} already exists')
                        error_count += 1
                        continue
                    
                    file_path.rename(new_file_path)
                    success_count += 1
                    
                except Exception as exc:
                    errors_list.append(f'{file_path.name}: {str(exc)}')
                    error_count += 1
            
            # Show results
            result_msg = f'Batch update complete!\n\n'
            result_msg += f'Successfully updated: {success_count} file(s)\n'
            if error_count > 0:
                result_msg += f'Errors: {error_count} file(s)\n\n'
                if errors_list:
                    result_msg += 'Errors:\n' + '\n'.join(errors_list[:5])
                    if len(errors_list) > 5:
                        result_msg += f'\n... and {len(errors_list) - 5} more'
            
            messagebox.showinfo('Batch Update Complete', result_msg)
            dialog.destroy()
            
            # Refresh file list if we're in batch tab
            if hasattr(self, 'available_files'):
                # Reload files to show updated names
                self.load_files()
        
        def cancel() -> None:
            dialog.destroy()
        
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text='Apply', command=apply_batch_namespace).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text='Cancel', command=cancel).pack(side=tk.LEFT, padx=5)
        
        # Bind Enter key to apply
        base_entry.bind('<Return>', lambda e: apply_batch_namespace())
        base_entry.bind('<Escape>', lambda e: cancel())

    def apply_changes(self) -> None:
        selected_files = self.get_selected_files()
        if not selected_files:
            messagebox.showwarning('No Files', 'Please select at least one file.')
            return
        response = messagebox.askyesno(
            'Confirm',
            f'Apply scale factor {self.scale_factor:.2f}x ({self.percentage_var.get():.1f}%) '
            f'to {len(selected_files)} file(s)?\n\nThis will modify the files permanently.',
        )
        if not response:
            return
        self.update_scale_factor()
        self.clear_results()
        self.log_message(f'Applying changes - Scale factor: {self.scale_factor:.2f}x ({self.percentage_var.get():.1f}%)')
        self.log_message('=' * 60)

        total_changes = 0
        files_with_changes = 0

        for file_path in selected_files:
            stats = process_file(file_path, self.scale_factor, dry_run=False)
            if stats.get('error'):
                self.log_message(f'✗ Error processing {file_path.name}: {stats["error"]}')
                continue
            changes = stats.get('changes', [])
            if changes:
                files_with_changes += 1
                total_changes += len(changes)
                self.log_message(f'✓ Modified {file_path.name}: {len(changes)} change(s)')
            else:
                self.log_message(f'○ {file_path.name}: No size parameters found')

        self.log_message('=' * 60)
        self.log_message('Summary:')
        self.log_message(f'  Files processed: {len(selected_files)}')
        self.log_message(f'  Files with changes: {files_with_changes}')
        self.log_message(f'  Total parameter changes: {total_changes}')
        messagebox.showinfo('Complete', 'Changes applied successfully!')


def main() -> None:
    root = tk.Tk()
    app = FXEditorApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
