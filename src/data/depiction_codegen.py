"""Generate draft ``depiction_edits`` / ``new_depictions`` Python files.

Reads the audit output (``logs/depiction_audit.json``), the unit / new-unit
definitions, and ``depiction_data.json`` to emit one draft Python module per
flagged unit. Drafts land in a ``_generated/`` subfolder so they aren't picked
up by the faction ``__init__.py`` until promoted manually.

Usage:
    python -m src.data.depiction_codegen --all
    python -m src.data.depiction_codegen --unit Para_POL
    python -m src.data.depiction_codegen --faction POL

A small ``<Unit>.codegen.json`` diagnostic is written next to each draft with
the exact ``depiction_data`` lookups used.

For non-infantry units (ground vehicles, aerial) the codegen emits a stub
file containing a ``# TODO_CODEGEN:`` block listing the unhandled keys; the
geometry / mesh wiring for those is bespoke and must be hand-authored.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Tuple

from src.constants.unit_edits.replace_schema import ReplaceSpec, normalize_replace
from src.data.depiction_lookups import lookup as _dd_lookup
from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


# ---------------------------------------------------------------------------
# Configuration / classification
# ---------------------------------------------------------------------------

# Mapping from unit-name suffix to faction subdirectory prefix.
# Unit names use suffixes like ``_DDR`` / ``_US`` while the depiction-edit
# folder structure uses ``RDA_depiction_edits`` / ``USA_depiction_edits``.
_EXISTING_SUFFIX_TO_FACTION = {
    "POL": "POL",
    "SOV": "SOV",
    "UK": "UK",
    "US": "USA",
    "USA": "USA",
    "FR": "FR",
    "DDR": "RDA",
    "RDA": "RDA",
    "RFA": "RFA",
    "BEL": "BEL",
}
# new_depictions/ folder structure uses ``US_new_depictions`` (not ``USA``).
_NEW_SUFFIX_TO_FACTION = {
    "POL": "POL",
    "SOV": "SOV",
    "UK": "UK",
    "US": "US",
    "USA": "US",
    "FR": "FR",
    "DDR": "RDA",
    "RDA": "RDA",
    "RFA": "RFA",
    "BEL": "BEL",
}
_FACTION_SUFFIXES_SORTED = sorted(_EXISTING_SUFFIX_TO_FACTION.keys(), key=len, reverse=True)

_AERIAL_TOKENS = (
    "MiG_", "Su_", "F4", "F15", "F16", "F111", "FA16", "Phantom", "Harrier",
    "OV10", "L39", "Alpha_Jet", "Buccaneer", "AH1W", "G91",
    "Mi_24", "Mi_8", "Mi_2", "Mi_4", "Tornado", "Jaguar",
    "A4M", "A6", "A7D", "A10", "A_10",
)

_VEHICLE_TOKENS = (
    "Marder", "Bradley", "T34", "T_34", "T55", "T_55", "T62", "T_62", "T64", "T_64",
    "T72", "T_72", "T80", "T_80", "RM70", "RM_70", "ZSU", "DCA", "Tracked_Rapier",
    "TPZ_Fuchs", "MTLB", "MT_LB", "LAV", "BMP", "BTR", "BRDM", "MFRW",
    "M2_", "M3_", "M35", "M48", "M60", "M109", "M113", "M163",
    "Leopard", "Chieftain", "Challenger", "Centurion", "AMX", "Patton",
    "Spartan", "Scimitar", "Scorpion", "Stormer", "FV4", "FV5", "FV6",
    "Saracen", "Saladin", "OT_64", "OT_65", "Star_266", "Tatra",
    "Truck", "Jeep", "UAZ_", "GAZ_", "URAL", "GMC",
)

# Infantry-class name prefixes. Several infantry squads embed their
# transport vehicle in the unit id (``MotRifles_BTR_SOV``,
# ``Panzergrenadier_APC_RFA``, ``Cav_Scout_M3_US``), which would otherwise
# false-positive on the substring vehicle-token check below. Match these
# **first** -- pure-vehicle units always begin with the vehicle name
# (``Marder_1A3_MILAN_RFA``, ``ZSU_23_Shilka_POL``, ``T34_85M_DDR``), so
# this override is safe.
_INFANTRY_PREFIXES = (
    "Airmobile_", "ATteam_", "Cav_Scout_", "Commandos_", "DeltaForce_",
    "Engineers_", "Fallschirmjager_", "GreenBerets_", "Grenzer_", "Guards_",
    "HMGteam_", "HvyScout_", "LRRP_", "MANPAD_", "Marines_",
    "Mortier_paras_", "MotRifles_", "MotorizedRifles_", "MotShutzen_",
    "NatGuard_", "Naval_Rifle_", "Panzergrenadier_", "Para_", "Pathfinders_",
    "Pionniers_", "Recon_", "Reserve_", "Reservist_", "Rifles_", "Scout_",
    "Sniper_", "Spetsnaz_", "VDV_", "VIB_", "Volkspolizei_",
)


def _classify_unit(unit_name: str) -> str:
    """Return one of ``"infantry"``, ``"ground_vehicle"``, ``"aerial"``.

    Infantry-prefix check runs **before** the vehicle/aerial substring
    checks so squads whose name embeds the transport class
    (``MotRifles_BTR_SOV``) are not misclassified.
    """
    for prefix in _INFANTRY_PREFIXES:
        if unit_name.startswith(prefix):
            return "infantry"
    for tok in _AERIAL_TOKENS:
        if tok in unit_name:
            return "aerial"
    for tok in _VEHICLE_TOKENS:
        if tok in unit_name:
            return "ground_vehicle"
    return "infantry"


def _suffix_for_unit(unit_name: str) -> Optional[str]:
    for suffix in _FACTION_SUFFIXES_SORTED:
        if unit_name.endswith(f"_{suffix}"):
            return suffix
    return None


def _faction_for_existing(unit_name: str) -> Optional[str]:
    suffix = _suffix_for_unit(unit_name)
    return _EXISTING_SUFFIX_TO_FACTION.get(suffix) if suffix else None


def _faction_for_new(unit_name: str) -> Optional[str]:
    suffix = _suffix_for_unit(unit_name)
    return _NEW_SUFFIX_TO_FACTION.get(suffix) if suffix else None


# ---------------------------------------------------------------------------
# Depiction-data resolver
# ---------------------------------------------------------------------------


@dataclass
class ResolvedSpec:
    spec: ReplaceSpec
    donor_alt_index: Optional[int] = None  # index in WeaponAlternatives_<unit>
    donor_alt_selector: Optional[str] = None  # e.g. "WeaponAlternative_3"
    new_mesh_stem: Optional[str] = None  # e.g. "L7A2"
    new_fire_effect_tag: Optional[str] = None  # e.g. "FM_Tantal"
    new_animation_type: Optional[str] = None  # e.g. "kbk", "mmg"
    notes: List[str] = field(default_factory=list)

    def has_mesh_swap(self) -> bool:
        return self.new_mesh_stem is not None and self.donor_alt_index is not None

    def has_fire_effect_swap(self) -> bool:
        return self.spec.swap_fire_effect and self.new_fire_effect_tag is not None

    def has_animation_swap(self) -> bool:
        return self.new_animation_type is not None and self.donor_alt_selector is not None


def _resolve_spec(
    spec: ReplaceSpec,
    donor_unit: str,
    depiction_data: Mapping[str, Any],
) -> ResolvedSpec:
    resolved = ResolvedSpec(spec=spec)
    all_weapon_meshes: Mapping[str, Any] = depiction_data.get("all_weapon_meshes") or {}
    all_fire_effects: Mapping[str, Any] = depiction_data.get("all_fire_effects") or {}
    animation_weapon_map: Mapping[str, Any] = depiction_data.get("animation_weapon_map") or {}
    donor_block: Mapping[str, Any] = depiction_data.get(donor_unit) or {}
    weapon_alternatives = (donor_block.get("weapon_alternatives") or {}).get("alts") or {}
    weapon_subdepictions = donor_block.get("weapon_subdepictions") or {}

    # Locate the donor's WeaponAlternative slot for the OLD weapon.
    # ``weapon_subdepictions`` is keyed by the **vanilla** weapon id, so use
    # the rename-aware lookup to find post-rename ammo ids that the unit_edits
    # files reference (e.g. ``RocketInf_M72A3_LAW_66mm`` -> vanilla
    # ``RocketInf_M72_LAW_66mm``).
    sub = _dd_lookup(weapon_subdepictions, spec.old_weapon)
    if sub:
        wsd = sub.get("weapon_shoot_data", "")  # "WeaponShootData_0_<n>"
        m = re.search(r"_(\d+)$", wsd)
        if m:
            n = int(m.group(1))
            selector = f"WeaponAlternative_{n}"
            mesh_path = weapon_alternatives.get(selector)
            if mesh_path:
                resolved.donor_alt_index = n
                resolved.donor_alt_selector = selector
            else:
                resolved.notes.append(
                    f"donor has no {selector} entry in AllWeaponAlternatives"
                )
        else:
            resolved.notes.append(
                f"donor weapon_subdepiction for {spec.old_weapon!r} has no shoot-data index"
            )
    else:
        # Fallback: search alts by mesh stem.
        old_mesh_stem = _dd_lookup(all_weapon_meshes, spec.old_weapon)
        if old_mesh_stem:
            for selector, mesh_path in weapon_alternatives.items():
                if not isinstance(mesh_path, str):
                    continue
                if mesh_path.split("Modele_")[-1] == old_mesh_stem:
                    m = re.search(r"_(\d+)$", selector)
                    if m:
                        resolved.donor_alt_index = int(m.group(1))
                    resolved.donor_alt_selector = selector
                    break
        if resolved.donor_alt_selector is None:
            resolved.notes.append(
                f"donor has no weapon_subdepiction or mesh-matching alt for {spec.old_weapon!r}"
            )

    # New mesh / fire effect / animation type lookups -- post-rename names
    # in ``spec`` map to vanilla keys via ``_dd_lookup``.
    new_mesh_stem = _dd_lookup(all_weapon_meshes, spec.new_weapon)
    if new_mesh_stem:
        resolved.new_mesh_stem = new_mesh_stem
    else:
        resolved.notes.append(
            f"new mesh for {spec.new_weapon!r} not in depiction_data.all_weapon_meshes"
        )

    if spec.swap_fire_effect:
        new_fe = _dd_lookup(all_fire_effects, spec.new_weapon)
        if new_fe:
            resolved.new_fire_effect_tag = new_fe.replace("FireEffect_", "")
        else:
            resolved.notes.append(
                f"new fire effect for {spec.new_weapon!r} not in depiction_data.all_fire_effects"
            )

    new_anim = _dd_lookup(animation_weapon_map, spec.new_weapon)
    if new_anim:
        resolved.new_animation_type = new_anim
    else:
        resolved.notes.append(
            f"new animation type for {spec.new_weapon!r} not in animation_weapon_map "
            f"(animation tag may not need updating, or weapon type is novel)"
        )

    return resolved


# ---------------------------------------------------------------------------
# File emission
# ---------------------------------------------------------------------------

def _py_var_name(unit_name: str) -> str:
    return unit_name.lower()


_PY_HEADER = '"""Auto-generated draft from depiction_codegen. Review & promote.\n\nWhen promoting:\n  1. Move this file out of the ``_generated/`` folder (one level up).\n  2. Add the import + ``__all__`` (or registry) entry in the faction\n     ``__init__.py``.\n  3. Re-run the depiction audit to confirm the unit is no longer flagged.\n"""\n\nfrom typing import Dict, Tuple, Union\n'


def _format_indexed_ops_dict(
    ops: Dict[int, Tuple[str, List[Tuple[str, str]]]],
    indent: int = 16,
) -> str:
    pad = " " * indent
    lines = []
    for idx in sorted(ops.keys()):
        op_kind, fields = ops[idx]
        field_pairs = ", ".join(f'("{k}", "{v}")' for k, v in fields)
        lines.append(f'{pad}{idx}: ("{op_kind}", [{field_pairs}]),')
    return "\n".join(lines)


def _emit_infantry_existing_unit(
    unit_name: str,
    resolved: List[ResolvedSpec],
    valid_files: List[str],
) -> str:
    var_name = _py_var_name(unit_name)
    valid_files_lit = ", ".join(f'"{f}"' for f in valid_files)

    weapon_alt_ops: Dict[int, Tuple[str, List[Tuple[str, str]]]] = {}
    subdep_ops: Dict[int, Tuple[str, List[Tuple[str, str]]]] = {}
    soldier_ops: Dict[int, Tuple[str, List[Tuple[str, str]]]] = {}
    todos: List[str] = []

    soldier_op_index = 0
    for r in resolved:
        if r.donor_alt_index is None:
            todos.append(
                f"could not resolve donor WeaponAlternative for {r.spec.old_weapon!r} -> "
                f"{r.spec.new_weapon!r}: {'; '.join(r.notes) or 'no notes'}"
            )
            continue
        if r.has_mesh_swap():
            weapon_alt_ops[r.donor_alt_index] = (
                "edit",
                [("MeshDescriptor", r.new_mesh_stem)],
            )
        else:
            todos.append(
                f"WeaponAlternative_{r.donor_alt_index}: missing new mesh for "
                f"{r.spec.new_weapon!r}; {'; '.join(r.notes) or 'no notes'}"
            )
        if r.has_fire_effect_swap():
            subdep_ops[r.donor_alt_index] = (
                "edit",
                [("FireEffectTag", r.new_fire_effect_tag)],
            )
        if r.has_animation_swap():
            soldier_ops[soldier_op_index] = (
                "edit",
                [(r.new_animation_type, r.donor_alt_selector)],
            )
            soldier_op_index += 1

    sections: List[str] = []
    if weapon_alt_ops:
        sections.append(
            f'        ("AllWeaponAlternatives_{unit_name}", None): {{\n'
            f"{_format_indexed_ops_dict(weapon_alt_ops, indent=12)}\n"
            f'        }},'
        )
    if subdep_ops:
        sections.append(
            f'        ("AllWeaponSubDepiction_{unit_name}", "TemplateAllSubWeaponDepiction"): {{\n'
            f'            "Operators": {{\n'
            f"{_format_indexed_ops_dict(subdep_ops, indent=16)}\n"
            f'            }},\n'
            f'        }},'
        )
    if soldier_ops:
        sections.append(
            f'        ("TacticDepiction_{unit_name}_Soldier", "TemplateInfantryDepictionFactoryTactic"): {{\n'
            f'            "Operators": {{\n'
            f"{_format_indexed_ops_dict(soldier_ops, indent=16)}\n"
            f'            }},\n'
            f'        }},'
        )

    todo_block = ""
    if todos:
        todo_block = "\n".join(f"# TODO_CODEGEN: {t}" for t in todos) + "\n\n"

    body = "\n".join(sections) if sections else "        # TODO_CODEGEN: no resolvable depiction edits"

    return (
        f'"""{unit_name} depiction edits (auto-generated draft)."""\n\n'
        + todo_block
        + "from typing import Dict, Tuple, Union\n\n"
        + "# fmt: off\n"
        + f"{var_name}: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {{\n"
        + f'    "unit_name": "{unit_name}",\n'
        + f'    "valid_files": [{valid_files_lit}],\n'
        + f'    "DepictionInfantry_ndf": {{\n'
        + body + "\n"
        + "    },\n"
        + "}\n"
        + "# fmt: on\n"
    )


def _emit_infantry_new_unit(
    new_name: str,
    resolved: List[ResolvedSpec],
    valid_files: List[str],
) -> str:
    """Same structure as existing-unit infantry; differs only in the variable
    name convention and namespace -- the new unit will own its own
    ``AllWeaponAlternatives_<new_name>`` cloned at apply time."""
    return _emit_infantry_existing_unit(new_name, resolved, valid_files)


def _emit_stub(
    unit_name: str,
    classification: str,
    triggered_keys: List[str],
    notes: List[str],
) -> str:
    todo_lines = [
        f"# TODO_CODEGEN: {unit_name} classified as {classification!r} -- "
        f"depiction edits for this kind of unit are bespoke.",
        f"# TODO_CODEGEN: triggered equipmentchanges keys: {triggered_keys}",
    ]
    todo_lines.extend(f"# TODO_CODEGEN: {n}" for n in notes)
    var_name = _py_var_name(unit_name)
    return (
        f'"""{unit_name} depiction edits (auto-generated stub)."""\n\n'
        + "\n".join(todo_lines) + "\n\n"
        + "from typing import Dict, Tuple, Union\n\n"
        + "# fmt: off\n"
        + f"{var_name}: Dict[str, Dict[Union[str, Tuple[str, str]], dict]] = {{\n"
        + f'    "unit_name": "{unit_name}",\n'
        + f'    "valid_files": [],\n'
        + "}\n"
        + "# fmt: on\n"
    )


# ---------------------------------------------------------------------------
# Top-level driver
# ---------------------------------------------------------------------------

def _gather_targets(
    *,
    unit_filter: Optional[str],
    faction_filter: Optional[str],
    process_all: bool,
    audit_report: Mapping[str, Any],
) -> Tuple[List[Tuple[str, List[str]]], List[Tuple[str, str, List[str]]]]:
    """Return (existing, new) lists of audit hits to process.

    Each existing entry is ``(unit_name, equipmentchanges_keys)``.
    Each new-unit entry is ``(donor, new_name, equipmentchanges_keys)``.
    """
    existing: List[Tuple[str, List[str]]] = []
    new: List[Tuple[str, str, List[str]]] = []
    for entry in audit_report.get("existing_units", []):
        name = entry.get("unit_name")
        if not name:
            continue
        if unit_filter and unit_filter != name:
            continue
        if faction_filter:
            fac = _faction_for_existing(name)
            if fac != faction_filter:
                continue
        existing.append((name, list(entry.get("equipmentchanges_keys", []))))
    for entry in audit_report.get("new_units", []):
        donor = entry.get("donor")
        new_name = entry.get("new_name")
        if not new_name:
            continue
        if unit_filter and unit_filter != new_name:
            continue
        if faction_filter:
            fac = _faction_for_new(new_name)
            if fac != faction_filter:
                continue
        new.append((donor, new_name, list(entry.get("equipmentchanges_keys", []))))
    return existing, new


def _write_draft(
    out_dir: Path, unit_name: str, content: str, diagnostic: Mapping[str, Any]
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    py_path = out_dir / f"{unit_name}.py"
    diag_path = out_dir / f"{unit_name}.codegen.json"
    py_path.write_text(content, encoding="utf-8")
    diag_path.write_text(json.dumps(diagnostic, indent=2, default=str), encoding="utf-8")
    return py_path


def _process_existing_unit(
    unit_name: str,
    triggered_keys: List[str],
    project_root: Path,
    unit_edits: Mapping[str, Any],
    depiction_data: Mapping[str, Any],
) -> Optional[Path]:
    edits = unit_edits.get(unit_name)
    if not isinstance(edits, dict):
        logger.warning(f"codegen: {unit_name} not in unit_edits, skipping")
        return None

    faction = _faction_for_existing(unit_name)
    if faction is None:
        logger.warning(f"codegen: cannot determine faction for {unit_name}; skipping")
        return None

    out_dir = (
        project_root / "src" / "constants" / "unit_edits" / "depiction_edits"
        / f"{faction}_depiction_edits" / "_generated"
    )

    classification = _classify_unit(unit_name)
    weapon_descriptor = edits.get("WeaponDescriptor", {}) or {}
    equipment_changes = weapon_descriptor.get("equipmentchanges", {}) or {}
    raw_specs = normalize_replace(equipment_changes.get("replace"))
    # Drop per-row baked-in specs from the draft; the weapon mesh is part
    # of the hull/turret so no depiction wiring is needed for these rows.
    specs = [s for s in raw_specs if not s.depiction_baked_in]
    if raw_specs and not specs and not [k for k in triggered_keys if k != "replace"]:
        logger.info(
            f"codegen: skipping {unit_name} (all replace specs depiction_baked_in=True)"
        )
        return None
    out_of_scope = [k for k in triggered_keys if k != "replace"]

    diagnostic: Dict[str, Any] = {
        "unit_name": unit_name,
        "faction": faction,
        "classification": classification,
        "triggered_keys": triggered_keys,
        "out_of_scope_keys": out_of_scope,
        "specs": [],
    }

    if classification != "infantry":
        notes = []
        if out_of_scope:
            notes.append(f"unhandled keys: {out_of_scope}")
        if specs:
            notes.append(
                "replace specs detected; ground vehicles / aerial use bespoke "
                "DepictionVehicles_ndf or DepictionAerialUnits_ndf wiring."
            )
        content = _emit_stub(unit_name, classification, triggered_keys, notes)
        return _write_draft(out_dir, unit_name, content, diagnostic)

    resolved: List[ResolvedSpec] = []
    for spec in specs:
        r = _resolve_spec(spec, donor_unit=unit_name, depiction_data=depiction_data)
        resolved.append(r)
        diagnostic["specs"].append({
            "old_weapon": spec.old_weapon,
            "new_weapon": spec.new_weapon,
            "swap_fire_effect": spec.swap_fire_effect,
            "depiction_baked_in": spec.depiction_baked_in,
            "donor_alt_index": r.donor_alt_index,
            "donor_alt_selector": r.donor_alt_selector,
            "new_mesh_stem": r.new_mesh_stem,
            "new_fire_effect_tag": r.new_fire_effect_tag,
            "new_animation_type": r.new_animation_type,
            "notes": r.notes,
        })

    if not specs and out_of_scope:
        content = _emit_stub(unit_name, classification, triggered_keys, [
            f"out-of-scope keys for codegen: {out_of_scope}",
        ])
    else:
        valid_files = ["DepictionInfantry.ndf"]
        content = _emit_infantry_existing_unit(unit_name, resolved, valid_files)
        if out_of_scope:
            extra = "\n".join(
                f"# TODO_CODEGEN: hand-author handling for equipmentchanges key {k!r}"
                for k in out_of_scope
            )
            content = extra + "\n" + content

    return _write_draft(out_dir, unit_name, content, diagnostic)


def _process_new_unit(
    donor: str,
    new_name: str,
    triggered_keys: List[str],
    project_root: Path,
    new_units: Mapping[Any, Any],
    depiction_data: Mapping[str, Any],
) -> Optional[Path]:
    # Find the new-unit entry by NewName.
    edits: Optional[Mapping[str, Any]] = None
    for _key, candidate in new_units.items():
        if isinstance(candidate, dict) and candidate.get("NewName") == new_name:
            edits = candidate
            break
    if edits is None:
        logger.warning(f"codegen: new unit {new_name!r} not found in NEW_UNITS, skipping")
        return None

    faction = _faction_for_new(new_name)
    if faction is None:
        logger.warning(f"codegen: cannot determine faction for new unit {new_name}; skipping")
        return None

    out_dir = (
        project_root / "src" / "constants" / "new_units" / "new_depictions"
        / f"{faction}_new_depictions" / "_generated"
    )

    classification = _classify_unit(new_name)
    weapon_descriptor = edits.get("WeaponDescriptor", {}) or {}
    equipment_changes = weapon_descriptor.get("equipmentchanges", {}) or {}
    raw_specs = normalize_replace(equipment_changes.get("replace"))
    specs = [s for s in raw_specs if not s.depiction_baked_in]
    if raw_specs and not specs and not [k for k in triggered_keys if k != "replace"]:
        logger.info(
            f"codegen: skipping {new_name} (all replace specs depiction_baked_in=True)"
        )
        return None
    out_of_scope = [k for k in triggered_keys if k != "replace"]

    diagnostic: Dict[str, Any] = {
        "new_name": new_name,
        "donor": donor,
        "faction": faction,
        "classification": classification,
        "triggered_keys": triggered_keys,
        "out_of_scope_keys": out_of_scope,
        "specs": [],
    }

    if classification != "infantry":
        notes = []
        if out_of_scope:
            notes.append(f"unhandled keys: {out_of_scope}")
        if specs:
            notes.append("replace specs detected; non-infantry depictions are bespoke.")
        content = _emit_stub(new_name, classification, triggered_keys, notes)
        return _write_draft(out_dir, new_name, content, diagnostic)

    resolved: List[ResolvedSpec] = []
    for spec in specs:
        # The new unit will be cloned from `donor`; resolve against donor's
        # depiction data, but emit edits that target the NEW name's namespace.
        r = _resolve_spec(spec, donor_unit=donor, depiction_data=depiction_data)
        resolved.append(r)
        diagnostic["specs"].append({
            "old_weapon": spec.old_weapon,
            "new_weapon": spec.new_weapon,
            "swap_fire_effect": spec.swap_fire_effect,
            "depiction_baked_in": spec.depiction_baked_in,
            "donor_alt_index": r.donor_alt_index,
            "donor_alt_selector": r.donor_alt_selector,
            "new_mesh_stem": r.new_mesh_stem,
            "new_fire_effect_tag": r.new_fire_effect_tag,
            "new_animation_type": r.new_animation_type,
            "notes": r.notes,
        })

    valid_files = ["DepictionInfantry.ndf"]
    content = _emit_infantry_new_unit(new_name, resolved, valid_files)
    if out_of_scope:
        extra = "\n".join(
            f"# TODO_CODEGEN: hand-author handling for equipmentchanges key {k!r}"
            for k in out_of_scope
        )
        content = extra + "\n" + content
    return _write_draft(out_dir, new_name, content, diagnostic)


def _load_audit_report(project_root: Path) -> Mapping[str, Any]:
    audit_path = project_root / "logs" / "depiction_audit.json"
    if not audit_path.exists():
        logger.warning(
            f"depiction_audit.json not found at {audit_path}; running audit now."
        )
        from src.data.depiction_audit import run_depiction_audit
        return run_depiction_audit()
    with open(audit_path) as f:
        return json.load(f)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    g = parser.add_mutually_exclusive_group()
    g.add_argument("--unit", help="Only generate for this unit name")
    g.add_argument("--faction", help="Only generate for this faction code")
    g.add_argument("--all", action="store_true", help="Generate for every audit hit")
    args = parser.parse_args(argv)

    if not (args.unit or args.faction or args.all):
        parser.error("specify --unit NAME, --faction FAC, or --all")

    project_root = Path(__file__).resolve().parents[2]

    audit_report = _load_audit_report(project_root)

    from src.constants.new_units import NEW_UNITS
    from src.constants.unit_edits import load_unit_edits
    from src.data.depiction_audit import _load_depiction_data

    unit_edits = load_unit_edits()
    depiction_data = _load_depiction_data() or {}
    if not depiction_data:
        logger.warning(
            "depiction_data.json missing -- drafts will lack mesh/fire-effect lookups."
        )

    existing_targets, new_targets = _gather_targets(
        unit_filter=args.unit,
        faction_filter=args.faction,
        process_all=args.all,
        audit_report=audit_report,
    )

    written: List[Path] = []
    for unit_name, triggered_keys in existing_targets:
        path = _process_existing_unit(
            unit_name, triggered_keys, project_root, unit_edits, depiction_data,
        )
        if path:
            written.append(path)
            logger.info(f"wrote {path.relative_to(project_root)}")

    for donor, new_name, triggered_keys in new_targets:
        path = _process_new_unit(
            donor, new_name, triggered_keys, project_root, NEW_UNITS, depiction_data,
        )
        if path:
            written.append(path)
            logger.info(f"wrote {path.relative_to(project_root)}")

    logger.info(
        f"depiction_codegen wrote {len(written)} draft(s) "
        f"({len(existing_targets)} existing, {len(new_targets)} new)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
