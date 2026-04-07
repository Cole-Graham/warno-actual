"""Spatial classification of VFX groups within a source NDF.

Analyzes every TSimultaneousAction block and every TActionCall to determine
the spatial role of each VFX short name relative to the composite site
positions.  The classification drives per-category scaling policies in the
scaler so that artistic ratios (site vs random instances, offsets, etc.) are
preserved across target radii.

Categories
----------
composite_lead       : nil-Mobile parPositionRelative, precisely stacked at
                       ALL composite sites (1:1 with sites).
site_stacked         : Mobile blocks precisely at composite site positions.
site_offset          : Mobile blocks near composite sites but on a different
                       (slightly offset) coordinate lattice.
site_registered_precise : some instances precisely at sites + some random.
site_registered_offset  : some instances offset-near sites + some random.
field_random         : all instances are random, no site correlation.
center_only          : single spatial anchor at/near (0,0).
"""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Set, Tuple

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .ndf_io import (
    _SCATTER_NAMED_POSITION_KEYS,
    _list_row_child_v,
    action_short_from_taction,
    find_actions_list,
    first_taction_short_in_simultaneous,
    list_tsimultaneous_rows,
    mobile_position_from_simultaneous,
    parse_float3_plus_par,
    simultaneous_is_nil_mobile,
)


# ── Spatial role enum ─────────────────────────────────────────────

class SpatialRole(Enum):
    COMPOSITE_LEAD = auto()
    SITE_STACKED = auto()
    SITE_OFFSET = auto()
    SITE_REGISTERED_PRECISE = auto()
    SITE_REGISTERED_OFFSET = auto()
    FIELD_RANDOM = auto()
    CENTER_ONLY = auto()

    @property
    def is_site_bound(self) -> bool:
        return self in (
            SpatialRole.COMPOSITE_LEAD,
            SpatialRole.SITE_STACKED,
            SpatialRole.SITE_OFFSET,
            SpatialRole.SITE_REGISTERED_PRECISE,
            SpatialRole.SITE_REGISTERED_OFFSET,
        )


# ── Data classes ──────────────────────────────────────────────────

@dataclass
class VFXOccurrence:
    """One occurrence of a VFX at a specific gameplay position."""
    block_index: int
    gx: float
    gy: float
    source_type: str        # 'mobile' or 'par_position_relative'
    from_nil_mobile: bool
    is_primary_in_block: bool


@dataclass
class VFXGroupClassification:
    vfx_name: str
    role: SpatialRole
    site_count: int = 0
    random_count: int = 0
    per_site_multiplicity: float = 1.0
    offset_vector: Optional[Tuple[float, float]] = None
    occurrences: List[VFXOccurrence] = field(default_factory=list)


@dataclass
class BlockClassification:
    block_index: int
    vfx_names: List[str]
    primary_vfx: str
    is_nil_mobile: bool
    mobile_pos_gameplay: Optional[Tuple[float, float]]
    assigned_site: Optional[int] = None
    role: Optional[SpatialRole] = None
    is_site_instance: bool = False
    n_taction_calls: int = 0


@dataclass
class SourceClassification:
    """Full spatial analysis of a source NDF file."""
    composite_sites: List[Tuple[float, float]]
    n_sites: int
    vfx_groups: Dict[str, VFXGroupClassification]
    block_classifications: List[BlockClassification]
    nil_mobile_block_indices: List[int]

    def blocks_for_role(self, role: SpatialRole) -> List[BlockClassification]:
        return [b for b in self.block_classifications if b.role == role]

    def site_blocks_for_site(self, site_j: int) -> List[BlockClassification]:
        return [
            b for b in self.block_classifications
            if b.assigned_site == site_j and b.is_site_instance
        ]

    def random_blocks(self) -> List[BlockClassification]:
        return [
            b for b in self.block_classifications
            if not b.is_nil_mobile and not b.is_site_instance
            and b.role not in (SpatialRole.CENTER_ONLY, SpatialRole.COMPOSITE_LEAD)
        ]


# ── Internal helpers ──────────────────────────────────────────────

def _par_positions_from_taction(tac: ndf.model.Object) -> List[Tuple[float, float]]:
    """All scatter-named position offsets (parPositionRelative, parStartPosition, etc.)."""
    if tac.type != "TActionCall":
        return []
    out: List[Tuple[float, float]] = []
    for member in tac:
        if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
            continue
        for mr in member.v:
            key = strip_quotes(str(mr.k)) if mr.k is not None else ""
            if key not in _SCATTER_NAMED_POSITION_KEYS:
                continue
            s = ndf.printer.string(mr.v).strip()
            p = parse_float3_plus_par(s)
            if p:
                out.append(p)
    return out


def _all_taction_calls_in_simultaneous(
    sim: ndf.model.Object,
) -> List[ndf.model.Object]:
    out: List[ndf.model.Object] = []

    def walk(node: Any) -> None:
        if isinstance(node, ndf.model.Object):
            if node.type == "TActionCall":
                out.append(node)
            for m in node:
                walk(m.v)
        elif isinstance(node, ndf.model.List):
            for row in node:
                walk(row.v)
        elif isinstance(node, ndf.model.MemberRow):
            walk(node.v)
        elif isinstance(node, ndf.model.Map):
            for mr in node:
                walk(mr.v)
        elif isinstance(node, ndf.model.ListRow):
            walk(node.v)

    for m in sim:
        if m.member == "Actions" and isinstance(m.v, ndf.model.List):
            walk(m.v)
    return out


def _hypot(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def _nearest_site_dist(
    pt: Tuple[float, float],
    sites: List[Tuple[float, float]],
) -> Tuple[float, int]:
    best_d = float("inf")
    best_j = 0
    for j, s in enumerate(sites):
        d = _hypot(pt, s)
        if d < best_d:
            best_d = d
            best_j = j
    return best_d, best_j


# ── Main classifier ──────────────────────────────────────────────

def classify_source(
    parsed_root: ndf.model.List,
    ref_m: float,
    anchor_r: float,
    *,
    eps_precise: float = 1.0,
    eps_offset: float = 8.0,
) -> SourceClassification:
    """Classify every VFX group by spatial role.

    Parameters
    ----------
    parsed_root : parsed NDF tree
    ref_m, anchor_r : calibration values for NDF-to-gameplay mapping
    eps_precise : gameplay meters -- within this distance counts as "precise"
                  match to a composite site position
    eps_offset : gameplay meters -- within this but beyond eps_precise counts
                 as "offset" (slightly different lattice)
    """
    actions = find_actions_list(parsed_root)
    if actions is None:
        return SourceClassification(
            composite_sites=[], n_sites=0,
            vfx_groups={}, block_classifications=[],
            nil_mobile_block_indices=[],
        )

    s = ref_m / anchor_r if anchor_r > 0 else 1.0
    rows = list_tsimultaneous_rows(actions)

    # ── Pass 1: Collect per-block info ──
    block_infos: List[BlockClassification] = []
    vfx_occurrences: Dict[str, List[VFXOccurrence]] = defaultdict(list)
    nil_mobile_indices: List[int] = []

    for i, row in enumerate(rows):
        sim = row.v
        if not isinstance(sim, ndf.model.Object) or sim.type != "TSimultaneousAction":
            continue

        mob = mobile_position_from_simultaneous(sim)
        is_nil = simultaneous_is_nil_mobile(sim)
        mob_gp: Optional[Tuple[float, float]] = None
        if mob is not None:
            mob_gp = (mob[0] * s, mob[1] * s)

        tacs = _all_taction_calls_in_simultaneous(sim)
        vfx_names: List[str] = []
        primary = first_taction_short_in_simultaneous(sim) or ""

        if is_nil:
            nil_mobile_indices.append(i)
            for tac in tacs:
                vfx = action_short_from_taction(tac)
                if not vfx:
                    continue
                pars = _par_positions_from_taction(tac)
                for px, py in pars:
                    gx, gy = px * s, py * s
                    vfx_occurrences[vfx].append(VFXOccurrence(
                        block_index=i, gx=gx, gy=gy,
                        source_type="par_position_relative",
                        from_nil_mobile=True,
                        is_primary_in_block=True,
                    ))
                if vfx not in vfx_names:
                    vfx_names.append(vfx)
        elif mob_gp is not None:
            # For Mobile blocks: record ONE occurrence per VFX name per block
            # at the Mobile position.  The primary TActionCall (first in preorder)
            # is the one that "owns" the dot in scatter preview.
            seen_vfx_in_block: Set[str] = set()
            for tac in tacs:
                vfx = action_short_from_taction(tac)
                if not vfx or vfx in seen_vfx_in_block:
                    continue
                seen_vfx_in_block.add(vfx)
                is_prim = (vfx == primary)
                vfx_occurrences[vfx].append(VFXOccurrence(
                    block_index=i, gx=mob_gp[0], gy=mob_gp[1],
                    source_type="mobile",
                    from_nil_mobile=False,
                    is_primary_in_block=is_prim,
                ))
                if vfx not in vfx_names:
                    vfx_names.append(vfx)

        block_infos.append(BlockClassification(
            block_index=i,
            vfx_names=vfx_names,
            primary_vfx=primary,
            is_nil_mobile=is_nil,
            mobile_pos_gameplay=mob_gp,
            n_taction_calls=len(tacs),
        ))

    # ── Pass 2: Identify composite site positions ──
    # Use the R-lattice from the first nil-Mobile block's parPositionRelative
    composite_sites: List[Tuple[float, float]] = []
    if nil_mobile_indices:
        first_nil = nil_mobile_indices[0]
        seen_pos: Set[Tuple[int, int]] = set()
        for vfx, occs in vfx_occurrences.items():
            for occ in occs:
                if occ.block_index != first_nil:
                    continue
                key = (round(occ.gx), round(occ.gy))
                if key not in seen_pos:
                    seen_pos.add(key)
                    composite_sites.append((occ.gx, occ.gy))
            if composite_sites:
                break

    # Fallback: positions shared by >= 3 primary VFX types
    if not composite_sites:
        pos_vfx: Dict[Tuple[int, int], Set[str]] = defaultdict(set)
        for vfx, occs in vfx_occurrences.items():
            for occ in occs:
                if occ.is_primary_in_block:
                    pos_vfx[(round(occ.gx), round(occ.gy))].add(vfx)
        for pk, vfxs in sorted(pos_vfx.items(), key=lambda x: -len(x[1])):
            if len(vfxs) >= 3:
                composite_sites.append((float(pk[0]), float(pk[1])))

    n_sites = len(composite_sites)

    # ── Pass 3: Classify each VFX group ──
    # For VFX that appear as secondary calls inside Mobile blocks,
    # only count PRIMARY occurrences for spatial classification.
    # Secondary VFX inherit the block's role and are automatically
    # replicated when the block is cloned.
    vfx_groups: Dict[str, VFXGroupClassification] = {}

    for vfx_name, all_occs in vfx_occurrences.items():
        if not all_occs:
            continue

        # For Mobile blocks: use only PRIMARY occurrences for classification.
        # For nil-Mobile blocks: all occurrences are "primary" (each has its
        # own parPositionRelative).
        occs = [o for o in all_occs if o.is_primary_in_block]
        if not occs:
            # VFX only appears as secondary in Mobile blocks -- it will be
            # carried along when the block is cloned. Don't classify independently.
            # Still record it for display purposes.
            vfx_groups[vfx_name] = VFXGroupClassification(
                vfx_name=vfx_name,
                role=SpatialRole.SITE_STACKED,
                site_count=len(all_occs),
                random_count=0,
                per_site_multiplicity=len(all_occs) / n_sites if n_sites > 0 else 1.0,
                occurrences=all_occs,
            )
            continue

        # Check for center-only: all unique positions are at/near origin
        unique_positions = set((round(o.gx), round(o.gy)) for o in occs)
        if len(unique_positions) == 1:
            pos0 = next(iter(unique_positions))
            if math.hypot(pos0[0], pos0[1]) <= eps_offset:
                vfx_groups[vfx_name] = VFXGroupClassification(
                    vfx_name=vfx_name,
                    role=SpatialRole.CENTER_ONLY,
                    site_count=0, random_count=0,
                    per_site_multiplicity=0,
                    occurrences=all_occs,
                )
                continue

        near_precise: List[VFXOccurrence] = []
        near_offset: List[VFXOccurrence] = []
        far_field: List[VFXOccurrence] = []

        for occ in occs:
            if not composite_sites:
                far_field.append(occ)
                continue
            pt = (occ.gx, occ.gy)
            dist, _ = _nearest_site_dist(pt, composite_sites)
            if dist <= eps_precise:
                near_precise.append(occ)
            elif dist <= eps_offset:
                near_offset.append(occ)
            else:
                far_field.append(occ)

        n_near_precise = len(near_precise)
        n_near_offset = len(near_offset)
        n_near_total = n_near_precise + n_near_offset
        n_far = len(far_field)
        from_nil = any(o.from_nil_mobile for o in occs)

        if n_far == 0 and n_near_total > 0:
            if from_nil and n_near_precise >= n_sites:
                role = SpatialRole.COMPOSITE_LEAD
            elif n_near_precise >= n_near_offset:
                role = SpatialRole.SITE_STACKED
            else:
                role = SpatialRole.SITE_OFFSET
            offset_vec = _compute_offset_vector(near_offset, composite_sites) if near_offset else None
            vfx_groups[vfx_name] = VFXGroupClassification(
                vfx_name=vfx_name, role=role,
                site_count=n_near_total, random_count=0,
                per_site_multiplicity=n_near_total / n_sites if n_sites > 0 else 1.0,
                offset_vector=offset_vec,
                occurrences=all_occs,
            )
        elif n_near_total > 0 and n_far > 0:
            # Distinguish systematic site placement from coincidental proximity.
            # If fewer than half the sites have an instance, it's coincidental.
            sites_covered = set()
            for occ in near_precise + near_offset:
                _, sj = _nearest_site_dist((occ.gx, occ.gy), composite_sites)
                sites_covered.add(sj)
            if n_sites > 0 and len(sites_covered) < n_sites * 0.5:
                role = SpatialRole.FIELD_RANDOM
                vfx_groups[vfx_name] = VFXGroupClassification(
                    vfx_name=vfx_name, role=role,
                    site_count=0, random_count=len(occs),
                    per_site_multiplicity=0,
                    occurrences=all_occs,
                )
            else:
                if n_near_precise >= n_near_offset:
                    role = SpatialRole.SITE_REGISTERED_PRECISE
                else:
                    role = SpatialRole.SITE_REGISTERED_OFFSET
                offset_vec = _compute_offset_vector(near_offset, composite_sites) if near_offset else None
                vfx_groups[vfx_name] = VFXGroupClassification(
                    vfx_name=vfx_name, role=role,
                    site_count=n_near_total, random_count=n_far,
                    per_site_multiplicity=n_near_total / n_sites if n_sites > 0 else 1.0,
                    offset_vector=offset_vec,
                    occurrences=all_occs,
                )
        else:
            role = SpatialRole.FIELD_RANDOM
            vfx_groups[vfx_name] = VFXGroupClassification(
                vfx_name=vfx_name, role=role,
                site_count=0, random_count=n_far,
                per_site_multiplicity=0,
                occurrences=all_occs,
            )

    # ── Pass 4: Classify blocks ──
    for bc in block_infos:
        if bc.is_nil_mobile:
            bc.role = SpatialRole.COMPOSITE_LEAD
            continue

        if bc.mobile_pos_gameplay is None:
            bc.role = SpatialRole.FIELD_RANDOM
            continue

        if not composite_sites:
            bc.role = SpatialRole.FIELD_RANDOM
            continue

        dist, site_j = _nearest_site_dist(bc.mobile_pos_gameplay, composite_sites)

        # Block role inherits from its primary VFX
        prim_grp = vfx_groups.get(bc.primary_vfx)
        if prim_grp and prim_grp.role == SpatialRole.CENTER_ONLY:
            bc.role = SpatialRole.CENTER_ONLY
            bc.assigned_site = None
            bc.is_site_instance = False
            continue

        if dist <= eps_offset:
            bc.assigned_site = site_j
            bc.is_site_instance = True
            if prim_grp:
                bc.role = prim_grp.role
            elif dist <= eps_precise:
                bc.role = SpatialRole.SITE_STACKED
            else:
                bc.role = SpatialRole.SITE_OFFSET
        else:
            bc.is_site_instance = False
            if prim_grp and prim_grp.role in (
                SpatialRole.SITE_REGISTERED_PRECISE,
                SpatialRole.SITE_REGISTERED_OFFSET,
                SpatialRole.FIELD_RANDOM,
            ):
                bc.role = prim_grp.role
            else:
                bc.role = SpatialRole.FIELD_RANDOM

    return SourceClassification(
        composite_sites=composite_sites,
        n_sites=n_sites,
        vfx_groups=vfx_groups,
        block_classifications=block_infos,
        nil_mobile_block_indices=nil_mobile_indices,
    )


def _compute_offset_vector(
    near_offset_occs: List[VFXOccurrence],
    composite_sites: List[Tuple[float, float]],
) -> Optional[Tuple[float, float]]:
    """Average offset from nearest composite site for offset occurrences."""
    dx_sum, dy_sum, cnt = 0.0, 0.0, 0
    for occ in near_offset_occs:
        _, sj = _nearest_site_dist((occ.gx, occ.gy), composite_sites)
        cs = composite_sites[sj]
        dx_sum += occ.gx - cs[0]
        dy_sum += occ.gy - cs[1]
        cnt += 1
    if cnt > 0:
        return (dx_sum / cnt, dy_sum / cnt)
    return None


# ── Pretty-print for debugging / UI ──────────────────────────────

def format_classification_summary(cls: SourceClassification) -> str:
    lines = [
        f"Composite sites: {cls.n_sites}",
        f"VFX groups: {len(cls.vfx_groups)}",
        f"TSimultaneousAction blocks: {len(cls.block_classifications)}",
        f"Nil-Mobile blocks: {len(cls.nil_mobile_block_indices)}",
        "",
    ]
    for role in SpatialRole:
        groups = [g for g in cls.vfx_groups.values() if g.role == role]
        if not groups:
            continue
        lines.append(f"  {role.name}:")
        for g in sorted(groups, key=lambda x: x.vfx_name):
            parts = [f"    {g.vfx_name}"]
            if g.site_count:
                parts.append(f"site={g.site_count}")
            if g.random_count:
                parts.append(f"random={g.random_count}")
            if g.per_site_multiplicity and g.per_site_multiplicity not in (0, 1.0):
                parts.append(f"mult={g.per_site_multiplicity:.1f}")
            if g.offset_vector:
                parts.append(f"offset=({g.offset_vector[0]:.1f},{g.offset_vector[1]:.1f})")
            lines.append("  ".join(parts))
    return "\n".join(lines)
