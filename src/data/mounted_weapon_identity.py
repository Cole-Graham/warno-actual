"""Weapon identity that v206709 stores on each mounted weapon, not on ammunition.

Internal values match the old ammunition literals: single-quoted tokens for
Name, Caliber, TypeCategoryName, WeaponDescriptionToken, and TraitsToken, and
a double-quoted texture name. Mounts are written with double quotes.
"""

from __future__ import annotations

import copy
import re
from typing import Any, Dict, Iterable, List, Optional

from src import ndf
from src.utils.ndf_utils import is_obj_type, is_valid_turret, strip_quotes

IDENTITY_FIELDS = (
    "Name",
    "Caliber",
    "TypeCategoryName",
    "WeaponDescriptionToken",
    "TraitsToken",
    "InterfaceWeaponTexture",
)
_SCALAR_SINGLE = (
    "Name",
    "Caliber",
    "TypeCategoryName",
    "WeaponDescriptionToken",
)
_TEXTURE = "InterfaceWeaponTexture"
_TRAITS = "TraitsToken"
_VARIANT_SUFFIX = re.compile(
    r"(?:_strength\d+)?(?:_x\d+|_salvolength\d+|_infmagazine\d+)?(?:_AIR)?$"
)


def single_quoted(raw: Any) -> str:
    return "'" + strip_quotes(str(raw)) + "'"


def double_quoted(raw: Any) -> str:
    return '"' + strip_quotes(str(raw)) + '"'


def identity_map(ammo_db: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    return ammo_db.setdefault("mounted_identity", {})


def record_for(ammo_db: Dict[str, Any], namespace: str) -> Dict[str, Any]:
    return identity_map(ammo_db).setdefault(namespace, {})


def copy_identity(ammo_db: Dict[str, Any], src_namespace: Optional[str], dst_namespace: str) -> None:
    if not src_namespace or src_namespace == dst_namespace:
        return
    src = identity_map(ammo_db).get(src_namespace)
    if src is None:
        return
    identity_map(ammo_db)[dst_namespace] = copy.deepcopy(src)


def rekey_identity(ammo_db: Dict[str, Any], old_namespace: str, new_namespace: str) -> None:
    if not old_namespace or old_namespace == new_namespace:
        return
    mapping = identity_map(ammo_db)
    if old_namespace not in mapping:
        return
    mapping[new_namespace] = mapping.pop(old_namespace)


def resolve_identity(ammo_db: Dict[str, Any], namespace: str) -> Optional[Dict[str, Any]]:
    mapping = identity_map(ammo_db)
    if namespace in mapping:
        return mapping[namespace]
    base_name = _VARIANT_SUFFIX.sub("", namespace.removeprefix("Ammo_"))
    return mapping.get(f"Ammo_{base_name}")


def store_identity_value(record: Dict[str, Any], key: str, value: Any) -> None:
    """Store one authored identity value in the internal literal form."""
    if key == "Caliber" and isinstance(value, tuple):
        record[key] = single_quoted(value[1])
        return
    if key == _TRAITS and isinstance(value, list):
        record[key] = [single_quoted(item) for item in value]
        return
    if key == _TEXTURE:
        record[key] = double_quoted(value)
        return
    if key in _SCALAR_SINGLE:
        record[key] = single_quoted(value)
        return
    record[key] = value


def read_mount_identity(mounted: Any) -> Dict[str, Any]:
    record: Dict[str, Any] = {}
    for field in _SCALAR_SINGLE:
        membr = mounted.v.by_m(field, False)
        if membr is None or membr.v in (None, ""):
            continue
        record[field] = single_quoted(membr.v)
    texture = mounted.v.by_m(_TEXTURE, False)
    if texture is not None and texture.v not in (None, ""):
        record[_TEXTURE] = double_quoted(texture.v)
    traits = mounted.v.by_m(_TRAITS, False)
    if traits is not None:
        record[_TRAITS] = [single_quoted(trait.v) for trait in traits.v]
    return record


def ammo_namespace_from_mount(mounted: Any) -> Optional[str]:
    membr = mounted.v.by_m("Ammunition", False)
    if membr is None or membr.v in (None, ""):
        return None
    raw = strip_quotes(str(membr.v))
    index = raw.find("Ammo_")
    if index < 0:
        return None
    return raw[index:]


def iter_mounted_weapons(weapon_file: Iterable[Any]) -> Iterable[Any]:
    for weapon_descr in weapon_file:
        if not hasattr(weapon_descr, "v"):
            continue
        turrets = weapon_descr.v.by_m("TurretDescriptorList", False)
        if turrets is None:
            continue
        for turret in turrets.v:
            if not is_valid_turret(turret.v):
                continue
            mounts = turret.v.by_m("MountedWeaponDescriptorList", False)
            if mounts is None:
                continue
            for mounted in mounts.v:
                yield mounted


def build_mounted_identity(weapon_file: Iterable[Any]) -> Dict[str, Dict[str, Any]]:
    """First mount of each ammo namespace wins. Later mounts must match it."""
    identity: Dict[str, Dict[str, Any]] = {}
    for mounted in iter_mounted_weapons(weapon_file):
        namespace = ammo_namespace_from_mount(mounted)
        if not namespace or namespace in identity:
            continue
        identity[namespace] = read_mount_identity(mounted)
    return identity


def identity_matches(mounted: Any, record: Dict[str, Any]) -> bool:
    current = read_mount_identity(mounted)
    for field in IDENTITY_FIELDS:
        if field not in record:
            continue
        if current.get(field) != record[field]:
            return False
    return True


def _set_mount_member(mounted: Any, name: str, ndf_value: str) -> None:
    membr = mounted.v.by_m(name, False)
    if membr is None:
        mounted.v.add(f"{name} = {ndf_value}")
        return
    if name == _TRAITS:
        membr.v = ndf.convert(ndf_value.encode("utf-8"))[0].v
        return
    membr.v = ndf_value


def apply_identity_to_mount(mounted: Any, record: Dict[str, Any]) -> None:
    for field in _SCALAR_SINGLE:
        if field not in record:
            continue
        _set_mount_member(mounted, field, double_quoted(record[field]))
    if _TEXTURE in record:
        _set_mount_member(mounted, _TEXTURE, double_quoted(record[_TEXTURE]))
    if _TRAITS in record:
        traits = ", ".join(double_quoted(token) for token in record[_TRAITS])
        _set_mount_member(mounted, _TRAITS, f"[{traits}]")


def apply_mounted_weapon_identity(weapon_file: Iterable[Any], ammo_db: Dict[str, Any], logger: Any) -> None:
    """Write identity onto each mount whose ammo record differs from the mount."""
    written = 0
    missing = 0
    for mounted in iter_mounted_weapons(weapon_file):
        namespace = ammo_namespace_from_mount(mounted)
        if not namespace:
            continue
        record = resolve_identity(ammo_db, namespace)
        if not record:
            missing += 1
            continue
        if identity_matches(mounted, record):
            continue
        apply_identity_to_mount(mounted, record)
        written += 1
    logger.info(
        "Applied mounted weapon identity to %s mounts (%s ammo names had no identity)",
        written,
        missing,
    )


def warn_invalid_salves(weapon_file: Iterable[Any], logger: Any) -> None:
    """Log weapon managers the public build will reject for empty or zero salves."""
    for weapon_descr in weapon_file:
        if not hasattr(weapon_descr, "v"):
            continue
        if not is_obj_type(weapon_descr.v, "TWeaponManagerModuleDescriptor"):
            continue
        salves = weapon_descr.v.by_m("Salves", False)
        name = getattr(weapon_descr, "namespace", None) or getattr(weapon_descr, "n", "?")
        if salves is None:
            logger.error("%s has no Salves list", name)
            continue
        values: List[int] = []
        for entry in salves.v:
            try:
                values.append(int(str(entry.v)))
            except (TypeError, ValueError):
                logger.error("%s has a non-numeric salvo %r", name, entry.v)
        if not values:
            logger.error("%s has an empty Salves list", name)
            continue
        for value in values:
            if value < 1:
                logger.error("%s has salvo count %s", name, value)
