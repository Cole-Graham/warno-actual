"""Clone DepictionVehicles fire operators for SPAAG ``_AIR`` mounts.

Consumes ``game_db["he_dca_air_depiction_channels"]`` written by
``apply_he_dca_air_mounts``. For each recorded ground/air shoot-channel pair,
clones the ground fire operator onto the AIR channel and appends a matching
``weapon_effet_tag`` entry to the registration ``Actions`` MAP (reusing the
ground ``Weapon_*`` FX asset).

Most vehicles keep weapon Operators/Actions on the top-level registration.
Some (e.g. Faun_Kraka_20mm) nest them under ``SubDepictions``; when the
top-level Actions MAP is empty we edit that nested string instead.

Runs after new-unit cloning and unit depiction edits so those passes are not
wiped; this pass only appends.
"""

from __future__ import annotations

import re
from typing import Any, Dict, Optional, Tuple

from src.utils.ndf_utils import find_obj_by_blackhole_key, strip_quotes


_CHANNELS_KEY = "he_dca_air_depiction_channels"
_TAG_RE = re.compile(r"weapon_effet_tag(\d+)")
_WEAPON_NUM_RE = re.compile(r"_Weapon(\d+)(?:_|$)")
_SHOOT_TOKEN_RE = re.compile(r"WeaponShootData_\d+_\d+")
_FIRE_OP_TYPES = (
    "DepictionOperator_WeaponContinuousFire",
    "DepictionOperator_WeaponInstantFire",
    "DepictionOperator_WeaponMissileCarriageFire",
)


def _operator_shoot_name(operator: Any) -> Optional[str]:
    shoot_membr = operator.v.by_m("WeaponShootDataPropertyName", False)
    if shoot_membr is None:
        return None
    match = _SHOOT_TOKEN_RE.search(str(shoot_membr.v))
    return match.group(0) if match else None


def _max_effet_tag(source_path: Any, registration: Any) -> int:
    """Highest ``weapon_effet_tagN`` index referenced by this unit's depiction."""
    max_n = 0
    for member_name in ("Actions", "SubDepictions"):
        membr = registration.v.by_m(member_name, False)
        if membr is None:
            continue
        for match in _TAG_RE.finditer(str(membr.v)):
            max_n = max(max_n, int(match.group(1)))

    unit_prefix = None
    blackhole = registration.v.by_m("BlackHoleKey", False)
    if blackhole is not None:
        unit_prefix = f"DepictionOperator_{strip_quotes(str(blackhole.v))}_"

    for obj_row in source_path:
        ns = getattr(obj_row, "namespace", None) or ""
        if unit_prefix and not ns.startswith(unit_prefix):
            continue
        if not ns.startswith("DepictionOperator_"):
            continue
        fire_tag = obj_row.v.by_m("FireEffectTag", False)
        if fire_tag is None:
            continue
        for match in _TAG_RE.finditer(strip_quotes(str(fire_tag.v))):
            max_n = max(max_n, int(match.group(1)))
    return max_n


def _find_ground_operator(
    source_path: Any,
    unit_name: str,
    ground_shoot: str,
) -> Optional[Any]:
    """Find a fire operator for ``unit_name`` listening on ``ground_shoot``."""
    prefix = f"DepictionOperator_{unit_name}_"
    for obj_row in source_path:
        ns = getattr(obj_row, "namespace", None) or ""
        if not ns.startswith(prefix):
            continue
        op_type = getattr(obj_row.v, "type", None)
        if op_type not in _FIRE_OP_TYPES:
            continue
        if _operator_shoot_name(obj_row) == ground_shoot:
            return obj_row
    return None


def _air_operator_namespace(ground_ns: str) -> str:
    if ground_ns.endswith("_AIR"):
        return ground_ns
    return f"{ground_ns}_AIR"


def _find_existing_air_operator(
    source_path: Any,
    unit_name: str,
    air_shoot: str,
) -> Optional[Any]:
    prefix = f"DepictionOperator_{unit_name}_"
    for obj_row in source_path:
        ns = getattr(obj_row, "namespace", None) or ""
        if not ns.startswith(prefix):
            continue
        if not ns.endswith("_AIR"):
            continue
        if _operator_shoot_name(obj_row) == air_shoot:
            return obj_row
    return None


def _set_operator_shoot_channel(
    operator: Any,
    air_shoot: str,
    air_active: str,
) -> None:
    """Point a cloned fire operator at the AIR shoot/active channels."""
    shoot_membr = operator.v.by_m("WeaponShootDataPropertyName", False)
    if shoot_membr is not None:
        if getattr(operator.v, "type", None) == "DepictionOperator_WeaponContinuousFire":
            shoot_membr.v = f'"{air_shoot}"'
        else:
            # InstantFire / MissileCarriage use a list
            shoot_membr.v = f"['{air_shoot}']"

    active_membr = operator.v.by_m("WeaponActiveAndCanShootPropertyName", False)
    if active_membr is not None:
        active_membr.v = f'"{air_active}"'


def _weapon_fx_for_tag(actions_text: str, fire_tag: str) -> Optional[str]:
    """Return the ``Weapon_*`` asset paired with ``fire_tag`` in an Actions MAP."""
    # ( "weapon_effet_tag1", Weapon_Gatling_... )  — allow either quote style
    pattern = re.compile(
        rf'\(\s*["\']{re.escape(fire_tag)}["\']\s*,\s*([A-Za-z0-9_]+)\s*\)'
    )
    match = pattern.search(actions_text)
    return match.group(1) if match else None


def _append_sibling_map_entry(
    text: str,
    existing_tag: str,
    new_tag: str,
    weapon_fx: str,
) -> str:
    """Insert a new MAP pair in the same MAP that already contains ``existing_tag``."""
    if re.search(
        rf'\(\s*["\']{re.escape(new_tag)}["\']\s*,\s*{re.escape(weapon_fx)}\s*\)',
        text,
    ):
        return text

    entry_pat = re.compile(
        rf'\(\s*["\']{re.escape(existing_tag)}["\']\s*,\s*[A-Za-z0-9_]+\s*\),?'
    )
    match = entry_pat.search(text)
    if not match:
        return text

    close = text.find("]", match.end())
    if close < 0:
        return text

    new_entry = f'\n                    ( "{new_tag}", {weapon_fx} ),'
    return text[:close] + new_entry + text[close:]


def _append_actions_map_entry(actions_text: str, tag: str, weapon_fx: str) -> str:
    """Insert ``( "tag", Weapon_* )`` before the closing ``]`` of the first MAP.

    Prefer ``_append_sibling_map_entry`` when a ground tag is known; this remains
    for simple top-level empty-to-populated edge cases.
    """
    entry = f'( "{tag}", {weapon_fx} ),'
    if re.search(
        rf'\(\s*["\']{re.escape(tag)}["\']\s*,\s*{re.escape(weapon_fx)}\s*\)',
        actions_text,
    ):
        return actions_text

    map_close = actions_text.find("]")
    if map_close < 0:
        return actions_text

    before = actions_text[:map_close].rstrip()
    after = actions_text[map_close:]
    indent = "                "
    if before.endswith("["):
        insertion = f"\n{indent}{entry}\n            "
    else:
        insertion = f"\n{indent}{entry}"
    return before + insertion + after


def _operators_list_has(operators_list: Any, name: str) -> bool:
    for row in operators_list:
        if str(row.v).strip() == name:
            return True
    return False


def _insert_operator_after(
    operators_list: Any,
    after_name: str,
    new_name: str,
) -> None:
    """Insert ``new_name`` immediately after ``after_name`` in Operators."""
    insert_at = len(operators_list)
    for i, row in enumerate(operators_list):
        if str(row.v).strip() == after_name:
            insert_at = i + 1
            break
    operators_list.insert(insert_at, new_name)


def _insert_operator_name_in_text(
    text: str,
    after_name: str,
    new_name: str,
) -> str:
    """Insert ``new_name`` after ``after_name`` inside a SubDepictions string."""
    if new_name in text:
        return text
    needle = f"{after_name},"
    if needle in text:
        return text.replace(
            needle,
            f"{after_name},\n                    {new_name},",
            1,
        )
    idx = text.find(after_name)
    if idx < 0:
        return text
    end = idx + len(after_name)
    return text[:end] + f",\n                    {new_name}" + text[end:]


def _resolve_fx_target(
    registration: Any,
    ground_fire_tag: str,
    ground_op_ns: str,
) -> Tuple[Optional[str], Optional[Any], Optional[Any]]:
    """Locate the Actions text + edit target for a ground fire tag.

    Returns ``(weapon_fx, actions_or_sub_membr, operators_list_or_None)``.
    When ``operators_list_or_None`` is None, the operator name must be inserted
    into the same string member as the Actions MAP (SubDepictions case).
    """
    actions_membr = registration.v.by_m("Actions", False)
    if actions_membr is not None:
        weapon_fx = _weapon_fx_for_tag(str(actions_membr.v), ground_fire_tag)
        if weapon_fx is not None:
            operators_membr = registration.v.by_m("Operators", False)
            ops_list = operators_membr.v if operators_membr is not None else None
            # Prefer top-level only if the ground operator is listed there, or
            # SubDepictions is absent / does not reference the ground operator.
            sub_membr = registration.v.by_m("SubDepictions", False)
            ground_in_top = (
                ops_list is not None and _operators_list_has(ops_list, ground_op_ns)
            )
            ground_in_sub = (
                sub_membr is not None and ground_op_ns in str(sub_membr.v)
            )
            if ground_in_top or not ground_in_sub:
                return weapon_fx, actions_membr, ops_list

    sub_membr = registration.v.by_m("SubDepictions", False)
    if sub_membr is not None:
        weapon_fx = _weapon_fx_for_tag(str(sub_membr.v), ground_fire_tag)
        if weapon_fx is not None:
            return weapon_fx, sub_membr, None

    return None, None, None


def apply_he_dca_air_depiction_weapons(
    source_path: Any,
    game_db: Dict[str, Any],
    logger: Any,
) -> None:
    """Clone fire operators + Actions rows for SPAAG AIR shoot channels."""
    channels_by_unit = game_db.get(_CHANNELS_KEY) or {}
    if not channels_by_unit:
        logger.info("(he_dca_air_depiction) no air depiction channels recorded")
        return

    added = 0
    skipped = 0

    for unit_name, channel_list in channels_by_unit.items():
        registration = find_obj_by_blackhole_key(
            source_path, unit_name, "TacticVehicleDepictionRegistration"
        )
        if registration is None:
            logger.warning(
                f"(he_dca_air_depiction) {unit_name}: no "
                f"TacticVehicleDepictionRegistration; skipping"
            )
            continue

        next_tag = _max_effet_tag(source_path, registration)

        for channel in channel_list:
            ground_shoot = channel["ground_shoot"]
            air_shoot = channel["air_shoot"]
            air_active = channel["air_active"]

            if _find_existing_air_operator(source_path, unit_name, air_shoot):
                skipped += 1
                continue

            ground_op = _find_ground_operator(source_path, unit_name, ground_shoot)
            if ground_op is None:
                logger.warning(
                    f"(he_dca_air_depiction) {unit_name}: no fire operator for "
                    f"{ground_shoot}; skipping AIR depiction"
                )
                continue

            ground_fire_tag = strip_quotes(
                str(ground_op.v.by_m("FireEffectTag").v)
            )
            weapon_fx, target_membr, operators_list = _resolve_fx_target(
                registration, ground_fire_tag, ground_op.namespace
            )
            if weapon_fx is None or target_membr is None:
                logger.warning(
                    f"(he_dca_air_depiction) {unit_name}: no Actions MAP entry "
                    f"for {ground_fire_tag}; skipping AIR depiction"
                )
                continue

            next_tag += 1
            air_tag = f"weapon_effet_tag{next_tag}"
            air_ns = _air_operator_namespace(ground_op.namespace)

            # If a prior partial run left the namespace but not the shoot channel,
            # pick a unique namespace.
            if source_path.by_n(air_ns, False) is not None:
                match = _WEAPON_NUM_RE.search(ground_op.namespace)
                weapon_num = match.group(1) if match else "1"
                air_ns = f"DepictionOperator_{unit_name}_Weapon{weapon_num}_AIR"
                suffix = 2
                while source_path.by_n(air_ns, False) is not None:
                    air_ns = (
                        f"DepictionOperator_{unit_name}_Weapon{weapon_num}"
                        f"_AIR{suffix}"
                    )
                    suffix += 1

            new_op = ground_op.copy()
            new_op.namespace = air_ns
            fire_tag_membr = new_op.v.by_m("FireEffectTag", False)
            if fire_tag_membr is not None:
                fire_tag_membr.v = f'"{air_tag}"'
            _set_operator_shoot_channel(new_op, air_shoot, air_active)

            source_path.insert(registration.index, new_op)

            if operators_list is not None:
                if not _operators_list_has(operators_list, air_ns):
                    _insert_operator_after(
                        operators_list, ground_op.namespace, air_ns
                    )
                target_membr.v = _append_sibling_map_entry(
                    str(target_membr.v), ground_fire_tag, air_tag, weapon_fx
                )
            else:
                # Nested SubDepictions string: Operators + Actions live together.
                edited = _insert_operator_name_in_text(
                    str(target_membr.v), ground_op.namespace, air_ns
                )
                target_membr.v = _append_sibling_map_entry(
                    edited, ground_fire_tag, air_tag, weapon_fx
                )

            added += 1
            logger.info(
                f"(he_dca_air_depiction) {unit_name}: added {air_ns} "
                f"({air_shoot} -> {air_tag}, {weapon_fx})"
            )

    logger.info(
        f"(he_dca_air_depiction) added {added} AIR operators "
        f"(skipped {skipped} existing)"
    )
