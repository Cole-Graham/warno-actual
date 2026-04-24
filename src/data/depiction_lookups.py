"""Rename-aware lookups for ``game_db['depiction_data']``.

``depiction_data`` is scraped from the vanilla NDF (see
``src/data/depiction_data.py``), so every map keyed by weapon name
(``all_weapon_meshes``, ``all_fire_effects``, ``animation_weapon_map``,
per-unit ``weapon_subdepictions``) uses the **pre-rename** vanilla
weapon id.

Our ``WeaponDescriptor.equipmentchanges['replace']`` entries (and the
audit / codegen that consume them) reference the **post-rename** weapon
ids declared in
:mod:`src.constants.weapons.vanilla_inst_modifications`. A naive
``mapping[post_rename]`` lookup therefore misses every depiction-data
entry for a renamed weapon, which makes:

* the audit conservatively flag pure ammo-rename ``replace`` rows
  as needing depiction edits, and
* the codegen note ``"new mesh ... not in depiction_data.all_weapon_meshes"``
  even when the same mesh exists under the vanilla key.

This module exposes a tiny ``lookup`` helper that tries the literal
weapon name first and falls back to its vanilla equivalent.
"""

from __future__ import annotations

from typing import Any, Dict, Mapping, Optional

from src.constants.weapons.vanilla_inst_modifications import MERGED_RENAMES

_RENAMED_TO_VANILLA: Dict[str, str] = {new: old for old, new in MERGED_RENAMES}
_VANILLA_TO_RENAMED: Dict[str, str] = {old: new for old, new in MERGED_RENAMES}


def vanilla_name(weapon: str) -> str:
    """Return the pre-rename / vanilla form of ``weapon``.

    If ``weapon`` is not a known post-rename id it is returned unchanged.
    """
    return _RENAMED_TO_VANILLA.get(weapon, weapon)


def renamed_name(weapon: str) -> str:
    """Return the post-rename form of ``weapon``.

    If ``weapon`` is not a known vanilla id it is returned unchanged.
    """
    return _VANILLA_TO_RENAMED.get(weapon, weapon)


def lookup(mapping: Mapping[str, Any], weapon: str) -> Optional[Any]:
    """Look up ``weapon`` in ``mapping`` with a rename-aware fallback.

    Returns ``mapping[weapon]`` when present, else ``mapping[vanilla_name(weapon)]``
    when the vanilla form is present, else ``None``.
    """
    if weapon in mapping:
        return mapping[weapon]
    vanilla = _RENAMED_TO_VANILLA.get(weapon)
    if vanilla is not None and vanilla in mapping:
        return mapping[vanilla]
    return None


def same_vanilla(a: str, b: str) -> bool:
    """True when ``a`` and ``b`` collapse to the same vanilla weapon id."""
    return vanilla_name(a) == vanilla_name(b)
