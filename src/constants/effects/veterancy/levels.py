"""Per-pack veterancy level definitions (mod-intended values)."""

from __future__ import annotations

from src.constants.effects.veterancy._schema import LevelBonuses, PackConfig

SIMPLE_V3_LEVELS: tuple[LevelBonuses, ...] = (
    LevelBonuses(
        body_token="SGZVNLTRKE",
        level_key="simple_v3_0",
        stress_recovery=3.0,
    ),
    LevelBonuses(
        body_token="UGNZEELGTC",
        level_key="simple_v3_1",
        stress_recovery=4.0,
        accuracy_pct=5,
        aim_time_reduction_pct=4,
        salvo_reload_reduction_pct=10,
        stress_resistance_pct=14,
    ),
    LevelBonuses(
        body_token="KUJQCFUCWY",
        level_key="simple_v3_2",
        stress_recovery=4.8,
        accuracy_pct=10,
        aim_time_reduction_pct=8,
        salvo_reload_reduction_pct=17,
        stress_resistance_pct=22,
    ),
    LevelBonuses(
        body_token="SZISEJDYHF",
        level_key="simple_v3_3",
        stress_recovery=5.4,
        accuracy_pct=15,
        aim_time_reduction_pct=12,
        salvo_reload_reduction_pct=24,
        stress_resistance_pct=32,
    ),
)

SIMPLE_V3_MULTIPLICATIVE_LEVELS: tuple[LevelBonuses, ...] = tuple(
    LevelBonuses(
        body_token=token,
        level_key=key,
        stress_recovery=level.stress_recovery,
        accuracy_pct=level.accuracy_pct,
        aim_time_reduction_pct=level.aim_time_reduction_pct,
        salvo_reload_reduction_pct=level.salvo_reload_reduction_pct,
        stress_resistance_pct=level.stress_resistance_pct,
    )
    for level, (token, key) in zip(
        SIMPLE_V3_LEVELS,
        (
            ("YBXGZUCPGW", "simple_v3_multiplicative_0"),
            ("OZELGDYCJI", "simple_v3_multiplicative_1"),
            ("KODCDSFEDT", "simple_v3_multiplicative_2"),
            ("GQBPUEGUYF", "simple_v3_multiplicative_3"),
        ),
    )
)

SF_V2_LEVELS: tuple[LevelBonuses, ...] = (
    LevelBonuses(
        body_token="FSDWIVSTQO",
        level_key="SF_v2_0",
        stress_recovery=3.0,
    ),
    LevelBonuses(
        body_token="BTMBWVRSDH",
        level_key="SF_v2_1",
        stress_recovery=6.0,
        movement_speed_pct=10,
        accuracy_pct=20,
        aim_time_reduction_pct=30,
        salvo_reload_reduction_pct=30,
        stress_resistance_pct=30,
        physical_damage_reduction_pct=30,
    ),
    LevelBonuses(
        body_token="JHQIIEVPZF",
        level_key="SF_v2_2",
        stress_recovery=7.8,
        movement_speed_pct=20,
        accuracy_pct=30,
        aim_time_reduction_pct=40,
        salvo_reload_reduction_pct=40,
        stress_resistance_pct=40,
        physical_damage_reduction_pct=30,
    ),
    LevelBonuses(
        body_token="ZIUCSNONPU",
        level_key="SF_v2_3",
        stress_recovery=9.6,
        movement_speed_pct=30,
        accuracy_pct=40,
        aim_time_reduction_pct=50,
        salvo_reload_reduction_pct=50,
        stress_resistance_pct=50,
        physical_damage_reduction_pct=30,
    ),
)

SF_V2_MULTIPLICATIVE_LEVELS: tuple[LevelBonuses, ...] = tuple(
    LevelBonuses(
        body_token=token,
        level_key=key,
        stress_recovery=level.stress_recovery,
        movement_speed_pct=level.movement_speed_pct,
        accuracy_pct=level.accuracy_pct,
        aim_time_reduction_pct=level.aim_time_reduction_pct,
        salvo_reload_reduction_pct=level.salvo_reload_reduction_pct,
        stress_resistance_pct=level.stress_resistance_pct,
        physical_damage_reduction_pct=level.physical_damage_reduction_pct,
    )
    for level, (token, key) in zip(
        SF_V2_LEVELS,
        (
            ("OIKXZUZCBK", "SF_v2_multiplicative_0"),
            ("OPCTRVJHFT", "SF_v2_multiplicative_1"),
            ("KMDMZPBWMO", "SF_v2_multiplicative_2"),
            ("UOHDGZDXIE", "SF_v2_multiplicative_3"),
        ),
    )
)

ARTILLERY_LEVELS: tuple[LevelBonuses, ...] = (
    LevelBonuses(
        body_token="NWAXFLCAIU",
        level_key="artillery_0",
        stress_recovery=3.0,
        uses_dispersion_for_accuracy=True,
    ),
    LevelBonuses(
        body_token="SZTBFODBVW",
        level_key="artillery_1",
        stress_recovery=3.0,
        accuracy_pct=6,
        aim_time_reduction_pct=15,
        salvo_reload_reduction_pct=20,
        stress_resistance_pct=6,
        uses_dispersion_for_accuracy=True,
    ),
    LevelBonuses(
        body_token="YZGZLNRVWU",
        level_key="artillery_2",
        stress_recovery=3.8,
        accuracy_pct=12,
        aim_time_reduction_pct=30,
        salvo_reload_reduction_pct=40,
        stress_resistance_pct=12,
        uses_dispersion_for_accuracy=True,
    ),
    LevelBonuses(
        body_token="UQNUCMTWOZ",
        level_key="artillery_3",
        stress_recovery=4.6,
        accuracy_pct=16,
        aim_time_reduction_pct=45,
        salvo_reload_reduction_pct=60,
        stress_resistance_pct=24,
        uses_dispersion_for_accuracy=True,
    ),
)

HELICO_LEVELS: tuple[LevelBonuses, ...] = (
    LevelBonuses(
        body_token="CCPVCWPZKZ",
        level_key="helico_0",
        stress_recovery=3.0,
    ),
    LevelBonuses(
        body_token="NSWPFSVOYP",
        level_key="helico_1",
        stress_recovery=4.2,
        aim_time_reduction_pct=20,
    ),
    LevelBonuses(
        body_token="ETUVQWYSIR",
        level_key="helico_2",
        stress_recovery=6.2,
        accuracy_pct=5,
        aim_time_reduction_pct=40,
        stress_resistance_pct=20,
    ),
    LevelBonuses(
        body_token="BQBYGPLFJC",
        level_key="helico_3",
        stress_recovery=8.4,
        accuracy_pct=10,
        aim_time_reduction_pct=60,
        stress_resistance_pct=20,
        evasion_pct=5,
        add_evasion_descriptor=True,
    ),
)

HELICO_SF_LEVEL: LevelBonuses = LevelBonuses(
    body_token="ZLYYYBJDXI",
    level_key="helico_SF_3",
    effect_pack="UnitEffect_xp_elite_helo_SF",
    stress_recovery=7.8,
    movement_speed_pct=30,
    accuracy_pct=16,
    aim_time_reduction_pct=30,
    salvo_reload_reduction_pct=30,
    stress_resistance_pct=40,
    evasion_pct=5,
    add_evasion_descriptor=True,
)

HELICO_ATTACK_LEVELS: tuple[LevelBonuses, ...] = (
    LevelBonuses(
        body_token="QJYUDDORXU",
        level_key="helico_attack_0",
        stress_recovery=3.0,
    ),
    LevelBonuses(
        body_token="LSCFSBJBIV",
        level_key="helico_attack_1",
        stress_recovery=4.2,
        aim_time_reduction_pct=20,
    ),
    LevelBonuses(
        body_token="JFVVMTZTDB",
        level_key="helico_attack_2",
        stress_recovery=6.2,
        accuracy_pct=8,
        aim_time_reduction_pct=40,
        stress_resistance_pct=20,
    ),
    LevelBonuses(
        body_token="MPHFFBYNXE",
        level_key="helico_attack_3",
        stress_recovery=8.4,
        accuracy_pct=16,
        aim_time_reduction_pct=60,
        stress_resistance_pct=40,
        evasion_pct=5,
        add_evasion_descriptor=True,
    ),
)

# Flip to False to restore legacy veteran/elite avion bonuses (+4/+8 accuracy, +4/+8 evasion, evasion UI lines).
AVION_VET_REBALANCE_ENABLED = True

_AVION_VET_LEGACY_PRECISION = (4, 8)  # veteran, elite — moving precision ("accuracy")
_AVION_VET_REBALANCE_PRECISION = (9, 18)
_AVION_VET_LEGACY_EVASION = (4, 8)  # veteran, elite; None when rebalanced

_vet_precision = (
    _AVION_VET_REBALANCE_PRECISION if AVION_VET_REBALANCE_ENABLED else _AVION_VET_LEGACY_PRECISION
)
_vet_evasion: tuple[int | None, int | None] = (
    (None, None) if AVION_VET_REBALANCE_ENABLED else _AVION_VET_LEGACY_EVASION
)

AVION_LEVELS: tuple[LevelBonuses, ...] = (
    LevelBonuses(
        body_token="LNZBFCYAIE",
        level_key="avion_0",
    ),
    LevelBonuses(
        body_token="NMDXSJVEMU",
        level_key="avion_1",
        stress_recovery=2.0,
    ),
    LevelBonuses(
        body_token="ZCKHBWOUCJ",
        level_key="avion_2",
        stress_recovery=4.2,
        precision_moving_pct=_vet_precision[0],
        aim_time_reduction_pct=10,
        stress_resistance_pct=20,
        evasion_pct=_vet_evasion[0],
    ),
    LevelBonuses(
        body_token="KRMIXGZVQU",
        level_key="avion_3",
        stress_recovery=6.2,
        precision_moving_pct=_vet_precision[1],
        aim_time_reduction_pct=20,
        stress_resistance_pct=40,
        evasion_pct=_vet_evasion[1],
    ),
)

PACK_CONFIGS: dict[str, PackConfig] = {
    "simple_v3": PackConfig(pack_type="simple_v3", level_format="simple_v3_{level}"),
    "simple_v3_multiplicative": PackConfig(
        pack_type="simple_v3_multiplicative",
        level_format="simple_v3_multiplicative_{level}",
        modifier_mode="multiplicative",
    ),
    "SF_v2": PackConfig(
        pack_type="SF_v2",
        level_format="SF_v2_{level}",
    ),
    "SF_v2_multiplicative": PackConfig(
        pack_type="SF_v2_multiplicative",
        level_format="SF_v2_multiplicative_{level}",
        modifier_mode="multiplicative",
    ),
    "artillery": PackConfig(
        pack_type="artillery",
        level_format="artillery_{level}",
        uses_dispersion_for_accuracy=True,
    ),
    "helico": PackConfig(
        pack_type="helico",
        level_format="helico_{level}",
    ),
    "helico_attack": PackConfig(
        pack_type="helico_attack",
        level_format="helico_attack_{level}",
    ),
    "avion": PackConfig(
        pack_type="avion",
        level_format="avion_{level}",
    ),
}

PACK_LEVELS: dict[str, tuple[LevelBonuses, ...]] = {
    "simple_v3": SIMPLE_V3_LEVELS,
    "simple_v3_multiplicative": SIMPLE_V3_MULTIPLICATIVE_LEVELS,
    "SF_v2": SF_V2_LEVELS,
    "SF_v2_multiplicative": SF_V2_MULTIPLICATIVE_LEVELS,
    "artillery": ARTILLERY_LEVELS,
    "helico": HELICO_LEVELS,
    "helico_attack": HELICO_ATTACK_LEVELS,
    "avion": AVION_LEVELS,
}

EXTRA_LEVEL_ENTRIES: tuple[tuple[str, LevelBonuses], ...] = (
    ("helico", HELICO_SF_LEVEL),
)
