"""Normalization helpers for ``WeaponDescriptor.equipmentchanges.replace`` blocks.

The authored schema is usually a dict keyed by the old weapon's ammo name. Every
entry **must** declare ``new_weapon``, ``swap_fire_effect``, and
``depiction_baked_in``; ``old_new_effect`` is optional.

    "replace": {
        "FM_kbk_AKM": {
            "new_weapon": "FM_Tantal",
            "swap_fire_effect": True,
            "depiction_baked_in": False,
            # Optional - defaults to ("FM_kbk_AKM", "FM_Tantal") when omitted/None
            "old_new_effect": ("FM_kbk_AKM", "FM_Tantal"),
        },
    }

When the donor unit carries the **same** ammo on **multiple** mounts (e.g. two
RPG-7VR turrets) and each mount should become a **different** weapon, keep the
**same dict shape** as unit_edits: the old ammo stays the key, but the value is
an **ordered list** of per-row payloads (same keys as a single mapping). Each
replacement still consumes the next matching mount in turret order:

    "replace": {
        "RocketInf_RPG7VR_64mm": [
            {
                "new_weapon": "SAW_RPK_74_5_56mm",
                "swap_fire_effect": True,
                "depiction_baked_in": False,
                "old_new_effect": ("RocketInf_RPG7VR_64mm", "SAW_RPK_74_5_56mm"),
            },
            {
                "new_weapon": "RocketInf_RPG29_105mm",
                "swap_fire_effect": True,
                "depiction_baked_in": False,
                "old_new_effect": ("RocketInf_RPG7VR_64mm", "RocketInf_RPG29_105mm"),
            },
        ],
    }

``swap_fire_effect`` controls runtime EffectTag rewriting on the matching
mounted weapon's turret salvo. When ``False`` the row is also treated as
a no-op by the depiction audit.

``depiction_baked_in`` is an orthogonal per-row opt-out used for vehicles
/ aircraft whose weapon mesh is part of the hull/turret model rather
than a separate WeaponAlternative. When ``True`` the runtime EffectTag
rewrite still happens (gated by ``swap_fire_effect``), but the depiction
audit treats the row as not requiring a ``depiction_edits/`` file. Every
row must declare this flag explicitly so authors have to think about
whether a depiction edit is needed for each replacement.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Mapping, Optional, cast

from src.utils.logging_utils import setup_logger

logger = setup_logger(__name__)


@dataclass(frozen=True)
class ReplaceSpec:
    """Normalized view of a single weapon replacement entry.

    Attributes:
        old_weapon: The ammo name to replace (donor).
        new_weapon: The ammo name to swap in.
        swap_fire_effect: When ``True`` (default for explicit specs), the
            ``EffectTag`` on the matching mounted weapon is rewritten and the
            depiction audit considers this row as requiring a depiction edit
            (unless ``depiction_baked_in`` is also True).
        old_fire_effect: Fire-effect identifier currently on the mount.
            Defaults to ``old_weapon`` when omitted.
        new_fire_effect: Fire-effect identifier to install. Defaults to
            ``new_weapon`` when omitted.
        depiction_baked_in: When ``True``, this row is exempt from the
            depiction audit because the weapon mesh is part of the
            unit's hull / turret model (no separate WeaponAlternative
            mesh to swap). Runtime EffectTag rewriting still respects
            ``swap_fire_effect`` independently.
    """

    old_weapon: str
    new_weapon: str
    swap_fire_effect: bool
    old_fire_effect: Optional[str]
    new_fire_effect: Optional[str]
    depiction_baked_in: bool


def _spec_from_dict_entry(old_weapon: str, payload: Mapping[str, Any]) -> Optional[ReplaceSpec]:
    """Convert a single ``{old_weapon: {...}}`` entry into a ``ReplaceSpec``."""
    new_weapon = payload.get("new_weapon")
    if not isinstance(new_weapon, str):
        return None
    swap_fire_effect = bool(payload.get("swap_fire_effect", True))
    if "depiction_baked_in" not in payload:
        logger.warning(
            f"equipmentchanges.replace[{old_weapon!r}] is missing the required "
            f"'depiction_baked_in' key; defaulting to False."
        )
    depiction_baked_in = bool(payload.get("depiction_baked_in", False))
    old_new_effect = payload.get("old_new_effect")
    old_fe: Optional[str] = None
    new_fe: Optional[str] = None
    if old_new_effect is not None:
        if isinstance(old_new_effect, (list, tuple)) and len(old_new_effect) == 2:
            old_candidate, new_candidate = old_new_effect
            if isinstance(old_candidate, str):
                old_fe = old_candidate
            if isinstance(new_candidate, str):
                new_fe = new_candidate
    if swap_fire_effect:
        if old_fe is None:
            old_fe = old_weapon
        if new_fe is None:
            new_fe = new_weapon
    return ReplaceSpec(
        old_weapon=old_weapon,
        new_weapon=new_weapon,
        swap_fire_effect=swap_fire_effect,
        old_fire_effect=old_fe,
        new_fire_effect=new_fe,
        depiction_baked_in=depiction_baked_in,
    )


def normalize_replace(replace_block: Any) -> List[ReplaceSpec]:
    """Return a uniform ``List[ReplaceSpec]`` from a ``replace`` block.

    Accepts dict form only:

    * ``{old_weapon: {"new_weapon": ..., ...}}`` — one replacement for that
      donor ammo.
    * ``{old_weapon: [{...}, {...}, ...]}`` — same donor ammo on multiple
      mounts; list order is the order of ``ReplaceSpec``s (next mount per row).

    ``None`` or empty input yields ``[]``. Unsupported types log a warning and
    yield ``[]``.
    """
    if not replace_block:
        return []
    if not isinstance(replace_block, dict):
        logger.warning(
            "equipmentchanges.replace must be a dict {old_weapon: payload | [payloads]}; "
            f"got {type(replace_block).__name__}.",
        )
        return []

    specs: List[ReplaceSpec] = []
    for old_weapon, payload in replace_block.items():
        if not isinstance(old_weapon, str):
            continue
        if isinstance(payload, list):
            for index, item in enumerate(payload):
                if not isinstance(item, Mapping):
                    logger.warning(
                        f"equipmentchanges.replace[{old_weapon!r}] list entry {index} "
                        f"must be a mapping; got {type(item).__name__}.",
                    )
                    continue
                spec = _spec_from_dict_entry(old_weapon, cast(Mapping[str, Any], item))
                if spec is not None:
                    specs.append(spec)
        elif isinstance(payload, Mapping):
            spec = _spec_from_dict_entry(old_weapon, payload)
            if spec is not None:
                specs.append(spec)
        else:
            logger.warning(
                f"equipmentchanges.replace[{old_weapon!r}] must be a mapping or list "
                f"of mappings; got {type(payload).__name__}.",
            )
    return specs
