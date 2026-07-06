"""Build VETERANCY_BONUSES and VETERANCY_EFFECT_CHANGES from level definitions."""

from __future__ import annotations

from typing import Any

from src.constants.effects.veterancy._schema import LevelBonuses, PackConfig
from src.constants.effects.veterancy.effect_packs import (
    EFFECT_PACK_BY_PACK_TYPE,
    RUNTIME_CREATED_EFFECT_PACKS,
)
from src.constants.effects.veterancy.levels import EXTRA_LEVEL_ENTRIES, PACK_CONFIGS, PACK_LEVELS
from src.constants.effects.veterancy.ui_text import build_veterancy_ui_bodies

SUPPRESS_DAMAGE_TYPE = "EDamageType/Suppress"
PHYSICAL_DAMAGE_TYPE = "EDamageType/Physical"
DISPERSION_DESCRIPTOR = "TUnitEffectIncreaseWeaponDispersionMaxRangeDescriptor"

# Effect packs referenced by multiple experience packs — only the owner may patch them.
SHARED_EFFECT_PACK_OWNERS: dict[str, str] = {
    "UnitEffect_xp_rookie": "simple_v3",
}


def _reduction_to_multiplier(reduction_pct: int) -> float:
    return round(1.0 - reduction_pct / 100.0, 2)


def _accuracy_to_dispersion_multiplier(accuracy_pct: int) -> float:
    return round(1.0 - accuracy_pct / 100.0, 2)


def _effect_pack_for_level(
    pack_type: str,
    level_index: int,
    level: LevelBonuses,
) -> str | None:
    if level.effect_pack is not None:
        return level.effect_pack
    packs = EFFECT_PACK_BY_PACK_TYPE.get(pack_type)
    if packs is None or level_index >= len(packs):
        return None
    return packs[level_index]


def _level_patches(
    level: LevelBonuses,
    pack_config: PackConfig,
) -> dict[Any, Any]:
    patches: dict[Any, Any] = {}

    if level.stress_recovery is not None:
        patches["TUnitEffectHealOverTimeDescriptor"] = level.stress_recovery

    if level.aim_time_reduction_pct is not None:
        patches["TBonusWeaponAimtimeEffectDescriptor"] = _reduction_to_multiplier(
            level.aim_time_reduction_pct,
        )

    if level.salvo_reload_reduction_pct is not None:
        patches["TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor"] = (
            _reduction_to_multiplier(level.salvo_reload_reduction_pct)
        )

    if level.shot_reload_reduction_pct is not None:
        patches["TUnitEffectAlterWeaponTempsEntreDeuxTirsDescriptor"] = (
            _reduction_to_multiplier(level.shot_reload_reduction_pct)
        )

    accuracy_pct = level.accuracy_pct
    if accuracy_pct is not None:
        if pack_config.uses_dispersion_for_accuracy or level.uses_dispersion_for_accuracy:
            patches[DISPERSION_DESCRIPTOR] = _accuracy_to_dispersion_multiplier(accuracy_pct)
        else:
            patches["TUnitEffectIncreaseWeaponPrecisionArretDescriptor"] = accuracy_pct

    precision_moving = level.precision_moving_pct
    if precision_moving is not None:
        patches["TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor"] = precision_moving
    elif accuracy_pct is not None and pack_config.pack_type == "SF_v2":
        patches["TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor"] = accuracy_pct
    elif accuracy_pct is not None and pack_config.pack_type not in (
        "helico",
        "helico_attack",
        "artillery",
    ):
        if "TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor" not in patches:
            patches["TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor"] = accuracy_pct

    if level.stress_resistance_pct is not None:
        patches[("TUnitEffectIncreaseDamageTakenDescriptor", SUPPRESS_DAMAGE_TYPE)] = (
            -level.stress_resistance_pct
        )

    if level.physical_damage_reduction_pct is not None:
        patches[("TUnitEffectIncreaseDamageTakenDescriptor", PHYSICAL_DAMAGE_TYPE)] = (
            -level.physical_damage_reduction_pct
        )

    if level.movement_speed_pct is not None:
        patches["TUnitEffectIncreaseSpeedDescriptor"] = level.movement_speed_pct

    if level.evasion_pct is not None:
        if level.add_evasion_descriptor:
            patches["add_evasion"] = True
        else:
            patches["TUnitEffectBonusPrecisionWhenTargetedDescriptor"] = -level.evasion_pct
    elif level.add_evasion_descriptor:
        patches["add_evasion"] = True

    return patches


def build_veterancy_bonuses() -> dict[str, dict[str, dict[str, str]]]:
    ui_bodies = build_veterancy_ui_bodies()
    bonuses: dict[str, dict[str, dict[str, str]]] = {}

    for pack_type, levels in PACK_LEVELS.items():
        pack_data: dict[str, dict[str, str]] = {}
        for level in levels:
            pack_data[level.level_key] = {
                "body_token": level.body_token,
                "body": ui_bodies[pack_type][level.level_key],
            }
        bonuses[pack_type] = pack_data

    for pack_type, extra_level in EXTRA_LEVEL_ENTRIES:
        bonuses[pack_type][extra_level.level_key] = {
            "body_token": extra_level.body_token,
            "body": ui_bodies[pack_type][extra_level.level_key],
        }

    return bonuses


def build_veterancy_effect_changes() -> dict[str, dict[Any, Any]]:
    changes: dict[str, dict[Any, Any]] = {}

    patchable_pack_types = (
        "simple_v3",
        "SF_v2",
        "artillery",
        "helico",
        "avion",
    )

    for pack_type in patchable_pack_types:
        levels = PACK_LEVELS[pack_type]
        pack_config = PACK_CONFIGS[pack_type]
        for level_index, level in enumerate(levels):
            effect_pack = _effect_pack_for_level(pack_type, level_index, level)
            if effect_pack is None or effect_pack in RUNTIME_CREATED_EFFECT_PACKS:
                continue
            owner = SHARED_EFFECT_PACK_OWNERS.get(effect_pack)
            if owner is not None and owner != pack_type:
                continue
            patches = _level_patches(level, pack_config)
            if not patches:
                continue
            entry = changes.setdefault(effect_pack, {})
            for key, value in patches.items():
                if key == "add_evasion":
                    entry["add"] = [("evasion", -level.evasion_pct)]
                else:
                    entry[key] = value

    return changes


def build_runtime_effect_changes() -> dict[str, dict[Any, Any]]:
    """Patches for effect packs created during EffetsSurUnite.ndf editing."""
    changes: dict[str, dict[Any, Any]] = {}

    for pack_type, extra_level in EXTRA_LEVEL_ENTRIES:
        if (
            extra_level.effect_pack is None
            or extra_level.effect_pack not in RUNTIME_CREATED_EFFECT_PACKS
        ):
            continue
        pack_config = PACK_CONFIGS[pack_type]
        patches = _level_patches(extra_level, pack_config)
        if not patches:
            continue
        entry = changes.setdefault(extra_level.effect_pack, {})
        for key, value in patches.items():
            if key == "add_evasion":
                entry["add"] = [("evasion", -extra_level.evasion_pct)]
            else:
                entry[key] = value

    return changes


def build_helo_attack_effect_changes() -> dict[str, dict[Any, Any]]:
    """Patches for attack-helo packs created by cloning base helo packs."""
    changes: dict[str, dict[Any, Any]] = {}
    pack_type = "helico_attack"
    levels = PACK_LEVELS[pack_type]
    pack_config = PACK_CONFIGS[pack_type]
    for level_index, level in enumerate(levels):
        effect_pack = _effect_pack_for_level(pack_type, level_index, level)
        if effect_pack is None:
            continue
        patches = _level_patches(level, pack_config)
        if not patches:
            continue
        entry = changes.setdefault(effect_pack, {})
        for key, value in patches.items():
            if key == "add_evasion":
                entry["add"] = [("evasion", -level.evasion_pct)]
            else:
                entry[key] = value
    return changes


SEMANTIC_FIELD_TO_PATCH_KEYS: dict[str, tuple[Any, ...]] = {
    "stress_recovery": ("TUnitEffectHealOverTimeDescriptor",),
    "aim_time_reduction_pct": ("TBonusWeaponAimtimeEffectDescriptor",),
    "salvo_reload_reduction_pct": ("TUnitEffectAlterWeaponTempsEntreDeuxSalvesDescriptor",),
    "shot_reload_reduction_pct": ("TUnitEffectAlterWeaponTempsEntreDeuxTirsDescriptor",),
    "accuracy_pct": (
        "TUnitEffectIncreaseWeaponPrecisionArretDescriptor",
        DISPERSION_DESCRIPTOR,
    ),
    "precision_moving_pct": ("TUnitEffectIncreaseWeaponPrecisionMouvementDescriptor",),
    "stress_resistance_pct": (
        ("TUnitEffectIncreaseDamageTakenDescriptor", SUPPRESS_DAMAGE_TYPE),
    ),
    "physical_damage_reduction_pct": (
        ("TUnitEffectIncreaseDamageTakenDescriptor", PHYSICAL_DAMAGE_TYPE),
    ),
    "movement_speed_pct": ("TUnitEffectIncreaseSpeedDescriptor",),
    "evasion_pct": ("TUnitEffectBonusPrecisionWhenTargetedDescriptor",),
}
