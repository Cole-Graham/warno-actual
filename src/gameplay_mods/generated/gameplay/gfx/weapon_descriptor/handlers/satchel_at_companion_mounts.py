"""Auto-wire ``Grenade_Satchel_Charge_AT`` beside ``Grenade_Satchel_Charge``.

Runs as the final step of ``edit_gen_gp_gfx_weapondescriptor`` (after vanilla
renames, new units, unit edits, default salves, namespace ammo quantity updates,
and HE DCA air mounts) so the live NDF reflects every prior change. For each
``TMountedWeaponDescriptor`` carrying ``Grenade_Satchel_Charge``, we clone the
mount and swap the clone's ``Ammunition`` pointer to ``Grenade_Satchel_Charge_AT``.

Idempotent: a re-run skips any turret that already carries the AT companion.
"""

import re
from typing import Any, Dict

from src.utils.ndf_utils import is_obj_type, is_valid_turret

_AMMO_PREFIX = "$/GFX/Weapon/Ammo_"
_SUFFIX_RE = re.compile(r"(?:_strength\d+)?(?:_x\d+|_salvolength\d+)?$")

_SATCHEL_DONOR = "Grenade_Satchel_Charge"
_SATCHEL_COMPANION = "Grenade_Satchel_Charge_AT"


def _extract_ammo_namespace(weapon: Any) -> str | None:
    """Return the ammo namespace (without ``Ammo_`` prefix) or ``None``."""
    ammunition_membr = weapon.v.by_m("Ammunition", False)
    if ammunition_membr is None:
        return None
    raw = str(ammunition_membr.v)
    if _AMMO_PREFIX not in raw:
        return None
    return raw.split(_AMMO_PREFIX, 1)[1].strip()


def _base_ammo_name(ammo_ns: str) -> str:
    return _SUFFIX_RE.sub("", ammo_ns)


def apply_satchel_at_companion_mounts(
    source_path: Any,
    logger: Any,
    game_db: Dict[str, Any],
) -> None:
    """Clone each satchel mount to ``Grenade_Satchel_Charge_AT`` on the same turret."""
    added = 0
    skipped_existing = 0

    for weapon_descr in source_path:
        turret_list_membr = weapon_descr.v.by_m("TurretDescriptorList", False)
        if turret_list_membr is None:
            continue

        for turret in turret_list_membr.v:
            if not is_valid_turret(turret.v):
                continue

            mounted_list_membr = turret.v.by_m("MountedWeaponDescriptorList", False)
            if mounted_list_membr is None:
                continue

            mounts = list(mounted_list_membr.v)
            existing_bases = set()
            donor_mounts = []
            for mount in mounts:
                if not is_obj_type(mount.v, "TMountedWeaponDescriptor"):
                    continue
                ammo_ns = _extract_ammo_namespace(mount)
                if ammo_ns is None:
                    continue
                base = _base_ammo_name(ammo_ns)
                existing_bases.add(base)
                if base == _SATCHEL_DONOR:
                    donor_mounts.append(mount)

            for mount in donor_mounts:
                if _SATCHEL_COMPANION in existing_bases:
                    skipped_existing += 1
                    continue

                new_mount = mount.copy()
                new_mount.v.by_m("Ammunition").v = f"{_AMMO_PREFIX}{_SATCHEL_COMPANION}"
                mounted_list_membr.v.add(new_mount)
                existing_bases.add(_SATCHEL_COMPANION)
                added += 1
                logger.debug(
                    f"(satchel_at) {weapon_descr.namespace}: added companion mount "
                    f"-> Ammo_{_SATCHEL_COMPANION}"
                )

    logger.info(
        f"(satchel_at) added {added} companion mounts "
        f"(skipped {skipped_existing} existing)"
    )
