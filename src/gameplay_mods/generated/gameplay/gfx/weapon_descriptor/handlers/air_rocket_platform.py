"""Remount DamageFamily_roquette_ap rockets to plane avion / helo ammo.

Runs after unit_edits so intentional different-salvo remounts are already
applied, then corrects any remaining wrong-platform mounts (including mixed
vanilla loadouts). Registry pairs are same-salvo only; a ``_helo`` suffix is
just the non-avion name. Does not rewrite EffectTag. New units are out of scope.
"""

from typing import Any, Dict

from src.constants.unit_edits.standards import (
    AIR_ROCKET_DAMAGE_FAMILY,
    AIR_ROCKET_PLATFORM_PAIRS,
    build_air_rocket_platform_maps,
)
from src.utils.ndf_utils import is_obj_type, is_valid_turret

_AMMO_PREFIX = "$/GFX/Weapon/Ammo_"


def _extract_ammo_ns(ammo_path: str) -> str:
    if _AMMO_PREFIX in ammo_path:
        return ammo_path.split(_AMMO_PREFIX, 1)[1].strip()
    return ammo_path.strip()


def _resolve_ammo_name(
    ammo_ns: str,
    renames_old_new: Dict[str, str],
    renames_new_old: Dict[str, str],
) -> str:
    """Map vanilla / intermediate names onto registry (post-rename) keys."""
    if ammo_ns in renames_old_new:
        return renames_old_new[ammo_ns]
    if ammo_ns in renames_new_old or ammo_ns in renames_old_new.values():
        return ammo_ns
    return ammo_ns


def _lookup_family(
    ammo_ns: str,
    ammo_props: Dict[str, Any],
    renames_old_new: Dict[str, str],
    renames_new_old: Dict[str, str],
) -> str | None:
    candidates = [ammo_ns]
    if ammo_ns in renames_old_new:
        candidates.append(renames_old_new[ammo_ns])
    if ammo_ns in renames_new_old:
        candidates.append(renames_new_old[ammo_ns])
    for name in candidates:
        fam = ammo_props.get(f"Ammo_{name}", {}).get("Family")
        if fam:
            return fam
    return None


def _unit_platform(unit_info: Dict[str, Any]) -> str | None:
    """Return 'helo', 'plane', or None for ground/other."""
    if unit_info.get("is_helo_unit"):
        return "helo"
    if "airplane_movement" in unit_info:
        return "plane"
    return None


def apply_air_rocket_platform_standard(
    logger: Any,
    source_path: Any,
    game_db: Dict[str, Any],
) -> None:
    """Remount roquette_ap rockets to avion (planes) or non-avion (helos)."""
    unit_db = game_db.get("unit_data", {})
    ammo_db = game_db.get("ammunition", {})
    ammo_props = ammo_db.get("ammo_properties", {})
    renames_old_new = ammo_db.get("renames_old_new", {})
    renames_new_old = ammo_db.get("renames_new_old", {})

    helo_to_avion, avion_to_helo, helo_names, avion_names = build_air_rocket_platform_maps(
        AIR_ROCKET_PLATFORM_PAIRS,
    )
    registered = helo_names | avion_names

    swaps = 0
    warned: set[str] = set()

    for weapon_descr in source_path:
        if not hasattr(weapon_descr, "namespace"):
            continue
        if not weapon_descr.namespace.startswith("WeaponDescriptor_"):
            continue

        unit_name = weapon_descr.namespace.replace("WeaponDescriptor_", "", 1)
        unit_info = unit_db.get(unit_name)
        if not unit_info:
            continue

        platform = _unit_platform(unit_info)
        if platform is None:
            continue

        turret_list_membr = weapon_descr.v.by_m("TurretDescriptorList", False)
        if turret_list_membr is None:
            continue

        for turret in turret_list_membr.v:
            if not is_valid_turret(turret.v):
                continue
            mounted_list = turret.v.by_m("MountedWeaponDescriptorList", False)
            if mounted_list is None:
                continue

            for mount in mounted_list.v:
                if not is_obj_type(mount.v, "TMountedWeaponDescriptor"):
                    continue
                ammo_membr = mount.v.by_m("Ammunition", False)
                if ammo_membr is None:
                    continue

                ammo_ns = _extract_ammo_ns(str(ammo_membr.v))
                family = _lookup_family(
                    ammo_ns, ammo_props, renames_old_new, renames_new_old,
                )
                if family != AIR_ROCKET_DAMAGE_FAMILY:
                    continue

                resolved = _resolve_ammo_name(
                    ammo_ns, renames_old_new, renames_new_old,
                )

                if resolved not in registered:
                    if resolved not in warned:
                        logger.warning(
                            f"(air_rocket_platform) unpaired {platform} mount "
                            f"{unit_name}: {resolved} — add rocket.py clone + "
                            f"AIR_ROCKET_PLATFORM_PAIRS entry",
                        )
                        warned.add(resolved)
                    continue

                target: str | None = None
                if platform == "plane" and resolved in helo_names:
                    target = helo_to_avion.get(resolved)
                elif platform == "helo" and resolved in avion_names:
                    target = avion_to_helo.get(resolved)

                if not target or target == resolved or target == ammo_ns:
                    continue

                ammo_membr.v = f"{_AMMO_PREFIX}{target}"
                swaps += 1
                logger.debug(
                    f"(air_rocket_platform) {unit_name}: {ammo_ns} -> {target}",
                )

    logger.info(f"Air rocket platform remounts applied: {swaps}")
