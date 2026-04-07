"""Full scaling pipeline with spatial-classification-aware emit.

Parse -> classify -> layout composite sites -> emit per category -> budget
-> size params -> clamp -> serialize.
"""

from __future__ import annotations

import copy
import logging
import math
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

from src import ndf
from src.utils.ndf_utils import strip_quotes

from .budget import count_source_taction_calls
from .config import CalibrationConfig
from .extract import (
    apply_burst_position,
    clamp_positions_to_disk,
    set_first_wait_duration,
)
from .falloff import apply_falloff_position_bias, default_curve
from .layout import vogel_spiral_layout
from .naming import render_filename
from .ndf_io import (
    _SCATTER_NAMED_POSITION_KEYS,
    _list_row_child_v,
    action_short_from_taction,
    count_taction_calls,
    find_actions_list,
    list_tsimultaneous_rows,
    mobile_position_from_simultaneous,
    parse_float3_plus_par,
    parse_float3_plus_par_xyz,
    parse_ndf,
    serialize_ndf,
    stringify_position_expr,
    stringify_position_expr_xyz,
    update_export_name,
)
from .size_params import scale_size_params
from .spatial_classifier import (
    BlockClassification,
    SourceClassification,
    SpatialRole,
    VFXGroupClassification,
    _par_positions_from_taction,
    classify_source,
    format_classification_summary,
)

_log = logging.getLogger(__name__)


@dataclass
class ScaleResult:
    source_path: str
    target_radius_m: float
    output_path: str
    n_sites_target: int
    n_sites_effective: int
    taction_calls: int
    constrained: bool
    classification_summary: str = ""
    error: Optional[str] = None


@dataclass
class ScalerConfig:
    """All user-configurable knobs for the scaling pipeline."""

    source_radius_m: float = 60.0
    target_radii_m: List[float] = field(default_factory=list)
    rootname: str = ""
    output_dir: str = ""
    naming_template: str = "{rootname}_{radiusinmeters}m_{n}.ndf"
    taction_call_cap: int = 600
    min_burst_count: int = 3
    min_size_ratio: float = 0.3
    min_count_value: int = 1
    falloff_curve: List[float] = field(default_factory=default_curve)
    allowed_size_names: Optional[Set[str]] = None
    scale_sizes: bool = False
    scale_counts: bool = False

    calibration: CalibrationConfig = field(default_factory=CalibrationConfig)


# ── Nil-Mobile block expansion ────────────────────────────────────

def _extract_nil_mobile_branch_templates(
    sim: ndf.model.Object,
) -> Dict[str, List[Tuple[int, float, Tuple[float, float], Any]]]:
    """Extract per-VFX branch templates from a nil-Mobile block.

    Returns {vfx_name: [(branch_index, wait_s, (dx_ndf, dy_ndf), branch_row)]}
    """
    templates: Dict[str, List[Tuple[int, float, Tuple[float, float], Any]]] = defaultdict(list)
    for m in sim:
        if m.member != "Actions" or not isinstance(m.v, ndf.model.List):
            continue
        for bi, seq_row in enumerate(m.v):
            seq = _list_row_child_v(seq_row)
            if not isinstance(seq, ndf.model.Object) or seq.type != "TSequentialAction":
                continue
            wait_s = 0.0
            vfx_name = ""
            pos: Optional[Tuple[float, float]] = None
            for sm in seq:
                if sm.member != "Actions" or not isinstance(sm.v, ndf.model.List):
                    continue
                for step_row in sm.v:
                    o = _list_row_child_v(step_row)
                    if not isinstance(o, ndf.model.Object):
                        continue
                    if o.type == "TWaitInSec":
                        for wm in o:
                            if wm.member == "Duration":
                                wait_s = float(wm.v)
                    elif o.type == "TActionCall":
                        vfx_name = action_short_from_taction(o)
                        pars = _par_positions_from_taction(o)
                        if pars:
                            pos = pars[0]
            if vfx_name and pos is not None:
                templates[vfx_name].append((bi, wait_s, pos, seq_row))
    return templates


def _expand_nil_mobile_block(
    sim: ndf.model.Object,
    new_site_positions_ndf: List[Tuple[float, float]],
    source_waits: List[float],
) -> None:
    """Expand a nil-Mobile block to cover new_site_positions_ndf.

    Clears existing branches and rebuilds them for each new site position,
    using templates from the source block.
    """
    branch_templates = _extract_nil_mobile_branch_templates(sim)
    if not branch_templates:
        return

    actions_member = None
    for m in sim:
        if m.member == "Actions" and isinstance(m.v, ndf.model.List):
            actions_member = m.v
            break
    if actions_member is None:
        return

    # Collect non-positional branches (dummies, etc.) to preserve
    positional_vfx = set(branch_templates.keys())
    non_positional: List[Any] = []
    for bi, seq_row in enumerate(actions_member):
        seq = _list_row_child_v(seq_row)
        if not isinstance(seq, ndf.model.Object) or seq.type != "TSequentialAction":
            non_positional.append(seq_row)
            continue
        has_pos_vfx = False
        for sm in seq:
            if sm.member != "Actions" or not isinstance(sm.v, ndf.model.List):
                continue
            for step_row in sm.v:
                o = _list_row_child_v(step_row)
                if isinstance(o, ndf.model.Object) and o.type == "TActionCall":
                    vfx = action_short_from_taction(o)
                    if vfx in positional_vfx:
                        has_pos_vfx = True
        if not has_pos_vfx:
            non_positional.append(seq_row)

    # Clear the actions list
    while len(actions_member) > 0:
        del actions_member[-1]

    n_target = len(new_site_positions_ndf)

    # For each VFX type, create one branch per new site
    for vfx_name, tmpl_list in branch_templates.items():
        n_templates = len(tmpl_list)
        for site_j in range(n_target):
            tmpl_idx = site_j % n_templates
            _, _, _, template_row = tmpl_list[tmpl_idx]
            new_row = copy.deepcopy(template_row)

            # Update position
            target_ndf_x, target_ndf_y = new_site_positions_ndf[site_j]
            _update_branch_position(new_row, target_ndf_x, target_ndf_y)

            # Update wait time
            wait = source_waits[site_j % len(source_waits)] if source_waits else 0.2
            _update_branch_wait(new_row, wait)

            actions_member.add(new_row)

    # Re-add non-positional branches
    for row in non_positional:
        actions_member.add(copy.deepcopy(row))


def _update_branch_position(
    seq_row: Any,
    dx_ndf: float,
    dy_ndf: float,
) -> None:
    """Update scatter-named positions (parPositionRelative, parStartPosition, etc.)
    in a TSequentialAction branch row, preserving the original Z component."""
    seq = _list_row_child_v(seq_row)
    if not isinstance(seq, ndf.model.Object):
        return

    def walk(node: Any) -> None:
        if isinstance(node, ndf.model.Object):
            if node.type == "TActionCall":
                for member in node:
                    if member.member != "NamedParams" or not isinstance(member.v, ndf.model.Map):
                        continue
                    for mr in member.v:
                        key = strip_quotes(str(mr.k)) if mr.k is not None else ""
                        if key not in _SCATTER_NAMED_POSITION_KEYS:
                            continue
                        old_text = ndf.printer.string(mr.v).strip()
                        old_xyz = parse_float3_plus_par_xyz(old_text)
                        old_z = old_xyz[2] if old_xyz else 0.0
                        mr.v = stringify_position_expr_xyz(dx_ndf, dy_ndf, old_z)
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

    walk(seq)


def _update_branch_wait(seq_row: Any, wait_s: float) -> None:
    """Update the leading TWaitInSec.Duration in a branch row."""
    seq = _list_row_child_v(seq_row)
    if not isinstance(seq, ndf.model.Object):
        return

    def walk(node: Any) -> bool:
        if isinstance(node, ndf.model.Object):
            if node.type == "TWaitInSec":
                for m in node:
                    if m.member == "Duration":
                        m.v = round(float(wait_s), 2)
                        return True
                return False
            for m in node:
                if walk(m.v):
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

    walk(seq)


# ── Collect source wait times for stagger ─────────────────────────

def _collect_source_wait_pool(
    actions: ndf.model.List,
) -> List[float]:
    """Gather leading wait values from Mobile-positioned blocks for
    timing stagger assignment to new sites."""
    out: List[float] = []
    for row in list_tsimultaneous_rows(actions):
        sim = row.v
        if not isinstance(sim, ndf.model.Object):
            continue
        mob = mobile_position_from_simultaneous(sim)
        if mob is None:
            continue
        for m in sim:
            if m.member != "Actions" or not isinstance(m.v, ndf.model.List):
                continue
            for seq_row in m.v:
                seq = _list_row_child_v(seq_row)
                if not isinstance(seq, ndf.model.Object) or seq.type != "TSequentialAction":
                    continue
                for sm in seq:
                    if sm.member != "Actions" or not isinstance(sm.v, ndf.model.List):
                        continue
                    for step_row in sm.v:
                        o = _list_row_child_v(step_row)
                        if isinstance(o, ndf.model.Object) and o.type == "TWaitInSec":
                            for wm in o:
                                if wm.member == "Duration":
                                    out.append(round(float(wm.v), 2))
                break
            break
    return out or [0.2, 0.35, 0.7, 0.75, 1.25]


# ── Budget computation with priority ─────────────────────────────

def _compute_budget_counts(
    cls: SourceClassification,
    n_target: int,
    cap: int,
    source_total_calls: int,
    n_source: int,
) -> Tuple[int, Dict[str, int], bool]:
    """Compute per-category instance counts that fit within the call cap.

    Returns (n_sites_effective, random_counts_by_vfx, constrained).
    """
    if n_source <= 0 or source_total_calls <= 0:
        return n_target, {}, False

    # Calls per composite site from site-bound blocks only
    site_calls = 0
    for bc in cls.block_classifications:
        if bc.is_site_instance and bc.assigned_site == 0:
            site_calls += bc.n_taction_calls

    # Add calls from nil-Mobile blocks (divided by n_source = per-site share)
    for idx in cls.nil_mobile_block_indices:
        for bc in cls.block_classifications:
            if bc.block_index == idx:
                site_calls += bc.n_taction_calls // max(1, n_source)
                break

    calls_per_site = max(1, site_calls)

    # Compute random calls per source site ratio
    random_calls_total = 0
    random_vfx_calls: Dict[str, int] = {}
    for bc in cls.block_classifications:
        if not bc.is_site_instance and not bc.is_nil_mobile and bc.role != SpatialRole.CENTER_ONLY:
            random_calls_total += bc.n_taction_calls
            for vn in bc.vfx_names:
                random_vfx_calls[vn] = random_vfx_calls.get(vn, 0) + bc.n_taction_calls

    # Center-only calls (fixed)
    center_calls = sum(
        bc.n_taction_calls for bc in cls.block_classifications
        if bc.role == SpatialRole.CENTER_ONLY
    )

    # Scale random counts
    sf = n_target / max(1, n_source)
    random_counts: Dict[str, int] = {}
    for vfx, grp in cls.vfx_groups.items():
        if grp.random_count > 0:
            random_counts[vfx] = max(1, round(grp.random_count * sf))

    # Estimate total calls
    site_total = n_target * calls_per_site
    random_total = sum(random_counts.values())
    total_est = site_total + random_total + center_calls

    constrained = total_est > cap
    n_eff = n_target

    if constrained:
        # Phase 1: reduce random counts proportionally
        available_for_random = cap - center_calls - n_target * calls_per_site
        if available_for_random > 0 and random_total > 0:
            ratio = available_for_random / random_total
            for vfx in random_counts:
                random_counts[vfx] = max(1, round(random_counts[vfx] * ratio))
            random_total = sum(random_counts.values())
            total_est = n_target * calls_per_site + random_total + center_calls

        # Phase 2: if still over, reduce site count
        if total_est > cap:
            min_random = len(random_counts)
            available_for_sites = cap - center_calls - min_random
            if available_for_sites > 0 and calls_per_site > 0:
                n_eff = max(3, min(n_target, int(available_for_sites / calls_per_site)))
            else:
                n_eff = max(3, n_target)
            # Re-compute random at reduced scale
            sf2 = n_eff / max(1, n_source)
            for vfx, grp in cls.vfx_groups.items():
                if grp.random_count > 0:
                    random_counts[vfx] = max(1, round(grp.random_count * sf2))

    return n_eff, random_counts, constrained


# ── Set Mobile position on a sim block ────────────────────────────

def _set_mobile_position(sim: ndf.model.Object, dx_ndf: float, dy_ndf: float) -> bool:
    if sim.type != "TSimultaneousAction":
        return False
    expr = stringify_position_expr(dx_ndf, dy_ndf)
    for m in sim:
        if m.member != "Mobile" or not isinstance(m.v, ndf.model.Object):
            continue
        mob = m.v
        if mob.type != "TMobileWithLocalRepereMatrixFactory":
            continue
        for mm in mob:
            if mm.member == "Position":
                mm.v = expr
                return True
    return False


# ── Main scaling pipeline ─────────────────────────────────────────

def scale_single_file(
    source_path: Path,
    target_radius_m: float,
    config: ScalerConfig,
) -> ScaleResult:
    """Run the full spatially-classified pipeline for one source at one target radius."""
    cal = config.calibration
    ref_m = cal.reference_gameplay_radius_m
    anchor_r = cal.anchor_max_ndf_radius
    source_m = config.source_radius_m

    try:
        text = source_path.read_text(encoding="utf-8")
        parsed = parse_ndf(text)

        # Classify source
        cls = classify_source(parsed, ref_m, anchor_r)
        n_source = cls.n_sites
        if n_source <= 0:
            n_source = 10

        classification_summary = format_classification_summary(cls)
        _log.info("Source classification:\n%s", classification_summary)

        # Source call count
        total_src_calls = count_source_taction_calls(parsed)

        # Target site count
        sf = target_radius_m / source_m if source_m > 0 else 1.0
        n_target = max(config.min_burst_count, round(n_source * sf))

        # Budget
        n_eff, random_counts, constrained = _compute_budget_counts(
            cls, n_target, config.taction_call_cap, total_src_calls, n_source,
        )

        # Layout: compute new composite site positions
        site_positions_gp = vogel_spiral_layout(n_eff, target_radius_m)

        # Apply falloff to site positions
        site_positions_gp = apply_falloff_position_bias(
            site_positions_gp, config.falloff_curve, target_radius_m,
        )

        # Convert to NDF coordinates
        inv = anchor_r / ref_m if ref_m > 0 else 1.0
        site_positions_ndf = [
            (float(int(round(gx * inv))), float(int(round(gy * inv))))
            for gx, gy in site_positions_gp
        ]

        # Collect source wait pool for timing stagger
        actions = find_actions_list(parsed)
        if actions is None:
            return ScaleResult(
                source_path=str(source_path), target_radius_m=target_radius_m,
                output_path="", n_sites_target=n_target, n_sites_effective=0,
                taction_calls=0, constrained=constrained,
                classification_summary=classification_summary,
                error="No Actions list in source NDF",
            )
        source_waits = _collect_source_wait_pool(actions)
        rows = list_tsimultaneous_rows(actions)

        # ── Emit: clear Actions and rebuild per category ──
        # Save references to source blocks before clearing
        source_rows = list(rows)

        # Build per-site template mapping: for site 0, which block indices
        # are site-bound?
        site0_templates: Dict[int, Any] = {}
        for bc in cls.block_classifications:
            if bc.is_site_instance and bc.assigned_site == 0 and not bc.is_nil_mobile:
                site0_templates[bc.block_index] = source_rows[bc.block_index]

        # Also collect templates for other sites to add diversity
        site_templates_by_site: Dict[int, Dict[int, Any]] = defaultdict(dict)
        for bc in cls.block_classifications:
            if bc.is_site_instance and not bc.is_nil_mobile and bc.assigned_site is not None:
                site_templates_by_site[bc.assigned_site][bc.block_index] = source_rows[bc.block_index]

        # Random block templates (grouped by primary VFX)
        random_templates: Dict[str, List[Any]] = defaultdict(list)
        for bc in cls.block_classifications:
            if not bc.is_site_instance and not bc.is_nil_mobile and bc.role != SpatialRole.CENTER_ONLY:
                random_templates[bc.primary_vfx].append(source_rows[bc.block_index])

        # Center-only blocks
        center_blocks: List[Any] = []
        for bc in cls.block_classifications:
            if bc.role == SpatialRole.CENTER_ONLY:
                center_blocks.append(source_rows[bc.block_index])

        # Nil-Mobile blocks
        nil_mobile_blocks: List[Any] = []
        for idx in cls.nil_mobile_block_indices:
            nil_mobile_blocks.append(source_rows[idx])

        # Clear Actions
        while len(actions) > 0:
            del actions[-1]

        cluster_radius_scale = target_radius_m / source_m if source_m > 0 else 1.0

        # 1. Emit site-bound Mobile blocks for each new site
        for site_j in range(n_eff):
            # Pick source site for template diversity
            source_site = site_j % n_source
            templates = site_templates_by_site.get(source_site, site0_templates)
            if not templates:
                templates = site0_templates

            target_ndf = site_positions_ndf[site_j]
            target_gp = site_positions_gp[site_j]
            wait = source_waits[site_j % len(source_waits)]

            # Find the composite site position for this source site
            source_site_gp = cls.composite_sites[source_site] if source_site < len(cls.composite_sites) else (0.0, 0.0)

            for bi, tmpl_row in templates.items():
                new_row = copy.deepcopy(tmpl_row)
                sim = new_row.v
                if not isinstance(sim, ndf.model.Object) or sim.type != "TSimultaneousAction":
                    continue

                # Determine if this block has an offset from the composite site
                bc_match = None
                for bc in cls.block_classifications:
                    if bc.block_index == bi:
                        bc_match = bc
                        break

                if bc_match and bc_match.mobile_pos_gameplay and bc_match.role == SpatialRole.SITE_OFFSET:
                    # Preserve scaled offset from composite site
                    src_mob = bc_match.mobile_pos_gameplay
                    offset_gx = src_mob[0] - source_site_gp[0]
                    offset_gy = src_mob[1] - source_site_gp[1]
                    new_gx = target_gp[0] + offset_gx * cluster_radius_scale
                    new_gy = target_gp[1] + offset_gy * cluster_radius_scale
                    new_ndf_x = float(int(round(new_gx * inv)))
                    new_ndf_y = float(int(round(new_gy * inv)))
                    _set_mobile_position(sim, new_ndf_x, new_ndf_y)
                else:
                    _set_mobile_position(sim, target_ndf[0], target_ndf[1])

                set_first_wait_duration(sim, wait)
                actions.add(new_row)

        # 2. Emit nil-Mobile blocks (expanded with new site entries)
        for nil_row in nil_mobile_blocks:
            new_row = copy.deepcopy(nil_row)
            sim = new_row.v
            if isinstance(sim, ndf.model.Object) and sim.type == "TSimultaneousAction":
                _expand_nil_mobile_block(sim, site_positions_ndf, source_waits)
            actions.add(new_row)

        # 3. Emit random blocks (scaled count)
        random_positions_gp = vogel_spiral_layout(
            sum(random_counts.values()) + 1,
            target_radius_m,
        )
        random_positions_gp = apply_falloff_position_bias(
            random_positions_gp, config.falloff_curve, target_radius_m,
        )
        rnd_idx = 0
        for vfx_name, count in random_counts.items():
            templates_for_vfx = random_templates.get(vfx_name, [])
            if not templates_for_vfx:
                continue
            for k in range(count):
                tmpl = templates_for_vfx[k % len(templates_for_vfx)]
                new_row = copy.deepcopy(tmpl)
                sim = new_row.v
                if not isinstance(sim, ndf.model.Object) or sim.type != "TSimultaneousAction":
                    continue
                if rnd_idx < len(random_positions_gp):
                    rgx, rgy = random_positions_gp[rnd_idx]
                else:
                    rgx, rgy = 0.0, 0.0
                rnd_idx += 1
                rndf_x = float(int(round(rgx * inv)))
                rndf_y = float(int(round(rgy * inv)))
                _set_mobile_position(sim, rndf_x, rndf_y)
                wait = source_waits[k % len(source_waits)]
                set_first_wait_duration(sim, wait)
                actions.add(new_row)

        # 4. Emit site-registered random instances
        # (these are VFX that have both site and random instances --
        # the site instances were already emitted with the site blocks,
        # so here we only emit the ADDITIONAL random instances)
        # Already handled above via random_counts which includes
        # site_registered random components.

        # 5. Keep center-only blocks
        for center_row in center_blocks:
            actions.add(copy.deepcopy(center_row))

        # Scale size/count params (only when enabled)
        if config.scale_sizes or config.scale_counts:
            from .size_params import is_size_param, is_count_param
            effective_size_names = config.allowed_size_names
            if not config.scale_sizes:
                effective_size_names = set()
            scale_size_params(
                parsed, sf,
                min_size_ratio=config.min_size_ratio,
                min_count_value=config.min_count_value,
                allowed_size_names=effective_size_names,
                scale_counts_enabled=config.scale_counts,
            )

        # Clamp positions to target disk
        clamp_positions_to_disk(
            parsed, radius_m=target_radius_m, ref_m=ref_m, anchor_r=anchor_r,
        )

        # Update export name
        out_name = render_filename(
            config.naming_template, config.rootname,
            target_radius_m, source_path.stem,
        )
        out_stem = Path(out_name).stem
        update_export_name(parsed, out_stem)

        # Count actual TActionCalls
        actual_calls = count_taction_calls(parsed)
        if actual_calls > config.taction_call_cap * 1.05:
            _log.warning(
                "TActionCall count %d exceeds cap %d by >5%% for %s @ %gm",
                actual_calls, config.taction_call_cap, source_path.name, target_radius_m,
            )

        # Serialize and write
        out_dir = Path(config.output_dir)
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / out_name
        out_text = serialize_ndf(parsed)
        out_path.write_text(out_text, encoding="utf-8")

        return ScaleResult(
            source_path=str(source_path),
            target_radius_m=target_radius_m,
            output_path=str(out_path),
            n_sites_target=n_target,
            n_sites_effective=n_eff,
            taction_calls=actual_calls,
            constrained=constrained,
            classification_summary=classification_summary,
        )
    except Exception as exc:
        _log.exception("Error scaling %s @ %gm", source_path.name, target_radius_m)
        return ScaleResult(
            source_path=str(source_path),
            target_radius_m=target_radius_m,
            output_path="",
            n_sites_target=0,
            n_sites_effective=0,
            taction_calls=0,
            constrained=False,
            error=str(exc),
        )


def scale_single_file_in_memory(
    source_text: str,
    target_radius_m: float,
    config: ScalerConfig,
) -> Tuple[Optional[ndf.model.List], ScaleResult]:
    """Run the scaling pipeline and return the modified tree (no file I/O).

    Used by the scatter preview to get the emitted NDF tree for dot extraction.
    """
    cal = config.calibration
    ref_m = cal.reference_gameplay_radius_m
    anchor_r = cal.anchor_max_ndf_radius
    source_m = config.source_radius_m

    try:
        parsed = parse_ndf(source_text)
        cls = classify_source(parsed, ref_m, anchor_r)
        n_source = cls.n_sites or 10
        total_src_calls = count_source_taction_calls(parsed)

        sf = target_radius_m / source_m if source_m > 0 else 1.0
        n_target = max(config.min_burst_count, round(n_source * sf))
        n_eff, random_counts, constrained = _compute_budget_counts(
            cls, n_target, config.taction_call_cap, total_src_calls, n_source,
        )

        site_positions_gp = vogel_spiral_layout(n_eff, target_radius_m)
        site_positions_gp = apply_falloff_position_bias(
            site_positions_gp, config.falloff_curve, target_radius_m,
        )
        inv = anchor_r / ref_m if ref_m > 0 else 1.0
        site_positions_ndf = [
            (float(int(round(gx * inv))), float(int(round(gy * inv))))
            for gx, gy in site_positions_gp
        ]

        actions = find_actions_list(parsed)
        if actions is None:
            return None, ScaleResult(
                source_path="<memory>", target_radius_m=target_radius_m,
                output_path="", n_sites_target=n_target, n_sites_effective=0,
                taction_calls=0, constrained=constrained,
                error="No Actions list",
            )

        source_waits = _collect_source_wait_pool(actions)
        rows = list_tsimultaneous_rows(actions)
        source_rows = list(rows)

        site0_templates: Dict[int, Any] = {}
        site_templates_by_site: Dict[int, Dict[int, Any]] = defaultdict(dict)
        random_templates: Dict[str, List[Any]] = defaultdict(list)
        center_blocks: List[Any] = []
        nil_mobile_blocks: List[Any] = []

        for bc in cls.block_classifications:
            if bc.is_site_instance and not bc.is_nil_mobile and bc.assigned_site is not None:
                site_templates_by_site[bc.assigned_site][bc.block_index] = source_rows[bc.block_index]
                if bc.assigned_site == 0:
                    site0_templates[bc.block_index] = source_rows[bc.block_index]
            elif not bc.is_site_instance and not bc.is_nil_mobile and bc.role != SpatialRole.CENTER_ONLY:
                random_templates[bc.primary_vfx].append(source_rows[bc.block_index])
            elif bc.role == SpatialRole.CENTER_ONLY:
                center_blocks.append(source_rows[bc.block_index])

        for idx in cls.nil_mobile_block_indices:
            nil_mobile_blocks.append(source_rows[idx])

        while len(actions) > 0:
            del actions[-1]

        cluster_radius_scale = target_radius_m / source_m if source_m > 0 else 1.0

        for site_j in range(n_eff):
            source_site = site_j % n_source
            templates = site_templates_by_site.get(source_site, site0_templates)
            if not templates:
                templates = site0_templates
            target_ndf = site_positions_ndf[site_j]
            target_gp = site_positions_gp[site_j]
            wait = source_waits[site_j % len(source_waits)]
            source_site_gp = cls.composite_sites[source_site] if source_site < len(cls.composite_sites) else (0.0, 0.0)

            for bi, tmpl_row in templates.items():
                new_row = copy.deepcopy(tmpl_row)
                sim = new_row.v
                if not isinstance(sim, ndf.model.Object) or sim.type != "TSimultaneousAction":
                    continue
                bc_match = next((bc for bc in cls.block_classifications if bc.block_index == bi), None)
                if bc_match and bc_match.mobile_pos_gameplay and bc_match.role == SpatialRole.SITE_OFFSET:
                    offset_gx = bc_match.mobile_pos_gameplay[0] - source_site_gp[0]
                    offset_gy = bc_match.mobile_pos_gameplay[1] - source_site_gp[1]
                    new_gx = target_gp[0] + offset_gx * cluster_radius_scale
                    new_gy = target_gp[1] + offset_gy * cluster_radius_scale
                    _set_mobile_position(sim, float(int(round(new_gx * inv))), float(int(round(new_gy * inv))))
                else:
                    _set_mobile_position(sim, target_ndf[0], target_ndf[1])
                set_first_wait_duration(sim, wait)
                actions.add(new_row)

        for nil_row in nil_mobile_blocks:
            new_row = copy.deepcopy(nil_row)
            sim = new_row.v
            if isinstance(sim, ndf.model.Object) and sim.type == "TSimultaneousAction":
                _expand_nil_mobile_block(sim, site_positions_ndf, source_waits)
            actions.add(new_row)

        random_positions_gp = vogel_spiral_layout(
            sum(random_counts.values()) + 1, target_radius_m,
        )
        random_positions_gp = apply_falloff_position_bias(
            random_positions_gp, config.falloff_curve, target_radius_m,
        )
        rnd_idx = 0
        for vfx_name, count in random_counts.items():
            tmpl_list = random_templates.get(vfx_name, [])
            if not tmpl_list:
                continue
            for k in range(count):
                tmpl = tmpl_list[k % len(tmpl_list)]
                new_row = copy.deepcopy(tmpl)
                sim = new_row.v
                if not isinstance(sim, ndf.model.Object):
                    continue
                if rnd_idx < len(random_positions_gp):
                    rgx, rgy = random_positions_gp[rnd_idx]
                else:
                    rgx, rgy = 0.0, 0.0
                rnd_idx += 1
                _set_mobile_position(sim, float(int(round(rgx * inv))), float(int(round(rgy * inv))))
                set_first_wait_duration(sim, source_waits[k % len(source_waits)])
                actions.add(new_row)

        for center_row in center_blocks:
            actions.add(copy.deepcopy(center_row))

        if config.scale_sizes or config.scale_counts:
            from .size_params import is_size_param, is_count_param
            effective_size_names = config.allowed_size_names
            if not config.scale_sizes:
                effective_size_names = set()
            scale_size_params(
                parsed, sf,
                min_size_ratio=config.min_size_ratio,
                min_count_value=config.min_count_value,
                allowed_size_names=effective_size_names,
                scale_counts_enabled=config.scale_counts,
            )
        clamp_positions_to_disk(
            parsed, radius_m=target_radius_m, ref_m=ref_m, anchor_r=anchor_r,
        )

        actual_calls = count_taction_calls(parsed)
        result = ScaleResult(
            source_path="<memory>",
            target_radius_m=target_radius_m,
            output_path="",
            n_sites_target=n_target,
            n_sites_effective=n_eff,
            taction_calls=actual_calls,
            constrained=constrained,
            classification_summary=format_classification_summary(cls),
        )
        return parsed, result

    except Exception as exc:
        return None, ScaleResult(
            source_path="<memory>", target_radius_m=target_radius_m,
            output_path="", n_sites_target=0, n_sites_effective=0,
            taction_calls=0, constrained=False, error=str(exc),
        )


def scale_batch(
    source_paths: List[Path],
    config: ScalerConfig,
    *,
    progress_callback=None,
) -> List[ScaleResult]:
    """Scale all source files at all target radii."""
    results: List[ScaleResult] = []
    total = len(source_paths) * len(config.target_radii_m)
    done = 0
    for src in source_paths:
        for target_m in config.target_radii_m:
            result = scale_single_file(src, target_m, config)
            results.append(result)
            done += 1
            if progress_callback:
                progress_callback(done, total, result)
    return results
