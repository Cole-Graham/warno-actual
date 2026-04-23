"""Functions for gathering weapon depiction data."""

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict

from src import ndf
from src.constants.weapons.vanilla_inst_modifications import MERGED_RENAMES
from src.data.ammo_data import get_vanilla_renames
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type, strip_quotes

logger = setup_logger(__name__)


def gather_depiction_data(mod_src_path: Path) -> Dict[str, Any]:
    """Gather depiction data from DepictionInfantry.ndf.

    Per-unit dict structure (back-compat keys preserved for existing consumers):

    - ``weapon_alternatives.alts``      : ``{SelectorId: MeshDescriptor}`` (legacy)
    - ``weapon_alternatives.reference`` : ``{SelectorId: ReferenceMeshForSkeleton}`` (legacy)
    - ``weapon_alternatives.rows``      : ordered list of ``{index, type, selector_id, mesh, reference_mesh}`` (full row dump)
    - ``weapon_subdepictions``          : legacy ``{weapon_name: {...}}`` from ``DepictionOperator_WeaponInstantFireInfantry`` only
    - ``weapon_subdepictions_operators``: ordered list of ``{index, type, ...}`` covering every operator on the SubDepiction
    - ``tactic_alternatives``           : legacy single dict (last LOD_High row encountered)
    - ``tactic_alternatives_rows``      : ordered list of ``{index, lod, selector_number, mesh}`` for every TDepictionVisual row
    - ``tactic_soldier``                : ``{selector_tactic, animation_tags, operators[]}``
    - ``tactic_ghost``                  : ``{selector_tactic, operators[]}``
    - ``transported_infantry``          : list of ``{count, unique_count, identifier, meshes[]}`` rows referencing this unit
    """
    logger.info("Gathering depiction data from DepictionInfantry.ndf")

    depiction_data: Dict[str, Any] = {}

    template_data_entry = {
        "weapon_alternatives": {"alts": {}, "reference": {}, "rows": []},
        "weapon_subdepictions": {},
        "weapon_subdepictions_operators": [],
        "tactic_alternatives": {},
        "tactic_alternatives_rows": [],
        "tactic_soldier": {"selector_tactic": "", "animation_tags": {}, "operators": []},
        "tactic_ghost": {"selector_tactic": "", "operators": []},
        "transported_infantry": [],
    }

    all_fire_effects: Dict[str, str] = {}
    all_weapon_meshes: Dict[str, str] = {}
    all_animation_tags: Dict[str, Any] = {}
    animation_weapon_map: Dict[str, str] = {}

    try:
        mod = ndf.Mod(str(mod_src_path), "None")
        logger.debug(f"Created NDF mod for path: {mod_src_path}")

        ammo_ndf_path = "GameData/Generated/Gameplay/Gfx/Ammunition.ndf"
        missiles_ndf_path = "GameData/Generated/Gameplay/Gfx/AmmunitionMissiles.ndf"
        all_renames = _build_all_renames(mod, ammo_ndf_path, missiles_ndf_path)

        infantry_ndf_path = "GameData/Generated/Gameplay/Gfx/Infanterie/DepictionInfantry.ndf"
        logger.debug(f"Attempting to parse: {infantry_ndf_path}")

        try:
            infantry_parse_source = mod.parse_src(infantry_ndf_path)
            logger.debug("Successfully parsed infantry NDF file")
        except Exception as e:
            logger.error(f"Failed to parse infantry NDF file: {str(e)}")
            return depiction_data

        def _ensure_unit(unit_name: str) -> Dict[str, Any]:
            if unit_name not in depiction_data:
                depiction_data[unit_name] = deepcopy(template_data_entry)
            return depiction_data[unit_name]

        logger.debug("Starting to process entries...")

        for entry in infantry_parse_source:
            try:
                ns = getattr(entry, "namespace", None) or ""

                if ns.startswith("AllWeaponAlternatives_"):
                    unit = ns[len("AllWeaponAlternatives_"):]
                    if unit:
                        _ensure_unit(unit)
                        _process_weapon_alternatives(entry, depiction_data[unit], unit)

                elif ns.startswith("AllWeaponSubDepiction_"):
                    unit = ns[len("AllWeaponSubDepiction_"):]
                    if unit:
                        _ensure_unit(unit)
                        _process_weapon_subdepiction(
                            entry,
                            depiction_data[unit],
                            unit,
                            all_renames,
                            all_fire_effects,
                            all_weapon_meshes,
                        )

                elif ns.startswith("TacticDepiction_") and ns.endswith("_Alternatives"):
                    unit = ns[len("TacticDepiction_"):-len("_Alternatives")]
                    if unit:
                        _ensure_unit(unit)
                        _process_tactic_alternatives(entry, depiction_data[unit], unit)

                elif ns.startswith("TacticDepiction_") and ns.endswith("_Soldier"):
                    unit = ns[len("TacticDepiction_"):-len("_Soldier")]
                    if unit:
                        _ensure_unit(unit)
                        _process_tactic_soldier(
                            entry,
                            depiction_data[unit],
                            unit,
                            all_animation_tags,
                            animation_weapon_map,
                        )

                elif ns.startswith("TacticDepiction_") and ns.endswith("_Ghost"):
                    unit = ns[len("TacticDepiction_"):-len("_Ghost")]
                    if unit:
                        _ensure_unit(unit)
                        _process_tactic_ghost(entry, depiction_data[unit], unit)

                else:
                    _maybe_process_transported_catalog(entry, depiction_data, _ensure_unit)

            except Exception as e:
                logger.error(f"Error processing entry: {str(e)}")
                continue

        all_animation_tags = {k: sorted(list(v)) for k, v in all_animation_tags.items()}

        depiction_data["all_fire_effects"] = all_fire_effects
        depiction_data["all_weapon_meshes"] = all_weapon_meshes
        depiction_data["all_animation_tags"] = all_animation_tags
        depiction_data["animation_weapon_map"] = animation_weapon_map

        unit_count = sum(
            1
            for k in depiction_data
            if k not in ("all_fire_effects", "all_weapon_meshes", "all_animation_tags", "animation_weapon_map")
        )
        logger.info(f"Gathered depiction data for {unit_count} units")
        logger.info(f"Gathered {len(all_fire_effects)} total fire effects")
        logger.info(f"Gathered {len(all_animation_tags)} unique weapon types")
        logger.debug(f"Final depiction data: {json.dumps(depiction_data, indent=4)}")

        return depiction_data

    except Exception as e:
        logger.error(f"Error gathering depiction data: {str(e)}")
        return depiction_data


def _selector_id_list(alt_obj: Any) -> list:
    """Return SelectorId as a list of strings (LOD tag + value)."""
    try:
        raw = alt_obj.v.by_m("SelectorId").v
    except Exception:
        return []
    items = []
    for item in raw:
        try:
            items.append(strip_quotes(item.v))
        except Exception:
            items.append(strip_quotes(str(item)))
    return items


def _process_weapon_alternatives(entry: Any, unit_data: Dict[str, Any], unit: str) -> None:
    logger.debug(f"Processing weapon alternatives for {unit}")
    rows = unit_data["weapon_alternatives"]["rows"]
    alts = unit_data["weapon_alternatives"]["alts"]
    references = unit_data["weapon_alternatives"]["reference"]
    try:
        for alt in entry.v:
            row: Dict[str, Any] = {"index": int(getattr(alt, "index", len(rows)))}
            obj_type = getattr(alt.v, "type", None)
            row["type"] = obj_type
            selector_list = _selector_id_list(alt)
            row["selector_id"] = selector_list
            primary_selector = selector_list[0] if selector_list else None

            if is_obj_type(alt.v, "TDepictionVisual"):
                mesh_row = alt.v.by_m("MeshDescriptor", False)
                mesh = mesh_row.v if mesh_row is not None else None
                row["mesh"] = mesh
                if primary_selector and mesh is not None:
                    alts[primary_selector] = mesh
            elif is_obj_type(alt.v, "TMeshlessDepictionDescriptor"):
                ref_row = alt.v.by_m("ReferenceMeshForSkeleton", False)
                ref_mesh = ref_row.v if ref_row is not None else None
                row["reference_mesh"] = ref_mesh
                if primary_selector and ref_mesh is not None:
                    references[primary_selector] = ref_mesh
            rows.append(row)
            logger.debug(f"Added weapon alternative row {row['index']}: {row}")
    except Exception as e:
        logger.error(f"Error processing weapon alternative for {unit}: {str(e)}")


def _operator_field(op: Any, member: str) -> Any:
    row = op.v.by_m(member, False)
    if row is None:
        return None
    val = row.v
    if isinstance(val, str):
        return strip_quotes(val)
    if isinstance(val, list):
        out = []
        for item in val:
            try:
                out.append(strip_quotes(item.v))
            except Exception:
                out.append(strip_quotes(str(item)))
        return out
    return val


def _process_weapon_subdepiction(
    entry: Any,
    unit_data: Dict[str, Any],
    unit: str,
    all_renames: Dict[str, Any],
    all_fire_effects: Dict[str, str],
    all_weapon_meshes: Dict[str, str],
) -> None:
    logger.debug(f"Processing weapon subdepictions for {unit}")
    operators_dump = unit_data["weapon_subdepictions_operators"]
    weapon_subdepictions = unit_data["weapon_subdepictions"]
    alts_dict = unit_data["weapon_alternatives"]["alts"]
    try:
        operators = entry.v.by_m("Operators").v
        for op in operators:
            op_type = getattr(op.v, "type", None)
            op_index = int(getattr(op, "index", len(operators_dump)))
            op_dump: Dict[str, Any] = {"index": op_index, "type": op_type}
            for member in (
                "FireEffectTag",
                "WeaponShootDataPropertyName",
                "WeaponActiveAndCanShootPropertyName",
                "WeaponIgnoredPropertyName",
                "HandheldEquipmentKey",
                "Tag",
                "Selector",
                "Operator",
            ):
                value = _operator_field(op, member)
                if value is not None:
                    op_dump[member] = value
            operators_dump.append(op_dump)

            if not is_obj_type(op.v, "DepictionOperator_WeaponInstantFireInfantry"):
                continue
            fire_tag = _operator_field(op, "FireEffectTag")
            weapon_shoot_data = _operator_field(op, "WeaponShootDataPropertyName")
            if fire_tag is None or weapon_shoot_data is None:
                continue
            weapon_name = fire_tag.replace("FireEffect_", "")
            sub_entry: Dict[str, Any] = {
                "fire_tag": fire_tag,
                "weapon_shoot_data": weapon_shoot_data,
            }
            if weapon_name in all_renames:
                sub_entry["rename"] = all_renames[weapon_name]
            weapon_subdepictions[weapon_name] = sub_entry
            all_fire_effects[weapon_name] = fire_tag
            logger.debug(f"Added weapon subdepiction: {weapon_name} -> {fire_tag}")

            try:
                shoot_data_str = weapon_shoot_data if isinstance(weapon_shoot_data, str) else weapon_shoot_data[0]
                mesh_index = int(shoot_data_str.split("_")[-1])
                mesh_key = f"WeaponAlternative_{mesh_index}"
                if mesh_key in alts_dict:
                    mesh = alts_dict[mesh_key]
                    all_weapon_meshes[weapon_name] = mesh.split("Modele_")[-1]
                    logger.debug(
                        f"Mapped weapon '{weapon_name}' to mesh '{all_weapon_meshes[weapon_name]}'"
                    )
            except Exception:
                pass
    except Exception as e:
        logger.error(f"Error processing weapon subdepiction for {unit}: {str(e)}")


def _process_tactic_alternatives(entry: Any, unit_data: Dict[str, Any], unit: str) -> None:
    logger.debug(f"Processing tactic alternatives for {unit}")
    rows = unit_data["tactic_alternatives_rows"]
    try:
        for alt in entry.v:
            if not is_obj_type(alt.v, "TDepictionVisual"):
                continue
            selector_list = _selector_id_list(alt)
            lod = selector_list[0] if selector_list else None
            selector_number = selector_list[1] if len(selector_list) > 1 else None
            mesh_row = alt.v.by_m("MeshDescriptor", False)
            mesh_full = mesh_row.v if mesh_row is not None else None
            mesh_stem = mesh_full.split("Modele_")[-1] if isinstance(mesh_full, str) else None
            row = {
                "index": int(getattr(alt, "index", len(rows))),
                "lod": lod,
                "selector_number": selector_number,
                "mesh": mesh_stem,
                "mesh_full": mesh_full,
            }
            rows.append(row)
            unit_data["tactic_alternatives"] = {
                "selector_id": [lod, selector_number] if selector_number is not None else [lod],
                "mesh": mesh_stem,
            }
            logger.debug(f"Added tactic alternative row {row['index']}: {row}")
    except Exception as e:
        logger.error(f"Error processing tactic alternative for {unit}: {str(e)}")


def _process_tactic_soldier(
    entry: Any,
    unit_data: Dict[str, Any],
    unit: str,
    all_animation_tags: Dict[str, Any],
    animation_weapon_map: Dict[str, str],
) -> None:
    logger.debug(f"Processing SelectorTactic and animation tags for {unit}")
    try:
        selector = entry.v.by_m("Selector", False)
        if selector is not None:
            selector_tactic = selector.v.split("InfantrySelectorTactic_")[-1]
            unit_data["tactic_soldier"]["selector_tactic"] = selector_tactic

        operators_dump = unit_data["tactic_soldier"]["operators"]
        animation_tags = unit_data["tactic_soldier"]["animation_tags"]
        operators = entry.v.by_m("Operators").v
        for op in operators:
            op_type = getattr(op.v, "type", None)
            op_index = int(getattr(op, "index", len(operators_dump)))
            op_dump: Dict[str, Any] = {"index": op_index, "type": op_type}
            cond_row = op.v.by_m("ConditionalTags", False)
            if cond_row is not None:
                pairs = []
                for tag_tuple in cond_row.v:
                    if isinstance(tag_tuple.v, tuple):
                        pairs.append(
                            (strip_quotes(tag_tuple.v[0]), strip_quotes(tag_tuple.v[1]))
                        )
                op_dump["conditional_tags"] = pairs
            operators_dump.append(op_dump)

            if op_type != "DepictionOperator_SkeletalAnimation2_Default":
                continue
            if cond_row is None:
                continue
            for tag_tuple in cond_row.v:
                if not isinstance(tag_tuple.v, tuple):
                    logger.warning(f"Unexpected format for conditional tag: {tag_tuple}")
                    continue
                weapon_type = strip_quotes(tag_tuple.v[0])
                mesh_alt = strip_quotes(tag_tuple.v[1])
                animation_tags[weapon_type] = mesh_alt
                if weapon_type not in all_animation_tags:
                    all_animation_tags[weapon_type] = set()
                all_animation_tags[weapon_type].add(mesh_alt)
                mesh_alt_num = mesh_alt.split("_")[-1]
                for weapon_name, weapon_data in unit_data["weapon_subdepictions"].items():
                    shoot_data = weapon_data.get("weapon_shoot_data")
                    if isinstance(shoot_data, list):
                        shoot_data = shoot_data[0] if shoot_data else ""
                    if not shoot_data:
                        continue
                    if shoot_data.split("_")[-1] == mesh_alt_num:
                        animation_weapon_map[weapon_name] = weapon_type
                logger.debug(f"Added animation tag: {weapon_type} -> {mesh_alt}")
    except Exception as e:
        logger.error(f"Error processing animation tag for {unit}: {str(e)}")


def _process_tactic_ghost(entry: Any, unit_data: Dict[str, Any], unit: str) -> None:
    logger.debug(f"Processing TacticDepiction Ghost for {unit}")
    try:
        selector = entry.v.by_m("Selector", False)
        if selector is not None:
            unit_data["tactic_ghost"]["selector_tactic"] = selector.v.split("InfantrySelectorTactic_")[-1]
        operators_row = entry.v.by_m("Operators", False)
        if operators_row is None:
            return
        operators_dump = unit_data["tactic_ghost"]["operators"]
        for op in operators_row.v:
            op_type = getattr(op.v, "type", None)
            op_index = int(getattr(op, "index", len(operators_dump)))
            op_dump: Dict[str, Any] = {"index": op_index, "type": op_type}
            cond_row = op.v.by_m("ConditionalTags", False)
            if cond_row is not None:
                pairs = []
                for tag_tuple in cond_row.v:
                    if isinstance(tag_tuple.v, tuple):
                        pairs.append(
                            (strip_quotes(tag_tuple.v[0]), strip_quotes(tag_tuple.v[1]))
                        )
                op_dump["conditional_tags"] = pairs
            operators_dump.append(op_dump)
    except Exception as e:
        logger.error(f"Error processing tactic ghost for {unit}: {str(e)}")


def _maybe_process_transported_catalog(entry: Any, depiction_data: Dict[str, Any], ensure_unit) -> None:
    """Walk TTransportedInfantryCatalogEntries and dump each row by Identifier."""
    obj = getattr(entry, "v", None)
    if obj is None:
        return
    if not is_obj_type(obj, "TTransportedInfantryCatalogEntries"):
        return
    entries_row = obj.by_m("Entries", False)
    if entries_row is None:
        return
    for cat_entry in entries_row.v:
        cat_obj = cat_entry.v
        if not is_obj_type(cat_obj, "TTransportedInfantryEntry"):
            continue
        identifier_row = cat_obj.by_m("Identifier", False)
        identifier = strip_quotes(identifier_row.v) if identifier_row is not None else None
        if not identifier:
            continue
        count_row = cat_obj.by_m("Count", False)
        unique_row = cat_obj.by_m("UniqueCount", False)
        meshes_row = cat_obj.by_m("Meshes", False)
        meshes_full = []
        meshes_stems = []
        if meshes_row is not None:
            for mesh in meshes_row.v:
                try:
                    val = mesh.v
                except Exception:
                    val = str(mesh)
                meshes_full.append(val)
                if isinstance(val, str) and "Modele_" in val:
                    meshes_stems.append(val.split("Modele_")[-1])
                else:
                    meshes_stems.append(val)
        record = {
            "identifier": identifier,
            "count": count_row.v if count_row is not None else None,
            "unique_count": unique_row.v if unique_row is not None else None,
            "meshes": meshes_stems,
            "meshes_full": meshes_full,
        }
        unit_dict = ensure_unit(identifier)
        unit_dict["transported_infantry"].append(record)


def _build_all_renames(mod, ammo_ndf_path, missiles_ndf_path):
    try:
        all_merged_renames = {}
        all_merged_renames.update(MERGED_RENAMES)
        all_merged_renames.update(get_vanilla_renames(mod, ammo_ndf_path))
        all_merged_renames.update(get_vanilla_renames(mod, missiles_ndf_path))
        return all_merged_renames
    except Exception as e:
        logger.error(f"(depiction_data.py) Error building all renames: {str(e)}")
        return {}
