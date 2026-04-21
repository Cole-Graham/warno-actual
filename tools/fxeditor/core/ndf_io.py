"""Parse / serialize NDF text and navigate the model tree."""

from __future__ import annotations

import re
from typing import Any, Iterable, List, Optional, Tuple

from src import ndf
from src.utils.ndf_utils import strip_quotes

FLOAT3_PLUS_PAR = re.compile(
    r"float3\s*\[\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^\]]+)\s*\]\s*\+\s*parPosition",
    re.IGNORECASE,
)
FLOAT3_LITERAL_XY = re.compile(
    r"^float3\s*\[\s*([^,]+)\s*,\s*([^,]+)\s*,\s*([^\]]+)\s*\]\s*$",
    re.IGNORECASE,
)

_SCATTER_NAMED_POSITION_KEYS = frozenset({"parPositionRelative", "parStartPosition"})


# ── parsing / serialization ────────────────────────────────────────

def parse_ndf(text: str) -> ndf.model.List:
    parsed = ndf.convert(text)
    if not isinstance(parsed, ndf.model.List):
        raise ValueError(f"Expected ndf.model.List, got {type(parsed).__name__}")
    return parsed


def serialize_ndf(root: ndf.model.List) -> str:
    return ndf.printer.string(root)


# ── tree navigation ────────────────────────────────────────────────

def find_actions_list(parsed_root: ndf.model.List) -> Optional[ndf.model.List]:
    """First export object's ``Actions`` member list."""
    if len(parsed_root) == 0:
        return None
    first = parsed_root[0]
    if not isinstance(first, ndf.model.ListRow):
        return None
    obj = first.v
    if not isinstance(obj, ndf.model.Object):
        return None
    for member in obj:
        if member.member == "Actions" and isinstance(member.v, ndf.model.List):
            return member.v
    return None


def list_tsimultaneous_rows(actions: ndf.model.List) -> List[Any]:
    out: List[Any] = []
    for row in actions:
        try:
            sim = row.v
        except Exception:
            continue
        if isinstance(sim, ndf.model.Object) and sim.type == "TSimultaneousAction":
            out.append(row)
    return out


def _list_row_child_v(row: object) -> object:
    try:
        return row.v
    except Exception:
        return None


# ── position helpers ───────────────────────────────────────────────

def parse_float3_plus_par(text: str) -> Optional[Tuple[float, float]]:
    m = FLOAT3_PLUS_PAR.search(text.strip())
    if not m:
        return None
    try:
        return float(m.group(1)), float(m.group(2))
    except ValueError:
        return None


def parse_mobile_position_xy(text: str) -> Optional[Tuple[float, float]]:
    text = text.strip()
    p = parse_float3_plus_par(text)
    if p is not None:
        return p
    m = FLOAT3_LITERAL_XY.match(text)
    if m:
        try:
            return float(m.group(1)), float(m.group(2))
        except ValueError:
            return None
    if text.replace(" ", "").lower() == "parposition":
        return (0.0, 0.0)
    return None


def stringify_position_expr(dx: float, dy: float) -> str:
    """Vanilla-style integer components: ``float3[ix,iy,0] + parPosition``."""
    return f"float3[{int(round(dx))},{int(round(dy))},0] + parPosition"


def stringify_position_expr_xyz(dx: float, dy: float, dz: float) -> str:
    """Vanilla-style integer components preserving z: ``float3[ix,iy,iz] + parPosition``."""
    return f"float3[{int(round(dx))},{int(round(dy))},{int(round(dz))}] + parPosition"


def parse_float3_plus_par_xyz(text: str) -> Optional[Tuple[float, float, float]]:
    """Like ``parse_float3_plus_par`` but also returns the z component."""
    m = FLOAT3_PLUS_PAR.search(text.strip())
    if not m:
        return None
    try:
        return float(m.group(1)), float(m.group(2)), float(m.group(3))
    except ValueError:
        return None


def mobile_position_from_simultaneous(sim: ndf.model.Object) -> Optional[Tuple[float, float]]:
    if sim.type != "TSimultaneousAction":
        return None
    for m in sim:
        if m.member != "Mobile" or not isinstance(m.v, ndf.model.Object):
            continue
        mob = m.v
        if mob.type != "TMobileWithLocalRepereMatrixFactory":
            continue
        for mm in mob:
            if mm.member == "Position":
                s = ndf.printer.string(mm.v).strip()
                p = parse_mobile_position_xy(s)
                if p is not None:
                    return p
    return None


def simultaneous_is_nil_mobile(sim: ndf.model.Object) -> bool:
    if sim.type != "TSimultaneousAction":
        return False
    for m in sim:
        if m.member != "Mobile":
            continue
        s = ndf.printer.string(m.v).strip().lower()
        return s == "nil"
    return False


# ── VFX name extraction ───────────────────────────────────────────

def action_short_from_taction(obj: ndf.model.Object) -> str:
    if obj.type != "TActionCall":
        return ""
    for member in obj:
        if member.member == "Action":
            av = strip_quotes(str(member.v))
            return av.split("/")[-1] if av else ""
    return ""


def first_taction_short_in_simultaneous(sim: ndf.model.Object) -> str:
    def walk(node: Any) -> str:
        if isinstance(node, ndf.model.Object):
            if node.type == "TActionCall":
                s = action_short_from_taction(node)
                if s:
                    return s
            for m in node:
                got = walk(m.v)
                if got:
                    return got
        elif isinstance(node, ndf.model.List):
            for row in node:
                got = walk(row.v)
                if got:
                    return got
        elif isinstance(node, ndf.model.MemberRow):
            return walk(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                got = walk(mr.v)
                if got:
                    return got
        elif isinstance(node, ndf.model.ListRow):
            return walk(node.v)
        return ""

    if sim.type != "TSimultaneousAction":
        return ""
    for m in sim:
        if m.member == "Actions" and isinstance(m.v, ndf.model.List):
            for row in m.v:
                got = walk(row.v)
                if got:
                    return got
    return ""


# ── TActionCall iteration ─────────────────────────────────────────

def iter_taction_call_objects(root: Any) -> Iterable[ndf.model.Object]:
    if isinstance(root, ndf.model.Object):
        if root.type == "TActionCall":
            yield root
        for member in root:
            yield from iter_taction_call_objects(member.v)
    elif isinstance(root, ndf.model.List):
        for row in root:
            yield from iter_taction_call_objects(row.v)
    elif isinstance(root, ndf.model.MemberRow):
        yield from iter_taction_call_objects(root.v)
    elif isinstance(root, ndf.model.Map):
        for mr in root:
            yield from iter_taction_call_objects(mr.v)
    elif isinstance(root, ndf.model.ListRow):
        yield from iter_taction_call_objects(root.v)


def count_taction_calls(root: Any) -> int:
    return sum(1 for _ in iter_taction_call_objects(root))


# ── scatter-named position helpers ────────────────────────────────

def has_scatter_named_position(root: Any) -> bool:
    def walk(node: Any) -> bool:
        if isinstance(node, ndf.model.Object):
            if node.type == "TActionCall":
                for member in node:
                    if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
                        continue
                    for map_row in member.v:
                        key = strip_quotes(str(map_row.k)) if map_row.k is not None else ""
                        if key in _SCATTER_NAMED_POSITION_KEYS:
                            return True
            for member in node:
                if walk(member.v):
                    return True
        elif isinstance(node, ndf.model.List):
            for row in node:
                if walk(row.v):
                    return True
        elif isinstance(node, ndf.model.MemberRow):
            return walk(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                if walk(mr.v):
                    return True
        elif isinstance(node, ndf.model.ListRow):
            return walk(node.v)
        return False
    return walk(root)


def tsimultaneous_has_placeable_hook(sim: ndf.model.Object) -> bool:
    """True if emit can set burst XY (Mobile Position or scatter NamedParams)."""
    if sim.type != "TSimultaneousAction":
        return False
    for m in sim:
        if m.member != "Mobile" or not isinstance(m.v, ndf.model.Object):
            continue
        mob = m.v
        if mob.type != "TMobileWithLocalRepereMatrixFactory":
            continue
        for mm in mob:
            if mm.member == "Position":
                return True
    return has_scatter_named_position(sim)


def list_placeable_templates(actions: ndf.model.List) -> List[Any]:
    out: List[Any] = []
    for row in list_tsimultaneous_rows(actions):
        sim = row.v
        if isinstance(sim, ndf.model.Object) and tsimultaneous_has_placeable_hook(sim):
            out.append(row)
    return out


# ── namespace update ──────────────────────────────────────────────

def update_export_name(parsed_root: ndf.model.List, new_name: str) -> None:
    if len(parsed_root) == 0:
        return
    first = parsed_root[0]
    if isinstance(first, ndf.model.ListRow):
        first.namespace = new_name
