"""Validate ammunition descriptor shot count vs ammo consumed per salvo."""

from __future__ import annotations

import re
from typing import Any

_ROCKET_AMMO_PREFIXES = ("Ammo_RocketAir", "Ammo_RocketArt", "Ammo_MLRS")


def _parse_int(member: Any) -> int | None:
    if member is None:
        return None
    try:
        return int(float(str(member.v)))
    except (TypeError, ValueError):
        return None


def _base_weapon_namespace(namespace: str) -> str:
    """Strip strength, quantity, and salvo-length suffixes to the base ammo namespace."""
    name = namespace.removeprefix("Ammo_")
    prev = None
    while name != prev:
        prev = name
        name = re.sub(r"_salvolength\d+$", "", name)
        name = re.sub(r"_x\d+$", "", name)
        name = re.sub(r"_strength\d+$", "", name)
    return f"Ammo_{name}"


def _is_rocket_ammo(namespace: str) -> bool:
    base_namespace = _base_weapon_namespace(namespace)
    return base_namespace.startswith(_ROCKET_AMMO_PREFIXES)


def validate_ammunition_consumption(source_path: Any, logger: Any) -> bool:
    """Warn when ``AffichageMunitionParSalve`` does not match total ammo per salvo.

    Expected: ``AffichageMunitionParSalve == ShotsCountPerSalvo * SimultaneousShotsCount``
    (``SimultaneousShotsCount`` defaults to 1 when absent).

    Only applies to ``Ammo_RocketAir*`` and ``Ammo_RocketArt*`` descriptors. Scans every
    matching descriptor in the edited NDF file so post-edit values are checked, including
    standards, clones, and variants not listed in constants. Logs one warning per base
    weapon, not per strength/quantity/salvo variant.

    Returns:
        True if any mismatches were found.
    """
    mismatches_by_base: dict[str, tuple[int, int, int, int]] = {}

    for descr in source_path:
        if not _is_rocket_ammo(descr.n):
            continue

        shots = _parse_int(descr.v.by_m("ShotsCountPerSalvo", False))
        affichage = _parse_int(descr.v.by_m("AffichageMunitionParSalve", False))
        if shots is None or affichage is None:
            continue

        simultaneous = _parse_int(descr.v.by_m("SimultaneousShotsCount", False))
        if simultaneous is None:
            simultaneous = 1

        expected = shots * simultaneous
        if affichage != expected:
            base_namespace = _base_weapon_namespace(descr.n)
            if (
                base_namespace not in mismatches_by_base
                or descr.n == base_namespace
            ):
                mismatches_by_base[base_namespace] = (
                    affichage,
                    expected,
                    shots,
                    simultaneous,
                )

    for base_namespace, (affichage, expected, shots, simultaneous) in sorted(
        mismatches_by_base.items(),
    ):
        logger.warning(
            "%s: AffichageMunitionParSalve=%s but expected %s "
            "(ShotsCountPerSalvo=%s * SimultaneousShotsCount=%s)",
            base_namespace,
            affichage,
            expected,
            shots,
            simultaneous,
        )

    if mismatches_by_base:
        logger.warning(
            "Found %s ammunition consumption mismatch(es). "
            "Set AffichageMunitionParSalve to ShotsCountPerSalvo * SimultaneousShotsCount.",
            len(mismatches_by_base),
        )

    return bool(mismatches_by_base)
