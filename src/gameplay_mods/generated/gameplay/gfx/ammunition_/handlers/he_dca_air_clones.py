"""Auto-generate ``Ammo_<base>_AIR`` clones for every ``DamageFamily_he_dca`` weapon.

Runs as the final step of ``edit_gen_gp_gfx_ammunition`` (after standards,
per-weapon edits and ``apply_damage_families``) so the cloned descriptor
inherits every prior edit. Skips weapons excluded from the precomputed
``he_dca_weapons`` map (air-only DCA with ``MaximumRangeGRU == 0``; those get
``_AIR``-equivalent edits in ``autocanon_dca.py`` instead). The clone:

- Carries ``DamageFamily_he_dca_airtargets`` (registered in
  ``DamageResistance*.ndf``; ignored by every non-aerial resistance family via
  ``BlindagesToIgnoreForDamageFamilies`` in ``WeaponConstantes.ndf``).
- Uses ``SuppressDamages = round(W * ratio)`` (default ratio ``2/3``, optional
  per-weapon overrides) so the airplane stun pack threshold (``r * Mt = 175``
  written suppress, with ``Mt = 250``) lines up with each SPAAG's vanilla
  suppress-stun timing -- without affecting ground performance, since the
  original ammo retains ``DamageFamily_he_dca`` and its full ``SuppressDamages``.

Idempotent: a re-run skips any weapon whose ``Ammo_<base>_AIR`` clone already
exists in the source path.
"""

import re
from typing import Any, Dict
from uuid import uuid4

from src.constants.weapons.spaag_air import (
    SPAAG_AIR_AIMING_TIME,
    SPAAG_AIR_DAMAGE_FAMILY,
    SPAAG_AIR_W_RATIO_DEFAULT,
    SPAAG_AIR_W_RATIO_OVERRIDES,
)


_HE_DCA_AIR_FAMILY = SPAAG_AIR_DAMAGE_FAMILY
_SALVO_SUFFIX_RE = re.compile(r"(_x\d+|_salvolength\d+)$")


def _parse_int_suppress(value: Any) -> int | None:
    """Parse the post-edit ``SuppressDamages`` string into an int (None on failure)."""
    try:
        s = str(value).strip()
        if "." in s:
            return int(round(float(s)))
        return int(s)
    except (TypeError, ValueError):
        return None


def apply_he_dca_air_ammo_clones(
    source_path: Any,
    logger: Any,
    game_db: Dict[str, Any],
) -> None:
    """Clone every ``DamageFamily_he_dca`` ammo into a sibling ``_AIR`` variant.

    Uses the precomputed ``he_dca_weapons`` map (see
    ``build_he_dca_weapons``) to decide which descriptors to clone. Skips any
    descriptor whose ``_AIR`` sibling already exists so a re-run is a no-op.
    """
    he_dca_weapons = game_db.get("ammunition", {}).get("he_dca_weapons", {})
    if not he_dca_weapons:
        logger.info(
            "(he_dca_air) precomputed he_dca_weapons map is empty; "
            "no air ammo clones will be generated"
        )
        return

    cloned = 0
    skipped_existing = 0
    skipped_no_suppress = 0

    descriptors = list(source_path)
    for descr in descriptors:
        ns = getattr(descr, "namespace", None)
        if not ns or not ns.startswith("Ammo_"):
            continue
        if ns.endswith("_AIR"):
            continue

        base_with_suffix = ns[len("Ammo_"):]
        base = _SALVO_SUFFIX_RE.sub("", base_with_suffix)
        if base not in he_dca_weapons:
            continue

        air_namespace = f"Ammo_{base_with_suffix}_AIR"
        if source_path.by_n(air_namespace, strict=False) is not None:
            skipped_existing += 1
            continue

        suppress_membr = descr.v.by_m("SuppressDamages", False)
        if suppress_membr is None:
            logger.warning(
                f"(he_dca_air) {ns}: missing SuppressDamages, skipping clone"
            )
            skipped_no_suppress += 1
            continue
        w_value = _parse_int_suppress(suppress_membr.v)
        if w_value is None:
            logger.warning(
                f"(he_dca_air) {ns}: could not parse SuppressDamages "
                f"{suppress_membr.v!r}, skipping clone"
            )
            skipped_no_suppress += 1
            continue

        ratio = SPAAG_AIR_W_RATIO_OVERRIDES.get(base, SPAAG_AIR_W_RATIO_DEFAULT)
        w_air = max(1, int(round(w_value * ratio)))

        air_descr = descr.copy()
        air_descr.namespace = air_namespace
        air_descr.v.by_m("DescriptorId").v = f"GUID:{{{uuid4()}}}"
        air_descr.v.by_m("Arme").v.by_m("Family").v = _HE_DCA_AIR_FAMILY
        air_descr.v.by_m("SuppressDamages").v = str(w_air)
        air_descr.v.by_m("AimingTime").v = str(SPAAG_AIR_AIMING_TIME)
        source_path.add(air_descr)

        cloned += 1
        logger.info(
            f"(he_dca_air) cloned {ns} -> {air_namespace} "
            f"(W={w_value}, ratio={ratio:.4f}, W_AIR={w_air})"
        )

    logger.info(
        f"(he_dca_air) generated {cloned} air ammo clones "
        f"(skipped {skipped_existing} existing, {skipped_no_suppress} without parsable SuppressDamages)"
    )
