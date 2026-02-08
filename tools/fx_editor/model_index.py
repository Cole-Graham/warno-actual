"""Build a tree index from ndf_parse model objects for UI display."""

import itertools
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Add project root to path for imports (same as dpm_visualizer)
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from src import ndf
from src.utils.ndf_utils import strip_quotes


@dataclass
class TreeNode:
    """Tree node for UI mapping to ndf_parse objects."""
    node_id: str
    label: str
    kind: str
    ref: Any
    parent_id: Optional[str]
    children: List[str] = field(default_factory=list)


def build_tree(parsed_root: ndf.model.List) -> Tuple[TreeNode, Dict[str, TreeNode]]:
    """Build a TreeNode index from a parsed NDF root list."""
    node_map: Dict[str, TreeNode] = {}
    counter = itertools.count(1)

    def new_id() -> str:
        return f'node_{next(counter)}'

    def add_node(label: str, kind: str, ref: Any, parent_id: Optional[str]) -> TreeNode:
        node_id = new_id()
        node = TreeNode(
            node_id=node_id,
            label=label,
            kind=kind,
            ref=ref,
            parent_id=parent_id,
        )
        node_map[node_id] = node
        if parent_id:
            node_map[parent_id].children.append(node_id)
        return node

    def get_action_name(obj: ndf.model.Object) -> Optional[str]:
        if obj.type != 'TActionCall':
            return None
        try:
            action_member = obj.by_m('Action', None)
        except Exception:
            action_member = None
        if not action_member:
            return None
        action_value = strip_quotes(str(action_member.v))
        return action_value

    def value_summary(value: Any) -> str:
        if isinstance(value, ndf.model.Object):
            if value.type == 'TActionCall':
                action_name = get_action_name(value)
                if action_name:
                    action_short = action_name.split('/')[-1]
                    return f'{value.type}({action_short})'
            return value.type or 'Object'
        if isinstance(value, ndf.model.Map):
            return f'MAP[{len(value)}]'
        if isinstance(value, ndf.model.List):
            type_label = f' {value.type}' if value.type else ''
            return f'List{type_label}[{len(value)}]'
        return str(value)

    def add_value_children(value: Any, parent_id: str) -> None:
        if isinstance(value, ndf.model.Object):
            obj_node = add_node(value.type or 'Object', 'Object', value, parent_id)
            for member_row in value:
                member_label = member_row.member or '(unnamed)'
                add_member_node(member_row, obj_node.node_id, member_label)
            return
        if isinstance(value, ndf.model.Map):
            map_node = add_node('MAP', 'Map', value, parent_id)
            for map_row in value:
                key = strip_quotes(str(map_row.k)) if map_row.k is not None else '(nil)'
                map_label = key
                add_map_node(map_row, map_node.node_id, map_label)
            return
        if isinstance(value, ndf.model.List):
            list_label = 'List'
            if value.type:
                list_label = f'List {value.type}'
            list_node = add_node(list_label, 'List', value, parent_id)
            for idx, list_row in enumerate(value):
                list_label = list_row.namespace or f'[{idx}]'
                add_list_row_node(list_row, list_node.node_id, list_label)
            return

    def add_list_row_node(list_row: ndf.model.ListRow, parent_id: str, label: str) -> None:
        summary = value_summary(list_row.v)
        row_label = f'{label} = {summary}'
        row_node = add_node(row_label, 'ListRow', list_row, parent_id)
        add_value_children(list_row.v, row_node.node_id)

    def add_member_node(member_row: ndf.model.MemberRow, parent_id: str, label: str) -> None:
        summary = value_summary(member_row.v)
        row_label = f'{label} = {summary}'
        row_node = add_node(row_label, 'MemberRow', member_row, parent_id)
        add_value_children(member_row.v, row_node.node_id)

    def add_map_node(map_row: ndf.model.MapRow, parent_id: str, label: str) -> None:
        summary = value_summary(map_row.v)
        row_label = f'{label} = {summary}'
        row_node = add_node(row_label, 'MapRow', map_row, parent_id)
        add_value_children(map_row.v, row_node.node_id)

    root_label = 'Root'
    if len(parsed_root) > 0:
        first_row = parsed_root[0]
        if isinstance(first_row, ndf.model.ListRow):
            if first_row.namespace and isinstance(first_row.v, ndf.model.Object):
                root_label = f'{first_row.namespace} ({first_row.v.type})'
            elif first_row.namespace:
                root_label = first_row.namespace
    root_node = add_node(root_label, 'RootList', parsed_root, None)

    for idx, list_row in enumerate(parsed_root):
        label = list_row.namespace or f'[{idx}]'
        add_list_row_node(list_row, root_node.node_id, label)

    return root_node, node_map
