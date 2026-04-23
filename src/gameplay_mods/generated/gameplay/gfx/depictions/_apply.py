"""Shared apply layer for depiction edits.

Both `_handle_new_units` (for cloned-but-not-yet-inserted depiction objects) and
`_handle_complex_unit_edits` (for depiction objects already in the source NDF)
funnel per-namespace edits through the same dispatchers here, so the data schema
and behavior are consistent regardless of where the edits were authored
(`new_depictions/*` vs `depiction_edits/*`).

Each section apply function accepts the value verbatim from the edits dict and
detects which of three shapes is in play:

- ``dict`` keyed by ``int`` with ``(edit_type, ...)`` tuples - indexed ops
  (``edit`` / ``insert`` / ``add`` / ``remove``).
- ``dict`` keyed by member-name strings - per-member assignment / nested handling.
- raw NDF list string, ``list``, or ``ndf.model.List`` - wholesale replace of
  the target list value.
"""

from typing import Any, Iterable

from src import ndf
from src.utils.logging_utils import setup_logger
from src.utils.ndf_utils import is_obj_type

logger = setup_logger(__name__)


def is_indexed_ops(value: Any) -> bool:
    """True if value is a non-empty dict with all int keys (indexed edit ops)."""
    if not isinstance(value, dict) or not value:
        return False
    return all(isinstance(k, int) for k in value.keys())


def is_member_map(value: Any) -> bool:
    """True if value is a non-empty dict with all string keys (per-member assignments)."""
    if not isinstance(value, dict) or not value:
        return False
    return all(isinstance(k, str) for k in value.keys())


def is_wholesale_list(value: Any) -> bool:
    """True if value should be assigned wholesale to ``target.v``.

    Accepts raw NDF list strings (start with ``[``), python lists, tuples that
    were used to wrap a raw NDF string, or any value with an ``add`` method
    (e.g. ``ndf.model.List``).
    """
    if isinstance(value, str):
        return value.lstrip().startswith("[")
    if isinstance(value, (list, tuple)):
        return True
    return hasattr(value, "add") and not hasattr(value, "by_m")


def _wholesale_assign(target: Any, value: Any, *, label: str) -> None:
    """Assign ``value`` wholesale to ``target.v``.

    Tuple values are accepted for compatibility with NEW_DEPICTIONS authors who
    sometimes wrap a raw NDF list string in a tuple for readability; in that
    case the first element is used.
    """
    if isinstance(value, tuple) and value:
        value = value[0]
    target.v = value
    logger.info(f"Wholesale-replaced {label}")


def _coerce_quoted(value: str) -> str:
    """Strip surrounding ASCII quotes (single or double) from ``value``."""
    return value.strip('"').strip("'")


def apply_all_weapon_alternatives(
    target: Any,
    value: Any,
    *,
    unit_name: str,
) -> None:
    """Apply edits to an ``AllWeaponAlternatives_<unit>`` list object.

    Indexed ops support ``edit``, ``insert``, ``remove`` operating on rows; each
    op carries a list of ``(member, value)`` pairs where ``member`` is one of
    ``SelectorId``, ``MeshDescriptor``, or ``ReferenceMeshForSkeleton``.
    """
    if is_wholesale_list(value):
        _wholesale_assign(target, value, label=f"AllWeaponAlternatives for {unit_name}")
        return

    if not is_indexed_ops(value):
        logger.error(
            f"AllWeaponAlternatives edits for {unit_name}: unrecognized value shape {type(value).__name__}"
        )
        return

    rows_to_remove: list[int] = []
    rows_to_insert: list[tuple[int, str]] = []
    rows_to_edit: list[tuple[int, list]] = []
    for row_index, op in value.items():
        logger.debug(f"AllWeaponAlternatives edit for {unit_name} at index {row_index}: {op}")
        edit_type, *edit_payload = op
        edit_list = edit_payload[0] if edit_payload else []
        if edit_type == "edit":
            rows_to_edit.append((row_index, edit_list))
        elif edit_type == "insert":
            selector_id = None
            new_mesh = None
            for member, mv in edit_list:
                if member == "SelectorId":
                    selector_id = f"['{mv}']"
                elif member in ("MeshDescriptor", "ReferenceMeshForSkeleton"):
                    new_mesh = f"$/GFX/DepictionResources/Modele_{mv}"
            if selector_id and new_mesh:
                rows_to_insert.append((
                    row_index,
                    (
                        f"TDepictionVisual"
                        f"("
                        f"    SelectorId = {selector_id}"
                        f"    MeshDescriptor = {new_mesh}"
                        f")"
                    ),
                ))
            else:
                logger.error(f"Insert payload for {unit_name} at index {row_index} missing fields")
        elif edit_type == "remove":
            rows_to_remove.append(row_index)
        else:
            logger.warning(f"Unknown edit_type '{edit_type}' for {unit_name} at row {row_index}")

    for row_index in sorted(rows_to_remove, reverse=True):
        target.v.remove(row_index)
        logger.info(f"Removed AllWeaponAlternatives row {row_index} for {unit_name}")
    for row_index, ndf_str in sorted(rows_to_insert):
        target.v.insert(row_index, ndf_str)
        logger.info(f"Inserted AllWeaponAlternatives row {row_index} for {unit_name}")
    for row_index, edit_list in rows_to_edit:
        if row_index >= len(target.v):
            logger.error(
                f"AllWeaponAlternatives edit for {unit_name} at index {row_index} "
                f"out of range (list length {len(target.v)}); skipped"
            )
            continue
        for member, mv in edit_list:
            if member == "SelectorId":
                member_row = target.v[row_index].v.by_m(member, False)
                if member_row is None:
                    logger.error(f"SelectorId for {unit_name} at index {row_index} not found")
                    continue
                member_row.v = f"['{mv}']"
                logger.info(f"Changed SelectorId for {unit_name} to {mv}")
            elif member in ("MeshDescriptor", "ReferenceMeshForSkeleton"):
                new_mesh = f"$/GFX/DepictionResources/Modele_{mv}"
                member_row = target.v[row_index].v.by_m(member, False)
                if member_row is None:
                    logger.error(f"{member} for {unit_name} at index {row_index} not found")
                    continue
                member_row.v = new_mesh
                logger.info(f"Changed {member} for {unit_name} to {new_mesh}")


def apply_all_weapon_sub_depiction(
    target: Any,
    value: Any,
    *,
    unit_name: str,
) -> None:
    """Apply edits to an ``AllWeaponSubDepiction_<unit>`` object.

    Value is expected to be a member-map dict whose ``Operators`` member can
    itself be either a wholesale list value or an indexed-ops dict with
    ``FireEffectTag`` / ``WeaponShootDataPropertyName`` payloads.
    """
    if is_wholesale_list(value):
        _wholesale_assign(target, value, label=f"AllWeaponSubDepiction for {unit_name}")
        return

    if not is_member_map(value):
        logger.error(
            f"AllWeaponSubDepiction edits for {unit_name}: unrecognized value shape {type(value).__name__}"
        )
        return

    for member, member_value in value.items():
        if member == "Operators":
            operators_member = target.v.by_m("Operators")
            _apply_subdepiction_operators(operators_member, member_value, unit_name=unit_name)
        else:
            logger.warning(
                f"AllWeaponSubDepiction member '{member}' for {unit_name} not handled by shared apply layer"
            )


def _apply_subdepiction_operators(
    operators_member: Any,
    value: Any,
    *,
    unit_name: str,
) -> None:
    """Apply edits to ``AllWeaponSubDepiction_<unit>.Operators`` list."""
    if is_wholesale_list(value):
        _wholesale_assign(
            operators_member,
            value,
            label=f"AllWeaponSubDepiction.Operators for {unit_name}",
        )
        return

    if not is_indexed_ops(value):
        logger.error(
            f"AllWeaponSubDepiction.Operators edits for {unit_name}: unrecognized shape {type(value).__name__}"
        )
        return

    rows_to_remove: list[int] = []
    rows_to_insert: list[tuple[int, str]] = []
    rows_to_edit: list[tuple[int, list]] = []
    for index, op in value.items():
        edit_type, *edit_payload = op
        edit_list = edit_payload[0] if edit_payload else []
        if edit_type == "edit":
            rows_to_edit.append((index, edit_list))
        elif edit_type == "insert":
            effect_tag = None
            shoot_property = None
            for submember, mv in edit_list:
                if submember == "FireEffectTag":
                    effect_tag = f'"FireEffect_{_coerce_quoted(mv)}"'
                elif submember == "WeaponShootDataPropertyName":
                    shoot_property = f'"{mv}"'
            if effect_tag and shoot_property:
                rows_to_insert.append((
                    index,
                    (
                        f"DepictionOperator_WeaponInstantFireInfantry"
                        f"("
                        f"    FireEffectTag = {effect_tag}"
                        f"    WeaponShootDataPropertyName = {shoot_property}"
                        f")"
                    ),
                ))
            else:
                logger.error(
                    f"Insert payload for {unit_name} Operators[{index}] missing fields"
                )
        elif edit_type == "remove":
            rows_to_remove.append(index)
        else:
            logger.warning(f"Unknown edit_type '{edit_type}' for {unit_name} Operators[{index}]")

    for index in sorted(rows_to_remove, reverse=True):
        operators_member.v.remove(index)
        logger.info(f"Removed AllWeaponSubDepiction.Operators[{index}] for {unit_name}")
    for index, ndf_str in sorted(rows_to_insert):
        operators_member.v.insert(index, ndf_str)
        logger.info(f"Inserted AllWeaponSubDepiction.Operators[{index}] for {unit_name}")
    for index, edit_list in rows_to_edit:
        if index >= len(operators_member.v):
            logger.error(
                f"AllWeaponSubDepiction.Operators edit for {unit_name} at index {index} "
                f"out of range (list length {len(operators_member.v)}); skipped"
            )
            continue
        for submember, mv in edit_list:
            if submember == "FireEffectTag":
                new_value = f'"FireEffect_{_coerce_quoted(mv)}"'
                member_row = operators_member.v[index].v.by_m(submember, False)
                if member_row is None:
                    logger.error(f"{submember} for {unit_name} Operators[{index}] not found")
                    continue
                member_row.v = new_value
                logger.info(f"Changed {submember} for {unit_name} Operators[{index}] to {new_value}")
            elif submember == "WeaponShootDataPropertyName":
                member_row = operators_member.v[index].v.by_m(submember, False)
                if member_row is None:
                    logger.error(f"{submember} for {unit_name} Operators[{index}] not found")
                    continue
                member_row.v = f'"{mv}"'
                logger.info(f"Changed {submember} for {unit_name} Operators[{index}] to {mv}")
            else:
                logger.warning(
                    f"AllWeaponSubDepiction.Operators[{index}] unknown submember "
                    f"'{submember}' for {unit_name}"
                )


def apply_tactic_depiction_alternatives(
    target: Any,
    value: Any,
    *,
    unit_name: str,
) -> None:
    """Apply edits to a ``TacticDepiction_<unit>_Alternatives`` list."""
    if is_wholesale_list(value):
        _wholesale_assign(
            target, value, label=f"TacticDepiction_{unit_name}_Alternatives"
        )
        return

    logger.error(
        f"TacticDepiction_{unit_name}_Alternatives edits expected a wholesale list value; "
        f"got {type(value).__name__}"
    )


def apply_tactic_depiction_soldier(
    source_path: Any,
    target: Any,
    value: Any,
    *,
    unit_name: str,
) -> None:
    """Apply edits to a ``TacticDepiction_<unit>_Soldier`` object.

    Supported keys in the member map:

    - ``skeleton_tags``: full overwrite of the skeletal animation operator's
      ``ConditionalTags`` list (replaces all entries).
    - ``Selector``: set to ``InfantrySelectorTactic_<value>``; the template is
      auto-created in ``source_path`` if missing.
    - ``Operators``: indexed ops on the skeletal animation operator's
      ``ConditionalTags`` list (``edit`` / ``insert`` / ``add`` / ``remove``).
    """
    if not is_member_map(value):
        logger.error(
            f"TacticDepiction_{unit_name}_Soldier edits expected a member-map dict; "
            f"got {type(value).__name__}"
        )
        return

    if "skeleton_tags" in value:
        overwrite_skeleton_conditional_tags(target.v, value["skeleton_tags"])
        logger.info(f"Overwrote ConditionalTags for {unit_name} via skeleton_tags")
        return

    for member, member_value in value.items():
        if member == "Selector":
            template_namespace = f"InfantrySelectorTactic_{member_value}"
            template = source_path.by_n(template_namespace, False)
            if not template:
                # member_value is "UU_SS" where UU is UniqueCount and SS is the
                # surrogates count; the Surrogates member references
                # TacticDepiction_{SS:02}_Surrogates (NOT the UniqueCount).
                uu_str, ss_str = member_value.split("_")
                unique_count = int(uu_str)
                surrogates_count = int(ss_str)
                source_path.add(
                    f"InfantrySelectorTactic_{member_value} is TemplateInfantrySelectorTactic"
                    f"("
                    f"    Surrogates = TacticDepiction_{surrogates_count:02}_Surrogates"
                    f"    UniqueCount = {unique_count}"
                    f")"
                )
            target.v.by_m(member).v = template_namespace
            logger.info(f"Set Selector for {unit_name} to {template_namespace}")
        elif member == "Operators":
            _apply_soldier_conditional_tags(target, member_value, unit_name=unit_name)
        else:
            logger.warning(
                f"TacticDepiction_Soldier member '{member}' for {unit_name} not handled"
            )


def _apply_soldier_conditional_tags(
    soldier_target: Any,
    operator_edits: Any,
    *,
    unit_name: str,
) -> None:
    """Apply indexed ops to the SkeletalAnimation operator's ConditionalTags list."""
    operators_member = soldier_target.v.by_m("Operators")
    skeletal_animation_operator = None
    for obj in operators_member.v:
        if is_obj_type(obj.v, "DepictionOperator_SkeletalAnimation2_Default"):
            skeletal_animation_operator = obj.v
            break
    if skeletal_animation_operator is None:
        logger.error(
            f"Could not find DepictionOperator_SkeletalAnimation2_Default for {unit_name}"
        )
        return

    conditional_tags = skeletal_animation_operator.by_m("ConditionalTags", False)
    if conditional_tags is None:
        skeletal_animation_operator.add("ConditionalTags = []")
        conditional_tags = skeletal_animation_operator.by_m("ConditionalTags")

    if not is_indexed_ops(operator_edits):
        logger.error(
            f"TacticDepiction_{unit_name}_Soldier.Operators expected indexed ops; "
            f"got {type(operator_edits).__name__}"
        )
        return

    rows_to_remove: list[int] = []
    rows_to_insert: list[tuple[int, str]] = []
    rows_to_edit: list[tuple[int, list]] = []
    for index, op in operator_edits.items():
        edit_type, *edit_payload = op
        edit_list = edit_payload[0] if edit_payload else []
        if edit_type == "edit":
            rows_to_edit.append((index, edit_list))
        elif edit_type == "insert":
            for new_tag, mesh_alternative in edit_list:
                rows_to_insert.append((index, f"('{new_tag}', '{mesh_alternative}')"))
        elif edit_type == "add":
            for new_tag, mesh_alternative in edit_list:
                conditional_tags.v.add(f"('{new_tag}', '{mesh_alternative}')")
                logger.info(
                    f"Added ConditionalTags ('{new_tag}', '{mesh_alternative}') for {unit_name}"
                )
        elif edit_type == "remove":
            rows_to_remove.append(index)
        else:
            logger.warning(
                f"Unknown edit_type '{edit_type}' for {unit_name} ConditionalTags[{index}]"
            )

    for index in sorted(rows_to_remove, reverse=True):
        conditional_tags.v.remove(index)
        logger.info(f"Removed ConditionalTags[{index}] for {unit_name}")
    for index, ndf_str in sorted(rows_to_insert):
        conditional_tags.v.insert(index, ndf_str)
        logger.info(f"Inserted ConditionalTags[{index}] for {unit_name}")
    for index, edit_list in rows_to_edit:
        if index >= len(conditional_tags.v):
            logger.warning(
                f"Index {index} out of range for ConditionalTags "
                f"(length {len(conditional_tags.v)}) for {unit_name}; skipped"
            )
            continue
        for new_tag, mesh_alternative in edit_list:
            conditional_tags.v[index].v = f"('{new_tag}', '{mesh_alternative}')"
            logger.info(
                f"Updated ConditionalTags[{index}] to ('{new_tag}', '{mesh_alternative}') for {unit_name}"
            )


def apply_tactic_depiction_ghost(
    target: Any,
    value: Any,
    *,
    unit_name: str,
) -> None:
    """Apply edits to a ``TacticDepiction_<unit>_Ghost`` object."""
    if not is_member_map(value):
        logger.error(
            f"TacticDepiction_{unit_name}_Ghost edits expected a member-map dict; "
            f"got {type(value).__name__}"
        )
        return

    for member, member_value in value.items():
        if member == "Selector":
            target.v.by_m(member).v = f"InfantrySelectorTactic_{member_value}"
            logger.info(f"Set Ghost Selector for {unit_name} to InfantrySelectorTactic_{member_value}")
        else:
            logger.warning(
                f"TacticDepiction_Ghost member '{member}' for {unit_name} not handled"
            )


def apply_transported_infantry_entry(
    target_entry: Any,
    value: Any,
    *,
    unit_name: str,
) -> None:
    """Apply per-member edits to a single ``TTransportedInfantryEntry`` row.

    Supported members: ``Count``, ``UniqueCount`` (assigned as strings),
    ``Meshes`` (list of mesh stems, expanded to ``$/GFX/DepictionResources/Modele_<stem>``).
    """
    if not is_member_map(value):
        logger.error(
            f"TTransportedInfantryEntry edits for {unit_name} expected a member-map dict; "
            f"got {type(value).__name__}"
        )
        return

    for member, member_value in value.items():
        if member == "Count":
            target_entry.v.by_m("Count").v = str(member_value)
        elif member == "UniqueCount":
            target_entry.v.by_m("UniqueCount").v = str(member_value)
        elif member == "Meshes":
            new_meshes = ndf.model.List()
            for mesh in member_value:
                new_meshes.add(f"$/GFX/DepictionResources/Modele_{mesh}")
            target_entry.v.by_m("Meshes").v = new_meshes
        else:
            logger.error(f"TTransportedInfantryEntry unknown member '{member}' for {unit_name}")


def overwrite_skeleton_conditional_tags(
    soldier_depiction_obj: Any,
    tags_list: Iterable[tuple[str, str]],
) -> None:
    """Overwrite the SkeletalAnimation operator's ConditionalTags list."""
    operators_member = soldier_depiction_obj.by_m("Operators")
    skeletal_animation_operator = None
    for obj in operators_member.v:
        if is_obj_type(obj.v, "DepictionOperator_SkeletalAnimation2_Default"):
            skeletal_animation_operator = obj.v
            break
    if skeletal_animation_operator is None:
        logger.warning(
            "Could not find DepictionOperator_SkeletalAnimation2_Default in Operators; "
            "skeleton_tags not applied"
        )
        return
    conditional_tags = skeletal_animation_operator.by_m("ConditionalTags", False)
    if conditional_tags is None:
        skeletal_animation_operator.add("ConditionalTags = []")
        conditional_tags = skeletal_animation_operator.by_m("ConditionalTags")
    for i in range(len(conditional_tags.v) - 1, -1, -1):
        conditional_tags.v.remove(i)
    for tag, mesh_alternative in tags_list:
        conditional_tags.v.add(f"('{tag}', '{mesh_alternative}')")


def apply_infantry_section(
    source_path: Any,
    target: Any,
    namespace: str,
    obj_type: str,
    value: Any,
    *,
    unit_name: str,
) -> bool:
    """Dispatch a single ``(namespace, obj_type) -> value`` infantry edit.

    Returns ``True`` if the section was recognized and processed, ``False``
    otherwise. The caller is responsible for locating ``target`` (either a
    cloned, not-yet-inserted object for new units, or an object looked up
    inside ``source_path`` for existing units).
    """
    if namespace and namespace.startswith("AllWeaponAlternatives_"):
        apply_all_weapon_alternatives(target, value, unit_name=unit_name)
        return True
    if namespace and namespace.startswith("AllWeaponSubDepictionBackpack_"):
        if is_wholesale_list(value):
            _wholesale_assign(
                target, value, label=f"AllWeaponSubDepictionBackpack for {unit_name}"
            )
        else:
            logger.warning(
                f"AllWeaponSubDepictionBackpack edits for {unit_name} only support wholesale "
                f"replacement; got {type(value).__name__}"
            )
        return True
    if namespace and namespace.startswith("AllWeaponSubDepiction_"):
        apply_all_weapon_sub_depiction(target, value, unit_name=unit_name)
        return True
    if namespace and namespace.startswith("TacticDepiction_") and namespace.endswith("_Alternatives"):
        apply_tactic_depiction_alternatives(target, value, unit_name=unit_name)
        return True
    if namespace and namespace.startswith("TacticDepiction_") and namespace.endswith("_Soldier"):
        apply_tactic_depiction_soldier(source_path, target, value, unit_name=unit_name)
        return True
    if namespace and namespace.startswith("TacticDepiction_") and namespace.endswith("_Ghost"):
        apply_tactic_depiction_ghost(target, value, unit_name=unit_name)
        return True
    if obj_type == "TTransportedInfantryEntry":
        apply_transported_infantry_entry(target, value, unit_name=unit_name)
        return True
    return False


def apply_indexed_list_ops(
    list_member: Any,
    value: Any,
    *,
    label: str,
    op_handlers: dict[str, Any],
) -> None:
    """Apply indexed ``edit`` / ``insert`` / ``replace`` / ``remove`` ops to a list member.

    ``op_handlers`` is a mapping from op-name to a callable. Each callable is
    invoked with ``(list_member, index, payload)`` for ops that need custom
    handling (typically ``edit``); ``insert`` / ``replace`` / ``remove`` are
    handled inline using the standard ndf_parse list API. This helper keeps
    the per-namespace patchers in vehicles, aerial, missile carriages, etc.
    consistent in how they batch removals/inserts (reverse-order to keep
    indices stable).
    """
    if is_wholesale_list(value):
        _wholesale_assign(list_member, value, label=label)
        return

    if not is_indexed_ops(value):
        logger.error(f"{label}: unrecognized value shape {type(value).__name__}")
        return

    rows_to_remove: list[int] = []
    rows_to_insert: list[tuple[int, Any]] = []
    rows_to_replace: list[tuple[int, Any]] = []
    for row_index, op in value.items():
        edit_op, *edit_data = op
        if edit_op == "remove":
            rows_to_remove.append(row_index)
        elif edit_op == "insert":
            rows_to_insert.append((row_index, edit_data[0]))
        elif edit_op == "replace":
            rows_to_replace.append((row_index, edit_data[0]))
        elif edit_op in op_handlers:
            op_handlers[edit_op](list_member, row_index, edit_data[0] if edit_data else None)
        else:
            logger.warning(f"{label}: unknown op '{edit_op}' at index {row_index}")

    for row_index, payload in rows_to_replace:
        list_member.v.replace(row_index, payload)
        logger.info(f"{label}: replaced row {row_index}")
    for row_index in sorted(rows_to_remove, reverse=True):
        list_member.v.remove(row_index)
        logger.info(f"{label}: removed row {row_index}")
    for row_index, payload in sorted(rows_to_insert, reverse=True):
        list_member.v.insert(row_index, payload)
        logger.info(f"{label}: inserted row at {row_index}")
