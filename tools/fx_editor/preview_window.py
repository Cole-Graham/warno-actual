"""Detailed preview window showing file structure and parameter changes."""

import sys
import tkinter as tk
from tkinter import ttk, scrolledtext
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Add project root to path for imports (same as dpm_visualizer)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .model_index import build_tree, TreeNode
from .size_batch import iter_map_rows, scale_map_row


class PreviewWindow:
    """Detailed preview window for viewing file structure and changes."""

    def __init__(self, parent: tk.Tk, file_path: Path, scale_factor: float):
        self.parent = parent
        self.file_path = file_path
        self.scale_factor = scale_factor
        self.parsed_root = self._parse_file()
        self.tree_nodes: Dict[str, TreeNode] = {}
        self.tree_item_refs: Dict[str, TreeNode] = {}

        self.window = tk.Toplevel(parent)
        self.window.title(f'Preview Changes: {file_path.name}')
        self.window.geometry('1200x800')

        self.setup_ui()
        self.populate_tree()

    def _parse_file(self) -> ndf.model.List:
        with open(self.file_path, 'r', encoding='utf-8') as handle:
            content = handle.read()
        parsed = ndf.convert(content)
        if not isinstance(parsed, ndf.model.List):
            raise ValueError(f'Expected ndf.model.List, got {type(parsed).__name__}')
        return parsed

    def setup_ui(self) -> None:
        main_frame = ttk.Frame(self.window, padding='10')
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(
            main_frame,
            text=f'Preview: {self.file_path.name}',
            font=('Arial', 14, 'bold'),
        )
        title_label.pack(pady=(0, 10))

        info_label = ttk.Label(
            main_frame,
            text=f'Scale Factor: {self.scale_factor:.2f}x ({self.scale_factor * 100:.1f}%)',
            font=('Arial', 10),
        )
        info_label.pack(pady=(0, 10))

        paned = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)

        left_frame = ttk.LabelFrame(paned, text='File Structure', padding='5')
        right_frame = ttk.LabelFrame(paned, text='Details', padding='5')
        paned.add(left_frame, weight=1)
        paned.add(right_frame, weight=2)

        tree_frame = ttk.Frame(left_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True)
        tree_scrollbar = ttk.Scrollbar(tree_frame)
        tree_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree = ttk.Treeview(
            tree_frame,
            yscrollcommand=tree_scrollbar.set,
            selectmode=tk.BROWSE,
        )
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tree_scrollbar.config(command=self.tree.yview)
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

        self.node_info_label = ttk.Label(
            right_frame,
            text='Select a node to view details',
            font=('Arial', 10, 'bold'),
        )
        self.node_info_label.pack(pady=(0, 5))

        details_frame = ttk.Frame(right_frame)
        details_frame.pack(fill=tk.BOTH, expand=True)
        self.details_text = scrolledtext.ScrolledText(
            details_frame,
            wrap=tk.WORD,
            state=tk.DISABLED,
            font=('Consolas', 9),
        )
        self.details_text.pack(fill=tk.BOTH, expand=True)

        summary_frame = ttk.Frame(right_frame)
        summary_frame.pack(fill=tk.X, pady=(5, 0))
        self.summary_label = ttk.Label(summary_frame, text='', font=('Arial', 9))
        self.summary_label.pack()

    def populate_tree(self) -> None:
        self.tree.delete(*self.tree.get_children())
        self.tree_item_refs = {}

        root_node, node_map = build_tree(self.parsed_root)
        self.tree_nodes = node_map

        def add_node(parent_item: str, node_id: str, depth: int) -> None:
            node = node_map[node_id]
            item = self.tree.insert(
                parent_item,
                'end',
                text=node.label,
                open=(depth < 2),
            )
            self.tree_item_refs[item] = node
            for child_id in node.children:
                add_node(item, child_id, depth + 1)

        add_node('', root_node.node_id, 0)

        total_changes = len(self._collect_changes(self.parsed_root))
        self.summary_label.config(
            text=f'Total size-parameter changes: {total_changes}',
        )

    def on_tree_select(self, event: Any) -> None:
        selection = self.tree.selection()
        if not selection:
            return
        node = self.tree_item_refs.get(selection[0])
        if not node:
            return
        self.display_node_details(node)

    def display_node_details(self, node: TreeNode) -> None:
        self.node_info_label.config(text=node.label)
        self.details_text.config(state=tk.NORMAL)
        self.details_text.delete(1.0, tk.END)

        changes = self._collect_changes(node.ref)
        if not changes:
            self.details_text.insert(tk.END, 'No size-related parameters found in this section.\n')
        else:
            self.details_text.insert(tk.END, f'Size-related parameters: {len(changes)}\n')
            self.details_text.insert(tk.END, '=' * 70 + '\n\n')
            for change, action_name in changes:
                self.details_text.insert(tk.END, f'Parameter: {change.name}\n', 'param_name')
                if action_name:
                    self.details_text.insert(tk.END, f'  VFX: {action_name}\n', 'action_name')
                self.details_text.insert(tk.END, f'  Old Value: {change.old_value}\n', 'old_value')
                self.details_text.insert(tk.END, f'  New Value: {change.new_value}\n', 'new_value')
                self.details_text.insert(tk.END, '\n')

        self.details_text.tag_config('param_name', font=('Consolas', 10, 'bold'), foreground='#0066CC')
        self.details_text.tag_config('action_name', foreground='#555555')
        self.details_text.tag_config('old_value', foreground='#CC0000')
        self.details_text.tag_config('new_value', foreground='#006600', font=('Consolas', 9, 'bold'))
        self.details_text.config(state=tk.DISABLED)

    def _get_action_name(self, obj: ndf.model.Object) -> Optional[str]:
        if obj.type != 'TActionCall':
            return None
        try:
            action_member = obj.by_m('Action', None)
        except Exception:
            action_member = None
        if not action_member:
            return None
        action_value = strip_quotes(str(action_member.v))
        return action_value.split('/')[-1] if action_value else action_value

    def _collect_changes(self, root: Any) -> List[Tuple[Any, Optional[str]]]:
        changes: List[Tuple[Any, Optional[str]]] = []

        def walk(node: Any, current_action: Optional[str]) -> None:
            if isinstance(node, ndf.model.Object):
                action_name = self._get_action_name(node) or current_action
                for member in node:
                    walk(member.v, action_name)
                return
            if isinstance(node, ndf.model.Map):
                for map_row in node:
                    change = scale_map_row(map_row, self.scale_factor, dry_run=True)
                    if change:
                        changes.append((change, current_action))
                    walk(map_row.v, current_action)
                return
            if isinstance(node, ndf.model.List):
                for row in node:
                    walk(row.v, current_action)
                return
            if isinstance(node, ndf.model.MemberRow):
                walk(node.v, current_action)
                return
            if isinstance(node, ndf.model.ListRow):
                walk(node.v, current_action)
                return

        walk(root, None)
        return changes
